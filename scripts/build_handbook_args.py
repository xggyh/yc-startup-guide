#!/usr/bin/env python3
"""读取 notes/*.summary.json,按主题把视频分组成手册章节,输出 handbook_args.json。
供 handbook_workflow.js 作为 args 使用。"""
import glob, json, os

CHAPTERS = [
    (1, "mindset",     "创始人心态与素质",     "Founder Mindset & Traits",
     "创业动机、韧性、信念、创始人特质、决策心态与自我管理"),
    (2, "idea",        "找方向与选 idea",      "Finding & Choosing Ideas",
     "如何寻找/评估创业点子、Request for Startups、AI-native 机会、市场与赛道选择"),
    (3, "validation",  "验证需求与和用户对话",  "Validation & Talking to Users",
     "需求验证、用户访谈、validation vs committing、早期信号判断"),
    (4, "mvp_pmf",     "做 MVP 与找到 PMF",    "MVP & Product-Market Fit",
     "构建 MVP、快速迭代、找到并度量 product-market fit"),
    (5, "growth",      "增长与获客",           "Growth & Distribution",
     "获客、分发渠道、do things that don't scale、销售与增长策略"),
    (6, "fundraising", "融资与申请 YC",        "Fundraising & Applying to YC",
     "融资、pitch、估值与条款、如何申请并通过 YC"),
    (7, "team",        "联合创始人与团队",      "Co-founders & Team",
     "寻找联合创始人、招聘、团队协作与公司文化"),
    (8, "ai_agent",    "AI / Agent 时代专题",  "The AI / Agent Era",
     "agent-first 产品、YC 对 AI/agent 的判断、护城河与切入点、AI 时代的创业机会与打法"),
    (9, "pitfalls",    "常见陷阱与反模式",      "Common Pitfalls & Anti-patterns",
     "创始人常犯的错误、反模式、失败教训与如何规避"),
]

def main():
    summaries = []
    for p in sorted(glob.glob("notes/*.summary.json")):
        try:
            summaries.append(json.load(open(p, encoding="utf-8")))
        except Exception as e:
            print("skip", p, e)
    by_id = {s["id"]: s for s in summaries if "id" in s}
    print(f"loaded {len(by_id)} summaries")

    MAX_PER_CHAPTER = 16
    chapters = []
    for num, key, zh, en, scope in CHAPTERS:
        # 相关度打分:主题在该视频 themes 列表里越靠前越核心(agent 往往把最核心主题写在前)
        scored = []
        for sid, s in by_id.items():
            themes = s.get("themes") or []
            if key in themes:
                score = len(themes) - themes.index(key)  # 越靠前分越高
                scored.append((score, sid))
        scored.sort(key=lambda x: (-x[0], x[1]))
        ids = [sid for _, sid in scored[:MAX_PER_CHAPTER]]
        chapters.append({"num": num, "key": key, "zh": zh, "en": en,
                         "scope": scope, "ids": ids})
        print(f"  ch{num} {key}: {len(scored)} matched -> top {len(ids)}")

    all_videos = [{"id": s["id"], "en_title": s.get("en_title", ""),
                   "zh_title": s.get("zh_title", ""),
                   "url": f"https://www.youtube.com/watch?v={s['id']}"}
                  for s in by_id.values()]

    out = {"chapters": chapters, "allVideos": sorted(all_videos, key=lambda v: v["id"])}
    json.dump(out, open("scripts/workflows/handbook_args.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote scripts/workflows/handbook_args.json")

if __name__ == "__main__":
    main()
