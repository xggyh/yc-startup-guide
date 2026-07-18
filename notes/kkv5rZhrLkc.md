# 十亿分之一:用「分步走」战略把硬科技做成 40 亿美元公司 / BillionToOne Is Solving One of Biotech's Hardest Problems

> **来源**: [BillionToOne Is Solving One of Biotech's Hardest Problems](https://www.youtube.com/watch?v=kkv5rZhrLkc) · Y Combinator · 2026-04-06 · 时长 20:49
> **讲者**: 主持 Jared Friedman(YC 合伙人,SPEAKER_02);嘉宾 Oguzhan "Ozan" Atay(联合创始人/CEO,SPEAKER_01)、David Tsao(联合创始人,SPEAKER_00)
> **一句话定位**: 一家生物科技公司如何用「先做最省钱、能变现的产品,再拿现金流去攻更大更贵的市场」的分步走策略,从半张实验台起步做到上市 40 亿美元——对任何想做「大愿景 AI Agent」但一上来就烧钱的创始人都是一堂反直觉的路径课。

## 🎯 TL;DR(中文核心要点)
- **分步走(step-by-step)是核心战略**:同一套底层技术(检测血液中游离 DNA),他们从「产前基因检测(最省钱、能马上变现)→ 晚期癌症 → 早期癌症 → 全人群癌症筛查」分四步走。先用能赚钱的产品养活团队,再用现金流去攻「holy grail」级难题,而不是一次性融 10 亿去赌终极目标。
- **把难的领域问题转化成可计算的问题**:产前/肿瘤 DNA 极其稀释(十亿分之一),PCR 扩增会引入巨大噪声。他们在扩增前往样本里掺入**已知的合成 DNA**当标尺,反推每个位点被引入了多少误差,再从数据里减掉——「把一个困难的生物学问题变成了近乎简单的数学问题」。这就是给系统装「可测量的基准/标尺」的思路。
- **产品再好,进不了客户面前也是零**:上线两个月只有 1 个医生用户。CEO 开紧急会,三周内逼销售负责人招 5 个 rep、周末培训、周一上岗;并改走「患者→医生」的间接获客,把 CTA 前移到患者端。
- **有牵引力(traction)才招得到好人**:好的销售/科学家「只有在有牵引力时才愿意加入」;先做出一点成绩,人才才会来。
- **要的是「跨学科的人」,不是「跨学科的团队」**:一个人同时懂数据分析和实验化学,把「实验→分析→再实验」的迭代闭环压进一个人身上,效率提升一个数量级。
- **「公司里养很多小创业」的组织结构**:每个产品由一位跨学科 PI 带 2–3 人的小组端到端负责,直接向两位创始人汇报、无官僚阻塞、迭代极快。
- **资源受限反而是优势**:正因为一开始融不到 10 亿、作为首次创业者也不敢赌,才被逼出「分步走」这条更稳、更快见成果的路。
- **用「压力是一种特权(pressure is a privilege)」筛选和留住愿意啃硬骨头的人**。

## 🧭 适合谁 / 什么时候看
- 想做「大愿景、长周期、重研发」产品的 AI Agent / 硬科技创始人——尤其是那种忍不住想一步到位做「终极通用 Agent」的人。
- 正在纠结「先做窄而能变现的垂直产品,还是直接冲最大市场」的早期创始人。
- 有很强技术但卖不出去、或产品好却进不了客户面前的团队(销售/分发困局)。
- 想学「如何组织小而全栈、迭代飞快的研发团队」的技术型 CEO。

## 📝 分段精读

### 1. 针尖对麦芒:要解决的问题 / Finding One Mutation in Billions `[00:00–02:10]`
**要点(中文)**: 人体所有组织(包括母体内的胎儿、体内的肿瘤)都会把 DNA 碎片释放到血液里。很多疾病只差一个碱基对,而目标 DNA 在数十亿分子中只有几个——这是极端的「大海捞针」问题,也是公司名字「Billion to One」的由来。他们现在一年处理 60 万+样本,约占 20% 市场份额,去年上市估值超 40 亿美元。
> 🗣️ "you're looking for one base pair that's different out of billions, and that's where the Billion to One name came from." —— David Tsao (SPEAKER_00)
> 译:你要在数十亿个碱基对里找出那一个不同的——「十亿分之一」这个名字就是这么来的。

### 2. 从实验室点子到 40 亿美元公司 / From Lab Idea to a $4B Company `[02:10–03:05]`
**要点(中文)**: 惊人的是,公司 2017 年申请 YC 时的核心想法,和今天上市公司的核心一模一样:通过测序母体血液里天然存在的胎儿 DNA 碎片来做产前基因检测,并相信它终将被普遍采用。在当时这是个「激进」的想法。启示:一个足够对的核心洞察,可以支撑一家公司走完从 idea 到 IPO 的全程。
> 🗣️ "the core idea behind Billion to One is the same as when they applied to YC back in 2017." —— Jared Friedman(旁白)
> 译:Billion to One 背后的核心想法,和他们 2017 年申请 YC 时是同一个。

### 3. 让它成为可能的突破:把生物问题变成数学问题 / The Breakthrough — Turning Biology Into Math `[03:05–05:15]`
**要点(中文)**: 目标 DNA 又稀又少,而放大信号必须用 PCR 扩增,但扩增本身会引入巨大噪声,把微弱信号淹没。他们的巧招:在任何扩增发生**之前**,往样本里掺入**已知的合成 DNA**。因为知道自己加了什么,就能反推出扩增在各基因组位点引入了多少误差,再用机器学习把这些噪声从最终测序数据里减掉,还原样本最初的真实状态。对做 AI 系统的人:这就是「先埋入可验证的基准信号,再用它来度量并扣除系统性误差」——评测集、ground truth、可观测性的本质。
> 🗣️ "That converts a difficult biology problem to almost a simple mathematical problem." —— Oguzhan Atay (SPEAKER_01)
> 译:这就把一个困难的生物学问题,转化成了一个近乎简单的数学问题。
> 🗣️ "These synthetic DNA allow us to know how much amplification happened at different genomic locations... So then we can remove those errors from the sequencing data." —— SPEAKER_01
> 译:这些合成 DNA 让我们知道不同基因组位点各被扩增了多少……于是我们能把那些误差从测序数据里减掉。

### 4. 白手起家造出第一个产品 / Building the First Test From Scratch `[05:15–07:30]`
**要点(中文)**: 两位创始人本是各自读 PhD 的老同学(Ozan 在斯坦福,David 在莱斯),一个电话就开干了。他们能第一个做成,是因为**跨越了学科断层**:懂数据、能看出数据被如何污染的人,通常不懂产生数据的化学;他们把两边打通了。第一个实验室连一整张实验台都没有,和另一家创业公司的朋友合用半张台子,连买试剂都因为「你有银行账户吗」被供应商为难。
> 🗣️ "People who understand chemistry tend to be not the kind of data scientists and bioinformaticians that analyze the data. We were able to... bridge that gap." —— SPEAKER_01
> 译:懂化学的人往往不是分析数据的那类数据科学家/生信人员,而我们能把这道鸿沟接上。

### 5. 只有一个客户:销售危机 / One Customer and a Sales Crisis `[07:30–08:55]`
**要点(中文)**: 第一笔 30 万美元融资花了六个月、还是一次一万地凑,极其艰难。产品上线两个月后,还只有 1 个医生每周送一两个样本——这是「做了两年、通过审批、终于上线却几乎没用户」的至暗时刻。CEO 的反应不是继续等,而是开紧急会:三周内招 5 个销售、周末培训、周一上岗;并改打「患者→医生」的间接获客(能说服患者、也能说服医生,问题只是**进不到他们面前**)。这一招把回收率做到「五分之一寄回」,也才终于让好的销售愿意加入——因为有了牵引力。
> 🗣️ "When we talk with patients, we can convince them. When we talk with physicians, we can convince them, but we are not getting in front of them." —— Oguzhan Atay (SPEAKER_01)
> 译:我们跟患者谈能说服他们,跟医生谈也能说服他们——问题只是,我们根本进不到他们面前。
> 🗣️ "They really only want to join a company if there's traction." —— SPEAKER_01
> 译:好的人才,只有在公司有牵引力时才真的愿意加入。

### 6. 实验室内部:如何真正运转 / Inside the Lab: How It Actually Works `[08:55–12:10]`
**要点(中文)**: 一天处理上千样本时,「样本登记」(把血样录入系统、保证身份不错乱)反而成了整条流水线的瓶颈——于是他们上了 AI 和计算机视觉重做这一步,项目叫「60 秒登记」。关键工程手法:给每个样本的序列打上专属「条形码」再混在一起测序,数据里一看到那个 barcode 就知道属于哪个患者。多数样本走「happy path」自动出报告,少数疑难病例甚至叫上 20 人一起讨论。启示:找到你系统里真正的瓶颈(常常不是你以为的那个核心算法),用自动化/AI 去打通它。
> 🗣️ "this actually became the bottleneck of all of our processes. So we had to incorporate AI and computer vision to accelerate this." —— SPEAKER_01
> 译:这一步反而成了我们所有流程的瓶颈,于是我们不得不引入 AI 和计算机视觉来提速。

### 7. 用同一技术进入癌症:选对 MVP 的顺序 / Detecting Cancer & the Step-by-Step MVP `[12:10–13:50]`
**要点(中文)**: 本质上「胎儿游离 DNA」和「肿瘤游离 DNA」没有区别,同一套技术两边都能用。但**先做哪个**至关重要:他们成立一年就定下「产前 → 晚期癌症 → 早期癌症」的顺序。如果一开始就冲肿瘤,几乎不可能拿下那次「初步成功的商业化」,而正是那次商业化带来的资源,才让他们能造新测试、改进老测试。这就是「选对最小可行产品」的价值——不是选最性感的,而是选**最能先跑通、先带来现金流**的那个。
> 🗣️ "it was very important to actually select the right problem, the right minimal viable product to work on." —— Oguzhan Atay (SPEAKER_01)
> 译:选对问题、选对那个最小可行产品来做,真的极其重要。

### 8. 团队、路线图与「资源受限反而是优势」/ Team, Roadmap & Why Constraints Help `[13:50–20:49]`
**要点(中文)**: 组织上,他们招的是「跨学科的**人**」而非拼凑「跨学科的**团队**」——把「实验→分析→再实验」的闭环压进一个人身上,效率提升一个数量级;每个产品由一位 PI 带 2–3 人小组端到端负责、直接向创始人汇报、无官僚阻塞,等于「在大公司里养很多小创业」。路线图上,第三步是术后微小残留病(MRD)检测,第四步是全人群早筛——癌症检测的圣杯。而他们能走到这里的根本原因,恰恰是**资源受限**:作为首次创业者,他们知道自己永远融不到「零收入还要烧 10 亿美元」的钱,所以被逼出了分步走这条路。文化上用「压力是一种特权」筛人留人。
> 🗣️ "We're not looking to build an interdisciplinary team here. We're actually looking for interdisciplinary people." —— David Tsao (SPEAKER_00)
> 译:我们要的不是搭一个跨学科的团队,而是找到跨学科的人本身。
> 🗣️ "it almost creates this interesting structure where we have many startups within the larger company." —— SPEAKER_01
> 译:这几乎形成了一种有意思的结构——在一家大公司里养着很多个小创业。
> 🗣️ "Being resource limited is sometimes very helpful... you would have to raise more than a billion dollars... without generating a single dollar of revenue. And as first-time founders, we knew that... we could never do that." —— Oguzhan Atay (SPEAKER_01)
> 译:资源受限有时反而很有帮助……(要一步到位)你得在零收入的情况下融超过 10 亿美元,而作为首次创业者我们清楚,自己根本做不到。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **给你的「大愿景」拆一条分步走路线**:明确「最省钱、最快能变现」的那个窄产品是什么,先靠它跑通商业化和现金流,再用收入去攻更大更贵的目标——不要一上来就为终极 Agent 融一大笔、烧到没收入。
- [ ] **为你的 Agent 装「合成 DNA 标尺」**:在系统里预埋已知答案的评测集/ground truth/金丝雀样本,用它实时度量并**扣除**模型的系统性误差,把「玄学调 prompt」变成可测量、可计算的问题。
- [ ] **别只优化产品,先解决「进不到客户面前」**:设计一条能真正把你产品送到决策者面前的分发路径(必要时走间接获客,把 CTA 前移到真正会转发/推荐的人身上)。
- [ ] **用一点早期牵引力去撬动招聘**:先做出可展示的成绩,再去招那些「只在有 traction 时才愿意加入」的顶尖人才。
- [ ] **招「跨学科的人」而非拼团队**:优先找能独自跑通「产品↔评测↔prompt/模型↔工程」整个闭环的全栈型建设者,把迭代周期压到最短。
- [ ] **用「公司内小创业」结构组织研发**:每条产品线交给 2–3 人的小组端到端负责、直接向你汇报、清掉官僚阻塞,让迭代速度成为护城河。
- [ ] **主动识别真正的瓶颈**:定期找出拖慢整条流水线的那一步(往往不是核心模型),用自动化/AI 去打通它。

## 🔑 关键术语 / 概念
- **cell-free DNA(游离 DNA)** — 各组织(含胎儿、肿瘤)释放到血液中的 DNA 碎片,是这套检测技术的原料。
- **Needle-in-a-haystack / one in a billion** — 目标 DNA 在数十亿分子中只有几个,信噪比极端,是核心技术挑战与公司命名来源。
- **PCR 扩增噪声 & 合成 DNA 标尺(QCT, quantitative counting templates)** — 扩增放大信号也放大噪声;掺入已知合成 DNA(QCT)作标尺以度量并扣除各位点偏差,把生物问题转成数学问题。
- **Barcoding / 样本条码** — 混样测序前给每个样本的序列打专属条码,数据里靠条码把序列归回对应患者。
- **Minimal Viable Product(最小可行产品)的「顺序选择」** — 不是选最性感的,而是选最能先跑通、先带来现金流的那个,作为分步走的第一步。
- **MRD(minimal residual disease,微小残留病)** — 术后扫描查不到、但仍残留的微量肿瘤 DNA;路线图第三步。
- **Liquid biopsy(液体活检)** — 通过一管血而非组织切片检测癌症。
- **Interdisciplinary people(跨学科的人)** — 把多学科能力集于一人,压缩迭代闭环,而非拼凑多人团队。

## 🔖 高价值金句时间戳
- `[04:27]` "That converts a difficult biology problem to almost a simple mathematical problem." — 把难问题转成可度量、可计算的问题,是这套技术(也是好 AI 系统)的精髓。
- `[08:58]` "we are not getting in front of them." — 产品再能打,进不到客户面前就等于零;分发和产品同等重要。
- `[13:45]` "select the right problem, the right minimal viable product to work on." — 选对 MVP 的**顺序**,是分步走战略成败的关键。
- `[15:47]` "having that iterative cycle within one scientist actually accelerates the work... by an order of magnitude." — 把迭代闭环压进一个人,效率提升一个数量级——全栈建设者的价值。
- `[19:02]` "Being resource limited is sometimes very helpful, right?" — 融不到大钱的约束,反而逼出了更稳更快见成果的分步走路径。
- `[19:53]` "We have a saying that... pressure is a privilege." — 用使命与挑战筛选、留住愿意啃硬骨头的人。
