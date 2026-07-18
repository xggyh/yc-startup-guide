# 用 AI Agent 在规模上抓欺诈:Variance 的隐身创业实录 / This Startup Catches Fraud at Scale

📄 **[点此查看全文转录 / Full transcript »](../transcripts/JF6XIixstmQ.md)**

> **来源**: [This Startup Catches Fraud at Scale](https://www.youtube.com/watch?v=JF6XIixstmQ) · Y Combinator · 2026-03-31 · 时长 31:23
> **讲者**: 主持 Jared Friedman(YC Managing Partner,SPEAKER_00);嘉宾 Karine Mellata(Variance 联合创始人 / CEO,W23,SPEAKER_01)
> **一句话定位**: 一个把"合规/反欺诈"这类高价值、原本靠人工审核的枯燥流程,用 AI Agent 彻底自动化的真实案例——对想做垂直 Agent、卖给企业客户的创始人,示范了产品架构、"why now"、以及冷启动第一个企业客户的完整路径。

## 🎯 TL;DR(中文核心要点)
- **垂直 Agent 的最小构件只有三个**:合规文档 / SOP(判断规则)、你自建的工具、内外部数据。把这三样拼起来,就能自动化复杂的 KYC / KYB / 内容审核——不要一上来就造复杂的"决策层"。
- **Agent 取代的是"规则引擎 + 分类器 + 人工"三段式补丁系统**。分类器不再需要(Agent 直接读 SOP 对图片/非结构化数据推理),人工推理也大幅减少,形成一个能在对抗环境里快速自愈的闭环。
- **不要造 100% 端到端决策层**。Agent 负责 triage 99% 的简单案子,剩下 1% 最复杂的留给人——所以你还必须给人做一个"很好的调查可视化面板",这才是产品的关键一环。
- **数据接入是最难的技术活,不是模型**。企业数据散在 5–10 个系统、无 schema、petabyte 级,有些甚至藏在只给人用的老 UI 后面——他们的第三种接入方式就是"开个浏览器、爬那个人工审核工具再推理"。
- **"访问开放网络"是让整件事跑通的最后一块拼图**。人工分析师本质上是"Google 一下再判断",Agent 能查开放网络后才能补全整张滥用关系图。
- **Why now 讲得极清楚**:公司 pre-ChatGPT 成立,GPT-4 在 YC batch 期间发布,一次模型更新把成本降 10 倍、性能大涨——技术演进恰好把一个"半不可能"的问题变成可解。
- **12 人团队、只有 5 个工程师**,跑 Fortune 500、petabyte 数据,靠 AI coding maximalism:每个工程师 3 块屏跑 coding agent,人人是"一小队 AI 的经理";连非技术的 CSM 都能用 Cursor 自主上线简单需求。
- **企业冷启动靠两点**:第一个客户先信"创始人",而不是信产品;问题空间必须"on fire"(正在着火),否则没人愿赌一个没有背书的小 startup。首单 IAC 花了 8 个月。

## 🧭 适合谁 / 什么时候看
- 想做**面向企业(尤其风控/合规/信任安全)的垂直 AI Agent**,正在纠结产品架构与技术护城河的创始人。
- 处在**冷启动阶段、要拿下第一个大企业客户**、且自己就是唯一销售的技术型创始人。
- 想理解"**为什么这类任务现在才能自动化**(why now)"、以及如何用小团队 + coding agent 放大产出的人。
- 需要一份**创始人韧性 / 抗压**真实样本(CEO 被卡车撞、bus factor = 1)的人。

## 📝 分段精读

### 1. 走出隐身 & 为什么藏了三年 / Coming Out of Stealth & Why Stay Secret `[00:00–02:26]`
**要点(中文)**: Variance 为风控与合规打造"专用 AI agents",自动化内容审核、欺诈审核、身份审核,客户包括 GoFundMe、Fortune 50 等,本次走出隐身并宣布 2100 万美元 A 轮。之所以隐身三年,是因为客户数据与议题极度敏感:他们造的是"坏人常用、但给好人用"的系统,过度营销这些用例反而会催生更多滥用。这对做敏感领域 Agent 的创始人是个反直觉信号——低调本身可以是产品的一部分。
> 🗣️ "The phrase I like to use is that we're building the systems that are often used by the bad guys, but we're building them for the good guys." —— Karine Mellata
> 译:我常用的一句话是——我们造的是那些常被坏人使用的系统,但我们是为好人而造。

### 2. 你早就用过它:GoFundMe、身份与企业验证 / Real Use Cases You've Already Touched `[02:26–07:44]`
**要点(中文)**: 具体展示了 Agent 落地的三类高价值场景:GoFundMe 每个募捐发起前都被 Variance 校验(比如 Charlie Kirk 去世后冒出上百个假冒家属的募捐,要靠身份、历史行为、募捐页信息等行为信号 + 平台条款来判定);零工平台的骑手身份核验(自拍 + 驾照 + 公司 SOP);以及最难的 KYB——要在充满壳公司、跨国代理的巨大关系图里,找出某个节点是否处于受制裁国、是否有负面媒体。原本全靠人工的活,现在能一致地全自动完成。
> 🗣️ "That work used to be done by human panelists, and now can be fully automated in a much more consistent manner." —— Karine Mellata
> 译:这些工作过去由人工评审小组来做,现在可以用一种一致得多的方式完全自动化。

### 3. Agent 怎么搭:三个构件 + 数据 / How the Agents Work: Three Building Blocks `[07:44–12:07]`
**要点(中文)**: 作者把 Agent 架构讲得极其精炼——只需要三块积木:合规文档 / SOP(规定要验什么)、自建工具、数据(内外部)。数据一半是客户内部数据(Variance 擅长把散乱的非结构化数据抽进自己的数据存储),一半是外部数据(100+ 国家的商业登记库 + 开放网络)。她特别点出:"访问开放网络"才是让这个长期难自动化的问题跑通的最后一块拼图,因为人工分析师的核心动作就是"Google 一下再用判断力"。而真正最难的技术挑战是数据接入本身:数据散在 5–10 个系统、无 schema、petabyte 级,有的还只藏在给人用的老 UI 后面。
> 🗣️ "There's really only three building blocks that you need. So you have the compliance documents, the standard operating procedure... Those are the only building blocks you need to automate complex KYC, complex KYB, complex content review." —— Karine Mellata
> 译:你真正需要的只有三块积木:合规文档、标准作业流程(SOP)……要自动化复杂的 KYC、KYB、内容审核,你需要的就只有这三块。
> 🗣️ "Access to the web was one of the final nodes that made this whole problem... really hard to automate." —— Karine Mellata
> 译:能访问网络,是让这整个问题(此前极难自动化)得以跑通的最后几个节点之一。

### 4. 为什么是现在:从"补丁系统"到自愈系统 / Why This Only Works Now `[12:07–16:26]`
**要点(中文)**: 过去规模化解决欺诈靠"确定性系统的拼凑"——规则引擎(交易超一千美元就怎样)+ 分类器(只擅长某一种滥用)+ 人工(懂上下文但慢且不一致)。而欺诈是最动态的对抗环境,这套三段式的反馈闭环快不起来,做不到自愈。创始人从一开始就固执于"系统里不能有任何低效节点":如今 Agent 能凭 SOP 对图片和非结构化数据推理,直接判定"这可能是拒付欺诈",既能实现规则引擎的特征、又不再需要专门分类器和人工推理,形成规模化下真正变革性的自愈系统。真实战果:选举期间靠"实体间关系上下文"识别出单个分类器绝无可能发现的、国家支持的复杂欺诈团伙。
> 🗣️ "Michael and I were always really, really, really stubborn about making the system have no nodes that were inefficient." —— Karine Mellata
> 译:Michael 和我一直非常非常固执地坚持:系统里不能存在任何低效的节点。
> 🗣️ "You don't need a specialized classifier for it, and you don't need human reasoning anymore. So you have this fully self-healing system." —— Karine Mellata
> 译:你不再需要专门的分类器,也不再需要人工推理——于是你得到一个完全自愈的系统。

### 5. 小团队,大产出:AI coding maximalist / Tiny Team, Huge Output `[16:26–20:18]`
**要点(中文)**: 一个关键的产品教训:他们最初固执地想做"端到端决策层",以为要把决策做到极精准、像个 API 被调用——事后证明错了。因为 Agent 能吃掉最简单的部分、triage 掉 99% 的案子,剩下 1% 恰恰是最复杂、必须人来审的,所以你反而必须做一个"很好的调查可视化工具"给人用。团队只有 12 人、5 个工程师,却服务 Fortune 500、处理 petabyte 数据:每个工程师 3 块屏跑 coding agent,人人像"管一小队 AI 的经理";连完全非技术的 CSM 都能把简单需求直接丢给 Cursor agent、几小时后自主上线,不用惊动工程团队。
> 🗣️ "AI agents are able to take on the simplest part of the workflow, so they're able to triage 99% of cases, that 1% is usually going to be the most complex cases that need to be reviewed by a human. And you need a really good dashboard." —— Karine Mellata
> 译:AI agent 能承接工作流里最简单的部分,triage 掉 99% 的案子;那剩下的 1% 往往是最复杂、需要人来审的案子——所以你需要一个非常好的仪表盘。
> 🗣️ "Every engineer is going to have three monitors with their coding agents running... in terms of output, everyone is a manager of a small team of AI agents." —— Karine Mellata
> 译:每个工程师都有三块屏幕跑着自己的 coding agent……就产出而言,每个人都是一小队 AI agent 的经理。

### 6. 起源与第一个客户 / Origin Story & First Customer `[20:18–24:57]`
**要点(中文)**: 两位创始人在 Apple 反欺诈团队共事(她是数据工程师,Michael 是 ML 工程师),对行业解决方式有强烈不满,于是决定申请 YC。拿下第一个企业客户的两条心法:一是客户先信"创始人"——相信这对创始人有能力、真懂他们的问题,再把这份信任转化为对产品的信任(因为产品会随首个客户需求大幅演化);二是问题空间必须"on fire",否则没人愿意赌一个毫无背书的小 startup。首单是上市公司 IAC(旗下 Care.com、Angie 等),痛点是海量营销内容合规审核无法用正则或传统分类器表达,只能靠外包 BPO 人工做,严重拖累增长——他们是第一个敢说"我们能用大模型做这件事"的公司,足足花了 8 个月才拿下。
> 🗣️ "Your first customer really believes in the founders first. They believe in the founders' ability to be able to solve their problem." —— Karine Mellata
> 译:你的第一个客户,首先相信的是创始人本身——相信这对创始人有能力解决他们的问题。
> 🗣️ "We needed to land on a problem space... which was on fire. It needed to be on fire because... if it wasn't on fire, then there was no reason to go and trust this really small startup." —— Karine Mellata
> 译:我们必须找到一个正在"着火"的问题空间。它必须在着火,因为如果它没着火,就没有理由去信任一个这么小的初创公司。

### 7. 被卡车撞后的复原 / Recovering from Getting Hit by a Truck `[24:57–29:36]`
**要点(中文)**: 2024 年 7 月公司高速增长(月收入接连翻倍),TrustCon 大会后极度疲惫,她在自行车道被卡车撞倒,脊椎和腿骨折、住院十天无法行走。当时全公司只有工程师 + 她一人做全部销售与客户关系——CEO 的 bus factor 是 1。Michael 到病房探望,两人沉默良久后,他用"这会是我们 IPO 电影里很好的一幕"来化解;也一度怀疑这是否是公司的终点。但两人都强烈感到"这不是终点"。最直接的教训:必须"scale me"(把创始人这个单点复制/降依赖)。对创始人是一堂关于单点故障与韧性的血泪课。
> 🗣️ "The CEO has a bus factor of one. We only have engineers and we have me that's running all the sales and the customer relationships." —— Karine Mellata
> 译:CEO 的 bus factor 是 1。我们只有工程师,还有我一个人在跑全部销售和客户关系。
> 🗣️ "He laughed and said, well, this is going to make a really good scene in our IPO movie." —— Karine Mellata
> 译:他笑着说:嗯,这会成为我们 IPO 电影里非常好的一幕。

### 8. 坚持一个大想法 / Sticking to One Big Idea `[29:36–31:23]`
**要点(中文)**: 与很多 YC 创始人"带着假设进来、反复 pivot 追风口"相反,他们从第 0 天就有极强的信念:亲眼见过问题,整家公司就是那个初始假设的展开。驱动力不是"为创业而创业",而是一种把稀有技能用于行业公益的"责任感"——他们要解决的是这个特定问题,而不是随便什么问题。这份笃定既让他们在低谷时觉得"不可能就此结束",也深深打动客户:客户看到的是一对真正想解决自己日常痛点、且有能力解决的创始人。
> 🗣️ "We didn't want to just start a company for any problems. We wanted to solve that problem." —— Karine Mellata
> 译:我们并不想只是为了随便某个问题去创业。我们想解决的,是那个特定的问题。
> 🗣️ "We always felt a really strong sense of duty to put our very specific and quite rare pair of skillsets to the good of the industry." —— Karine Mellata
> 译:我们始终有一种强烈的责任感,要把我们这对非常具体、相当稀有的技能组合,用在造福这个行业上。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **用"三块积木"重构你的 Agent**:把领域知识写成清晰的 SOP / 合规文档,配上自建工具 + 内外部数据,先跑通;别一开始就造复杂的"决策层"或自训分类器。
- [ ] **别追求 100% 自动化**:设计 Agent triage 掉简单的 95–99%,把最难的 1–5% 连同一个"高质量调查/审核面板"交给人——这个人机协作面板是产品护城河,不是附属品。
- [ ] **把"数据接入"当成头号工程投入**:预设客户数据散在 5–10 个系统、无 schema、甚至只在人用的老 UI 后面;准备好 API / reverse-ETL / 浏览器爬取多种接入方式。
- [ ] **给 Agent 开放网络访问能力**:很多关键判断信号只在开放网络的非结构化数据里,补上这块才能"补全整张关系图"。
- [ ] **验证你的"why now"**:明确说清是哪一次模型/能力跃迁,把你的问题从"半不可能"变成"可解"——这是投资人和企业客户都会追问的。
- [ ] **冷启动锁定一个"正在着火"的问题 + 一个愿赌你的旗舰客户**:接受首单周期以月计(他们用了 8 个月),用创始人信任而非成熟产品去撬动。
- [ ] **用 coding agent 放大小团队产出**:让每个工程师做"一队 AI 的经理",同时保留全量 PR review;把简单需求下放给非技术同事 + coding agent 自主上线。
- [ ] **消除创始人单点故障**:趁早"scale me"——把销售/客户关系的知识与流程文档化、可交接,别让 bus factor 停在 1。

## 🔑 关键术语 / 概念
- **KYC / KYB** — Know Your Customer / Know Your Business,身份 / 企业合规核验;KYB 需在壳公司、代理、UBO(最终受益人)构成的关系图中排查制裁、洗钱、负面媒体等风险。
- **SOP(Standard Operating Procedure)** — 标准作业流程 / 合规文档;是喂给 Agent 的"判断规则"来源,取代了传统需要人手写正则或训练分类器的环节。
- **Self-healing system(自愈系统)** — 能在对抗性、动态环境中以极紧反馈闭环自我修正的系统;Agent 让规则引擎 + 分类器 + 人工的三段式补丁演化为单一自愈闭环。
- **Deterministic patchwork(确定性补丁系统)** — 规则引擎 + 专用分类器 + 人工评审拼凑而成的传统风控架构,反馈慢、不一致。
- **Triage(分诊/分流)** — Agent 先处理掉大批简单案子,把最复杂的少数留给人工审核。
- **Bus factor** — "巴士系数",指团队能承受多少关键成员突然缺席;此处 CEO 的 bus factor = 1,是致命单点风险。
- **Reverse ETL** — 把数仓/系统里的数据回流对接到业务系统的一种数据集成方式,是 Variance 接入客户数据的方式之一。
- **KYB graph / 滥用关系图** — 把实体及其关联(公司、代理、身份、行为)连成的图;单一节点(如受制裁国、负面媒体)即可放大整体风险,需 Agent 跨开放网络补全。

## 🔖 高价值金句时间戳
- `[01:28]` "We're building the systems that are often used by the bad guys, but we're building them for the good guys." — 敏感领域创业的定位与价值观一句话,也是"为何隐身"的注脚。
- `[07:44]` "There's really only three building blocks that you need." — 垂直 Agent 架构的极简范式:SOP + 工具 + 数据。
- `[08:00]` "Access to the web was one of the final nodes that made this whole problem... really hard to automate." — 别小看"让 Agent 上网",它常是补全判断链的最后一块拼图。
- `[13:00]` "You don't need a specialized classifier for it, and you don't need human reasoning anymore." — Agent 时代"why now"的技术本质:一个自愈闭环取代规则+分类器+人工。
- `[16:40]` "They're able to triage 99% of cases, that 1% is usually going to be the most complex... you need a really good dashboard." — 不要追求全自动;人机协作面板才是产品关键。
- `[21:35]` "Your first customer really believes in the founders first." — 企业冷启动第一性原理:先卖创始人,再卖产品。
- `[26:35]` "The CEO has a bus factor of one." — 创始人单点故障的血泪教训,务必尽早"scale me"。
