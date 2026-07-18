import glob, json, os
THEME_ZH = {'mindset':'心态','idea':'选题','validation':'验证','mvp_pmf':'MVP/PMF',
            'growth':'增长','fundraising':'融资','team':'团队','ai_agent':'AI/Agent','pitfalls':'陷阱'}
rows=[]
for p in sorted(glob.glob('notes/*.summary.json')):
    s=json.load(open(p,encoding='utf-8')); vid=s['id']
    meta=f'yc_video/metadata/{vid}.info.json'
    dur=date=''; 
    if os.path.exists(meta):
        m=json.load(open(meta,encoding='utf-8'))
        d=int(m.get('duration') or 0); dur=f'{d//60}:{d%60:02d}'
        ud=str(m.get('upload_date') or ''); date=f'{ud[:4]}-{ud[4:6]}-{ud[6:]}' if len(ud)==8 else ''
    themes='、'.join(THEME_ZH.get(t,t) for t in (s.get('themes') or []))
    rows.append((date,vid,s.get('zh_title',''),s.get('en_title',''),dur,themes))
rows.sort(key=lambda r:r[0],reverse=True)
out=['# 附录 · 视频索引 / Video Index','',
     f'共 **{len(rows)}** 支 Y Combinator 视频(按上传时间倒序)。每支都有对应的逐视频双语笔记 `notes/<id>.md`。','',
     '| # | 视频 / Video | 时长 | 日期 | 主题 | 笔记 |','|---|---|---|---|---|---|']
for i,(date,vid,zh,en,dur,themes) in enumerate(rows,1):
    zt=zh.replace('|','\\|'); et=en.replace('|','\\|')
    out.append(f'| {i} | **{zt}**<br/>[{et}](https://www.youtube.com/watch?v={vid}) | {dur} | {date} | {themes} | [note](../notes/{vid}.md) |')
open('handbook/10-appendix.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
print(f'wrote handbook/10-appendix.md with {len(rows)} videos')
