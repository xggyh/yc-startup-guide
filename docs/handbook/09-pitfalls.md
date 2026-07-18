# 第 9 章 · 常见陷阱与反模式 / Common Pitfalls & Anti-patterns

> 这一章不讲"该做什么",而讲"别人是怎么死的"。把 15 支 YC 谈话里反复出现的失败模式抽出来,你会发现 AI Agent 创始人最常栽的跟头几乎都不是技术不够,而是**判断力被噪音污染**:被"套壳焦虑"劝退、把酷炫 demo 当成产品、把注册量当成 PMF、被 AI 的"能做"绑架去做"不该做"的事、追风口做衍生点子、把试点收入当 ARR、以及在成功后让公司腐坏或把自己变成单点故障。看清这些反模式,比多学一个 prompt 技巧更能决定你能不能活下来。

## 核心原则 / Core Principles

### 反模式一:被"套壳焦虑"和护城河幻觉提前劝退 / Letting "wrapper anxiety" & moat-paranoia talk you out of building

最普遍、也最致命的早期错误,是**在还没有值得防御的东西之前就为护城河焦虑**,或因为产品"看起来像个 ChatGPT 套壳"而不敢动手。YC《七种力量》那期把话说透了:护城河本质是防御性的,是"后来才有的事";早期唯一真正的护城河是**速度**(甚至不在书里的七种力量之内),而它的前提永远是先去解决一个具体的人的存亡级痛点(bxBzsSsqQAM)。Jake Heller 把 CoCounsel 卖了 6.5 亿美元后回望,对"你不就是个套壳"的最好回应是"直接造,一造你就知道它有多难"——两年只做一件事堆出的无数细节,本身就是别人复制不了的壁垒(l0h3nAW13ao)。而《大厂做不好 AI》那期更是直接把"MIT 说 95% 企业 AI 项目失败"翻译成机会:失败的是自建和咨询,外购创业公司的成功率远高——所谓"套壳没护城河"的担忧,答案恰恰藏在客户被训练/配置沉淀后高到无法承受的切换成本里(DULfEcPR0Gc)。

> 🗣️ "the moats come later, like it would be like pretty dumb for somebody to decide not to work on a startup idea because they can't see what the long term moats of that idea could be" —— Jared Friedman, 7 Moats / The Lightcone (bxBzsSsqQAM)
> 译:护城河是后来才有的——因为看不清一个点子的长期护城河就决定不做它,是相当蠢的。

> 🗣️ "So all these people who are worried that these like chat GPT rappers won't have moats, like that's the moat." —— Jared Friedman, Enterprise Is Bad At AI (DULfEcPR0Gc)
> 译:所以那些担心"ChatGPT 套壳没有护城河"的人——喏(客户投入训练后的切换成本),这就是护城河。

**🤖 对 AI Agent 创始人**: 别用"五年后护城河看不清""这不就是个 wrapper"当作不做的借口——这是把自己劝退最蠢的方式。先用极致速度解决一个具体客户"痛到不想上班"的问题,护城河会在你死磕交付、积累真实数据与切换成本的过程中自然长出来。

### 反模式二:把酷炫 demo 当成产品,却没人肯做 eval / Mistaking a cool demo for a product — nobody does the evals

AI 让"做出一个 60–70% 能跑的 demo"变得极其容易——容易到足以骗过 VC、签下试点。但 Jake Heller 反复强调:**难的从来不是造出来,而是做对**;LLM 像人一样"没喝咖啡就会出错",demo 一进生产就崩,而绝大多数人从不做 eval、也从不花时间搞清专业人士到底怎么干活(l0h3nAW13ao)。这与《七种力量》里的"流程力"是同一件事:把最后 10% 做到每天数万次请求下 99% 可靠,是一种连大模型实验室的人都不愿干的"schlepp blindness"式苦活,而这正是壁垒(bxBzsSsqQAM)。三个具体反模式值得警惕:① 追求 100% 端到端自动化——Variance 的教训是让 Agent triage 掉 99% 简单案子、把最难的 1% 连同一个"好用的调查面板"交给人,人机协作面板才是产品而非附属品(JF6XIixstmQ);② 什么都塞给 LLM——能用确定性代码或数学计算搞定的就别用 prompt,"prompt 又慢又贵"(l0h3nAW13ao);③ 指望一次 LLM 调用吃下非结构化数据——Flexport 的做法是让 AI 去写解析器,而不是把几千行的 Excel 直接喂给模型要 JSON(KTmxaMdUbHA)。

