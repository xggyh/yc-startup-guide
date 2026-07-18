# AI 创业公司的 FDE(前置部署工程师)实战手册 / The FDE Playbook for AI Startups with Bob McGrew

> **来源**: [The FDE Playbook for AI Startups with Bob McGrew](https://www.youtube.com/watch?v=Zyw-YA0k3xo) · Y Combinator · 2025-09-08 · 时长 50:42
> **讲者**: 嘉宾 Bob McGrew(前 OpenAI 首席研究官,主导 ChatGPT / GPT-4 / o1;Palantir 早期高管、FDE 模式共建者;PayPal 早期工程师)；主持 Jared Friedman、Diana Hu、Harj Taggar(YC《The Lightcone》播客;Garry Tan 本期缺席)
> **一句话定位**: 用 Palantir 发明的"前置部署工程师(FDE)"打法,系统讲清 AI Agent 创业为何要"把不可规模化的事规模化地做"——如何选问题、组团队、按结果定价、把单客户方案泛化成产品,并识别当下最大的创业机会。

## 🎯 TL;DR(中文核心要点)
- **FDE 的本质是"doing things that don't scale at scale"**:不是权宜的高触达,而是当市场高度异质、没有既有产品可替代时,唯一可行的打法,并可能成为护城河。Bob 的前三条建议都是"能不做就别做",逼到"不做就活不下去"时,它才是你的 moat。
- **卖的是"结果"(outcome / 已解决的问题),不是软件安装、席位或用量**。定价按交付价值走,合同规模应随时间越做越大(land & expand),而不是像 SaaS 那样越做越小、越标准。
- **只做客户 CEO 的"前五大优先级"**;若带不来 3x–10x 的阶跃式改变就别碰,否则不如卖个简单软件。先解决一个,再"赢得资格"去承接同一客户内更有价值的问题。
- **团队分两类角色**:Echo(懂行业、敢当"异端/叛逆者"的嵌入式分析师 + 客户关系)与 Delta(能极快写原型、"能吃苦 eating a lot of pain"的部署工程师);产品团队负责把单客户的"砂石路"抽象成服务未来 5–10 个客户的"高速公路"。
- **抽象层要"上提一级"**:别把为单个客户做的东西直接塞进产品(过度特化陷阱)。像 Palantir 的 ontology 那样,把每客户的特化信息编码在可定制层,产品团队守住可泛化的产品愿景。
- **Demo 驱动开发**:好 demo 会在客户心里"制造渴望(creating desire)",逼你从"我能造什么"切到"客户到底要什么",并提前暴露特性间的衔接痛点。
- **早期敢承担全部风险**(you pay us if it works),用"我们真的能执行"这一不对称优势拿下大企业;但要搞清组织内"谁必须点头"——IT/安全团队不像创始人思考,需要高层授予 authority to operate 来绕过。
- **为什么 AI Agent 创业都在抄这套**:AI agent 没有 incumbent product、市场极碎片、产品发现量巨大,而"能力(capabilities)跑得远快于采用(adoption)"——填补"能力能做的"与"客户能采用的"之间的鸿沟,就是当下最大机会。

## 🧭 适合谁 / 什么时候看
- 正在或考虑用 FDE / 高触达打法切入大企业的 AI Agent 创始人与早期团队。
- 面对高度异质、无既有产品可替代的市场,纠结"我这是不是在做外包咨询"的团队。
- 需要设计 outcome-based 定价、组建 Echo/Delta 团队、平衡"客户定制 vs 可泛化产品"的创始人。
- 处于 0→1(拿前几个大客户)阶段,想知道"高触达到底能推多远、何时该抽象成产品"的人。

## 📝 分段精读

### 1. 从 PayPal 到 OpenAI:什么是前置部署工程师 / What an FDE Is `[00:29–03:19]`
**要点(中文)**: Bob 的履历横跨 PayPal、Palantir、OpenAI。FDE 的定义很简单:一个通常是工程师的技术人员,坐在客户现场,填补"产品能做的"与"客户需要的"之间的鸿沟。落地方式是:带着现有产品去新客户,面对一个你从没解决过、但相信"再花点(甚至很多)功夫能解决"的问题,由 FDE 在产品团队协助下,把产品改造成对这个客户真正可用、能交付高价值结果的形态。这一年 Bob 见到的大量创业者,几乎"只想学 FDE 怎么玩"。
> 🗣️ "a forward deployed engineer is someone, typically technical and engineer, who sits at the customer site and fills the gap between what the product does and what the customer needs." —— Bob McGrew
> 译:前置部署工程师通常是个技术型工程师,他坐在客户现场,填补"产品能做的"与"客户需要的"之间的鸿沟。

### 2. Palantir 如何发明它:砂石路与高速路 / How Palantir Invented It `[03:19–07:56]`
**要点(中文)**: Palantir 起步是给情报界(间谍)做软件,而没人认识间谍、间谍也不会告诉你他们干什么。于是他们先做一个 demo 拿去客户面前,被骂"这跟我们做的完全无关",再追问"那你想要它怎样"并逐条记下——这正是今天"走出办公室、做用户想要的东西"的标准建议。真正的转折在于:传统剧本是"早期贴近客户找到 PMF,之后转向规模化、拉开与客户的距离、把所有客户一视同仁";但 Palantir 发现每个客户需要的产品都略有不同,于是 Shyam Sankar 反其道而行——把 FDE 当作**产品发现**的手段:FDE 到现场铺一条通往目标的"砂石路",产品团队再看着它,想清楚"如何泛化到接下来的 5 个、10 个客户",把砂石路修成"高速公路"。
> 🗣️ "the FDE goes and builds like a gravel road to where the product needs to go and then the role of my team ... was to look at that and basically figure out how that should generalize to the next five customers or the next 10 customers and then turn that gravel road into like a paved super highway" —— Bob McGrew
> 译:FDE 去现场铺一条通往产品目标的"砂石路",而我的团队(产品工程团队)的职责是看着它,想清楚它该如何泛化到接下来的 5 个、10 个客户,再把这条砂石路修成一条"高速公路"。
> 🗣️ "If you have the opportunity to just scale, treat all the customers the same, go ahead and do that. But it didn't work for us." —— Bob McGrew
> 译:如果你有机会直接规模化、把所有客户一视同仁,那就去做。但这条路对我们不管用。

### 3. 现场做产品发现 vs 销售式发现 / Product Discovery in the Field vs. Sales `[07:56–09:51]`
**要点(中文)**: 主持人问:卖给政府/国防,直觉是雇个穿西装、在国防部干了 20 年、带将军吃牛排的老销售(像 Don Draper)。但 Palantir 没这么做——那些人问"我干嘛不去大军火商而来你这",且和公司文化不合,试过几乎都失败。销售式产品发现是"从外部"和人聊,不如 FDE"从内部"解决问题有效。关键纪律:必须解决客户 CEO 的前五大优先级之一,否则客户没有足够动力熬过"重新造一块产品"的艰难路径;解决完第一个问题后,FDE 能从内部发现更有价值、外人根本看不出你能解的问题——于是从"怎么把同一样东西卖给每个客户"转向"land and expand"。
> 🗣️ "if you're not solving one of the top five priorities for the CEO it's probably not going to work they probably won't have the energy to persist through the much more challenging route" —— Bob McGrew
> 译:如果你解决的不是 CEO 的前五大优先级之一,基本上是行不通的——客户多半没有足够的能量,去熬过那条艰难得多的路径。
> 🗣️ "it switches from how do I sell the same thing to each customer to how do I land and expand" —— Bob McGrew
> 译:它于是从"我怎么把同一样东西卖给每个客户",转变为"我如何先落地、再扩张"。

### 4. Echo 与 Delta:两类人怎么配 / Echo and Delta Teams `[09:51–13:34]`
**要点(中文)**: FDE 团队的两个核心角色始终不变。**Echo(嵌入式分析师)**:到客户现场、与用户交谈、判断哪个 demo/用例最有意义、找出可解的关键问题,同时兼任客户关系的 account manager。**Delta(部署工程师)**:极快写代码、"能吃很多苦",把想法变成能真跑起来的原型并部署,而且要在几个月的极短周期内完成——设定好几个月后向客户 leadership 汇报进展,汇报顺利就全组织铺开。选人画像:Echo 要来自该行业、有深厚领域知识,更要是"叛逆者/异端(heretics)"——认清现状不行、才可能推动阶跃式改变;做不出 3x–10x 的改变就没必要折腾。Delta 要擅长快速原型,而**不是**追求抽象完美、代码能维护十年的"匠人"——第一版经常要被丢掉重写。
> 🗣️ "the deployed engineers were effectively software engineers typically very good at writing code extremely quickly eating a lot of pain as we put it" —— Bob McGrew
> 译:部署工程师本质上是软件工程师,通常极擅长飞快地写代码,用我们的话说就是"能吃很多苦"。
> 🗣️ "They need to be rebels ... Or Sean would probably call them heretics. They need to be someone who understands how things are done right now and recognizes that it's insufficient" —— Bob McGrew(谈 Echo 画像)
> 译:他们必须是叛逆者——Sean 大概会叫他们"异端"。他们得是那种懂得现状是怎么运作的、并且认清它根本不够用的人。

### 5. 是外包咨询,还是真软件?/ Consulting or Real Software? `[13:34–17:54]`
**要点(中文)**: 这套训练"就是"创始人训练——难怪 Palantir 孵出大量创业者:你在每个客户现场都像在当创始人,只是手里多了一件强大的产品杠杆。针对"FDE 不过是包装花哨的咨询、永远做不成软件生意"的质疑,Bob 不回避:2015 年前后确有这风险。判据在商业模型:新客户部署早期你可能是亏钱的;但随着产品因产品发现越来越贴合客户,现场需要的人越来越少,同时你"赢得资格"去解决客户更重要的问题,于是"单位价值的成本"持续下降——利润率从负转正(可能一年、也可能数年),这才证明你在交付**可重复的真实价值**。产品团队的关键作用:守住产品愿景,把单客户方案"上提一级"泛化;否则会掉进"把为一个客户做的东西直接塞进产品、结果过度特化"的经典失败。
> 🗣️ "your profit margins start off negative, but then ultimately become positive after some period of time ... And if you look at it from that perspective, you can see that you're actually delivering real, repeatable, value." —— Bob McGrew
> 译:你的利润率一开始是负的,但经过一段时间(可能一年、也可能数年)后最终转正。从这个视角看,你就能看出自己其实在交付真实、可重复的价值。
> 🗣️ "there's a classic failure mode here, where the FDE implements something for one customer ... you bring it directly into the product. And it turns out ... you're building something that's over-specialized for one customer." —— Bob McGrew
> 译:这里有个经典的失败模式:FDE 为某一个客户实现了某个东西,你就直接把它搬进产品——结果你造出来的是一件为单个客户过度特化的东西。

### 6. Ontology 的诞生:把抽象层上提一级 / The Birth of Palantir's Ontology `[17:54–23:04]`
**要点(中文)**: 最基础的泛化例子就是 Palantir 的 ontology。给情报机构做时,若"人一张表、钱一张表、船一张表"这样硬编码,部署到多个客户后 schema 就崩了。正确做法是把类型上提到更高抽象:数据库只保留 objects / properties / media / links 的通用概念,而"这是人、这是船、这是资金流"这类每客户特化的信息,交给 ontology 层、由 FDE 团队按客户定义。Bob 说他长期没招 PM,后来面试"别家的顶尖 PM",让他们在这个抽象层次上思考,他们做不到——只会说"这个客户的流程该长这样",而正确的是"上提一级、改 ontology 让这个特化需求能跨客户通用"。文化张力必然存在:FDE 在现场只面对一个具体问题、理应取最简解(砂石路);产品团队的高速路要途经好几个客户,所以长得不一样。Palantir 的做法是把初始客户的 FDE、以及其他几个相似客户的 FDE 都拉进设计讨论——当大家看到三种细微不同的 workflow,"该通用还是该特化"的争论就消解成"大家在解同一个问题",激励自然对齐。
> 🗣️ "instead of thinking about specific types of objects, we should allow that to be defined per customer by the forward-deployed engineering team. And so that's the sort of origin story of where Palantir famously got its ontology." —— Bob McGrew
> 译:与其去想具体的对象类型,我们应该让这些由前置部署工程团队"按客户"来定义。这就是 Palantir 那著名的 ontology 的起源故事。

### 7. 为什么 AI 公司都在采用它 / Why AI Companies Adopt It `[23:04–36:17]`
**要点(中文)**: 这是全片信息密度最高的一段。Bob 直言:"别在家试(don't do this at home)"——前三条建议都是能避就避,大概率你只是在做服务;只有当你拼命想避开却失败、发现它是市场里唯一行得通的路时,它才是护城河。为什么 Palantir 必须采用?因为市场不是一个连贯市场,而是高度异质的**细分(segments)**集合——反扩散与反恐、造核弹与造 IED 的 workflow 完全不同;在每个细分内找到 PMF、低定制复制,再攻下一个需要新技术的细分。"segment ≠ customer",大企业一个客户可能就是上万用户。为什么 AI Agent 也这样?因为你在造一个全新的产品品类,没有 incumbent product 可替代,产品发现量巨大,而且"到底什么叫做 AI agent"本身可能有很多种不同的东西、现在还没人知道——五年后回看,也许"AI agent"根本不是一个东西,而是我们在做的一堆不同的事。**定价**:卖的不是软件安装,而是 outcome / "我已经解决了这个问题";合同会被推向越来越大、越来越灵活。**不对称**:大企业既不相信自己能成、也不相信你能成(因为他们见过太多大项目失败);而你知道自己真能执行——所以早期理应由创业公司承担全部风险(做成/上量才付费)。**组织阻力**:要想清"组织里谁必须点头"——IT/安全团队不像创始人思考、不与终端用户对齐,得靠你所解决的 CEO 前五大问题,把高层拉进来授予 authority to operate、绕过为内部自研设的规矩。
> 🗣️ "my first, second, and third pieces of advice to people who are thinking about trying an FDE strategy is, don't do this at home. If you can avoid it, it's probably bad for you ... only if you really try hard not to do it and fail. Then ... maybe actually it's a moat for you if it's the only thing that can possibly work in your market." —— Bob McGrew
> 译:对想尝试 FDE 策略的人,我的第一、第二、第三条建议都是:别在家试。能避开就避开,它多半对你有害……只有当你真的拼命想避开却失败了——那时候,如果它是你的市场里唯一可能行得通的路,它才可能成为你的护城河。
> 🗣️ "With AI agents, there is no incumbent product. And so ... that I think is why you're seeing the FDE model taking off because there's so much product discovery to do. And you can only do it from inside the enterprise." —— Bob McGrew
> 译:对 AI agent 来说,没有既有产品可替代。我认为这正是 FDE 模式起飞的原因——要做的产品发现太多了,而这只能从企业内部去做。
> 🗣️ "you're not selling the installation of software, you're selling an outcome. As Sean would say, you're selling that you have solved a problem." —— Bob McGrew
> 译:你卖的不是软件的安装,而是一个结果。用 Sean 的话说,你卖的是"你已经解决了这个问题"。

### 8. 成功指标长什么样:把合同做大 / What Success Metrics Look Like `[36:17–41:14]`
**要点(中文)**: 这里精确点出 PMF 策略与 FDE 策略的分野:PMF 策略是"每个客户的工作量越做越少、压低成本、合同规模保持不变";FDE 策略是"把合同规模越做越大"——你为这个客户(及未来客户)做越来越有价值的工作,因此每客户的定制量维持不变也没关系。可测的 KPI 是合同规模,但更本质的是"你交付的 outcome 的价值"(能否变现/定价/捕获是另一回事)。第二个要盯的指标:你对这个 outcome 的**产品杠杆(product leverage)**是否在上升——你的另一个关键"客户"其实是 FDE,产品要让 FDE 无需再拉三个工程师就能交付更多价值;第二个客户应比第一个省力,越往后越省。若平台抽象对了,连做"相似但不同"的用例时都更省力,甚至 FDE 会用你造的能力去解决完全不同的新问题——这时产品内部会出现"FDE 主动选择用你的抽象、而不是自己 hack 一次性方案"的需求信号。Bob 反复强调这过程"充满 pain",判断何时该抽象、FDE 与创始人谁对,归根结底是 judgment。并延伸到:你要造的是一家"学习型公司"——建议年轻人加入"年轻、快速成长、还没成功、还在摸索"的公司,那正是成为创始人的最佳训练。
> 🗣️ "In the product market fit strategy, you want to be doing less work for every customer ... keep the contract size the same. In the FD strategy, you want to drive the contract size up." —— Bob McGrew
> 译:在 PMF 策略里,你想为每个客户做更少的工作、把合同规模保持不变;而在 FDE 策略里,你要把合同规模不断做大。
> 🗣️ "your other key customer is the FTE [FDE]. Your product should be ... delivering leverage to the FDE who's delivering that outcome at the customer site. And that amount of product leverage should be going up over time." —— Bob McGrew
> 译:你的另一个关键客户其实是 FDE。你的产品应当为那个在客户现场交付结果的 FDE 提供杠杆,而这份产品杠杆应当随时间不断上升。

### 9. 用 Demo 驱动开发 / Building with Demo-Driven Development `[41:14–44:56]`
**要点(中文)**: 因为要不断向新客户演示,你被迫持续做新 demo;而只要产品对路,demo 驱动开发效果极好。Palantir 早期只有一个 demo——一个"阻止恐怖袭击"的完整流程;每集成一个新特性(直方图、地图……),都必须回答"它如何帮到走这条流程、正在阻止阴谋的分析师""它如何与已有特性协同"。当你从"我能造什么"出发,只会孤立地想每个特性;而做 demo 时你被迫从**客户视角**出发。好 demo 的标准是:客户一看就"产生渴望(creating desire)",想伸手抓住、带进自己的生活——看到这个,你就知道命中了真实痛点。同时,demo 逼你打磨特性之间的衔接(哪怕只是从一个特性切到另一个的路径要顺滑),这些产品痛点通常要到部署后才暴露,而 demo 让你提前看到。核心是:demo 把你思考的焦点从"我能造什么"切换到"客户到底想要什么、我有没有在解他的痛"。
> 🗣️ "a really good demo is something where you show it to the customer and you are creating desire in that customer for what you're doing. They have to see what you're doing and just want to reach out and grab it and bring it into their life. And if you see that, then you know that you've identified a real pain for the customer." —— Bob McGrew
> 译:真正好的 demo 是:你演示给客户看,你在客户心里制造出渴望。他们看到你在做的东西,就想伸手抓住、把它带进自己的生活。看到这一幕,你就知道自己命中了客户的真实痛点。
> 🗣️ "what the demo does is it changes the locus of what you're thinking about from thinking about what can I build to what is it that the customer wants?" —— Bob McGrew
> 译:demo 的作用,是把你思考的焦点从"我能造什么"转移到"客户到底想要什么"。

### 10. 加入陆军预备役 & 给创始人的机会 / Army Reserve & Opportunities for Founders `[44:56–50:42]`
**要点(中文)**: Bob 加入美国陆军预备役 Detachment 201(强调仅代表个人观点),担任中校、真受训、真宣誓——是"有 skin in the game"的军官而非旁观顾问,把 FDE 那套用在陆军转型上(看清 leadership 的前五大优先级、就地找问题、必要时上升到高层修正)。给创始人的机会(他难得戴上"研究者帽子"):能力提升极快——把 2024 年 4 月 GPT-4o 到 2025 年 4 月 o3 这一年放在一起看,进步惊人,且会持续;但**采用(adoption)远远跟不上能力的速度**。未来五年会是:能力一路狂奔,而世界却越来越"平淡"(你坐在 Waymo 里只会抱怨堵车)。就像 FDE 填补"产品能做的"与"客户需要的"之间的鸿沟一样,如今的巨大机会在于填补"能力能做的"与"客户能采用的"之间的鸿沟——AGI 不会自己发生,需要人的巧思、探索、和大量吃苦去推动采用。Jared 的类比:OpenAI 像"总部产品团队",创业公司则是在外面想办法让研究成果被采用的 FDE——Bob 认同这可能正是 FDE 策略令人兴奋的底层真相。
> 🗣️ "the adoption is not anywhere near what you would expect from the speed of these capabilities." —— Bob McGrew
> 译:采用的速度,远远达不到你根据这些能力的进步速度所应期待的水平。
> 🗣️ "this is a time where there's so much availability to fill the gap between what the capabilities can actually do and what the customers are able to adopt." —— Bob McGrew
> 译:当下有着巨大的空间,去填补"能力实际能做到的"与"客户能够采用的"之间的鸿沟。
> 🗣️ "AI needs to be adopted. It's something that doesn't just happen by itself, but you need human ingenuity and exploration and while dealing with a lot of pain in order to make that happen." —— Bob McGrew
> 译:AI 需要被采用。它不会自己发生,你需要人的巧思、探索,并在过程中吃很多苦,才能让它真正发生。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **锁定 CEO 的前五大优先级**:从中挑一个能带来 3x–10x 阶跃改变的问题作为首个部署,拒绝"客户觉得好交付但其实不痛"的活。
- [ ] **把定价从 seat/usage 改成 outcome-based**:早期主动承担风险(做成才付费/上量才付费),再随交付价值把合同越做越大(land & expand),而不是压小合同。
- [ ] **组两类人 + 挖一个 FDE 老兵**:Echo(懂行业、敢质疑现状的"异端")+ Delta(能极快出原型、抗压"能吃苦"的工程师);若可能,从做过真 FDE 的人里挖一个进核心岗,机制差异很难自己摸索出来。
- [ ] **建立"砂石路→高速路"流水线**:FDE 单客户方案 → 拉上多个相似客户的 FDE 与产品团队一起评审 → 抽象出服务下一批客户的可泛化产品;把"抽象层上提一级"当纪律,防过度特化。
- [ ] **维护一个端到端故事化 demo**:每加一个特性都追问"它如何帮到走这条流程的用户、如何与已有特性协同",以"客户是否想伸手抓住"作为真痛点的验证标准。
- [ ] **提前排查"谁必须点头"**:梳理 IT/安全/合规/on-prem 等阻力点,借你所解决的 CEO 级问题争取高层授予 authority to operate,别让底层组织规则卡死部署。
- [ ] **押注"能力—采用鸿沟"**:选一个能力已经足够、但采用严重滞后的细分,用 FDE 从企业内部把"能力"翻译成"可采用的结果"。

## 🔑 关键术语 / 概念
- **Forward Deployed Engineer(FDE / 前置部署工程师)** — 驻客户现场、填补"产品能做的"与"客户需要的"之间鸿沟的技术工程师;卖结果而非软件。
- **Echo team(嵌入式分析师)** — 到现场做产品发现、判断关键用例、兼任客户关系;画像是懂行业且敢当"异端/叛逆者"。
- **Delta team(部署工程师)** — 极快写原型、交付可用软件、"能吃苦";不是追求抽象完美、代码可维护十年的匠人。
- **Ontology(本体)** — Palantir 的通用数据抽象(objects / properties / media / links),把每客户的特化信息编码在 ontology 层,而非硬编码进产品。
- **Gravel road → Paved highway(砂石路→高速路)** — FDE 为单客户快速搭的粗糙方案 vs 产品团队泛化后服务多客户的成熟产品。
- **Land and expand(先落地再扩张)** — 先解决一个高价值问题,再"赢得资格"在同一客户内发现并承接更多、更有价值的问题。
- **Outcome-based pricing(按结果定价)** — 卖"已解决的问题/交付的价值",而非软件安装、席位或用量;合同随时间越做越大。
- **Doing things that don't scale at scale(把不可规模化的事规模化地做)** — FDE 精髓:对每个市场细分反复、可规模化地执行高触达的产品发现。
- **Demo-driven development(Demo 驱动开发)** — 以端到端 demo 为核心组织开发,用"是否在客户心中制造渴望"验证真需求、暴露特性衔接痛点。
- **Segment vs customer(细分 vs 客户)** — 市场是异质细分的集合;在每个细分内找 PMF、低定制复制,再攻下一个需要新技术的细分(一个大客户可能就是上万用户)。
- **Authority to operate(授权运营)** — 借高层授权,绕过为内部自研设立、却会卡死外部创业公司的 IT/安全规矩。

## 🔖 高价值金句时间戳
- `[00:00]` "The FDE model effectively is doing things that don't scale at scale." — 一句点破 FDE 与"do things that don't scale"的差别:是把不可规模化的事**规模化地**做。
- `[24:33]` "don't do this at home. If you can avoid it, it's probably bad for you ... only if you really try hard not to do it and fail. Then ... maybe actually it's a moat" — FDE 不是首选,是被市场逼出来、避无可避时才成立的护城河。
- `[26:xx]` "With AI agents, there is no incumbent product ... there's so much product discovery to do. And you can only do it from inside the enterprise." — AI Agent 天然适配 FDE 的根因:没有既有产品、产品发现量巨大、只能从企业内部做。
- `[29:13]` "you're not selling the installation of software, you're selling an outcome ... you're selling that you have solved a problem." — AI 定价的心智转变:卖结果,不卖软件。
- `[41:14]` "a really good demo is ... creating desire in that customer ... They have to see what you're doing and just want to reach out and grab it" — 好 demo 的唯一验证标准:客户想伸手抓住。
- `[47:43]` "the adoption is not anywhere near what you would expect from the speed of these capabilities." — 当下最大机会:填补能力与采用之间越拉越大的鸿沟。
