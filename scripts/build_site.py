#!/usr/bin/env python3
"""把 handbook/ + notes/ + transcripts/ 组织成三部分 MkDocs Material 站点。
  ① 逐视频精读 one-page(notes,顶部加"全文转录"跳转链接)
  ② 创业手册(handbook)
  ③ 全量转录(由说话人分离 json 生成带时间戳/说话人的可读全文)
可反复运行:重建 docs/ 并生成导航。"""
import glob, json, os, shutil, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SITE_URL = os.environ.get("SITE_URL", "")
REPO_URL = os.environ.get("REPO_URL", "")

THEME_ORDER = ["mindset", "idea", "validation", "mvp_pmf", "growth",
               "fundraising", "team", "ai_agent", "pitfalls"]
THEME_ZH = {"mindset": "心态 Mindset", "idea": "选题 Ideas", "validation": "验证 Validation",
            "mvp_pmf": "MVP / PMF", "growth": "增长 Growth", "fundraising": "融资 Fundraising",
            "team": "团队 Team", "ai_agent": "AI / Agent", "pitfalls": "陷阱 Pitfalls"}
CH_TITLES = {
    "00-intro": "导言 Introduction", "01-mindset": "第 1 章 · 创始人心态与素质",
    "02-idea": "第 2 章 · 找方向与选 idea", "03-validation": "第 3 章 · 验证需求与用户对话",
    "04-mvp_pmf": "第 4 章 · 做 MVP 与找到 PMF", "05-growth": "第 5 章 · 增长与获客",
    "06-fundraising": "第 6 章 · 融资与申请 YC", "07-team": "第 7 章 · 联合创始人与团队",
    "08-ai_agent": "第 8 章 · AI / Agent 时代专题", "09-pitfalls": "第 9 章 · 常见陷阱与反模式",
    "10-appendix": "附录 · 视频索引 Video Index",
}

def load_summaries():
    s = {}
    for p in glob.glob("notes/*.summary.json"):
        try:
            d = json.load(open(p, encoding="utf-8")); s[d["id"]] = d
        except Exception:
            pass
    return s

def mmss(sec):
    sec = int(sec or 0)
    return f"{sec // 60:02d}:{sec % 60:02d}"

# ---------- ③ 全量转录页 ----------
def build_transcripts(sums):
    os.makedirs("docs/transcripts", exist_ok=True)
    made = 0
    for vid, s in sums.items():
        jp = f"transcripts/{vid}.speaker.json"
        if not os.path.exists(jp):
            jp = f"transcripts/{vid}.json"
        if not os.path.exists(jp):
            continue
        data = json.load(open(jp, encoding="utf-8"))
        segs = data.get("segments", [])
        n_spk = data.get("num_speakers", 1) or 1
        multi = n_spk > 1
        # 把 segments 合并成可读段落:说话人变化 或 累计 > ~480 字 时断段
        paras, cur_spk, cur_start, buf, cur_chars = [], None, None, [], 0
        for seg in segs:
            spk = seg.get("speaker", "SPEAKER_00")
            txt = (seg.get("text") or "").strip()
            if not txt:
                continue
            if not buf:
                cur_spk, cur_start, buf, cur_chars = spk, seg["start"], [txt], len(txt)
            elif (multi and spk != cur_spk) or cur_chars > 480:
                paras.append((cur_start, cur_spk, " ".join(buf)))
                cur_spk, cur_start, buf, cur_chars = spk, seg["start"], [txt], len(txt)
            else:
                buf.append(txt); cur_chars += len(txt)
        if buf:
            paras.append((cur_start, cur_spk, " ".join(buf)))

        zt, et = s.get("zh_title", vid), s.get("en_title", "")
        out = [f"# 全文转录 · {zt}", "",
               f"> ▶ [YouTube](https://www.youtube.com/watch?v={vid}) &nbsp;·&nbsp; "
               f"← [返回精读 One-page](../notes/{vid}.md) &nbsp;·&nbsp; {et}"]
        if multi:
            out.append(f">\n> 🗣️ 说话人分离识别到 **{n_spk}** 位发言者(标注为 SPEAKER_00 …)。")
        out.append("")
        for start, spk, text in paras:
            tag = f"`[{mmss(start)}]` **{spk}:** " if multi else f"`[{mmss(start)}]` "
            out.append(tag + text + "\n")
        open(f"docs/transcripts/{vid}.md", "w", encoding="utf-8").write("\n".join(out))
        made += 1
    return made

# ---------- ① 精读 one-page(注入转录跳转链接)----------
def build_notes():
    os.makedirs("docs/notes", exist_ok=True)
    for f in glob.glob("notes/*.md"):
        vid = os.path.splitext(os.path.basename(f))[0]
        lines = open(f, encoding="utf-8").read().split("\n")
        out, inserted = [], False
        for ln in lines:
            out.append(ln)
            if not inserted and ln.startswith("# "):
                out.append("")
                out.append(f"📄 **[点此查看全文转录 / Full transcript »](../transcripts/{vid}.md)**")
                inserted = True
        open(f"docs/notes/{vid}.md", "w", encoding="utf-8").write("\n".join(out))

def build_docs(sums):
    if os.path.isdir("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs/handbook")
    for f in glob.glob("handbook/*.md"):
        shutil.copy(f, "docs/handbook/" + os.path.basename(f))
    build_notes()
    n_trans = build_transcripts(sums)
    write_index(sums)
    print(f"  notes: {len(glob.glob('docs/notes/*.md'))} | transcripts: {n_trans} | "
          f"handbook: {len(glob.glob('docs/handbook/*.md'))}")

