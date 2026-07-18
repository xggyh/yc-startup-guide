#!/usr/bin/env python3
"""把 handbook/ + notes/ 组织成 MkDocs Material 站点(docs/ + mkdocs.yml)。
可反复运行:重建 docs/ 并生成导航。"""
import glob, json, os, shutil, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SITE_URL = os.environ.get("SITE_URL", "")          # 例如 https://xggyh.github.io/yc-startup-guide/
REPO_URL = os.environ.get("REPO_URL", "")          # 例如 https://github.com/xggyh/yc-startup-guide

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

def build_docs(sums):
    if os.path.isdir("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs/handbook"); os.makedirs("docs/notes")
    for f in glob.glob("handbook/*.md"):
        shutil.copy(f, "docs/handbook/" + os.path.basename(f))
    for f in glob.glob("notes/*.md"):
        shutil.copy(f, "docs/notes/" + os.path.basename(f))
    write_index(sums)

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

<div class="grid" markdown>

| 指标 Metric | 值 |
|---|---|
| 视频 Videos | **{n}** |
| 音频时长 Audio | **~43.8 h** |
| 转写词数 Words | **~530k** |
| 手册章节 Chapters | **9 + 附录** |
| 逐视频双语笔记 Notes | **{n}** |

</div>

## 🚀 怎么读 / Reading paths

- **想清楚要不要干** → [第 1 章 心态](handbook/01-mindset.md)
- **找方向 / 选 idea** → [第 2 章 选题](handbook/02-idea.md) → [第 3 章 验证](handbook/03-validation.md)
- **动手做产品** → [第 4 章 MVP/PMF](handbook/04-mvp_pmf.md) → [第 5 章 增长](handbook/05-growth.md)
- **融资与团队** → [第 6 章 融资](handbook/06-fundraising.md) → [第 7 章 团队](handbook/07-team.md)
- **本时代的核心题** → ⭐ [第 8 章 AI / Agent 专题](handbook/08-ai_agent.md) → [第 9 章 陷阱](handbook/09-pitfalls.md)

## 📖 章节地图 / Chapters

{cards_block}

## 🧭 也可以直接看

- [手册导言](handbook/00-intro.md) — 完整的使用说明
- [视频索引附录](handbook/10-appendix.md) — {n} 支视频一览 + 对应笔记
- **逐视频双语笔记** — 左侧「逐视频笔记 Notes」按主题浏览全部 {n} 篇

---

## 🛠️ 怎么来的 / How it was built

```text
{n} 支 YC YouTube 视频(只下音频)
   → 本地 Whisper large-v3 转写(RTX 4090)
   → pyannote 说话人分离(谁在说)
   → 逐视频双语笔记 notes/<id>.md
   → 跨视频主题综合 → handbook/ 各章
```

全流程本地运行、脚本开源(见仓库 `scripts/`)。
"""
    open("docs/index.md", "w", encoding="utf-8").write(md)

def build_nav(sums):
    handbook_nav = [{CH_TITLES[k]: f"handbook/{k}.md"} for k in
                    ["00-intro"] + [f"{i:02d}-{key}" for i, key in
                                    enumerate(THEME_ORDER, 1)] + ["10-appendix"]]
    # 笔记按主 theme 分组
    groups = {t: [] for t in THEME_ORDER}
    other = []
    for vid, s in sums.items():
        themes = s.get("themes") or []
        prim = themes[0] if themes else None
        (groups[prim] if prim in groups else other).append((s.get("zh_title", vid), vid))
    notes_nav = []
    for t in THEME_ORDER:
        items = sorted(groups[t])
        if items:
            notes_nav.append({THEME_ZH[t]: [{title: f"notes/{vid}.md"} for title, vid in items]})
    if other:
        notes_nav.append({"其他 Other": [{title: f"notes/{vid}.md"} for title, vid in sorted(other)]})
    return [{"首页 Home": "index.md"},
            {"手册 Handbook": handbook_nav},
            {"逐视频笔记 Notes": notes_nav}]

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
