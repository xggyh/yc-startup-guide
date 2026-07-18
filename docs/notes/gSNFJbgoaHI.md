# 如何从零打造 AI 原生服务公司 / How to Build an AI-Native Services Company

📄 **[点此查看全文转录 / Full transcript »](../transcripts/gSNFJbgoaHI.md)**

> **来源**: [How to Build an AI-Native Services Company](https://www.youtube.com/watch?v=gSNFJbgoaHI) · Y Combinator · 2026-06-03 · 时长 11:22
> **讲者**: Charlie Warren（YC Visiting Partner,Startup School 单人讲授)
> **一句话定位**: 讲清一种全新创业范式——不做 co-pilot 工具、而是用 AI 直接"交付结果"重做保险/税务/法律等万亿级服务行业;为想创业的 AI Agent 工程师提供选市场、组团队、做产品、定价、算 P&L 的完整 playbook。

## 🎯 TL;DR(中文核心要点)
- **卖"结果"而不是卖"工具"**:AI-native 服务公司直接把外包工作的产出交付给客户,而不是造一个客户内部自己用的 co-pilot;客户只关心最终产物,不关心你怎么做出来的。
- **选市场看四个新特征**:低信任(工作本就外包)、任务级低判断(大部分步骤可自动化)、高智力门槛(整体活儿要够难)、监管反而是护城河(合规拉高门槛与竞争壁垒)。
- **用 Sam Altman Test 做体检**:自问"模型变强,我的服务是变强还是被商品化(commoditize)?"——你要在"变强"那一侧。
- **创始团队三要素**:领域熟练度(domain fluency,买家很挑剔且常在监管行业)、模型熟练度(model fluency,知道前沿模型今天能做什么并顺着曲线设计)、运营严谨度(operational rigor,吞吐/周期/SOP)。
- **产品的本质是"人是界面、产品让人非线性放大"**,与传统软件相反;把吞吐量和周期时间当成产品指标来追踪,像追踪 DAU 一样。
- **Variance(输出不一致)是生死问题**:客户因为输出不稳定炒掉你,比因为你慢一点、贵一点快得多。
- **警惕"早期需求陷阱"**:头几个 pilot 客户务必只签一小撮,否则被服务压垮、永远靠堆人、做不出可规模化产品。
- **定价对标人力成本而非软件**:优先按单量(per return/claim/loan)或按结果定价;绝对不要成本加成(cost-plus)或直线低价抢单。押注"AI operating leverage"把毛利做到 50%+、且 TAM 是纯软件的 2–3 倍。
- **不要买一家老服务公司再套 AI**:PMF 买不来,legacy 就是 legacy;除非为快速拿到监管牌照(如保险牌照),否则自建几乎总是更好。

## 🧭 适合谁 / 什么时候看
- 正在考虑创业、且技术底子在 AI/Agent 的工程师——尤其在纠结"做工具型 SaaS 还是做交付结果的服务公司"。
- 想切入税务、审计、保险、按揭、法律、医疗/物流某环节等"高价值、已外包"传统行业的创始人。
- 已在跑软件产品、但增长困于"卖 seat/token"、想理解"卖 outcome"商业模式与 P&L 结构的团队。
- 注意:讲者明确说这是给"还没开始的人"的 playbook,不是给已在运营公司的人。

## 📝 分段精读

### 1. 什么是 AI 原生服务公司 / Intro to AI Services Companies `[00:00–01:01]`
**要点(中文)**: 下一个十年最大的公司里,有一批根本不是软件公司,而是被 AI 从零重做的服务公司(保险公司、律所等)。关键差别:交付"结果"给客户,而不是造一个客户内部自用的 co-pilot。市场是万亿级(税务、审计、保险、法律、部分医疗),这个机会两年前还不存在,是模型进步解锁的。整个领域仍处早期,变化很快。
> 🗣️ "Some of the biggest companies of the next decade won't be software businesses at all. They'll be services companies like insurance carriers and law firms, rebuilt from scratch with AI doing most of the work." —— Charlie Warren
> 译:下一个十年里最大的一批公司根本不会是软件公司。它们会是像保险公司、律所这样的服务公司,用 AI 承担大部分工作、从零重建而成。
> 🗣️ "companies provide the outcome to the customer versus build a co-pilot that the customer uses internally"
> 译:这类公司是把"结果"直接交付给客户,而不是造一个让客户在内部自己用的 co-pilot。

