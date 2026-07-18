# AI Agent 经济已经到来:为"会挑工具的智能体"做产品 / The AI Agent Economy Is Here

> **来源**: [The AI Agent Economy Is Here](https://www.youtube.com/watch?v=Q8wVMdwhlh4) · Y Combinator · 2026-02-21 · 时长 23:21
> **讲者**: The Lightcone 播客四位 YC 合伙人 —— Garry Tan(SPEAKER_00)、Diana Hu(SPEAKER_01)、Harj Taggar(SPEAKER_02)、Jared Friedman(SPEAKER_03)
> **一句话定位**: 当智能体(agent)本身成为选择、购买、使用开发者工具的"新用户",创业者要把 GTM、文档、基础设施全部改造成"面向 agent"——这决定了 AI Agent 创业公司能不能被 agent 选中。

## 🎯 TL;DR(中文核心要点)
- **Agent 已经是软件市场的"买家"**:vibe coding + 自主 agent(节目里戏称 OpenClaw / Clawed Code)让开发者从 2000 万暴涨到数亿人,再加上每个人背后半自主的 agent,是它们在替人挑工具。口号从 "Make something people want" 变成 "Build something agents choose"。
- **文档就是 agent 的"前门"(front door)**:agent 通过读文档来决定用哪个工具。文档要为 agent 优化(结构化、可解析、代码片段、`llms.txt`),而不只是给人看。Resend 因此成为 LLM 回答"如何发邮件"的默认答案。
- **谁的文档最好,谁就成默认栈**:agent 把 Supabase 当默认 Postgres,只因为"Supabase 文档最好,所以推断它最好用"——文档质量直接=市场份额。
- **文档的 5% 改进 = 业务的巨大杠杆**:未来做决策的 agent 数量指数级超过人类,哪怕开发者文档只优化 5%,对 dev tool 业务的影响也可能是"史无前例地巨大"(Mintlify 抓的就是这个红利)。
- **"给 agent 用的 X"是整片空地**:给 agent 的邮箱(Agent Mail)、给 agent 的电话号码(Twilio for agents)……存在一个"为 agent 原生打造的平行技术栈",这是明确的 Request for Startup。
- **要先长出对模型的"手感直觉"**:亲手重度使用 agent,搞清它们在哪卡住、擅长什么;做工具时站在 agent 视角想"它愿不愿意用我"。像 Boris(Claude Code)那样"共情模型"、顺着模型的天性去支持它,而不是对抗它。
- **agent 想要开源 + API,讨厌网页**:它们要 API、要写代码、要开源;把一切做成 open、open-source、API-first。
- **人仍是"责任兜底器"(liability sink)**:agent 不是能签字的法律主体、连未成年人都不如,所以短期内每个 agent 背后仍需要一个人来承担责任与法律主体地位。

## 🧭 适合谁 / 什么时候看
- 正在做/想做 **开发者工具、agent 基础设施、API 产品** 的 AI Agent 创始人:这集直接告诉你新的 GTM 长什么样。
- 卡在"怎么让 agent 发现并选中我的产品"的团队:文档即分发渠道,这里有 Resend / Supabase / Mintlify 的具体打法。
- 想找 agent 时代空白赛道的人:"给 agent 用的 X"清单式 RFS。
- 15 分钟就能看完的趋势速览,适合在写下一版产品/文档/落地页之前先看。

## 📝 分段精读

### 1. 开场:AGI 真的来了,人人"赛博精神病" / Intro `[00:00–02:12]`
**要点(中文)**: 主持人用夸张的自嘲开场——非技术 CEO 在用 OpenClaw 自动化整块业务,十年没写代码的产品型 CEO 半夜同时跑四个 Clawed Code worker。核心观感是:模型能力"喊了几年,突然就到了",AGI 已经在门口,大家正处在楔子的最薄边缘。这一段为全集定调:不是空想未来,而是描述"此刻正在发生"的行为改变。
> 🗣️ "There's sort of this explosion in model capability. We've been talking about this for several years, but then it feels like it's here. AGI is literally actually here, and we're sort of at the thin edge of the wedge." —— Garry Tan
> 译:模型能力正在爆发。这事我们说了好几年,但现在感觉它真的到了。AGI 确实已经来了,而我们正处在这个楔子最薄的边缘。

### 2. "无需人类介入"正在改变一切 / No human involvement is changing the experience `[02:12–04:55]`
**要点(中文)**: 一年前还在争 Cursor vs Windsurf,产品体验本质是"高级自动补全";现在人们直接信任 agent 替自己做决定、同时跑五个不干预。由此衍生出一个关键判断:**agent 会自己去挑工具**,从而在人类经济之外并行出现一个"agent 经济"。dev tool 的 go-to-market 被彻底改写——过去靠开发者口口相传、Stack Overflow、GitHub trending;现在开发者群体从 2000 万暴涨到数亿人,而且每个人背后还有半自主的 agent 充当"告诉你该用什么工具的神谕(oracle)"。
> 🗣️ "The agents are going to go out and choose tools to use to build things, which is going to essentially create a whole economy of agents, like picking and choosing dev tools... it will essentially have this whole agent economy going on in parallel to the human economy." —— Harj Taggar
> 译:agent 会自己出去挑选用来构建东西的工具,这基本上会催生出一整个"agent 的经济"——它们在挑选 dev tool……于是就形成了一个与人类经济并行运转的完整 agent 经济。

### 3. YC 要不要改口号? / Does YC need to change its motto? `[04:55–07:48]`
**要点(中文)**: 全集最"金句密集"的一段。Supabase(节目里读作 Superbase)的 Postgres 数据库需求爆炸式增长,原因是 vibe coder 和 agent 把它当默认——**而 agent 选它,仅仅因为"它文档最好,所以推断它最好用"**。由此 Ben Tossall 的推文被抬出来:agent 从现在起就是软件市场,要做 agent 会选的东西。YC 的 "Make something people want" 被戏改为 "Make something agents want"。Garry 还讲了亲身踩坑:Claude Code 默认给他选了几年前、几乎废弃的 Whisper V1,慢得离谱;Perplexity 告诉他应该用带队列的 Groq——快 200 倍、便宜 10 倍。说明"agent 还没优化到位",正是创业者切进去做更好东西的窗口。
> 🗣️ "Agents are the software market from now on. Build something agents choose." —— Ben Tossall 推文,由 Jared Friedman 引述
> 译:从现在起,agent 就是软件市场。去做那些 agent 会主动选择的东西。
>
> 🗣️ "The agents are choosing Superbase as a default tool to like set up and host their Postgres database. Because... Superbase has the best documentation, it's reasonable for the agents to assume that that's like the best tool to use." —— Harj Taggar
> 译:agent 把 Supabase 当成搭建和托管 Postgres 数据库的默认工具。因为……Supabase 文档最好,agent 便合理地推断它就是最好用的工具。

### 4. 邮件工具与 agent 基础设施:Resend 案例 / Email tools and agent infrastructure `[07:48–09:36]`
**要点(中文)**: 具体案例——Resend(W23,发信客户端)。当你问 ChatGPT / Claude "怎么让 web app 发邮件",默认答案就是 Resend。创始人一年多前就领先地发现:客户转化的前三大 inbound 渠道之一来自 ChatGPT;随后他**主动把文档改造成"agent 友好"**——用人/agent 真会问的问题("我怎么发/收邮件")做条目,给出结构化、要点化、带代码片段的答案。对比 SendGrid 这种 Web 2.0 老派做法:把你丢进客服、代码片段难解析。**文档结构直接决定 LLM 会不会把你当默认栈。**
> 🗣️ "He made this post over a year ago that the number top three channel of inbound of customer conversion came from chat GPT. One thing that he did after that, he actually optimized his documentation to be agent friendly." —— Diana Hu
> 译:他一年多前就发帖说,客户转化的前三大 inbound 渠道之一来自 ChatGPT。之后他做的一件事,就是把文档优化成对 agent 友好的形式。

### 5. Agent 驱动的文档,与"给 agent 用的 X" / Agent driven documentation & infra `[09:36–13:00]`
**要点(中文)**: 把"文档=分发"讲透。文档正在成为 agent 推荐 dev tool 的**前门(front door)**;Resend 甚至专门放了为 agent 优化的 `LLM doc text`(即 `llms.txt`)。Mintlify 抓的就是这波顺风——它给 dev tool 公司自动生成/同步对 agent 优化的文档,而未来做决策的 agent 数量指数级碾压人类,**哪怕文档只提升 5%,业务影响都可能巨大**。基础设施层同样空白:Agent Mail(给 AI agent 的收件箱)因为 Gmail 等刻意反自动化而应运而生,OpenClaw 火了之后它直接爆发;Jared 顺势发问"有没有人做 Twilio for agents / 给 agent 的电话号码",Diana 直接定性为 Request for Startup——存在一个"为 agent 原生打造的平行技术栈"。
> 🗣️ "Documentation is going to be the front door for a lot of these agents to recommend dev tools." —— Diana Hu
> 译:文档将成为许多 agent 推荐 dev tool 时的"前门"。
>
> 🗣️ "Even if you can eke out like a 5% improvement on your developer documentation, like the impact on your business as a developer tool could be like, you know, gigantic, which is sort of unprecedented." —— Harj Taggar
> 译:哪怕你的开发者文档只能挤出 5% 的改进,作为一家 dev tool 公司,它对业务的影响都可能是巨大的、几乎史无前例的。
>
> 🗣️ "Has anybody built like Twilio for agents yet or like phone numbers for agents? ... what are the other Xs for agents that people have to build?" —— Jared Friedman
> 译:有没有人已经做出"给 agent 用的 Twilio"、或者给 agent 的电话号码?……还有哪些"给 agent 用的 X"是必须被造出来的?

### 6. 群体智能:人类的钱 vs agent 的钱 / Swarm intelligence `[13:00–15:36]`
**要点(中文)**: 更"仰望星空"的一段。当 agent 有了邮箱和电话号码,它们能替你订餐厅,再把"该把人往哪送"发到 agent 社区(MoltBook)上互相交换情报——这已经跨过某种"恐怖谷"。引 Paul Buchheit 的"human money vs agent money":一开始 agent 用人类的钱交易(合理),但迟早它们会有自己的经济体系,届时人类货币的价值就不好说了。Garry 的核心洞见:未来大概率不是单一"上帝智能(God intelligence)",而是像生物/人类文明那样,由大量单体协作涌现的**群体智能(swarm intelligence)**。
> 🗣️ "Instead of God intelligence... it's going to be swarm intelligence again with these agents." —— Garry Tan(节选归纳其原话)
> 译:未来大概率不是"上帝智能",而是这些 agent 再一次形成的"群体智能"。

### 7. agent 生产内容与"死亡互联网理论" / Content generation & dead Internet theory `[15:36–18:12]`
**要点(中文)**: 互联网上多数代码已由 agent 写就,多数文字也终将由 agent 写(比如 Yelp 上 99% 的评论)——这正呼应"死亡互联网理论";但 Garry 给了反直觉的正面解读:如果 agent 更聪明、更对齐、更诚实,那么"内容大多由 agent 生成"反而可能是好事。技术判断上,Jared 提出:下一个刷榜 SOTA 的,可能不是最贵、GPU 最多的新基座模型,而是**一群更便宜的小模型像人类一样协作**。同时点破一个硬约束:agent 不是能签字的法律实体,连未成年人都不如,所以每个 agent 背后仍需要一个人当"责任兜底器(liability sink)"和法律主体——这也是 YC 目前只接受人类(而非 agent)申请的原因。
> 🗣️ "It's like a swarm of lower cost, cheaper models working together, just like humans do to solve a problem." —— Jared Friedman
> 译:它更像是一群更低成本、更便宜的模型协同工作,就像人类那样合力解决一个问题。
>
> 🗣️ "You actually like need a human to be like the liability sink and to be, you know, to have standing." —— Garry Tan
> 译:你其实仍然需要一个人来当"责任兜底器",并且拥有(法律上的)主体资格。

### 8. 增长、规则与创始人洞见 / Growth, rules and founder insights `[18:12–23:21]`
**要点(中文)**: 收尾给行动建议。(1)创始人应该"某种程度上都陷入赛博精神病"——重度亲手用 agent(但至少睡 6 小时),**长出对模型能力/边界的直觉手感**:哪种工具 agent 用得顺、在哪卡住。(2)做 dev tool 要**站在 agent 的视角**想:怎么让它"愿意用你、用得爽"。(3)学 Boris(Claude Code 团队)那样**共情模型**——别跟模型的天性对抗,而是顺着它的自然倾向去支持它。(4)agent 想要的东西很直接:开源、开放、API;它们讨厌网页,只想调 API、写代码。全集落回改写后的口号。
> 🗣️ "Developing an intuitive fuel, like a hands-on fuel for the agents, their limitations, their capabilities... think about it from the agent's perspective, like how can you make your tool something that the agent actually wants to work with." —— Harj Taggar
> 译:培养一种对 agent 的直觉手感——亲手上手去感受它们的局限和能力……然后站在 agent 的视角思考:你怎样才能把工具做成 agent 真正愿意使用的东西。
>
> 🗣️ "He really empathizes with the model... instead of fighting what the models want he like tries to let the model like do what it wants and to like support the model in whatever its natural inclination is." —— Jared Friedman(谈 Boris)
> 译:他是真的在"共情模型"……与其对抗模型想做的事,他更倾向于让模型去做它想做的,并顺着模型的天然倾向去支持它。
>
> 🗣️ "One thing agents want for dev tools is really make everything open and open source... they hate using websites, they want to use APIs, they want to write code." —— Diana Hu / Jared Friedman
> 译:对于 dev tool,agent 想要的一点就是把一切做成开放、开源的……它们讨厌用网页,它们想调 API、想写代码。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把文档当第一分发渠道来运营**:发布 `llms.txt`,用"用户/agent 真会问的问题"组织条目,每条给结构化要点 + 可复制的代码片段;拿 Claude/ChatGPT/Perplexity 反复测"我这类需求默认会被推荐谁"。
- [ ] **做一次"agent 默认答案"审计**:针对你所在品类的高频提问,看主流 LLM 现在默认推荐哪家(如发邮件=Resend、数据库=Supabase);若不是你,逆推对手文档为什么更好解析,并补上。
- [ ] **API-first + 开源优先**:确保核心能力都有干净的 API 与代码示例,能开源就开源;凡是"只能点网页 / 走人工客服"的环节,都是 agent 的劝退点,优先干掉。
- [ ] **每天亲手重度用 agent**:同时跑多个 agent 干真实任务,记录它们在哪卡住、误选了什么(如默认选了过时模型),把这些"卡点"直接变成你的产品机会清单。
- [ ] **站在 agent 视角设计 DX**:把"agent 会不会愿意用我、用得顺不顺"作为一等评审标准,而不是只优化人类 UI;必要时给 agent 单独的接入路径。
- [ ] **盘一遍"给 agent 用的 X"空白位**:邮箱(Agent Mail 已占)、电话号码/短信(Twilio for agents 待建)、身份、支付、日历……在这个"agent 原生技术栈"里挑一个你能做深的切入。

## 🔑 关键术语 / 概念
- **Agent economy(agent 经济)** — 与人类经济并行、由 agent 自主挑工具/下决定/相互交易而形成的经济体系。
- **"Build / Make something agents want"** — 把 YC 经典口号 "Make something people want" 改写为面向 agent:让 agent(而非只是人)想用、会选你的产品。
- **Documentation as the front door(文档即前门)** — agent 主要通过读文档来发现和推荐工具,所以文档质量≈市场准入与份额。
- **`llms.txt` / LLM doc text** — 专为 LLM/agent 解析优化的文档文本格式,用于让 agent 更容易把你当默认栈。
- **Agent-native infrastructure(agent 原生基础设施)** — 专为 agent 设计的邮箱、电话号、支付等底层服务;"给 agent 用的 X"。
- **Swarm intelligence vs God intelligence(群体智能 vs 上帝智能)** — 未来强能力更可能来自大量廉价模型的协作涌现,而非单一超大基座模型。
- **Liability sink(责任兜底器)** — 因 agent 无法律主体资格,每个 agent 背后需要一个承担责任、具备法律 standing 的人。
- **Dead Internet theory(死亡互联网理论)** — 认为网上大部分内容已是机器/垃圾生成;在 agent 时代被重新讨论(可能反而是好事)。
- **OpenClaw / Clawed Code / MoltBook** — 本集用于指代"自主 agent / Claude Code / agent-only 社交网络"的戏称,对应当下 agent 自动化与 agent 社区的现象。

## 🔖 高价值金句时间戳
- `[04:45]` "Superbase has the best documentation, it's reasonable for the agents to assume that that's like the best tool to use." — 文档最好=被 agent 默认选中,文档就是市场份额。
- `[05:01]` "Agents are the software market from now on. Build something agents choose." — 一句话概括新 GTM:你的用户变成了 agent。
- `[07:55]` "He actually optimized his documentation to be agent friendly." — Resend 的领先动作:主动把文档改造成 agent 友好。
- `[09:35]` "Documentation is going to be the front door for a lot of these agents to recommend dev tools." — 文档是 agent 推荐你的"前门"。
- `[10:47]` "Even if you can eke out like a 5% improvement on your developer documentation... the impact on your business could be gigantic." — agent 数量指数级放大了文档的杠杆。
- `[12:14]` "Has anybody built like Twilio for agents yet... what are the other Xs for agents?" — 一份现成的 agent 基础设施 RFS。
- `[21:54]` "Think about it from the agent's perspective, how can you make your tool something that the agent actually wants to work with." — 做 dev tool 的第一性原则:以 agent 为设计对象。
- `[22:55]` "They hate using websites, they want to use APIs, they want to write code." — agent 的偏好清单:API/代码/开源,不要网页。
