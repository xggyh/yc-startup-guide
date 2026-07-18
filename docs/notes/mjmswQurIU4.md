# Legora 如何在 18 个月内从 YC 干到 1 亿美金 ARR / How Legora Went From YC to $100M ARR in 18 Months

> **来源**: [How Legora Went From YC to $100M ARR in 18 Months](https://www.youtube.com/watch?v=mjmswQurIU4) · Y Combinator · 2026-06-05 · 时长 22:47
> **讲者**: Max Junestrand(Legora 联合创始人兼 CEO,YC W24,SPEAKER_01)· 主持:Gustaf Alströmer(YC General Partner,SPEAKER_00);录制于斯德哥尔摩 YC 活动
> **一句话定位**: 一个瑞典法律 AI 团队用"极速做大 + 创始人亲自扫楼卖 + 长期主义产品宣言 + 在基础模型不断变强时找护城河"的打法,18 个月冲到 1 亿美金 ARR——对做垂直行业 AI Agent、要在大厂和基础模型阴影下建立防御性的创始人极有参考价值。

## 🎯 TL;DR(中文核心要点)
- **护城河问题不是"OpenAI/Anthropic 会不会做",而是"当模型持续变聪明,你的业务里什么是防御性的"**:答案落在专有数据、工作流模式、以及你教给用户的行为习惯,而不是模型本身能力。
- **早期产品"其实并不好",但你必须自己先信到底**:Max 拎着小公文包在斯德哥尔摩到处扫楼,客户不是被产品打动,是被那个"疯了一样兴奋"的创始人打动——投资人和客户都能"闻到"你自不自信。
- **别过度聚焦单点,要有捆绑打法 + 更长的地平线战略**:竞品单做"表格审阅"一项做到 ~50M ARR 时 Legora 只有 1M,但 Legora 用"聊天助手 + 表格审阅 + Word 插件"三合一捆绑,最终反超并把对手客户搅churn掉。
- **速度即战略——"我们意识到必须快速做大"**:一年前 40 人,现在近 500 人,横跨 SF/芝加哥/得州/纽约/伦敦/斯德哥尔摩/德国/印度/澳洲;因为"律师全世界干活方式都差不多"。
- **从"增强单个任务"进化到"主动式 Agent 做端到端工作产品"**:圣诞前后模型能力阶跃,配合他们为法律任务搭的 harness + 工具 + 企业内文档/邮件的信任访问,Agent 现在能主动替合伙人处理积压邮件、跑完整个尽调。
- **新瓶颈是"端到端工作产品的 evals",不再是单任务**:一个 M&A 尽调任务可能跑 20–30 分钟,用户体验正从"实时协作"转向"像用 Cursor / Claude Code 一样下达宽泛指令,让多个 Agent 并行去干活"。
- **融资是能量管理:被拒得越多越容易自我怀疑,但你越沮丧投资人越能闻到**:YC 的最大价值之一是给首次创业者带来投资人 inbound 和 signaling,一周排 80 场会集中冲刺 demo day。
- **把"活儿"当"毕生事业",而非一场创业游戏**:一旦决定"这是我的公司、这是我这辈子的事",你的在意程度和野心会自动往上爬——目标是从欧洲造出下一个巨型科技公司。

## 🧭 适合谁 / 什么时候看
- 做**垂直行业(法律/医疗/金融等)企业级 AI Agent**、需要回答"基础模型变强后我凭什么活下来"的创始人。
- 正在或即将进入 **YC / 加速器融资冲刺**,想知道如何利用 signaling、如何在连续被拒时维持能量的人。
- 想把产品从"单任务助手"升级到"主动式、端到端 Agent",并因此开始被 **evals 卡脖子**的团队。
- 非美/非硅谷创始人(尤其欧洲),想验证"从本地起步也能造全球级公司"的路径。

## 📝 分段精读

### 1. 开场:用 Jude Law 让"最无聊的法律科技"变性感 / The Jude Law Marketing Stunt `[00:00–03:11]`
**要点(中文)**: 法律科技的营销"无聊到让汽车零件都显得性感"。Legora 的破局是拿真实客户证言去打动大牌影星 Jude Law——不是靠钱(Jude 起初直接拒绝),而是把 "customer love" Slack 频道里"我一天审了 1000 份合同,还赶回家过周末"这类真实赞誉做成 PPT 砸给他。Jude 自带 SNL 编剧和《奥本海默》摄影师拍出爆款广告,并带来真实 leads。给 Agent 创始人的启示:**真实的、可量化的客户结果(节省的时间)是最强的营销和说服素材**。

> 🗣️ "has anybody ever looked at advertisement or marketing for a legal technology company and said that's sexy no it is the most boring the most bland it makes like automotive parts look hot" —— Max Junestrand
> 译:有谁看着一家法律科技公司的广告说过"这真性感"吗?没有。那是最无聊、最平庸的东西,让汽车零件都显得火辣。

> 🗣️ "i use legora to review a thousand agreements in one day and i got home to see my family in time for the weekend" —— Max 引述客户证言
> 译:我用 Legora 一天审了一千份合同,还赶在周末前回家陪了家人。

### 2. 起步、风险与放弃 McKinsey / Risk, McKinsey Offers & Taking the Leap `[03:11–05:37]`
**要点(中文)**: Max 在校期间"尽可能多地尝试"(计算机、商科、McKinsey、两家 YC 创业公司),不是主动挑中法律,而是"法律选中了我们,然后我们决定拼命跑"。风险管理很实际:先在暑假做,McKinsey 全职 offer 揣在兜里当保险;真正下注的时刻是拿到 YC offer 后打电话说"我不回去了"。Legora 里有 10–15 人都放弃了 McKinsey offer,CTO Jake 甚至把 offer 拖了六年。启示:**降低下注的心理门槛(保留退路),等信号明确后再 all in**。

> 🗣️ "if people ask me like did we pick law or did law pick me I think law picked me and then we just decided to run like hell" —— Max Junestrand
> 译:如果有人问我们是选中了法律,还是法律选中了我们——我觉得是法律选中了我们,然后我们决定拼命地跑。

> 🗣️ "it didn't seem that risky to work on something over the summer when I still had my full-time offer at McKinsey in the back of the pocket" —— Max Junestrand
> 译:当 McKinsey 的全职 offer 还揣在兜里时,利用一个暑假去做点东西,看起来并没那么冒险。

### 3. 进入 YC 与冒充者综合症:亲自扫楼卖 / Getting Into YC & Arriving With Imposter Syndrome `[05:37–09:59]`
**要点(中文)**: 三个瑞典辍学生带着强烈 FOMO 进 YC,以为会遇到一堆 MIT/Google 的 PhD、早已高营收,结果发现"很多人还在瞎找方向",而自己反而是营收最高之一。他们把整个 10 人公司搬进 Airbnb 当"劳改营",凌晨 1 点到 10 点打销售电话(给笔记本装补光灯)。Max 飞回斯德哥尔摩,拎着公文包扫楼——**客户被"一个对法律科技疯狂兴奋的人"打动,尽管"产品其实并不怎么样"**。销售杀手锏:社会认同("北欧最大律所已经在用,你不用就是 loser")。

> 🗣️ "we realized that we had amongst the highest revenue in the batch and we were coming in with such FOMO like three college dropouts from Sweden" —— Max Junestrand
> 译:我们发现自己是整批里营收最高的之一,而进来时我们还带着巨大的 FOMO——三个瑞典辍学生。

> 🗣️ "our product was frankly not that great but they wanted to work with me and they wanted to work with us" —— Max Junestrand
> 译:老实说我们的产品并不怎么样,但他们就是想和我合作、想和我们合作。

> 🗣️ "the biggest firm in the Nordics already work with us so if you don't you're kind of a loser and they were like okay I get it I have to get on the train" —— Max Junestrand
> 译:北欧最大的律所已经和我们合作了,你不合作就有点像 loser 了——他们就说,好吧我懂了,我得上这趟车。

### 4. YC 融资冲刺与在"No"里保持自信 / The Fundraise Grind & Staying Confident `[09:59–12:00]`
**要点(中文)**: 团队做了"热插拔"——发货团队回去接客户,Max 去 YC 做融资。对无人脉的首次创业者,YC 的被低估价值是**投资人 inbound + signaling**:一周排 80 场会冲刺 demo day。练习轮"又累又没准备,很烂",但真正上场("到 Benchmark 见 Peter Fenton")就"打爆了"。主持人 Gustaf 补刀关键心法:被拒次数越多越容易钻进投资人的 notes、开始自我怀疑,但**投资人能"闻到"你不自信;你自己不信,没人会信你会赢**。

> 🗣️ "there's a lot of signaling value to be in YC you basically get a lot of investor inbound building up to demo day and then you just schedule everything so you have like 80 meetings in a week" —— Max Junestrand
> 译:在 YC 有很强的 signaling 价值——临近 demo day 你会收到大量投资人主动来敲门,然后你把它们全排上,一周排出大概 80 场会,集中火力硬啃。

> 🗣️ "investors they can see that they can they can smell it that you are not confident in your own company and in order to get anyone else to be confident you're going to succeed you have to be confident yourself" —— Gustaf Alströmer
> 译:投资人看得出来、能闻得到你对自己公司不自信;要想让任何人相信你会成功,你自己必须先足够自信。

> 🗣️ "the guy is perfect the only problem is that he's from Sweden and I'll tell you what I don't think that's going to be a problem anymore" —— Max 引述 Peter Fenton
> 译:(Peter Fenton 说)这家伙很完美,唯一的问题是他来自瑞典——而我要说,我觉得这个问题已经不再是问题了。

### 5. 从欧洲造下一个 Google 的野心 / Building the Next Google From Europe `[12:00–14:25]`
**要点(中文)**: 一旦把公司定义为"毕生事业、这是我的公司",在意程度和野心会自动往上长。Max 拿 Google(靠搜索/广告的现金流去做自动驾驶)、Facebook(做 Meta VR)举例,想从欧洲造出"最大的科技公司"(吐槽欧洲最大科技公司居然是 SAP)。核心论点对创始人有普适性:**AI 正在民主化对技术与人才的access,唯一稀缺的是野心**;"如果你在美国排 150,AI 就是你从 150 冲到 10 的门票"。Legora 15% 的工程与产品组织成员本身是(前)创始人——"apes together strong"。

> 🗣️ "if you're ranked number 150 in the US AI is your ticket to go from 150 to 10" —— Max Junestrand
> 译:如果你(律所)在美国排第 150,AI 就是你从 150 冲到前 10 的入场券。

> 🗣️ "technology is democratizing access to technology access to Talent and the only thing we need is the ambition" —— Max Junestrand
> 译:技术正在把对技术、对人才的获取门槛民主化,我们唯一还需要的,就是野心。

### 6. Mini Games 与产品宣言:捆绑打法 / Mini Games & the Product Manifesto `[14:25–16:28]`
**要点(中文)**: 主持人金句:"每家创业公司都是一连串的 mini game,赢下一局就进入下一局。"2024 年 10 月正式 GA 时,团队写了一份三页 Word "产品宣言":要在**聊天助手、表格化审阅(tabular review)、Word 插件**这三件事上都做到最好并捆绑。当时对手单做表格审阅一项做到近 50M ARR,而 Legora 才 1M——但靠捆绑三合一,Legora 最终大幅反超并搅走对手大量客户。教训:**别在"当下此刻"过度聚焦,即使在快节奏世界也要有稍长地平线的取胜战略**(他们甚至建议写"10 年后律师如何工作"的科幻小说)。

> 🗣️ "we wrote a three-paged Word document that was our product manifesto ... if we can be the best at all these three and bundle them we will win" —— Max Junestrand
> 译:我们写了一份三页的 Word 文档,那就是我们的产品宣言……如果我们能在这三件事上都做到最好并把它们捆绑起来,我们就会赢。

> 🗣️ "we should write a sci-fi novel about you know what a lawyer 10 years from now and how they will work because at the end of the day it's that future we are building for" —— Max Junestrand
> 译:我们该写一本科幻小说,描绘 10 年后的律师是什么样、如何工作——因为归根结底,我们正是在为那个未来而造东西。

### 7. 1 亿 ARR、全球化与主动式 M&A Agent / $100M ARR, Going Global & M&A Agents `[16:28–20:41]`
**要点(中文)**: 一年从 40 人到近 500 人,横跨十国;"律师全世界干活方式都差不多"所以能全球复制。心态是"刚到大本营,真正的攀登才开始",公司由大量创始人/前 CEO 运营,充满 founder mode 能量。产品的关键转折:圣诞前后模型能力阶跃 + 他们搭的 **harness/工具/对企业全量文档邮件的信任访问**,让路线从"增强律师单个任务"跃迁到"**主动式 Agent**"——主动看完所有 matter 的上下文替合伙人清理积压邮件;Agent 能操作文件树、按模板重构杂乱的 data room、跑完整 M&A 尽调。**新瓶颈是端到端工作产品的 evals**;交互模式变成"像用 Cursor / Claude Code 一样下宽泛指令,让 Agent 并行去干"。他判断法律 Agent"落后 code 约 6 个月",因为 code 更二进制、上下文更简单、模型开箱即用。

> 🗣️ "we are going global because turns out lawyers work the same way all over the world give or take" —— Max Junestrand
> 译:我们正在全球化,因为事实证明律师在全世界的工作方式大同小异。

> 🗣️ "now because of the capabilities of the agents and the harness that we have built for our type of tasks ... now we can build really powerful um proactive agents" —— Max Junestrand
> 译:如今凭借 Agent 的能力,以及我们为自己这类任务搭建的 harness……我们现在能造出真正强大的主动式 Agent。

> 🗣️ "one of our main bottlenecks is evals for end-to-end work products because we're no longer just working with an individual task" —— Max Junestrand
> 译:我们现在的主要瓶颈之一是对端到端工作产品的 evals,因为我们不再只是处理单个任务了。

> 🗣️ "the lawyer or the legal professional is moving from ... working with it um in real time to very much like working with cursor or cloud code like you're giving broader instructions and then you're having the agents go out and do work in parallel" —— Max Junestrand
> 译:律师/法律专业人士正从"实时地与它协作",转向"很像用 Cursor 或 Claude Code 那样"——你下达更宽泛的指令,然后让多个 Agent 出去并行地干活。

### 8. "如果 OpenAI/大厂做了怎么办":模型变强时的护城河 / Finding Your Moat as Models Get Smarter `[20:41–22:47]`
**要点(中文)**: 主持人回忆当年"如果 Google 做了怎么办"是个真问题,但 Google 15 年里几乎没在新内部产品上执行成功,最后大家都在笑这个问题。Max 给出框架:参照 AWS 时代的 MongoDB——**去做那些"对更大平台来说不自然去做"的东西**。真正的问题不是"Anthropic/OpenAI 会不会做",而是"当模型呈线性持续变聪明,你业务里什么是防御性的"。如果真到了模型能即时写完所有代码、取到所有数据、解决一切的地步,那大家不如去喝 piña colada——但他不认为那是终局。所以要死磕:**输入与输出、专有数据、工作流模式、你教给用户的行为**;而 Legora 的第一性结论是"必须快速做大"。

> 🗣️ "what is your moat when the models continue to get smarter ... it's not like is anthropic gonna do it is open ai gonna do it it's like what's defensible in your business" —— Max Junestrand
> 译:当模型持续变得更聪明,你的护城河是什么……问题不在于 Anthropic 会不会做、OpenAI 会不会做,而在于你的业务里什么是有防御性的。

> 🗣️ "if we all think about a world where the model is so good that it on the fly writes all the code gets all the data figures out all the print like everything to solve a task then we should all go have a pina colada instead" —— Max Junestrand
> 译:如果我们设想一个模型强到能即时写出所有代码、拿到所有数据、把解决任务所需的一切都搞定的世界,那我们干脆都去喝杯 piña colada 算了。

> 🗣️ "we've actually seen this play out one time before with um databases and infrastructure and aws and ... companies like mongodb ... what did they build which wasn't natural for a bigger platform like aws to build" —— Max Junestrand
> 译:这一幕其实上演过一次——数据库、基础设施和 AWS;看看 MongoDB 这样的公司……他们造了什么是对 AWS 这种更大平台而言"不自然去做"的东西。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **写一页"护城河假设":** 明确列出当基础模型继续线性变强时,你业务里防御性来自哪里——专有数据、工作流模式、用户行为习惯、企业信任/数据访问权,而不是模型能力本身。
- [ ] **做那些"大平台不自然去做"的事:** 用 MongoDB vs AWS 的类比审视自己——找到 OpenAI/Anthropic 因焦点或组织惯性不会认真做的垂直深度(合规、企业内数据接入、行业工作流)。
- [ ] **把交互升级为"主动式 + 并行 Agent":** 从"实时增强单任务"转向"下宽泛指令、Agent 后台并行跑长任务(20–30 分钟级)",并配套能操作文件树/结构化非结构数据的工具(harness)。
- [ ] **优先把 evals 从单任务扩到端到端工作产品:** 当 Agent 交付完整工作产品(如整套尽调)时,评测集是新瓶颈——提前投入建 end-to-end evals。
- [ ] **用可量化的客户结果做销售与营销素材:** 建"customer love"式证言库(如"一天审 1000 份合同、周末回家"),这既是最强 marketing 也是最强 social proof。
- [ ] **速度即战略:定"必须快速做大"为第一性目标,** 并用捆绑打法(多个都做到最好再打包)对抗单点专注的竞品;同时保留一条更长地平线的产品宣言。

## 🔑 关键术语 / 概念
- **Harness(Agent 骨架/脚手架)** — 围绕特定任务类型为模型搭建的工具链、上下文接入与执行框架;Legora 强调正是"为法律任务搭的 harness + 工具 + 企业数据信任访问"才让主动式 Agent 成为可能。
- **Proactive agents(主动式 Agent)** — 不等用户逐条指令,而是主动读取全部上下文(如所有 matter、邮件)并预先替用户完成工作产品的 Agent。
- **End-to-end evals(端到端评测)** — 针对 Agent 交付的完整工作产品(而非单个子任务)的评测集;是从"增强单任务"迈向"Agent 干完整活儿"后的核心瓶颈。
- **Tabular review(表格化审阅)** — 法律场景把大量文档按维度拉成表格批量审阅的功能;Legora 三大捆绑功能之一。
- **Signaling value(信号价值)** — 身处 YC 等品牌带来的投资人主动 inbound 与背书效应,对无人脉首次创业者尤为关键。
- **Data room / due diligence(数据室 / 尽调)** — M&A 中一堆常为非结构化的资料;Legora Agent 可按模板重构文件树并跑尽调清单。

## 🔖 高价值金句时间戳
- `[21:52]` "what is your moat when the models continue to get smarter" — 护城河的正确提问方式:不问大厂会不会做,而问模型变强后你凭什么防御。
- `[22:38]` "what is the proprietary data what are the workflow modes what is the behavior that we're teaching our users" — 防御性的三个具体落点,建议直接抄成自查清单。
- `[19:00]` "one of our main bottlenecks is evals for end-to-end work products" — Agent 迈向端到端交付后,evals 是新瓶颈,值得提前重投。
- `[11:59]` "investors ... can smell it that you are not confident in your own company" — 融资本质是能量管理:你自己不信,谁都不会信你会赢。
- `[08:20]` "our product was frankly not that great but they wanted to work with me" — 早期靠创始人极致的兴奋与信念带客户上车,产品不完美也能卖。
- `[13:20]` "technology is democratizing access to technology access to Talent and the only thing we need is the ambition" — 非硅谷/欧洲创始人的底气:稀缺的只剩野心。