> 🗣️ "most people never eval, and they never take the time to figure out how professionals really do the job" —— Jake Heller, Casetext (l0h3nAW13ao)
> 译:大多数人从不做 eval,也从不花时间去搞清专业人士真正是怎么干活的。

**🤖 对 AI Agent 创始人**: 第一天就搭 eval 流水线,把关键判断设计成可客观打分(true/false、0–7 分),把"为一个 prompt 磨两周从 60% 提到 97%"当成核心工作而非杂活;把客户投诉和"最蠢的用法"变成回归测试。你的护城河不在模型里,在这套没人愿意做的苦工里。

### 反模式三:只跟一侧用户聊、把"很多用户"当 PMF、把需求当"还没准备好" / Talking to the wrong people, mistaking usage for PMF, misreading pull

需求验证的三个经典死法在这些谈话里被反复点名。**第一,只搞懂市场的一侧。** Meesho 第一版 Fashion Nearby 只访谈卖家、从没跟消费者聊,做出"比商场差、比电商也差"的两头不讨好产品,3 个月关停(49L8lVe_PVo)。**第二,把注册量当 PMF。** Meesho 有几十万商家在用却不肯付费、不是重度用户,真正的 PMF 藏在一小撮"每天用 15–20 次、一边骂缺功能一边离不开"的 power users 身上;"在你真正见到 PMF 之前,你永远不知道 PMF 是什么"(49L8lVe_PVo)。**第三,把强烈的用户需求误读成"我还没做好"。** Dylan Field 直到第五年被微软提醒才明白,用户早就在"把产品从你手里拽出来"(写 12 页需求文档、执念般给反馈)——这是 product-market **pull**,该疯狂加倍下注,而不是解读成"等我全做完才算 fit"。同样,Figma 拖了 5 年才收费是他最想撤回的教训:尽早发布、尽早收费才能验证价值(-7Qz7tSTfUU)。别信用户嘴里说的,去现场蹲点看真实行为(Meesho 正是坐在店里一整天才发现店主早就在用 WhatsApp 群卖货)。

> 🗣️ "we started this product and we never ever spoke to consumers" —— Vidit Aatrey, Meesho (49L8lVe_PVo)
> 译:我们做这款产品时,从来、从来没有跟消费者聊过(只跟卖家聊,只搞懂了市场的一侧)。

> 🗣️ "everyone talks about product market fit, but product market pull is really important" —— Dylan Field, Figma (-7Qz7tSTfUU)
> 译:人人都在谈产品市场契合(fit),但产品市场拉力(pull)才真正重要。

**🤖 对 AI Agent 创始人**: 如果你的 Agent 是双边/多边的,验证期必须同时访谈两侧;用"每天反复调用 + 主动写需求"这类 pull 信号判断 PMF,而不是注册量或礼貌好评。给每个 idea 设一道"3 个月证伪"闸门,并且本周就让 Agent 上线、挂上收费。

### 反模式四:把"能做"当成"该做",把思考外包给 LLM / Confusing "can" with "should" — outsourcing your judgment to the model

AI 给了你一堆超能力,于是最隐蔽的陷阱是**克制不住地对每个"能做"说"是"**。Vibe coding 落地页那期把它讲成一整套病症:紫色渐变、追光标的按钮、滚动劫持、假 dashboard——这些是 LLM 训练数据里的高频套路,一个好设计火了下周所有创业公司官网就撞脸,原创性被稀释成一眼可辨的 "AI slop";更糟的是很多人 one-shot 生成后根本没真去用一遍,把小 bug 直接上线,客户会怀疑"产品是不是也是 vibe 出来的"(DNSXlBmukck)。Cursor 设计负责人补刀:别用只有你团队懂的自造行话(如 "progressive discovery"),用户只会说"我 MCP 太多管不过来"(RynySryqM_0)。这股引力有个名字——Katie Dill 叫它"通往平庸的引力":AI 能很快做出 7 分货,你会本能觉得"够了",而每天每件事都选"够好",复利成一家平庸公司(ypzNhwpmOD4)。同样的病在技术侧也有:Hassabis 怀疑"放几十个 agent 跑 40 小时"的产出配不上投入,也没见过 vibe coding 做出的 App Store 榜首作品——它仍需要人的手艺、灵魂与品味(JNyuX1zoOgU);Poetiq 则点名"微调陷阱":一进微调就烧掉几百万到几亿美元,下一个前沿模型一出就等于"一把火烧了",押注在会迅速贬值的资产上(UPGB-hsAoVY)。