### 2. 选对市场(含 YC 当下看好的赛道) / Picking the Right Market `[01:01–03:43]`
**要点(中文)**: 常规选市场建议依然成立(要能做十年、要真心热爱客户/市场/技术难题之一),但 AI 服务的好市场有四个独特新特征:①低信任——工作本已外包,你是在替换供应商而非改变客户行为,"在预算已经在的地方出现";②任务级低判断——能拆成小块,且大部分步骤可自动化,人类判断集中在少数环节;③高智力门槛——整体工作要够难,难到需要"模型+人"才能完成,所以你才是在交付客户愿意接受的结果;④监管反而是好事——更高预期与法律问责拉高门槛与护城河(举例 Panacea 为生物/医疗科技做 FDA 合规服务)。已验证的好赛道:税务、审计、保险、按揭、部分医疗、部分物流——但别把自己限死在 X 上大家常聊的那几个。
> 🗣️ "You're displacing a vendor, not asking the customer to do something fundamentally different... You're showing up where the budget already lives and doing the work." —— Charlie Warren
> 译:你是在替换一个供应商,而不是要求客户去做根本不同的事……你是出现在预算本来就在的地方,把活儿干了。
> 🗣️ "The overall work has to be hard. Hard enough that models plus humans are needed to act."
> 译:整体工作必须够难——难到需要"模型加人类"才能完成。

### 3. Sam Altman 测试 / The Sam Altman Test `[03:43–04:35]`
**要点(中文)**: 判断模型进步会不会颠覆你的业务的方法:自问"模型越强,我的服务是越强、还是被商品化?"——你要站在"越强"那一侧。要警惕的领域:任何涉及设备与现场人工的活儿——你一旦拥有并运营实体资产,软件的毛利数学就失效,很难产生真正杠杆(留给机器人创始人)。还有一条诚实体检:你用人到底是因为工作真需要人类判断,还是在用人力掩盖产品缺陷?要诚实,别用真人去糊产品的短板。
> 🗣️ "You should ask yourself, as the models get better, does your service get stronger? Does the model itself commoditize you? You want to be in the first camp." —— Charlie Warren
> 译:你该问自己:随着模型变强,你的服务是变得更强,还是模型本身把你商品化了?你要待在第一种阵营里。
> 🗣️ "are you using humans because the work genuinely needs judgment, or are you compensating for product gaps?"
> 译:你用人,是因为工作真的需要判断,还是在弥补产品的缺口?

### 4. 对的创始团队 / The Right Founding Team `[04:35–05:28]`
**要点(中文)**: 通用建议成立——和你已经共事、了解的人一起干;如果是单人,去找你共事过的最优秀的人,你会惊讶有多少人答应。AI 服务创始人共有三种特质:①领域熟练度(domain fluency)——直接经验最好,后天学的也行;你面对的是挑剔、常在监管行业的买家,必须"浑身透着可信度";②模型熟练度(model fluency)——知道前沿模型今天能做什么,并把产品设计成能随模型变强而受益;此处技术不可替代,很多人低估它;③运营严谨度(operational rigor)——方差、吞吐、周期、SOP,虽然不性感,但你本质在跑一个运营,产品就在运营里。举例 General Legal Team(YC 投的 AI 原生律所)把轮班制引入服务以缩短周期、吸引最好的律师。
> 🗣️ "You're selling to skeptical buyers in often regulated spaces. You have to bleed credibility." —— Charlie Warren
> 译:你卖给的是常处在监管行业里的、满腹狐疑的买家。你必须浑身都在渗出可信度。
> 🗣️ "You need to know what frontier models can do today and design the product to ride the curve as they get better."
> 译:你得知道前沿模型今天能做什么,并把产品设计成能随着它们变强而顺势乘上这条曲线。

### 5. 做产品:人是界面,方差是生死线 / Building the Product & Variance `[05:28–07:08]`
**要点(中文)**: AI 服务的产品结构与软件相反:人是面向客户的界面,产品不是;产品的作用是让人的工作非线性放大。这改变了做产品的一切。①用运营思维——找到瓶颈、为瓶颈而建;吞吐量与周期时间现在就是产品指标,要像追 DAU 一样追踪。②方差(输出不一致)是存亡问题——客户因为输出不稳定炒掉你,比因为慢一点/贵一点快得多;不一致摧毁信任,信任崩了就流失。③人在环路(humans in the loop)必须非线性扩张——如果收入只跟你加的人数同步增长,就有大麻烦;而且这些人也是你的用户,他们得爱用你的软件。开头可以做不可规模化的事,但最终必须规模化——"把流程自动化本身就是产品"。
> 🗣️ "Customers will fire you for variance faster than they will fire you for being a bit slower or a bit more expensive than the incumbents." —— Charlie Warren
> 译:客户会因为方差而炒掉你,比因为你比在位者慢一点、贵一点而炒掉你要快得多。
> 🗣️ "The human is the interface of the customer, not the product. The product helps the humans scale their work non-linearly."
> 译:人才是面向客户的界面,产品不是。产品的作用是帮助这些人把工作非线性地放大。

