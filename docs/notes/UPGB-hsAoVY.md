# 微调的强力替代方案:给 LLM 装上"高跷"的递归自我改进 / The Powerful Alternative To Fine-Tuning

📄 **[点此查看全文转录 / Full transcript »](../transcripts/UPGB-hsAoVY.md)**

> **来源**: [The Powerful Alternative To Fine-Tuning](https://www.youtube.com/watch?v=UPGB-hsAoVY) · Y Combinator · 2026-02-27 · 时长 19:46
> **讲者**: Ian Fischer(Poetiq 联合创始人兼 co-CEO,前 Google DeepMind 研究员,曾在 YC 做过移动开发者工具创业并被 Google 收购)= SPEAKER_04;主持为 The Lightcone 团队(YC,含 Garry Tan / Diana Hu 等,以 SPEAKER_00–03 区分,身份无法逐一确证故保留标签)
> **一句话定位**: 与其花几百万到几亿美元去微调、每出一个新前沿模型就被"清零"重来,不如在模型之上构建可自动优化、模型无关的 agent харness(harness),让你的 agent 永远"站在最新模型的肩膀上"——对做垂直 AI Agent 的创始人是一条更省钱、更抗淘汰的技术路线。

## 🎯 TL;DR(中文核心要点)
- **微调是陷阱**:一旦进入 fine-tuning,你花几百万到几亿美元,下一个前沿模型一发布你就"点火烧掉",永远追不上。对创业者这是把钱和时间押在会迅速贬值的资产上。
- **正确姿势是"高跷(stilts)"**:把前沿模型当地基,在其之上构建 harness(代码 + prompts + 数据),让 agent 表现超过底座模型;新模型出来时同一个 harness 直接兼容,不用改任何东西就能再吃一波提升。
- **前沿模型不是竞争对手,而是你踩的高跷**:GPT/Claude/Gemini 越强,你的 agent 越强——这叫"对 the bitter lesson 免疫(vaccinated against the bitter lesson)"。
- **harness 本质是可手搓的,但很难搓好**:它就是"code, prompts, data",理论上你用 Claude Code 也能拼;难点在于要有大量 insight 才能真正调好,Poetiq 把这一步自动化(递归自我改进的"元系统")。
- **成绩背书**:7 人团队,用 <$100,000 的优化成本在 Humanity's Last Exam 上做到 55%(高于 Anthropic Claude Opus 4.6 的 53.1%);在 ARC-AGI v2 上以 Gemini 3 Pro 为底座、用一半成本比 Gemini 3 DeepThink 高 9 个百分点。对比:基础大模型一次训练动辄上亿美元。
- **把"懂数据"外包给 AI**:传统 ML 铁律是"你必须极其了解你的数据集";现在让元系统自己去看数据、找 failure modes、找 robust reasoning strategies,人不去手动 monkey around。
- **真正的杠杆在 reasoning strategies(写成代码),不只是更好的 prompt**:纯自动 prompt 优化(如 GEPA)只能拿到一部分收益;加上用代码写的推理策略,他们把某任务从 5% 拉到 95%。
- **创始人心态**:世界变化极快,每天都用 AI 做点东西,去探它能力的边界;"Don't limit yourself"。

## 🧭 适合谁 / 什么时候看
- 正在做垂直 AI Agent、纠结"要不要微调/自训模型"的技术创始人。
- 已经手搓了 agent/harness、卡在"可靠性和鲁棒性差最后一公里"上不去的团队。
- 想理解"为什么应该把底层模型当可热插拔的通用层(common layer)"、以及如何在架构上对模型迭代免疫的工程师。
- 想看一个 7 人前 DeepMind 团队如何用极低成本屠榜(ARC-AGI / HLE)的具体打法。

## 📝 分段精读

### 1. Poetiq 是什么 / 递归自我改进 / What Is Poetiq & Recursive Self-Improvement `[00:40–02:07]`
**要点(中文)**: Poetiq 在做"递归自我改进(recursive self-improvement)"——AI 让自己变得更聪明,被视作 AI 的圣杯。他们的核心洞察是:能比业界其他方案"更快更便宜"地做到这件事。别人的思路大多要求"从零训练一个新 LLM",成本上亿、耗时数月;而大厂(Anthropic/OpenAI/Google)也在探索递归自我改进,但停留在"必须训一个新模型"这个层级上。
> 🗣️ "recursive self-improvement is this, you know, kind of the holy grail of AI where the AI is making itself smarter." —— Ian Fischer / SPEAKER_04
> 译:递归自我改进是 AI 的圣杯——AI 在让自己变得更聪明。
> 🗣️ "The core insight that we had is that we could do recursive self-improvement far faster and cheaper than all of the other ways that people had been proposing to do this." —— Ian Fischer / SPEAKER_04
> 译:我们的核心洞察是:我们能比别人提出的所有方案都更快、更便宜地实现递归自我改进。

### 2. 微调陷阱 & "高跷"比喻 / The Fine-Tuning Trap & "Stilts" `[02:07–05:05]`
**要点(中文)**: 主持人一针见血:进了微调这条路,你花几百万到几亿美元,下一个前沿模型一出你就"追不上、要么倒闭"。Ian 给出替代范式:不要把前沿模型当竞争对手,而当作你踩上去的"高跷"——在模型之上做一个自动生成的、总能跑赢底座模型的系统(harness / agentic system)。关键优势:**新模型发布时,同一个 harness 完全兼容,什么都不用改就能再吃一波性能提升**,不像微调那样"烧掉几亿美元还得重来"。
> 🗣️ "the second you're in fine-tuning land, I'm spending, you know, millions to hundreds of millions of dollars. And then guess what? Like, I just lit it on fire because, you know, the next version of the frontier model comes out, and I'll never catch up." —— 主持人 / SPEAKER_02
> 译:一旦进了微调这块地,我就在花几百万到几亿美元;然后猜怎么着?下一版前沿模型一出,我等于把这笔钱一把火烧了,而且永远追不上。
> 🗣️ "we don't view the, you know, the frontier models as competitors. They're, you know, they're the ones that were using the stilts, you know, building stilts to stand on top of." —— Ian Fischer / SPEAKER_04
> 译:我们不把前沿模型看作竞争对手,它们是我们用来搭高跷、站上去的地基。
> 🗣️ "when the new model comes out, that same harness is perfectly compatible with it. And you don't need to change anything to get the, you know, an even bigger performance bump." —— Ian Fischer / SPEAKER_04
> 译:新模型一出,同一个 harness 完全兼容,你什么都不用改,就能拿到更大的性能跃升。

### 3. 屠榜:ARC-AGI 与 Humanity's Last Exam / Topping ARC-AGI & Beating Claude on HLE `[05:05–08:40]`
**要点(中文)**: 用具体战绩证明"高跷"逻辑:Gemini 3 DeepThink 登顶 ARC-AGI v2(45%),两天后 Poetiq 以更便宜的 Gemini 3 Pro 为底座、用一半成本反超 9 个百分点(54%,$32/题)。在 Humanity's Last Exam(2500 道各领域专家出的极难题)上做到 55%,高于上一周 Anthropic Claude Opus 4.6 的 53.1%;整个优化成本 <$100,000,团队只有 7 人——对比大模型单次训练动辄上亿美元。主持人还点出很多顶尖创始人已经在手动做的事:把底层模型当"可切换的通用层",难验证的 bug 丢给某个模型、架构问题丢给另一个模型,而 Poetiq 把这个"人工调度"自动化了。
> 🗣️ "we were half the cost of Gemini 3, DeepThink because we were building on top of Gemini 3 Pro, which is a much cheaper model. But we still got in the end, a nine percentage point improvement." —— Ian Fischer / SPEAKER_04
> 译:我们只花了 Gemini 3 DeepThink 一半的成本,因为我们是搭在更便宜的 Gemini 3 Pro 上;但最终仍拿到 9 个百分点的提升。
> 🗣️ "we got to 55%, which is almost two percentage points higher than the... previous state-of-the-art. Which came out just last week from Anthropic with Claude Opus 4.6. They got 53.1% and we got 55%" —— Ian Fischer / SPEAKER_04
> 译:我们做到 55%,比上一个 SOTA 高近 2 个百分点——那个 SOTA 上周才出自 Anthropic 的 Claude Opus 4.6,它是 53.1%,我们是 55%。
> 🗣️ "a lot of founders that get very good results for agents, they treat the underlying model as a common layer that you can switch in between." —— 主持人 / SPEAKER_01
> 译:很多把 agent 做得很好的创始人,都把底层模型当成一个可以随时切换的通用层。

### 4. 元系统如何工作 & 超越 RL 的新 S 曲线 / How the Meta-System Works & A New S-Curve `[08:40–11:32]`
**要点(中文)**: harness 到底是什么?就是"code, prompts, data",搭在一个或多个语言模型之上——原则上你手搓、或用 Claude Code 也能拼出来,但**实际上要调好需要大量 insight**。Poetiq 的核心技术是递归自我改进的"元系统(metasystem)",它的产出物就是"能解决难题的系统"(难题 = 直接丢给 GPT-5.2 也很难给出可靠稳健结果的问题)。对已经自建 agent 的垂直创业公司,Poetiq 可以直接优化你整个 agent 或其中某些部分(只优化 prompts、只优化 reasoning strategies 等)。范式上,这不同于 RL:每个模型/每套模型有自己的 S 曲线,元系统本身也有自己的 S 曲线,随着两者变好,曲线不断上移,直到饱和或逼近 AGI。
> 🗣️ "These harnesses, they are code, prompts, data, built on top of one or more language models. And so this is something that, in principle, you can build by hand. Or with like cloud code, or whatever. But in practice, it takes a lot of work to do these, to have all the insights to make these work well." —— Ian Fischer / SPEAKER_04
> 译:这些 harness 本质就是代码、prompt、数据,搭在一个或多个语言模型之上。原则上你可以手搓、或用 Claude Code 之类拼出来;但实际上要做好需要大量工作、需要各种洞察。
> 🗣️ "you're a startup that's going after a particular vertical... you've put together your agent... then you can bring that to us. And we can optimize that entire agent or pieces of that agent." —— Ian Fischer / SPEAKER_04
> 译:如果你是在做某个垂直方向的创业公司、已经搭好了自己的 agent,你可以把它交给我们,我们能优化你整个 agent 或其中的某些部分。

### 5. 自动化 Prompt/Context 工程:从 5% 到 95% / Automating Prompt Engineering `[11:32–14:50]`
**要点(中文)**: 传统 ML 铁律是"你必须极其了解自己的数据集";Poetiq 把这件事外包给 AI——不花大量时间盯着数据,而是让元系统自己去看数据、决定要不要 context stuffing、要不要生成更多示例、去找 failure modes 与 robust reasoning strategies。有趣的是,元系统写出的 prompt"明显不是人会写的",甚至有个示例是错的,他们也不去改。**最大的杠杆不是"更好的 prompt",而是用代码写出来的 reasoning strategies**:纯自动 prompt 优化(如大家都在复现的 GEPA 论文)只能拿到一部分收益;在一个极难任务上,他们把 Gemini 1.5 Flash 从 5% 手动优化提示后再叠加推理策略,直接干到 95%。
> 🗣️ "We don't spend a lot of time looking at the particular data that we're working with. Instead, we're letting the poetic meta system look at that data." —— Ian Fischer / SPEAKER_04
> 译:我们不花大量时间去看具体数据,而是让 Poetiq 的元系统去看这些数据。
> 🗣️ "it's the ai's job to understand the data set and figure out where are the failure modes" —— Ian Fischer / SPEAKER_04
> 译:理解数据集、找出失败模式在哪里,这是 AI 的活儿(不再是人的)。
> 🗣️ "when we added on the the reasoning strategies we went from five percent to ninety five percent" —— Ian Fischer / SPEAKER_04
> 译:当我们叠加上推理策略后,性能从 5% 直接涨到了 95%。

### 6. 早期访问:给你的 agent 上高跷 / Early Access & Putting Your Agent on Stilts `[14:50–16:17]`
**要点(中文)**: 产品尚未正式发布,但 poetiq.ai 上有早期访问入口。Ian 明确他们在找的用例:**有一个真正难的问题、已经把能试的都试过了、就是没法做到足够可靠稳健、需要"更进一步"的创业公司或企业**。他们把能力总结为两类:"大幅提升 reasoning" 和 "大幅提升从模型里做 deep knowledge extraction"。核心承诺:让任何 agentic 公司都能站上 SOTA,并对 the bitter lesson"免疫"。
> 🗣️ "if you're a startup or a company who has a really hard problem and you've tried everything that you can to make it reliable and robust and you just can't get all the way there... let us know we're looking for problems like that" —— Ian Fischer / SPEAKER_04
> 译:如果你是一家有个真正难题、能试的都试了、就是没法做到足够可靠稳健的创业公司或企业……告诉我们,我们要找的正是这类问题。
> 🗣️ "the stilts basically let any agentic company become soda [SOTA] that's the idea" —— 主持人 / SPEAKER_02
> 译:高跷基本上能让任何做 agent 的公司都变成 SOTA,这就是核心思路。

### 7. 从 YC 创始人到 DeepMind 研究员 & 给工程师的建议 / Career Pivot & Advice for AI-Era Engineers `[16:17–19:46]`
**要点(中文)**: Ian 的第一家 YC 创业 Apportable(跨平台移动应用)被 Google 收购;收购给了他一个"重新想清楚自己想做什么"的机会。他发现自己最兴奋的是 AI 与机器人,而当时世界上最好的这批人在 Google,于是硬转方向,零背景切进机器学习研究,做了约十年(Google → DeepMind)。给想进 applied AI 创业的工程师的建议:世界变化极快,**每天都用 AI 做点东西,不断去探它能力的边界,构建你想构建的东西**。他举例:去年一个周末用 GPT-5 做了个 iPhone app,十年没碰过、却快到离谱——而那已是八个月前的"古董"了。
> 🗣️ "I realized that the problems that i was most excited about were really actually ai and... robotics and the best people in the world many of them in those fields were at google at the time" —— Ian Fischer / SPEAKER_04
> 译:我意识到自己最兴奋的问题其实是 AI 和机器人,而当时这些领域里全世界最好的一批人很多都在 Google。
> 🗣️ "you should just try things. And like every day, do something with AI." —— Ian Fischer / SPEAKER_04
> 译:你就该去动手试;而且最好每天都用 AI 做点什么。
> 🗣️ "Don't limit yourself. Like anything that you imagine, you should just try to use AI and see how far you can get with it." —— Ian Fischer / SPEAKER_04
> 译:别自我设限。任何你能想到的东西,都直接用 AI 去试,看能走多远。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **默认不微调**:把"要不要微调/自训模型"改成"能否用 harness(code + prompts + data)在模型之上解决"——除非有极强的护城河理由,否则别把钱押在会被下个模型清零的微调上。
- [ ] **架构上做到模型无关**:把底层 LLM 当可热插拔的 common layer,按任务把请求路由到最合适的模型(难验证的 bug → 一个模型,架构设计 → 另一个模型),并确保换新模型时上层几乎零改动。
- [ ] **把重心从"写更好的 prompt"上移到"用代码写 reasoning strategies"**:纯 prompt 优化(GEPA 类)只是起点,真正的大跳变来自代码化的推理/校验/重排/多次调用编排策略。
- [ ] **建可自动优化的评测闭环**:让系统自己去看数据、找 failure modes、生成示例并迭代,而不是人工逐条盯数据 monkey around;先搭好 evals,再让优化过程自动跑。
- [ ] **用"低成本高名次"证明力**:像 Poetiq 一样在公开 benchmark 或你垂直领域的硬指标上,以显著更低成本超越 SOTA/基础模型,作为对客户与投资人的硬背书。
- [ ] **锁定"最后一公里可靠性"这类难题**:如果你有一个"试过一切仍不够可靠稳健"的问题,这正是外部优化系统(如 poetiq.ai 早期访问)最有价值的切入点——把它形式化成可优化的目标。
- [ ] **每天动手用最新模型造东西**:一个周末就能验证一个想法(Ian 用 GPT-5 周末做 app);把"探模型能力边界"当日常习惯。

## 🔑 关键术语 / 概念
- **Recursive self-improvement(递归自我改进)** — AI 让自己变得更聪明,被称为 AI 圣杯;Poetiq 主张不必"从零训新模型"也能做到,且更快更省。
- **Harness / agentic system(推理外壳/agent 系统)** — 搭在一个或多个 LLM 之上的"code + prompts + data",让整体表现超过底座模型;新模型出来时保持兼容。
- **Stilts("高跷"比喻)** — 把前沿模型当地基踩上去:模型越高你越高,而非与它竞争。
- **The bitter lesson(苦涩的教训)** — Richard Sutton 的论断:靠通用算力/规模的方法长期胜过靠人工精调的方法;Ian 说好的架构能让你对它"免疫(vaccinated)",即新模型越强你越受益。
- **Poetiq metasystem(元系统)** — 递归自我改进的系统,其产出物是"能解决难题的系统";把"理解数据、找失败模式"外包给它。
- **Fine-tuning trap(微调陷阱)** — 花巨资微调,新前沿模型一出即贬值/追不上,被迫重来或倒闭。
- **ARC-AGI v2 / Humanity's Last Exam(HLE)** — 两个极难基准;前者考抽象推理,后者是 2500 道各领域专家难题,用来展示"reasoning"与"deep knowledge extraction"两类能力。
- **Reasoning strategies(推理策略)** — 用代码(而非仅靠 prompt)实现的推理/校验/编排方法,是性能大跳变的主要来源。
- **GEPA(自动 prompt 优化,转录中作 "jepa")** — 当下很流行、大家都在复现的自动提示优化范式;能拿到部分收益但远非全部。
- **Context stuffing / context engineering(上下文填充/工程)** — 往上下文里塞入更多信息或示例以提升表现;Poetiq 让元系统自行决定是否这么做。

## 🔖 高价值金句时间戳
- `[02:07]` "the second you're in fine-tuning land... I just lit it on fire because... the next version of the frontier model comes out, and I'll never catch up." — 微调陷阱的最凝练表述:钱和时间押在会被下个模型清零的资产上。
- `[02:39]` "we don't view the... frontier models as competitors. They're... the ones that were using the stilts... to stand on top of." — 心智重构:前沿模型是地基不是对手。
- `[03:15]` "We have built a system that can automatically generate systems for your particular problem that will always outperform the underlying language models." — 一句话产品定位。
- `[08:40]` "These harnesses, they are code, prompts, data... in principle, you can build by hand. Or with like cloud code... But in practice, it takes a lot of work... to make these work well." — harness 可手搓但难搓好,价值在自动化与 insight。
- `[13:34]` "when we added on the... reasoning strategies we went from five percent to ninety five percent" — 代码化推理策略带来的量级跃升,不是更好 prompt 能替代的。
- `[16:01]` "then you're just totally vaccinated against the bitter lesson" — 好架构 = 对模型迭代免疫,越新越强。
- `[18:28]` "you should just try things. And like every day, do something with AI." — 给 AI 时代工程师/创始人的行动纲领。
