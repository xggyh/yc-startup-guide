# 好消息:大厂做不好 AI —— 创业公司的机会窗 / Good News For Startups: Enterprise Is Bad At AI

📄 **[点此查看全文转录 / Full transcript »](../transcripts/DULfEcPR0Gc.md)**

> **来源**: [Good News For Startups: Enterprise Is Bad At AI](https://www.youtube.com/watch?v=DULfEcPR0Gc) · Y Combinator · 2025-10-30 · 时长 21:43
> **讲者**: The Lightcone 播客 —— Garry Tan(YC CEO,主持,SPEAKER_00)、Jared Friedman(SPEAKER_03)、Diana Hu(SPEAKER_01)、Harj Taggar(Triplebyte 创始人,SPEAKER_02)
> **一句话定位**: 用 MIT "95% 企业 AI 项目失败" 报告的真相,论证大厂根本建不出能用的 AI —— 这正是 AI Agent 创业者切入企业市场、拿下大合同的历史性机会窗。

## 🎯 TL;DR(中文核心要点)
- MIT 报告被 X 上的标题党曲解成 "AI 是骗局";真相是 **企业内部/咨询公司自己建 AI 大多失败,而向外部创业公司采购的成功率高得多**(报告样本 2/3 是自建/咨询,1/3 是外购,外购成功率远高)。
- 大厂建不出好软件不是偶然:连有无限资金和顶尖人才的 Apple 都做不好日历 app。普通企业内部 IT + Deloitte/EY 咨询,产出通常很差。
- 企业 AI 落地难,核心不是技术,而是 **政治、部门利益、老旧割裂的 systems of record**;既需要咨询公司的"协调对齐"能力,又需要真正能写代码把系统建出来的工程能力,而这两者很少同时具备。
- 能赢的创业者是 **稀有的"多面手"**:既有最前沿的 AI + 产品品味,又懂人、懂业务流程,能把混乱的人类流程 grok 成产品。这就是"每个流程里都有一个 startup-shaped hole"。
- 打法不是标准 SaaS 即插即用,而是 **深度嵌入业务流程、深度集成到 systems of record**,慢但一旦插进去,回报(pot of gold)极大,且切换成本就是护城河。
- 进大厂的实操:找一个"想创业但不敢的"内部 champion,和他做朋友(do things that don't scale);找被大厂收购过的创始人帮你引荐、教你走采购和内部政治。
- Karpathy 说 agent 被高估,其实是"你不能给个 prompt 就指望它一次做对,还得做数据、context、evals、tooling"—— 对创业者这恰恰是巨大的机会,不是唱衰。
- 别被 AI Doomer 影响者带偏:AI 确实极难落地(只有约 5% 成功),但顶尖 YC 创始人(录取率 <1%)恰恰就是能做出那 5% 的人。

## 🧭 适合谁 / 什么时候看
- 正准备做 **AI Agent / 企业级 AI 产品** 卖给大公司(尤其银行、金融、传统行业)的创始人。
- 被 "95% AI 项目失败"、"ChatGPT 套壳没有护城河" 这类论调劝退、心里犯嘀咕的技术创业者。
- 正在打大客户、卡在 bake-off / 采购 / 内部政治环节,需要 go-to-market 打法参考的早期团队。

## 📝 分段精读

### 1. 拆穿 "95% AI 项目失败" 的迷思 / Debunking the MIT "95% fail" myth `[00:36–02:08]`
**要点(中文)**: Garry 吐槽 AI 影响者拿 MIT《State of AI in Business》报告当"AI 是骗局"的证据。Jared 真去读了报告,发现被疯传的是"推特版"的曲解 —— 连一些大学生都以为"YC 吹的 AI 创业都不行"。但报告实际上恰恰印证了这个播客一直讲的:真实世界里 AI agent 什么样、哪些品类和打法在 work。Diana 补充,关键区别在 go-to-market:不是标准企业销售,而是把团队"嵌入业务流程、深度集成 systems of record"。
> 🗣️ "the more I read the study, the more I realized it was actually confirming a lot of the things we've talked about here on this podcast about what AI agents are really like in the real world" —— Jared Friedman
> 译:我越读这份报告,越发现它其实印证了我们在这个播客里一直讲的东西 —— 真实世界里的 AI agent 到底是什么样子。
> 🗣️ "when you do succeed and plug into the systems of record, the pot of gold is actually quite big. But it does take a long time." —— Diana Hu
> 译:一旦你真的成功接入企业的 systems of record,那桶金非常大 —— 但这需要很长时间。

### 2. 为什么失败率这么高:连 Apple 都做不好软件 / Even Apple is bad at software `[02:40–04:30]`
**要点(中文)**: Garry 给出一个心智模型:企业想做成一件事,先靠内部 IT,做不了就找 EY / Deloitte 这类咨询公司 —— 于是"两个问题变一个问题"。世界上真正被建出来的软件,大多数都非常差。他的最爱例子:Apple 有无限资金和无限顶尖人才,却连日历 app 都做不好,你几乎每天都会撞上奇怪的 bug。那连 Apple 都做不好,普通公司的内部 IT、Deloitte/EY 又怎么可能做好?
> 🗣️ "So, Apple, a company with infinite resources and infinite access to the smartest people in the world, cannot make a good calendar app." —— Garry Tan
> 译:Apple —— 一家有无限资源、能接触全世界最聪明的人的公司 —— 连一个好用的日历 app 都做不出来。

### 3. 让企业软件真正跑起来,难在哪:自建 vs 外购 / Why it's so hard, and buy-vs-build `[04:29–11:08]`
**要点(中文)**: Harj 点出真正的难点是 **政治、部门利益和老旧割裂的系统**。咨询公司(EY)的价值在于把数据、客服、IT 各团队拉到一起、写出大家都认的 spec(扮演调停者),但下一步"真的把它建出来",咨询没有技术能力,内部系统又太老太割裂 —— 于是既需要咨询的协调、又需要工程的实现,最后往往做出一头"委员会设计的骆驼"。Jared 给出报告的关键数据:样本中 2/3 是企业自建或咨询代建,1/3 是外购;**外购(如 Greenlight、Tactile)的成功率远高于自建**。案例:Tactile 给银行做实时 KYC/AML 决策引擎,Citibank/JPMorgan 自建要 3–5 年、耗资数千万美元,Tactile 用一个 REST API 就搞定;Greenlight 曾因银行"信任 EY"而丢单,结果 EY 花一年没做出来,银行回头找 Greenlight,现已上线可用。Garry 总结:世界上真正稀缺的是既懂产品又懂工程、还能走出"coding cave"理解银行业务的多面手 —— 所以"每个流程里都留着一个 startup-shaped hole"。
> 🗣️ "enterprises are mostly trying to build things in-house, but the success rate of the ones where the enterprise went with an outside vendor, like a Greenlight or a Tactile, was much higher than the success rate of when they tried to build stuff themselves." —— Jared Friedman
> 译:企业大多想自己内部建,但那些选择了外部供应商(比如 Greenlight 或 Tactile)的项目,成功率远高于自己动手建的。
> 🗣️ "So for now, there's just this startup-shaped hole in basically every process that's going on in the world." —— Garry Tan
> 译:所以就现在而言,世界上几乎每一个流程里,都留着一个"创业公司形状的洞"等着被填上。
> 🗣️ "you actually need both the external consultancy expertise to bring everyone together, but then also the software expertise to actually build the systems." —— Harj Taggar
> 译:你其实同时需要两样东西:外部咨询把所有人拉到一起的能力,以及真正能把系统建出来的软件工程能力。

### 4. Reducto 案例:launch 后 154 天拿下大厂 / The Reducto case study `[11:07–13:39]`
**要点(中文)**: Diana 讲 Reducto(AI 文档处理,刚宣布 Series B):一家 154 年历史的大公司因看了 YC launch 主动找上门。这家公司多年自建方案、试过开源、AWS、Tesseract 等各种 OCR 都不达标,最终靠产品的极致品质,Reducto 在 launch 后 **154 天** 就拿下大单,如今已在生产环境跑了一两年。要点:Reducto 要和内部团队竞争、要有 finesse 处理政治(MIT 报告也承认这点),赢的秘诀是 **do things that don't scale** —— 和 champion 交朋友。创始人身上那种野心和乐观是有感染力的,让对方愿意"赌这些聪明孩子一把"。
> 🗣️ "This is where you do things that don't scale. One of the things that they did is they became really good friends with the champion" —— Diana Hu
> 译:这正是"做不可规模化的事"的地方 —— 他们做的一件事就是和内部 champion 成为真正的好朋友。
> 🗣️ "This is a bit of a boring problem to like process documents, but you're super jazzed about it and I'll give you a shot." —— Diana Hu(转述 champion 心态)
> 译:处理文档这问题其实有点无聊,但你们却为它超级兴奋 —— 那我就赌你们一把。

### 5. 找对 champion:企业里"想创业但不敢的人" / The champion archetype & warm intros `[13:39–15:25]`
**要点(中文)**: Harj 描述最佳 champion 的原型:**一个一直有创业梦、但太厌恶风险永远不会真去做的大厂员工** —— 他会通过一个让他有共鸣的创业团队"替代性地"体验创业,于是真心希望你成功。Diana 说,要找的就是这种"想滋养内心那个创业小孩"的人。Garry 提醒年轻创始人别装:别穿西装、别去模仿 Microsoft 官网,保持真实、聪明、in with it 就行,不必套上大公司的形式主义。Harj 的另一个高效战术:**找那些公司被大厂收购过的创始人当引荐人**。Triplebyte 当年能进 Apple,靠的是被 Apple 收购的 YC 公司 Cue(Robby Walker、Danny Gross);进 Oracle 的 pilot 则靠一位把公司卖给 Oracle 的创始人,他帮忙走采购、讲清内部政治和 step-by-step playbook。
> 🗣️ "It's someone that really wants to do a startup or has always sort of had dreams of a startup, but ... they're not actually ever going to do it. They're too risk averse. And so they can kind of live vicariously through an exciting startup with founders that they get along with." —— Harj Taggar
> 译:那种人一直很想创业、一直有创业梦,但其实永远不会真的去做,因为太厌恶风险 —— 于是他会借由一个和他合得来的、令人兴奋的创业团队,替代性地过一把创业瘾。
> 🗣️ "find founders whose companies were acquired by big companies and get them to your champion" —— Harj Taggar
> 译:去找那些公司被大厂收购过的创始人,让他们来当你的引荐 champion。

### 6. 创业公司前所未有的机会:大厂建不出来 & 切换成本护城河 / The shot startups never had, and the moat `[15:24–19:40]`
**要点(中文)**: Harj 点破共生逻辑:企业其实更愿意从成熟软件公司或晚期创业公司采购(感觉风险低),但它们**根本建不出产品** —— 因为这些大厂的工程团队里坐满了自己都不信 AI、不用 code gen 工具、觉得全是炒作、看到 MIT 报告就转发叫好的人。"如果你的工程师都不信,你怎么可能建出真能用的产品?"于是能真正建出东西的创业公司,拿到了以前从没有过的机会 —— 企业别无选择。Garry 呼吁那些被"AI 完了"叙事困住的工程师:去真试一次,投入一个真项目(哪怕副业),它能把 10x 工程师变成 100x、1x 变成 10x。Harj 用 Karpathy 访谈做"罗夏墨迹测验":Karpathy 的意思不是 agent 没用,而是你得做数据、context、evals、tooling —— 这对创业者恰恰是海量机会。Diana:软件需要为 AI 彻底重写,这全是创始人的机会。最后 Jared 抛出护城河:一位 50 亿美元金融公司 CIO 亲口说"一旦我们投入时间训练了某套系统,切换成本就高到无法承受" —— 那些担心"ChatGPT 套壳没护城河"的人,这就是护城河。
> 🗣️ "So if your engineers don't believe in this, then how are you going to build a product that actually works? ... so the startups are actually getting like the shot that they never had before." —— Harj Taggar
> 译:如果你的工程师们自己都不相信这件事,你又怎么可能建出一个真正能用的产品?……所以创业公司现在拿到的,是它们以前从来没有过的机会。
> 🗣️ "you can't just like give an agent a prompt and expect it to do everything perfectly the first time. ... there's like tons of opportunity to build really great tooling." —— Harj Taggar
> 译:你不能只给 agent 一个 prompt,就指望它第一次就把所有事都做得完美……这里其实有海量机会去构建真正优秀的工具链。
> 🗣️ "We're currently evaluating five different gen AI solutions, but once we've invested time in training a system, the switching costs will become prohibitive." —— Jared Friedman 引述某 50 亿美元金融公司 CIO
> 译:我们现在同时在评估五种不同的生成式 AI 方案,但一旦我们投入时间去训练某一套系统,切换成本就会高到无法承受。
> 🗣️ "So all these people who are worried that these like chat GPT rappers won't have moats, like that's the moat." —— Jared Friedman
> 译:所以那些担心"ChatGPT 套壳没有护城河"的人 —— 喏,这就是护城河。

### 7. Outro:1% 的人做出那 5% 能跑的实现 / The 1% who build the working 5% `[19:40–21:43]`
**要点(中文)**: Garry 收尾:AI Doomer 影响者把你带偏了。AI 确实极难落地,难到只有约 5% 真能跑起来;但如果你是 YC 里真正顶尖的创始人(录取率已 <1%),你完全有可能成为那 5% 里能跑的实现之一 —— 因为最聪明、最强的产品人和工程师正聚焦于此。关键还是那种既极强技术、又是多面手、懂人、懂那个 50 亿美元金融 CIO 到底想要什么的人。别看到这些统计就说"我永远进不了那 5%";只要你真的足够好,你绝对可以。
> 🗣️ "And it turns out it's so hard to implement that only 5% of the time it actually works. But it also turns out that if you're a startup founder and you're a really good one at YC, the acceptance rate is under 1% now." —— Garry Tan
> 译:结果就是,它太难落地了,只有大约 5% 的情况真能跑起来。但同样地,如果你是 YC 里一个真正优秀的创业者 —— 现在录取率已经低于 1%。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **选战场**:优先找那些"内部/咨询建过、失败了"的企业流程(银行、金融、传统行业的 KYC/AML、文档处理、老旧 systems of record),这里正是 startup-shaped hole。
- [ ] **改打法**:放弃 SaaS 即插即用心态,准备深度嵌入客户业务流程、深度集成 systems of record —— 慢,但护城河与回报都在这里。
- [ ] **做 launch 引流**:像 Reducto 一样公开做 YC launch / 产品发布,让大客户主动找上门(Reducto 就是这样被 154 年历史的大厂发现的)。
- [ ] **经营 champion**:找到那个"想创业但不敢"的内部人,do things that don't scale,和他做真朋友,让他借你的团队圆创业梦。
- [ ] **借力引荐**:主动去找"公司被大厂收购过"的创始人帮你引荐、教你走采购流程与内部政治(Triplebyte 进 Apple/Oracle 的原路径)。
- [ ] **把 Karpathy 的"缺口"变产品**:围绕 data、context 工程、evals、tooling 去补 agent 一次做不对的部分,这本身就是可卖的价值。
- [ ] **做真实的自己**:面对大客户别装西装 / 别抄大厂官网,用真实的野心和乐观打动人。
- [ ] **把切换成本设计进产品**:让客户越用越难迁走(训练/配置/数据沉淀),主动把"套壳没护城河"变成"训练即护城河"。

## 🔑 关键术语 / 概念
- **MIT State of AI in Business report** — MIT 关于企业 AI 落地的报告,被断章取义成"95% 企业 AI 项目失败 = AI 是骗局";实际结论对创业公司偏乐观。
- **Systems of record** — 企业核心业务系统(账务、客户、风控等真相数据源),往往老旧、割裂;深度集成进去是难点也是护城河。
- **Startup-shaped hole** — Garry 的说法:世界上几乎每个流程里都留着一个"只有创业公司能填"的洞。
- **Do things that don't scale** — YC 经典理念:早期靠不可规模化的动作(和 champion 交朋友、手把手服务)拿下关键客户。
- **Champion** — 客户内部推动你成交的关键内应;最佳原型是"想创业但不敢、愿替代性圆梦"的员工。
- **Bake-off** — 企业采购时让新方案和现有 incumbent 方案同台比拼;Castle AI 靠产品品质在 bake-off 中击败老牌 vendor。
- **Rorschach test(罗夏墨迹)** — Harj 比喻:同一段 Karpathy 访谈,想唱衰的人读成"AI 被高估",想建东西的人读成"海量机会"。
- **Switching cost moat(切换成本护城河)** — 企业一旦投入时间训练/配置某套 AI 系统,迁移成本高到无法承受,即为护城河。

## 🔖 高价值金句时间戳
- `[01:39]` "the more I read the study, the more I realized it was actually confirming a lot of the things we've talked about" — 报告不是打脸 AI 创业,反而印证了真实世界 agent 的规律。
- `[02:29]` "when you do succeed and plug into the systems of record, the pot of gold is actually quite big. But it does take a long time." — 深度集成是"慢但重"的护城河生意。
- `[04:08]` "Apple ... cannot make a good calendar app." — 连 Apple 都做不好软件,遑论企业内部 IT + 咨询。
- `[07:38]` "the success rate of the ones where the enterprise went with an outside vendor ... was much higher than the success rate of when they tried to build stuff themselves." — 外购 > 自建,这就是创业公司的市场证据。
- `[08:49]` "there's just this startup-shaped hole in basically every process" — 机会遍布每一个企业流程。
- `[13:01]` "This is where you do things that don't scale." — 拿下大客户靠不可规模化的关系经营。
- `[16:19]` "if your engineers don't believe in this, then how are you going to build a product that actually works?" — 大厂建不出来的根因:自己人不信 AI。
- `[18:35]` "you can't just like give an agent a prompt and expect it to do everything perfectly the first time." — Karpathy 的真意:agent 需要大量工程,恰是创业机会。
- `[19:58]` "once we've invested time in training a system, the switching costs will become prohibitive." — 50 亿美元金融 CIO 亲证:切换成本就是护城河。
- `[20:27]` "only 5% of the time it actually works. But ... if you're a startup founder and you're a really good one at YC, the acceptance rate is under 1%" — 顶尖 1% 的人,正好去做那 5% 能跑的实现。
