# 打造可复用火箭的创业内幕:从车库到轨道的硬科技创业课 / Inside The Startup Building Reusable Rockets

> **来源**: [Inside The Startup Building Reusable Rockets](https://www.youtube.com/watch?v=2hgjgycOU_0) · Y Combinator · 2026-01-08 · 时长 15:44
> **讲者**: 主持 Aaron Epstein(YC,SPEAKER_01);嘉宾为 Stoke Space 两位联合创始人 Andy Lapsa(CEO,SPEAKER_02)与 Tom Feldman(SPEAKER_00)
> **一句话定位**: 一家做"完全可复用火箭"的硬科技公司,如何用"复用优先架构 + 极速迭代 + 自建工具 + 最小可信 Demo 融资"从零起步——这套方法论对 AI Agent 创始人几乎逐条可迁移。

## 🎯 TL;DR(中文核心要点)
- **从"复用优先"倒推架构**:别人事后想办法回收,他们从第一天就把"可反复飞、快速周转"当成设计约束——对 Agent 而言就是从 day 1 把"可评测、可回滚、可迭代"设进架构,而不是产品跑通后再补。
- **用最小可信 Demo 撬动第一张支票**:他们没有先造整枚火箭,而是用"很少的钱造一个小推力器、让尾焰喷出来",拿这个"极小的已完成部件"去说服天使投资人。Agent 创业同理——先跑通一个窄场景、能看得见的成果。
- **给自己设"时间盒"再 all-in**:辞掉高薪、家里有三个月大的孩子,他们约定"六个月没有实质 traction 就重新评估",用有限风险换取行动的决心。
- **迭代速度就是护城河**:把"一个月一轮"压缩到"一两天一轮";关键手段是**垂直整合**——自己能造每个零件,否则迭代周期被外部供应商卡死。
- **早早自建内部工具**:他们很早决定自研运营系统 "Bolt Line" 并围绕它组织公司,认为这是成功的关键之一。Agent 创始人应尽早自建 eval/日志/数据回流工具链。
- **融资的核心技能是"学会听 no"**:他们严重低估了融资难度、没有人脉、又撞上 COVID;Andy 说最重要的一条建议是 get good at hearing no,在一连串拒绝中守住信念。
- **别死磕分析,要上测试台**:硬的东西无法"分析到完美",最终 rubber meets road,必须尽快真实测试并从失败中快速学习——对应 Agent 的"尽快上线真实用户/真实数据"。
- **conviction 高到"欠世界一个尝试"**:让他们跨出去的,是对想法本身的确信——"不管成不成,这个想法好到必须一试"。

## 🧭 适合谁 / 什么时候看
- 正在做**硬核、长周期、技术风险高**方向(含复杂 Agent 系统)的创始人,想学"如何在没成品时也能推进与融资"。
- 纠结"要不要离开大厂稳定工作去创业"、需要一套**降低下行风险的决策框架**的人。
- 想理解**迭代速度、垂直整合、自建工具**为何是护城河,而不只是"效率优化"的技术型创始人。

## 📝 分段精读

### 1. 开场与使命:把"快速可复用"当作火箭工业的 iPhone 时刻 / Intro & Mission: Rapid Reusability `[00:00–02:18]`
**要点(中文)**: Stoke Space 要做的是"完全且快速可复用"的火箭,目标是降本、提升可用性与可靠性。今天商业发射每年只有约 150 次,且大多被 Starlink 占用,可用性是瓶颈。他们把"能随时上天、随时回到你要的地点"类比成 App Store 时刻——一旦成本与可用性打开,会催生大量此前想都不敢想的新应用。这对平台型创业者是个强提示:**先把底层成本/可用性打下来,生态会自己长出来**。
> 🗣️ "if you have something that can go up and come back to the place where you want it to go, when you want it to go, I think it is like the iPhone app store moment." —— Tom Feldman (SPEAKER_00)
> 译:如果你能造出一个"想去哪儿就回到哪儿、想什么时候飞就什么时候飞"的东西,我觉得那就是 iPhone App Store 时刻。
> 🗣️ "to make the space economy more ubiquitous, more diverse, and to enable some of these new verticals and applications, yeah, cost is a huge barrier." —— Andy Lapsa (SPEAKER_02)
> 译:要让太空经济更普及、更多样、催生这些新的垂直领域和应用,成本是巨大的障碍。

### 2. 为什么第二级会烧毁、以及他们的解法 / Why Stage 2 Fails & Stoke's Solution `[02:18–05:30]`
**要点(中文)**: 行业已能复用第一级(把年发射从十几次推到 150 次),但第二级每次都被扔掉——它以 17,000 英里/时再入、承受 2,700°F 高温。Stoke 的关键洞察是**"从第一天就为复用而设计"**:用液氢流过换热器做主动冷却热盾 + 24 个小推力器控制再入姿态与着陆。这样做的杠杆在于——**用"提升飞行频次"替代"扩建工厂"**,复用把边际成本和产能解耦。迁移到 Agent:把架构设计成"复用/可迭代优先",能让你在不成比例扩张成本的情况下扩大产出。
> 🗣️ "What rapid reusability allows you to do is to scale the flight frequency without having to scale your factories and your test facilities and all of the infrastructure that comes with it." —— Andy Lapsa (SPEAKER_02)
> 译:快速可复用让你能在不扩建工厂、测试设施和一切配套基础设施的前提下,扩大飞行频次。

### 3. 复用优先的设计哲学 & 为什么敢开这家公司 / Reusability-First Philosophy & Deciding to Start `[05:30–07:25]`
**要点(中文)**: 起步时市面上已有 150 多家火箭公司,他们逐一看过,发现**很多只是"PPT 上看不到光明前景"的东西**;而两人都是硬件出身,懂得把 PPT 变成现实要付出什么——这就是差异化。选题方法是"找两人**能力、欲望、待解问题三者的交集**":别人还在扔火箭、且没人以足够的严谨去攻这个问题,而他们自认有解法。离开高薪、拖家带口去创业"感觉极不负责任",于是他们用**时间盒**(六个月无实质 traction 就重估)来把不确定性框住。
> 🗣️ "let's brainstorm some things that sort of like meet in the middle of our Venn diagram of like desires and skills and problems that need to be solved." —— Tom Feldman (SPEAKER_00)
> 译:我们来头脑风暴一些正好落在我们"欲望、技能、待解问题"这三者交集里的事情。
> 🗣️ "a bunch of PowerPoint stuff that didn't seem like it had a very bright future. And we were certainly both hardware people. And so we kind of understood what it would take to take some of those PowerPoint ideas into reality." —— Tom Feldman (SPEAKER_00)
> 译:一堆看不出有多光明前景的 PPT。而我们俩都是实打实的硬件人,所以我们清楚把这些 PPT 想法落地成现实到底要付出什么。
> 🗣️ "Let's give ourselves a time bounded, you know? scenario where like in six months if we don't have any kind of legitimate traction that's gonna be the sort of cue to reevaluate" —— Tom Feldman (SPEAKER_00)
> 译:我们给自己设一个有时间边界的方案——如果六个月内拿不到任何实质性的进展,那就是重新评估的信号。

### 4. 早期发动机开发:最小 Demo 与融资 / Early Engine Dev: MVP Demo & Fundraising `[07:25–10:48]`
**要点(中文)**: 他们没有先造整枚火箭,而是**用很少的钱在集装箱/后院里造一个压力供给的氢氧小推力器,让尾焰真的喷出来**,以此对早期投资人证明"这件小到不能再小的事我们已经做成了"。这就是硬件版的 MVP。融资上他们踩了大坑:**严重低估融资难度**、没有 Rolodex、没有富叔叔、还撞上 COVID 市场冻结,而当时 VC 世界为 SaaS 而生,他们的故事和财务模型完全不同。Andy 给出的最重要一条建议:**learn to hear no**——在一连串拒绝里守住信念与火种。(截至采访已累计融资约 9.9 亿美元。)
> 🗣️ "We knew that with a reasonably small amount of money we could develop a pressure-fed gaseous hydrogen liquid oxygen thruster and be able to show fire coming out the end and say you know hey early investors we want to do this thing. Here's a teeny tiny little piece that we already did." —— Tom Feldman (SPEAKER_00)
> 译:我们知道花不多的钱就能做出一个压力供给的气氢/液氧推力器,让尾焰喷出来,然后对早期投资人说:嘿,我们想做这件大事——这是我们已经做成的极小一块。
> 🗣️ "We wildly underestimated the challenge in raising money. If there's one thing we totally missed on that was it." —— Andy Lapsa (SPEAKER_02)
> 译:我们严重低估了融资的难度。要说我们完全看走眼的一件事,就是这个。
> 🗣️ "get good at hearing no. It is tough to keep it going when all you hear is no after no after no to just keep the conviction and keep the fire alive to keep going." —— Andy Lapsa (SPEAKER_02)
> 译:要练就"善于听到 no"的本事。当你听到的全是一个又一个拒绝时,要撑下去、守住信念、让火种不灭,是非常难的。

### 5. 垂直整合 & 把迭代速度当竞争优势 / Vertical Integration & Iteration Speed `[10:48–12:29]`
**要点(中文)**: 你无法把一切分析到完美,最终必须上测试台。所以**能多快迭代,直接决定了你多快能做成硬事、以及总开发成本**。他们的做法是**尽可能自造每一个零件**——因为一旦零件依赖外部供应商,迭代周期就被别人卡住。为失败预先规划:发动机炸了,要"车间地板上已经有下一台随时能上",于是把"一个月一轮"压缩到"一两天一轮"(去测试台学到东西→拆→开回车间改→再开回测试台装上→继续)。
> 🗣️ "You can't analyze everything to perfection and at the end of the day rubber meets road and you have to test. And so the speed can iterate becomes fundamentally important" —— Andy Lapsa (SPEAKER_02)
> 译:你没法把一切都分析到完美,最终橡胶总要落地——你必须去测试。所以能不能快速迭代,就变得至关重要。
> 🗣️ "if you can't make parts yourself, then your iteration cycle is dependent on an out-of-house supplier." —— Andy Lapsa (SPEAKER_02)
> 译:如果你自己造不了零件,那你的迭代周期就受制于外部供应商。
> 🗣️ "So a one-month cycle is down to a day or two." —— Aaron Epstein(主持,SPEAKER_01)
> 译:于是一个月的周期被压缩到一两天。

### 6. 软件是核心基础设施:自研 Bolt Line / Software as Core Infrastructure `[12:29–14:00]`
**要点(中文)**: 令主持人意外的是——软件不只用在产品里,更用来**运营公司本身**。公司要从"字面意义上的车库"跨越到"给政府送载荷、甚至载人、受 FAA 监管",而这道从车库到规模化的桥"对很多公司是极其痛苦的"。他们要打造能一次次快速周转复飞的载具,于是"零件用了多久?何时做预防性维护?何时非计划维护?"这些问题必须被系统化记录与切分。答案是**很早就决定自研运营工具 Bolt Line 并围绕它组织运营**,并对 AI 让工人录入与信息流转更顺畅感到兴奋。
> 🗣️ "This company has to scale from building things in a literal garage to flying government payloads or even humans on a vehicle that is overseen by the FAA. And somehow you have to bridge from garage to that. And that bridge is often very, very painful for a lot of companies." —— Andy Lapsa (SPEAKER_02)
> 译:这家公司必须从"字面意义上在车库里造东西",一路扩张到把政府载荷、甚至人送上受 FAA 监管的载具。你得想办法架起这座桥,而这座桥对很多公司来说往往极其痛苦。
> 🗣️ "we made the decision very early on we're going to build our own tool to to do all this we're going to base our operations around it and call it bolt line and it's been a big part of our success" —— Andy Lapsa (SPEAKER_02)
> 译:我们很早就决定要自研一套工具来做这一切,把运营围绕它来组织,叫它 Bolt Line——它一直是我们成功的重要一环。

### 7. 通往轨道 & 如果成功会怎样 / Path to Orbit & Changing the World `[14:00–15:44]`
**要点(中文)**: 他们在卡纳维拉尔角历史性的 Complex 14(1962 年 John Glenn 首次美国载人绕地之处)建发射场,同时并行推进一二级发动机资格测试、结构件低温测试、以及"硬件在环"仿真飞行来验证航电与软件栈的鲁棒性。回望起点,让他们跨出去的不是把握,而是**对想法本身的确信到了"欠世界一个尝试"的程度**——不管成不成,这个想法好到必须被一试。这是硬科技创业的情感内核,也适用于任何"非共识但你深信"的 Agent 方向。
> 🗣️ "I got to the level of conviction in the idea that I said, we owe it to the world to try this idea. Whether or not it succeeds, this idea is good enough, it has to be tried." —— Andy Lapsa (SPEAKER_02)
> 译:我对这个想法的确信达到了这样的程度:我说,我们欠世界一次尝试。不管它成不成,这个想法足够好,它必须被试一次。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把"可迭代/可评测"设进 day-1 架构**:像"复用优先"一样,先建好 eval 集、日志回流、回滚机制,再谈功能扩张;别等产品跑通再补测试。
- [ ] **造你的"喷火小推力器"**:在真正做大系统前,先在一个窄场景上做出一个"看得见成果、已完成"的最小可信 Demo,拿它去谈第一批用户/投资人。
- [ ] **给创业决策设时间盒**:约定一个明确的里程碑与期限(如 6 个月的实质 traction 标准),把下行风险框住再 all-in。
- [ ] **把迭代周期当第一 KPI**:量化"从想法到上线验证"的周期,想尽办法把"周/月"压到"天",这比单点性能更像护城河。
- [ ] **垂直整合关键环节**:凡是会卡住你迭代速度的外部依赖(数据、评测、关键模型/工具),尽量自建可控,别让供应商决定你的节奏。
- [ ] **尽早自建内部工具链(你的 Bolt Line)**:把运营、评测、数据切分做成自有系统并围绕它组织团队,而不是拿一堆临时脚本硬撑到规模化。
- [ ] **把"听 no"当技能来练**:提前准备好在一连串融资/客户拒绝中守住 conviction 的机制(节奏、心态、复盘),尤其当你的模型不符合主流 VC 模板时。

## 🔑 关键术语 / 概念
- **Rapid / Full Reusability(快速完全可复用)** — 火箭一二级都能反复回收并快速周转再飞;核心价值是"用提升频次代替扩建产能",把边际成本与产能解耦。
- **Stage 1 / Stage 2(一级/二级)** — 一级把火箭推出大气层后返场着陆;二级继续入轨,过去每次被抛弃——正是 Stoke 主攻的"可复用二级"。
- **Vertical Integration(垂直整合)** — 尽量自造每个零件/工具,避免迭代周期被外部供应商卡住。
- **Bolt Line** — Stoke 自研的运营/制造管理软件系统,用于记录零件寿命、维护、信息切分,支撑从车库到规模化的过渡。
- **Hardware-in-the-loop(硬件在环测试)** — 把真实航电与飞控/GNC 软件集成起来跑仿真任务,验证软硬件栈鲁棒性后再真飞。
- **"Get good at hearing no"** — 把承受连续拒绝、维持信念的能力当作一项可练习的融资核心技能。

## 🔖 高价值金句时间戳
- `[00:26]` "it is like the iPhone app store moment. People are going to come up with like absolutely crazy ideas for how to take advantage of that." — 先把底层成本/可用性打下来,生态会自发涌现。
- `[04:48]` "meet in the middle of our Venn diagram of like desires and skills and problems that need to be solved." — 好选题=能力×欲望×待解问题的交集。
- `[06:20]` "It felt wildly irresponsible, to be honest. Easily the hardest decision that I've ever made personally." — 承认离开舒适区的决定很难,不美化创业。
- `[07:20]` "Here's a teeny tiny little piece that we already did." — 硬件版 MVP:用极小的已完成成果换第一张支票。
- `[08:39]` "get good at hearing no." — 融资最关键的可练技能,是承受拒绝、守住信念。
- `[11:19]` "your overall development timeline and therefore your development cost is tied to how quickly you can iterate." — 迭代速度直接决定时间与成本,是硬科技的护城河。
- `[15:15]` "we owe it to the world to try this idea... it has to be tried." — 非共识方向的情感内核:确信到"必须一试"。
