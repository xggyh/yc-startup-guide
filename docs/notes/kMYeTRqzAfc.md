# 未来公司只剩两种岗位:Replit CEO 谈 AI 原生建造者时代 / Replit's CEO On The Only Two Jobs Left In The Company Of The Future

> **来源**: [Replit's CEO On The Only Two Jobs Left In The Company Of The Future](https://www.youtube.com/watch?v=kMYeTRqzAfc) · Y Combinator · 2026-04-25 · 时长 39:11
> **讲者**: Amjad Masad(Replit 联合创始人兼 CEO,SPEAKER_01)· 主持 Andrew Miklas(YC,SPEAKER_00)
> **一句话定位**: 一个把"写代码"整层抽象掉、让离问题最近的非工程师也能造出真软件的 vibe-coding 平台创始人复盘,教 AI Agent 创始人如何选用户、做 GTM、按 AI 能力排产品路线图、并对 PMF 保持诚实。

## 🎯 TL;DR(中文核心要点)
- **最有价值的用户不是传统开发者,而是"技术相邻"的人**:产品经理、设计师、领域专家、创业者——他们有想法、有热情,只是被"必须先变得很技术"卡住了。把 ICP 从"会写代码"重新定义为"离问题最近、且有创始人心态的人"。
- **离问题最近的人自己造产品**:物理治疗师、养泳池的 SaaS、运动俱乐部软件……真正的机会藏在硅谷看不见的行业角落里。AI Agent 的分发红利在于"让原本造不出软件的人造出软件"。
- **GTM 双引擎**:自下而上用 PLG(做到好用、易推荐、有推荐机制)+ 自上而下"销售即布道/教育"。对非开发者,销售的工作是办 hackathon、教领导层用 AI、造内部 champion。
- **给非开发者做工具,内容是护城河**:文档要比标准 dev tool 简单得多,DevRel 更像"教育者"而非布道工程师,还要大量视频内容——"必须在内容上做到超额"。
- **按 AI 能力节奏排产品路线图**:Replit 判断 AI 能力大约每半年一次台阶式跃迁,于是每 6 个月发一个新 Agent 版本,既押注也拉高"什么是可能的"边界。产品要提前为下一次能力跃迁改架构(如为长时自主运行重写后端长驻容器)。
- **并行 Agent = 团队协作**:解决了并行 agent 与 merge 冲突,就顺带解决了多人实时协作;再加异步设计 canvas,让人在等 agent 时不被阻塞,进入心流。
- **对 PMF 要极度诚实**:拿到任何用户、任何付费都值得庆祝,但那不是 PMF;真正的 PMF 是"爆炸式"的、"一旦成了就是真的成了"。别自欺,该早点转向就早点转。
- **未来公司只剩两类岗位:建造者(builder)与销售者**——但销售会变成"帮客户转型的布道者/教育者",反而是更难被自动化、更有防御性的岗位;而"人人都是创始人",每天想的是"怎么让公司更成功",然后调度 agent 去解决发现的问题。

## 🧭 适合谁 / 什么时候看
- 正在做 **AI Agent / vibe-coding / no-code 平台** 的创始人,尤其想服务"非开发者"人群的。
- 纠结 **ICP 到底是谁、如何做 GTM(PLG vs 企业销售)** 的早期团队。
- 想学习 **如何把产品路线图对齐到 AI 能力演进** 的技术型创始人。
- 需要一剂 **PMF 诚实清醒剂** 的、正在"感觉好像有点起色"的创始人。

## 📝 分段精读

### 1. Replit 是什么:人人皆可造软件 / What Replit Is `[00:29–02:07]`
**要点(中文)**: 十年使命——让任何"会读会写"的人,带着一个想法进来,带着一个已部署、有流量、能扩容的真软件离开,全程不必操心任何技术细节。路径是逐层解决:先解决开发环境,再解决部署环境,最后在 2024 年 9 月把"写代码"这层也彻底抽象掉,背后是一个 coding agent,用户只用自然语言(以及 canvas 拖拽、评论等多模态)交互。关键定位:产出的是"真软件、安全的、可扩展的",不是玩具。
> 🗣️ "anyone who can read and write, basically that's the skill that you need, can come in with an idea and can leave with an app that's deployed, that's hosted, that's getting traffic, that can scale, and they don't have to worry about any technical aspect of building." —— Amjad Masad
> 译:任何会读会写的人——基本上你需要的技能就这些——都能带着一个想法进来,带着一个已部署、有托管、有流量、能扩容的应用离开,而完全不必操心搭建它的任何技术层面。

### 2. AI 原生建造者的崛起:谁最受益 / The Rise of AI-Native Builders `[02:27–06:26]`
**要点(中文)**: Amjad 从小就迷"创造"而非"技术本身",而开发者工具随时间反而越变越糟(BASIC 命令行 → 配置 React+Webpack 的噩梦)。他发现从产品中获益最多的,不是喜欢折腾配置的"匠人型"开发者,而是**技术相邻**的人:老早写过代码的 PM、被工程排期卡住的设计师、以及有想法有火的创业者。2023 年 Replit 做出一个明确取舍:**不再瞄准传统开发者**,转而服务因 AI 而出现的"AI 原生建造者"。
> 🗣️ "people that are getting the most value out of a product tend to be the more tech-adjacent ones." —— Amjad Masad
> 译:从产品中获益最多的人,往往是那些"技术相邻"的人。
> 🗣️ "There's a new generation of developers that are coming up right now because of AI. They're AI-native developers that are creating software without having to worry about every component in the system." —— Amjad Masad
> 译:因为 AI,现在正冒出一代新的开发者。他们是 AI 原生的开发者,无需操心系统里的每一个组件,就能创造软件。
> 🗣️ "but programming got worse. I wanted to bring it back, make programming great again, essentially." —— Amjad Masad
> 译:编程反而变糟了。我想把它找回来,基本上就是"让编程再次伟大"。

### 3. 用户在造什么:离问题最近的人 / What People Are Building `[06:31–11:03]`
**要点(中文)**: 三大类:个人软件、企业软件、创业者的产品。最打动人的案例都是**领域专家亲手造出自己需要的产品**:懂筋膜疗法的物理治疗师造出顶尖健康 App(此前花几十万美元外包却屡屡受挫);养泳池的家族生意做成 SaaS;还在用 MS-DOS 软件的体育俱乐部。硅谷之外有海量"盲区"行业等待被软件化。企业侧两类用武之地:一是加速产品开发(能尝试的想法量级提升一个数量级,从 100 个里试 5 个到能试 50 个),二是内部工具/业务线应用(RevOps 打通 CRM/Gong 数据、自建 CPQ 报价配置器,省下数十万甚至上百万美元 SaaS 费用)。
> 🗣️ "People who are closest to the problem can build up the products they need." —— Amjad Masad
> 译:离问题最近的人,能造出他们真正需要的产品。
> 🗣️ "suddenly, when anyone can make software, a lot of parts of the economy is just going to improve." —— Amjad Masad
> 译:突然之间,当任何人都能造软件,经济体的很多部分都会随之改善。

### 4. 如何扩张:PLG + 布道式销售 / How Replit Spreads `[11:16–13:31]`
**要点(中文)**: 复用了 YC dev-tool 公司(Stripe、PagerDuty)的洞察——过去二十年开发者被赋权把软件带进公司;如今这种赋权正外溢到 PM、设计师、运营。个人/周末玩耍的用法与工作用法高度重叠:一旦一个人意识到"我能用代码解决问题",会发生类似"神经系统层面的转变"。打法上:**PLG 仍是黄金标准**(做到极好用、易推荐、建推荐机制)+ **销售即布道/教育**(champion 带进公司→帮他办 hackathon 造更多 champion、教领导层懂 AI)。企业自上而下的单子靠长期积累的安全/合规信任赢下。
> 🗣️ "the moment you understand that you can solve a problem with code, it changes their mind." —— Amjad Masad
> 译:当一个人意识到自己能用代码解决问题的那一刻,他的心智就变了。
> 🗣️ "the PLG play, I think, is still the gold standard. Just make a product that's really good that people want to recommend to their friends and make it easy to refer others" —— Amjad Masad
> 译:PLG 这套打法我认为仍是黄金标准。就是做一个真正好到用户愿意推荐给朋友的产品,并让推荐他人变得容易。

### 5. 能力边界、集成与面向非开发者的 GTM / What You Can Build, Skills & DevRel `[13:48–19:25]`
**要点(中文)**: 边界:SaaS、消费级、自动化类产品"可以放心地建";但新云平台、新机器学习系统不是当前重点。集成靠与厂商共建,并顺应"skills 革命"——公司放出 skills/MCP,Replit 审核后接入,agent 现场检索技能库、把上下文拉进来(比喻成《黑客帝国》里"下载技能")。给非开发者做工具,**内容是护城河**:文档要更简单、DevRel 更像教育者、要产大量视频;agent 本身也要能与非开发者对话、当头脑风暴伙伴,所以加了 canvas、可视化界面、"生成多个变体"等按钮来"展示什么是可能的"。识别 champion 的信号:**创业者心态、resourceful、不会被卡住**。
> 🗣️ "I can confidently say to any entrepreneur out there, that you can build a SaaS product, a consumer product, like an automation product on Replit comfortably." —— Amjad Masad
> 译:我可以很有底气地告诉每一位创业者:你完全可以在 Replit 上从容地做出一个 SaaS 产品、一个消费级产品、或一个自动化产品。
> 🗣️ "If you're building a dev tool for non-developers, you have to go above and beyond on content." —— Amjad Masad
> 译:如果你在为非开发者做开发工具,你必须在内容上做到超额、更进一步。
> 🗣️ "resourceful, someone who's not going to get blocked, who's going to figure out what other AI tool I need to integrate, what can I like go learn in order to figure it out." —— Amjad Masad(描述理想 champion)
> 译:足智多谋、不会被卡住的人——会自己弄清楚还要接入哪个 AI 工具、要去学点什么才能把事情搞定。

### 6. YC 的影响:三个月、7% 增长、融资破局 / YC, Growth & Fundraising `[19:36–23:01]`
**要点(中文)**: YC 最大的领悟是"三个月能做成多少事":Sam 让整批人"未来三个月从朋友生活里消失",极度专注;他们用白板 + Demo Day 倒计时,每天擦掉数字往前推,三个月内从一个 repl(命令行跑代码)做到具备 Web 开发、初步托管、代码智能等 IDE 能力。这套"高强度冲刺 + 简单待办清单"至今用于每次 agent 发布(4 周把全员集中到办公室、包三餐+全天咖啡)。增长上反复回到 YC 基本功——**7% 周环比增长**是启动新产品线的好锚。融资上:进 YC 前只融到约 50 万美元、VC 不愿见;YC 后网络骤然打开,他大胆要到 Marc Andreessen 的引荐,A16Z 领投种子轮——"没有 YC 我们大概率会因融不到钱而放弃"。
> 🗣️ "The main realization from YC is how much you can get done in three months." —— Amjad Masad
> 译:从 YC 得到的最主要领悟,是三个月里你能做成多少事。
> 🗣️ "like 7% week over week growth, is like a very good way to bootstrap a new product line." —— Amjad Masad
> 译:比如 7% 的周环比增长,是启动一条新产品线非常好的方式。
> 🗣️ "We raised like maybe $500,000 and, you know, VCs did not want to meet us." —— Amjad Masad
> 译:我们当时大概只融了 50 万美元,而且 VC 们根本不想见我们。

### 7. 从 Vibe Coding 到自主 / 并行 Agent(Agent 4)/ From Vibe Coding to Autonomous Agents `[23:17–28:04]`
**要点(中文)**: 核心方法论:**把产品路线图对齐到 AI 能力演进**。判断 AI 能力大约每半年一次台阶式跃迁,于是每 6 个月发一个新 Agent 版本——既是预测、也是主动拉高"可能性"的边界。Agent 3 押注"自主性":为让 agent 后台跑 2–4 小时("下大 prompt→去吃午饭→回来软件已建好"),不得不重写后端做长驻容器,在真正的自主能力到来(11、12 月)前就先把方向做出来。Agent 4 三大主题:**并行 agent**(解决 merge 冲突→顺带解决团队实时协作)、**内置异步设计 canvas**(等 agent 时不被阻塞、进入心流)、以及**跨形态共享上下文**(同一项目一键生成 Web、移动 App、slide、视频,部署时 web 上线、app 进 TestFlight)。
> 🗣️ "every six months, we release a new agent version. And it's an act of predicting what's possible. It's also pushing the edge of what's possible." —— Amjad Masad
> 译:我们每六个月发布一个新的 agent 版本。这既是一种对"什么是可能的"的预测,也是在主动把可能性的边界往前推。
> 🗣️ "People should be able to put in a big prompt, go to lunch, come back and see the stuff." —— Amjad Masad
> 译:人们应该能够下一个大 prompt,去吃个午饭,回来就看到东西(已经做好)。
> 🗣️ "once you solve parallel agents you've also solved teamwork." —— Amjad Masad
> 译:一旦你解决了并行 agent,你也就顺带解决了团队协作。

### 8. 需要什么技能、对 PMF 诚实、在等待什么、未来公司 / Skills, PMF Honesty & The Future `[28:25–38:57]`
**要点(中文)**: 技能:正走向"后 prompting 世界"——更多是给高层目标(如"优化我的营销漏斗"),prompting 只在需要交互时保留。真正重要的是:**知道什么是可能的**(保持玩心、持续尝试、紧跟前沿资讯)、**不放弃**(今天做不出的,一个月/两周后再试可能就行了)、以及**持续的想法生成能力**(小型创业者的产品有生命周期,要不断创造新东西)。对 PMF 要**极度诚实**:拿到任何用户、任何付费都值得庆祝,但那都不是 PMF;真正的 PMF 是爆炸式的,别自欺、该早点转向。在等待的两项技术:**computer-use 模型**(意外地难做,coding agent 成了绕过它的 hack)与**持续学习/在岗学习**(现在只能靠写 skill.md 文件硬凑,真正的在岗学习尚未解锁)。未来公司:只剩**建造者 + 销售者**两类岗位,销售变成帮客户转型的布道/教育者(更有防御性),而"人人都是创始人",每天想"怎么让公司更成功",然后调度/派遣 agent 去解决发现的问题(Replit 内部已有"vibe coding in residence"小队巡回各部门找问题、造工具)。
> 🗣️ "true product market fit is entirely different it's like an explosive thing" —— Amjad Masad
> 译:真正的产品-市场契合完全是另一回事,它是一种爆炸式的东西。
> 🗣️ "I actually think we're headed to like a post prompting world" —— Amjad Masad
> 译:我其实认为我们正走向一个"后 prompting"的世界。
> 🗣️ "I think the company of the future is made of builders and salespeople broadly" —— Amjad Masad
> 译:我认为未来的公司,大体上由建造者和销售者构成。
> 🗣️ "and so the sales probably part is like one of the more defensible jobs" —— Amjad Masad
> 译:所以销售这部分,大概是更具防御性(更难被取代)的岗位之一。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **重新定义你的 ICP**:不要默认"会写代码的人",去找"离问题最近 + 有创始人心态 + resourceful"的技术相邻者(PM、设计师、运营、领域专家),他们才是最愿意付费和传播的 champion。
- [ ] **把路线图对齐 AI 能力曲线**:假设能力每半年一次台阶跃迁,提前为下一次跃迁改架构(如长时自主运行、并行执行),在能力真正到来前就把方向 demo 出来。
- [ ] **内容即护城河**:如果服务非开发者,配"教育者型 DevRel"、把文档做到极简、批量产视频,并在产品里内置"展示可能性"的按钮/模板/canvas。
- [ ] **建 GTM 双引擎**:PLG(极致好用 + 推荐机制)负责自下而上获客;"布道式销售"(hackathon、教领导层用 AI、造内部 champion)负责把单点 champion 放大成企业采购。
- [ ] **接入 skills/MCP 生态**:让 agent 能现场检索并加载外部技能/集成(如 Stripe、CRM),但把"审核安全性"当作正式关卡。
- [ ] **对 PMF 建立诚实指标**:明确区分"有用户/有收入"与"爆炸式 PMF",设定何时该转向的判据,避免自欺式坚持。

## 🔑 关键术语 / 概念
- **Tech-adjacent(技术相邻者)** — 曾接触过技术但不想操心环境/部署的人(老 PM、设计师、运营),Amjad 眼中最能从 AI 造软件工具获益、最该被当作 ICP 的人群。
- **AI-native developer(AI 原生开发者)** — 因 AI 而出现的新一代"开发者",无需理解系统每个组件即可创造软件。
- **Vibe coding** — 用自然语言/高层意图交互、由 coding agent 在幕后生成真软件的开发方式;Replit 2024-09 起把"写代码"这层整体抽象掉。
- **PLG(Product-Led Growth,产品驱动增长)** — 靠产品本身好用+易推荐驱动获客;Amjad 称其为"仍是黄金标准"。
- **Champion(内部拥护者)** — 把工具带进公司、推动采购与传播的人;理想画像是"有创始人心态、resourceful、不会被卡住"。
- **Skills / MCP** — 可被 agent 检索并加载的外部能力/集成包(公司对外发布,平台审核后接入);比喻为《黑客帝国》里"下载技能"。
- **Parallel agents(并行 agent)** — 多个 agent 同时工作;解决其 merge 冲突后即等价于解决了多人实时团队协作。
- **Computer-use models(计算机操作模型)** — 直接操作鼠标/界面的模型;意外地难做好,coding agent 目前是绕过它的 hack。
- **Continual / on-the-job learning(持续/在岗学习)** — agent 在组织内边干边变强;目前只能靠写 skill.md 文件硬凑,真正解锁尚远。

## 🔖 高价值金句时间戳
- `[05:36]` "There's a new generation of developers that are coming up right now because of AI." — AI 让"造软件的人"重新定义,ICP 也随之改写。
- `[07:41]` "People who are closest to the problem can build up the products they need." — Agent 时代的分发红利,在于赋能离问题最近的领域专家。
- `[12:21]` "the PLG play, I think, is still the gold standard." — 即便有 AI,增长底盘仍是"做到好用+易推荐"。
- `[19:36]` "The main realization from YC is how much you can get done in three months." — 高强度专注冲刺 + 简单待办,是产品从 0 到有的引擎。
- `[24:30]` "It's an act of predicting what's possible. It's also pushing the edge of what's possible." — 把路线图押注在 AI 能力的下一次跃迁上。
- `[31:32]` "true product market fit is entirely different it's like an explosive thing" — 别把"有用户/有收入"误当 PMF,真 PMF 是爆炸式的。
- `[35:15]` "I think the company of the future is made of builders and salespeople broadly" — 未来公司只剩两类岗位:建造者与(会转型为布道者的)销售者。
