#!/usr/bin/env bash
# 串联 ASR:先 Whisper 转写,再 pyannote 说话人分离。二者都可断点续跑。
set -uo pipefail
cd "$(dirname "$0")/.."
export HF_TOKEN="$(cat scripts/.hf_token 2>/dev/null)"

echo "=== [1/2] 转写 $(date '+%F %T') ==="
python scripts/03_transcribe.py
echo "=== [2/2] 说话人分离 $(date '+%F %T') ==="
python scripts/04_diarize.py
echo "=== ASR 全部完成 $(date '+%F %T') ==="
ls transcripts/*.speaker.json 2>/dev/null | wc -l | xargs echo "speaker-tagged transcripts:"
