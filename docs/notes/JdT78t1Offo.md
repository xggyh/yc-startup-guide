# Anthropic 联创谈 Claude Code、GPT-3 与 AI 系统设计 / Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design

📄 **[点此查看全文转录 / Full transcript »](../transcripts/JdT78t1Offo.md)**

> **来源**: [Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design](https://www.youtube.com/watch?v=JdT78t1Offo) · Y Combinator · 2025-08-19 · 时长 35:57
> **讲者**: 嘉宾 Tom Brown(Anthropic 联合创始人,曾在 OpenAI 主导 GPT-3 基础设施)= SPEAKER_04;主持为 The Lightcone / YC 团队(Garry Tan、Jared Friedman、Diana Hu、Harj Taggar 等)= SPEAKER_00/01/02/03
> **一句话定位**: 一位从"线性代数拿 B-"自学转型的工程师,如何一路做到共建 Anthropic —— 讲透了规模定律、"把 Claude 当用户"造 Claude Code 的产品直觉,以及 AI Agent 创业者可切入的巨大空白市场。

## 🎯 TL;DR(中文核心要点)
- **做"狼"不做"狗"**:大厂只教你如何在大厂工作;真正的成长来自"没人给你派活、公司默认会死"的创业环境里被逼着自己找食吃。
- **规模定律是核心信念**:12 个数量级的直线关系("花钱就能可靠换来更多智能")说服 Tom 把全部精力 all-in scaling;Anthropic 的口号就是"做那个能 work 的蠢办法"。
- **使命驱动的招聘=可扩展的文化护城河**:前 100 人全是为使命而来,所以 2000 人规模了政治仍未渗入 —— 有人跑偏,别人会主动举手。
- **犹豫的代价**:早期不确定该不该发布 Claude,于是拖太久没建 serving 基础设施,等 ChatGPT 引爆时反应不及,这是 Tom 亲口承认的教训。
- **编码 PMF 是刻意 + 意外的叠加**:主动投入让模型擅长代码,但 3.5 Sonnet 有多大反响、3.7 解锁 agentic coding 都超出预期 —— 快速上线、边发边学。
- **不刷榜**:别的大厂有专门团队把 benchmark 分数刷高,Anthropic 没有,反而带来"实测体验远好于榜单预测"的口碑。
- **把 Claude 当"用户"**:Claude Code 成功的最大秘诀不是技术壁垒,而是"对 Claude 更有同理心" —— 给它对的工具、对的上下文。这条护城河创业者一样能建。
- **巨大空白 + 硬约束**:让模型胜任"编码之外的绝大多数商业工作"是超大蓝海;同时算力以每年约 3 倍增长,电力(尤其美国本土)是最大瓶颈。

## 🧭 适合谁 / 什么时候看
- 在 Claude / GPT 等 API 之上做 AI Agent、且担心"被大厂原生功能碾压"的创始人。
- 想理解"为什么 Anthropic 编码体验好、MCP 能跑通"背后产品哲学的工程师。
- 正在纠结"要不要 all-in AI / 离开稳定路径"的技术人,想听一个自学转型的真实样本。

## 📝 分段精读

### 1. 开场:七个联创 vs 手握十亿的 OpenAI,以及"狼"的心态 / From Failure to Success `[00:00–02:24]`
**要点(中文)**: 起步时 Anthropic 完全不被看好 —— OpenAI 有十亿美金和全部明星光环,他们只有 7 个联创在 COVID 里摸索。Tom 回溯 21 岁从 MIT 毕业进入创业圈的最大收获:创业让你从"等着被喂食的狗"变成"必须自己捕猎的狼"。这种"公司默认会死、没人给你派活"的心态转变,是他做更大事情最有价值的底层能力。
> 🗣️ "I think it was more like wolves and we have to like hunt our real life food otherwise like where our kids are gonna starve or something like that." —— Tom Brown (SPEAKER_04)
> 译:感觉更像狼群 —— 我们得自己去捕猎真实的食物,否则孩子们就要饿肚子了。
> 🗣️ "big tech just teaches you to work at a big tech company whereas it's much more fun to be a wolf" —— 主持人 (SPEAKER_01)
> 译:大厂只会教你如何在大厂里工作,而当一只狼要有意思得多。

### 2. 创业试错路:Linked Language 到 Grouper,被 Tinder 击败 / Early Startup Years `[02:24–06:05]`
**要点(中文)**: Tom 早年当过多家 YC 创业公司的首位工程师,自认"编程很烂"却坚持要当"狼"。Grouper(线下相亲局)想解决"社恐不敢主动搭讪"的问题,但 Tinder 用"双向表态才配对、无被拒风险"更漂亮地解决了同一个问题。关键教训:同一使命,谁给出更好的解法谁就赢 —— 竞品不是模仿你,而是把你要解决的问题解得更好。这段经历也让他结识了后来把他引荐进 OpenAI 的 Greg Brockman。
> 🗣️ "good work tinder good work all the swipers i think that that that solved the like mission that we were trying to solve better than we solved it" —— Tom Brown (SPEAKER_04)
> 译:干得好 Tinder,干得好所有划屏的人 —— 我们想解决的那个使命,他们比我们解得更好。

### 3. 下注 AI:六个月自学 + "扫地也行"进 OpenAI / Making the Leap & Self-Study `[06:05–12:08]`
**要点(中文)**: 2015 年 OpenAI 刚成立,Tom 线性代数只拿了 B-,朋友都说"这事太怪、你未必行"。他先接了 Twitch 的三个月合同攒够半年生活费,再"闭关自学"(Coursera 机器学习、Kaggle、线代与统计教材、租 GPU 上机)。真正的破局点是主动出击:OpenAI 一宣布他就给 Greg 发消息,姿态放到极低"扫地都行"。Greg 的回复点破了他的独特定位 —— 同时懂机器学习和分布式系统的人极稀缺。他先靠做 StarCraft 训练环境把脚踏进门,头九个月根本没碰 ML。
> 🗣️ "if you guys need help I'm like happy to mop floors if if you guys need I want to help out however" —— Tom Brown (SPEAKER_04)
> 译:如果你们需要人手,我扫地都行 —— 只要能帮上忙,怎么都行。
> 🗣️ "there's a paucity of people who know both machine learning and distributed systems so like yes you should do that" —— Greg Brockman(经 Tom 转述,SPEAKER_04)
> 译:同时懂机器学习又懂分布式系统的人非常稀缺,所以是的,你该来做这个。

### 4. 规模定律:12 个数量级的直线 + "做能 work 的蠢办法" / Scaling Laws `[12:08–15:44]`
**要点(中文)**: GPT-3 的突破本质就是"把算力堆上去"。Tom 说服自己 all-in scaling 的,是那条跨越 12 个数量级仍笔直的规模定律曲线("花钱就能可靠地换来更多智能"),叠加 Danny Hernandez 关于算法效率随时间变便宜的论文 —— 两者相乘意味着未来几年智能会暴涨。当时很多研究者反感这条路,觉得"堆 GPU 不优雅、纯粹烧钱",而这恰恰印证了 Anthropic 的口号:做那个"看起来很蠢、但确实 work"的事。
> 🗣️ "like seeing that line of reliably you get more intelligence if you spend money was the main thing" —— Tom Brown (SPEAKER_04)
> 译:看到那条"只要花钱就能可靠地得到更多智能"的直线,是最关键的一击。
> 🗣️ "like anthropic's slogan I think is like do the stupid thing that works" —— Tom Brown (SPEAKER_04)
> 译:Anthropic 的口号大概就是:做那个"看起来蠢但真的有效"的事。

### 5. Anthropic 诞生:使命驱动的团队文化 / The Anthropic Spinoff `[15:44–18:23]`
**要点(中文)**: 从 OpenAI 拆分出来的核心是 scaling 组和 safety 组 —— 都把规模定律当真,都认定"人类迟早要把控制权交给变革性 AI,而这次交接必须做好"。7 个联创起步,几个月内约 25 位 OpenAI 老同事加入,团队已经知道怎么协作。Tom 认为最关键的护城河是招聘:最初 100 人全是为使命而来,他们本可以去别处拿更高薪酬和名望。正因如此,涨到 2000 人时政治仍未渗入 —— 一旦有人偏离使命,别人会主动举手。
> 🗣️ "all of the initial people who joined were there for the mission too they all could have worked somewhere else for more prestige more more more money" —— Tom Brown (SPEAKER_04)
> 译:最早加入的所有人都是为使命而来,他们本可以去别处拿更多名望、更多钱。
> 🗣️ "the first hundred people all were just there for the mission so like if something starts to go wrong they'll like raise their hand" —— Tom Brown (SPEAKER_04)
> 译:前一百人全是为使命而来,所以一旦有什么开始跑偏,他们会主动举手示警。

### 6. 早期 Claude 与 ChatGPT 警钟:犹豫太久没建基础设施 / Early Claude & the ChatGPT Wake-Up `[18:23–21:00]`
**要点(中文)**: 第一年 Tom 的两大任务就是搭训练基础设施、拿到训练算力。ChatGPT 之前约 9 个月,他们已有一个 Slackbot 版的 Claude 1(YC 里试用过),但当时既不确定发布产品是否对世界有益,也没想清楚"影响力理论"。结果拖太久没建 serving 基础设施 —— 等 ChatGPT 2022 秋引爆时,他们即便想发也发不出来。Tom 直言这是他的教训:在"该不该做"上犹豫,拖累了"能不能做"的准备。真正开始 work 要到 Claude 3.5 和编码场景。
> 🗣️ "because we weren't sure whether or not we wanted to we like hesitated for too long on building that infrastructure which I think is learning for for me" —— Tom Brown (SPEAKER_04)
> 译:因为我们不确定到底要不要做,就在建那套基础设施上犹豫了太久 —— 这对我是个教训。

### 7. 编码 PMF 与"不刷榜"哲学 / Coding PMF & Why Benchmarks Don't Tell the Whole Story `[21:00–26:07]`
**要点(中文)**: 2023 年 startup 默认用 OpenAI;2024 年 Claude 3.5 Sonnet 尤其在编码上把 YC batch 里的份额从个位数拉到 20–30%,如今编码场景更是 80–90%。这既是刻意(团队里的个人早在 3.5 之前就想做好编码,看到 PMF 信号后加倍投入),也有意外(3.5 反响之大、3.7 解锁 agentic coding 都超预期)。口碑好于榜单的"X 因素"是:别家大厂有专门团队刷 benchmark,Anthropic 没有 —— 他们只盯内部不公开的 benchmark,并大量 dogfooding 加速自家工程师。
> 🗣️ "I think that all the other big Labs I think have teams where they like their whole job with the team is to like make the benchmarks scores good and we don't have such a team" —— Tom Brown (SPEAKER_04)
> 译:其他大厂都有专门团队,整份工作就是把 benchmark 分数刷高,而我们没有这样的团队。
> 🗣️ "I think we invested more in trying to make the model really good at code because we wanted the model to be good at code" —— Tom Brown (SPEAKER_04)
> 译:我们在"让模型真正擅长写代码"上投入更多,就是因为我们想让模型擅长代码。

### 8. 把 Claude 当"用户":Claude Code 的秘诀与给 API 创业者的建议 / Building for the AI Agent `[26:07–30:59]`
**要点(中文)**: Claude Code 起初只是内部工程师 Boris 给自己和同事攒的工具。Anthropic 原本全押 API("外面那么多好点子,凭什么我们最懂该造什么产品"),却意外做出了市面上体验最好的 agentic 工具。Tom 的理论:秘诀不是技术壁垒,而是心智转变 —— 把 Claude 本身当成用户,给它对的工具、对的上下文。这也解释了为什么他们的 MCP 工具调用标准能跑通。对在 API 上创业的人,他的信号很明确:Claude Code 没有专属技术优势,"一家 startup 完全能做同样的事";最大的空白是让模型胜任"编码之外的绝大多数商业工作"。
> 🗣️ "really the like users are the developers but also I think the users is Claude it's like give Claude the right tools that Claude can actually do that effectively help Claude get the right contexts to work effectively" —— Tom Brown (SPEAKER_04)
> 译:用户当然是开发者,但我认为用户也是 Claude —— 给 Claude 对的工具让它真能高效干活,帮 Claude 拿到对的上下文来高效工作。
> 🗣️ "it's not super clear to me what the big advantage was for us for Claude code besides more empathy for Claude" —— Tom Brown (SPEAKER_04)
> 译:除了对 Claude 更有同理心之外,我其实说不清 Claude Code 到底有什么大优势。
> 🗣️ "finding ways to coach Claude or uh approach whatever model to like do useful tasks for businesses seems like there's just like a huge huge space there" —— Tom Brown (SPEAKER_04)
> 译:想办法"教练"Claude(或任何模型)去完成对企业有用的任务 —— 这里有一片巨大巨大的空间。

### 9. 史上最大基建、多芯片策略与给年轻人的建议 / The Largest Buildout, Multi-Chip & Advice `[30:59–35:57]`
**要点(中文)**: 人类正在进行史上最大规模的基础设施建设 —— 今年若维持约每年 3 倍的 AGI 算力投入增长,将超过阿波罗计划与曼哈顿计划之和。最大瓶颈是电力(尤其美国本土),推动美国多批数据中心许可是 Anthropic 的核心政策目标。芯片上他们同时用 GPU / TPU / Trainium:代价是性能工程团队被摊薄,好处是能吸收总量更大的产能、并为训练 / 推理匹配最合适的芯片。给年轻人的最后一句:多冒险,去做"朋友会为你兴奋、更理想的自己会为你骄傲"的事 —— 更看重内在动机,别追学位或 FANG 这类外部标签。
> 🗣️ "humanity is on track for like the largest infrastructure build out of all time ... roughly 3x per year increase in spending on AGI compute which is just bonkers" —— Tom Brown (SPEAKER_04)
> 译:人类正走向史上最大规模的基础设施建设……AGI 算力投入大约每年增长 3 倍,简直离谱。
> 🗣️ "Taking more risks I think is wise, and then also trying to work on stuff where your friends would be really excited and impressed" —— Tom Brown (SPEAKER_04)
> 译:多冒些险是明智的,并且去做那些会让你朋友真心兴奋和佩服的事。
> 🗣️ "More intrinsic, less extrinsic. Don't chase these other credentials and getting the degree or working at Fang. Those are just irrelevant as of today" —— 主持人 (SPEAKER_01)
> 译:更看重内在、少看重外在。别去追那些证书、学位或进 FANG —— 到今天,这些都无关紧要了。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把"模型/Agent"列为一等用户**:除了终端用户,专门为 Claude/模型设计工具接口、上下文投喂与错误反馈,像做 UX 一样做"Agent 体验"。
- [ ] **攻编码之外的商业工作流**:选一类"懂代码、会用工具但缺业务上下文的聪明人能做"的重复工作(财务、运营、合规、客服等),把上下文与工具喂给 Agent,这是 Tom 点名的超大空白。
- [ ] **不把技术壁垒当唯一护城河**:承认大厂能复刻你的功能;用"对特定用户/场景的深度同理心 + 更快迭代"建立优势,这条路 startup 同样能走通。
- [ ] **别为"要不要做"而拖延基础设施**:一旦方向可能成立,提前把 serving / infra 备好,避免像早期 Anthropic 那样在爆发点反应不及。
- [ ] **建自己的私有评测 + 疯狂 dogfooding**:别刷公开榜,盯住真实任务的内部 eval,并用自家产品加速自家团队,以质性体验取胜。
- [ ] **用使命而非薪酬招前 20 人**:早期团队为使命而来才能在规模化后抵御政治与漂移,把"会主动举手"写进招聘标准。

## 🔑 关键术语 / 概念
- **Scaling Laws(规模定律)** — 模型能力随算力/数据/参数按幂律可预测提升;Tom 眼中跨 12 个数量级的直线是 all-in 的决定性证据。
- **"Do the stupid thing that works"** — Anthropic 的信条:哪怕方法"不优雅、像蛮力堆算力",只要 work 就做。
- **Claude as the user(把 Claude 当用户)** — 产品设计视角:模型/Agent 本身是需要被赋能的利益相关方,给它对的工具与上下文。
- **MCP(Model Context Protocol)** — Anthropic 主导、真正跑通并被广泛采用的工具调用标准。
- **Agentic coding** — 模型自主地多步骤完成编码任务(如 Claude 3.7 解锁),Claude Code 是其代表产品。
- **Dogfooding** — 用自家模型加速自家工程师,作为真实、质性的评测与改进闭环。
- **Trainium** — 亚马逊自研 AI 加速芯片;Anthropic 采取 GPU/TPU/Trainium 多芯片并用策略。

## 🔖 高价值金句时间戳
- `[01:12]` "I think it was more like wolves and we have to like hunt our real life food" — 创业心态的本质:从等喂食的狗变成自己捕猎的狼。
- `[08:30]` "good work tinder ... solved the like mission that we were trying to solve better than we solved it" — 竞品赢在把同一问题解得更好,不是模仿你。
- `[15:28]` "anthropic's slogan I think is like do the stupid thing that works" — 别为"不优雅"而放弃有效解法。
- `[16:05]` "the first hundred people all were just there for the mission ... they'll like raise their hand" — 使命驱动的早期招聘=可扩展文化的护城河。
- `[20:10]` "we like hesitated for too long on building that infrastructure which I think is learning for for me" — 在"要不要做"上犹豫,会让你在爆发点措手不及。
- `[26:23]` "the users is Claude ... give Claude the right tools ... help Claude get the right contexts" — 把 Agent 当用户,是 Claude Code 成功的核心心智。
- `[30:00]` "finding ways to coach Claude ... do useful tasks for businesses ... huge huge space there" — 编码之外的商业任务是 AI Agent 创业的最大蓝海。
