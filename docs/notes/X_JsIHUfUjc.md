# 如何用 AI 打造一家"自我改进"的公司 / How to Build a Self-Improving Company with AI

📄 **[点此查看全文转录 / Full transcript »](../transcripts/X_JsIHUfUjc.md)**

> **来源**: [How to Build a Self-Improving Company with AI](https://www.youtube.com/watch?v=X_JsIHUfUjc) · Y Combinator · 2026-05-21 · 时长 13:28
> **讲者**: Tom Blomfield(YC General Partner);现场引用/致谢 Diana Hu、Garry Tan、Jack Dorsey、Harj Taggar、Pete Koomen 的观点
> **一句话定位**: 不要把 AI 当"副驾"贴在旧组织上,而是把整家公司重构成一组"感知→决策→工具→质量闸→学习"的递归自改进循环——对 AI Agent 创始人来说,这是从"做工具"升级到"设计会自我进化的公司大脑"的架构蓝图。

## 🎯 TL;DR(中文核心要点)
- **旧组织=罗马军团**:传统公司是人肉充当信息上下传递管道的层级结构;AI 打破了这个前提,不该照搬。
- **Copilot 是错误心智模型**:给工程师加 20% 效率的副驾,只是"在旧工作方式上装了个更强的引擎",天花板很低。
- **真正的杠杆=递归自改进循环**:感知层(sensor)→决策/策略层(policy)→工具层(deterministic tools)→质量闸(evals/人审)→学习机制,闭环跑起来后公司"在你睡觉时也在变好"。
- **YC 的"卧槽时刻"**:在数据库查询 agent 之上加一个**监控 agent**,它观察每个员工的查询何时失败,当晚自动写代码、提 MR、让 agent 评审合并部署——第二天同样的查询就能成功。自改进,而不只是提效。
- **烧 token,不是烧 headcount**:YC 看到公司在 Demo Day 的人均营收比 18 个月前高约 5 倍;瓶颈正从人头转向 token 用量。
- **中层管理结束**:协调问题交给 AI,只保留两种角色——IC(建设者/操作者)和每件事都有一个具名负责人(DRI),不要委员会。
- **让公司对 AI"可读(legible)"**:一切都要被记录——邮件、Slack、DM、office hour 录音;"没被记录=对你的智能而言没发生"。再做 diarization/摘要,给 AI"面包屑"而非原始 2000 小时。
- **软件是一次性的,上下文才值钱**:内部 dashboard/工具用 Codex 一次性生成、随模型变强就丢弃重造;要极度珍惜地保存原始数据、业务上下文与 skills。

## 🧭 适合谁 / 什么时候看
- 正在或即将创业、想从第一天就"按 AI 原生形态"搭公司的 AI Agent 工程师。
- 已有小团队(<20 人)、还来得及"推倒重建"组织与内部工具的早期创始人。
- 想理解"agent 提效"与"agent 自改进闭环"本质区别、以及如何设计学习机制的技术负责人。

## 📝 分段精读

### 1. 公司就是罗马军团 / Companies Are Roman Legions `[00:00–00:54]`
**要点(中文)**: 罗马军团用嵌套层级和固定管辖幅度,把命令自上而下传、信息自下而上收。今天大多数公司同构:人是信息上下流动的"管道"。Tom 借 Jack Dorsey 的推文点破一个隐含假设——"层级化组织是组织经济价值的正确方式",而 AI 恰恰打破了它。
> 🗣️ "If you think about most companies today, they are organised like a Roman legion, where human beings are the conduit for information flowing up and down." —— Tom Blomfield
> 译:如果你审视今天的大多数公司,它们的组织方式就像罗马军团——人类是信息上下流动的管道。

### 2. Copilot 是错误的心智模型 / Extract the Domain Knowledge `[00:54–02:24]`
**要点(中文)**: 一年前大家谈 AI 只谈生产力——加个 copilot 让工程师提效 20%。Tom(引 Pete 的博客)认为这是错的:等于在旧工作方式上装个更强引擎。正确做法是"重新想象公司是什么":把散落在人脑、Slack、邮件、Notion 里的领域知识/business know-how 抽取出来,定义成 context 或一组 skills,使公司"对 AI 可读",从而从层级组织跃迁为 AI 原生组织。
> 🗣️ "The thing that's really stuck with me is this idea of extracting the domain knowledge from your company and defining it as context or a set of skills or whatever you want to call it." —— Tom Blomfield
> 译:最触动我的,是把公司的领域知识抽取出来、定义成 context 或一组 skills(叫什么都行)这个想法。
> 🗣️ "AI is not something you bolt on to the side of your company... you can reimagine what a company is as a set of recursive, self-improving AI loops." —— Tom Blomfield
> 译:AI 不是你螺栓式地拧在公司侧面的东西……你可以把公司重新想象成一组递归的、自我改进的 AI 循环。

### 3. 递归自改进循环 / The Recursive Self-Improving Loop `[02:24–04:12]`
**要点(中文)**: 一个完整的 AI 循环有五层:**感知层**(sensor:客户邮件、支持工单、代码变更、退订、产品埋点等外部信号)→ **策略/决策层**(policy:能做什么、什么必须请人批准、什么必须记录)→ **工具层**(deterministic APIs,如查数据库、看日历——即 Garry 说的"代码/skills")→ **质量闸**(evals、确定性检查、安全过滤、高风险人审)→ **学习机制**(从现实反馈里发现失败并回灌到顶部)。每一步都做到最小人工干预,系统就会在你睡觉时越变越好。
> 🗣️ "your system interacts with the real world, picks up where it doesn't work, and loops back into the top again... your system gets better and better and better while you're sleeping." —— Tom Blomfield
> 译:系统与真实世界交互,捕捉哪里失效,再回灌到循环顶端……于是它在你睡觉时越来越好、越来越好、越来越好。

### 4. YC 的"卧槽时刻"与自优化产品/客服循环 / The Holy Shit Moment + Self-Optimizing Loops `[04:12–06:29]`
**要点(中文)**: 起点是一个能查数据库的 agent(如"我上次和这家公司 office hour 是什么时候"),再进化到用 RAG 帮你找 5 位相关创始人——但这只是"副驾",让 Tom 提效 20–30%。真正的跃迁,是在其上加一个**监控 agent**:它盯着每个 YC 员工的每次查询,记录成功与失败;失败时自问"缺什么工具?要不要改 skills 文件/换数据库/加索引?",然后当晚自动写代码、提 MR、让 agent 评审并合并部署——第二天同样查询就成功。同样的模式可用于产品分析(自动找漏斗摩擦点→做 A/B→选优部署)和客服(agent 扮演 CPO/CTO 做取舍,合乎路线图的当晚就上线)。
> 🗣️ "The aha moment for me came when we put a monitoring agent on top of that, which looked at every single query every single YC employee was doing, and saw when it worked and when it did not work." —— Tom Blomfield
> 译:我的顿悟时刻,是我们在它之上加了一个监控 agent——它盯着每个 YC 员工的每一次查询,观察它何时成功、何时失败。
> 🗣️ "you can just throw tokens at this problem and your company will get better." —— Tom Blomfield
> 译:你只需要往这个问题上砸 token,你的公司就会变好。

### 5. 烧 token,不是烧人头 / Burn Tokens, Not Headcount `[06:29–07:23]`
**要点(中文)**: 含义是资源分配的重心转移:YC 观察到公司到 Demo Day 时人均营收比 18 个月前高约 5 倍,且会延续到 A、B 轮;未来很快会被 token 用量而非人头卡住。当下最粗糙的衡量就是看每个人的 token 消耗——极端下当然可被博弈、不能拿来做晋升/开除排行榜,但作为方向性信号,谁在"token maxing"、谁没有,是判断该把时间花在哪些员工身上的好参考。现在的核心任务是"最大化实验,搞清楚这个新智能到底能做什么"。
> 🗣️ "We are seeing companies get to demo day with about 5X more revenue per employee than they did 18 months ago." —— Tom Blomfield
> 译:我们看到,公司到 Demo Day 时的人均营收,比 18 个月前高了大约 5 倍。

### 6. 中层管理结束 / Middle Management Is Over `[07:23–08:05]`
**要点(中文)**: 中层的核心职能是协调,而协调正是 AI 该做的事,因此中层不再需要。只保留两种角色:每个人都是 IC(builder/operator),以及每件事都必须有一个**具名的负责人(DRI)**——不是委员会、不是一群人,而是单个人。公司可以完全建立在 IC 之上并高效运转。
> 🗣️ "you need a named human, not a committee, not a group of people, just a single person." —— Tom Blomfield
> 译:你需要一个具名的人来负责,不是委员会,不是一群人,就是单独一个人。

### 7. 让一切对 AI 可读:记录一切 + 重生成 YC 用户手册 / Make Everything Legible to AI `[08:05–11:19]`
**要点(中文)**: 想建自改进公司,第一要务是"让整个组织对 AI 可读",而这要求**记录一切**:所有 partner 邮件进 YC 数据库,每条 Slack、每条 DM、每次 office hour(近三四个月已在录)全部录下来——"被记录=对 AI 而言发生过;没被记录=对你的智能而言没发生"。手段可以是手机、录音夹、智能眼镜或给每个房间装麦。但不能把 2000 小时原始录音塞进上下文,要做 **diarization/摘要**,压缩成要点再给 AI"面包屑"。实例:Harj 用三个月约 2000 小时 office hour 录音,一个周末就重生成了一本 150 页、远胜旧版的用户手册,并能每月自更新——新建议与旧手册比对后被吸收或丢弃,手册变成"活的大脑",再灌进 agent 就能一次拿到"16 位 YC partner 的合并智慧"。
> 🗣️ "if it is recorded, it happened to the AI. If it did not get recorded, it did not happen to your intelligence." —— Tom Blomfield
> 译:如果它被记录了,它对 AI 来说就发生过;如果它没被记录,它对你的智能来说就没发生过。
> 🗣️ "you cannot pump in 2,000 hours worth of recordings into a context window. So you have to diarize it... and then give the AI breadcrumbs." —— Tom Blomfield
> 译:你不可能把 2000 小时录音直接塞进上下文窗口,所以必须做 diarization(说话人分离/摘要)……然后给 AI 留下"面包屑"。

### 8. 软件是一次性的,上下文才值钱 / Software Is Ephemeral, Context Is Valuable `[11:19–12:18]`
**要点(中文)**: 每个职能不只需要 dashboard,而是**按需生成的软件**:Codex 5.5 已经好到能一次性(one-shot)生成大多数内部工具/看板且质量不俗。所以内部运营团队应坐在这层"理解/智能"之上,自己生成 dashboard 和工作流,并把这些软件视为**完全可抛弃**的。要极度珍惜地保存原始数据(如 Garry 把邮件全存成 Markdown、什么都不丢),但把软件当临时品——模型一两个月后更强,就丢掉旧软件、用原始指令重新生成。值钱的是业务上下文和 skills,不是上面那层软件。
> 🗣️ "The models get smarter in a month or two. Throw the software away. Give it your original set of instructions and regenerate the data." —— Tom Blomfield
> 译:模型一两个月就更聪明了。把软件丢掉,给它你最初那套指令,重新生成。
> 🗣️ "the business context and skills are the valuable part. I think the software on top of it is ephemeral." —— Tom Blomfield
> 译:业务上下文和 skills 才是有价值的部分,而其上的软件是一次性的。

### 9. 人类还在哪里重要 / Where Humans Still Matter `[12:18–13:28]`
**要点(中文)**: 公司的中心是"company brain"——所有数据、邮件、DM、skills、know-how;人类站在这个大脑的**边缘**,作为智能与现实接触的界面,伸进模型还去不了的地方:新奇情境、伦理判断、高风险高情绪时刻(比如创始人来找你聊要不要和联合创始人分手),以及销售现场——Tom 认为这类场合未来 20 年仍需要真人。收尾抛出一个"愿景大喇叭"式的问题:如果今天从零建公司,你会不会一开始就按这种形态搭?对足够小的团队,没有借口不做对。
> 🗣️ "the humans sit around the edge of this interfacing with the real world... Human beings reach into places the models can't go yet." —— Tom Blomfield
> 译:人类坐在这个(公司大脑)的边缘,作为与真实世界对接的界面……人类伸进模型目前还去不了的地方。
> 🗣️ "If you were building your company today, would you start it in this shape? For most of you, you're small enough to build it right." —— Tom Blomfield
> 译:如果你今天在建公司,你会不会一开始就按这个形态来搭?你们大多数人足够小,完全来得及一开始就搭对。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把产品/公司拆成五层循环**:为你的核心 agent 明确画出 sensor(输入信号)→ policy(权限与必须记录项)→ tools(确定性 API)→ quality gate(evals/人审)→ learning(失败回灌)五层,缺哪层补哪层。
- [ ] **给主 agent 加一个"监控 agent"**:记录每次调用的成功/失败,让它诊断失败原因并自动发起代码/skills/索引改动的 MR,由 agent 评审合并——把"提效"升级成"自改进"。
- [ ] **从第一天记录一切**:邮件、Slack、通话、会议全量留存并结构化入库;建立 diarization/摘要管线,产出可喂给 agent 的"面包屑",而不是原始长录音。
- [ ] **把内部工具当一次性品**:用一次性生成的 dashboard/脚本跑运营,极度珍惜地保存原始数据与 skills 文件;模型迭代后重生成软件,而非维护它。
- [ ] **组织按 IC + DRI 搭建**:每个关键任务指定单个具名负责人,不设中层协调层,把协调交给 agent。
- [ ] **建立 token 消耗可观测性**:把 token 用量作为方向性内部指标(别做成晋升/开除排行榜),识别谁在真正"token maxing"并向其学习。
- [ ] **让你的知识库自改进**:像 YC 重生成用户手册那样,把每条新洞见与现有 knowledge base 比对,自动决定吸收或丢弃,使其成为"活的大脑"。

## 🔑 关键术语 / 概念
- **Recursive self-improving loop(递归自改进循环)** — sensor→policy→tools→quality gate→learning 的闭环,能在最小人工干预下让系统随时间自动变好。
- **Sensor layer(感知层)** — 从外部世界采集信号的入口:客户邮件、支持工单、代码变更、退订、产品埋点等。
- **Policy / decision layer(策略层)** — 规定 agent 能做什么、什么须请人批准、什么必须记录的规则层。
- **Tool layer / deterministic APIs(工具层)** — agent 可调用的确定性工具,如查数据库、看日历;即"Garry 的代码/skills"。
- **Quality gate(质量闸)** — evals、确定性检查、安全过滤与高风险人审组成的把关层。
- **Legible to AI(对 AI 可读)** — 组织的所有知识都被记录并可被 AI 检索理解;"没被记录=对智能而言没发生"。
- **Diarization(说话人分离/摘要)** — 把海量录音压缩、归类、按说话人切分成要点,为 AI 提供"面包屑"而非原始上下文。
- **DRI(Directly Responsible Individual,具名负责人)** — 每件事只由单个具名的人负责,取代委员会式协调。
- **Token maxing** — 员工把 token/AI 用到极致的程度,作为方向性(非考核)信号。
- **Company brain(公司大脑)** — 由全部数据、邮件、DM、skills、know-how 构成的中心;人类站在其边缘与现实对接。
- **Ephemeral software(一次性软件)** — 可按需生成、随模型变强即抛弃重造的内部工具,与永久保存的数据/上下文相对。

## 🔖 高价值金句时间戳
- `[02:32]` "you can reimagine what a company is as a set of recursive, self-improving AI loops." — 全场核心命题:公司=一组自改进循环,而非层级军团。
- `[04:29]` "The aha moment for me came when we put a monitoring agent on top of that." — "监控 agent"是从提效跃迁到自改进的关键动作,可直接照搬进你的架构。
- `[06:29]` "burn tokens, not headcount." — 资源观转变的一句话口号,直接影响你怎么配人和配算力。
- `[07:23]` "I think middle management is done. I just don't think you need middle management for this coordination problem." — 组织设计判断:协调交给 AI,只留 IC 与 DRI。
- `[08:33]` "if it is recorded, it happened to the AI. If it did not get recorded, it did not happen to your intelligence." — "记录一切"的最狠表述,决定你的数据/可读性基建优先级。
- `[11:48]` "The models get smarter in a month or two. Throw the software away." — 把软件当一次性品、只珍藏数据与上下文的反直觉结论。
- `[13:04]` "If you were building your company today, would you start it in this shape?" — 留给创始人的收尾拷问:小团队没有借口不一次搭对。
