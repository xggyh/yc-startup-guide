# 创业前该问自己的问题:在 AGI 逼近时如何做 AI 创业 / Ask These Questions Before Starting An AI Startup

> **来源**: [Ask These Questions Before Starting An AI Startup](https://www.youtube.com/watch?v=DJjZzzPANBY) · Y Combinator · 2025-10-07 · 时长 40:36
> **讲者**: Jordan Fisher(Standard AI 联合创始人兼前 CEO,现于 Anthropic 领导一支 AI 对齐研究团队;YC 校友)。演讲录于 2025-06-17 的 AI Startup School。后半为现场观众问答。
> **一句话定位**: 在"AGI 可能两三年内到来"的假设下,用一连串尖锐问题(而非答案)逼你重估产品、团队、护城河与信任——帮 AI Agent 创始人避免做出"六个月后就成为四舍五入误差"的东西。

## 🎯 TL;DR(中文核心要点)
- **按"两年后"而非"六个月后"来规划**:主流建议是照下一代模型的能力做产品;Jordan 加码——按"极可能几年内出现 AGI"来定战略、招聘、GTM,但别真写死一份两年计划(不确定性极大)。
- **AI 不只武装卖方,也武装买方**:别指望"大公司采购慢"给你多年窗口。企业内部团队会用下一代 LLM 做采购决策、自己让 Claude Code 造内部软件,SaaS 的护城河可能被两头夹击。
- **"信任"是贯穿一切的主线**:按需生成代码/UI、个人 agent 与工作 agent 协作、把数据库层交给模型——每一步能不能落地,取决于你能否信任模型、信任构建 agent 的那家公司(也就是信任你)。
- **半自动团队会瓦解传统信任机制**:公司之所以可信,靠的是"人多口杂"——有人会举报、会辞职、会带人走。团队越小越自动化,单个坏人越容易一手遮天;这正是大企业不信任小创业公司的原因之一,未来普通用户也会这么想。
- **护城河在"AGI 也难替代"处**:通用 LLM 抹平了自定义数据的优势,但锁在企业内部、从未外泄的隐性知识(材料科学、TSMC/ASML 式的先进制程)前沿模型学不会;基础设施、能源、制造、芯片这类"硬问题"两三年后依然硬。
- **警惕"智能天花板"带来的更快商品化**:某些任务(写诗、生成一段 git diff、生成视频)一旦饱和,你就无法靠"换下一代模型"继续领先,商品化压力会更猛——按垂直领域逐一判断。
- **别用观点代替验证**:"AI 原生新产品 vs 老产品加持分发"、"团队会不会更小"这类问题没有普适答案,往往因垂直领域而异——去找出能证伪你假设的因果机制,而不是拍脑袋站队。
- **这可能是你"改变世界"的最后一班车**:如果只想在 6–18 个月里冲 ARR、快速套现,你不需要长期护城河;但若想穿越这场转型,就把"防御性"和"社会真正需要什么"想得更深——build something people **need**。

## 🧭 适合谁 / 什么时候看
- 正在(或准备)做 AI/Agent 创业,想在"下一代模型 + AGH 逼近"的假设下重新校准战略、团队与护城河的创始人。
- 纠结"选自己热爱的方向、还是选防御性最强方向"的人:本片给出明确排序——防御性 > 热爱。
- 关注 Agent 信任/安全/对齐如何变成**产品与商业问题**(而非纯研究问题)的工程型创始人。
- 想要一套"提好问题"的思维框架、而非现成答案的人;不适合想要"照着抄的创业清单"的人。

## 📝 分段精读

### 1. 为什么他比以往更困惑:创始人天生适合回答"一切都在变" / Why He's More Confused Than Ever `[00:00–03:42]`
**要点(中文)**: 一辈子靠"看得懂未来五到十年"来提前布局的人,现在只能看清"三周以内"。但困惑是好事——受过科学训练的人最该关注的正是"我不懂"的瞬间。创业存在一个悖论:人人都说"专注是一切",可创始人的工作偏偏是"什么都要管"(招聘、融资、产品、GTM,还随时有人要离职)。正是这种"被迫回答一切问题"的处境,让创始人天然适合面对社会级的大问题:AI 会怎样、我们该做什么。提好问题,是经营创业、研究团队乃至人生的关键。
> 🗣️ "I can't see five years into the future. I can see, like, three weeks or less." —— Jordan Fisher
> 译:我看不到五年之后了,我只能看到大约三周、甚至更短。
> 🗣️ "Focus is everything... but the other truth of running a startup is you have to focus on everything." —— Jordan Fisher
> 译:专注就是一切……但经营创业公司的另一条真理是,你必须专注于每一件事。

### 2. 按"AGI 两三年内到来"规划,别忘了买方也会被 AI 武装 / Plan for AGI in 2–3 Years; the Buy-Side Gets Armed Too `[03:42–06:06]`
**要点(中文)**: 常见最佳实践是"照下一代模型能力做产品、别只为今天的能力规划"。Jordan 加码:应按"极可能几年内出现 AGI"来做规划——但因不确定性巨大,别真写死两年计划,而要让 AGI 这个前提影响你对招聘、营销、GTM 的思考。他还纠正一个流行的乐观论:"大公司采购慢,所以 AI 冲击会来得慢"是短视的——企业买方自己也会被下一代 LLM 武装,用 AI 做采购决策、加速采纳,甚至直接扔两个人给 Claude Code 造专属内部软件,不再向 SaaS 采购。AI 抬高的是"所有的船",在位者同样受益。
> 🗣️ "You should be planning two years in advance because it's extremely likely that we will have AGI in the next few years." —— Jordan Fisher
> 译:你应该提前两年来规划,因为我们极有可能在未来几年内迎来 AGI。
> 🗣️ "It's not just the startups, the incumbents benefit from AI, too." —— Jordan Fisher
> 译:受益于 AI 的不只是创业公司,在位巨头同样受益。

### 3. 软件会被彻底商品化吗?按需代码、生成式 UI 与信任 / Will Software Commoditize? On-Demand Code, UI & Trust `[06:06–10:20]`
**要点(中文)**: 一个开放的大问题:两三年后还有没有必要做 SaaS?一种结局是软件彻底商品化——企业一条 prompt 就让下一代 Claude Code 内建全部软件,消费者也不再"下载 App",而是按需即时生成。另一种相反的结局是:自动化把"质量下限"拉到人人可及,于是竞争转向"质量上限"——你能否做出明天的卓越 App?答案很可能因垂直领域而异。他还抛出更激进的"按需代码":当用户当场需要 App 不支持的功能时,实时为这个用户生成后端/数据库层的代码——但这要求你**信任**模型能把事做对,而今天的 AI 还不够可信。关键方法论:别停在观点上,去找能验证假设的因果机制。
> 🗣️ "But if you can do code on demand, why not do it on demand?" —— Jordan Fisher
> 译:可如果你能按需写代码,为什么不就地按需去写呢?
> 🗣️ "So I think trust is going to be a big theme over how these different questions play out." —— Jordan Fisher
> 译:所以我认为,信任将是决定这些问题如何演变的一大主线。
> 🗣️ "Don't just have an opinion. Like, figure out the causal mechanisms that allow you to validate your hypothesis." —— Jordan Fisher
> 译:别只有一个观点。要去找出那些能让你验证自己假设的因果机制。

### 4. AI 原生团队、安全模型与"一个 agent 服务你的全部" / AI-Native Teams, Security & the Unified Agent `[10:20–13:00]`
**要点(中文)**: 团队会不会更小?默认假设是会。但类比产品的"改造 vs 重建",真正的问题是:从零构建的 AI 原生团队,会不会跑出与"缩编求效率的大公司"不同的运作范式?而且"AI 原生"的定义每 6–12–18 个月都在变,今天的 AI 原生公司到 12 个月后可能已经过时。安全模型也随之改变:要让 LLM 一路下探到数据库层为用户按需做事,就必须信任你的控制机制和模型能力。Agent 的另一难题是"围墙花园":用户想要**一个** agent 打通一切,而个人 agent 与工作 agent 协作会牵出信息隔离难题——如何既让它们协作,又不让雇主看到你的私人信息。
> 🗣️ "As a user, you want one agent for all of your things, right?" —— Jordan Fisher
> 译:作为用户,你想要一个 agent 打理你所有的事,对吧?
> 🗣️ "Are AI native teams that were built from scratch... going to have some advantage over large companies that are downsizing?" —— Jordan Fisher
> 译:那些从零就按 AI 原生方式搭建的团队,会不会相对那些靠 AI 缩编增效的大公司拥有某种优势?

### 5. 半自动团队的信任崩塌、AI 审计与"有牙齿的绑定承诺" / Trust in Semi-Automated Orgs, AI Audits & Binding Guardrails `[13:00–17:30]`
**要点(中文)**: 即便模型"意图对齐",它仍会被公司拿去为用户造 agent——于是问题变成:你能信任那家造 agent 的公司吗?如果它靠广告盈利,你搜鞋子时它会不会偷偷把你往某个方向推?更深一层:我们今天信任公司,靠的是"人的多样性"——CEO 想干坏事,总有人举报、辞职、带人走;没有员工支持,公司就没有产品。可在半自动的世界里,单个人就能改变整个产品的走向,且除他自己外无人知情,坏人作恶的门槛骤降。解决思路之一是 **AI 审计**:AI 审计员相比人类的优势是"可无偏见、可无记忆"——审计结束若未发现违规,AI 连同笔记一起自我删除,不会像人类那样带走 IP 或敏感信息。更进一步,把公司的公开使命从"口头承诺"升级为"可绑定、可持续审计的承诺"(让中立 AI 审查每一条 Slack 消息),这才"有牙齿"。这些今天还做不到,但很快可能实现。
> 🗣️ "A single person could make a decision that changes the entire impact of a product. And there's no single person that might be aware of that, except themselves." —— Jordan Fisher
> 译:单独一个人就能做出改变整个产品走向的决定,而除了他自己,可能没有任何人会察觉。
> 🗣️ "If after your audit you've decided that we didn't do anything wrong... then the AI deletes itself." —— Jordan Fisher
> 译:如果审计结束后你判定我们没有做错任何事……那么这个 AI 就把自己删除。
> 🗣️ "Are you actually willing to make that a binding statement?" —— Jordan Fisher
> 译:你是否真的愿意把它变成一个具有约束力的承诺?

### 6. 对齐的经济压力:长时程 Agent 逼着你解决对齐 / Alignment's Economic Pressure & Long-Horizon Agents `[17:30–18:40]`
**要点(中文)**: 对齐不只是"人类控制 AI"的安全议题,更是一个未来 12 个月的高压商业问题:要让 agent 在经济上真正可用,必须解决其中一部分对齐。用 Claude Code 时它一次只干五分钟、你会逐段 review,风险可控;可一旦你要让 LLM 连续工作一天、一周才介入,就必须有相当把握它不会彻底跑偏。Jordan 对此反而乐观:正是这种"长时程 agent 需要对齐"的经济压力,会以好的方式推动对齐进步——只是"要解决多少、解决哪些方面"仍是开放问题。
> 🗣️ "If you're going to trust an LLM to work for a day at a time or a week at a time before you intervene, you better have some degree of certainty that it's not going completely off the rails." —— Jordan Fisher
> 译:如果你要信任一个 LLM 一次连续工作一天、一周才去干预,那你最好有相当的把握,它不会彻底失控脱轨。

### 7. 护城河:自定义数据、隐性知识、硬问题、算力与"智能天花板" / Moats: Data, Tacit Knowledge, Hard Problems, Capacity & Ceilings `[18:40–23:40]`
**要点(中文)**: 几年前"自定义数据 = 壁垒"是事实;但通用 LLM 变强后,直接用通用模型往往胜过在自有数据上微调。开放问题是:是否存在通用 AI 不擅长的行业?比如材料科学、或 TSMC/ASML 这类把巨额投注与**隐性知识**牢牢锁在内部、从不外泄的公司——前沿 LLM 并不知道如何造出尖端半导体晶圆厂,这正是可防御的位置。产品层面他的口诀是"先做到极致,再做规模化(make it great, then make it scale)";在 GPU 产能跟不上 100x 需求的一两年里,上下文管理、模型路由等技术能构成暂时的技术护城河,但会随模型变强而消失。真正的问题是:两三年后如果我一句 prompt 就能让 Claude 7 / GPT 7 复刻你的创业,你的持久优势是什么?他自己的答案是"专挑硬问题"——基础设施、能源、制造、芯片,这些即便有机器人也会滞后。最后一个隐患是"智能天花板":某些任务一旦饱和,就无法靠换下一代模型继续领先,商品化会来得更快、更猛。
> 🗣️ "Frontier LLMs do not know how to build a cutting edge semiconductor fab. That's an important fact, actually." —— Jordan Fisher
> 译:前沿 LLM 并不知道如何建造一座尖端的半导体晶圆厂——这其实是个很重要的事实。
> 🗣️ "In two years or three years, if I can just prompt Claude 7 or GPT 7 to just replicate your startup, what's your advantage going to be?" —— Jordan Fisher
> 译:两三年后,如果我只要给 Claude 7 或 GPT 7 一句 prompt 就能复刻你的创业公司,你的优势还剩什么?
> 🗣️ "If there is a ceiling, then the commoditization for that task is going to hit much sooner." —— Jordan Fisher
> 译:如果某项任务存在(能力)天花板,那么它被商品化的时刻就会来得早得多。

### 8. 中立性、"改变世界还是只想赚钱"、做社会真正需要的东西 / Neutrality, Change the World vs. Make Money, Build What People Need `[23:40–29:00]`
**要点(中文)**: 若全社会都依赖少数几家公司的模型,那这几家就成了"什么能被造出来"的仲裁者(想想 refusal 拒答)。类比电网中立——若 GE 规定"只有插我家烤箱才准用我的电网",那是灾难;网络的这场中立之战我们打过也输过,那 AI 呢?是否需要"AI 中立 / token 中立"?收尾他讲了最触动他的一点:硅谷创始人过去真心想"改变世界"(哪怕做的是撸猫 App)。如今普通人也已切身意识到"我们正把第二种智能带入世界"的历史级重量;但当他把人一路讲到这里,对方常问"那怎么靠这个赚钱?"——他会为此感到失望(尽管完全理解那份恐惧)。他的呼吁:这可能是你"做出改变、改变世界"的最后一班车,也可能是你造的最后一款产品;YC 的口号"build something people want"要往深处理解——别只想人们会消费什么,而要想社会需要什么;做对了,自然很多人会想要。
> 🗣️ "Do we need AI neutrality? Token neutrality? I don't know what we call it." —— Jordan Fisher
> 译:我们是否需要"AI 中立"?"token 中立"?我不知道该怎么称呼它。
> 🗣️ "This might be the last product you build. This might be the last company you build." —— Jordan Fisher
> 译:这可能是你造的最后一款产品,这可能是你创办的最后一家公司。
> 🗣️ "When we say build something people want, don't just think about what people will consume. Like, what does society need?" —— Jordan Fisher
> 译:当我们说"做人们想要的东西"时,别只想人们会消费什么——想想社会需要什么。

### 9. 观众问答精选 / Audience Q&A `[29:55–40:36]`
**要点(中文)**: 一连串高信号回答:
- **信息来源(SPEAKER_03 问)**:诚实的答案是 Twitter,但要极其严格地策展——好观点就 follow,蠢观点就 unfollow。别只挑你认同的人,要为"多样性"最大化(RL 里的 explore vs exploit);先大量探索,再去"利用"(比如创业)。
- **热爱 vs 防御性(SPEAKER_06 问)**:一旦进入每周 100 小时、连续六个月,再热爱的方向你都会厌恶;支撑你走下去的是影响力、对公司与合伙人的承诺,而非对领域的热爱。防御性才是最关键的问题之一——除非你只想在 6–18 个月冲 ARR 快速套现。
- **钱会更值钱还是更不值钱(SPEAKER_00 问)**:取决于政策(UBI?"通用基本算力"?)。AGI 到来后不再需要"劳动力的认可"——资本自我繁殖(capital begets capital),财富可能失控集中。
- **用户级对齐/谄媚(SPEAKER_07 问)**:用户"不知道自己想要什么",但有价值观。同一件事在不同层级提问会得到不同答案:让用户二选一具体回复,很多人会选谄媚那条;但若问他们要"绝不拍马屁"还是"整天吹捧你"的原则,几乎人人选前者——所以要设计"问对问题"的方式,别被人利用提问方式操纵。
- **与主流的分歧(SPEAKER_01 问)**:这个号称前瞻的行业其实存在极强的从众(groupthink);多数 VC 自以为在投 AI,其实已经落后两年——真正该问的是"今天投什么,才能在两年后依然稳固"。
- **区块链能否助力信任(SPEAKER_04 问)**:自称重度怀疑者,但承认在"需要信任"的世界里,这类思路(AI 互审、去中心化中介 UBI/基本算力)值得考虑。
- **Agent 对 Agent 协议(SPEAKER_05 问)**:以"帮你排会议的私人助理"为例——看似 trivial,实则充满博弈论:太爽快地暴露空档,等于告诉对方你不忙、或这场会对你很重要;把会排到两三周后则是在拉权力位。好助理靠隐性、语义化的默契处理这些,难点正在于此。
> 🗣️ "You really need to be the master of your information diet." —— Jordan Fisher
> 译:你必须成为自己"信息食谱"的主人。
> 🗣️ "Once you're six months into 100-hour work weeks, I don't care how passionate you are about an idea, you're going to hate it." —— Jordan Fisher
> 译:一旦你进入每周 100 小时、连续六个月,不管你对这个点子多有热情,你都会厌恶它。
> 🗣️ "Once AGI arrives, you don't need labor buy-in anymore... capital begets capital in that world, and that can easily spiral out of control." —— Jordan Fisher
> 译:AGI 一旦到来,你就不再需要劳动力的认可……在那个世界里资本自我繁殖,而这很容易失控。

## 🚀 给 AI Agent 创始人的行动项
- [ ] 写一份"两年后假设清单":把你产品/团队/GTM 里,哪些环节会因"AGI 逼近 + 下一代模型"而改变逐条列出,每季度重估一次——但不锁死成僵化的两年计划。
- [ ] 对你的核心押注做一次"商品化压测":问"两三年后一句 prompt 能否让 Claude 7 复刻我?",若能,现在就去补护城河(隐性知识、硬问题、分发)。
- [ ] 为你所在垂直领域判断是否存在"智能天花板":会饱和的任务(生成类)别把它当长期壁垒;不会饱和的任务才值得押"跟随下一代模型"的策略。
- [ ] 把"信任"做成产品特性而非事后补丁:为你的 agent 设计可审计、可留痕、可回滚的控制层,并想清楚"个人数据 / 工作数据"如何隔离又协作。
- [ ] 把"是否操作在用户一方"写进产品原则:明确 agent 的激励是否与用户对齐(尤其广告/佣金模式),并考虑用"可绑定的公开承诺 + 第三方(AI)审计"建立可信度。
- [ ] 用"问对层级的问题"来采集用户真实价值观:别用会诱导谄媚的二选一,去问原则级问题;把结果沉淀为产品的对齐/风格准则。
- [ ] 主动策展你的信息食谱(如严格管理的 Twitter 关注),为多样性而非认同感最大化;创业前先"探索"够,再"利用"。

## 🔑 关键术语 / 概念
- **Buy-side gets armed(买方被武装)** — 不只是创业公司用 AI 造产品,企业采购方也会被下一代 LLM 武装,自己做决策、造内部软件,从而压缩 SaaS 空间。
- **On-demand code / generative UI(按需代码 / 生成式 UI)** — 当用户当场需要现有 App 不支持的功能时,由 agent 实时生成后端乃至数据库层代码;能否落地取决于对模型的信任。
- **Semi-automated team(半自动团队)** — 高度 AI 化、人数极少的团队;传统"靠人多制衡坏决策"的信任机制在此失效,单人即可决定产品走向。
- **AI-powered auditing(AI 审计)** — 让可无偏见、可无记忆的 AI 审查公司是否遵守其使命;审计后自我删除,避免人类审计员带走 IP 或敏感信息。
- **Tacit knowledge moat(隐性知识护城河)** — 锁在企业内部、从未外泄的经验(材料科学、TSMC/ASML 的先进制程),前沿 LLM 学不到,构成可防御位置。
- **Intelligence ceiling(智能天花板)** — 某任务的能力上限;一旦饱和,换下一代模型也无法继续领先,该任务的商品化会更早、更猛。
- **Make it great, then make it scale(先做到极致,再做规模化)** — 产品优先做好体验,再解决规模化;在 GPU 产能紧张期,规模化相关技术(上下文管理、模型路由)可成暂时护城河。
- **AI / token neutrality(AI / token 中立)** — 类比电网中立:若少数模型公司成为"什么能被造出来"的仲裁者,社会是否需要一种中立性保障。
- **Capital begets capital(资本自我繁殖)** — AGI 到来后不再需要"劳动力认可",资本可绕过人力约束自我放大,加剧财富集中。
- **Explore vs exploit(探索 vs 利用)** — 借自强化学习:创业前应大量探索(多样化信息与想法),再进入"利用"阶段(锁定并创业)。

## 🔖 高价值金句时间戳
- `[03:42]` "You should be planning two years in advance because it's extremely likely that we will have AGI in the next few years." — 把规划视野从"下一代模型"拉长到"AGI 到来",是全片的核心前提。
- `[05:18]` "It's not just the startups, the incumbents benefit from AI, too." — 别把"大公司迟钝"当护城河,水涨众船高、买方也在被武装。
- `[07:33]` "But if you can do code on demand, why not do it on demand?" — 把"按需生成"推到极致的产品想象,也把"信任"逼成前置条件。
- `[13:28]` "A single person could make a decision that changes the entire impact of a product." — 团队越小越自动化,信任机制越脆弱——这是 Agent 时代的治理隐患。
- `[19:44]` "Frontier LLMs do not know how to build a cutting edge semiconductor fab." — 隐性知识 = 通用 AI 抹不平的护城河,值得创始人认真对待。
- `[21:26]` "In two years or three years, if I can just prompt Claude 7 or GPT 7 to just replicate your startup, what's your advantage going to be?" — 用最锋利的方式逼你回答"防御性"。
- `[28:46]` "When we say build something people want... what does society need?" — 把 YC 口号从"想要"升级到"需要",给这波 AI 创业一个更高的标尺。
- `[37:31]` "You're two years behind already." — 对自诩前瞻的 VC/创始人的当头棒喝:该问"今天投什么才能在两年后稳固"。
