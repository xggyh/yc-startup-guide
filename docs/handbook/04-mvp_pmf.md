# 第 4 章 · 做 MVP 与找到 PMF / MVP & Product-Market Fit

> 这一章要解决的是创业最危险的中段:你已经选定方向,但还没证明"世界真的需要它"。对 AI Agent 创始人来说,这一段尤其凶险——模型让你几天就能做出一个惊艳 demo,却也让"demo 惊艳"和"客户敢在生产里依赖你"之间的鸿沟前所未有地大。本章把 YC 这批讲者反复讲的东西拧成一条主线:**用最小的东西验证真需求 → 把 demo 做成可靠产品 → 用真实信号度量 PMF,而不是自欺**。

---

## 核心原则 / Core Principles

### 唯一的立项准绳:有人愿意为它掏真钱 / The Only Test That Matters: Someone Pays Real Money

AI 时代做 MVP,最容易犯的错是"先纠结点子好不好、市场够不够大",然后闷头把产品做完再去找人用。这批讲者的共识正好相反:**点子和市场都不是准绳,唯一的准绳是"有没有人愿意为你解决的问题付真金白银"**——甚至在动手之前就先拿到付费承诺(先卖后建)。逻辑很硬:如果问题足够重要,人就会用钱或时间来投票;如果没人愿意付,你多半在解一个"假问题"。常见误区有两个:一是只跟市场的一侧聊(Meesho 第一版只访谈卖家、从没访谈消费者,做出"比商场差、比电商也差"的两头不讨好产品,三个月关停);二是相信用户嘴里说的问题,而不去现场蹲点看他们真实在用什么"土办法"。

> 🗣️ "It's never about the idea. It's about if somebody is willing to pay you money for it." —— Varun Vummadi(Giga,《Two IIT Engineers…》)
> 译:关键从来不是点子,而是有没有人愿意为它付钱给你。

> 🗣️ "If it's an important enough problem, people would pay. Either with money or with time... Otherwise, like, you're just solving a fake problem." —— Varun Vummadi(Giga)
> 译:如果问题足够重要,人们就会付费——要么付钱,要么付时间;否则你只是在解决一个假问题。

**🤖 对 AI Agent 创始人**: 做新 Agent 功能前,先给目标客户报一个预估价、拿到口头/书面付费承诺再开发,把"是否有人愿付真钱"当成唯一立项门槛。别靠"市场很大"选赛道——像 Giga 从微调业务里发现"客服 + 编程"两类客户增长最快才顺势掉头一样,让方向从你现有客户里长出来,而不是从 PPT 里想出来。

### 先卖"结果",别卖"工具" / Sell the Outcome, Not the Tool

传统 SaaS 卖的是"席位、用量、一个客户自己用的 co-pilot";而这批 AI 应用公司反复强调:**你要卖的是"已经解决的问题(outcome)",客户不关心你怎么做出来的,只关心最终产物**。这不是措辞游戏,它直接改写了两件事:一是定价——不再是 20 美元/月的软件,而是"每份合同 500 美元"这种按价值定价;二是 TAM——天花板从"座位数 × 月费"变成"这些岗位的全部薪资总和",往往大 10 到 1000 倍。误区是把 Agent 当成又一个卖 token 的工具:那样你会被压在软件的毛利与心智里,既做不大也守不住。

> 🗣️ "You have to sell outcomes, not seats or tokens. The pilot is the product." —— Charlie Warren(《How to Build an AI-Native Services Company》)
> 译:你必须卖结果,而不是卖席位或 token。pilot 就是产品。

> 🗣️ "you're not selling the installation of software, you're selling an outcome... you're selling that you have solved a problem." —— Bob McGrew(《The FDE Playbook》)
> 译:你卖的不是软件的安装,而是一个结果……你卖的是"你已经解决了这个问题"。

**🤖 对 AI Agent 创始人**: 把你的 MVP 定义成"交付一个可验证的结果",而不是"给用户一个界面去自己操作"。定价对标它替代的人力成本(内部或外包),优先按单量(per case / claim / return)或按结果收费;坚决避开成本加成(会永久锁死上限)和直线低价抢单(让你的活儿显得廉价可疑)。同时直接问客户"你想怎么付"——Casetext 发现客户宁愿要可预测的按座位年费,也不要更便宜的按用量。

### MVP 的使命:用最短路径把人拽到 Aha 时刻 / The MVP's Job Is to Drag People to the Aha Moment

