# 两个 IIT 工程师为何拒绝 55 万美元工作去创业 / Why Two IIT Engineers Turned Down $550K Jobs To Build A Startup

📄 **[点此查看全文转录 / Full transcript »](../transcripts/2Ap1dnv-GXA.md)**

> **来源**: [Why Two IIT Engineers Turned Down $550K Jobs To Build A Startup](https://www.youtube.com/watch?v=2Ap1dnv-GXA) · Y Combinator · 2026-05-29 · 时长 24:29
> **讲者**: 嘉宾 Varun Vummadi(Giga / GigaML 联合创始人,做客服 AI Agent);主持 Ankit Gupta(YC General Partner)。录制于 Startup School India。
> **一句话定位**: 一位 AI 客服 Agent 创始人复盘从 EdTech → 微调 → 客服的多次 pivot,核心结论对做 AI Agent 创业者极有价值:不要纠结点子和市场,而要盯住"客户是否愿意为价值付真钱",并把 Agent 产品化为"可迭代的 markdown 策略 + KPI"。

## 🎯 TL;DR(中文核心要点)
- **点子不重要,愿不愿意付钱才重要**:不要一开始就分析市场大小,先确认"有人愿意为你解决的问题付真金白银",甚至先拿到付费承诺再动手建。
- **真正的方向是从客户里长出来的,不是想出来的**:他们做微调时发现只有"客服 + 编程"两类客户增长最快,于是掉头做客服——是被客户"拉"出来的,不是看市场"选"出来的。
- **微调(fine-tuning)是个烂市场**:唯一价值是降本提速,或卖给极重合规的大公司,而后者是销售流程不是工程流程,工程师团队很难打。这是一次昂贵的教训。
- **AI Agent 的本质是 markdown**:几乎任何 Agent 公司都可归结为"policies / markdown 文件",关键是如何迭代这个文件去撬动业务 KPI(客服里就是解决率 / CSAT),从 30-40% 迭代到 90%。
- **产品 > 销售**:成功的 AI 公司靠产品,没人因为销售团队好而用 Anthropic;OpenAI / Anthropic 甚至不给销售发提成。产品在短时间内交付足够价值,其余自然跟上。
- **小团队 + 编码 Agent = 巨大套利**:8 人干掉 400 人的重资本对手拿下 DoorDash;若没有 Cloud Code,工程团队规模要 6-7 倍。"自己端到端拥有一件事"比多人协作+上下文切换快得多。
- **Burn the boats(烧船)**:拒掉高薪 offer、把退路断掉,会逼你把东西真正做出来;何况在 AI 时代建东西成本极低,退路其实一直在(大不了回去上班)。
- **AI 交付的最大瓶颈是 Forward Deploy Engineer**:企业 AI 落地卡在需要大量 FDE 现场配置,他们正在做"AI Forward Deploy Engineer"来吃掉这个瓶颈。

## 🧭 适合谁 / 什么时候看
- 正在做 **B2B / 企业级 AI Agent**(客服、合规、ITSM 等)、想理解如何把 Agent 产品化并驱动客户 KPI 的创始人。
- 卡在**选方向 / 纠结市场和竞品**、不知道该不该"先收费"的早期技术创始人。
- **技术背景强、没有商业/销售背景**,担心"没人会为我付钱"的工程师型创始人。
- 想了解**用编码 Agent(Cloud Code)把工程团队做小、把公司自动化**的实操心态。

## 📝 分段精读

### 1. Giga 是什么 + 出身与研究背景 / What Giga Is & Origin Story `[00:00–03:36]`
**要点(中文)**: Giga 做客服 AI Agent,客户包括 DoorDash、全球最大加密交易所之一、Top3 电信商。传统客服经 IVR/chatbot 再转人工,deflection(自助解决)率仅 10-15%;AI 能做到 60-70%,目标 90-95%,体验更好、无需排队。Varun 出身印度小镇教师家庭,苦读进 IIT Kharagpur 电气工程,大三在斯坦福做 LLM(BERT/Transformer)研究,拿到量化基金 55 万美元 offer 和斯坦福 PhD——然后 ChatGPT 发布,他决定去申请 YC。
> 🗣️ "With AI, it's just like you call, it's entirely like human experience, closer to like 60 to 70% deflection rates. We're aiming to get it closer to like 90 to 95% for top of the customers." —— Varun (SPEAKER_01)
> 译:用了 AI 之后,你打电话来就是完全类人的体验,自助解决率接近 60-70%,对头部客户我们的目标是 90-95%。

### 2. YC 面试"灾难" + 逃离 EdTech / The YC Interview Disaster & Pivoting Away From Ed Tech `[03:37–07:24]`
**要点(中文)**: 他们本想做"用 LLM 的 EdTech",面试官 Haj 完全不问点子和市场,直接说"这是 EdTech,行不通,换一个",看中的是他们的 LLM 研究经历。Varun 当场崩溃以为要挂,但 Haj 反而想让他们进 YC——"你们是很好的工程师,去挑别的东西做"。进营后一个月,Haj 安排他们和 Coursera COO 等成功 EdTech 前辈聊,所有人都说 EdTech 是坏主意,于是 pivot。他们读了 Databricks 联创关于"缓存 LLM 降本"的论文,判断微调更好,开源模型登顶 Hugging Face 榜,靠此拿到流量并融了 400 万美元种子轮。
> 🗣️ "you guys are really good engineers. Just pick something else and work on it. ... you would not have existed without Hutch taking a bet." —— Varun 转述 Haj(SPEAKER_01)
> 译:你们是非常好的工程师,去挑点别的东西做。……没有 Haj 押注在我们身上,就没有今天的我们。
> 🗣️ "the only reason you want to fine tune is to reduce the cost and make it faster." —— Varun (SPEAKER_01)
> 译:你想做微调的唯一理由就是降成本、提速度。(暗示:这决定了它是个小而受限的市场)

### 3. 找到真正的问题:客服 / Finding the Real Idea `[07:25–08:38]`
**要点(中文)**: 微调是个烂市场:除了降本提速,另一个用例是卖给极重安全/合规的大保险、医疗公司——但那是销售流程而非工程流程,工程师团队很难卖进去,他们花了约一年才想明白。转机在于观察自己客户:所有增长很好的用例只归结为两类——**客服和编程**。于是选了客服。第一个客户 Zepto 正在飞速扩张,主动试用后成交。方向不是"看市场选出来"的,而是从现有客户里"自然长出来"的。
> 🗣️ "the only two use cases on GigUp customers, which are growing very well, are customer support and coding. So we decided to customer support." —— Varun (SPEAKER_01)
> 译:我们客户里增长很好的用例只有两个——客服和编程,所以我们决定做客服。

### 4. 击败重资本对手 + 8 人拿下 DoorDash / Beating a Well-Funded Competitor & Winning DoorDash `[08:39–11:08]`
**要点(中文)**: 决定做客服时,Sierra、Decagon 这类明星、重资本公司已存在,但 Varun 坦言"我们根本不知道 Sierra、Decagon 存在",也不太考虑竞争——只问"客户愿不愿付钱、你能否交付大量价值"。Zepto 之后,真正的对决发生在他们(8 人)和一家 400 人重资本公司之间争 DoorDash,他们赢了。之所以能赢:YC 是"不公平优势"(Gary 引荐 Tony,双方都是 YC 公司,天然信任),加上试点 3 个月零宕机、指标全绿,DoorDash 又极重实力主义。这让他们意识到存在巨大套利——**用好产品去打,而不是靠销售团队**。拿下 DoorDash 后,更多大公司因这个 logo 而选择他们。
> 🗣️ "we're building a great product, rather than a sales team." —— Varun (SPEAKER_01)
> 译:我们靠的是打磨一个很棒的产品,而不是靠一支销售团队。
> 🗣️ "you've got to have some unfair advantage, right? For us, YC was that." —— Varun (SPEAKER_01)
> 译:你得有某种不公平优势——对我们来说,YC 就是那个优势(带来了天然信任)。

### 5. Giga 现在的样子:一切归于 markdown / What Giga Looks Like Now `[11:09–12:39]`
**要点(中文)**: 现在服务全美最大加密交易所等大量 Fortune 客户,并被最大消费公司试点用于内部支持、合规等。Varun 给出对 Agent 创业最有价值的洞察:几乎任何 Agent 公司,本质都归结为两件事——**policies / markdown 文件**,以及**如何迭代这个 markdown 去撬动业务 KPI**。客服里 KPI 就是解决率或 CSAT,关键是如何从 30-40% 的解决率迭代改进到 90%;同样的底层逻辑适用于合规、ITSM、ITSD。
> 🗣️ "It's like policies or the markdown file, and how can you iterate the markdown file to affect a business KPI?" —— Varun (SPEAKER_01)
> 译:(Agent 的本质)就是策略,或者说 markdown 文件,以及你如何迭代这个 markdown 文件去影响某个业务 KPI。
> 🗣️ "we started like 30 to 40% resolution rate, how to get to 90%, how can you iteratively improve to get there." —— Varun (SPEAKER_01)
> 译:我们从 30-40% 的解决率起步,问题是如何做到 90%、如何一步步迭代到那里。

### 6. 给大学生的建议 + 为什么要尽早收费 / Advice for Students & Why Charge Early `[12:40–17:11]`
**要点(中文)**: 很多人觉得他拒掉量化 offer 很蠢,但他和联创只想"看看自己能走多高",甚至后来拒过顶级公司的收购。他读 PG 的《How to Make Wealth》,结论是要在大东西里持有股权。他向父亲摊牌很难(中下产家庭期望重),但他给父母看 YC 视频、说明"就算一两年不成也能回去上班"。核心建议:**永远不是点子的问题,而是有没有人愿意为它付钱**;甚至"不需要关心市场"——只要有人为你交付的价值付真钱就行。现在做新产品,他们都会先预测客户会付多少、拿到付费承诺,再去建。为什么早收费重要?因为**只要问题足够重要,人就会付费(付钱或付时间)**,否则你只是在解决一个假问题。地域上:贴近客户;但若做 Gen AI / research 相关,SF 不可替代(接触研究者的密度远超印度)。
> 🗣️ "It's never about the idea. It's about if somebody is willing to pay you money for it." —— Varun (SPEAKER_01)
> 译:关键从来不是点子,而是有没有人愿意为它付钱给你。
> 🗣️ "If it's an important enough problem, people would pay. Either with money or with time. ... Otherwise, like, you're just solving a fake problem." —— Varun (SPEAKER_01)
> 译:如果问题足够重要,人们就会付费——要么付钱,要么付时间;否则你只是在解决一个假问题。
> 🗣️ "if you're doing anything closer to, like, Gen AI and very, like, research-based things, I strongly think SF is the place." —— Varun (SPEAKER_01)
> 译:如果你做的是接近 Gen AI、非常偏研究的东西,我强烈认为 SF 才是那个地方。

### 7. 下一个大赌注:AI Forward Deploy Engineer / The Next Big Bet `[17:12–18:42]`
**要点(中文)**: 他判断每一个企业 AI 部署(无论客服还是任何自动化)最大的瓶颈都是 **Forward Deploy Engineer(FDE)**——需要一群人现场进驻、贴着客户去配置。Giga 正在造一个"AI Forward Deploy Engineer":当客户要改策略、要新看板、或想把解决率从 40% 提到 60% 时,这个 AI FDE 会加入 Slack、进 Google Meet、记录并自动完成改动。他对这个方向最有信心,认为这是攻克企业 AI 采用的关键。
> 🗣️ "The biggest bottleneck of every single enterprise AI deployment, regardless of support or any automation ... this concept called forward deploy engineer. ... We're trying to build an AI forward deploy engineer." —— Varun (SPEAKER_01)
> 译:每一个企业 AI 部署的最大瓶颈,无论是客服还是任何自动化,都是这个叫"前置部署工程师(FDE)"的角色……我们正在造一个 AI 版的 forward deploy engineer。

### 8. 用 AI 运营公司 + 怎么招人 / Running on AI & How They Hire `[18:43–21:39]`
**要点(中文)**: 公司价值观之一是"automate, automate, automate",使命是"自动化世界上所有的工作",并有意做成"通用自动化搭建器"。例子:用 Cloud 自动排会当私人助理;销售从 Gong 拉转录、分析对某个竞对最有效的打法。Varun 特别推崇 Cloud Code——它把很多人变成了 builder。若没有编码 Agent,工程团队要 6-7 倍大;而这不只是省钱,更因为**"自己端到端拥有并搭建整件事"比多人协作快得多**——上下文转移会拖慢并杀死很多东西。招聘上:面试里让候选人先 vibe-code,再切断 AI 让他手改代码,确保真正理解代码;总体只看"极端能力和 spikiness(尖锐特长)"——那种 0.1% 的人才会做到的事。
> 🗣️ "that's the one thing I love about cloud code. It turned a lot of people into builders." —— Varun (SPEAKER_01)
> 译:这正是我最喜欢 Cloud Code 的一点——它把很多人变成了真正的 builder(能亲手造东西的人)。
> 🗣️ "the context transfer actually kills a lot of things and slows down things." —— Varun (SPEAKER_01)
> 译:(多人协作里的)上下文转移其实会扼杀很多东西、拖慢一切。
> 🗣️ "we're trying to look at very spiky things on which is the 0.1% of people would do." —— Varun (SPEAKER_01)
> 译:我们在找非常"尖"的特质——那种只有 0.1% 的人才会做到的东西。

### 9. 产品高于销售 + 烧船启程 / Product Over Sales & Burn the Boats `[21:40–24:29]`
**要点(中文)**: 关于"没有商业背景怎么办":总有客户会在你没销售背景时买单,关键是**找对买家、找到你的 ICP**(Zepto、DoorDash 都不在乎你有没有大销售团队)。Varun 复盘早期最大错误:他曾以为销售最重要,和联创大吵,结果大错特错——看所有成功的 AI 公司,靠的都是产品;没人因为销售团队好而用 Anthropic,OpenAI / Anthropic 甚至不给销售发提成。**AI 时代产品才是最重要的**:产品能在短时间内为客户交付大量价值,其余自然跟上。临别建议:**Burn the boats(烧船)**——真正断掉退路,东西才会变得"真实",逼你把它做出来;但本质上退路一直在(有工作总能再找),而 AI 时代建东西成本极低,所以就去建、去为很小一批客户交付尽可能多的价值,看他们愿不愿付钱。
> 🗣️ "If you take a look at all the successful AI companies, it's product. ... Nobody uses Anthropic for the best sales team." —— Varun (SPEAKER_01)
> 译:你去看所有成功的 AI 公司,靠的都是产品……没有人是因为 Anthropic 销售团队最好才用它的。
> 🗣️ "How good is your product at delivering a lot of value to the customer in a short amount of time? If you can do that, everything else should follow through." —— Varun (SPEAKER_01)
> 译:你的产品在短时间内为客户交付大量价值的能力有多强?只要能做到这点,其余一切都会自然跟上。
> 🗣️ "the cost of building things is so low. People should just build things and try to deliver as much value as they can ... and see if they can pay the money." —— Varun (SPEAKER_01)
> 译:如今建东西的成本极低,人们就应该去建、尽可能多地交付价值……然后看他们愿不愿付钱。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先卖后建**:在动手做新 Agent 功能前,给目标客户报出预估价格、拿到付费承诺再开发;把"是否有人愿付真钱"当作唯一的立项门槛。
- [ ] **把你的 Agent 抽象成"markdown 策略 + KPI"**:显式管理 policy/markdown 文件,建立"迭代 markdown → 撬动某个 KPI(如解决率/CSAT)"的可度量闭环,并给客户看从 X% 到 90% 的改进曲线。
- [ ] **从现有客户里发现真方向**:不要靠"市场很大"来选赛道;盯住自己产品里增长最快的少数用例,像他们从微调里发现"客服+编程"那样,顺势聚焦。
- [ ] **绕开销售壁垒、用产品做套利**:在大客户不再排斥小团队的今天,用"三个月零宕机、指标全绿的试点"去正面赢下重资本对手,而不是拼销售团队规模;主动找 YC/共同投资人这类"天然信任"通道引荐。
- [ ] **用编码 Agent 把团队做小**:把 Cloud Code 等工具作为默认工作方式,追求"一人端到端拥有一件事、减少上下文转移";招聘时用"先 vibe-code、再断 AI 手改代码"来验证候选人是否真懂代码。
- [ ] **瞄准 FDE 瓶颈**:如果你做企业 Agent,认真评估"部署/配置(forward deploy)"这一环能否被你的 Agent 自己吃掉——这可能是比模型能力更大的护城河。
- [ ] **产品优先于销售**:早期把最强的人和精力压在产品交付价值上,而非先堆销售;先找准 ICP,让第一批愿付费的客户验证价值。

## 🔑 关键术语 / 概念
- **Deflection rate(自助解决率 / 转人工规避率)** — 客服请求中无需转人工就被解决的比例;传统 IVR/chatbot 约 10-15%,Giga 的 AI 做到 60-70%,目标 90-95%。
- **Fine-tuning(微调)** — 在小模型上微调以降本提速;Varun 认为这是个烂市场,除降本外主要卖给重合规大客户,而那是销售而非工程问题。
- **Markdown / policies(策略文件)** — Varun 眼中 Agent 的本质载体:Agent 行为可归结为一份可迭代的 markdown 策略,通过改它来影响业务 KPI。
- **Resolution rate / CSAT** — 客服 Agent 的核心 KPI(问题解决率 / 客户满意度),是迭代 markdown 的优化目标。
- **Forward Deploy Engineer(FDE,前置部署工程师)** — 企业 AI 落地时需现场进驻、为客户配置系统的工程师;Varun 认为这是企业 AI 采用的最大瓶颈,Giga 正做"AI FDE"取代它。
- **ICP(Ideal Customer Profile,理想客户画像)** — 最可能付费且不在乎你有无销售背景的买家类型(如 Zepto、DoorDash)。
- **Burn the boats(烧船)** — 主动断掉退路(如拒绝高薪 offer)以逼自己全力交付的创业心态。
- **Vibe coding** — 用 AI 辅助快速写代码;Giga 面试要求候选人先 vibe-code、再断 AI 手改,以验证其真正理解代码。
- **Cloud Code** — Varun 反复称赞的编码 Agent 工具,"把很多人变成了 builder",让工程团队规模缩小 6-7 倍。

## 🔖 高价值金句时间戳
- `[08:39]` "we don't know Sierra and Deco existed ... we didn't think of competition much." — 对竞争的"天真"反而是优势;别被明星竞品吓退,先专注客户与价值。
- `[09:16]` "we're building a great product, rather than a sales team." — 8 人赢下 DoorDash 的底层逻辑:产品套利胜过销售堆人。
- `[11:44]` "it's fundamentally bogged down to markdown, and how can you improve markdown to more KPI." — 对 Agent 创业者最实操的一句:把 Agent 产品化为"可迭代的 markdown → KPI"。
- `[15:02]` "It's never about the idea. It's about if somebody is willing to pay you money for it." — 立项唯一准绳:有人愿付真钱,而非点子好坏或市场大小。
- `[17:33]` "The biggest bottleneck of every single enterprise AI deployment ... forward deploy engineer." — 指出企业 AI 落地的真正瓶颈,也是下一个大机会所在。
- `[22:32]` "If you take a look at all the successful AI companies, it's product." — AI 时代产品 > 销售;把最强资源压在产品交付价值上。
- `[23:37]` "things get really real if you burn the boats." — 断掉退路会逼你把东西真正做出来;而 AI 时代建东西成本极低,退路其实一直在。
