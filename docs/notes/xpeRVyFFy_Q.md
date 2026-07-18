# 破解"空白画布"难题:Gusto 的 AI 联合创始人 / Solving the Blank Canvas Problem: Gusto's AI Co-Founder

📄 **[点此查看全文转录 / Full transcript »](../transcripts/xpeRVyFFy_Q.md)**

> **来源**: [Solving the Blank Canvas Problem: Gusto's AI Co-Founder](https://www.youtube.com/watch?v=xpeRVyFFy_Q) · Y Combinator · 2026-07-08 · 时长 32:27
> **讲者**: Eddie Kim(Gusto 联合创始人兼技术负责人,W12);主持 Harj Taggar(YC Managing Partner)
> **一句话定位**: 一个已到 10 亿美元营收的 SaaS 老兵,讲他如何绕过"空白画布"陷阱、用已有数据 + 聊天界面把 agentic AI 真正落地到 50 万小企业,以及五人十周、无文档无 Jira 造出新产品的打法——对做垂直 AI Agent 的创始人是一份"落地手册"。

## 🎯 TL;DR(中文核心要点)
- **别给用户一张空白画布**。通用 chat/agent 强大但有"blank canvas problem":99.9% 的人只把 AI 当"美化版搜索引擎"。Gusto 的做法是从用户**已经在做的重复任务**(跑工资单、审批休假)出发,主动建议自动化,而不是让用户从零想 prompt。
- **聊天就是最好的界面**。通过短信/Slack/Telegram 触发 AI、无需登录任何后台,是被严重低估的体验;技术人的本能是加 UI、加功能,正确方向是**让 agent 更聪明**,让用户在 IM 里就能把事做完。
- **技术负责人必须亲自下场**。Eddie 亲手搭了一套自托管 AI agent(air-gap 的 Mac Mini),读了它的源码,才发现"心跳"不过是**每 30 分钟跑一次 LLM 的 cron job**——"读到"和"亲手做"是两种完全不同的认知。
- **原型可以是一次误机的五小时**。灵感来自"为什么客户要等我们排 roadmap?能不能客户自己下 prompt、Gusto 就给他造出体验";在伦敦转机误机的 5 小时里用 Claude Code 现场撸出可用原型。
- **护城河 = 你已有的数据/记录系统**。原型只是"CRUD web app builder",没用上客户数据;进化后变成"prompt + Gusto 已知的行业与个人数据 → 自动化每周固定流程",这才是别人抄不走的。
- **卖 AI 给小企业几乎不用"卖"**。他们做的是"工作前的工作"(从 MindBody 导数据、在 Google Sheet 算佣金再录入工资单),每周 1 小时、痛点具体,一说就懂;而且不像大企业那样怕丢工作,是"hard yes"。
- **确定性任务别只靠 heartbeat**。心跳(每 30 分钟跑 LLM)不确定且贵;工资单这类要确定性的任务应识别出来、走**普通 cron / 多种触发方式**。
- **AI 时代的团队打法:五人、十周、无会议无文档无 Jira**。只留一个 7×24 的常开 Zoom("permazoom")+ 海量 Claude Code token;设计师写生产级代码、工程师做设计,"craft 退居其次,共同职责就是写和提交代码";先开 PR 再讨论,50% 命中率也比先写 PRD/Figma 快。

## 🧭 适合谁 / 什么时候看
- 正在做**垂直/行业 AI Agent**、纠结"给用户开放式对话还是引导式自动化"的创始人。
- 手里已有**数据或记录系统(system of record)**,想在其上叠加 agent 层的团队。
- 想学**AI 时代高速度产品开发**(小团队、去流程化、vibe coding)落地细节的技术负责人 / eng 团队。
- 想理解"agentic AI 为什么对普通用户没落地、怎么才能落地"的产品经理。

## 📝 分段精读

### 1. Gusto Co-Founder 是什么 & AI 现状:被当成"美化搜索引擎" / What it is & AI as a glorified search engine `[00:00–02:41]`
**要点(中文)**: Gusto Co-Founder 面向小企业,把他们在 Gusto 上做的业务流程(跑工资、审批休假、催员工提交工时表)端到端全自动化,甚至能做 Gusto 之外的事(下雨了就自动发邮件提醒旅行团客户带伞)。Eddie 的核心判断:被承诺的 "agentic world" 对绝大多数人从未真正到来,99.9% 的人只把 AI 当"美化版搜索引擎"——问一句、答一句,顶多让它做点调研、写点报告。
> 🗣️ "this like sort of like agentic world that we've been promised has never really materialized for most people out there." —— Eddie Kim
> 译:这个我们被许诺的、所谓的 agentic 世界,对外面绝大多数人来说其实从未真正实现。
> 🗣️ "the remaining 99.9% are still kind of like using this as a glorified search engine." —— Eddie Kim
> 译:剩下 99.9% 的人还是把它当成一个美化版的搜索引擎在用。

### 2. 解决"空白画布"问题 / Solving the blank canvas problem `[02:41–03:53]`
**要点(中文)**: 通用 agent(如自托管 Claude 那类)能力强,但有个致命问题——"空白画布":用户面对无限可能反而不知从何下手。Gusto 的破解法是**反过来**:不从空白开始,而从"我们已经在替客户解决的事"(payroll、HR、排班)出发,主动建议"要不要我把你每周跑工资这件事端到端自动化",客户甚至不用登录 Gusto。对 AI Agent 创业者:引导式、场景化的入口 > 万能对话框。
> 🗣️ "instead of starting with like, an open-claw type experience where it has a lot of powerful capabilities, but it has a problem, which I call the blank canvas problem. We actually start with all of the things that Gusto is already solving for our customers." —— Eddie Kim
> 译:我们没有从那种能力很强、但有"空白画布问题"的通用 agent 体验入手,而是从 Gusto 已经在为客户解决的所有事情开始。

### 3. 从个人折腾到产品灵感 & 为什么"发短信给 AI"有效 / From hobby project to product idea; why texting AI works `[03:53–07:06]`
**要点(中文)**: 灵感始于 Eddie 自己花 8 小时搭了一套自托管 AI agent(为防误删邮件特意 air-gap,买了 Mac Mini),搭完却发现自己也只把它当搜索引擎——但"能用 Telegram 发消息给它"这个看似不起眼的点,亲手一试才发现体验远胜打开浏览器登录网页版。两人共识:**聊天界面被严重低估**;技术人本能想加 UI/加功能,但真正该做的是让 agent 更聪明,好让你在 IM 里就把事办了。Eddie 补充一条元认知:一定要亲自下场"钻到细节里"。
> 🗣️ "people just really underestimate chat as the interface." —— Harj Taggar
> 译:人们真的严重低估了"聊天"作为交互界面(的价值)。
> 🗣️ "it is really important to still get into the weeds. Like if you're a technical leader, you should be coding." —— Eddie Kim
> 译:亲自钻进细节里非常重要;如果你是技术负责人,你就应该还在写代码。
> 🗣️ "there's this big gap between like what you read about and what you actually experience." —— Eddie Kim
> 译:你"读到的"和你"亲身体验到的"之间,存在着巨大的鸿沟。

### 4. 误机催生的原型:五小时用 Claude Code 撸出来 & v1 到底做了什么 / The missed flight that built a prototype + what v1 did `[07:06–10:47]`
**要点(中文)**: 真正点燃产品的问题是:"为什么客户要等我(等 Gusto 排 roadmap 交付)?能不能客户自己下个 prompt,Gusto 就当场给他造出这个体验?" 从马德里度假返程,在伦敦转机误了第二程,凭空多出 5 小时不被打断的时间,他用 Claude Code 现场造出原型。v1 本质是个 **CRUD web app builder**:客户说"我要一个能给员工发问卷/建 to-do/建 CRM 的应用",原型就用 Gusto 设计系统生成一个看起来像 Gusto 官方出品的 web app。回公司后拿给工程师、设计师和 leadership 看,几周内迭代成型。
> 🗣️ "why can't we bring this power into the hands of our customers? Why do they have to wait for me? Why do they have to wait for Gusto to, you know, build its roadmap and deliver it to our customers?" —— Eddie Kim
> 译:为什么我们不能把这种能力直接交到客户手里?为什么他们非得等我?为什么他们非得等 Gusto 排完 roadmap 再交付给他们?
> 🗣️ "because of this missed flight, like I actually had five hours of uninterrupted time where I could actually try to build this." —— Eddie Kim
> 译:正因为这次误机,我实际上有了 5 小时不被打断的时间,可以真正动手把它做出来。

### 5. 用 Gusto 已有的数据:从"造 web app"进化到"自动化工作流" / Leveraging what Gusto already knows `[10:47–13:49]`
**要点(中文)**: 原型虽酷,却**没用上 Gusto 对客户的了解**(不知道客户是谁、不填充已知数据)。这正是转折点:产品从"帮你造 web app"进化为"**prompt + 我们已有的数据(行业聚合数据 + 单客户在 Gusto 上的行为)→ 为你每周固定流程生成一个自动化**"。每个自动化按"心跳"周期性触发。技术上直接受自托管 agent 启发——Eddie 读源码发现所谓心跳就是"每 30 分钟跑一次 LLM 的 cron job"。但他也指出心跳不确定且贵,于是 Co-Founder 加了**多种触发方式**,能识别出更适合走普通 cron 的任务(如工资单这种要确定性的)。
> 🗣️ "It's just a cron job that runs an LLM every 30 minutes. And that's exactly how it works in Gusto Co-Founder." —— Eddie Kim
> 译:(所谓心跳)不过就是一个每 30 分钟跑一次 LLM 的 cron job——Gusto Co-Founder 也正是这么工作的。
> 🗣️ "there's some things you actually want to be deterministic. And so like payroll, probably one of those things... the heartbeat not being deterministic means it's like probably going to fire." —— Harj Taggar
> 译:有些事你其实是要它确定性执行的,比如工资单大概就是其中之一;而心跳不确定,意味着它"大概会"触发(但你无法保证到底什么时候)。

### 6. 卖给小企业、自动化"工作前的工作" & 从自动化到真·联合创始人 / Selling to SMBs, the work before the work, becoming a true co-founder `[13:49–19:48]`
**要点(中文)**: Gusto 处境独特:客户做的都是每周重复、且明知浪费时间的任务(跑工资前要从 MindBody 导数据、在 Google Sheet 算佣金/小费/工时,再录入 Gusto)——这些"工作前的工作"才最耗时。所以几乎不用"卖",一说就懂,而且小企业主没有大企业那种"怕丢工作"的阻力,是"hard yes"。更进一步,"Co-Founder"之名意味着它要**主动**:提示合规事项、发现你可能符合但不知道的 R&D 税收抵免(真实案例:Cabana Pools 被找回 5 万美元抵免),从"业务流程自动化器"升级为"主动的业务伙伴"。
> 🗣️ "it's all like kind of like this work before the work that takes them a lot of time. And they do like literally every single week." —— Eddie Kim
> 译:真正耗掉他们大量时间的,是这些"工作之前的工作",而且他们每周都要做一遍。
> 🗣️ "They just want to be able to do more with less... anything that you give them that can like save them time... that's a hard yes for them." —— Eddie Kim
> 译:他们只想用更少做更多;任何能替他们省时间的东西,对他们都是一个毫不犹豫的"要"。
> 🗣️ "there was a company called Cabana Pools that like we actually found them. Fifty thousand dollars in R&D tax credit. They didn't really know that that was possible." —— Eddie Kim
> 译:有家叫 Cabana Pools 的公司,我们实际帮他们找出了 5 万美元的研发税收抵免——他们此前根本不知道还有这种可能。

### 7. 早期结果与惊喜用例 & 路线图 / Early results, surprising use cases & roadmap `[19:48–23:37]`
**要点(中文)**: 刚上线就加了 500 家客户;此前有个 20 家客户的"small business council"内测,反馈"惊为天人"——尤其是"能用短信跑整个业务"这一点,Eddie 说他在客户脸上看到了自己当初用 Telegram 的同款表情。惊喜在于很多自动化**与 Gusto 本身业务无关**(下雨就给旅行团客户群发邮件)。路线图:更多渠道(Telegram、WhatsApp,因 SMS 字数受限)、更多 connectors(QuickBooks、Notion、Google Workspace,还有垂直系统如牙科的 Curve Dental);策略是**先观察客户怎么用,再让客户引导 roadmap**。下一版还要向"还没有 EIN(公司)的人"开放——数据模型一开始就是这么设计的,让想创业/有副业的人也能用,长大后再帮你注册 EIN、在加州登记为雇主。
> 🗣️ "we're going to let the customers guide how we evolve the roadmap." —— Eddie Kim
> 译:我们打算让客户来引导这个 roadmap 该如何演进。
> 🗣️ "You could use Gusto Co-Founder even if you don't have an EIN yet." —— Eddie Kim
> 译:哪怕你还没有 EIN(还没正式开公司),你也能用 Gusto Co-Founder。

### 8. 五人十周、无 Jira:AI 时代的团队与纪律 / Five people, ten weeks, no Jira; discipline in an age of abundance `[23:37–32:27]`
**要点(中文)**: 比"造了什么"更炸裂的是"怎么造的":从一次白板会到走完公司级 tier-one 发布,**5 个人(4 工程师 + 1 设计师,含 Eddie 本人)、10 周**。关键不是"改了什么",而是"**没做什么**":没有会议、没有 tech spec、没有 Figma、不写 docs、没有 Jira/sprint planning/retro——只留一个 7×24 常开的 Zoom("permazoom")+ 海量 Claude Code token。设计师写生产级代码、工程师做设计,"craft 退居其次,共同职责就是写和提交代码"。工作流是**先开 PR 再讨论**,大量代码被扔掉也没关系——50% 命中率也远快于先写 PRD/Figma 走审批。AI 让写代码变便宜,但因此**更要有纪律、更要会说"不"**;而"实现本身"是产品讨论中最不可省的输入,光靠会议/文档/前置用研会丢掉大量信息。给小企业的收尾建议:AI 让创业又一次"阶跃式变简单",把合规、福利、HR 这些杂活自动化掉,专注做产品、拉客户、长业务。
> 🗣️ "this was actually built by five people, five AI builders over the course of 10 weeks from start to finish. It was a white boarding session. And 10 weeks later, like we went through a full blown like tier one launch." —— Eddie Kim
> 译:它其实是 5 个人、5 个 AI builder,从头到尾 10 周做出来的;一开始只是一次白板会,10 周后我们就走完了一场彻头彻尾的公司级 tier-one 发布。
> 🗣️ "We didn't have meetings. We didn't have any tech specs. We didn't have any Figma's. We set the goal of like we're not going to write any docs... the only thing that we had was one permazoom... And cloud code. Lots of cloud code tokens." —— Eddie Kim
> 译:我们没有会议、没有技术规格、没有 Figma,还定了个目标"不写任何文档";我们唯一有的,就是一个常开的 Zoom("permazoom"),外加 Claude Code——海量的 Claude Code token。
> 🗣️ "if you do that and like you have a hit rate of 50%, it actually is significantly faster than like trying to like, you know, write a PRD and a Figma and like getting a green light and like all that stuff." —— Eddie Kim
> 译:如果你就这么干,哪怕命中率只有 50%,也比去写 PRD、做 Figma、等审批放行那一整套要快得多。
> 🗣️ "you have to be much more disciplined than before... there's actually a lot of information you lose when you don't actually have the implementation in front of you." —— Eddie Kim
> 译:你必须比以前更有纪律;而当你面前没有真正的实现时,你其实会丢掉大量信息。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **消灭空白画布**:不要一上来给用户开放式对话框。用你对用户/场景的了解,把入口做成"我建议帮你自动化 X(你每周都在做的那件事),要吗?"的引导式建议。
- [ ] **押注 IM 触发、去后台化**:让核心操作能通过短信/Slack/Telegram 完成审批与触发,而非"登录一个新 dashboard";把精力投在让 agent 更聪明,而不是堆 UI。
- [ ] **在自己产品里找到"记录系统"式的护城河数据**:确保 agent 真正调用你独有的行业聚合数据 + 单用户历史行为——没用上专有数据的 agent 谁都能抄。
- [ ] **区分确定性 vs. 概率性任务**:给 agent 配"多触发器":要确定性/成本敏感的走普通 cron,探索性的才走 LLM 心跳;别让每 30 分钟跑一次 LLM 成为默认(又慢又贵)。
- [ ] **找"工作前的工作"作为切入点**:去问目标用户"哪件事你每周都做、明知浪费时间、还得手动搬数据"——那就是最好卖、最易感知价值的第一个自动化。
- [ ] **用 vibe coding 压缩 0→1**:小团队、常开语音、先开 PR 再讨论、敢扔代码;拿"可运行的实现"而非文档去做产品决策;同时刻意练习"说不",别因为造得便宜就什么都塞进去。
- [ ] **让 agent 从"执行"走向"主动"**:除了自动化用户点名的任务,主动发现用户不知道该做但该做的事(合规、可申领的补贴/税收抵免),这是从工具升级为"co-founder"的关键。

## 🔑 关键术语 / 概念
- **Blank canvas problem(空白画布问题)** — 通用 agent 能力越强,普通用户越因"什么都能做"而无从下手,导致只当搜索引擎用。解法是从用户已在做的具体任务反向引导。
- **Glorified search engine(美化版搜索引擎)** — 指绝大多数人使用 AI 的现状:一问一答、顶多做点调研/摘要,并未进入真正的 agentic 自动化。
- **Heartbeat(心跳)** — agent 定时自触发机制;本质是"每 30 分钟跑一次 LLM 的 cron job",不确定且成本高,适合探索性任务而非确定性任务。
- **The work before the work(工作前的工作)** — 一项核心业务动作(如"跑工资单")之前那些耗时的准备工作(导数据、算表格),往往才是自动化价值最大的地方。
- **System of record(记录系统)** — 沉淀了客户核心数据的底层系统(如 Gusto 的 payroll/HR),在其上叠加 agent 层,是难以被复制的数据护城河。
- **Permazoom** — 团队一个 7×24 常开、随进随出的 Zoom 会议,取代传统会议/站会,作为 AI 时代高速协作的唯一"仪式"。
- **cloud code(即 Claude Code)** — 转写口误;Eddie 全程用它做原型与生产开发。文中 "open claw / OpenClaw" 亦为转写口误,指他自托管的一套开源个人 AI agent。

## 🔖 高价值金句时间戳
- `[01:47]` "this like sort of like agentic world that we've been promised has never really materialized for most people out there." — 一句戳破泡沫:agent 对普通人尚未落地,这正是垂直 agent 的机会。
- `[02:41]` "it has a problem, which I call the blank canvas problem." — 全片方法论核心:别给开放式画布,从已知任务引导。
- `[06:18]` "it is really important to still get into the weeds. Like if you're a technical leader, you should be coding." — 技术负责人别只"读到",要亲手做。
- `[07:17]` "why can't we bring this power into the hands of our customers? Why do they have to wait for me?" — 产品灵感的原点:把 vibe coding 的能力交到客户手里。
- `[10:47]` "It's just a cron job that runs an LLM every 30 minutes." — 把 agent 神秘感祛魅:核心其实极简。
- `[23:52]` "this was actually built by five people... over the course of 10 weeks from start to finish." — AI 时代产品速度的具体样本:5 人 10 周做出公司级发布。
- `[26:15]` "the only thing that we had was one permazoom... And cloud code. Lots of cloud code tokens." — 去流程化协作的极简配方。
- `[28:52]` "you have to be much more disciplined than before." — 代码变便宜后,纪律与"说不"的能力反而更值钱。