> 🗣️ "just because something is possible. Doesn't mean you should say yes to it." —— Aaron Epstein, Vibe Coded Websites Review (DNSXlBmukck)
> 译:一件事"能做到",不代表你就该对它说"是"。

> 🗣️ "you are still kind of like responsible to not outsource your thinking to llms" —— Raphael Schaad, Vibe Coded Websites Review (DNSXlBmukck)
> 译:你仍然有责任——不要把你的思考外包给 LLM。

**🤖 对 AI Agent 创始人**: 给每个 AI 生成的动效/特性做"转化审计"(它帮我转化了吗?答不上来就删);当"有主见的编辑",而不是无脑 accept all changes。把 AI 省下的时间投到 messaging、原创设计和把关键路径从 7 分推到 9 分上;别急着微调,先把底层模型当可热插拔的通用层。

### 反模式五:只追风口做衍生点子,并照搬"共识剧本" / Chasing hot ideas & cargo-culting the consensus playbook

只做"当下火的东西",等于主动选择做衍生的、明显的、有一堆竞争对手的点子——AI 垂直赛道的绿地红利正在关闭,靠"随便挑个垂直做 workflow 自动化"已经不够(Hm-ZIiwiN1o)。同样危险的是**无脑照搬已成默认的 playbook**:FDE(前置部署工程师)如今被当成 AI 企业级标配,但它的共建者 Bob McGrew 的前三条建议都是"别在家试"——能避就避,还有一个经典失败模式是把为单个客户做的东西直接塞进产品,造出过度特化、没法泛化的东西(Zyw-YA0k3xo)。Flexport 的 Ryan Petersen 给了两把锋利的尺子:一是很多机会"小到不该开一家公司,它也许只是个 feature,不是 company",在位者能第二天推给上千客户的东西你别硬刚;二是别去自动化那"最后一小截长尾"——"没有 API 我就做不了、Agent 干不了这个任务就当它做不了",正是传统市场里的人栽跟头的错觉(KTmxaMdUbHA)。而用 VC 的军规(硬件不投、TAM 太小、地点不对)提前否掉自己也是陷阱:Flock Safety 集齐三宗"不投",如今 75 亿美元、侦破全美 10% 报案犯罪(Hm-ZIiwiN1o)。

> 🗣️ "If you only want to work on things that are hot, you're going to find yourself working on derivative ideas that end up being obvious, that end up having 5, 10, 100 competitors." —— Garry Tan, Unpopular Ideas / The Lightcone (Hm-ZIiwiN1o)
> 译:如果你只想做当下火的东西,你会发现自己在做衍生的点子,最终它们都很明显、都有 5 个、10 个、100 个竞争对手。

> 🗣️ "It's maybe a feature, not a company." —— Ryan Petersen, Flexport (KTmxaMdUbHA)
> 译:它也许只是一个功能,而不是一家公司。

**🤖 对 AI Agent 创始人**: 列一张"AI 创业共识 playbook"清单(纯 FDE 打法、只做 point-solution、"wrapper 会被大模型碾死"),逐条问"如果它在特定场景下是错的,反着做会怎样"。用第一性原理而非 TAM 筛点子;别把为第一个客户做的定制直接搬进产品(要"抽象上提一级");也别浪费生命去自动化那注定要人来兜底的长尾。

### 反模式六:把试点收入当 ARR,把产品当"屏幕上的像素" / Vanity revenue (the PRR trap) & neglecting delivery