### 6. 早期需求陷阱 / The Early Demand Trap `[07:08–07:53]`
**要点(中文)**: 最大的坑:刚起步时很容易签下一大批 pilot 客户,但这会迅速压垮你的服务能力,让你造不出可规模化的产品、只能一直堆人——这是一个字面意义上的陷阱。建议:把最初的 pilot 客户限制在一小撮,抵住诱惑别签太多太快。这些 pilot 是用来"学"的,不要过早标准化;用它们找出"AI 给你独特杠杆"的地方 vs. "只是自动化显而易见之事"的地方,据此快速造产品。"pilot 就是产品。"
> 🗣️ "It's easy to sign up a lot of pilot customers when you're just starting out but it can quickly overwhelm your ability to serve them... It is a literal trap." —— Charlie Warren
> 译:刚起步时很容易签下一大堆 pilot 客户,但这会迅速把你服务他们的能力压垮……这是一个字面意义上的陷阱。
> 🗣️ "For the first handful of customers, don't try and standardize too early. Use those pilots to learn."
> 译:对最初的一小撮客户,别急着标准化。用这些 pilot 去学习。

### 7. 如何给 AI 服务定价 / How to Price AI Services `[07:53–08:41]`
**要点(中文)**: 你要卖的是"结果",不是 seat 或 token。定价比传统软件更难,因为你不是在和别家软件竞争,而是直接和人力成本(内部或外包)竞争。可选方案:①按单量定价(per return/claim/loan)——最干净、最好解释;②按结果定价——激励对齐得漂亮,但对你自己的业务更难预测。两种要坚决避免的策略:成本加成(cost-plus)会永久锁死你的上限,别用;直线低价抢单会让你的工作显得廉价、疑似低质。要"按价值定价"。
> 🗣️ "You have to sell outcomes, not seats or tokens. The pilot is the product." —— Charlie Warren
> 译:你必须卖结果,而不是卖席位或 token。pilot 就是产品。
> 🗣️ "Cost plus pricing caps your upside permanently. Don't do it. Straight line undercutting makes your work seem cheap and potentially low quality. Price on value."
> 译:成本加成定价会永久锁死你的上限,别这么干。直线低价抢单会让你的工作显得廉价、甚至疑似低质。要按价值定价。

### 8. P&L 走查与 AI 运营杠杆 / P&L Walkthrough & AI Operating Leverage `[08:41–10:27]`
**要点(中文)**: 这些公司在 P&L 上决生死。结构:收入 − COGS = 毛利;毛利 − OPEX = 营业利润。收入相对最容易——你能签合同,但能否可重复交付取决于产品与流程,早期按月会很"跳",没关系。COGS 从第一天就要死磕,三块成本:模型成本、托管成本、人在环路——每一块都要有数字、有趋势线、有明确负责人;对零毛利/负毛利的 pilot 要高度警惕,好玩但别上瘾。核心押注:产品越做,成本越低,毛利越好——这叫 "AI operating leverage(AI 运营杠杆)"。OPEX=研发+销售+G&A。你会比想象中更快地被"营业利润"评判。机会所在:传统服务公司毛利顶到约 30%,纯软件/agent 公司毛利更高但 TAM 常更小;这类服务公司的赌注是——用 AI 运营杠杆逼近软件级毛利(50%+),而市场是软件的 2–3 倍。不必马上到位,但轨迹要可信。
> 🗣️ "The core bet here is the more the product is built, the lower the cost... I call this AI operating leverage." —— Charlie Warren
> 译:这里的核心押注是:产品做得越多,成本就越低……我把这叫做 AI 运营杠杆。
> 🗣️ "AI operating leverage gets you closer to software margins, say 50% plus, on a market that's two to three times bigger than software." —— Charlie Warren
> 译:AI 运营杠杆能让你逼近软件级毛利,比如 50% 以上,而且是在一个比软件大两到三倍的市场上。

