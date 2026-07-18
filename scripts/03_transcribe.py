#!/usr/bin/env python3
"""本地 Whisper 批量转写(faster-whisper large-v3 / CUDA / fp16)。
遍历 yc_video/audio/*.m4a,输出 transcripts/<id>.json(带时间戳段落)+ .txt + .srt。
已存在 <id>.json 的跳过 => 可断点续跑。"""
import os, sys, json, glob, time

AUDIO_DIR = "yc_video/audio"
OUT_DIR   = "transcripts"
MODEL     = os.environ.get("WHISPER_MODEL", "large-v3")
# --watch:边下边转,处理完当前文件后轮询新文件,直到出现下载完成哨兵且无待处理
WATCH     = "--watch" in sys.argv
SENTINEL  = "yc_video/.download_done"


def srt_ts(t: float) -> str:
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    from faster_whisper import WhisperModel
    try:
        model = WhisperModel(MODEL, device="cuda", compute_type="float16")
        print(f"loaded {MODEL} on CUDA/fp16")
    except Exception as e:
        print(f"CUDA load failed ({e!r}); falling back to CPU/int8", file=sys.stderr)
        model = WhisperModel(MODEL, device="cpu", compute_type="int8")

    def pending():
        return [a for a in sorted(glob.glob(os.path.join(AUDIO_DIR, "*.m4a")))
                if not os.path.exists(os.path.join(OUT_DIR,
                    os.path.splitext(os.path.basename(a))[0] + ".json"))]

    done_count = 0
    while True:
        todo = pending()
        for ap in todo:
            vid = os.path.splitext(os.path.basename(ap))[0]
            jpath = os.path.join(OUT_DIR, vid + ".json")
            if os.path.exists(jpath):
                continue
            done_count += 1
            print(f"[{done_count}] transcribing {vid} ...", flush=True)
            segments, info = model.transcribe(
                ap, language="en", vad_filter=True, beam_size=5,
                vad_parameters=dict(min_silence_duration_ms=500),
            )
            segs, srt_lines, txt_parts = [], [], []
            for k, seg in enumerate(segments, 1):
                text = seg.text.strip()
                segs.append({"start": round(seg.start, 3), "end": round(seg.end, 3), "text": text})
                srt_lines.append(f"{k}\n{srt_ts(seg.start)} --> {srt_ts(seg.end)}\n{text}\n")
                txt_parts.append(text)
            tmp = jpath + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump({"id": vid, "language": info.language,
                           "duration": round(info.duration, 1), "segments": segs},
                          f, ensure_ascii=False, indent=1)
            os.replace(tmp, jpath)  # 原子写,避免半成品被 diarize 读到
            with open(os.path.join(OUT_DIR, vid + ".srt"), "w", encoding="utf-8") as f:
                f.write("\n".join(srt_lines))
            with open(os.path.join(OUT_DIR, vid + ".txt"), "w", encoding="utf-8") as f:
                f.write(" ".join(txt_parts))
            print(f"    done: {len(segs)} segments, {info.duration:.0f}s audio", flush=True)
        if not WATCH:
            break
        if os.path.exists(SENTINEL) and not pending():
            print("download finished and all transcribed -> exit watch", flush=True)
            break
        time.sleep(15)


if __name__ == "__main__":
    main()