卖出去不等于成交,试点开始更不等于。Jake Heller 作为天使投资人看到大量号称 10M ARR 的公司,扒开一看是付了半年高价、根本不会转化的试点——他造了个词 **PRR(pilot recurring revenue,试点循环收入)**,并预言一场"大灭绝"在酝酿:报表数字再漂亮也危险(l0h3nAW13ao)。根因是把"产品"误解成"屏幕上的像素",而忽视了交付——培训、客户成功、创始人贴身的 onboarding、必要时派"前线部署工程师"坐到客户旁边,让每个用户真正理解并用起来。定价上的反模式是继续卖 20 美元/月的 SaaS 逻辑:Bob McGrew 指出 FDE/Agent 卖的是"结果(outcome)、已解决的问题",合同应该随 land-and-expand 越做越大,而不是像 SaaS 那样越做越小、越标准(Zyw-YA0k3xo)。

> 🗣️ "instead of ARR, it's like PRR, like pilot recurring revenue... A big part of your job as a founder... is making sure that everybody who uses the product really understands it." —— Jake Heller, Casetext (l0h3nAW13ao)
> 译:那不是 ARR,更像 PRR——试点循环收入……而你作为创始人很重要的一部分工作,是确保每个使用产品的人真正理解它。

**🤖 对 AI Agent 创始人**: 盯紧"试点 → 付费"的真实转化率,别把 pilot 收入包进 ARR 汇报。按交付价值/完成的任务定价,并直接问客户想怎么付;把 onboarding、培训和贴身交付当成产品的一部分来投入,而不是签完试点就走。

### 反模式七:创始人单点故障,以及公司在成功后腐坏 / Single points of failure & the rot that comes with success

最后一类陷阱发生在你开始成功之后。**第一是创始人单点故障。** Variance 高速增长时,CEO 被卡车撞、住院十天无法行走,而当时全公司只有工程师加她一人做全部销售与客户关系——"CEO 的 bus factor 是 1",这是一堂关于单点故障与"尽早 scale me"的血泪课(JF6XIixstmQ)。**第二是钱会自己把自己花掉。** Ryan Petersen 的硬核建议:拿完大额 up round 后第二天就做 90 天招聘冻结,先建立"用解决问题而非加人来应对困难"的文化,别让组织在融资后膨胀(KTmxaMdUbHA)。**第三是把成功当护身符、把治理丢给律师。** Eric Ries 警告:越成功,公司作为"被夺取的目标"就越值钱;绝大多数创始人从没读过自己的公司章程,还以为拿了双重股权就无敌——而双重股权一直在被击穿(股价暴跌、投资人断供、创始人去世)。对做高价值、有安全争议 Agent 的人,"使命可信度"本身就是招聘与信任护城河,但它必须靠结构(如 PBC、永续目的信托)而非口头承诺才成立(7VKliOQXQ9M)。

> 🗣️ "The CEO has a bus factor of one. We only have engineers and we have me that's running all the sales and the customer relationships." —— Karine Mellata, Variance (JF6XIixstmQ)
> 译:CEO 的 bus factor(巴士系数)是 1——我们只有工程师,还有我一个人在跑全部销售和客户关系。

> 🗣️ "founders think that having dual class shares makes you invincible, but it really doesn't. Dual class is defeated all the time." —— Eric Ries, Incorruptible (7VKliOQXQ9M)
> 译:创始人以为拿了双重股权就无敌了,其实根本不是——双重股权一直在被击穿。

**🤖 对 AI Agent 创始人**: 趁早把销售/客户关系文档化、可交接,别让 bus factor 停在 1;融资后立刻定 90 天招聘冻结,只盯每股价格与控制权两个变量。今天就读一遍你的公司章程;如果你在做能力强、有安全争议的 Agent,趁只有 SAFE 时把公司变成 PBC——这是门槛最低、收益最高的一步。

## ⚡ 本章行动清单 / Action Checklist
- [ ] 停止为"五年后护城河"和"这是不是套壳"焦虑——先用极致速度解决一个具体客户的存亡级痛点,护城河后面自然长出来。
- [ ] 第一天就搭 eval 流水线,把"为一个 prompt 磨两周从 60% 到 97%"当核心工作;能用确定性代码解决的绝不塞给 LLM。
- [ ] 双边产品同时访谈两侧;用"重度使用 + 主动写需求"(pull)而非注册量判断 PMF;本周让 Agent 上线并挂上收费。
- [ ] 对每个 AI 生成的特性/动效做"该不该做"审计,当有主见的编辑;one-shot 之后一定亲自走一遍并 QA,拒绝 slop 和"够好就行"。
- [ ] 列出你正在照搬的"共识 playbook",逐条质疑;别自动化注定要人兜底的长尾,也别做只是在位者一个 feature 的东西。
- [ ] 区分 ARR 与 PRR:盯真实转化率,按结果/任务定价,把 onboarding 与交付当产品的一部分投入。
- [ ] 消除创始人单点故障(文档化、可交接);融资后 90 天招聘冻结;今天读一遍公司章程,必要时 day-one 转 PBC。

