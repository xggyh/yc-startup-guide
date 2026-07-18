# AI 创业最强的 7 条护城河 / The 7 Most Powerful Moats For AI Startups

> **来源**: [The 7 Most Powerful Moats For AI Startups](https://www.youtube.com/watch?v=bxBzsSsqQAM) · Y Combinator · 2025-10-03 · 时长 45:06
> **讲者**: YC 播客《The Light Cone》四人对谈 —— Garry Tan(SPEAKER_00,YC CEO)、Diana Hu(SPEAKER_01,YC GP)、Jared Friedman(SPEAKER_02,YC GP)、Harj Taggar(SPEAKER_03,YC GP)。
> **一句话定位**: 用 Hamilton Helmer《七种力量》框架逐条拆解"AI Agent 公司到底有没有护城河",回答大学生和早期创始人最焦虑的问题——ChatGPT 套壳会不会被大模型厂碾死;结论是护城河真实存在但来得晚,早期唯一的护城河是速度,先去解决一个真痛点。

## 🎯 TL;DR(中文核心要点)
- **护城河是"防御性"的,先有值得守的东西再谈守**:没有找到值钱的、值得防御的东西之前,担心护城河等于"守一片空地上的水坑"。别用"看不清五年后的护城河"当作不做某个点子的理由——这是最蠢的错误。
- **早期唯一的护城河是速度(Speed),而它不在书里的七种力量之内**:Cursor 早期把冲刺周期压到"一天一个",大公司要走 PRD、spec doc、PM、运营流程,几周到几个月甚至几年才能发一个功能——初创靠"无情执行(relentless execution)"赢在这里。
- **七种力量本质是"七种护城河"**:流程力、独占资源、转换成本、反向定位、品牌、网络经济、规模经济——框架 2016 年出版但"永恒",AI 时代只是换了具体形态,类别没变。对 Agent 创始人最常出现的是**速度 + 流程力**这两条。
- **流程力(Process Power)= 把最后 10% 做到 99% 可靠的"苦活"**:周末黑客松能搓出 demo,但要在每天数万次 KYC 请求下稳定跑起来,是一种"schlepp blindness"式的painstaking 苦工,大模型实验室的人也不愿干——这恰恰是垂直 Agent 的壁垒。
- **独占资源(Cornered Resource)的最佳形态是"你自己的模型",但不是唯一**:早期靠 context engineering 拿到 80-90% 就够用,别用"没有自研模型"提前给自己判死刑;更现实的独占资源是 FDE(前置部署工程师)贴着客户拿到的**真实数据与真实工作流**,以及"客户脑子里的心智份额"。
- **转换成本有 AI 时代的新形态**:不只是 Salesforce/Oracle 那种"数据搬不动",而是六个月到一年的深度 onboarding,把 Agent 的**逻辑(而非只是数据)**为客户高度定制,一旦跑通转成七位数合同就"被 mint 住了";消费端则是 memory / 个性化正在变成新的转换成本。
- **反向定位(Counter-Positioning)是打在位者的软肋**:SaaS 在位者按"人头/座席(per seat)"收费是致命弱点——Agent 越成功,客户需要的座席越少,收入越被自我蚕食;founder-controlled 的公司可能敢自我革命,非 founder-controlled 的"不抱希望"。第二个打法是**做第二名**(Stripe 之于 Braintree、DoorDash 之于 Grubhub、Legora 之于 Harvey)。
- **垂直 AI SaaS 会比 SaaS 大 10 倍**:软件在 HVAC 这类生意里只占 1% 钱包份额,但把客服工作本身接过来能吃到 4%-10%——不是抢有限的软件预算,而是吃"原本花在人力工作流上的钱"。

## 🧭 适合谁 / 什么时候看
- 正在做或准备做 **AI Agent 创业**、被"这不就是个 ChatGPT 套壳、会不会被大模型厂碾死"这个问题劝退或困住的技术创始人。
- 已经找到 PMF、开始被抄袭和竞争追赶,需要系统性思考**如何构筑长期防御**的成长期创始人。
- 想把《七种力量 / Seven Powers》这本"商学院教材"翻译成 **2025 年 AI 语境**下可操作打法的人。
- **注意**:如果你还没找到一个值得守的东西,这期可以先看结论(速度 + 找真痛点),护城河的细节可以等有了"值得守的宝藏"再回来看。

## 📝 分段精读

### 1. 护城河问题 & 七种力量框架 / The Moat Problem & The Seven Powers Framework `[00:00–04:20]`
**要点(中文)**: 大学生在最近的校园巡讲里普遍问:这些新 AI Agent 公司(播客里聊过的那些)看不出有护城河,像是"ChatGPT 套壳"、一个周末就能克隆,能赚点钱但建不成长久的生意。四位主持认为这不对——这些生意其实有很深、很有意思的护城河,只是不显眼。Garry 引用他在 AI Startup School 后台和 Sam Altman 的对话:如今最该读的书之一居然是商学院教材——Hamilton Helmer 的《七种力量》(2016)。Jared 点破:书名叫 seven powers,但其实就该叫 **seven moats**——只是"一个生意能有的护城河种类就那么多,且不随时代改变",AI 时代变的是具体版本,类别没变。给创始人的定调:护城河是防御性的,面对无限竞争,它最终是"存亡问题"。
> 🗣️ "a moat is inherently a defensive thing and you have to have something to defend. If you have nothing to defend, don't worry about your moat." —— Harj Taggar (SPEAKER_03) `[00:16]`
> 译:护城河本质是防御性的,你得先有值得防御的东西;如果你没有任何要守的东西,就别操心护城河。
> 🗣️ "it'd make a lot more sense if you just call the thing, the seven moats, because that's really what he's talking about." —— Jared Friedman (SPEAKER_02) `[03:01]`
> 译:其实把这本书叫"七种护城河"会更好懂,因为他讲的就是护城河。
> 🗣️ "having a moat is relatively existential eventually." —— Garry Tan (SPEAKER_00) `[04:15]`
> 译:归根到底,有没有护城河是关乎存亡的事(否则无限竞争会把你的利润压到零、生意会死)。

### 2. 什么时候才该想护城河 + 前置部署工程 / When to Think About Moats & Forward Deployed Engineering `[04:20–10:18]`
**要点(中文)**: 关键是"在正确的时间"担心护城河。早期创始人该做的是:去找一个有真痛点的人,先把那个问题解决掉——世界上到处是没被软件/AI 解决的严重痛点,解决它本身就能造出十亿到千亿美元的公司。护城河是"后来的事":因为看不清长期护城河就不做某个点子,是很蠢的;更蠢的是用这个框架"提前给自己判死刑",或拿它去在两个点子之间预测五年后谁护城河更大——"根本不是这么运作的"。Diana 引用 Windsurf 的 Varun:早期唯一的护城河就是**速度**;Jared 认同"速度虽不在七种力量里,但应该算一种"。心智模型(来自 Bob McGrew):这些初创其实都是"面向实验室的前置部署工程团队(FDE)"——赛道一片 greenfield,第一步是先探明哪个垂直/产品真的值钱(两年前连"是 Cogen / IDE"都不清楚),挖到金子、别人闻风而来,才开始需要防御你挖到的宝藏。
> 🗣️ "the moats come later, like it would be like pretty dumb for somebody to decide not to work on a startup idea because they can't see what the long term moats of that idea could be" —— Jared Friedman (SPEAKER_02) `[05:32]`
> 译:护城河是后来才有的——因为看不清一个点子的长期护城河就决定不做它,是相当蠢的。
> 🗣️ "the early stages at the beginning, the only moat that startups have. It's really just speed." —— Diana Hu(转述 Windsurf 的 Varun,SPEAKER_01) `[06:09]`
> 译:在最开始的早期阶段,初创唯一拥有的护城河,其实就是速度。
> 🗣️ "I really like Varun's point that the only moat is speed. That is not one of the seven powers in the book, but I think it probably should be." —— Jared Friedman (SPEAKER_02) `[06:31]`
> 译:我很认同 Varun 的观点——唯一的护城河是速度;它虽不在书里的七种力量之列,但我觉得它应该算一种。

### 3. 流程力(Process Power)/ Process Power `[10:18–14:34]`
**要点(中文)**: 流程力 = 你搭建了一套复杂到别人难以复制的东西。书里的例子是丰田流水线,AI 版本就是"一个被多年精调、能在真实世界条件下稳定工作的复杂 Agent"(Case Text / Jake Heller 是原型;卖给银行的 Greenlight 做 KYC、Casca 做贷款发放)。大学生脑子里想的是"周末黑客松版",而黑客松版对任何人都没用——Casca/Greenlight 一旦出错银行会损失数百万美元,这是"关键任务基础设施",更像自动驾驶。Garry 补充:**更好的工程本身就是最深刻的流程力**(如 Plaid 要支撑上千到上万家金融机构的爬虫和 CICD,谁能用最新 CodeGen 最快接入每一家谁就赢)。Harj 点出"schlepp blindness":黑客松版比以往任何时候都快,但把最后 10% 做到在每天数万次请求下可靠,是工程师不爱干的 painstaking 苦活——连大实验室里造 AGI 的团队也提不起劲去死磕 KYC 工具最后 5% 的一致性。这正是护城河。
> 🗣️ "the version you build in a hackathon isn't useful to anyone. It's, like, if Casca or Greenlight fail, like, the banks will lose millions of dollars. This is, like, mission-critical infrastructure." —— Jared Friedman (SPEAKER_02) `[11:31]`
> 译:你在黑客松里搭的那个版本对谁都没用;要知道 Casca 或 Greenlight 一旦出错,银行会损失数百万美元——这是关键任务级的基础设施。
> 🗣️ "way better engineering is actually, that's, like, the most profound form of process power." —— Garry Tan (SPEAKER_00) `[11:46]`
> 译:好得多的工程能力,才是流程力最深刻的形态。
> 🗣️ "It's sort of, like, a particular type of painstaking drudgery work in a way. That I think, like, lots of engineers are just not excited to do." —— Harj Taggar (SPEAKER_03) `[13:16]`
> 译:这是一种特别磨人的苦活,我觉得很多工程师根本提不起兴趣去做(而这正是壁垒所在)。

### 4. 独占资源(Cornered Resources)/ Cornered Resources `[14:34–19:30]`
**要点(中文)**: 独占资源 = 被觊觎、不可套利、独立有价值、常带来优惠准入的资产。经典例子是药企专利 + FDA 审批(所以专利有期限);现代监管版是 ScaleAI/Palantir 与 DoD/情报机构的深度绑定——建 SCIF、常驻华盛顿、把"政府里做 AI 的人的心智份额"变成独占资源。对初创更相关的是 **FDE 模式**:坐进平时买不到好软件的客户那里,拆解一个可能很无聊的"时间-动作"工作流(邮件进来→富化→呼叫中心打电话),再翻译成自己的 prompt、evals,最终变成微调自有模型的数据集——这些都极其值钱。**最好的独占资源就是你自己的模型**(Character AI 把服务成本压低 10 倍即一例)。但要点是:别因为"没有自研模型"就以为自己完了——这只是众多护城河之一;这么早期,光靠 context engineering 拿到 80-90% 就够撑过头两年(Cursor 起步时并没做 GPT 全参微调)。真正的 10,000 英尺级威胁,是实验室哪天把模型当独占资源、限制访问。
> 🗣️ "they're going out and getting a cornered resource in the form of real data and real workflows." —— Garry Tan (SPEAKER_00) `[16:38]`
> 译:(成功的初创)正在去获取一种独占资源——真实的数据和真实的工作流。
> 🗣️ "The best cornered resource to have is a model." —— Garry Tan (SPEAKER_00) `[18:02]`
> 译:能拥有的最好的独占资源,就是一个(你自己的)模型。
> 🗣️ "even if just context engineering gets you 80 or 90% of the way there, that's plenty." —— Garry Tan (SPEAKER_00) `[18:49]`
> 译:即便只靠上下文工程就能把你带到 80-90% 的程度,那也已经足够了(别用"没有自研模型"提前把自己出局)。
> 🗣️ "The 10,000-foot scary thing is if the labs at some point decide to treat their models as a cornered resource and they restrict access." —— Harj Taggar (SPEAKER_03) `[18:21]`
> 译:从万米高空看,真正吓人的是:大模型实验室哪天决定把模型当成独占资源、限制访问权限。

### 5. 转换成本(Switching Costs)/ Switching Costs `[19:30–24:54]`
**要点(中文)**: 转换成本 = 客户被"困住",换方案在财务/运营/时间/精力上太痛,即便新方案更好也不换(经典例子:Oracle 数据库迁移、Salesforce CRM 换一次可能损失一整年生产力)。AI 公司的新玩法与 FDE 相关:Happy Robot、Salient 从每家公司高度定制的工作流入手,pilot 长达半年到一年,但一旦成功就转成七位数合同、"被 mint 住"——大企业不会再做又一次 bake-off。Jared 区分两种:老 SaaS 式(数据/系统记录搬不动,如 Salesforce、Lever)和 **AI 原生的新式**——冗长 onboarding 带来对 Agent **逻辑(而非只是数据)**的深度定制,SaaS 时代基本不存在。Garry 双面提醒:AI 同时也能**把转换成本降到零**(用 CodeGen 把数据从对手僵化系统里抽出来),这是初创可用的另一根杠杆;消费端则相反,memory / 个性化正在变成越来越强的转换成本。
> 🗣️ "very long pilot periods, which might last like six months to a year. But if they succeed, these convert into seven-figure contracts." —— Diana Hu (SPEAKER_01) `[21:13]`
> 译:pilot 周期非常长,可能持续六个月到一年;但一旦成功,就会转化成七位数的合同。
> 🗣️ "these lengthy onboarding processes that lead to deep customizations of the logic of the agent, not just the data, that didn't really exist in the SaaS era." —— Jared Friedman (SPEAKER_02) `[24:01]`
> 译:这些冗长的 onboarding 会带来对 Agent 逻辑(而不只是数据)的深度定制——这在 SaaS 时代基本不存在。
> 🗣️ "memory is already becoming a bit of a switching cost for me. It actually blew me away that Claude was so behind on memory." —— Garry Tan (SPEAKER_00) `[24:24]`
> 译:memory 已经开始成为我个人的一种转换成本了;Claude 在 memory 上落后到让我震惊。

### 6. 反向定位(Counter-Positioning)/ Counter-Positioning `[24:54–31:24]`
**要点(中文)**: 反向定位 = 做在位者难以模仿的事,因为模仿会蚕食它自己的生意。第一种形态:每个品类里都在上演"SaaS 在位者自建 Agent" vs "AI 原生公司在其之上建 Agent"的达尔文式竞争(客服里 Zendesk/Intercom/Front vs 新一代)。在位者的**致命弱点是按座席(per seat)收费**——Agent 越好用,客户需要的员工越少,越成功越自我减收;founder-controlled 的公司(如 Intercom)可能敢自我革命,非 founder-controlled 的"不抱希望"。而初创把定价改成"按交付的工作/完成的任务",反过来逼产品必须真能干完活。Harj 补第二种形态:**做第二名**——Stripe 之于 Braintree、DoorDash 之于 Grubhub;Legora 反打早入局却押注微调的 Harvey(专注应用层做更好的产品)、GigaML 靠"开箱即用更好用、上手更快"反打 Sierra/Decagon;Speak 用语音真学语言反打"更像游戏"的 Duolingo。反向定位与品牌护城河高度重叠。最典型的反向定位案例就是 Google:守着广告这头"人类史上最大现金牛",不敢自我颠覆,于是被 ChatGPT 抢走了消费 AI 的心智。
> 🗣️ "The definition of counter-positioning is doing something that is difficult for the incumbent that you are competing with to copy because it would cannibalize their business." —— Jared Friedman (SPEAKER_02) `[24:55]`
> 译:反向定位的定义,就是做一件你的在位竞争对手很难照抄的事——因为照抄会蚕食它自己的生意。
> 🗣️ "if their AI agents do a good job and actually work, those companies will need fewer employees doing this work because the work will be automated by AI agents." —— Jared Friedman (SPEAKER_02) `[26:01]`
> 译:如果它们的 AI Agent 干得好、真管用,这些公司需要做这份工作的员工就更少——因为活被 AI Agent 自动化了(于是按座席收费越成功越减收)。
> 🗣️ "there's advantage to being the second mover in a space like Stripe came after Braintree and authorized.net and a bunch of things and was able to like actually win by just building a better product." —— Harj Taggar (SPEAKER_03) `[31:39]`
> 译:做第二个进场者是有优势的——Stripe 在 Braintree、authorized.net 等之后进场,靠做出更好的产品真的赢了。

### 7. 劳动力替代的现实 & 垂直 AI 大 10 倍 / The Workforce Displacement Reality `[31:24–34:00]`
**要点(中文)**: 承接反向定位:在位者除了不愿放弃 per seat 定价,更根本的是"交付不了能真正干完活的产品"——因为它们很难重置工程文化去拥抱 AI、做 context/prompt engineering,团队做不到 AI-native,产品自然做不出来。Garry 用 YC 公司 Avoca(给 HVAC 做客服软件,类似 Service Titan)举例:软件在这类低毛利服务生意里只占 1% 钱包份额,但 Avoca 发现可以把**客服工作本身**接过来收费,占比不是 1% 而是 4%-10%——所以垂直 AI SaaS 会拿到更高钱包份额、增长更猛。Diana 概括:垂直 AI SaaS Agent 会比 SaaS 大至少 10 倍,因为它吃的是"原本花在人力工作流上的钱",而非有限的软件预算。关于替代:HVAC 客服本就是没人愿干、年流失 50-80% 的苦差,人是在"辞职"而非"被裁";留下来的人反而升级成"管理一群 AI Agent、处理疑难案例"的更有趣的工作。
> 🗣️ "customer support for an HVAC services company is not a fun job. And you can tell because all of these customer support jobs actually have like 50, 80% annual attrition rates." —— Garry Tan (SPEAKER_00) `[29:51]`
> 译:给 HVAC 服务公司做客服不是个好差事——你看这些客服岗位的年流失率高达 50%-80% 就明白了。
> 🗣️ "vertical AI SaaS agents will be 10 times, at least 10 times bigger than SaaS" —— Diana Hu (SPEAKER_01) `[29:24]`
> 译:垂直的 AI SaaS Agent 会比 SaaS 大 10 倍,至少 10 倍。

### 8. 品牌与速度 / Brand & Speed as Moats `[34:00–37:30]`
**要点(中文)**: 品牌护城河 = 你出名到即便产品对等,消费者仍因品牌效应选你(书里的例子是可口可乐)。AI 语境下品牌很难直接作为初创的护城河(需要时间积累),但效应惊人:ChatGPT 每日消费者用户数超过 Google Gemini——尽管懂模型的人都会说 Gemini 2.5 Pro/Flash 与之对等,且 Google 手握全世界的用户、是互联网最大消费品牌,OpenAI 起步时一个用户都没有,却抢先建立了"消费 AI App"的品牌,把 Google 逼到追赶。这既是品牌案例,也是反向定位案例(Google 因广告现金牛而不敢自我颠覆)。而 ChatGPT 的起源本身,又回到第一护城河——**速度**:几个月就发出来了(靠 Sam Altman、YC Research、Greg Brockman 把 Ilya 等人从 DeepMind 挖出来——人才早就在,只是那个地方没能孕育社会真正需要的东西)。
> 🗣️ "ChatGPT has more consumers using it per day than Google's Gemini." —— Harj Taggar (SPEAKER_03) `[35:28]`
> 译:ChatGPT 每天使用它的消费者数量,比 Google 的 Gemini 还要多。
> 🗣️ "brand is, it's essentially a mode when you become so well known that even if you have an equivalent product, consumers will still choose you because of the brand effects." —— Harj Taggar (SPEAKER_03) `[34:00]`
> 译:品牌本质是一种护城河——当你出名到即便产品对等,消费者仍会因为品牌效应而选择你。

### 9. 网络经济(Network Economies)/ Network Economies `[37:30–41:00]`
**要点(中文)**: 网络经济 = 用户越多,产品对每个人越有价值(Facebook 朋友越多越好玩、Visa 商户越多消费者越有用)。AI 时代网络效应的形态变成了**数据**:数据越多→自研/微调模型越好→产品越好→用户越多。ChatGPT 把历代对话喂回训练;Cursor 的免费版明确告知会用你的数据训练,"几乎是你的每一次鼠标点击、每一次击键都被喂进模型"——开发者越多、tab 补全越好、复利越滚越大。初创版:进企业拿到私有数据(Salient、Happy Robot 客户员工的使用数据),让工作流越来越好;而实现这个飞轮的第二种方式是 **evals**——把"这个工作流没跑通"的反馈拿回来迭代 context engineering,这个飞轮只有在获得越来越多真实使用后才能转起来。
> 🗣️ "network economy is described as where the value of the product increases as more users or customers get and use the product and everyone derives more value as an effect of more people using it." —— Diana Hu (SPEAKER_01) `[37:30]`
> 译:网络经济指的是:随着越来越多用户或客户获得并使用产品,产品的价值随之上升,每个人都因更多人使用而获得更多价值。
> 🗣️ "that is a flywheel that you can only achieve when you get more and more usage of your product." —— Diana Hu (SPEAKER_01) `[40:32]`
> 译:(evals 驱动的迭代)是一个只有当你获得越来越多产品使用量时,才能转起来的飞轮。

### 10. 规模经济 & 最终建议 / Scale Economies & Final Advice `[41:00–45:06]`
**要点(中文)**: 规模经济 = 砸大钱建出很大的东西,从而单位成本比谁都低(UPS/FedEx/Amazon 的物流网)。在 AI 世界,这条主要发生在**模型层**而非应用层:训练 SOTA LLM 极度资本密集,只有少数公司烧得起,烧完后推理可以很便宜——所以 DeepSeek 的公告"石破天惊",因为它似乎意味着训前沿模型比想象的便宜得多,会削弱实验室的规模护城河(Diana 澄清:DeepSeek 真正公开的是更便宜的 RL 方法,底座大模型仍很贵)。应用层少见的例子是 Exa(为 AI Agent 做搜索):像模型公司一样早早押注、爬下一大块网页(不像 Google 爬全网),固定资本投入大,但爬一次可复用给众多客户;最新一批的 Channel 3、Orange Slice 也在做类似 play。**最终建议(Garry)**:主要聚焦那条根本不在书里的第一护城河——速度;别一上来纠结"要不要成为独占资源",那是想错了方向。起点永远是:我有没有一个具体的人、有个足够痛的痛点——不是"要是能做到就好了",而是"今年拿不到晋升、可能被炒、痛到不想上班"的那种存亡级痛;能写软件缓解这种痛,就先做好从 0 到 1,别拿护城河框架把自己劝退。
> 🗣️ "You need to mainly focus on the first moat that isn't even in the book, which is speed." —— Garry Tan (SPEAKER_00) `[43:57]`
> 译:你主要要聚焦的,是那条根本不在书里的第一护城河——速度。
> 🗣️ "It's not like, oh, it'd be nice if I could do this. It's a, oh, I am not going to get promoted this year. Maybe I will get fired. Like, this is so painful that I don't want to go to work today." —— Garry Tan (SPEAKER_00) `[44:14]`
> 译:那不是"要是能做到就好了"这种痛,而是"我今年拿不到晋升、可能会被炒、痛到今天都不想去上班"这种痛——去找这种量级的痛点。
> 🗣️ "once you crawl a big chunk of the web, you can reuse that same crawl for for many different customers." —— Jared Friedman(讲 Exa,SPEAKER_02) `[43:11]`
> 译:一旦你爬下了一大块网页,同一份爬取结果就能复用给许多不同客户(这就是规模经济护城河)。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先冲速度,别先想护城河**:把交付节奏当第一护城河,压缩发布/冲刺周期到极限(对标 Cursor 早期"一天一冲刺");用"无情执行"去对抗大公司必须走 PRD/PM/运营的迟缓。切勿因看不清五年后护城河就否掉点子或在两个点子间做"护城河预测"。
- [ ] **锁定一个存亡级痛点的具体客户**:立项标准是"这个人痛到不想上班/怕被炒",而不是"要是有就好了";先从 0 到 1 解决它,护城河会在你服务客户、做产品、搞清需要什么数据的过程中自然长出来。
- [ ] **把"最后 10%"当作你的流程力护城河**:刻意去死磕黑客松版做不到的那部分——在每天数万次真实请求下的 99% 可靠性、边缘 case、垂直领域知识;这正是连大实验室都不愿干的苦活,也是你最难被复制的壁垒。
- [ ] **用 FDE 模式把"真实数据 + 真实工作流"变成独占资源**:坐进买不到好软件的客户现场,拆解其时间-动作流程,翻译成自己的 prompt → evals → 微调数据集;别因"没有自研模型"自我判死,context engineering 先拿 80-90% 就够撑两年。
- [ ] **设计 AI 时代的转换成本,并按"交付的工作/任务"定价**:用长 onboarding 把 Agent 的**逻辑**(而非只是数据)为客户深度定制,把 pilot 做成七位数合同的入口;用"按完成的活收费"直接反打在位者的 per seat 软肋(同时你的产品被逼着真能干完活)。
- [ ] **考虑当"第二名"做反向定位**:进入已有早期赢家的垂直时,靠"开箱即用更好、上手更快、专注应用层"反打(对标 Legora vs Harvey、GigaML vs Sierra/Decagon、Speak vs Duolingo),尤其瞄准在位者因蚕食自身而不敢做的动作。
- [ ] **搭建 evals + 数据飞轮当网络护城河**:把每次"没跑通"的反馈系统化回流,迭代 context engineering;争取合法使用产品数据(如免费版数据训练),让用户越多→模型/产品越好→用户更多的复利转起来。

## 🔑 关键术语 / 概念
- **Seven Powers / 七种力量(= 七种护城河)** — Hamilton Helmer 2016 年著作提出的七类可持续竞争优势:流程力、独占资源、转换成本、反向定位、品牌、网络经济、规模经济;Jared 认为该叫"seven moats"更贴切。
- **Process Power(流程力)** — 你搭建了复杂到难以复制的系统;AI 版本 = 多年精调、在真实条件下稳定工作的复杂 Agent,核心在把最后 10% 做到 99% 可靠。
- **Cornered Resource(独占资源)** — 被觊觎、不可套利、独立有价值的资产;AI 里的最佳形态是自研模型,更现实的是 FDE 拿到的真实数据/工作流与客户心智份额。
- **Switching Cost(转换成本)** — 客户换方案太痛而被困住;AI 新形态 = 长 onboarding 带来的对 Agent 逻辑(而非仅数据)的深度定制,以及消费端的 memory/个性化。
- **Counter-Positioning(反向定位)** — 做在位者难以照抄的事,因为照抄会蚕食其现有生意(如打在位者的 per seat 收费软肋、或"做第二名")。
- **FDE(Forward Deployed Engineer,前置部署工程师)** — 贴着客户现场部署/配置的工程模式;初创借此拿到真实数据与工作流,是构筑独占资源与转换成本的关键路径。
- **Schlepp blindness / painstaking drudgery** — 对"又苦又烦但必要"的苦活的盲视;把 AI 工具从黑客松 demo 打磨到大规模可靠的最后一段,正是这种苦活,也是壁垒。
- **Context engineering(上下文工程)** — 不做全参微调,靠组织上下文就把 Agent 带到 80-90% 可用;早期初创的主力手段。
- **Evals(评测)** — 把"工作流没跑通"的反馈回流迭代的机制;被反复称为 AI 初创的关键护城河与数据飞轮引擎。
- **Per seat pricing(按座席/人头收费)** — SaaS 在位者的定价模式,也是其被反向定位打击的致命弱点:Agent 越成功→座席越少→收入越减。
- **Wallet share(钱包份额)** — 软件在客户总支出里的占比;垂直 AI SaaS 通过接管人力工作流,把份额从 1% 提到 4%-10%,故"比 SaaS 大 10 倍"。

## 🔖 高价值金句时间戳
- `[00:16]` "a moat is inherently a defensive thing and you have to have something to defend. If you have nothing to defend, don't worry about your moat." — 护城河是防御性的;没有值得守的宝藏前,别为护城河焦虑。
- `[05:32]` "the moats come later ... pretty dumb for somebody to decide not to work on a startup idea because they can't see what the long term moats" — 别用"看不清长期护城河"劝退自己,这是最常见也最蠢的错误。
- `[06:31]` "the only moat is speed. That is not one of the seven powers in the book, but I think it probably should be." — 早期第一护城河是速度,虽不在七种力量之列却最该重视。
- `[13:16]` "a particular type of painstaking drudgery work ... lots of engineers are just not excited to do." — 流程力护城河藏在别人不愿干的最后 10% 苦活里。
- `[18:49]` "even if just context engineering gets you 80 or 90% of the way there, that's plenty." — 没有自研模型也别自我判死,context engineering 足够撑过头两年。
- `[26:01]` "if their AI agents do a good job and actually work, those companies will need fewer employees ... automated by AI agents." — 反向定位打在位者软肋:per seat 定价越成功越自我减收。
- `[29:24]` "vertical AI SaaS agents will be 10 times, at least 10 times bigger than SaaS" — 吃"人力工作流的钱"而非有限软件预算,垂直 AI 天花板远高于 SaaS。
- `[44:14]` "this is so painful that I don't want to go to work today." — 立项要找的痛点量级:存亡级、痛到不想上班,而非"有就好了"。