def write_index(sums):
    n = len(sums)
    cards = []
    for key in THEME_ORDER:
        num = THEME_ORDER.index(key) + 1
        fn = f"{num:02d}-{key}"
        cards.append(f"-   __{CH_TITLES[fn]}__\n\n    [:octicons-arrow-right-24: 阅读本章](handbook/{fn}.md)")
    cards_block = "<div class=\"grid cards\" markdown>\n\n" + "\n\n".join(cards) + "\n\n</div>"
    md = f"""# YC 创业手册 · AI Agent 创始人版

> 从 **{n} 支 Y Combinator 近期(2026)视频**综合而成的**中英双语创业教程**,写给即将下场的 **AI Agent 工程师**。
> A bilingual startup handbook synthesized from {n} recent Y Combinator talks — for AI-agent engineers about to build.

## 📚 三个部分怎么配合 / Three parts

<div class="grid cards" markdown>

-   __① 逐视频精读 · One-page__

    每支视频一页,学完就知道它讲了什么:中文 TL;DR + 分段精读(英文金句 + 中文小结)+ 给 AI Agent 创始人的行动项。每页顶部可**一键跳到该视频的全文转录**。

    [:octicons-arrow-right-24: 进入精读](notes/{sorted(sums)[0]}.md)

-   __② 创业手册 · Handbook__

    把 {n} 支视频的共识抽象成 9 章「核心原则 + 行动清单」,**跟着学、跟着做**。

    [:octicons-arrow-right-24: 从导言开始](handbook/00-intro.md)

-   __③ 全量转录 · Transcripts__

    每支视频的**完整逐字转录**(带时间戳与说话人),从精读页跳转过来,想深挖细节时用。

    [:octicons-arrow-right-24: 视频索引](handbook/10-appendix.md)

</div>

**建议路径**:先在 ② 手册建立框架 → 用 ① 精读逐支吃透 → 需要原话/细节时点进 ③ 转录。

## 🗺️ 手册章节地图 / Chapters

{cards_block}

---

## 🛠️ 怎么来的 / How it was built

```text
{n} 支 YC YouTube 视频(只下音频)
   → 本地 Whisper large-v3 转写(RTX 4090)
   → pyannote 说话人分离(谁在说)→ ③ 全量转录
   → 逐视频双语笔记 → ① 精读 one-page
   → 跨视频主题综合 → ② 手册
```

全流程本地运行、脚本开源(见仓库 `scripts/`)。
"""
    open("docs/index.md", "w", encoding="utf-8").write(md)

# ---------- 导航 ----------
def group_by_theme(sums, subdir):
    groups = {t: [] for t in THEME_ORDER}
    other = []
    for vid, s in sums.items():
        themes = s.get("themes") or []
        prim = themes[0] if themes else None
        (groups[prim] if prim in groups else other).append((s.get("zh_title", vid), vid))
    nav = []
    for t in THEME_ORDER:
        items = sorted(groups[t])
        if items:
            nav.append({THEME_ZH[t]: [{title: f"{subdir}/{vid}.md"} for title, vid in items]})
    if other:
        nav.append({"其他 Other": [{title: f"{subdir}/{vid}.md"} for title, vid in sorted(other)]})
    return nav

def build_nav(sums):
    handbook_nav = [{CH_TITLES[k]: f"handbook/{k}.md"} for k in
                    ["00-intro"] + [f"{i:02d}-{key}" for i, key in enumerate(THEME_ORDER, 1)]
                    + ["10-appendix"]]
    return [
        {"首页 Home": "index.md"},
        {"① 逐视频精读 · One-page": group_by_theme(sums, "notes")},
        {"② 创业手册 · Handbook": handbook_nav},
        {"③ 全量转录 · Transcripts": group_by_theme(sums, "transcripts")},
    ]

def write_mkdocs(sums):
    cfg = {
        "site_name": "YC 创业手册 · AI Agent 创始人版",
        "site_description": "从 80 支 Y Combinator 视频综合的中英双语创业教程(AI Agent 创始人向)",
        "theme": {
            "name": "material", "language": "zh",
            "palette": [
                {"media": "(prefers-color-scheme: light)", "scheme": "default",
                 "primary": "deep orange", "accent": "orange",
                 "toggle": {"icon": "material/weather-night", "name": "切换到深色模式"}},
                {"media": "(prefers-color-scheme: dark)", "scheme": "slate",
                 "primary": "deep orange", "accent": "orange",
                 "toggle": {"icon": "material/weather-sunny", "name": "切换到浅色模式"}},
            ],
            "features": ["navigation.instant", "navigation.tracking", "navigation.top",
                         "navigation.indexes", "navigation.footer", "search.highlight",
                         "search.suggest", "content.code.copy", "toc.follow"],
            "icon": {"repo": "fontawesome/brands/github"},
        },
        "markdown_extensions": [
            "admonition", "attr_list", "md_in_html", "tables", "footnotes",
            {"toc": {"permalink": True}},
            "pymdownx.details", "pymdownx.superfences",
            {"pymdownx.tasklist": {"custom_checkbox": True}},
        ],
        "plugins": [{"search": {}}],
        "nav": build_nav(sums),
    }
    if SITE_URL:
        cfg["site_url"] = SITE_URL
    if REPO_URL:
        cfg["repo_url"] = REPO_URL
        cfg["repo_name"] = REPO_URL.rstrip("/").split("/")[-1]
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

def main():
    sums = load_summaries()
    print(f"loaded {len(sums)} summaries")
    build_docs(sums)
    write_mkdocs(sums)
    print("wrote docs/ and mkdocs.yml")

if __name__ == "__main__":
    main()