### 9. 别想着"买进去" / Don't Buy Your Way In `[10:27–11:22]`
**要点(中文)**: 有运营背景的创始人常想买一家现成服务公司、套上 AI、抄近路拿到收入——这通常是陷阱。唯一说得过去的理由:你需要快速拿到监管护城河(如保险牌照)。除此之外几乎行不通,因为 PMF 买不来——legacy 服务公司就是 legacy,它在指标、招聘、绩效上的预期都不同,套个 AI 不会立刻改变这些现实。自建几乎总是优于买。总结:把"流程当产品、产品当流程",避开这些坑,你就有机会造出一家世代级公司。
> 🗣️ "You just can't acquire a product market fit. Legacy service businesses are legacy... Building is almost always better than buying." —— Charlie Warren
> 译:你根本买不来产品市场契合。老牌服务公司就是老牌的……自建几乎总是优于购买。
> 🗣️ "focus on the process as the product and the product as the process, you have a chance to create a generational company"
> 译:把流程当作产品、把产品当作流程,你就有机会造出一家世代级的公司。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **用四特征筛选你的赛道**:列 2–3 个你懂的行业,逐一打分——是否低信任(已外包)、任务级低判断(可自动化占多数)、高智力门槛、有监管护城河;选全中的那个。
- [ ] **对每个候选做 Sam Altman Test**:写下"下一代模型发布后,我的服务是变强还是被商品化"的答案;砍掉会被商品化的方向。
- [ ] **重构产品指标**:把 Agent 系统的评估从"demo 好不好看"改为吞吐量、周期时间、单位成本(model+hosting+human)三条趋势线,并给每条指定负责人。
- [ ] **把 Variance 当头号 bug**:为你的 Agent 输出建立一致性/质量的自动评测与人审关卡,量化输出方差并设 SLO;variance 是流失第一因。
- [ ] **限流 pilot**:最初只接一小撮客户,用他们区分"AI 独特杠杆点"与"显而易见的自动化点",快速迭代,拒绝提前标准化。
- [ ] **按 outcome / 单量定价并测算对人力的替代成本**:立一张 P&L 模型,验证"产品越做、COGS 越低"能否把毛利推向 50%+;放弃 cost-plus 与低价抢单。
- [ ] **自建而非收购**:除非为快速拿监管牌照,否则不要买老服务公司套 AI;把工程重心放在"自动化流程=产品"上。

## 🔑 关键术语 / 概念
- **AI-native services company** — AI 原生服务公司:用 AI 从零重做的传统服务业务,向客户交付"结果/产出",而非提供内部使用的工具。
- **Outcome vs. co-pilot** — 交付结果 vs. 副驾工具:前者你把活干完交付,后者只是给客户一个内部自用的辅助工具;本视频主张做前者。
- **四大市场特征** — 低信任(low trust)、任务级低判断(low judgment at the task level)、高智力门槛(high intelligence threshold)、监管为护城河(regulation as moat)。
- **Sam Altman Test** — 自问"模型变强时,我的服务是变强还是被商品化",用来判断业务是否会被模型进步颠覆。
- **Domain / Model / Operational fluency** — 创始团队三要素:领域熟练度、模型熟练度、运营严谨度。
- **Variance(方差)** — 服务输出的不一致;此处是存亡级问题,直接摧毁客户信任并导致流失。
- **Humans in the loop** — 人在环路:参与交付的人既是产能也是产品用户,收入必须相对人数非线性增长。
- **Early demand trap(早期需求陷阱)** — 过早签太多 pilot 客户,被服务压垮、只能堆人、造不出可规模化产品。
- **COGS / OPEX / Operating income** — 销货成本(模型+托管+人力)/ 运营费用(研发+销售+G&A)/ 营业利润;AI 服务公司会很快被营业利润评判。
- **AI operating leverage(AI 运营杠杆)** — 产品越完善、单位成本越低,从而把服务毛利推向软件级(50%+),而 TAM 是软件的 2–3 倍。

## 🔖 高价值金句时间戳
- `[00:09]` "Some of the biggest companies of the next decade won't be software businesses at all." — 定调:下个十年的巨头是被 AI 重做的服务公司,不是软件公司。
- `[01:49]` "The first is low trust." — 好市场第一特征:工作已外包,你替换供应商而非改变客户行为。
- `[03:35]` "Does the model itself commoditize you?" — Sam Altman Test 的核心一问,决定你是否会被模型进步吞掉。
- `[06:12]` "Customers will fire you for variance faster than they will fire you for being a bit slower or a bit more expensive." — 方差比慢和贵更致命,是流失第一因。
- `[06:47]` "The biggest challenge facing founders here is what I'll call the early demand trap." — 提醒:pilot 别签太多太快,否则永远被人力困住。
- `[07:14]` "You have to sell outcomes, not seats or tokens. The pilot is the product." — 商业模式与定价的根本转向:卖结果。
- `[09:14]` "The core bet here is the more the product is built, the lower the cost." — AI 运营杠杆的一句话本质,毛利改善的引擎。
- `[10:50]` "Building is almost always better than buying." — 别买老公司套 AI,PMF 买不来,自建几乎总是更优。
