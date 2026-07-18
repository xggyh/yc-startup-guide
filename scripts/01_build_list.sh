#!/usr/bin/env bash
# 生成待下载视频清单:从 YC 主频道拉取近期上传(已涵盖 Lightcone / Dalton & Michael /
# 讲座 / 访谈,它们都发布在 @ycombinator 主频道),去重 + 过滤时长 + 封顶,
# 产出 video_list.md(人看)与 video_list.txt(下载器用)。
set -euo pipefail
cd "$(dirname "$0")/.."

MAX_TOTAL="${MAX_TOTAL:-80}"     # 总量封顶
MIN_DUR="${MIN_DUR:-180}"        # 跳过 < 3 分钟(shorts/预告)
MAX_DUR="${MAX_DUR:-9000}"       # 跳过 > 2.5 小时(超长直播)

# 数据源:"URL<TAB>标签<TAB>抓取条数"。主频道按时间倒序,取足够多再全局封顶。
SOURCES=(
  $'https://www.youtube.com/@ycombinator/videos\tmain\t100'
)

TAB=$'\t'
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
for entry in "${SOURCES[@]}"; do
  IFS=$'\t' read -r url label end <<< "$entry"
  echo ">> 拉取 $label ($url) end=$end" >&2
  # 注意:--print 模板必须用真实制表符(双引号里的 "\t" 是字面反斜杠+t,不是 TAB)
  yt-dlp --flat-playlist --playlist-end "$end" \
    --print "%(id)s${TAB}%(title)s${TAB}%(duration)s${TAB}%(webpage_url)s${TAB}${label}" \
    "$url" >> "$TMP" 2>>/tmp/ytdlp_list_err.log || echo "!! 失败: $label" >&2
done

python3 - "$TMP" "$MAX_TOTAL" "$MIN_DUR" "$MAX_DUR" <<'PY'
import sys
tmp, maxtotal, mindur, maxdur = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
seen, rows = set(), []
for line in open(tmp, encoding='utf-8'):
    p = line.rstrip('\n').split('\t')
    if len(p) < 5:
        continue
    vid, title, dur, url, label = p[0], p[1], p[2], p[3], p[4]
    if not vid or vid in seen:
        continue
    try:
        d = int(float(dur))
    except Exception:
        d = 0
    if d and (d < mindur or d > maxdur):
        continue
    seen.add(vid)
    rows.append((vid, title, d, url, label))
rows = rows[:maxtotal]

with open('video_list.txt', 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(r[3] + '\n')

total_sec = sum(r[2] for r in rows)
with open('video_list.md', 'w', encoding='utf-8') as f:
    f.write(f'# 待处理 YC 视频清单\n\n')
    f.write(f'- 共 **{len(rows)}** 个视频,合计约 **{total_sec/3600:.1f} 小时**音频\n')
    f.write(f'- 下载前可手动删改本文件对应的 `video_list.txt`(每行一个 URL)\n\n')
    f.write('| # | 时长 | 标题 | 来源 | 链接 |\n|---|------|------|------|------|\n')
    for i, (vid, title, d, url, label) in enumerate(rows, 1):
        mm = f'{d//60}:{d%60:02d}' if d else '?'
        t = title.replace('|', '\\|')
        f.write(f'| {i} | {mm} | {t} | {label} | {url} |\n')
print(f'wrote {len(rows)} videos ({total_sec/3600:.1f}h) -> video_list.txt / video_list.md')
PY
