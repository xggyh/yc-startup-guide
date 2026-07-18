# YC 创业教程流水线(YC → 音频 → 转写 → 双语笔记 → 主题手册)

把 Y Combinator YouTube 近期视频**只下音频**到本地,用 **RTX 4090 上的 Whisper** 转写、
**pyannote** 做说话人分离,产出一套面向 **AI Agent 方向创始人**的双语创业教程:
- `notes/` —— 逐视频双语笔记(中文 TL;DR + 英文金句 + 中文小结 + 行动项)
- `handbook/` —— 跨视频综合的中英双语主题手册

## 环境
- GPU: RTX 4090 24GB;`ffmpeg` 已装;Python 3.10 (anaconda base)。
- 依赖:`pip install -U yt-dlp faster-whisper pyannote.audio`(见 `scripts/requirements.txt`)。

## 运行步骤
```bash
# 1) 生成待下载清单(可调:MAX_TOTAL / MIN_DUR / MAX_DUR)
bash scripts/01_build_list.sh          # -> video_list.md / video_list.txt

# 2) 只下音频 + 字幕 + 元数据(可重复运行,断点续跑)
bash scripts/02_download.sh

# 3) Whisper 转写 -> transcripts/<id>.{json,txt,srt}
python scripts/03_transcribe.py

# 4) 说话人分离 -> transcripts/<id>.speaker.{json,txt}
#    需 HF token(scripts/.hf_token,已 chmod 600)且已接受 pyannote gated 模型条款
python scripts/04_diarize.py

# 5) 逐视频双语笔记 + 6) 主题手册:由 Claude 通过 Workflow 并行生成
```

## 目录
```
yc_video/audio|subs|metadata   # 音频 / 字幕 / info.json
transcripts/                   # Whisper + 说话人分离输出
notes/  handbook/              # 最终教程
scripts/                       # 流水线脚本 + .hf_token(机密,勿分享)
video_list.md                  # 待处理清单(下载前可删改)
```

## 安全
`scripts/.hf_token` 是机密,已 `chmod 600` 且在 `.gitignore` 中。该 token 曾在会话中明文出现,
建议用完后到 huggingface.co **轮换**。