## 📚 本章取材视频 / Sources
- [The 7 Most Powerful Moats For AI Startups](https://www.youtube.com/watch?v=bxBzsSsqQAM) — 点破"护城河是后来的事、别用它劝退自己",早期唯一护城河是速度 (`notes/bxBzsSsqQAM.md`)
- [From Idea to $650M Exit: Lessons in Building AI Startups](https://www.youtube.com/watch?v=l0h3nAW13ao) — evals 才是真护城河、"直接造破套壳焦虑"、PRR 试点收入陷阱 (`notes/l0h3nAW13ao.md`)
- [Good News For Startups: Enterprise Is Bad At AI](https://www.youtube.com/watch?v=DULfEcPR0Gc) — 拆穿"95% 失败/套壳没护城河"迷思,切换成本就是护城河 (`notes/DULfEcPR0Gc.md`)
- [How Meesho Became India's Biggest Shopping App](https://www.youtube.com/watch?v=49L8lVe_PVo) — 只听一侧用户、把注册量当 PMF、观察真实行为的三大教训 (`notes/49L8lVe_PVo.md`)
- [Dylan Field: Scaling Figma and the Future of Design](https://www.youtube.com/watch?v=-7Qz7tSTfUU) — 尽早发布收费、别把强 pull 误读成"还没准备好" (`notes/-7Qz7tSTfUU.md`)
- [Common Mistakes With Vibe Coded Websites](https://www.youtube.com/watch?v=DNSXlBmukck) — AI slop、"能做≠该做"、别把思考外包给 LLM (`notes/DNSXlBmukck.md`)
- [Cursor Head of Design Roasts Startup Websites](https://www.youtube.com/watch?v=RynySryqM_0) — 自造行话、首屏讲不清"这是什么"的转化反模式 (`notes/RynySryqM_0.md`)
- [How Stripe Built Their New Website](https://www.youtube.com/watch?v=ypzNhwpmOD4) — "通往平庸的引力"、7 分货陷阱、不接受 slop (`notes/ypzNhwpmOD4.md`)
- [Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough](https://www.youtube.com/watch?v=JNyuX1zoOgU) — 警惕"40 小时 agent"的虚荣指标、锯齿状智能、别只做套壳 API (`notes/JNyuX1zoOgU.md`)
- [The Powerful Alternative To Fine-Tuning](https://www.youtube.com/watch?v=UPGB-hsAoVY) — "微调陷阱":押注会迅速贬值的资产 (`notes/UPGB-hsAoVY.md`)
- [Billion-Dollar Unpopular Startup Ideas](https://www.youtube.com/watch?v=Hm-ZIiwiN1o) — 只追风口=做衍生点子、别用 VC 军规否掉大机会、反共识剧本 (`notes/Hm-ZIiwiN1o.md`)
- [The FDE Playbook for AI Startups with Bob McGrew](https://www.youtube.com/watch?v=Zyw-YA0k3xo) — "别在家试 FDE"、过度特化陷阱、按结果定价 (`notes/Zyw-YA0k3xo.md`)
- [AI Is Eating Logistics](https://www.youtube.com/watch?v=KTmxaMdUbHA) — "feature 不是 company"、别自动化长尾、融资后 90 天招聘冻结 (`notes/KTmxaMdUbHA.md`)
- [This Startup Catches Fraud at Scale](https://www.youtube.com/watch?v=JF6XIixstmQ) — 别追求 100% 端到端、创始人 bus factor=1 的单点故障 (`notes/JF6XIixstmQ.md`)
- [How The Best Companies Defend Against Mediocrity And Rot](https://www.youtube.com/watch?v=7VKliOQXQ9M) — 成功是靶子不是护身符、双重股权会被击穿、读你的章程/转 PBC (`notes/7VKliOQXQ9M.md`)