一个好的 MVP / demo 不是把你能做的东西堆出来给人看,而是**在客户心里"制造渴望"——让他看一眼就想伸手抓住、带进自己的生活**。这是判断你有没有命中真痛点的最直接标准。要做到这点,产品得干两件事:第一,首屏就露出真实产品(截图、≤2 分钟录屏、甚至一个内嵌的 prompt bar 当场生成结果),别用抽象的图标动画,"没人会为看不见的东西 book demo";第二,用最短路径把人送到价值点,**拆掉一切过早的注册墙——"你能设下的最大障碍,就是先登录/先创建账号"**。反过来,当律所看完一场 demo 就下单、当那个曾嘲讽"AI 更多是 artificial 而非 intelligent"的管理合伙人当场被现场检索震住,你就知道自己做对了。哪怕在硬科技里,一个"喷火的小推力器"这样的最小可信 demo,也足以撬开第一张支票。

> 🗣️ "a really good demo is something where you show it to the customer and you are creating desire in that customer for what you're doing. They have to see what you're doing and just want to reach out and grab it and bring it into their life." —— Bob McGrew(《The FDE Playbook》)
> 译:真正好的 demo 是:你演示给客户看,在客户心里制造出渴望。他们看到你在做的东西,就想伸手抓住、把它带进自己的生活。

