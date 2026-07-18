# AI 泡沫的真相:2025 年 YC 眼中最意外的事 / The Truth About The AI Bubble

> **来源**: [The Truth About The AI Bubble](https://www.youtube.com/watch?v=cqrJzG03ENE) · Y Combinator · 2025-12-22 · 时长 30:22
> **讲者**: The Light Cone 播客四位 YC 合伙人 —— Garry Tan(SPEAKER_00)、Diana Hu(SPEAKER_01)、Jared Friedman(SPEAKER_02)、Harj Taggar(SPEAKER_03)
> **一句话定位**: 从 YC 一线数据看 2025 年 AI 创业格局如何"稳定成型"——模型层商品化、价值回流应用层、泡沫其实是创业者的机会窗口,给想做 AI Agent 创业的人一份"现在该怎么打"的地图。

## 🎯 TL;DR(中文核心要点)
- **模型换旗**:Winter 26 批次里 Anthropic 首次超过 OpenAI 成为第一 API(OpenAI 曾一度 90%+),Gemini 也爬到约 23%。Claude 在编码上的口碑通过"个人 vibe coding"渗透到大家给产品选模型的决策。
- **别锁死单一模型**:成熟创业公司正把模型抽象成一个可热插拔的编排层(orchestration layer),不同任务用不同模型(例:用 Gemini 3 做 context engineering,喂给 OpenAI 执行),真正的护城河是**你自己的私有 evals + 垂直数据集**。
- **"是不是泡沫"是问错了人**:泡沫问题只对 Nvidia/超大厂(资本开支方)相关;在宿舍里做 AI 创业的你不是 Comcast,你是 YouTube——算力过剩=更便宜的原料=你的机会。
- **Carlota Perez 框架**:技术革命分"安装期(重资本、像泡沫)"与"部署期(应用爆发)",现在正处在过渡点——"未来的 Facebook / Google 还没被创立",它们诞生在部署期。
- **自建模型正从稀有技能变常见**:开源基座 + 针对性 RL 微调,8B 参数的垂直模型能在特定领域(如医疗)benchmark 上打赢大模型;但代价是要持续投入 post-training,大模型一升级就可能把你的微调优势抹平。
- **微调可能是烧钱陷阱**:第一波"AI + 行业"公司(如 Harvey)在 fine-tuning 上烧掉双位数百分比的融资却买不到优势,第二波(Legora、Giga)正逼近;把资本浪费在微调上,唯一赢家是持股更多的投资人。
- **AI 没让团队变小**:公司确实更快到千万 ARR,但到了 Series A 之后照样按老剧本扩张团队——瓶颈不是 idea,而是能真正执行的人;客户期待水涨船高,反而要招更多人。
- **别信 fast takeoff 恐慌**:scaling law 是 log-linear(每提升一档要 ~10x 算力),加上"人类和组织天然抗拒变化 + 企业落地慢",社会有时间消化——这对创业者反而是好消息。

## 🧭 适合谁 / 什么时候看
- 正在纠结"现在入场 AI 创业会不会追高接盘/泡沫破了怎么办"的早期创始人。
- 要做**垂直 AI Agent**、需要决定"自建/微调模型 vs 直接调 API + 编排层"的工程师型创始人。
- 想理解 2025 年模型格局(Anthropic/OpenAI/Gemini 此消彼长)与融资/团队现实的人。

## 📝 分段精读

### 1. 换旗:Anthropic 成为 YC 批次首选模型 / Anthropic overtakes OpenAI at YC `[00:50–05:36]`
**要点(中文)**: YC 在申请里问所有创始人"你的 tech stack 和首选模型是什么"。Winter 26 批次,Anthropic 首次略微超过 OpenAI 成为第一 API——而当年 OpenAI 曾占 90%+。Diana 认为核心原因是 Anthropic 有意把"编码能力"当作内部北极星指标(Tom Brown 印证),而 coding agent / vibe coding 恰好成了创造巨大价值的大品类。Jared 补充了一个关键的"渗透效应":大多数人用 Claude 其实不是做编码,但因为个人写代码时熟悉了 Claude 的"人格",给自家产品选模型时更倾向它——哪怕产品跟编码无关。Gemini 3 也被这几位合伙人亲测并印象深刻,爬到约 23%。
> 🗣️ "In this batch, the number one API is actually Anthropic, came out a bit more than OpenAI. Which who would have thought? ... when we started this podcast series back then, OpenAI was like 90 plus percent." —— Diana Hu (SPEAKER_01)
> 译:这一批里排第一的 API 其实是 Anthropic,略微超过了 OpenAI。谁能想到?……我们刚开始做这个播客那会儿,OpenAI 还占 90% 多。
> 🗣️ "So I wonder if there's like a bleed through effect where people are using Claude for their personal coding and then as a result, they're more likely to choose it for their application, even if their application is not doing coding at all." —— Jared Friedman (SPEAKER_02)
> 译:所以我怀疑存在一种"渗透效应"——大家用 Claude 写自己的代码,结果就更倾向于在自家产品里也选它,哪怕这个产品根本不做编码。

### 2. 为什么还没有更多 AI 消费级应用? / Why aren't there more AI consumer apps `[05:34–07:01]`
**要点(中文)**: Harj 说今年他生活里最大的变化,是给"个人生活"做大量 prompting 和 context engineering(买房时把每份验房报告塞进一个超长 ChatGPT 对话,以拉平自己和中介之间的信息差)。他觉得"这本该有个 App 来替我做完所有活儿",但又不敢完全信任模型的准确性、高价值交易里还得亲自下功夫——这正好指向一个尚未被填满的消费级机会:把重复的 prompt/上下文工程封装成产品。Garry 还提到自己手动做"LLM 竞技场"(Claude/Gemini/ChatGPT 各开一个标签页,同一任务喂进去、再让 Claude 互相检查)。
> 🗣️ "One of the big changes for me this year is just the amount of prompting and context engineering i do for like my life ... it just feels like there should be an app for that." —— Harj Taggar (SPEAKER_03)
> 译:今年我最大的变化之一,就是我为"自己的生活"做了大量的 prompting 和上下文工程……总觉得这本该有个 App 来干这件事。

### 3. 模型热插拔成为新常态 / Swapping models in and out is the norm `[07:00–09:08]`
**要点(中文)**: 到了 Series B 级别的公司不再"忠于某一家模型",而是把模型全部抽象掉,建一个编排层:新模型一发布就换进换出,按"每类 agent 工作谁最强"来分配(Diana 举例:一家垂直 AI Agent 用 Gemini 3 做 context engineering,再喂给 OpenAI 执行,并随新模型不断切换)。之所以能这么干,是因为**一切都以他们自己的、私有的 evals 为准绳**,而这套 evals 来自他们在受监管行业里积累的专有数据集。Garry 把这比作 Intel/AMD 时代——新架构出来就能换,前提是你站在栈的最高层。
> 🗣️ "They're actually abstracting all that away and building this orchestration layer where perhaps as each new release comes out they can swap them in and out." —— Diana Hu (SPEAKER_01)
> 译:他们其实是把这些全都抽象掉,搭一个编排层——每次有新模型发布,就能把它们换进换出。
> 🗣️ "They used gemini 3 to do the context engineering which they actually then fed into open ai to execute it ... it is all grounded based on the evals and the evals are all proprietary to them because they're a vertical ai agent." —— Diana Hu (SPEAKER_01)
> 译:他们用 Gemini 3 做上下文工程,再把结果喂给 OpenAI 去执行……这一切之所以站得住,是因为都以 evals 为准绳,而这套 evals 完全是他们私有的——因为他们是一家垂直 AI Agent 公司。

### 4. AI 是泡沫吗?宿舍里的你其实是 YouTube / The big AI bubble question `[09:08–14:32]`
**要点(中文)**: 这是全片最值钱的思维框架。"是不是泡沫"只对资本开支方(Nvidia、超大厂)才是要命的问题;对在宿舍里做创业的人,你不是 Comcast,你是 YouTube。Garry 用 90 年代电信泡沫类比:正因为有过剩且便宜的带宽,YouTube 才可能存在;算力过剩=更便宜的原料=更多机会。Jared:就算明年 Nvidia 的股票跌了,也不代表现在做 AI 创业是坏时机——那是它们的资本开支,不是创业者的。Diana 引经济学家 Carlota Perez:技术革命有"安装期(重资本、像泡沫、狂热)"和"部署期(应用大爆发)",现在正处在过渡,对创始人是大利好——"未来的 Facebook / Google 还没被创立",它们诞生在部署期(就像互联网的 dark fiber 过剩,最终互联网仍是巨大经济引擎)。
> 🗣️ "If you're doing a start-up in your dorm room it's like the AI equivalent of like YouTube and like kind of doesn't really matter that much ... even if [Nvidia's stock] does [go down], that doesn't actually mean that it's like a bad time to be working on an AI startup." —— Jared Friedman (SPEAKER_02)
> 译:如果你在宿舍里做创业,那你就是 AI 时代的 YouTube,(泡沫)其实没那么重要……就算 Nvidia 股价真跌了,也不代表现在做 AI 创业是个坏时机。
> 🗣️ "That's why youtube was able to exist ... if you just have a whole bunch of extra bandwidth that isn't being used and is relatively cheap the cost is low enough for like something like youtube to exist." —— Garry Tan (SPEAKER_00)
> 译:这正是 YouTube 得以存在的原因……当你手里有一大堆没被用上、相对便宜的过剩带宽,成本就低到足以让 YouTube 这样的东西存在。
> 🗣️ "Startups like the future facebook or the future google are yet to be started because those come in in the deployment phase." —— Diana Hu (SPEAKER_01)
> 译:未来的 Facebook、未来的 Google 这类创业公司还没被创立,因为它们诞生在"部署期"。

### 5. 数据中心与能源:把它搬到太空 / Space as the solve for data centers & energy `[14:32–17:27]`
**要点(中文)**: 一个关于"约束反推方向"的插曲。18 个月前 StarCloud 说要在太空建数据中心时被全网嘲笑,如今 Google、Elon 都在做同样的事。原因是地面约束太硬:发电跟不上(连喷气发动机供应链都紧到要提前两三年下单)、加州 CEQA 等法规拖累建设、没有足够土地。于是"逃生阀"就是去太空。YC 甚至凑齐了解决数据中心瓶颈的"三件套":太空数据中心(无土地)、Boom/Helion(能源/超音速)、以及 Garry 刚投的太空聚变公司 Zephyr Fusion。对 AI 创始人的意义:基础设施瓶颈是真实且会长期存在的,但那是超大厂的战场,不是你的。
> 🗣️ "We literally don't have power generation ... these constraints end up like influencing like fairly directly what the giant tech companies need to do to win the game three or five years out." —— Garry Tan (SPEAKER_00)
> 译:我们是真的没有足够的发电能力……这些约束会相当直接地决定,那些巨头为了赢下三五年后的这局游戏必须去做什么。

### 6. 自建模型的兴起:开源 + RL 微调 / Interest in starting model companies `[17:27–21:01]`
**要点(中文)**: 做模型公司这件事正从"稀有技能"变成"常见技能"。十年前 OpenAI 那种"研究脑+工程脑+商业脑"的团队配置极其罕见(Ilya/Greg/Sam),如今具备这三种背景的人已经很多,资本也可被教会。更大的雪球来自 RL:在开源基座上用特定 RL 环境和任务做微调,完全可能造出打赢大模型的垂直模型(Diana:某 YC 医疗创业公司靠最好的数据集,用仅 80 亿参数就在多个医疗 benchmark 上超过 OpenAI)。但 Garry 泼冷水:你必须有 post-training 基础设施并持续投入——有 YC 公司微调打赢了 GPT-3.5,结果 GPT-4.5、5.1 一出就把优势"炸没了"。你得一直往前跑,持续贴着前沿。
> 🗣️ "It is very possible that you can create the best domain specific let's say healthcare model trained on a generic open source model by just doing fine tuning on it and doing rl it beats the regular big model." —— Diana Hu (SPEAKER_01)
> 译:完全有可能:你在一个通用开源模型上做微调 + RL,就能造出某个领域(比如医疗)最好的专用模型,而且它能打赢常规大模型。
> 🗣️ "They were doing fine tuning with rl but then gpt 4.5 and then 5.1 came out and basically blew their fine tuning out of the water you have to keep going." —— Garry Tan (SPEAKER_00)
> 译:他们用 RL 做微调(打赢了),可 GPT-4.5、然后 5.1 一出,基本上就把他们的微调优势炸得粉碎——你必须一直往前跑。

### 7. Vibe coding 成为大品类(但还不能 100% 上生产) / Vibe coding became a big category `[20:58–22:23]`
**要点(中文)**: 年初这几位还只是把 vibe coding 当作"观察到的一种创始人行为",一年后它成了有大量赢家的巨型品类(Replit、Emergent 等;Varun Mohan 去 Google 发布了 Antigravity)。但 Garry 明确点出边界:截至 2025 年底,vibe coding 还做不到 100% 可用、可信、可直接上生产的代码——不要以此为前提去承诺产品的可靠性。
> 🗣️ "It is not true that you can like ship a hundred a hundred percent solid production code today as of ... the end of 2025." —— Garry Tan (SPEAKER_00)
> 译:说你今天(截至 2025 年底)就能靠它交付 100% 可靠的生产级代码,这是不成立的。

### 8. AI 经济稳定成型,找 idea 回归常态难度 / AI economy has stabilized (& the AI 2027 piece) `[22:24–25:49]`
**要点(中文)**: Jared 说 2025 最让他意外的是 AI 经济"稳定"下来了:2024 年底还感觉地在脚下移动、随时可能"另一只鞋落地";现在已分层成型——模型层、应用层、基础设施层,大家似乎都能赚很多钱,并出现了"在模型之上搭建 AI 原生公司的相对成熟打法"。副作用是:模型今年只是渐进改进、没有掀桌式突破,所以"等几个月就有大发布解锁一批新 idea"的红利消退,**找 idea 的难度回归常态**。Garry 补充对 fast takeoff 的怀疑:scaling law 是 log-linear(每进一档要 ~10x 算力),加上人类和组织天然抗拒变化、90% 企业连 IT 都没搞明白更别说 AI——这些"刹车"让社会有时间消化,这对创业者反而是好消息。
> 🗣️ "There's kind of like a relative playbook for how to build an ai native company on top of the models." —— Jared Friedman (SPEAKER_02)
> 译:现在已经有了一套相对成熟的打法,教你怎么在模型之上搭建一家 AI 原生公司。
> 🗣️ "Finding ideas is sort of returning to sort of normal levels of difficulty." —— Harj Taggar (SPEAKER_03)
> 译:找 idea 这件事,正在回归到常态的难度水平。
> 🗣️ "This fast takeoff argument ... even with the scaling law it is uh log linear so it is slower it requires like 10x more compute." —— Garry Tan (SPEAKER_00)
> 译:这套"快速起飞"的论调……即便有 scaling law,它也是 log-linear 的,所以更慢,每提升一档都需要大约 10 倍的算力。

### 9. 收入飞快但团队照样要扩:第二波公司与执行力瓶颈 / Founders still need to hire teams `[25:49–30:22]`
**要点(中文)**: 去年"公司只靠创始人就做到百万 ARR 拿 Series A"很反常,但今年并没演化成"不加人就冲到千万 ARR"——他们到了 Series A 之后照样按老剧本扩张团队;只是因为收入来得太快,瓶颈在人,而非需求。两个现实:(1)**资本作为护城河**——Harvey 这类公司很早就把 Sandhill Road 上能开 1000 万~1 亿支票的~30 家 VC 的钱"包圆",让后续 Series A 无人可投,以资本为壁垒(但 Legora 正快速逼近)。(2)**微调是烧钱陷阱**——第一波 AI+行业公司(Harvey)可能在 fine-tuning 上白烧了双位数百分比的资本,第二波(Legora、Giga)证明"没那么简单";烧钱微调却买不到优势,唯一赢家是持股更多的投资人。Harj 的判断:AI 让客户期待水涨船高,你反而要招更多人;瓶颈不是 idea,而是能真正执行的人。Garry 给出正面榜样:Gamma 只用 50 人做到 1 亿美元 ARR——"少人多收入"的反向炫耀,是个好趋势;但"一个人跑一家万亿公司"的时代还没到(2026 也不会)。
> 🗣️ "Now we're seeing a second wave of companies like legora and giga and it [turns out] like oh actually like it isn't so simple." —— Jared Friedman (SPEAKER_02)
> 译:现在我们看到第二波公司(如 Legora、Giga),结果发现——哦,其实事情没那么简单。
> 🗣️ "I don't think anyone's bottlenecked on ideas but they're bottlenecked on like people who can execute really well." —— Harj Taggar (SPEAKER_03)
> 译:我不认为有谁是被 idea 卡住的,大家卡住的是"能真正把事情执行好的人"。
> 🗣️ "It's a good trend to have the reverse flex which is like look at all this revenue and look how few people work for us." —— Garry Tan (SPEAKER_00)
> 译:这是个好趋势——反向炫耀:看我们做出这么多收入,而团队却这么小。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **默认多模型 + 编排层**:一开始就把模型抽象成可热插拔的一层,按任务分配(如 context engineering 用一家、执行用另一家),新模型发布就能快速换入换出,不要把架构锁死在单一供应商。
- [ ] **把护城河建在私有 evals + 专有数据集上**,而不是模型本身。选一个(最好受监管、数据难拿的)垂直领域,持续积累"只有你有"的评测集与数据。
- [ ] **微调要算清 ROI**:先用 API + 好的 prompt/上下文工程把 PMF 打出来;只有当你有 post-training 基础设施、能持续迭代、且垂直数据确实能带来可衡量优势时再做 RL 微调——否则大模型一升级就把你炸没,唯一受益的是投资人。
- [ ] **用"YouTube 心态"看泡沫**:算力过剩=你的廉价原料。别因"是不是泡沫"的宏观焦虑而不入场;把注意力放在部署期的应用价值上。
- [ ] **找一个"本该有 App 却还没有"的重复性上下文工程场景**(参考 Harj 的买房例子),把人们手动堆 prompt 的高价值流程产品化。
- [ ] **别指望 AI 帮你省掉团队**:按"客户期待会水涨船高、要靠人执行"来做人力规划;招"能真正执行"的人是核心瓶颈,提前布局招聘。
- [ ] **融资时理解"资本护城河"**:头部赛道里,早期领先者可能会用资本包圆一轮投资人来卡后来者;评估自己是要挤进拥挤赛道,还是选一个资本壁垒还没形成的垂直方向。

## 🔑 关键术语 / 概念
- **Orchestration layer(模型编排层)** — 把底层 LLM 全部抽象掉的一层,按任务/新版本把不同模型换进换出,让产品不依赖任何单一模型供应商。
- **Bleed-through effect(渗透效应)** — 用户因个人使用(如用 Claude 写代码)熟悉了某模型的"人格",从而在给产品选型时也更倾向它,哪怕用途无关。
- **Proprietary evals(私有评测集)** — 创业公司基于自己垂直领域数据构建的、外部拿不到的评测标准,是模型商品化时代真正的护城河。
- **Installation phase / Deployment phase(安装期 / 部署期)** — 经济学家 Carlota Perez 的技术革命两阶段论:安装期重资本、像泡沫;部署期应用大爆发,"未来的巨头"诞生于此。
- **Fast takeoff(快速起飞)** — AGI 会在极短时间内自我加速的假说;讲者用 scaling law 的 log-linear 特性(每进一档要 ~10x 算力)+ 社会/组织抗拒变化来反驳。
- **Log-linear scaling** — 模型能力随算力对数线性提升,即每要好一档就要约 10 倍算力,意味着进步比"指数爆炸"更慢、更可控。
- **Reverse flex(反向炫耀)** — 用"极少的人做出极高收入"来炫耀(如 Gamma 50 人做到 1 亿 ARR),与传统"看我们融了多少钱、雇了多少人"相反。
- **Capital as a moat(以资本为护城河)** — 领先者通过"包圆"能开大额支票的投资人,让后来者拿不到后续融资,从而以资本本身构筑壁垒。

## 🔖 高价值金句时间戳
- `[01:00]` "In this batch, the number one API is actually Anthropic, came out a bit more than OpenAI." — 模型偏好换旗的一手数据:Anthropic 首次登顶 YC 批次。
- `[07:00]` "Building this orchestration layer where perhaps as each new release comes out they can swap them in and out." — Agent 架构的标准答案:模型可热插拔的编排层。
- `[11:38]` "If you're doing a start-up in your dorm room it's like the AI equivalent of like YouTube and like kind of doesn't really matter that much." — 泡沫焦虑与创业者无关的最佳一句总结。
- `[12:32]` "Startups like the future facebook or the future google are yet to be started because those come in in the deployment phase." — 用 Perez 框架给"现在入场太晚了吗"一个否定回答。
- `[20:25]` "They were doing fine tuning with rl but then gpt 4.5 and then 5.1 came out and basically blew their fine tuning out of the water you have to keep going." — 自建模型的现实成本:得永远贴着前沿跑。
- `[28:08]` "I don't think anyone's bottlenecked on ideas but they're bottlenecked on like people who can execute really well." — 团队与执行力才是真瓶颈。
- `[29:02]` "It's a good trend to have the reverse flex which is like look at all this revenue and look how few people work for us." — 小团队高收入是新时代的正确姿势(Gamma:50 人 1 亿 ARR)。
