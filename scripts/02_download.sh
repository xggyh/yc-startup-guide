#!/usr/bin/env bash
# 只下载音频 + 英文字幕 + 元数据。可重复运行(download-archive 去重、断点续跑)。
set -euo pipefail
cd "$(dirname "$0")/.."

[ -f video_list.txt ] || { echo "缺少 video_list.txt,请先运行 01_build_list.sh"; exit 1; }

yt-dlp \
  -f 'bestaudio/best' -x --audio-format m4a --audio-quality 0 \
  --write-info-json \
  --write-auto-subs --write-subs --sub-langs "en.*,en" --convert-subs vtt \
  --download-archive yc_video/archive.txt \
  --impersonate chrome \
  -P "yc_video" -P "temp:tmp" \
  -o "audio/%(id)s.%(ext)s" \
  -o "infojson:metadata/%(id)s.%(ext)s" \
  -o "subtitle:subs/%(id)s.%(ext)s" \
  --match-filter "duration > ${MIN_DUR:-180} & duration < ${MAX_DUR:-9000}" \
  --concurrent-fragments 4 --sleep-requests 1 --retries 10 --ignore-errors \
  -a video_list.txt

# 清理临时目录
rm -rf yc_video/tmp
echo "== 下载完成:$(ls yc_video/audio/*.m4a 2>/dev/null | wc -l) 个音频 =="
