#!/usr/bin/env python3
"""说话人分离(pyannote speaker-diarization-3.1)+ 与 Whisper 段落按时间重叠对齐。
读取 transcripts/<id>.json + yc_video/audio/<id>.m4a,产出:
  transcripts/<id>.speaker.json  —— 每个段落带 speaker 标签
  transcripts/<id>.speaker.txt   —— 合并同一说话人的连续段落,便于阅读/做笔记
已存在 <id>.speaker.json 的跳过 => 可断点续跑。

HF token 优先读环境变量 HF_TOKEN,否则读 scripts/.hf_token。
需先在 huggingface.co 接受以下 gated 模型条款:
  pyannote/speaker-diarization-3.1  与  pyannote/segmentation-3.0
"""
import os, sys, json, glob, subprocess, tempfile, wave

AUDIO_DIR = "yc_video/audio"
OUT_DIR   = "transcripts"


def get_token() -> str:
    tok = os.environ.get("HF_TOKEN", "").strip()
    if tok:
        return tok
    p = os.path.join(os.path.dirname(__file__), ".hf_token")
    if os.path.exists(p):
        return open(p).read().strip()
    sys.exit("找不到 HF token(设置 HF_TOKEN 或写入 scripts/.hf_token)")


def load_waveform(src: str):
    """m4a -> 16k mono s16 wav(临时) -> (waveform[1,T] float32 tensor, 16000)。
    直接把内存波形交给 pyannote,绕开 pyannote 4.x 依赖的 torchcodec(与 torch 2.4.1 不兼容)。"""
    import numpy as np, torch
    fd, wav = tempfile.mkstemp(suffix=".wav"); os.close(fd)
    try:
        subprocess.run(["ffmpeg", "-y", "-i", src, "-ac", "1", "-ar", "16000",
                        "-c:a", "pcm_s16le", wav],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with wave.open(wav, "rb") as w:
            sr, ch, n = w.getframerate(), w.getnchannels(), w.getnframes()
            raw = w.readframes(n)
    finally:
        os.remove(wav)
    arr = (np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0)
    arr = arr.reshape(-1, ch).T  # (channel, time)
    return torch.from_numpy(arr.copy()), sr


def assign_speakers(segs, turns):
    """给每个 whisper 段落分配重叠时间最长的说话人。"""
    for s in segs:
        best, best_ov = "SPEAKER_?", 0.0
        for (t0, t1, spk) in turns:
            ov = max(0.0, min(s["end"], t1) - max(s["start"], t0))
            if ov > best_ov:
                best_ov, best = ov, spk
        s["speaker"] = best
    return segs


def write_speaker_txt(path, segs):
    """合并连续同说话人段落成段。"""
    lines, cur_spk, buf, start = [], None, [], None
    def flush():
        if buf:
            mm = f"{int(start//60):02d}:{int(start%60):02d}"
            lines.append(f"[{mm}] {cur_spk}: " + " ".join(buf))
    for s in segs:
        if s["speaker"] != cur_spk:
            flush(); cur_spk, buf, start = s["speaker"], [s["text"]], s["start"]
        else:
            buf.append(s["text"])
    flush()
    open(path, "w", encoding="utf-8").write("\n\n".join(lines))


def main():
    import torch
    from pyannote.audio import Pipeline
    token = get_token()
    print("loading pyannote/speaker-diarization-3.1 ...", flush=True)
    model_id = "pyannote/speaker-diarization-3.1"
    try:
        # pyannote.audio >= 4.x 用 token=;3.x 用 use_auth_token=
        try:
            pipeline = Pipeline.from_pretrained(model_id, token=token)
        except TypeError:
            pipeline = Pipeline.from_pretrained(model_id, use_auth_token=token)
    except Exception as e:
        sys.exit(f"加载 pyannote 失败(检查 token / 是否已接受 gated 模型条款):{e!r}")
    if torch.cuda.is_available():
        pipeline.to(torch.device("cuda")); print("pyannote on CUDA")

    jsons = sorted(glob.glob(os.path.join(OUT_DIR, "*.json")))
    jsons = [j for j in jsons if not j.endswith(".speaker.json")]
    print(f"{len(jsons)} transcripts to diarize")
    for i, jp in enumerate(jsons, 1):
        vid = os.path.splitext(os.path.basename(jp))[0]
        out = os.path.join(OUT_DIR, vid + ".speaker.json")
        if os.path.exists(out):
            print(f"[{i}/{len(jsons)}] skip {vid} (done)"); continue
        audio = os.path.join(AUDIO_DIR, vid + ".m4a")
        if not os.path.exists(audio):
            print(f"[{i}/{len(jsons)}] no audio for {vid}, skip"); continue
        print(f"[{i}/{len(jsons)}] diarizing {vid} ...", flush=True)
        data = json.load(open(jp, encoding="utf-8"))
        waveform, sr = load_waveform(audio)
        result = pipeline({"waveform": waveform, "sample_rate": sr})
        # pyannote 4.x 返回 DiarizeOutput(.speaker_diarization 为 Annotation);3.x 直接返回 Annotation
        dia = getattr(result, "speaker_diarization", result)
        turns = [(t.start, t.end, spk) for t, _, spk in dia.itertracks(yield_label=True)]
        n_spk = len({spk for _, _, spk in turns})
        data["segments"] = assign_speakers(data["segments"], turns)
        data["num_speakers"] = n_spk
        json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        write_speaker_txt(os.path.join(OUT_DIR, vid + ".speaker.txt"), data["segments"])
        print(f"    done: {n_spk} speakers")


if __name__ == "__main__":
    main()
