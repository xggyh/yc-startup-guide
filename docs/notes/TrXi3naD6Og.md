# 24 岁做出 Cursor:在 GitHub Copilot 阴影下,靠"信念一致性"押注编程的未来 / Building Cursor At 23, Taking On GitHub Copilot & Advice To Engineering Students

> **来源**: [Michael Truell: Building Cursor At 23, Taking On GitHub Copilot & Advice To Engineering Students](https://www.youtube.com/watch?v=TrXi3naD6Og) · Y Combinator · 2025-09-03 · 时长 27:56
> **讲者**: Michael Truell(Cursor / Anysphere 联合创始人兼 CEO,SPEAKER_02) · 对谈主持:Diana Hu(YC General Partner,SPEAKER_00);SPEAKER_01 为 YC 广告口播
> **一句话定位**: 一个 AI 编程公司如何在明知巨头(Copilot 已年入 $1 亿+)先行、且自己数次失败后,靠"如果我们对自己的信念保持一致,未来五年所有编程都会经由模型流动"这一判断,一年从 $1M 做到 $100M ARR——对 AI Agent 创始人是关于"选赛道、砍旧想法、务实自研、口碑增长"的实战样本。

## 🎯 TL;DR(中文核心要点)
- **别因为"太卷"而回避你真正相信的赛道**:他们最初刻意避开 AI 编程(Copilot 已年入 $1 亿+),结果这才是他们最激动、最有信念的方向。回避的理由("太竞争")事后看很荒谬。
- **判断赛道的核心不是当下产品差距,而是"信念一致性推演"**:如果你真信 AI 会让"今天我们所知的编程被自动化",那现有玩家只是在把已有形态"再打磨一点点",没人认真为终局做产品——机会正在这里。
- **失败的想法要果断砍**:CAD 机械工程 copilot、端到端加密通讯,做了半年、基本零用户。选 CAD 的理由是"觉得它无聊、冷门、不竞争"这种"扶手椅 MBA"式推理,而团队里根本没人是机械工程师——一开始就是烂选择。
- **MVP 要极度务实,不要重造轮子**:第一版自建编辑器耗时且是无底洞(VS Code 花了 12 年、几百人),他们很快认清"时间最该花在 AI 上",于是像浏览器基于 Chromium 一样,转向基于 VS Code 分叉。
- **自研模型是"务实的第二步"而非起点**:一开始"完全不自研",先用现成模型跑通产品;随着规模上来,自研 tab/下一步预测模型才成为关键的"产品杠杆",并让产品数据反哺模型。
- **在对的市场里,做得更好会立刻反映在数字上**:终端用户偏好至上的市场,"你把产品做得更好,增长立刻能看到";口碑像野火一样传播,靠这个从 0 到 $100M。
- **抵住"产品已经够好、去搞增长工程"的诱惑**:2023 年像"苦行僧"一样只打磨产品、砍掉营销,反而是复利增长的根基。也要抵住吵闹用户把你拉偏(非程序员用户、绑死单一技术栈的需求)。
- **给未来工程师的判断**:AI 是几十年尺度的产业级变革,不是 1-2 年 AGI 一步到位;中间会有"漫长而混乱的中段",AI 越来越像同事、也像更高级的编译器,但你仍要读逻辑、审查、编辑代码。编程"像数学一样是好的通识教育",不会消失。

## 🧭 适合谁 / 什么时候看
- 正在纠结"赛道太卷、巨头已在、要不要还做"的 AI 应用创始人(尤其 AI Agent / 开发者工具方向)。
- 连续试错、几个想法都不 work、在犹豫"是否再 pivot"的早期团队。
- 在"自研模型 vs 用现成 API"之间摇摆的技术型创始人。
- 想理解"靠产品口碑而非投放做增长"是什么体感的人。

## 📝 分段精读

### 1. 起点:PG 的文章与最早的代码 / Origins: PG essays & first code `[00:38–02:36]`
**要点(中文)**: Michael 很早就想创业,而且是"带着商业动机"进入编程的——最早看到代码是和哥哥想做一款爆款手游、上 Google 搜"怎么做游戏"、下载 Xcode 撞上一堵 Objective-C 的墙。哥哥当场退出,他买了本书坚持下来。高中起就深受 PG(Paul Graham)和 Sam Altman 的文章、以及 YC 一众人的影响。这一段确立了"长期主义"的底色:Cursor 看似横空出世,其实是十年积累。
> 🗣️ "I originally got into programming being interested in in starting something." —— Michael Truell (SPEAKER_02)
> 译:我最初进入编程,恰恰是因为对"创办点什么"感兴趣。

### 2. 少年时代:机器人与从零手搓 ML / Games, robots, and hacking ML as a teenager `[02:36–06:54]`
**要点(中文)**: 手游做得不好,反而是最"技术上最简单"的东西火了——一个能在 Piano Tiles、Flappy Bird 里伪造高分发给朋友的 App。这是他总结的第一条创业教训:代码不是全部。随后和朋友想做一只"用奖惩来教、而不是编程"的机器狗,一路踩坑从遗传算法学到神经网络再到强化学习;因为在微控制器上内存太小、装不下 Torch/TensorFlow,他们 16、17 岁时从零手写了一个极小的神经网络库,甚至还没学微积分。
> 🗣️ "which was maybe a lesson in startups of the code isn't everything" —— Michael Truell (SPEAKER_02)
> 译:这也许是关于创业的一课——代码不是一切。
> 🗣️ "we implemented our own tiny neural network library ... not really understanding calculus, but kind of fumbling our way through reimplementing some important ideas from neural networks" —— Michael Truell (SPEAKER_02)
> 译:我们自己实现了一个极小的神经网络库……当时甚至没真正搞懂微积分,只是磕磕绊绊地把神经网络里一些重要思想重新实现了一遍。

### 3. 从 Hemisphere 到 Cursor:最初几次失败尝试 / First startup attempts (CAD & encrypted messaging) `[06:54–09:54]`
**要点(中文)**: 2022 年初,四位联合创始人(刚从 MIT 毕业)搞了一个月的"黑客松",挑一个知识工作领域押注 AI 会成熟。第一个认真做很久的想法是**给机械工程师做 CAD copilot**(预测你在 SOLIDWORKS/Fusion 360 里的建模动作)。选它的理由是"觉得它无聊、冷门、不竞争"——一种"扶手椅 MBA"式推理,但团队没人是机械工程师,一开始就是烂选择。大量精力耗在爬 CAD 文件、格式转换、给不可扩展的软件硬塞插件、以及当时简陋的训练基础设施上。同时另两位联合创始人在做**隐藏"谁在和谁通信"元数据的端到端加密通讯**(Signal/WhatsApp 只加密正文)。做了约半年,基本零用户。
> 🗣️ "We picked it because we thought it would be boring and sleepy and uncompetitive. And we were kind of doing an armchair MBA thing, even though it was a horrible choice from the get-go because none of us were really mechanical engineers" —— Michael Truell (SPEAKER_02)
> 译:我们选它是因为觉得它无聊、冷门、不竞争。我们其实是在做一种"扶手椅 MBA"式的推理,可从一开始它就是个糟糕的选择,因为我们里面根本没人是真正的机械工程师。
> 🗣️ "All of these projects were ill-fated, and it had basically no users." —— Michael Truell (SPEAKER_02)
> 译:所有这些项目都命途多舛,基本上没有用户。

### 4. 全都不行时的果断转向 & 硬刚 GitHub Copilot / Pivoting hard & taking on Copilot `[09:54–13:10]`
**要点(中文)**: 关键转折:是"做了一堆想法、越做越提不起劲、又都没成"的绝望,反而塑造了他们真正在乎什么。他们退一步意识到——自己真正内在地为编程的未来激动;而且如果对自己的信念保持一致,未来五年所有编程都会经由模型流动,当时没人认真为这个终局做产品。他们之前正因为"太卷"(Copilot 已年入 $1 亿+)而回避 AI 编程,这个理由事后看很荒谬。做这个决定当时并不觉得"大胆"——不过是几个人在客厅抱着笔记本;他们甚至先想过做很窄的东西(CVE 安全审查、给量化研究员的工具),但满脑子都是"如果只做'用 AI 写代码的最好方式'会怎样"的点子,于是干脆全力去做。
> 🗣️ "we had avoided working on AI and coding because we thought it was too competitive. Which is crazy." —— Michael Truell (SPEAKER_02)
> 译:我们一直回避做 AI 和编程,因为觉得太竞争了。这现在看来很疯狂。
> 🗣️ "it felt like no one working on the space at the time was really taking that seriously. It felt like they had great products, and they were making them a bit better. But they weren't really aiming for a world where all of coding as we know it today gets automated." —— Michael Truell (SPEAKER_02)
> 译:当时感觉这个领域里没人真的认真对待这件事。他们有很好的产品、也在把它们做得好一点,但他们并没有真正瞄准一个"今天我们所知的编程被全部自动化"的世界。
> 🗣️ "It didn't really feel bold or like a move at the time, because it's like a bunch of people sitting around in their living room on laptops." —— Michael Truell (SPEAKER_02)
> 译:那在当时其实并不觉得大胆、也不像什么"重大决策",因为不过是几个人坐在客厅里抱着笔记本。

### 5. 出货第一版编辑器 & 早期教训(转向 VS Code) / Shipping the first editor & early lessons `[13:10–16:26]`
**要点(中文)**: 从第一行代码到 GA 约三个月:4 周做出自己能当主力用的版本,再 4 周给首批 beta,再 4 周 GA。第一版是**从零自建编辑器**(用 CodeMirror、language server 等开源积木),自研远程 SSH、Copilot 集成等。两个核心教训:(1)当时的 AI 形态需要"更多控制"——最早只有一个万能快捷键让 AI 猜你要什么,反馈后他们迭代出后来成为 Cursor 核心的早期 AI 功能;(2)"给全世界做一个功能完备的编辑器"是远远更长的路(VS Code 做了 12 年、几百人),他们迅速认清时间最该花在 AI 上,于是像浏览器基于 Chromium 一样,改为**基于 VS Code 分叉**。
> 🗣️ "our time was going to be best spent just focused on the AI stuff. And so similar to how browsers often base themselves off of Chromium's rendering engine, we then switched to being based off of VS Code." —— Michael Truell (SPEAKER_02)
> 译:我们的时间最该花在 AI 上。于是,就像浏览器常常基于 Chromium 的渲染引擎一样,我们转而基于 VS Code 来做。

### 6. Codex、自研模型与务实的押注 / Codex, custom models, and pragmatic bets `[16:26–17:58]`
**要点(中文)**: 融第一轮时,他们四处引用的一篇论文正是 OpenAI 的 Codex(Copilot 背后的第一个自动补全模型)——因为按他们的估算,当时人人都说训模型很贵,而 Codex 训练成本其实只有约 $100K。在 CAD 阶段被自研"烧过",做 Cursor 时他们选择**极度务实、不重造轮子,一开始完全不自研**。但在 2023 打磨产品、规模上来后,自研模型(尤其 tab / 下一步编辑预测)反而成了关键的"产品杠杆",还能用产品数据持续把产品做得更好——这成了公司很重要的一块肌肉。
> 🗣️ "we wanted to be as pragmatic as possible, not reinvent the wheel. And so we started by doing none of that." —— Michael Truell (SPEAKER_02)
> 译:我们想尽可能务实、不去重造轮子,所以一开始我们什么(自研)都不做。
> 🗣️ "I think it was about $100K in training costs." —— Michael Truell (SPEAKER_02)
> 译:我记得(Codex 的)训练成本大约是 10 万美元。

### 7. 2023 的荒野徘徊 & $1M→$100M 的爆发 / Wandering in 2023 & the breakthrough `[17:58–22:46]`
**要点(中文)**: 2023 增长很慢、数字很小,且"下一步不总是清晰"——这不是那种去访谈、把用户痛点系统列出再逐个解决的市场;作为一个"没多少复杂度预算"的终端应用,难点在于"用今天的工具到底能做出什么"。如果只跟着早期用户的梯度走,会被带偏:一批很吵的用户完全不会写代码、另一批要求绑死单一技术栈——他们都抵住了。2024 则从 $1M 到 $100M、每周复利 ~10%。驱动力很朴素:codebase 感知、预测下一步动作、更准、更快、更有野心(预测一连串修改)、让模型在你代码库里采取更多动作并且快——每次把产品做得更好,增长立刻反映在数字里。
> 🗣️ "there was a lot of early prototyping and kind of wandering the desert in 2023" —— Michael Truell (SPEAKER_02)
> 译:2023 年有大量的早期原型试验,某种程度上是在沙漠里徘徊。
> 🗣️ "we had a really loud segment of users that didn't know how to code at all ... a really loud segment of users that wanted us to do things that were very tech stack specific ... And we resisted doing that too." —— Michael Truell (SPEAKER_02)
> 译:我们有一批很吵的用户根本不会写代码……还有一批很吵的用户要我们做非常绑死某个技术栈的东西……这些我们也都抵住了没做。
> 🗣️ "if you make the product better, you kind of see it in the numbers immediately" —— Michael Truell (SPEAKER_02)
> 译:在这个市场里,你把产品做得更好,几乎能立刻在数字上看到反应。

### 8. 口碑野火式增长 & 编程的未来与给学生的建议 / Word-of-mouth growth, the future & advice `[22:46–27:56]`
**要点(中文)**: 早期靠一位联合创始人在推特上持续、深度地谈 AI(读遍论文、认真思考、公开输出,甚至因推荐 Flan T5 被业内重要人物注意到)攒下"SF 微名人"影响力,做出"电影魔法般"的首发 demo 和候补名单。此后他们**退出营销、像苦行僧一样只打磨产品**,靠口碑传播。团队里几次有人说"产品已经够好了,去搞增长工程吧",但打磨产品的方向始终没被冲淡。对未来:AI 是几十年尺度、全行业接力的变革,不是 1-2 年 AGI 一步到位;会有"漫长而混乱的中段",AI 越来越像同事、也像更高级的编译器,但你仍要读逻辑、审查、编辑。编程"像数学一样是好的通识教育",不会消失。给想成为"三年前的自己"的人的建议:做你真正感兴趣的事,和你既喜欢相处、又非常尊重的人一起,并且认真对待。
> 🗣️ "we kind of lived like monks in 2023 and just focused on the product. And it really just spread from word of mouth." —— Michael Truell (SPEAKER_02)
> 译:2023 年我们某种程度上像苦行僧一样活着,只专注打磨产品,而它真的就靠口碑传播开来。
> 🗣️ "there will be this long, messy middle where you will be working with the AI. More and more, it will become like a colleague ... it may also become like a very advanced compiler." —— Michael Truell (SPEAKER_02)
> 译:会有这样一段漫长而混乱的中段,你将与 AI 一起工作。它会越来越像一个同事……也可能越来越像一个非常高级的编译器。
> 🗣️ "just working on things that you're interested in and doing it with people both that you enjoy being around, but that you respect a ton, and taking that really seriously." —— Michael Truell (SPEAKER_02)
> 译:就是去做你真正感兴趣的事,并且和那些你既享受与之相处、又非常尊重的人一起做,而且认真对待它。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **用"信念一致性"而不是"当前竞争格局"来选赛道**:写下你对 3–5 年后 Agent 世界的真实信念,再问"如果我完全一致地相信它,现在该做的产品是不是没人在认真做?"——别因为"已经有巨头/太卷"就自我否决。
- [ ] **给每个想法设"证据止损线"**:CAD/加密通讯做了半年零用户才停。为当前 Agent 方向预设"多久内、要看到什么用户信号",到线就砍,避免靠感情硬撑。
- [ ] **MVP 阶段坚决站在巨人肩上**:别从零自建平台层(编辑器/框架/基础设施),像 Cursor 转向基于 VS Code 一样,复用成熟开源底座,把稀缺时间全押在你独有的 Agent 能力上。
- [ ] **自研模型当"第二步杠杆",不当起点**:先用现成 API 把 Agent 产品跑通、拿到规模和产品数据;当某个高频窄任务(如你的"tab 式"预测/补全)成为核心体验时,再自研专用小模型并用产品数据反哺。
- [ ] **选一个"产品变好→数字立刻涨"的市场,并据此排优先级**:优先做那些能立刻反映在留存/使用/口碑上的能力(codebase 感知、更准更快、能采取更多动作),把它当作增长引擎。
- [ ] **早期靠"深度公开输出"建立口碑,再切换为苦行僧式打磨**:像那位联合创始人一样持续输出对 AI/Agent 的深度思考换取早期关注与首发势能;拿到势能后抵住"产品够好了去投放"的诱惑,让口碑做增长。
- [ ] **谨慎对待"吵闹用户"的需求梯度**:识别哪些呼声(如非目标用户、绑死单一栈)会把水平化 Agent 拉偏,敢于对高声量但错方向的需求说不。

## 🔑 关键术语 / 概念
- **信念一致性推演(being consistent with your beliefs)** — 讲者反复用的判断框架:不看当下产品差距,而是把"你真正相信的终局(所有软件开发都经由模型流动)"推到底,看现有玩家是否只在小修小补、终局是否无人认真做。
- **Armchair MBA(扶手椅式 MBA 推理)** — 只凭"市场看起来无聊/冷门/不竞争"这类纸面推断选赛道,而不顾团队是否具备领域能力;被他讲者列为选 CAD 的反面教训。
- **Codex(paper / model)** — OpenAI 的代码模型,GitHub Copilot 背后第一代自动补全模型;讲者估算其训练成本约 $100K,用来说服投资人"训模型没那么贵"。
- **Tab / next edit prediction(下一步编辑预测)** — Cursor 的核心自研能力:预测你接下来的编辑动作(乃至一连串修改),是自研模型带来的关键"产品杠杆"。
- **Codebase-aware(代码库感知)** — 让 AI 理解整个代码库上下文的能力,是驱动 Cursor 增长复利的一系列产品改进之一。
- **VS Code fork(基于 VS Code 分叉)** — 放弃从零自建编辑器,改用成熟开源底座(类比浏览器基于 Chromium),以把时间集中在 AI 上的务实取舍。
- **Complexity budget(复杂度预算)** — 终端用户应用能承载的复杂度有限;Cursor 认为自己"没多少复杂度预算",因此必须克制功能、聚焦。
- **Long, messy middle(漫长而混乱的中段)** — 讲者对未来的判断:AI 不会 1-2 年一步到位,而是几十年产业级接力,中途人与 AI 长期协作,AI 像"同事"也像"高级编译器"。

## 🔖 高价值金句时间戳
- `[11:04]` "there was going to be an opportunity for all of coding to change in the next five years and for all of software development to flow through models" — 全片的核心信念,也是选赛道的底层逻辑:押终局,而非押当下差距。
- `[10:42]` "we had avoided working on AI and coding because we thought it was too competitive. Which is crazy." — "太卷所以别做"往往是错的自我否决,尤其在你最有信念的方向上。
- `[09:39]` "All of these projects were ill-fated, and it had basically no users." — 坦诚承认半年多的多个项目基本零用户,证明果断止损比硬撑更重要。
- `[16:15]` "we wanted to be as pragmatic as possible, not reinvent the wheel. And so we started by doing none of that." — 自研是"务实的第二步":先跑通,再在关键点自研。
- `[14:29]` "our time was going to be best spent just focused on the AI stuff." — MVP 取舍准则:把稀缺时间押在你独有的价值上,平台层复用现成的。
- `[20:14]` "if you make the product better, you kind of see it in the numbers immediately" — 选一个"产品变好即刻反映在数字"的市场,并据此排优先级。
- `[21:48]` "we kind of lived like monks in 2023 and just focused on the product. And it really just spread from word of mouth." — 抵住"去搞增长工程"的诱惑,让口碑成为增长引擎。
- `[27:19]` "just working on things that you're interested in and doing it with people ... that you respect a ton, and taking that really seriously." — 给早期创始人的选题与选人原则:真兴趣 + 高度尊重的同伴 + 认真对待。
