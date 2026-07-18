# 六个月折腾折出一家 $100M ARR 公司:Emergent 的打法 / Emergent: How Six Months of Tinkering Led To A $100M ARR Company

📄 **[点此查看全文转录 / Full transcript »](../transcripts/yyXCQHX55N4.md)**

> **来源**: [Emergent: How Six Months of Tinkering Led To A $100M ARR Company](https://www.youtube.com/watch?v=yyXCQHX55N4) · Y Combinator · 2026-06-06 · 时长 29:05
> **讲者**: Mukund Jha(Emergent 联合创始人 & CEO,SPEAKER_00)· 对谈主持 Jared Friedman(YC 管理合伙人,SPEAKER_01)· 录于 Startup School India
> **一句话定位**: 一位连续创业者(第五次创业、Dunzo → Emergent)手把手讲他如何靠"押注 AI 指数级进步、把最后一公里做到能用、用 benchmark 锚定团队"在九个月做到 8.5M 用户 / $100M ARR;对做 AI coding/agent、又是"第 N 个入场者"的创始人极对症。

## 🎯 TL;DR(中文核心要点)
- **护城河是"最后一公里",不是能跑 demo**:Emergent 不是第一个 AI 建站/写码工具,但市面产品都停在前端、只会做 demoware——"上手容易、收尾差",交付不出能跑的真软件(真后端、真数据库)。他从"要自动化整个软件工程"的角度整体重造,靠交付可用软件后来居上。第二入场者照样能赢。
- **永远朝 AI 的方向建,并主动跳过"模型很快会解决"的问题**:早期模型连 JSON 输出都做不好,20–30 家 YC 公司在做 JSON 解析;Emergent 判断"下一代模型会解决它",直接跳过这个问题,把精力全压在 agent 本身。这是给 AI Agent 创始人最值钱的一条。
- **每出一代新模型,就把已学的全部删掉、按新模型重新想象世界**:九个月里他们把系统重写了 3 次;像 Opus 这种"新一类模型"要求推倒重来。别把架构焊死在当前模型的缺陷上。
- **"活在边缘"(living at the edge)**:最好的创业点子来自"现在还差一点点做不到"的事——把模型能力向前投影 6 个月来定方向,而不是只看今天能做什么。当年"自动化软件工程"被 10–12 家 VC 拒了,就因为模型还没到那一步。
- **用一个"数字 / benchmark"锚定方向**:还没想清做什么产品时,他让团队去打 SWE-bench(当时最难的基准),三个月做到世界第一;并行 test-time compute、记忆系统、agent 间通信等核心能力全在打榜过程中练出来了。一个能显示进度的数字,能把团队焊到对的方向上。
- **从个人痛点出发、跟着直觉走**:Dunzo(城市杂事太多)和 Emergent(想把无数点子快速做成软件)都源于自己的真实痛点——痛点近则反馈回路更强、更懂客户;作为创始人,信自己的直觉常比听一堆建议靠谱。
- **解最难的问题,但要聚焦**:87 家公司做一样的事,Dunzo 靠死磕"最后一公里"胜出;但后期同时做十件事(marketplace、代拿代送……)、没在跑通的暗店模式上 double down,是它没能规模化的教训。
- **从第一天就做全球,把目标 10x / 100x**:做本地公司和做全球公司一样难,不如 day 0 就面向全球(Emergent 95% 团队在班加罗尔、190 国用户、收入主要来自欧美)。更难的点子反而更容易——因为能召感更多人;现在"不是攻地板,是攻天花板"。

## 🧭 适合谁 / 什么时候看
- 你在做 AI coding / agent 产品,正纠结架构该押注**当前**模型能力还是**未来**模型能力。
- 你是某赛道的"第 N 个入场者",想知道在已有大玩家的情况下如何靠"把最后一公里做到真能用"后来居上。
- 你想要一套"把 AI 能力向前投影 6 个月"来定产品方向的心智框架,以及用 benchmark / 数字锚定团队的具体做法。
- 想听一位连续创业者(五次创业、Dunzo → Emergent)在 to C 规模化与 AI native 全球化上的第一手复盘。

## 📝 分段精读

### 1. Emergent 是什么:与 AI 对话就能上线真软件 / What Is Emergent `[00:56–02:54]`
**要点(中文)**: Emergent 让完全不会编程的人只靠"和 agent 聊天"就能构建、上线、变现真正可用的软件——托管、部署、维护全托管掉。团队最初是一间研究实验室,四个人做编码 agent,在 SWE-bench 上拿到世界第一,然后才转向"把编程能力普惠给所有人"。底层信念:过去 30 年世界的经济增长几乎全来自软件公司,把这份能力交到十亿人手里,是巨大的未被满足需求。九个月内做到 8.5M+ 用户、10M+ App、$100M ARR。
> 🗣️ "If you look at the last 30 years, most of the economic gain in the world has come from software companies. If you remove all the software companies from NASDAQ and S&P, you'll see it's been just a flat line." —— Mukund Jha `[00:00]`
> 译:回看过去 30 年,世界上绝大部分经济收益都来自软件公司;如果你把所有软件公司从纳斯达克和标普里剔掉,会发现剩下的就是一条平线。
> 🗣️ "There are a billion people with so many ideas, so many ideas just die because you do not have an access to sort of bring them to life." —— Mukund Jha `[02:14]`
> 译:有十亿人怀着无数点子,而无数点子就这么死掉了——只因为你没有把它变成现实的门路。

### 2. 九个月 $100M ARR & 为什么从印度做全球公司 / 9 Months to $100M ARR, Global From India `[02:54–05:00]`
**要点(中文)**: 市场的潜在需求极大:大量想做软件却没技术团队的创业者被"接触不到工具"卡住,平台一出现就被引爆。用户遍布 190 国,收入主力是美国和欧洲,印度只占约 10%。Mukund 2014 年从美国 Google 回印度,一直有个执念:为什么印度出不了 Google、出不了 Facebook?这些巨头的高层有大量印度人,却没有一家"技术优先的全球公司"来自印度——他要造的正是这个。
> 🗣️ "Why is there no sort of technology first global company from India?" —— Mukund Jha `[04:15]`
> 译:为什么就没有一家"技术优先的全球公司"是从印度出来的?

### 3. Dunzo 起源 + 五次创业:解最难的问题、从个人痛点出发 / Dunzo & Five Startups `[05:00–10:35]`
**要点(中文)**: Emergent 是他的第五家创业公司,上一家是估值巨大的 Dunzo(印度 quick commerce 先驱,峰值月单 1000 万,一度成为"Dunzo 一下"的动词)。反复出现的方法论有三条:(1)**去解最难的问题**——起步时有 87 家公司做一模一样的事,Dunzo 靠死磕"最后一公里"(亲自骑车送货、do things that don't scale)贴近客户、辨别真痛点;(2)**从个人痛点出发**——搬到班加罗尔杂事太多,他建了个 WhatsApp 群帮朋友跑腿,痛点近则反馈回路强、更懂客户;(3)**信自己的直觉**——建议会很多,但创始人对客户要什么往往有更好的直觉。
> 🗣️ "We picked up to solve the hard problems. When we started Dunzo, there were about 87 companies which were doing exactly the same thing." —— Mukund Jha `[05:45]`
> 译:我们选择去解那些最难的问题。我们做 Dunzo 时,市场上大约有 87 家公司在做一模一样的事。
> 🗣️ "Where I've been able to sort of solve a personal pain point, like the feedback loop has been stronger. You relate with the problem more deeply. You relate to the customer more deeply." —— Mukund Jha `[10:13]`
> 译:凡是我能从个人痛点出发去解的,反馈回路都更强——你和问题的关系更深,和客户的关系也更深。

### 4. 规模化 Dunzo 的教训:极致关怀客户,但要聚焦 / Lessons From Scaling Dunzo `[10:35–13:21]`
**要点(中文)**: Dunzo 峰值近百万骑手、月单 1000 万、约 5000 家门店。两条核心复盘:(1)**极致关怀客户**——早期没有 AI,晚高峰所有工程师都放下手里的活去客服聊天窗口;曾为把一个包裹送到另一座城,直接让骑手坐飞机去送,由此赢得客户真心热爱;(2)**聚焦**——暗店(Darkstore)模式明明跑通了,却同时做 marketplace、代拿代送等十件事,没有 double down,是没能规模化的关键教训。运营铁律(实时监控每一单的"war room"文化)被他原样搬到了 Emergent——现在监控每一个正在构建的软件任务,出问题就报警。
> 🗣️ "So we would go that extra mile for every single customer." —— Mukund Jha `[11:54]`
> 译:我们愿意为每一个客户多走那一步。
> 🗣️ "Focus is really important. ... Knowing that, hey, this is working, let's double down on this model, would have really, really helped." —— Mukund Jha `[12:01]`
> 译:聚焦真的非常重要……如果我们当时能认清"这个模式跑通了,就 all in 这个模式",会帮上大忙。

### 5. 离开 Dunzo,用"纯粹折腾"找到 Emergent / Leaving Dunzo, Tinkering Into Emergent `[13:21–17:25]`
**要点(中文)**: 2023 年 9 月离开 Dunzo 后他一度抑郁,前六个月只在反思。恰逢 ChatGPT / GPT-4 爆发,写代码成了他逃离噪音的出口——每天 10–12 小时纯粹地折腾新出的语音模型、开源模型,毫无目标(比如给 Mac 做了个能对话的助手,类似早期 open interpreter)。正是这段"无压力纯玩"的深潜,让他极早看清:编程这个领域会被极快颠覆。关键判断:他们押注 **AI 进步是指数级的、要永远朝 AI 的方向建**,于是从"整体自动化软件工程"而非"一块块拼"的角度切入。当时主流是做 copilot,他们逆着来去做自主 agent,结果被 10–12 家 VC 拒了(那时"agent"这个词都还不存在)。
> 🗣️ "I actually got this luxury of six months of like just pure tinkering on things that I really liked with no objective in mind." —— Mukund Jha `[14:30]`
> 译:我实实在在地享受了六个月的奢侈——纯粹地、毫无目标地折腾我真正喜欢的东西。
> 🗣️ "AI progress is going to be exponential and we will always build in the direction of AI." —— Mukund Jha `[17:02]`
> 译:AI 的进步会是指数级的,而我们永远朝着 AI(未来的方向)去建。
> 🗣️ "We in fact went and pitched to like 10, 12 VCs, got rejected from most of them." —— Mukund Jha `[16:37]`
> 译:我们实际上找了大概 10、12 家 VC 去 pitch,被其中大多数拒了。

### 6. 活在边缘 + 多智能体架构 / Living At The Edge & The Multi-Agent System `[17:25–20:42]`
**要点(中文)**: Jared 把这套打法命名为"活在边缘"——最好的创业点子恰恰来自"现在还差一点点做不到"的事,你要把模型能力向前投影 6 个月来定方向。Emergent 早在"agent"还不是个词时就做多 agent 编排:测试 agent、设计 agent 等在不同时点介入,由一个巨大的记忆系统协调,每构建一个新 App 就自学、把可学习点存进记忆,让平台越用越强(叠加 RL 与少量微调);为支持多个并行 agent 跑在同一快照上,他们自研了容器与内存快照技术。两条对 AI 创始人极其锋利的洞见:(1)**每出一类新模型(如 Opus)就把已学的全删掉、按新模型重新想象世界**——九个月里系统已重写 3 次;(2)**主动跳过模型很快会解决的问题**——当年 20–30 家 YC 公司在死磕 JSON 解析,他们判断下一代模型会解决,直接跳过,把精力压在 agent 上。
> 🗣️ "That's just where a lot of the best startup ideas come from — it's the things that aren't quite possible yet." —— Jared Friedman `[17:51]`
> 译:很多最好的创业点子恰恰就诞生在那里——那些"现在还没完全可能"的事情上。
> 🗣️ "Every time a new class of model, for example Opus is a new class of model, you have to actually delete whatever you have learned so far and sort of reimagine the world from the lens of this new model." —— Mukund Jha `[19:51]`
> 译:每次出现一类新模型(比如 Opus 就是一类新模型),你其实得把此前学到的一切全部删掉,从这个新模型的视角重新想象整个世界。
> 🗣️ "We took this view that the next model will be able to solve this, so let's say we just completely skipped that problem." —— Mukund Jha `[20:29]`
> 译:我们的判断是"下一代模型能解决这个问题",所以我们干脆彻底跳过了那个问题。

### 7. 打榜 SWE-bench:用一个数字锚定方向 / Beating SWE-bench `[20:42–22:42]`
**要点(中文)**: 在 YC 期间他们疯狂 pivot——每周白板上都是一个新点子(这周"AI 版 Zapier"……),团队被搞得很沮丧。为了"分散团队注意力",他随手挑了当时最难的 benchmark SWE-bench 让大家去攻,花三个月做到世界第一。这一打榜意外奠定了 Emergent 的全部技术地基:并行 test-time compute、记忆 agent、agent 间通信,都是在攻 benchmark 时发现的。方法论:把自己拴在一个"能显示进度的数字"上,是攻目标 / 建公司极好的方式,它逼你聚焦到对的方向、给你强反馈。
> 🗣️ "Attaching yourself to a number which can sort of show you progress is a really, really good way to attack a goal or go towards building a company." —— Mukund Jha `[22:22]`
> 译:把自己拴在一个能显示进度的数字上,是攻克目标、乃至去建一家公司的极好方式。

### 8. 第二入场者优势 + 从班加罗尔做全球 + 给创始人的建议 / Second Mover, Global From Bangalore & Advice `[22:42–29:05]`
**要点(中文)**: Emergent 不是第一个 AI 建站工具,但当时的玩家几乎都聚焦前端、做 demoware——上手容易、收尾差,交付不出真后端、真数据库、真能跑的软件。他们从"如果要自动化整个软件工程该怎么设计"的角度整体重造,实测在各平台跑同样的 prompt 时大幅领先,由此后来居上(第二入场者优势)。GTM 上他们把增长当成一道数学题(需要多少社媒曝光、多少展示、多少点击 → 多少用户),因产品足够好而选择红人/influencer 策略引爆。团队 95% 在班加罗尔、小队在 SF,面向全球用户,招人看"学习斜率"和对 AI 的真心热爱。收尾建议:做本地公司和做全球公司一样难,**从 day 0 就做全球**;更难的点子反而更容易(能召感更多人);**信直觉、想得更大**——把当下的设想 10x / 100x,"现在不是攻地板,是攻天花板"。
> 🗣️ "They were good at getting started, they were really bad at finishing. You will not get a working software out of that." —— Mukund Jha `[24:15]`
> 译:他们(其他平台)擅长让你起步,却非常不擅长收尾——你根本得不到一个能真正运行的软件。
> 🗣️ "Building a company for India, a local company, versus building a global company is actually exactly same effort." —— Mukund Jha `[27:22]`
> 译:为印度做一家本地公司,和做一家全球公司,其实花的力气一模一样。
> 🗣️ "It's not a time to sort of attack the floor, it's the time to attack the ceiling and think really big." —— Mukund Jha `[28:31]`
> 译:现在不是去攻地板的时候,而是去攻天花板、把格局想得非常大的时候。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **画一条"6 个月能力线"**:列出你的 agent 今天做不好、但按当前模型斜率半年内很可能被解决的问题(如格式/结构化输出、长上下文、工具调用可靠性),明确决定"自己解 vs. 等模型解",把工程力压在模型不会替你解决的差异化上。
- [ ] **把架构设计成"可推倒重建"**:假设每 3–6 个月要按一类新模型(如 Opus 级)重写核心,别把 prompt/编排/后处理焊死在当前模型的缺陷上;留好评测集与回归基线,让重写成本可控。
- [ ] **锁定一个能显示进度的数字**:选一个贴近你价值主张的 benchmark 或自建评测(端到端"任务真正跑通率"而非 demo 通过率),用它当北极星把团队焊到对的方向。
- [ ] **把"最后一公里"做成护城河**:别停在能演示,交付真后端/真数据、能部署能维护的成品;拿同一批 prompt 对着竞品做横向对比,用"真正可用软件的产出率"证明领先。
- [ ] **从个人痛点起步、缩短反馈回路**:选一个你自己每天真受其苦的场景做 agent,自己当第一个用户,像运营 war room 一样实时监控每个任务并对失败报警。
- [ ] **从 day 0 面向全球、把目标 10x/100x**:用远程/低成本地区团队 + 全球分发,把增长拆成"曝光→点击→用户"的数学题;产品足够好时优先红人/内容驱动的引爆式获客。

## 🔑 关键术语 / 概念
- **Emergent** — 讲者的公司(转写里常被误听成 "Immersion"/"a merchant");让不会编程的人靠对话构建、上线、变现真软件的 AI 平台。
- **Living at the edge / 活在边缘** — Icon(YC)与讲者共用的说法:在"模型现在还差一点点做不到、但投影 6 个月就能到"的地带找点子和定方向。
- **Demoware** — 只能跑演示、经不起真实使用的"演示软件";多数早期 AI 建站工具的通病(前端好看、无真后端)。
- **SWE-bench** — 评测编码 agent 解决真实 GitHub issue 能力的高难度基准;Emergent 前身实验室曾拿到世界第一。
- **Test-time compute(并行推理算力)** — 推理阶段用更多算力/并行 agent 换取更强解题能力;Emergent 打榜时练出的核心能力之一。
- **Multi-agent orchestration / 多智能体编排** — 测试 agent、设计 agent 等在不同时点介入、由统一记忆系统协调、可在同一快照上并行 swarm。
- **Second mover advantage / 第二入场者优势** — 不做第一个入场者,而是看清前人停在哪(如只做前端),从根子上重造把它做到能用而胜出。
- **Do things that don't scale** — YC 名言:早期亲自做不可规模化的事(如创始人自己送货)以贴近客户、辨别真痛点。

## 🔖 高价值金句时间戳
- `[00:00]` "If you remove all the software companies from NASDAQ and S&P, you'll see it's been just a flat line." — 软件是过去 30 年增长的近乎全部来源,这是"普惠编程"这门生意的底层信念。
- `[16:37]` "We in fact went and pitched to like 10, 12 VCs, got rejected from most of them." — 押注未来模型能力的点子在当下常被拒;被拒不等于错,只是别人还没看到那条能力曲线。
- `[17:51]` "That's just where a lot of the best startup ideas come from — it's the things that aren't quite possible yet." — "活在边缘"的一句话总结:去做现在还差一点点、6 个月后能成的事。
- `[19:51]` "You have to actually delete whatever you have learned so far and sort of reimagine the world from the lens of this new model." — 每出一类新模型就推倒重来;别把架构焊死在当前模型缺陷上(九个月重写 3 次)。
- `[20:29]` "We took this view that the next model will be able to solve this, so let's say we just completely skipped that problem." — 主动跳过模型很快会解决的问题(如 JSON 解析),把工程力压在差异化上。
- `[22:22]` "Attaching yourself to a number which can sort of show you progress is a really, really good way to attack a goal." — 用一个能显示进度的 benchmark/数字锚定团队,反而顺带练出核心能力。
- `[24:15]` "They were good at getting started, they were really bad at finishing. You will not get a working software out of that." — 把"最后一公里/收尾"做成护城河,是第二入场者后来居上的关键。
- `[28:31]` "It's not a time to attack the floor, it's the time to attack the ceiling and think really big." — AI 时代的野心校准:把设想 10x/100x,攻天花板而非地板。