> 🗣️ "You want people to get to the aha moment... this is like the biggest blocker you could possibly put up is just log in or create an account." —— Aaron Epstein(《Why Your Startup Website Isn't Converting》)
> 译:你要让人尽快到达 aha 时刻……而你能设下的最大障碍,就是"先登录/先创建账号"。

**🤖 对 AI Agent 创始人**: 设计一个"零摩擦试用 → 当场看到 Agent 交付结果"的路径,把登录挪到导出/分享那一步(用户已投入后再要账号)。首屏放 prompt bar 或可交互 demo 捕获用户意图并立即出结果。用一个可反复演示的端到端故事化 demo 驱动开发:每加一个特性都追问"它如何帮到走完整流程的用户、如何与已有特性协同",并以"客户是否想伸手抓住"作为真痛点的验证标准。

### Demo 到可靠是两条命:evals 才是真护城河 / From Demo to Production: Evals Are the Moat

这是 AI Agent 创业最反直觉、也最值钱的一课:**造出一个 60–70% 准确、能骗过 VC、能签下几个试点的 demo 并不难;难的是把它做到生产可靠**。LLM 像人一样会"没喝咖啡就犯错",一上真实业务就崩,所有兴奋随之瓦解。真正把 demo 变成产品的,不是模型,而是**评估集(evals)+ 验证回路(verification loop)**:把关键判断设计成可客观打分,愿意"为通过这些 eval,在单个 prompt 上不眠不休磨两周",从 60% 抠到 97%——大多数人 60% 就放弃了,这恰恰是你的护城河。与之并列的两件事:一是**方差(输出不一致)是存亡问题**,客户因为输出不稳定炒掉你,比因为你慢一点、贵一点快得多;二是别停在"能跑",**部署、后端、安全这"最后一公里"才是最值钱、也最被忽视的 20%**。

> 🗣️ "the biggest qualification for success here is whether you or whoever is working on the prompts in your company is willing to spend two weeks sleeplessly working on a single prompt to try to pass these evals." —— Jake Heller(Casetext,《From Idea to $650M Exit》)
> 译:这里最大的成功资格,就是你(或你公司里写 prompt 的人)是否愿意为通过这些 eval,不眠不休地在单个 prompt 上磨两周。

> 🗣️ "your agent is only as good as the feedback that you provide." —— Madhav Jha(Emergent,《AI Is Unlocking Millions Of New Builders》)
> 译:你的 Agent,只能好到你给它的反馈那么好。

**🤖 对 AI Agent 创始人**: 第一天就把 eval 流水线当一等公民——把 Agent 的输出建成可自动打分的验证回路(自动测试/裁判/CI 校验),把客户投诉和"用户干的最蠢的事"持续变成回归测试。为方差设 SLO,把吞吐量、周期时间、单位成本当成产品指标去追(像追 DAU 一样)。注意:长任务的 eval 是**超线性**难题(20 分钟的任务远不止比 2 分钟难 10 倍),而且随着 Agent 从"增强单任务"走向"端到端交付完整工作产品",瓶颈会从单任务 eval 转移到端到端 eval——提前重投。可以的话,让 Agent 在构建期和部署期共用同一套 infra,消灭"能生成、部署却挂"的最后一公里问题。

### 对问题刚性、对方案弹性:快速证伪 + 分步走 MVP / Rigid on the Problem, Flexible on the Solution

找 PMF 几乎从来不是一次到位,而是一连串 pivot。指导原则是**对要解决的问题极度刚性,对解决方案极度弹性**——Meesho 十一年做到"版本五",使命从未变、方案全换。配套两条纪律:一是**快速证伪比快速验证更重要**,idea 不行就三个月砍掉,别在一个方向上耗一两年;二是**分步走(step-by-step)——先做"最省钱、最快能变现"的那个窄 MVP**,用它跑通商业化和现金流,再用收入去攻更大更贵的目标,而不是一上来就为"终极通用 Agent"融一大笔烧到没收入。判断"该不该 pivot"的最靠谱先行指标,是**你自己已经不再相信手头这件事能成**;而真要 pivot,手上要有一组备选点子而非孤注一掷。别把"技术上要做半年"当成躲进车库不见客户的借口——用最糙的版本(套别人 API、bookmarklet、人工先跑)先把自己变成用户。

> 🗣️ "be problem first... be very rigid with your problem and be very flexible with your solution." —— Vidit Aatrey(Meesho,《How Meesho Became India's Biggest Shopping App》)
> 译:问题优先——对你的问题极度刚性,对你的解决方案极度灵活。

> 🗣️ "The actual leading indicator that maybe you should pivot is you just stop believing that what you're working on is going to work out." —— Pete Koomen(《Startup Advice: AI GTM, Pivoting & How To Hire》)
> 译:真正提示你该 pivot 的先行指标,是你自己已经不再相信手头这件事能成了。

**🤖 对 AI Agent 创始人**: 给每个方向设一个"三个月证伪闸门":做出能跑的 Agent demo、拉几十上百个真实用户试用,若明显不成立就快速换方向。给你的大愿景拆一条分步走路线,先靠一个能变现的窄场景(BillionToOne 先做最省钱的产前检测,再用现金流攻癌症早筛)跑通,别一步到位。把 Agent 抽象成"可迭代的 policy / markdown 文件 → 撬动某个 KPI(如解决率/CSAT)"的度量闭环,让"改 markdown、跑 eval、看 KPI 从 40% 到 90%"成为你迭代方案的主循环。

### 真正的 PMF 长什么样:power users 与"无限需求" / What Real PMF Actually Feels Like

很多创始人把"注册量"当 PMF,这是致命误判——**有几十万浅层用户 ≠ PMF**。真正的 PMF 藏在一小撮 power users 身上:他们每天用 15–20 次、一边骂你缺功能一边离不开你。它在数据上的样子是:**连续多月零营销预算、每月翻倍、极高留存**;在体感上则像被市场"拖着走"——"感觉我们有无限的需求",一断服务客户立刻来电话。反面教材是 **PRR(pilot recurring revenue,试点循环收入)**:很多号称 10M ARR 的公司,扒开是付了半年高价、根本不会转化的试点,一场"大灭绝"在酝酿。还要区分两种"卖不出去":产品能打却"进不到客户面前"是分发问题(要设计出真能把产品送到决策者面前的路径),而客户用了却不肯付费,则说明你没找对真正靠它赚钱的那撮人。

> 🗣️ "it literally feels like we have infinite demand... it's moved from being in this experimental AI bucket into we are reliant on this for core work." —— Max Junestrand(Legora,《How This 25-Year-Old Built A $675M Legal AI Startup》)
> 译:那感觉简直就像我们有无限的需求……它已经从"实验性 AI"这一档,变成了"客户的核心工作离不开它"。

> 🗣️ "for the next 10 months we spent zero rupees on marketing... we doubled every single month... unless you see product market fit you never know what product market fit is." —— Vidit Aatrey(Meesho)
> 译:接下来 10 个月我们在营销上花了零卢比……却每个月翻一倍……在你真正见到 PMF 之前,你永远不知道 PMF 是什么。

**🤖 对 AI Agent 创始人**: 用"重度使用频次 + 留存 + 主动反馈"而非注册数判断 PMF;去扒"谁用你的 Agent 用得最狠",把产品聚焦到这撮 power users 的核心痛点上。盯紧"试点 → 付费"的真实转化率,别把不会转化的 PRR 当 ARR 上报自欺。同时投资"交付"这件事——onboarding、培训、必要时派前置部署工程师(FDE)贴身让客户真正用起来:你的产品不只是屏幕上的像素,还包括围绕它的一切。

### 别过早规模化:先做不可规模化的事,再抽象成"高速路" / Do Things That Don't Scale — at Scale

早期最诱人的陷阱是"看到一点需求就急着堆人/签一堆客户去规模化"。这批讲者一致反对:**先做那些不可规模化的事,把它做到规模化,再抽象成产品**。FDE 打法的精髓正是"doing things that don't scale at scale"——FDE 去客户现场铺一条通往目标的"砂石路",产品团队再看着它想清楚"如何泛化到接下来 5 个、10 个客户",把砂石路修成"高速公路"(抽象层要上提一级,防止过度特化)。与之对应的纪律是躲开**"早期需求陷阱"**:刚起步很容易签下一大批 pilot,但这会迅速压垮你的服务能力,让你造不出可规模化产品、只能一直堆人。规模化的正确时序是:先 human-in-the-loop 的混合自主,把单位经济做正,再放量——"每单位亏钱就很难规模化"。学习速度,而非 TAM,才是早期最该优化的东西。

> 🗣️ "The FDE model effectively is doing things that don't scale at scale." —— Bob McGrew(《The FDE Playbook》)
> 译:FDE 模式的本质,就是把那些不可规模化的事,规模化地去做。

> 🗣️ "It's easy to sign up a lot of pilot customers when you're just starting out but it can quickly overwhelm your ability to serve them... It is a literal trap." —— Charlie Warren(《How to Build an AI-Native Services Company》)
> 译:刚起步时很容易签下一大堆 pilot 客户,但这会迅速把你服务他们的能力压垮……这是一个字面意义上的陷阱。

**🤖 对 AI Agent 创始人**: 最初只接一小撮 pilot,把它们当"学习样本"而不是急着标准化;用它们区分"AI 独特杠杆点"和"只是自动化显而易见之事"。设计"砂石路 → 高速路"流水线:单客户方案先跑通,再拉多个相似客户一起评审、抽象出可泛化的产品层(像 Palantir 的 ontology 那样把每客户的特化留在可定制层)。若走"全栈/替客户干活"路线,盯住一个公开的自动化率指标并逼它上升,而不是靠招人堆营收——先让 Agent 吃掉更多流程,再扩人。规模化前先确认单位毛利为正。

---

## ⚡ 本章行动清单 / Action Checklist

- [ ] **先卖后建**:对目标客户报价、拿到付费承诺(付钱或明确投入时间)再动手做,把"有人愿付真钱"当唯一立项门槛;做双边产品就同时访谈两侧,并去现场观察真实行为而非听自述。
- [ ] **把 MVP 定义成"交付一个可验证的结果"**,按它替代的人力成本定价(优先按单量/按结果),避开成本加成与低价抢单;直接问客户"你想怎么付"。
- [ ] **打造零摩擦到 Aha 的路径**:首屏露出真实产品或可交互 demo,拆掉一切过早的注册墙,把登录挪到导出/分享那一步;用"客户是否想伸手抓住"验证真痛点。
- [ ] **第一天就搭 eval + 验证回路**:关键判断可客观打分,把客户投诉和真实失败样例持续加进 eval,愿意为单个 prompt 从 60% 磨到 97%;为输出方差设 SLO,把吞吐/周期/单位成本当产品指标追。
- [ ] **给每个方向设三个月证伪闸门**,对问题刚性、对方案弹性;给大愿景拆分步走路线,先做最省钱能变现的窄 MVP;pivot 的信号是"你自己已不再相信",手里常备一组备选点子。
- [ ] **用重度使用频次 + 留存 + 主动反馈度量 PMF**,聚焦每天用 15–20 次的 power users;盯紧试点→付费转化率,别把不会转化的 PRR 当 ARR。
- [ ] **别过早规模化**:早期只接一小撮 pilot 当学习样本,先做不可规模化的事再抽象成可泛化产品;先把单位毛利做正(必要时 human-in-the-loop),再放量。
- [ ] **把产品造成"随潮水上涨的船"**:默认模型会持续变强,做那些"新模型一出会更强、而非被吃掉"的东西(GPT-5 测试),护城河押在专有数据、工作流模式、用户行为与交付上,而不是模型能力本身。

## 📚 本章取材视频 / Sources

- [Why Two IIT Engineers Turned Down $550K Jobs To Build A Startup](https://www.youtube.com/watch?v=2Ap1dnv-GXA) — 贡献"唯一准绳是有人愿付真钱""先卖后建""方向从客户里长出来"与 Agent=可迭代 markdown/KPI (`notes/2Ap1dnv-GXA.md`)
- [How to Build an AI-Native Services Company](https://www.youtube.com/watch?v=gSNFJbgoaHI) — 贡献"卖结果不卖席位""方差是存亡问题""早期需求陷阱""pilot 就是产品" (`notes/gSNFJbgoaHI.md`)
- [The FDE Playbook for AI Startups with Bob McGrew](https://www.youtube.com/watch?v=Zyw-YA0k3xo) — 贡献"把不可规模化的事规模化地做""demo 制造渴望""卖 outcome""砂石路→高速路/land & expand" (`notes/Zyw-YA0k3xo.md`)
- [From Idea to $650M Exit: Lessons in Building AI Startups](https://www.youtube.com/watch?v=l0h3nAW13ao) — 贡献"难在做对而非造出""evals 才是护城河""PRR 陷阱""TAM=薪资总和/按价值定价" (`notes/l0h3nAW13ao.md`)
- [How Meesho Became India's Biggest Shopping App](https://www.youtube.com/watch?v=49L8lVe_PVo) — 贡献"对问题刚性对方案弹性""只听一侧的死法""真 PMF 长什么样/power users""快速证伪" (`notes/49L8lVe_PVo.md`)
- [How This 25-Year-Old Built A $675M Legal AI Startup](https://www.youtube.com/watch?v=pHuXCzM2ntU) — 贡献"aha demo 打动怀疑者""无限需求的 PMF 手感""规模化与可靠性(第一次登录是唯一机会)""把产品造成船" (`notes/pHuXCzM2ntU.md`)
- [How Legora Went From YC to $100M ARR in 18 Months](https://www.youtube.com/watch?v=mjmswQurIU4) — 贡献"早期产品不完美但创始人信念带客户上车""端到端 evals 成新瓶颈""护城河=专有数据/工作流/用户行为" (`notes/mjmswQurIU4.md`)
- [Startup Advice: AI GTM, Pivoting & How To Hire](https://www.youtube.com/watch?v=nGLmpKi-jRU) — 贡献"pivot 先行指标=你不再相信""学习速度>TAM""别过早规模化(自动化率)""GPT-5 测试""最糙版本先把自己变用户" (`notes/nGLmpKi-jRU.md`)
- [BillionToOne Is Solving One of Biotech's Hardest Problems](https://www.youtube.com/watch?v=kkv5rZhrLkc) — 贡献"分步走 MVP:先做最省钱能变现的那个""产品再好进不到客户面前也是零""有牵引力才招得到人" (`notes/kkv5rZhrLkc.md`)
- [AI Is Unlocking Millions Of New Builders](https://www.youtube.com/watch?v=8SVocWnDHwE) — 贡献"验证回路是核心壁垒""Agent 只和你给的反馈一样好""为生产而建/最后一公里""后发者需碾压式强产品" (`notes/8SVocWnDHwE.md`)
- [Harshil Mathur: AI Is Compressing Every Moat](https://www.youtube.com/watch?v=X5bABLCuIHA) — 贡献"信念来自客户""难在客户端才是问题、难在别处是护城河""构建趋零、速度是唯一护城河""愿意干十年的问题" (`notes/X5bABLCuIHA.md`)
- [The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ) — 贡献"eval 超线性变难""混合自主→单位经济打平→再规模化""外科手术级选择切入点" (`notes/4EsUaur0nsQ.md`)
- [Why Your Startup Website Isn't Converting](https://www.youtube.com/watch?v=leQ89XSHILw) — 贡献"首屏露出真实产品""5–10 秒讲清价值""冲向 aha、拆掉过早注册墙" (`notes/leQ89XSHILw.md`)
- [Inside The Startup Building Reusable Rockets](https://www.youtube.com/watch?v=2hgjgycOU_0) — 贡献"用最小可信 demo 撬第一张支票""迭代速度即护城河""给创业决策设时间盒" (`notes/2hgjgycOU_0.md`)
