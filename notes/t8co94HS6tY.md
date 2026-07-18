# Amplitude 从 AI 怀疑者到「全押 AI」:老牌 SaaS 的自我重造 / How Amplitude Went From Skeptics to "All In" on AI

> **来源**: [How Amplitude Went From Skeptics to "All In" on AI](https://www.youtube.com/watch?v=t8co94HS6tY) · Y Combinator · 2025-12-03 · 时长 44:22
> **讲者**: 嘉宾 Spencer Skates(Amplitude CEO / 联合创始人,YC W12);主持 The Lightcone 团队 —— Garry Tan、Harj Taggar,以及另两位 YC 合伙人(SPEAKER_00 / SPEAKER_03,推测为 Jared Friedman / Diana Hu)
> **一句话定位**: 一家做了十年分析、原本对 AI 深度怀疑的 SaaS 公司,如何用「自下而上让全员先信、先用工具」的方式完成 AI 重造 —— 对想做 AI Agent 创业的人,既讲清了 incumbent 的软肋,也讲清了「AI 原生产品」和传统 SaaS 在方法论上的根本差别。

## 🎯 TL;DR(中文核心要点)
- **AI 产品和 SaaS 的根本差别:SaaS 是「问客户要什么」,AI 是「技术优先」。** 因为模型能力「参差不齐(jagged)」,客户根本描述不出「可能做到什么」,你必须先吃透模型能力,再反向映射到产品。
- **转型第一步不是「定义要造什么 AI 产品」,而是让现有团队先用起来、先相信。** Amplitude 办了一场「AI Week」:两天培训 + 一场当众 vibe code(现场给 Amplitude 撸了个 dark mode,还当场撞 bug 又修好),再加黑客松,让所有 leader 现身示范。
- **AI 采用是「自上而下(tops-down)」的反常现象。** 通常是工程师推着公司用新技术,这次却反过来 —— 因为投资人、高管、世界领袖都被「AI 愿景」说服了,而能力还在追赶。Spencer 直言:「Sam Altman 是这一代最好的销售,没有之一。」
- **「AI 杀死 SaaS」被严重高估。** 很多业务流程需要「极高的确定性保证」(往 CRM 写一条记录必须 100% 在),别学那些想让 agent 端到端全包的公司 —— 用户能「编辑、重做」的产品设计,才是 AI × B2B 的关键。
- **对创业者:别做「AI 可见性(AI visibility)」这类会飞速商品化的功能。** 真正的生意必须在下游(如 Air Ops 把可见性接到内容生成业务上)。Amplitude 几周就做出来、免费送,把它当获客工具用。
- **打法建议:选一个「具体问题 + 具体买家」,而不是做又一个通用 agent builder。** 每个 YC batch 都有好几家做通用 agent,胜出的是对某类买家有强观点、能解决其真实痛点(如企业采用 AI 的安全合规顾虑)的公司。
- **心态是第一过滤器:成功者都熬过了「理性上该放弃」的那一两年。** 关键不是聪明,而是把「为什么创业」的顶层节点(top node)想到极其清晰,才能在长期不确定中反复锚回它。内在动机 > 外部认可/赚钱。
- **创始人 → 大公司高管是最难的一跃。** 创始人「冲向最难的问题、身先士卒」;高管却必须承认「层级(hierarchy)有其道理」、大量说不、变成「你曾经嘲笑的那种只评判别人工作的人」。

## 🧭 适合谁 / 什么时候看
- 想从 incumbent 手里抢市场的 AI Agent 创始人 —— 听听在位者亲口说「哪里是软肋、哪里别碰」。
- 正在纠结「先定产品还是先建团队能力」的技术型创始人:这集给出了「先让人用起来、自下而上长出产品」的具体剧本。
- 还在找 idea、或担心自己做的是「feature 不是 company」的人。
- 从工程师视角转向要学销售、找导师、扛长期不确定性的早期创始人。

## 📝 分段精读

### 1. 从怀疑到入局:Amplitude 的 AI 转身 / From Skeptics to Embracing AI `[00:38–11:00]`
**要点(中文)**: Amplitude 曾长期是 AI 怀疑派 —— 创始团队是 MIT 算法背景,受不了「不干活只吹」的 grifting。真正的转折是 2024 年底看到 Cursor / Claude Code / Codex 让写代码明显更快,才确信「这里有东西」。落地抓手有两个:请来硅谷老将 Wade Chambers 当工程负责人,收购 YC 公司 Command AI(带来实战过模型能力的团队)。转型的第一步不是定义产品,而是办「AI Week」把全组织(含产品、设计)训练成会用工具、且相信工具的人。即便只有 200 人的产研团队,让全员真正上船也花了整整一年。

> 🗣️ "if you look at the capabilities of any of these models, it's like, they're very, very jagged. So there's some things they're exceptional about. And there's some things that there's absolutely terrible about." —— Spencer Skates
> 译:如果你看这些模型的能力,它是非常非常「参差不齐」的 —— 有些事情它们做得极其出色,有些事情则烂到极点。

> 🗣️ "we had our, like one of our product leaders, you know, vibe code, like a dark mode for Amplitude in front of the entire organization, which is actually very scary, but actually it happened, you know, they ran into a bug, but they happened to sort it out." —— Spencer Skates
> 译:我们让一位产品负责人当着整个组织的面 vibe code 出 Amplitude 的暗黑模式 —— 这其实挺吓人的,但真做成了;中途撞了个 bug,恰好也当场解决了。

### 2. AI 产品 vs SaaS 的根本差别:技术优先 / The Core Difference: Tech-First `[10:22–13:17]`
**要点(中文)**: 这是全集最值钱的方法论。SaaS 是史上最好的交付循环:问客户要什么 → 排优先级 → 造 → 交付 → 循环,Amplitude 十年就靠这个循环建立竞争力。但 AI 不行 —— 因为能力太 jagged,是「技术优先」的理解问题:你去问客户,他们根本描述不出「什么是可能的」,只会要「一匹更快的马」。所以你必须先熟悉模型能力,再把它反向映射回产品能做什么。这也解释了 AI 采用为何「自上而下」:投资人、高管、社会精英被愿景说服在前,能力追赶在后。

> 🗣️ "if you go to your customers and tell them and ask them what they want, like they're not even going to be able to describe what's possible. Give me a faster horse." —— Spencer Skates
> 译:如果你去问客户他们想要什么,他们甚至无法描述什么才是可能的 —— 只会说「给我一匹更快的马」。

> 🗣️ "with the capabilities of AI, because they're so jagged, it's a technology first, understanding of what is possible. And so if you go to your customers and tell them and ask them what they want... what's much more important is you have to be familiar with the capabilities of the models, then how those can map back into what your product does." —— Spencer Skates
> 译:由于 AI 能力如此参差,它是一种「技术优先」的、对可能性的理解。所以真正更重要的是:你必须先熟悉模型的能力,再看这些能力如何反向映射到你的产品要做的事情上。

> 🗣️ "I think Sam Altman is the best salesperson of this generation by no bar none." —— Spencer Skates
> 译:我认为 Sam Altman 是这一代最好的销售,毫无疑问、没有之一。

### 3. AI 原生的心态,不是年龄 / AI-Native Is a Mentality, Not an Age `[16:45–18:37]`
**要点(中文)**: 谁在 AI 时代掉队?不是年纪大的人,而是心态没转过来的人。SaaS 老手擅长那个「问-排-造」的循环;AI 原生的做法是:先看某个领域的 state of the art,再问「如果用 AI 原生方式重做,会怎样」。但反过来,很多 AI 原生团队的短板是「没学过这个问题为什么被这样解决」—— 只想从零造新界面,丢掉了过去十年的领域积累(比如做分析却让用户看不到数据)。适应得最好的工程师,始终清楚:代码本身不是目的,交付只是「解决客户问题」的副产品。

> 🗣️ "what a lot of these AI native teams are really missing is they haven't learned the product and the problem and why things are solved the way they're solved. And so like they try to create these new interfaces from scratch without drawing on the previous expertise." —— Spencer Skates
> 译:很多 AI 原生团队真正缺的,是他们没搞懂这个产品、这个问题,以及「为什么过去要这样解决」;于是他们从零造新界面,却没有借用过去积累下来的专业经验。

> 🗣️ "the code is not an end in itself. It just like shipping it, that's just a side effect of solving whatever problem, for the customer." —— Spencer Skates
> 译:代码本身不是目的;把它发布出去,只是「为客户解决某个问题」的副产品而已。

### 4. 「AI 杀死 SaaS」被高估 & 别做端到端全包 / "AI Killing SaaS" Is Overblown `[18:37–20:30]`
**要点(中文)**: Garry 分享了一个反直觉的用户行为:他是 YC 内部 agent 的「超级用户」,而这个 agent「大多数时候仍然会失败」—— 他只是换个问法、换个模型(Gemini 3 不行就试 Claude、GPT 5.1)、调推理档位,最终把它跑通;在传统 SaaS 里,软件坏一次你就再也不用了。Spencer 借此点破:正因为很多业务流程需要极高的确定性保证,「AI 杀死 SaaS」被严重高估。呼应 Karpathy 的观点 —— 别想让 agent 端到端全包一个流程,让用户能「编辑、重做」的产品设计,才是 AI × B2B 的胜负手。

> 🗣️ "you have to like rewire your brain to be, it's like working with a child right now." —— Garry Tan
> 译:你得给自己的大脑重新布线 —— 现在用它,就像在带一个小孩。

> 🗣️ "This is why I think a lot of the hype in that AI killing SaaS is way overblown because particularly for a lot of business workflows, like very high guarantees on performance are fundamental to it." —— Spencer Skates
> 译:这就是为什么我认为「AI 杀死 SaaS」的炒作被严重高估 —— 因为对很多业务流程来说,对性能的极高确定性保证是根本要求。

> 🗣️ "a lot of these businesses are trying to overshoot the mark and just say, okay, well, hey, we'll just have this agent handle this workflow end to end. Actually the editing and redoing it... is actually incredibly important." —— Spencer Skates
> 译:很多公司都想一步登天,说「让这个 agent 端到端处理整个流程就好了」;可实际上,让用户能去编辑、能去重做,才是极其重要的。

### 5. 「Feature 还是 Company」之争 & incumbent 的软肋 / Features vs Companies `[23:30–29:06]`
**要点(中文)**: 这段直接对创业者。以「AI visibility(AI 可见性/在 LLM 里被引用的排名)」为例:Amplitude 几周就做出来、免费送,当作强力获客,一发布免费版新注册翻倍。结论 —— 这类东西会飞速商品化,真正的生意必须在「下游」构建(如 Air Ops 把可见性接到内容生成业务)。Incumbent 的优势就是有几亿营收垫底,可以免费送来碾压。而 incumbent 的软肋:凡是 Google 想做的都是机会 ——「Google 是史上最差的 B2B 公司」,太慢太保守(邮件、Workspace、Google Docs 对标 Notion、编码工具的 GTM)。对新公司:别做又一个通用 agent builder,要「选具体问题 + 具体买家」,对某类买家有强观点(如解决企业采用 AI 的安全合规顾虑)。他还随口抛了个点子:「科技支持界的 Uber」—— 有钱但不懂技术的老人 × 极需赚钱且懂技术的年轻人。

> 🗣️ "you're going to have to construct a real business kind of downstream." —— Spencer Skates
> 译:你必须在下游构建出一个真正的生意。

> 🗣️ "picking a particular problem in a particular buyer is going to be a much more successful way of building a business... having a strong point of view for a particular buyer that cares about some things." —— Spencer Skates
> 译:选定一个具体的问题、一个具体的买家,才是更可能成功的建业方式……对某个在意特定事情的具体买家,拥有一个强有力的观点。

> 🗣️ "there's going to be a cursor moment in analytics in the next two years. No question in my mind where people are going to use analytics with AI and you're going to be like, why did we ever do it the old way?" —— Spencer Skates
> 译:未来两年,分析领域会迎来一个「Cursor 时刻」—— 我毫不怀疑,人们会用 AI 来做分析,然后回头想:我们以前怎么会用老办法干活?

### 6. 找到 idea、学销售、找导师 / Finding the Idea, Learning to Sell, Finding Mentors `[29:06–34:50]`
**要点(中文)**: Amplitude 不是一开始就想到的。他们先做了语音识别公司 Sonalite(早期版 Siri),demo 惊艳、拿了一堆媒体报道,但「产品和技术就是不够好」,DemoDay 后直接关掉。真正的 idea 来自「工程师习惯自己造分析工具」—— 他们把内部自建的分析给别的公司看,对方说「我们要这个」,于是 2012 年 6 月 pivot 成 Amplitude。关键反思:分析虽是极度拥挤的红海,但相比语音识别这种「概率性、没有正确答案」的问题,分析是「能算出正确答案」的确定性问题,恰好适配他们这群 MIT 算法工程师 —— 「事后看,我们运气好,正好特别适合这个问题」。学销售的方法论:不是读书读会的,而是「像学一项运动或乐器」—— 亲自下场做,再找个好教练在旁边一周敲打你一次(他的销售教练 Mitch 一直逼问「客户的痛在哪」,直到他明白「他们要仪表盘」不是业务痛点)。找导师的心法:先把「你想学什么」在自己脑子里想清楚,再对来源保持开放。

> 🗣️ "we had always, built our own analytics in-house. It's like, it's what you do as an engineer. You're always like, I want to build this instead of paying Amplitude money." —— Spencer Skates
> 译:我们一直都是自己在内部搭建分析工具 —— 这就是工程师会做的事,你总是想「我要自己造这个,而不是花钱买 Amplitude」。

> 🗣️ "It's very much like learning a sport or to play an instrument in a lot of ways. You're not going to do it reading a book. You want to just do it and then get a little bit of advice and coaching on the side." —— Spencer Skates
> 译:这在很多方面很像学一项运动或学一种乐器 —— 你靠读书是学不会的;你要亲自去做,然后在旁边得到一点建议和辅导。

> 🗣️ "the best advice I can have is be clear in your own head about what you're trying to learn and then... be open to where it comes from." —— Spencer Skates
> 译:我能给的最好建议是:先在自己脑子里想清楚你到底想学什么,然后对它从哪来保持开放。

### 7. 内在动机:成功者的第一过滤器 / Intrinsic Motivation, the Top Node `[34:50–38:09]`
**要点(中文)**: 全集情绪最重的部分。Spencer 直言创业「情绪上极度痛苦」,他每隔几年就会到一个「想放弃」的点。对抗它的唯一办法,是回到最开始「为什么进这行」的顶层节点(top node)—— 把它想到极清晰,才能在极长的不确定期里反复锚回它,再从这个节点长出「造什么产品、怎么卖」的目标树。他引用《Founders at Work》:几乎每段创业旅程都有一个一两年后「理性上该放弃」的点,成功者「不知为何就是没放弃」—— 这是第一过滤标准。最忌讳的心态:「我先试试,起飞就 all in,不行就回去读研/上班」—— 这种给自己留后路的人,扛不过长期的存在性不确定。驱动力必须是内在的:为外部认可或为赚钱而做,你的续航会差得多。

> 🗣️ "there is a point that you get to a year, maybe two years in, where from a rational standpoint, you probably should quit. But for whatever reason, those successful ones don't. And so that is the number one filtering criteria." —— Spencer Skates
> 译:创业一到两年时,总会到一个点 —— 从理性角度看,你大概应该放弃。但不知为何,那些成功者就是没放弃。这就是第一过滤标准。

> 🗣️ "If you're doing it for, like, recognition from others or... because you're going to get paid a lot or whatever else, your ability to last through is going to be much, much worse than someone else's." —— Spencer Skates
> 译:如果你是为了别人的认可,或者因为能赚很多钱之类的原因去做,那你能坚持下来的能力,会比别人差得多得多。

### 8. 创始人 vs 大公司高管:最难的一跃 / Founder vs Big-Company Executive `[38:09–42:35]`
**要点(中文)**: 创始人的工作永远是「冲向业务里最难的问题,身先士卒」—— 最难的代码、最难的产品/设计、最难的客户、最难的员工问题,优秀创始人一头扎进去,把团队带在身后。但公司到 800 人后,你没法处处身先士卒,必须变得极其克制时间、对绝大多数事说不 —— 于是「你变成了自己讨厌的那种人」(以前嘲笑大公司高管只评判别人的工作,现在懂了为什么)。他也承认「层级(hierarchy)是有道理的」这件事至今让他别扭但不得不接受。这段也修正了「founder mode」最肤浅的理解:不是 100% 全程扎在细节里 —— 那在 800 人时根本不可能,而是有更多微妙的取舍。一个残酷又真实的彩蛋:有了 PMF 之后「你其实干得更轻松」,因为你有巨大的资源和杠杆,问题从「怎么活下去」变成「怎么高效部署这些资源」。

> 🗣️ "As a founder... your job is always... to run to the most difficult problem in the business and lead from the front... The great founders will go headfirst into it and lead from the front, and they will rally the rest of the team behind them." —— Spencer Skates
> 译:作为创始人,你的工作永远是冲向业务中最困难的问题,并身先士卒……伟大的创始人会一头扎进去、带头冲锋,把团队的其他人聚拢到身后。

> 🗣️ "what you realize is you become the person you hate. You'd always make fun of big companies. You'd always make fun of big company executives for not doing any work for themselves and just judging other people's work all the time. But there's a reason for that. And you have to embrace that reason." —— Spencer Skates
> 译:你会意识到,你变成了自己讨厌的那种人 —— 你以前总嘲笑大公司,嘲笑大公司高管自己不干活、整天只评判别人的工作;但那是有原因的,你必须接受这个原因。

> 🗣️ "Well, you have product market fit. You actually work less hard... So there's leverage that you have as a large company executive that you don't as a founder." —— Spencer Skates
> 译:有了产品市场契合,你其实干得更轻松……作为大公司高管,你拥有创始人所没有的那种杠杆。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先建「模型能力地图」,再定产品。** 别照抄「问客户要什么」的 SaaS 打法 —— 花时间摸清你所选模型在你领域里「哪些做得极好、哪些烂」,再反向映射成产品功能;客户描述不出可能性。
- [ ] **给自己产品做「AI Week」式的团队上手。** 哪怕只有 3 人,先让全员用 Cursor/Claude Code 把自己的活干得更快,建立「相信 + 会用」的共识,再自下而上长出功能(Amplitude 的 MCP server、AI Visibility 都是工程师自发做的)。
- [ ] **产品设计默认「人机协作、可编辑可重做」,而非 agent 端到端全包。** 对确定性要求高的 B2B 工作流,把「让用户轻松纠错/重试」当成一等公民 —— 这是 AI × B2B 的胜负手。
- [ ] **别做会飞速商品化的「薄壳功能」(如 AI visibility)。** 若你的核心能力 incumbent 几周就能免费送,先想清楚「下游的真生意」在哪,再决定要不要做。
- [ ] **聚焦「一个具体问题 × 一个具体买家」,而不是又一个通用 agent builder。** 找一类有强付费意愿、有明确顾虑(如安全/合规)的买家,对他们建立强观点。
- [ ] **优先攻 incumbent 反应最慢的地盘。** 参考「凡是 Google 想做的」这类信号 —— 太慢太保守的在位者,GTM 和产品化是软肋,即使技术已被验证也来不及落地。
- [ ] **在创业前把「为什么做这件事」的顶层节点写到极清晰**,并诚实自查:你能在「理性上该放弃」的那一两年里靠它撑住吗?为赚钱/认可而来的人续航更差。

## 🔑 关键术语 / 概念
- **Jagged capabilities(参差不齐的能力)** — 指当前 AI 模型能力分布极不均匀:有些任务超神、有些任务极烂。这是「AI 产品必须技术优先」的根本原因。
- **Tops-down adoption(自上而下的采用)** — 与以往「工程师推动公司用新技术」相反,这轮 AI 是投资人/高管/社会精英先被愿景说服、自上而下推动,而模型能力仍在追赶。
- **AI Week** — Amplitude 的转型抓手:约两天全员培训(含当众 vibe code 示范)+ 一场「把手头的活用 AI 干得更快」的黑客松,让 leader 现身示范、全组织建立共识。
- **AI Visibility(AI 可见性)** — 衡量/优化你的品牌在 LLM 回答中被提及、被引用的表现,类比 SEO;会飞速商品化,单独难成公司。
- **Features, not companies(是功能,不是公司)** — 对某类 AI 产品的批评:能被 incumbent 几周复制并免费送的东西,只是功能,真生意得在「下游」构建。
- **"Cursor for X"(某领域的 Cursor 时刻)** — 指某垂直领域被 AI 重做后出现「回不去」的拐点;Spencer 预测两年内分析领域会有这样的时刻。
- **Top node(顶层节点)/ goal tree(目标树)** — 把「为什么创业」这个最顶层的动机想清楚,再往下派生「造什么产品、怎么卖」;不确定时反复锚回顶层节点。
- **Founder mode vs 大公司高管** — 创始人「身先士卒冲最难的问题」;高管必须克制时间、承认层级、大量说不 —— 这是最难的一次身份转变。

## 🔖 高价值金句时间戳
- `[04:00]` "if you look at the capabilities of any of these models, it's like, they're very, very jagged." — 一切 AI 产品方法论的起点:能力参差,所以不能照搬 SaaS。
- `[10:22]` "Give me a faster horse." — 客户描述不出可能性,别用「问客户要什么」的方式做 AI。
- `[12:00]` "I think Sam Altman is the best salesperson of this generation by no bar none." — 解释了 AI 采用为何反常地「自上而下」。
- `[18:37]` "you have to like rewire your brain to be, it's like working with a child right now."(Garry Tan)— AI 工具会频繁失败,超级用户靠「换问法/换模型」跑通,而非放弃。
- `[19:30]` "This is why I think a lot of the hype in that AI killing SaaS is way overblown." — 高确定性工作流是 SaaS 的护城河,也是 AI × B2B 的设计约束。
- `[24:40]` "you're going to have to construct a real business kind of downstream." — 薄壳功能会商品化,真生意在下游。
- `[35:24]` "there is a point that you get to a year, maybe two years in, where from a rational standpoint, you probably should quit. But... those successful ones don't." — 创业成功的第一过滤器是心态而非聪明。
- `[38:40]` "you become the person you hate." — 创始人→高管转型中最扎心也最真实的觉悟。
