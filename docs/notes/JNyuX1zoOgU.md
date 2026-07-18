# 通往 AGI 还缺什么:Demis Hassabis 谈 Agent、深科技创业与下一场科学突破 / Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough

📄 **[点此查看全文转录 / Full transcript »](../transcripts/JNyuX1zoOgU.md)**

> **来源**: [Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough](https://www.youtube.com/watch?v=JNyuX1zoOgU) · Y Combinator · 2026-04-29 · 时长 40:57
> **讲者**: Demis Hassabis(Google DeepMind CEO、2024 诺贝尔化学奖得主,SPEAKER_02) · 主持 Garry Tan(YC CEO,SPEAKER_01) · 现场 YC 广告播报(SPEAKER_00)
> **一句话定位**: 从 DeepMind 一线视角讲清"AGI 还差哪一两块拼图、Agent 真实进度到哪、以及在 2030 AGI 时间线下深科技创业该怎么下注"——对 AI Agent 创始人,这是一份"护城河与时机"的实战地图。

## 🎯 TL;DR(中文核心要点)
- **AGI 只差"一两块拼图"**:大规模预训练 + RLHF + 思维链几乎确定会进入最终架构;真正未解的是**持续学习(continual learning)、长期推理、部分记忆机制、跨场景一致性**。这些能不能靠现有方法 scale 出来,Hassabis 的赌注是 50-50。
- **持续学习是 Agent 无法"fire and forget"的根因**:现在只能把一切塞进 context window("用胶带糊起来"),Agent 不会随所处上下文自适应,所以只能做"任务的局部",做不了完整任务。
- **小模型是核心红利**:Flash 类小模型约达前沿 90-95% 能力、约 1/10 价格;蒸馏还看不到理论上限。对 Agent 而言,速度带来的迭代/协作收益,常常超过那损失的 5-10% 能力。
- **Agent 现在"刚刚开始",别被 40 小时跑一堆 agent 的 demo 迷惑**:真正有价值的用法过去几个月才开始出现;还没出现"vibe coding 做出的 App Store 榜首级 AAA 作品"——差的可能是流程、工具,或"人的手艺、灵魂与品味"。
- **护城河 = AI × 另一门深科技**:纯粹给基础模型套 API 会被下一次模型更新"冲垮";真正防御性的位置是把 AI 与材料/医药/生物等"原子世界"的硬科学结合,需要跨学科团队,没有捷径。
- **给创业者的时机观**:深科技通常是 10 年旅程,而 Hassabis 的 AGI 时间线约 2030——意味着 AGI 会在你旅程"中途"出现,今天就要设计"AGI 到来后能被它放大"的东西。
- **架构判断(对做 Agent 极关键)**:未来不会是"一个巨脑装下一切",而是**强通用工具调用模型 + 把专用系统(如 AlphaFold)当作工具**来编排,专用能力放在独立系统里,避免通用模型能力回退。
- **可被 AI 攻克的科学问题有固定模式**:巨大的组合搜索空间 + 清晰可爬山的目标函数 + 足够数据或能生成 in-distribution 合成数据的模拟器——三者齐备,今天的方法就能"大海捞针"。

## 🧭 适合谁 / 什么时候看
- **正在或打算做 AI Agent / AI-for-Science 创业的技术创始人**:想搞清楚"哪些位置有护城河、哪些会被基础模型碾压"。
- **纠结"套壳 API vs. 深科技"路线的人**:需要一个来自前沿实验室的判断框架。
- **在规划 3-10 年产品/公司的人**:想把"2030 AGI 到来"这件事纳入路线图与架构设计。
- **对 Agent、记忆、持续学习、RL 技术方向感兴趣的工程师**。

## 📝 分段精读

### 1. AGI 还缺什么:持续学习、记忆与"塞进上下文的胶带" / What's Missing & Why Memory Is Unsolved `[01:48–06:14]`
**要点(中文)**: Hassabis 认为当前范式(预训练 + RLHF + 思维链)几乎确定是最终架构的一部分,不会是死胡同;但顶上还缺一两样东西:持续学习、长期推理、部分记忆、跨场景一致性。现在的记忆是"把所有东西暴力塞进上下文窗口",既存无关/错误信息,检索到"当下决策真正相关的那条"本身也有成本。百万 token 上下文对文本够用,但类比人类"工作记忆"其实很粗糙,处理实时视频时一百万 token 只够约 20 分钟——记忆仍是巨大的创新空间。
> 🗣️ "continual learning, some aspects of memory, these are still unsolved, and how to get the systems to be more consistent across the board. I think all of these are going to be required for AGI." —— Demis Hassabis
> 译:持续学习、部分记忆机制,这些仍未解决,还有怎么让系统在各方面更一致。我认为这些都是 AGI 的必要条件。
> 🗣️ "I agree with you, we're kind of using duct tape right now. So shove it all in the context window. Yeah. This seems a bit unsatisfying." —— Demis Hassabis
> 译:我同意你,我们现在基本是用胶带糊——把一切都塞进上下文窗口。这确实让人有点不满意。
> 🗣️ "if you're now trying to try and process live video, and you're just going to naively record all the tokens, then actually a million tokens isn't that much. It's only like 20 minutes." —— Demis Hassabis
> 译:如果你要处理实时视频、还傻乎乎地把所有 token 都记下来,那一百万 token 其实没多少——只有大概 20 分钟。

### 2. RL 与 AlphaGo 的血脉,以及小模型蒸馏红利 / How AlphaGo Shaped Gemini & Why Small Models Are Powerful `[06:14–10:39]`
**要点(中文)**: DeepMind 从第一天起做的就是 agent——能自主达成目标、主动决策与规划的系统(Atari、AlphaGo、AlphaStar)。今天所有带"thinking / 思维链"的前沿模型,本质是 AlphaGo/AlphaZero 思想(含蒙特卡洛搜索)在大规模、更通用形态下的回归,未来几年很多进展会来自重新审视这些老想法。另一条主线是蒸馏:必须先造最大模型拿到前沿能力,但把这份能力快速压进越来越小的模型是 DeepMind 的核心强项;因为要服务十几个十亿级用户产品,天然有极强动机做 Flash/Flash-Lite 这类高效小模型,而且目前看不到蒸馏的理论上限。
> 🗣️ "you can think of a lot of the things we're doing today all the leading models with thinking modes and chain of thought reasoning as aspects of what was sort of pioneered with AlphaGo coming back now" —— Demis Hassabis
> 译:今天所有带思考模式、思维链推理的前沿模型,很多方面都可以看作是当年由 AlphaGo 开创、如今卷土重来的东西。
> 🗣️ "you have to build the biggest models to have the Frontier capabilities but I think one of our biggest strengths has been distilling and packing that power into smaller and smaller models very quickly" —— Demis Hassabis
> 译:你必须造最大的模型才能拿到前沿能力,但我们最大的强项之一,就是把这份能力极快地蒸馏、压进越来越小的模型里。

### 3. 1000x 工程师、边缘模型,与持续学习对 Agent 的意义 / The 1000x Engineer & Continual Learning `[10:39–13:24]`
**要点(中文)**: Garry 指出现在工程师能做 6 个月前 500-1000 倍的工作量。Hassabis 认为小模型价值不只在成本,更在速度带来的快速迭代与人机协作——即便只有前沿的 90-95%,靠迭代速度赚回来的远超那损失的 10%。他还看好边缘/本地模型:为了效率、隐私与安全,音视频等极私密数据在本地处理、必要时再由云端前沿模型编排,是很好的终局(手机、眼镜、家用机器人)。回到 Agent:**缺少持续学习正是当前 Agent 只能做"任务局部"、无法"fire and forget"的关键**——它们无法很好地适应你放入的具体上下文。
> 🗣️ "not having continual learning currently is one of the things holding back agents from doing full tasks ... they don't adapt well with the context that you're in and I think that's the missing piece from them being really kind of fire and forget" —— Demis Hassabis
> 译:当前缺少持续学习,是阻碍 Agent 完成完整任务的原因之一……它们无法很好地适应你所处的上下文,而这正是它们真正做到"发出去就不用管"所缺的一块。
> 🗣️ "you gain back more than the 10 on the iteration speed" —— Demis Hassabis(谈用略逊前沿的快模型)
> 译:你在迭代速度上赚回来的,比那损失的 10% 还多。

### 4. 推理的缺口与 Agent 的真实进度 / Reasoning Gaps & Are Agents Overhyped `[13:24–17:59]`
**要点(中文)**: 推理范式还很"暴力":模型常常"想太多"、陷入思维回路。Hassabis 用和 Gemini 下棋举例——它会看出一步是败招却找不到更好的,于是照走不误,这在精确推理系统里本不该发生;这正是"锯齿状智能(jagged intelligence)"——能解 IMO 金牌题,却在换个问法的小学数学/推理上出错,缺的可能是对自身思考过程的"内省"。谈 Agent:他和 Garry 一致认为"刚刚开始"。真正有价值的用法过去一两个月才浮现;他对"放一堆 agent 跑 40 小时"的产出是否配得上投入表示怀疑;至今没见过"vibe coding 做出的 App Store 榜首 AAA 作品"——缺的可能是流程、工具,或人的手艺、灵魂与品味。他判断未来 6-12 个月会兑现真正价值,而且**先出现的不是全自主,而是这群人以团队方式实现 1000x**。
> 🗣️ "that's why you get this kind of jagged intelligence ... on the one hand it can solve gold medal problems in IMO which is super hard but on the other hand ... it can still make basic elementary math errors if you pose the question in a certain way" —— Demis Hassabis
> 译:所以你会看到这种锯齿状智能——一方面能解超难的 IMO 金牌题,另一方面换个问法它还会犯小学级别的数学错误。
> 🗣️ "I see a lot of people working on uh like setting off you know dozens of agents for like 40 hours but I'm not sure I've seen the output ... quite justify that level of input going in" —— Demis Hassabis
> 译:我看到很多人一口气放出几十个 agent 跑上 40 小时,但我不确定见过哪个产出能配得上这么大的投入。
> 🗣️ "we haven't seen a AAA game that tops the App Store charts that was sort of vibe coded yet ... it still needs craft and you know human sort of soul into it and taste" —— Demis Hassabis
> 译:我们还没见过 vibe coding 做出的、登顶 App Store 的 AAA 游戏……它仍需要手艺,需要人注入的那种灵魂和品味。

### 5. 创造力、开源(Gemma)与多模态 / Creativity, Open Models & Multimodal `[17:59–24:02]`
**要点(中文)**: 创造力的分水岭:AlphaGo 的"第 37 手"很酷,但更高目标是"能不能发明围棋本身"——给一段高层描述(五分钟学会规则、数生才能精通、美学优雅),让系统还给你"围棋"。今天的系统做不到,但可能不是模型不行,而是需要足够有创造力的人"与工具合一"地去激发。开源上,DeepMind 是开源/开放科学的坚定支持者(AlphaFold 免费给全球科学家);Gemma 两周半下载 4000 万次。他强调需要"西方的开源栈"(中国开源模型很强),并透露 Nano/边缘模型选择完全开放——因为它们部署到端侧后本就"暴露",不如索性全开,这在战略上也成立。多模态是 Gemini 被低估的一点:从一开始就多模态虽起步更难,但对世界模型、机器人(Gemini Robotics)、随身助手理解物理世界是长期优势。
> 🗣️ "it's not enough to come up with move 37 ... but can it invent go that's what I want a system that can invent go" —— Demis Hassabis
> 译:光能下出第 37 手还不够……它能不能发明围棋?我想要的是一个能发明出围棋的系统。
> 🗣️ "our Edge models the things we want to use for Android and glasses and robotics ... it's best that they're open models because they're vulnerable anyway on the ... surfaces so they might as well be actually fully open" —— Demis Hassabis
> 译:我们用于 Android、眼镜和机器人的边缘模型,最好做成开放模型——反正它们部署到端侧本就会暴露,那不如索性彻底开放。

### 6. 推理成本、虚拟细胞与"AI 作为科学的终极工具" / Cheap Inference, Virtual Cells & AI for Science `[24:02–30:36]`
**要点(中文)**: 推理不会真正"免费":Jevons 悖论意味着有多少算力就会用掉多少——百万级 agent 蜂群、或单 agent 多方向思考再集成,都会吃掉所有可用推理;即便未来靠聚变/超导让能源近乎零,芯片等物理制造在未来几十年仍是瓶颈,推理仍需高效使用与"配给"。科学是他 30 多年的初心:AI 是"科学的终极工具",DeepMind 的使命两步走——先"解决智能(造 AGI)",再"用它解决其它一切",尤其是能开启全新科学分支的"根节点问题(root node problems)"。AlphaFold 是范式:全球 300 多万研究者在用,据药企朋友说今后几乎每一款新药的发现过程都会用到它。虚拟细胞约 10 年之遥,先从相对自包含的"细胞核"切入;卡点是数据——若能在不杀死活细胞的前提下做纳米级成像,就能把它变成"我们已知如何求解的视觉问题"。
> 🗣️ "I'm not sure inference will ever be essentially free ... we'll just end up using all of us will end up using whatever we can get our hands on" —— Demis Hassabis
> 译:我不确定推理会不会真的近乎免费……最后我们所有人都会把能拿到的算力全部用光。
> 🗣️ "almost every drug discovered from now on will have used AlphaFold at some point in the drug discovery process" —— Demis Hassabis(转述药企高管朋友)
> 译:今后几乎每一款被发现的新药,在药物发现过程中的某个环节都会用到 AlphaFold。
> 🗣️ "if we could image a live cell without killing the cell that would be game-changing ... because then you could convert it into a vision problem which we would know how to solve" —— Demis Hassabis
> 译:如果能在不杀死活细胞的情况下对它成像,那将是颠覆性的——因为这样就能把它变成一个我们已知如何求解的视觉问题。

### 7. 给创始人的建议:深科技护城河、AlphaFold 模式与 AGI 时间线 / Advice for Founders, the Breakthrough Pattern & Building Before AGI `[30:43–40:57]`
**要点(中文)**: Garry 直击要害——"真正推动前沿的创业公司 vs. 只是给基础模型套 API 自称 AI-for-Science"的区别是什么。Hassabis 的答案:护城河在"AI 走向 × 另一门深科技(尤其涉及原子世界的材料/医药)"的甜蜜点,需要跨学科团队,没有捷径,这类位置"不会被下一次基础模型更新冲垮";而且要做自己真正热爱的事,因为一开始"没人相信你"。AlphaFold 式突破有可复用模式:**巨大的组合搜索空间 + 清晰可爬山的目标函数 + 足够数据/能生成 in-distribution 合成数据的模拟器**。科学发现的更高门槛是"提出好假设"而非只求解已知问题(他的"爱因斯坦测试":用 1901 年知识截止训练,能否重现 1905 年狭义相对论)。最关键的架构判断:AGI 时间线约 2030,深科技通常是 10 年旅程,所以 AGI 会在你旅程中途出现——**未来不是一个巨脑装下一切,而是强通用工具调用模型把 AlphaFold 这类专用系统当作独立工具来编排**;今天就该设计"AGI 到来能被它放大"的东西。
> 🗣️ "those kinds of interdisciplinary teams, especially if it involves the world of atoms as well, there's not going to be a shortcut to that ... Those are areas that are pretty safe from just getting swamped by whatever the next update is to the foundation models." —— Demis Hassabis
> 译:这类跨学科团队,尤其涉及原子世界的,没有捷径可走……这些领域相当安全,不会被基础模型的下一次更新直接冲垮。
> 🗣️ "if those things are true ... you can go a long way into tackling and finding the kind of needle in the haystack" —— Demis Hassabis(谈组合搜索空间 + 目标函数 + 数据/模拟器三要素)
> 译:如果这三点都成立……你就能走很远,去攻克并找到那根大海里的针。
> 🗣️ "much better, I think, is to have really good general purpose tool usage models that ... could even train those specific tools, but they would be in a separate system" —— Demis Hassabis
> 译:我认为更好的方式,是拥有非常强的通用工具调用模型……它甚至可以去训练那些专用工具,但这些工具会存在于独立的系统中。
> 🗣️ "depending on what your AGI timeline is ... mine's like 2030 or something like this, then if you start off on a deep tech journey today ... you have to just consider AGI appearing in the middle of that journey." —— Demis Hassabis
> 译:取决于你的 AGI 时间线……我的大概是 2030,如果你今天启动一段深科技旅程,就必须考虑到 AGI 会在这段旅程中途出现。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **不要只做"基础模型套壳"**:把产品定位在"AI × 一门你有专长的深领域(医疗/材料/生物/工业/金融等原子世界)",这是唯一"不被下次模型更新冲垮"的防御位。若你缺领域深度,优先组建"ML + 领域"双专长的联合创始团队。
- [ ] **把架构设计成"通用工具调用模型 + 专用系统当工具"**:不要幻想单一巨模型包办一切;把你的专有能力/数据做成可被通用 Agent 编排调用的独立工具或子模型,预留"AGI 到来后即插即用被放大"的接口。
- [ ] **围绕"持续学习/记忆缺口"做产品级补丁并沉淀护城河**:既然模型层短期无法自适应上下文,就在应用层做好上下文管理、检索相关性(不是无脑塞满 context)、per-user/per-task 的学习与记忆,这正是当前 Agent 从"局部好用"走向"fire and forget"的价值缺口。
- [ ] **默认用"够好且快"的小模型,把省下的能力换成迭代速度**:对协作式/交互式 Agent,90-95% 前沿能力 + 10 倍速度/成本通常净赚;把前沿大模型留给必须的编排与难推理环节。
- [ ] **警惕"堆 agent 数量/时长"的虚荣指标**:不要因为能"跑 40 小时、几十个 agent"就上,先用真实产出/ROI 验证;找到过去几个月才成熟的"真正加价值"的具体工作流再规模化。
- [ ] **用"AlphaFold 三要素"筛选你的核心技术赌注**:目标问题是否有(1)巨大组合搜索空间、(2)清晰可爬山的目标函数、(3)足够数据或能造 in-distribution 合成数据的模拟器?三者齐备,今天的方法就能出成果;缺目标函数或数据,先补这两块。
- [ ] **按"2030 AGI、10 年深科技"做路线图**:明确写下"若 AGI 在第 3-5 年出现,我的产品/数据/客户关系/物理资产如何被它放大而非替代",据此选择今天要积累的资产(专有数据、真实世界接入、工具化能力)。

## 🔑 关键术语 / 概念
- **Continual learning(持续学习)** — 模型在部署后持续吸收新知识而不必重训、且不遗忘旧知识的能力;Hassabis 认为这是 Agent 无法做完整任务、无法"fire and forget"的关键缺口。
- **Jagged intelligence(锯齿状智能)** — 同一模型能力极不均衡:能解 IMO 金牌题,却在换个问法的基础数学/推理上出错;疑似缺"对自身思考过程的内省"。
- **Distillation(蒸馏)** — 把大模型能力快速压入更小模型(如 Flash/Flash-Lite/Nano/Gemma)的技术;DeepMind 视为核心强项,目前看不到理论上限。
- **Root node problems(根节点问题)** — 一旦解决就能解锁整片新科学分支的基础性问题(如蛋白质结构预测);AlphaFold 是范式,DeepMind 使命第二步"解决其它一切"即指攻这类问题。
- **General-purpose tool-use + specialized tools(通用工具调用 + 专用工具)** — Hassabis 预判的 AGI 架构:不是单一巨脑,而是强通用模型把 AlphaFold 等专用系统当独立工具编排,避免通用模型能力回退。
- **Move 37 / "invent Go"** — AlphaGo 名局中的"神之一手";Hassabis 用"能否发明围棋本身"作为真创造力(而非模式匹配/外推)的更高标尺。
- **Einstein test / 1901→1905** — 用 1901 年知识截止训练系统,看它能否独立重现 1905 年狭义相对论,作为"AI 能否做真正原创科学发现"的判定测试。
- **Jevons paradox(杰文斯悖论)** — 效率提升反而拉高总消耗;Hassabis 用它论证推理不会真正免费——算力越便宜,agent 蜂群等用法会把它全部吃掉。

## 🔖 高价值金句时间戳
- `[02:42]` "there still might be one or two things missing on top of what we already know works ... my betting is about 50-50" — AGI 只差一两块拼图,能否靠 scale 解决是 50-50,别把时间线当确定性。
- `[12:46]` "not having continual learning currently is one of the things holding back agents from doing full ... tasks" — 记住 Agent 当前天花板的技术根因:应用层的记忆/上下文工程就是你的机会。
- `[16:48]` "we haven't seen a AAA game that tops the App Store charts that was sort of vibe coded yet" — Agent"刚刚开始"的最好试金石:别用 demo 自我感动,看有没有真正登顶的产出。
- `[31:30]` "Those are areas that are pretty safe from just getting swamped by whatever the next update is to the foundation models." — 一句话定义护城河:AI × 深科技,而非套壳 API。
- `[33:53]` "massive combinatorial search space ... a clear objective function ... enough data and or simulator" — 可复用的"能被 AI 攻克的问题"三要素清单,拿去筛你的技术赌注。
- `[39:30]` "you have to just consider AGI appearing in the middle of that journey" — 用 2030 AGI 时间线倒推今天该积累什么资产。
- `[40:10]` "much better ... is to have really good general purpose tool usage models ... but they would be in a separate system" — 对做 Agent 最直接的架构指引:通用编排 + 专用工具分离。
