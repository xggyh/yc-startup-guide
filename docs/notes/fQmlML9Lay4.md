# 像指挥家一样管理一群编程 Agent:Conductor CEO 的 AI 编码工作流 / Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup

> **来源**: [Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup](https://www.youtube.com/watch?v=fQmlML9Lay4) · Y Combinator · 2026-06-04 · 时长 16:35
> **讲者**: Charlie Holtz —— Conductor 联合创始人 / CEO(YC S24);SPEAKER_00 为 YC《Full Stack》系列主持人(片中未点名,推测与文中提到的 Gary 相关)
> **一句话定位**: 一位已经"几乎不再手写代码"的 YC 创始人,逐屏演示如何用语音同时指挥多个编程 Agent、把哪些决策留给人、哪些放手给 AI——给 AI Agent 创始人一套可直接照抄的"人在环上"工作流与产品哲学。

## 🎯 TL;DR(中文核心要点)
- **把自己当成"小公司 CEO",不是程序员**:一天里不断 `Cmd+N` 开新任务、语音下指令,一个 Agent 在跑时就切到下一个 chat,人只做 review / 指方向 / 合并,不写代码。
- **默认全速、全权限跑**:始终开 Fast Mode、`--dangerously-skip-permissions`(全部自动批准),要 token max 就得舍得花——他单月最高烧过 $22,000 token。
- **Skills 文件 + CLAUDE.md 是真正值钱的定制**:几百行明确写下"我们是 startup,不写你习惯的那套企业级代码",把团队工程规范固化进去,胜过零散调参。
- **划出"无 slop 区"(slop-free zones)**:代码库和文档里明确标注"人类专属、AI 勿动",因为 AI 会陷入"看到烂代码→写更多烂代码"的恶性循环;正向也同理。
- **别让 AI 当架构师**:核心抽象(workspace 概念)、API/契约、UI 与交互决策都由人想清楚;放手给 AI 的是"随便试想法、不影响核心基础设施"的大块区域,边界要清晰。
- **信念靠"逼自己天天用"建立,而非 A/B 与埋点**:强观点、少配置,凭手感(gut feel)判断"这样对不对",并刻意领先 frontier 半步、逼用户跳出舒适区。
- **强制工作流本身就是产品**:Conductor 故意不让你直接改文件——每个 workspace 必须是 work tree、必须建 PR、必须合并,用约束把好习惯变成默认。
- **代码正在变成"锯末"(sawdust)**:真正的资产是你的 prompt;下一代模型出来后重跑 prompt 就能生成新代码,旧代码本身没那么重要——软件正走向"可 mod、可塑"。

## 🧭 适合谁 / 什么时候看
- 正在做/想做 **AI coding agent、agent 编排(orchestration)、开发者工具** 的创始人,想看一个真实高强度用户的工作流长什么样。
- 已经在用 Claude Code / Codex,但还停留在"一次盯一个 agent"、想升级到**并行管理多个 agent**的工程师。
- 纠结"哪些决策该交给 AI、哪些必须人来把关",以及如何在产品里**用强制约束固化工作流**的产品/技术负责人。

## 📝 分段精读

### 1. 用语音同时指挥多个 Agent / Talking to computers & orchestrating agents `[00:00–02:39]`
**要点(中文)**: Charlie 一天大部分时间待在 Conductor 里"用 Conductor 造 Conductor"。核心动作是不断 `Cmd+N` 开新任务、对着 $20 的鹅颈麦克风口述需求(如"看下最新的 linear issue,给我一版粗解法"),趁一个 Agent 在跑就切到下一个 chat 做 review。工作方式高度**实验化**:大量并行开 workspace 试不同想法,绝大多数不会合入,喜欢的才逐级晋升到 internal / experimental。甚至能用手机语音在"路上"发起任务。
> 🗣️ "We're using Conductor to build Conductor." —— Charlie Holtz
> 译:我们在用 Conductor 来打造 Conductor。
> 🗣️ "A big part of how I use Conductor is experimentation. I'm always kicking off workspaces to try different ideas. Most of them don't make it in." —— Charlie Holtz
> 译:我用 Conductor 很大一部分就是在做实验——不停开新 workspace 试各种想法,其中绝大多数都进不了主干。

### 2. 不再手写代码,像"小公司 CEO"一样管理 Agent / No longer coding by hand; feeling like a CEO `[02:39–04:17]`
**要点(中文)**: 问他今天还写不写代码,答案是"基本不写"——偶尔只改改 Tailwind class 或 `.env`。他们甚至专门做了个 **Caveman mode**(原始人模式)让你能手敲改文件,但名字本身就是提醒"这是退化操作"。绝大多数小修改靠高亮圈选 + 口述评论完成。理想状态是:你像一家小公司的 CEO,看着一群 Agent 替你干活、给你交上可消化的简报,你只需要"指个方向"或"看着行就合并"。
> 🗣️ "Once in a while, you do need to make a change to a file by hand, but it's called Caveman mode for a reason." —— Charlie Holtz
> 译:偶尔你确实得手动改一下文件,但它叫"原始人模式"是有原因的。
> 🗣️ "But the ideal is you should feel like the CEO of a little company. And you can see all your agents working for you." —— Charlie Holtz
> 译:但理想状态是,你应该感觉自己像一家小公司的 CEO,能看到一群 Agent 都在替你干活。

### 3. 真正值钱的定制:Skills / CLAUDE.md、Fast Mode、无 slop 区 / Customizations that actually matter `[04:17–06:32]`
**要点(中文)**: 被问哪些 tweak 真的重要,他给出三样:(1) 在 **skills 文件和 CLAUDE.md** 上投入大量时间,几百行明确写下团队工程规范("我们是 startup,别写你习惯的企业级代码");(2) 始终开 **Fast Mode**、用 **Context7 MCP** 取文档、且默认**全权限(dangerously accept all permissions)**运行——这是 Conductor 里的默认跑法;(3) 划清 **slop-free zones**:代码/文档里标注"人类专属",每一行都必须由人读过,因为 AI 一旦看到烂代码就会**滚雪球写出更多烂代码**。
> 🗣️ "I always use Fast Mode. ... If you're trying to token max, you have to be in Fast Mode." —— Charlie Holtz
> 译:我永远开 Fast Mode……如果你想把 token 用到极致,就必须开 Fast Mode。
> 🗣️ "The AI can get in a vicious cycle where it sees bad code, and then it writes more bad code as a result." —— Charlie Holtz
> 译:AI 会陷入恶性循环——它看到烂代码,结果就写出更多烂代码。
> 🗣️ "We have some lines in our code base that are like, do not touch if you are an AI. This is for human eyes only." —— Charlie Holtz
> 译:我们代码库里有些地方写着:如果你是 AI,不要碰,这是给人看的。

### 4. 别让 AI 当你的架构师 / Don't let the AI be your architect `[06:32–08:31]`
**要点(中文)**: 技术栈是 Tauri 桌面壳(Safari 原生渲染)+ Rust 后端,但 90–95% 是 TypeScript,web 端用 Elixir/Phoenix。真正的观点在方法论:**核心抽象、API/契约、UI 与交互决策都必须由人想清楚**——比如 workspace 这个概念、三栏布局、"Open In"按钮该怎么设计,都是人反复琢磨的结果;放任 AI 定 UI 就会得到"不像被精心打磨过"的东西。人该做的是把核心搭在"人写的 API 与契约"上,再划出大块**让 AI 自由发挥**的区域(随便试、不碰核心基础设施)。他强调要刻意**领先 frontier 半步**、逼用户跳出舒适区(Conductor 刚发布时用户普遍觉得"管一个 agent 都难,管三五个疯了")。
> 🗣️ "If you let the AI make your UI choices for you, you can end up with something that just doesn't feel crafted." —— Charlie Holtz
> 译:如果你把 UI 决策交给 AI,最后很可能得到一个"完全不像被精心打磨过"的东西。
> 🗣️ "It's important to have big chunks of your code base have free reign for the AI, where you can just throw a ton of different ideas at it and know that it's not going to affect the core infrastructure." —— Charlie Holtz
> 译:很重要的一点是,让代码库里的大块区域交给 AI 自由发挥——你可以往里扔海量想法,同时确信它不会动到核心基础设施。
> 🗣️ "It's really important to us that we stay a little ahead of the frontier, push people's comfort zones a little bit more than they'd expect." —— Charlie Holtz
> 译:对我们很重要的是始终领先 frontier 一点点,把用户往舒适区外多推一步,超出他们的预期。

### 5. 用强制工作流固化好习惯 + 靠"逼自己用"建立信念 / Enforcing workflows & building conviction `[08:31–10:39]`
**要点(中文)**: Conductor 是**刻意"有主见"**的产品:故意不让你直接改文件——任何 workspace 必须是 work tree、必须建 PR、必须合并,用约束把 review/PR 流程变成默认。被问强观点的信念从哪来,他的答案是**"逼自己天天用"**:不靠 A/B、不靠埋点分析,而是靠**手感(gut feel)**——用着不对劲就立刻能判断出来。同时他也承认工具需要保留灵活性、"feel like yours"。
> 🗣️ "We also purposely made it so you can't edit files directly. ... So we really enforced our workflow." —— Charlie Holtz
> 译:我们还故意做成你不能直接改文件……我们是真的把这套工作流强制了下来。
> 🗣️ "The way we build conviction is we force ourselves to use it. ... We're not big on analytics or looking at our A-B testing. It's very much a gut feel." —— Charlie Holtz
> 译:我们建立信念的方式,就是逼自己去用它……我们不太看数据分析或 A/B 测试,基本靠手感。

### 6. 模型选型、终端 vs GUI、Token maxing / Model choice, GUI, and token maxing `[10:39–13:24]`
**要点(中文)**: 模型分工很明确:**Codex 是"劳模"**,不怕大量 tool call、能陪你死磕一个具体问题;**Opus/Claude 更像"创作伙伴"**,做新功能时本能地会先找它、要更多来回讨论。为什么不用光秃秃的终端?因为"人是空间视觉动物",CLI 对 AI 友好但对人受限,GUI 能做很多终端做不到的事。Token 上他**极其舍得花**(Fast Mode、think extra hard、high effort 全开,单月烧过 $22,000),但对**代码行数则相反——刻意求少**,因为代码库很容易失控膨胀;而且"从零起一个 app"和"在 Conductor 这种成熟库里改"两种心态完全不同。
> 🗣️ "Codecs is like the workhorse. ... I feel like Opus is just a little more creative, like a little more of a partner." —— Charlie Holtz(注:Codecs 即 Codex 的口误/转写)
> 译:Codex 像是那头"老黄牛"……而 Opus 感觉更有创造力一点,更像一个搭档。
> 🗣️ "I spent $22,000 on tokens that month. ... We try and keep the lines of code minimal, actually." —— Charlie Holtz
> 译:那个月我在 token 上花了 22,000 美元……但代码行数上,我们其实是尽量往少了控。
> 🗣️ "There's a reason we moved from terminal interfaces to GUI interfaces in the 80s. I think humans are spatial visual creatures." —— Charlie Holtz
> 译:80 年代我们从命令行界面转向图形界面是有原因的——人本质上是空间视觉动物。

### 7. 代码变成"锯末":Prompt 才是资产,软件走向可塑 / Code is becoming sawdust `[13:24–16:35]`
**要点(中文)**: 他抛出核心世界观:**代码正在变成"锯末"(sawdust)**——过去代码是你精心打造的结构本身,现在你投入的是"描述你想要什么、要它怎么被造出来",代码只是这个过程掉出来的木屑。推论是:**真正的资产是你的 prompt**,下一代模型出来后重跑 prompt 就能得到新代码,旧代码本身不重要。更远处是**可塑软件(malleable software)**:就像玩《使命召唤》——骨架对所有人相同,但每个人能用自定义皮肤、改装,他希望用户也能像 mod 游戏一样 **mod Conductor**、内建自己的工作流。而人机协作还有大片空白待探索:能不能和 subagent 对话?能不能多人 multiplayer 一起和 AI 干活?他反复用的比喻是"你是乐团指挥"——大部分时间在乐团层面挥棒,偶尔才凑到某个乐手前纠音。
> 🗣️ "Code is almost like sawdust now ... you're putting time into describing what you want and how you want it to be built. And the code is almost just like sawdust that comes out of that process." —— Charlie Holtz
> 译:代码现在几乎像是锯末……你把时间花在"描述你想要什么、想让它怎么被造出来"上,而代码几乎只是这个过程里掉出来的木屑。
> 🗣️ "Really what matters is your prompts. And when the next generation of models come out, you can just rerun your prompts again, and then you'll get new code, and the old code didn't really matter." —— Charlie Holtz
> 译:真正重要的是你的 prompt。等下一代模型出来,你只要把 prompt 重跑一遍,就能得到新代码,而旧代码其实根本不重要。
> 🗣️ "The same way you can mod a video game, I want you to be able to mod Conductor, and build in your own workflows a little bit." —— Charlie Holtz
> 译:就像你能给游戏做 mod 一样,我希望你也能给 Conductor 做 mod,把你自己的工作流内建进去。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把自己的开发流程改成"并行编排"**:今天就试着同时开 3+ 个 agent 任务,一个在跑就切下一个,强迫自己从"写代码"切换到"review + 指方向 + 合并"的 CEO 心态。
- [ ] **把团队规范写进 skills 文件 / CLAUDE.md**:用几百行明确写下"我们这里怎么干活"(startup 风格、非企业级),把工程约束前置给 agent,而不是靠事后 review 兜底。
- [ ] **在你的代码/文档里划出 slop-free 区**:标注"人类专属、AI 勿动"的核心 API、契约、UI 决策,防止"烂代码→更烂代码"的恶性循环;其余大块区域再放手给 AI 自由试。
- [ ] **把好习惯做成产品级强制约束**:如果你做的是给别人用的 agent 工具,考虑像 Conductor 那样强制 work tree + PR + merge 流程,用约束而非说教推广最佳实践。
- [ ] **建立信念靠"自己天天吃狗粮"**:在有埋点数据之前,先逼团队每天用自己的产品,用手感快速判断"对不对";刻意领先 frontier 半步,敢于推用户出舒适区。
- [ ] **围绕 prompt 而非代码沉淀资产**:把关键 prompt / 工作流当作可复用、可随模型升级重跑的资产管理起来;把"代码是锯末"当作架构决策的默认假设。

## 🔑 关键术语 / 概念
- **Conductor** — YC S24 出品的 Mac 桌面 app,用于在本机同时编排(orchestrate)多个编程 agent;每个任务是一个 workspace(底层是 git work tree),经 PR → merge 入库。
- **Slop-free zone(无 slop 区)** — 代码库/文档中明确标注"人类专属、每行必须人读"的区域,用来隔离 AI 生成内容的质量污染;slop 指 AI 一把梭产出的低质内容。
- **Token maxing** — 不吝惜花 token 换产出的策略:全开 Fast Mode、think extra hard、high effort;讲者单月最高烧过 $22,000。
- **Fast Mode / dangerously accept all permissions** — Conductor 里默认的高速、全自动批准跑法(非 Claude Code 原生默认),让 agent 不停顿地连续执行。
- **Caveman mode(原始人模式)** — Conductor 里让你退回手敲键盘直接改文件的模式;名字本身是"这是退化操作"的自嘲提醒。
- **Malleable software(可塑软件)** — 软件骨架对所有人一致、但每个用户能像 mod 游戏一样定制/内建自己工作流的形态;讲者视之为软件的未来方向。
- **Code as sawdust(代码即锯末)** — 世界观:代码从"你打造的结构"降级为"描述需求过程中掉出的木屑",真正的资产变成 prompt。
- **Codex / Opus 分工** — Codex 当"劳模"死磕具体问题、敢做大量 tool call;Opus/Claude 更像创作伙伴,适合做新功能、要来回讨论。
- **Context7 MCP** — 讲者常用的、用于给 agent 取最新文档的 MCP 工具。

## 🔖 高价值金句时间戳
- `[04:04]` "But the ideal is you should feel like the CEO of a little company." — 一句话定义 AI 时代的开发者角色:从写代码的人变成管一群 agent 的 CEO。
- `[05:41]` "One core thing is that we always run Cloud and dangerously accept all permissions." — 要 token max、要 agent 连续产出,就得敢开全权限全速跑。
- `[06:16]` "The AI can get in a vicious cycle where it sees bad code, and then it writes more bad code as a result." — 划 slop-free 区的根本理由:AI 会放大你代码库里的熵。
- `[07:08]` "Don't let the AI be your architect." — 核心抽象、API、UI 决策必须人来定,这是本片方法论的题眼。
- `[10:08]` "The way we build conviction is we force ourselves to use it." — 早期产品建立强观点的最朴素办法:自己天天吃狗粮 + gut feel。
- `[14:58]` "Code is almost like sawdust now." — 全片最锋利的世界观:真正的资产是 prompt,代码只是副产物。
- `[16:04]` "The same way you can mod a video game, I want you to be able to mod Conductor." — 可塑软件愿景:让用户像 mod 游戏一样定制自己的工作流。
