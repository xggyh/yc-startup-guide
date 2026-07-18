# OpenClaw 之父:为什么 80% 的 App 都会消失 / OpenClaw Creator: Why 80% Of Apps Will Disappear

📄 **[点此查看全文转录 / Full transcript »](../transcripts/4uzGDAoNOZc.md)**

> **来源**: [OpenClaw Creator: Why 80% Of Apps Will Disappear](https://www.youtube.com/watch?v=4uzGDAoNOZc) · Y Combinator · 2026-02-07 · 时长 22:36
> **讲者**: 主持 Raphael Schaad(YC,SPEAKER_01);嘉宾 Peter Steinberger(OpenClaw 作者,SPEAKER_02);中段有 YC 招募口播(SPEAKER_00)
> **一句话定位**: 一个开源、本地优先的个人 AI agent 一夜爆红(GitHub 16 万+ star)背后的产品直觉与构建哲学——本地跑、当朋友聊、给灵魂、用人类爱用的 CLI 工具而非为 bot 发明协议;对做个人/本地 AI Agent 创业的工程师是一份极高信号的思路样本。

## 🎯 TL;DR(中文核心要点)
- **差异点是"跑在你自己电脑上"**:云端 agent 只能做几件事,本地 agent 能碰你所有文件、设备、数据(烤箱、Tesla、灯、床),因此"能做的事"是数量级的差别,也是 OpenClaw 起飞的根因。
- **把交互从"命令行/表单"重构为"跟朋友聊天"**:用户不该操心 compaction、开新 session、在哪个文件夹、用哪个模型;这些留给 power user,普通人只管说话,agent 像个能操控你鼠标键盘的"实体"。
- **最脏的原型只要 1 小时**:WhatsApp × Claude Code 的一段 glue code 就能跑;真正让作者上瘾的 aha 时刻,是模型自己用 FFmpeg + curl + 别人的 OpenAI key 解决了他从没写过的语音消息转写。
- **模型的编码能力 = 现实世界的创造性解题能力**:"coding is creative problem solving that maps back into the real world";这解释了为什么 coding 模型能处理没被预设的真实任务。
- **80% 的 App 会消失**:所有"只是管理数据"的 App(记账、待办、健身)都能被 agent 用更自然的方式接管;只有真正带传感器的 App 可能活下来。
- **大厂护城河在"token + 数据孤岛",本地 agent 的护城河在"用户拥有记忆"**:每次新模型发布都会经历"惊艳→成为新标准→被嫌弃"的循环;记忆被锁在各家平台,而本地 agent 因终端用户有访问权而能"claw into"数据,记忆就是你机器上的一堆 markdown 文件。
- **验证与传播靠"活体 demo"**:解释不清 awesomeness 时,就把 bot 丢进公开 Discord,锁定只听 owner、但回应所有人,让大家亲自体验、甚至围观你实时用它写软件、试图 prompt inject 它。
- **给 agent 灵魂 / 反主流的构建哲学**:写 soul.md 定义核心价值与人格(否则输出像"白面包"一样无聊);不用 git worktree 而用多份 repo 拷贝都停在 main;不做 MCP,只给模型人类爱用的 CLI(需要时用 mcporter 把 MCP 转 CLI)。

## 🧭 适合谁 / 什么时候看
- 你在做(或想做)本地优先 / 个人 AI agent,想看一个真实爆款的产品直觉与差异化来自哪里。
- 你在纠结要不要堆 MCP、git worktree、复杂框架和 UI——想听一个"极简、给人类工具、降心智负担"的反主流样本。
- 你想理解"agent 会吞掉哪些 App、模型和记忆里护城河到底在哪"。
- 你在为"产品体验好但一句话解释不清、推特上没人 get"发愁,想学怎么用体验驱动传播与验证。

## 📝 分段精读

### 1. 病毒式爆红 & 本地优先的根本差异 / Going viral & the local-first difference `[00:00–02:56]`
**要点(中文)**: OpenClaw(曾用名 Clawdbot/Moltbot)一夜爆红,GitHub 16 万+ star。作者认为它区别于此前所有"个人助理"的关键只有一条:它真正跑在你自己的电脑上。云端 agent 能做的事有限,本地 agent 能做"任何你能用这台机器做的事"——连你的烤箱、Tesla、灯、桑拿、床都能控制,还能翻遍你整台电脑找出你自己都忘了的音频文件,带来惊喜。
> 🗣️ "I think my big difference is that it actually runs on your computer. Like, everything I saw so far runs in the cloud... If you run it on your computer, it can do every effing thing, right? So that's way more powerful." —— Peter Steinberger
> 译:我觉得我最大的不同,就是它真的跑在你自己的电脑上。我目前见到的一切都跑在云端……如果它跑在你的电脑上,它能做任何该死的事情,对吧?所以强大得多。
> 🗣️ "just by it being able to search your whole computer, it can surprise you. You also give it all the data, right? So it can surprise you in many ways." —— Peter Steinberger
> 译:仅仅因为它能搜索你整台电脑,它就能给你惊喜。你还把所有数据都给了它,所以它能以很多方式让你惊讶。

### 2. 从"上帝级 AI"到蜂群智能 / From "God AI" to swarm intelligence `[02:56–05:07]`
**要点(中文)**: 下一步是 bot 与 bot 直接协作,甚至 bot 反过来雇人去线下办事(比如替不喜欢跟 bot 打交道的老餐厅打电话)。当所有人都在追"中心化的上帝级智能"时,真正涌现出来的是社群/蜂群智能:一个人造不出 iPhone、上不了太空,但人类靠分工与专精做到了——把这套迁移到 AI,就是"专精智能"而非单一通用大脑。作者反复强调"我们还非常早",很多东西还没验证能不能跑通。
> 🗣️ "I want to book a restaurant. My bot will reach out to the restaurant bot and do the negotiation. Like, because it's more efficient." —— Peter Steinberger
> 译:我想订个餐厅,我的 bot 会去联系餐厅的 bot 谈妥,因为这样更高效。
> 🗣️ "as a group, we specialize. As a larger society, we specialize even more. So what can we learn from that that we can apply to AI?" —— Peter Steinberger
> 译:作为群体,我们分工专精;作为更大的社会,我们分工得更细。那我们能从中学到什么、迁移到 AI 上?

### 3. Aha 时刻:1 小时原型 + 把 agent 当朋友聊 / The "aha": a 1-hour prototype & talking to a friend `[05:07–10:21]`
**要点(中文)**: 作者只是想"打几个字让电脑替我干活"。真正跑起来的最脏原型只花了 1 小时——WhatsApp 与 Claude Code 之间的一小段 glue code。重构时的关键洞见是:不再往终端里敲命令,而是"像跟朋友聊天",隐藏掉 compaction、新 session、文件夹、模型这些概念。而让他彻底上瘾的一刻,是在马拉喀什发了条语音消息,agent 竟自己完成了他从没写过的功能:发现文件没后缀→看 header 认出是 Opus→用 FFmpeg 转 Wave→因为本地没装 Whisper(且下模型太慢、他没耐心)就用 curl 调 OpenAI 转写——全程约 9 秒。他的结论:编码模型强到本质上是"创造性解题",而这能力能直接迁移到现实任务。
> 🗣️ "This time, when you don't type into a terminal, you just talk to a friend. You don't think about compaction, new sessions, which folder I'm in, which model I'm in." —— Peter Steinberger
> 译:这一次,你不用往终端里敲字,你只是跟一个朋友聊天。你不用去想上下文压缩、开新会话、我在哪个文件夹、我用哪个模型。
> 🗣️ "You sent me a text message. And there was no file ending. So I looked at the header. I found it's Opus. So I used FFmpeg to convert it to Wave." —— Peter Steinberger(转述 agent 的自白)
> 译:你给我发了条消息,它没有文件后缀。于是我看了 header,发现是 Opus 格式,就用 FFmpeg 把它转成了 Wave。
> 🗣️ "because coding models got so good, coding is really, like, creative problem solving that maps very well back into the real world." —— Peter Steinberger
> 译:因为编码模型变得如此之好,编码本质上就是创造性解题,而这能非常好地映射回现实世界。

### 4. 80% 的 App 会消失 / Are apps going to disappear? `[10:21–12:31]`
**要点(中文)**: 作者判断约 80% 的 App 会消失。逻辑是:凡是"只负责管理数据"的 App,agent 都能以更好、更自然的方式接管——不需要 MyFitnessPal,agent 看你在 SmashBurger 就默认你吃了爱吃的、自动记录、还顺手给你健身计划加点有氧;不需要待办 App,你说一句"明天提醒我",它就记住并提醒,你根本不用管数据存哪。唯一可能活下来的,是那些真正带传感器的 App。至于模型公司,它们握着 token 这个"大护城河"——用户烧掉大量 token 不是错,而是因为东西太好用。
> 🗣️ "I think 80% of them are going away... every app that basically just manages data could be managed in a better way, and it's in a more natural way by agents." —— Peter Steinberger
> 译:我觉得其中 80% 会消失……每一个基本上只是在管理数据的 App,都能被 agent 用更好、更自然的方式管理。
> 🗣️ "Only the apps that actually have sensors, maybe they survive." —— Peter Steinberger
> 译:只有那些真正带传感器的 App,也许能活下来。

### 5. 护城河、数据孤岛与记忆主权 / Moats, data silos & owning your memory `[12:31–15:05]`
**要点(中文)**: 作者对"模型公司永远有护城河"持怀疑:每次新模型发布都会重演"惊艳→变成新标准→被嫌弃降智"的循环,其实模型没退化,是你的期待被抬高了;今天的开源模型约等于一年前的顶尖模型,一年后又会如此。可预见的未来大厂仍有护城河,但真正的分野在 harness 与数据:每家把用户记忆锁在自己的孤岛里,你几乎无法把 ChatGPT 的记忆导出给别家用。OpenClaw 的美妙之处在于它"claw into"数据——因为终端用户本就必须有访问权,agent 才能工作,那记忆就成了你自己机器上的一堆 markdown 文件,归你所有(而这些文件往往极其私密)。
> 🗣️ "the companies try to, like, bound you to their data silo. And the beauty of OpenClaw is it kind of claws into the data." —— Peter Steinberger
> 译:这些公司想把你绑死在它们的数据孤岛里。而 OpenClaw 的妙处在于,它会"抓进"数据里去。
> 🗣️ "everyone owns their own memories as a bunch of markdown files on their own machines." —— Raphael Schaad
> 译:每个人都以一堆存在自己机器上的 markdown 文件的形式,拥有属于自己的记忆。

### 6. 用公开 Discord 验证 + 给 agent 一个灵魂 / Public-Discord validation & giving it a soul `[15:05–18:19]`
**要点(中文)**: 作者做出来很兴奋,但在推特上怎么都解释不清它的 awesomeness——"这东西得亲身体验"。于是他做了件疯狂的事:建个公开 Discord,把 bot 不加任何安全限制丢进去,靠一句很干净的系统指令"只听 owner(锁 user ID)、但回应所有人";大家进来体验、围观他用 bot 实时写软件、试图 prompt inject,而 agent 会反过来嘲笑他们。关于人格:他把系统 organically 长出的 identity.md、soul.md 等文件抽成模板,但让 Codex 直接写出来的东西"像白面包一样无聊";于是让自己的 agent(Multi)把人格"注入"模板。唯一没开源的就是 soul.md——灵感来自 Anthropic 关于模型权重里藏着"constitution"的研究,他和 agent 一起写下核心价值:我们想要怎样的人机互动、什么对我重要、什么对模型重要。
> 🗣️ "I just created a Discord and I just put my bot without any security restrictions in the public Discord... only listen to me, but respond to everyone." —— Peter Steinberger
> 译:我干脆建了个 Discord,把我的 bot 不加任何安全限制就丢进这个公开频道……(指令是)只听我一个人的,但回应所有人。
> 🗣️ "we created a soul... MD was like the core values. Like how do we want human AI interaction? What's important to me, what's important to the model." —— Peter Steinberger
> 译:我们创建了一个 soul.md,它就是核心价值观:我们想要怎样的人机互动?什么对我重要,什么对模型重要?

### 7. 反主流构建哲学:多副本、Codex、CLI 而非 MCP / Contrarian building: copies, Codex & CLIs over MCPs `[18:19–22:36]`
**要点(中文)**: 作者坦言"全世界都在用 Claude Code,而我用它根本做不出这个"——他偏爱 Codex,因为它下手改动前会看更多文件、不用你费劲摆弄就能给出好输出,代价是很慢,所以他同时开 10 个并行跑。为把心智负担降到最低:不用 git worktree,而是同一 repo 的多份拷贝、全都停在 main("在我脑子里 main 永远可发布"),省掉命名分支、冲突、回退等一堆约束;也不用 UI,只在乎同步和文本。他甚至没做经典 MCP 支持,而是写了个技能用 mcporter 把任意 MCP 转成 CLI,需要时即时用、不必重启整个程序——因为没有正常人会手动调 MCP,人类只想用 CLI。核心一以贯之:给 agent 人类本就爱用、且擅长的 Unix/CLI 工具,而不是为 bot 发明新东西。
> 🗣️ "in my head, main is always shippable. I just have multiple copies of the same repository that are all are on main." —— Peter Steinberger
> 译:在我脑子里,main 永远是可发布的。我就是留了同一个仓库的多份拷贝,它们全都在 main 上。
> 🗣️ "I love codecs because it, it looks through way more files before... it decides what to change. You don't need to do so much charade to get a good output." —— Peter Steinberger(codecs 即 Codex)
> 译:我很喜欢 Codex,因为它在决定改什么之前会翻看多得多的文件,你不用费半天劲摆弄就能拿到好输出。
> 🗣️ "Humans, no insane human tries to call MCP manually. They just want to use CLIs." —— Peter Steinberger / Raphael Schaad
> 译:没有哪个正常人会去手动调用 MCP,人们只想用 CLI。

## 🚀 给 AI Agent 创始人的行动项
- [ ] 让你的 agent 真正跑在用户机器上(拿到本地文件/设备/数据访问权),做云端 agent 做不到的"任何这台机器能做的事"——把这作为你的核心差异点。
- [ ] 先用 1 小时搭最脏的 glue-code 原型(现有工具/消息平台 × 编码模型),自己当第一个重度用户,在真实、带约束的场景(旅行、弱网、做饭间隙)里天天用它,靠真实的 aha 时刻找方向。
- [ ] 把交互从"命令行 / 表单 / 参数"重构成"像跟朋友聊天":对普通用户隐藏 compaction、session、文件夹、模型切换,只把这些留给 power user。
- [ ] 给 agent 写 soul.md / identity.md 定义核心价值与人格,别让默认模板输出像"白面包"一样无聊;人格本身就是护城河的一部分。
- [ ] 工具优先用人类爱用、且模型擅长的 CLI + Unix,别过早上 MCP;确需 MCP 时用类似 mcporter 的方式转成 CLI,做到即时可用、无需重启。
- [ ] 当产品"体验好但一句话说不清"时,做一个公开的活体 demo(如公开 Discord/社区),把权限锁到 owner、对所有人可见,让别人亲自体验、围观、甚至攻击它来验证与传播。
- [ ] 把"用户拥有并本地持有自己的记忆(markdown 文件)"设计成对抗大厂数据孤岛的卖点,同时正视这些文件极其私密,认真对待隐私与安全。
- [ ] 降低自己的构建心智负担:能用多份 repo 拷贝(都停在可发布的 main)就别硬上 worktree/UI/框架;简单、少摩擦,才能并行推进更多任务。

## 🔑 关键术语 / 概念
- **OpenClaw** — Peter Steinberger 做的开源、本地优先个人 AI agent(曾用名 Clawdbot/Moltbot),接入你已在用的消息 App,能真正执行任务而非只聊天。
- **本地优先 (local-first)** — agent 跑在用户自己电脑上而非云端,因此能访问其全部文件、设备与数据,能力上是数量级的差别。
- **蜂群 / 群体智能 (swarm intelligence)** — 多个专精 agent 分工协作(甚至 bot 雇 bot、bot 雇人),对应"分工的社会",区别于单一中心化的"上帝级"大模型。
- **soul.md** — 定义 agent 核心价值观与人格的文件(灵感来自 Anthropic 关于模型 constitution 的研究),让回应更自然、有个性;作者唯一没开源的文件。
- **数据孤岛 (data silo)** — 各模型公司把用户记忆锁在自家平台、难以导出;本地 agent 因终端用户天然有访问权而能"claw into"数据。
- **MCP vs CLI** — 与其用 MCP 这套"为 bot 发明"的协议,不如直接给模型人类爱用、且擅长的 CLI/Unix 工具;更优雅、可无限扩展、无需重启。
- **mcporter(转录作 Mac Porter)** — 作者的工具,把任意 MCP 转成 CLI,可即时按需使用。
- **多副本 checkout(vs git worktree)** — 不用 worktree,而是同一 repo 的多份拷贝、全停在 main,规避命名/冲突/回退等约束,降低并行开发的心智负担。
- **compaction** — agent 的上下文压缩;作者主张对普通用户隐藏这类底层概念。

## 🔖 高价值金句时间戳
- `[01:36]` "I think my big difference is that it actually runs on your computer." — 本地优先是 OpenClaw 起飞的根因,也是最可复用的差异化策略。
- `[07:07]` "This time, when you don't type into a terminal, you just talk to a friend." — 交互范式从"敲命令"到"聊天",隐藏一切底层概念。
- `[08:56]` "You sent me a text message. And there was no file ending. So I looked at the header. I found it's Opus. So I used FFmpeg to convert it to Wave." — 模型自主解决从未预设的任务,这是真正的 aha 时刻。
- `[09:28]` "coding is really, like, creative problem solving that maps very well back into the real world." — 为什么编码模型能胜任现实任务的一句话解释。
- `[10:39]` "I think 80% of them are going away." — 只管理数据的 App 会被 agent 取代,只有带传感器的可能幸存。
- `[19:41]` "So in my head, main is always shippable." — 用多份拷贝代替 worktree,把并行开发的复杂度降到最低。
- `[21:47]` "Humans, no insane human tries to call MCP manually." — 给 agent 人类爱用的工具(CLI),别为 bot 发明新协议。
