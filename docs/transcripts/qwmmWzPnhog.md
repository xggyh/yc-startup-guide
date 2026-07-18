# 全文转录 · 我们都对 Claude Code 上瘾了:coding agent 时代的创业启示

> ▶ [YouTube](https://www.youtube.com/watch?v=qwmmWzPnhog) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/qwmmWzPnhog.md) &nbsp;·&nbsp; We're All Addicted To Claude Code

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** I feel like when I'm using Cloud Code, it's like, oh, I feel like I'm flying through the code.

> 我觉得用 Cloud Code 的时候,就像是,哦,感觉自己在代码里飞驰。

[00:03] **SPEAKER_01:** When it's in your CLI, this thing can debug nested, delayed jobs like five levels in and figure out what the bug was and then write a test for it and it never happens again. This is insane.

> 当它跑在你的命令行里时,这东西能调试嵌套了大概五层深的延迟任务,搞清楚 bug 在哪,然后为它写一个测试,从此再也不会出现。这太疯狂了。

[00:14] **SPEAKER_02:** I think everyone who's experimenting with this stuff on like a hobbyist level or at like a very small startup, they're just pushing the coding agents as far as they can go. Because it's like, you don't really have time to figure out anything else. Like as a startup, you have limited runway. You're just going to orient around speed.

> 我觉得每一个在业余爱好层面、或者在很小的创业公司里折腾这些东西的人,都在把编码 agent 逼到极限。因为你根本没时间去研究别的东西。作为一家创业公司,你的资金跑道有限,你只会围绕速度来组织一切。

[00:27] **SPEAKER_02:** I think at a bigger company, you have a lot more to lose.

> 我觉得在更大的公司里,你要失去的东西就多得多了。

[00:30] **SPEAKER_00:** What are some of the tips to become a top 1% user of coding agents?

> 要成为编码 agent 使用者中前 1% 的人,有哪些技巧?

[00:35] **SPEAKER_01:** Yeah, what's your stack?

> 是啊,你的技术栈是什么?

[00:37] **SPEAKER_03:** Hey everyone, welcome back to another episode of The Light Cone. Gary, are you ready to record?

> 大家好,欢迎回到又一期《光锥》(The Light Cone)。Gary,准备好录制了吗?

[00:49] **SPEAKER_01:** I'm in plan mode right now, but okay, yeah, I guess it's time. Sorry about that. Well, welcome to another episode of The Light Cone. And today we have an incredible guest, Kelvin French-Owen.

> 我现在正处在 plan 模式里,不过好吧,行,我想是时候了。抱歉。那么,欢迎来到又一期《光锥》。今天我们请到了一位了不起的嘉宾,Kelvin French-Owen。

[01:00] **SPEAKER_01:** He's one of the first people to create codecs at OPC. OpenAI. And before that, he started Segment, which is a multi-billion dollar company that got to a very successful exit. Kelvin, welcome back.

> 他是在 OpenAI 最早打造 Codex 的人之一。在那之前,他创办了 Segment,一家市值数十亿美元、成功退出的公司。Kelvin,欢迎回来。

[01:13] **SPEAKER_02:** Thanks for having me.

> 谢谢你们邀请我。

[01:14] **SPEAKER_01:** I guess what a crazy time for all of us. I recently got very, very addicted to Cloud Code. And I would describe it as like 10 years ago, I was a marathon runner and I loved doing it. And then I suffered a catastrophic knee injury, which is called manager mode.

> 我想对我们所有人来说,这都是一个疯狂的时代。我最近变得非常非常沉迷于 Cloud Code。我会这样形容它:十年前,我是个马拉松跑者,我热爱跑步。然后我遭遇了一次灾难性的膝盖损伤,那个伤叫做「管理者模式」。

[01:33] **SPEAKER_01:** And I... I stopped coding, which is tragic and horrible, but now the last nine days have been like this incredible unlock of all the things I remember being able to do.

> 于是我……我不再写代码了,这很悲剧、很可怕,但如今过去这九天,就像是一次不可思议的解锁,让我重新找回了记忆中自己曾经能做到的所有事情。

[01:46] **SPEAKER_01:** And it's like, you know, I got a new total knee replacement and actually it's a bionic knee and it allows me to run five times faster. What's your take on it? Because you're, I mean, right out there at the forefront of it, I mean, Codex pioneered all of the...

> 就好像,你知道,我换了一个全新的全膝关节,而且其实是个仿生膝盖,让我能以五倍的速度奔跑。你对此怎么看?因为你,我是说,你正处在最前沿,Codex 开创了所有那些……

[02:02] **SPEAKER_01:** A lot of the ideas that now like... Yeah.

> 很多如今……对。

[02:04] **SPEAKER_01:** Codex still uses and Codex is still evolving too.

> Codex 仍在使用、并且 Codex 自己也还在不断演进的想法。

[02:07] **SPEAKER_02:** For brief context, when I was at OpenAI, I was working on the Codex web product. At the time, Cursor was out in the market and they had kind of built this shim around, I think it was Sonnet 3.5, and it was able to work in your IDE. FOD code had just come out and it was working as a CLI.

> 简单交代一下背景,我在 OpenAI 的时候,是做 Codex 网页版产品的。当时 Cursor 已经上市了,他们大概是围绕 Sonnet 3.5 搭了一层封装,能在你的 IDE 里工作。Claude Code 刚刚发布,作为一个命令行工具运行。

[02:25] **SPEAKER_02:** And we kind of had this idea like, hey, in the future, coding is really going to feel more like talking to a coworker. Like you're going to send off a question. And then they'll go off and do something and come back to you with a PR. And so that's where we started with this WebView and that's what we were building.

> 我们当时有这样一个想法:嘿,未来写代码真的会更像是在跟一位同事对话。你抛出一个问题,然后他们去做点什么,再带着一个 PR 回来找你。所以我们就是从这个网页视图起步的,那也是我们当时在做的东西。

[02:41] **SPEAKER_02:** I think directionally, that's still kind of correct for where things should go. But obviously now everyone is coding with CLIs instead. Like they're using those tools a lot more, whether it's Cloud Code or whether it's Codex. And I think at least for me, kind of the lesson in that is I think in some sense, you're right that like everyone is going to become a manager in the future, or at least that's my hot take.

> 我觉得在方向上,这对于事情该往哪走仍然大致是对的。但显然现在大家都改用命令行来写代码了。他们用那些工具用得多得多,不管是 Cloud Code 还是 Codex。而且至少对我来说,这里面的教训是,我觉得从某种意义上你说得对,每个人未来都会变成管理者,或者至少这是我的一个大胆观点。

[03:02] **SPEAKER_02:** But in order to get there, there are steps along the way. And you have to really build a lot of trust in the model and understand what it's doing.

> 但为了走到那一步,途中还有一些步骤。你得真正对模型建立起大量的信任,理解它在做什么。

[03:08] **SPEAKER_01:** You recently came over to Cloud Code. What's the transition been like in terms of as using it as your, you know, one of your

> 你最近转到了 Cloud Code。把它作为你的主力工具之一来用,这个过渡体验是怎样的?

[03:15] **SPEAKER_02:** stacks? Yeah, yeah. So Cloud Code is certainly my kind of like daily driver today. And honestly, this is switched every few months.

> 是啊,是啊。所以 Cloud Code 如今确实是我的日常主力工具。老实说,这东西每隔几个月就会换一次。

[03:23] **SPEAKER_02:** For a while, I was deeply in Cursor. I think their new model, which is really fast, is actually quite good. Then I kind of moved over to Cloud Code, especially with Opus. Cloud Code is a really interesting product.

> 有一阵子,我深度用 Cursor。我觉得他们那个非常快的新模型其实相当不错。后来我就转向了 Cloud Code,尤其是配合 Opus。Cloud Code 是个非常有意思的产品。

[03:33] **SPEAKER_02:** And I think it's underrated how good the both product and model are working together. If you study them closely, I think one of the things that Cloud Code does in particular that's really amazing is split up context well. And so if you look at, I don't know, things like skills or subagents, like when you ask Cloud Code to do something, it will typically spawn and explore subagent or like multiple ones. And basically each of those are running haiku to traverse the file system and kind of like explore what's there.

> 我觉得它的产品和模型协同得有多好这一点被低估了。如果你仔细研究它们,我认为 Cloud Code 尤其了不起的一点,是它把上下文拆分得很好。你看看那些,比如 skills 或者 subagents,当你让 Cloud Code 做一件事时,它通常会派生出一个探索型 subagent,或者好几个。基本上每一个都在运行 Haiku 来遍历文件系统,去探索那里有什么。

[04:03] **SPEAKER_02:** And they're doing it in their own way. They're doing it in their own context window. And I think Anthropic has kind of like figured something out here around given a task. Does that task fit in the context window or should I actually like split it into many more?

> 而且它们是用自己的方式来做的,在自己独立的上下文窗口里做。我觉得 Anthropic 在这里搞明白了一件事:给定一个任务,这个任务是能塞进一个上下文窗口,还是我其实应该把它拆成很多个?

[04:15] **SPEAKER_02:** And the models are like insanely good at this, which I think gives them really good results.

> 模型在这件事上强得离谱,我觉得这给了它们非常好的结果。

[04:19] **SPEAKER_00:** And I think the fascinating thing is because it's on the terminal is the purest form for composable atomic integrations. Because if you came from ID first world, which is where Cursor was, and I suppose Codex too, this concept of. Finding the context more free form wouldn't come out so natural, right? Because which is so unique.

> 而我觉得最迷人的一点是,因为它在终端上,这是可组合的原子化集成最纯粹的形态。因为如果你来自一个 IDE 优先的世界——那正是 Cursor 所在的地方,我想 Codex 也是——这种以更自由的形式去寻找上下文的概念就不会那么自然地冒出来,对吧?这一点太独特了。

[04:41] **SPEAKER_02:** Yeah. And I personally, I was surprised, I don't know how you all feel, but I was surprised

> 是啊。而且我个人,我很意外,不知道你们怎么想,但我很意外……

[04:45] **SPEAKER_04:** that like CLIs. It's like a weird retro future that like the CLIs, which are the technology from 20 years ago have somehow beaten out all the actual IDEs, which were supposed to be the future.

> 意外的是命令行。这就像一种奇怪的复古未来感,那些命令行——二十年前的技术——竟然不知怎么就打败了所有真正的 IDE,而 IDE 本应是未来的方向。

[04:56] **SPEAKER_02:** A hundred percent. Yeah. And I think it's important actually to Cloud Code that it's not an IDE because it sort of distances you from the code. It's being written.

> 百分之百同意。是啊。而且我觉得对 Cloud Code 来说,它不是一个 IDE 这一点其实很重要,因为它把你和正在被写出来的代码拉开了一点距离。

[05:04] **SPEAKER_02:** Like IDEs are all about exploring files, right? And you're like trying to keep all the state in your head and understand what's going on. But the fact that a CLI is like a totally different thing means that they have a lot more freedom in terms of how it feels. And I don't know about you, but I feel like when I'm using Cloud Code, it's like, oh, I feel like I'm flying through the code.

> 你看 IDE 全都是围绕浏览文件的,对吧?你在努力把所有状态都装在脑子里,理解到底发生了什么。但命令行是个完全不同的东西,这一事实意味着它们在「感觉」上有大得多的自由度。我不知道你们怎么样,但我觉得用 Cloud Code 的时候,就像,哦,我感觉自己在代码里飞驰。

[05:20] **SPEAKER_02:** You know, it's like, there's all sorts of things going, there's like little progress indicators. It's kind of like giving me status updates, but like the code that's being written is not the front and center thing.

> 你知道,就是会有各种各样的东西在动,有各种小小的进度指示器。它有点像在给我状态更新,但正在被写出来的代码并不是那个摆在最正中央的东西。

[05:28] **SPEAKER_01:** I mean, dev environments are so messy. I mean, I really like how clean. Yeah. How clean a sandbox conceptually is in Codex.

> 我是说,开发环境太乱了。我真的很喜欢那种干净。是啊,Codex 里那种沙盒在概念上有多干净。

[05:37] **SPEAKER_01:** But then I just ran into all these crazy issues, like trying to do, you know, run just simple testing, right? It needs to access Postgres and then it can't do it, or, you know, my codex.md ended up being 20 lines long and even then it didn't work. When it's in your CLI, it could just access your development database.

> 但后来我就撞上了各种疯狂的问题,比如想跑,你知道,就跑个简单的测试,对吧?它需要访问 Postgres,然后它做不到;或者,你知道,我的 codex.md 最后写到了 20 行长,即便如此还是没用。而当它在你的命令行里时,它就能直接访问你的开发数据库。

[05:56] **SPEAKER_01:** I mean, I'm not sure if I'm supposed to do this, but I've actually also had it access my production database. Yeah. Yeah. Yeah.

> 我是说,我不确定我是不是该这么做,但我其实还让它访问过我的生产数据库。是啊。是啊。是啊。

[06:03] **SPEAKER_01:** It can just do it. It's like, yeah. Okay. Here, like I looked into it and I think this happened and I'm going to debug this, you know, concurrency issue.

> 它就是能做到。就像,是啊。好的。这样,我查了一下,我觉得是发生了这个情况,我要来调试这个,你知道,并发问题。

[06:10] **SPEAKER_01:** And I was like, oh my God, like this thing can debug nested delayed jobs, like five levels in and figure out what the bug was and then write a test for it and it never happens again. This is insane.

> 我当时就想,我的天,这东西能调试嵌套了大概五层深的延迟任务,搞清楚 bug 是什么,然后为它写一个测试,从此再也不会出现。这太疯狂了。

[06:22] **SPEAKER_02:** Yeah. And I think that distribution mode is frankly underrated. Like thinking about a cursor or a cloud code or a codex CLI, the fact that you can just download it and use it without having to get it. Any permissions or anything makes a huge difference.

> 是啊。而且我觉得那种分发模式坦白说被低估了。想想 Cursor、Cloud Code 或者 Codex CLI,你可以直接下载下来就用,不需要去获得任何权限之类的,这一点带来了巨大的差别。

[06:35] **SPEAKER_02:** And actually I was playing around with a product the other day where you download a desktop app and then it execs the cloud code that you have running on your laptop and uses that and communicates back via an MCP server to the desktop product. And it's like, this is a very interesting way of now starting to work with your laptop where you don't have to get anyone's permission to do it. You just download the product and go.

> 其实前几天我在玩一个产品,你下载一个桌面应用,然后它去执行你笔记本上正在运行的 Cloud Code,用它来干活,再通过一个 MCP server 把结果传回桌面产品。这就像是一种非常有意思的、开始跟你笔记本协作的新方式,你不需要征得任何人的许可,直接下载产品就能上手。

[06:57] **SPEAKER_01:** Yeah. I was looking at like New Relic has an MCP, but you know, Sentry. You can like copy markdown, but like it's like an auto bug fixer basically. It's right there.

> 是啊。我当时在看,比如 New Relic 有个 MCP,不过还有 Sentry。你可以复制 markdown,但它基本上就像一个自动修 bug 的工具,就摆在那儿。

[07:06] **SPEAKER_01:** Yeah.

> 是啊。

[07:07] **SPEAKER_04:** It's super interesting that in a world where things are changing so fast, you really want your pride to have a bottoms up distribution, not top down because like top down is like just too slow. Like the CTO of a company is going to be like, have all these concerns about security and privacy and what if the control exactly versus like the engineers just like install the thing and start using it. Like this thing is amazing.

> 非常有意思的一点是,在一个变化如此之快的世界里,你真的会希望你的产品走自下而上的分发,而不是自上而下,因为自上而下就是太慢了。一家公司的 CTO 会有一堆关于安全、隐私、万一失控怎么办的顾虑——正是这样;相比之下,工程师们就是直接把东西装上开始用。就像,这玩意儿太棒了。

[07:26] **SPEAKER_02:** Yeah. I think that's right. The one thing I do struggle with, I mean, I'm like a B2B enterprise guy generally. Yeah.

> 是啊。我觉得这说得对。我唯一比较纠结的一点是,我是说,我整体上是个做 B2B 企业级的人。是啊。

[07:31] **SPEAKER_02:** But I feel like there's some amount of moat that happens when you do that top down sale and there's got to be some company who manages to crack it where it's like, oh, this is the thing that everyone has access to. Maybe individual people can take it up.

> 但我觉得当你走自上而下的销售时,会形成某种护城河,而且总得有一家公司设法把它攻克,让它变成那种「哦,这是人人都能用上的东西」。也许个人可以自己先用起来。

[07:44] **SPEAKER_01:** That was the original Netscape Navigator. It was free for non-commercial use and then people would just download it and use it for commercial use and then they could just track down the IPs and figure out exactly how many clients were in all of these different companies and say, you should pay for this. You're in violation, but all you have to do is buy a license. Yeah, yeah.

> 那正是当年最初的 Netscape Navigator。它对非商业用途免费,然后人们就直接下载下来用于商业用途,接着他们就能追踪那些 IP,精确算出这些不同公司里各有多少客户端,然后说,你应该为此付费。你违规了,不过你只需要买个许可证就行。是啊,是啊。

[08:05] **SPEAKER_01:** So I'd be curious if you could do that work again here. I mean, your point about distribution is very interesting because now people are probably just making architecture decisions about what to use directly in Cloud Code. They might not even know what analytics to use and it's like, oh yeah, as long as Cloud Code says use PostHog, they're using PostHog.

> 所以我很好奇,你能不能在这里再把那套活儿重新做一遍。我是说,你关于分发的那个观点非常有意思,因为现在人们很可能直接就在 Cloud Code 里做架构决策,决定用什么。他们甚至可能都不知道该用什么分析工具,就像,哦对,只要 Cloud Code 说用 PostHog,他们就用 PostHog。

[08:27] **SPEAKER_02:** 100%. Yeah. Yeah. I was talking about their GEO strategy.

> 百分之百。是啊。是啊。我之前在聊他们的 GEO 策略。

[08:32] **SPEAKER_02:** This is like the generative optimization or how you show up in chatbots. And what he was saying is funny is one of their competitors had put together a top five list of tools in their category that you should be using and of course, their tool is ranked at the top of this top five list and any human looking at this would be like, oh, this is so obviously biased. It's like the top tool is the one that's in the domain, but the LLMs get fooled and they're pulling together a bunch of contacts and they're saying like, oh, this is the top and then they'll just recommend it. So I think, yeah, if you're selling a developer tool, like having good docs that are out there, like having social proof, like maybe being posted on Reddit a little bit more, all of that helps your case tremendously.

> 这就像是生成式优化,也就是你如何在聊天机器人里出现。他说的有意思的一点是,他们的一个竞争对手整理了一份「你该用的本品类前五工具」榜单,当然,他们自家的工具在这份前五榜单里排在第一,任何人看了都会觉得,哦,这也太明显地有偏向性了。就是那个排第一的工具正好是发布这份榜单的那家。但大语言模型会被骗到,它们把一堆内容拼在一起,然后说,哦,这是最好的,接着就直接推荐它。所以我觉得,是啊,如果你在卖一个开发者工具,拥有好的、公开可查的文档,拥有社会证明,也许在 Reddit 上多被人发一发,所有这些都会极大地帮到你。

[09:09] **SPEAKER_00:** Which is why I think a lot of the open source projects have taken off a lot more. I think one of the examples is Supabase actually, which really took off last year. And part of it is because they have such a good open source documentation, how to set up a bunch of stuff. Whenever someone asks how to set up anything that you need, some sort of backend, Firebase, whatever.

> 这也是为什么我觉得很多开源项目起飞得快得多。我觉得一个例子其实就是 Supabase,它去年真的火起来了。部分原因是他们有非常好的开源文档,教你怎么搭建一堆东西。每当有人问怎么搭建任何你需要的东西——某种后端、Firebase 之类的——

[09:29] **SPEAKER_00:** Yeah. That type of transaction. The default answer from all the LLMs is actually Supabase. I was just trying some of these questions that comes from that.

> 是啊,那类事情。所有大语言模型给出的默认答案其实就是 Supabase。我刚才就在试一些出自那儿的问题。

[09:38] **SPEAKER_01:** The thing is it's winning the internet. And it was like that before when it was like Stack Overflow, searching Google. And then now that nobody uses Google anymore, it's like crazy. It's kind of the same deal.

> 关键在于它正在赢得整个互联网。以前也是这样,当年是 Stack Overflow、用 Google 搜索。而现在,没人再用 Google 了,就很疯狂。这基本上是同一回事。

[09:52] **SPEAKER_02:** I will say it does help open source disproportionately, I would say. I don't know if you all saw there was a Ramp blog post that they recently published about building their own coding agent. And they were mentioning that they use OpenCode as a harness because the model can look and see the source code and understand how it's working. And I do this all the time with open source projects.

> 我得说,我认为它确实不成比例地帮到了开源。不知道你们有没有看到,Ramp 最近发过一篇博客,讲他们打造自己的编码 agent。他们提到,他们用 OpenCode 作为 harness,因为模型可以查看源代码、理解它是怎么工作的。而我一直在开源项目上这么做。

[10:09] **SPEAKER_02:** I'll clone the repo and then spin up Codex or Cloud Code and be like, hey, give me a walkthrough of what's going on here. It's really useful.

> 我会把仓库克隆下来,然后起一个 Codex 或者 Cloud Code,说,嘿,给我讲一遍这里到底是怎么回事。这非常有用。

[10:16] **SPEAKER_00:** What do you think are some of the tips for anyone that wants to build a coding agent since you've done it a lot? What are some now lessons that you learned that you want to share?

> 既然你做过很多次,那你觉得对任何想打造编码 agent 的人来说,有哪些技巧?你学到了哪些现在想分享的经验教训?

[10:25] **SPEAKER_02:** I mean, I think the number one thing is managing context well. Basically, we kind of had a checkpoint for, I think it was 03, one of the reasoning models. And then we did a bunch of fine tuning on it in reinforcement learning where it's like, oh, you're given a bunch of questions to solve these coding problems or fix tests or whatever or implement a feature. And then the model was RL'd to respond to those.

> 我是说,我觉得第一位的就是把上下文管理好。基本上,我们当时有一个检查点,我想是 o3,一个推理模型。然后我们在它之上做了大量的强化学习微调,就是,哦,给你一堆题目去解决这些编码问题、修测试之类的、或者实现一个功能。然后模型被用 RL 训练来回应这些。

[10:48] **SPEAKER_02:** And so I think most people are not going to be doing that, right? But the things that you can do are figure out like, hey, what context should I be supplying to this agent to get the best possible result? Yeah. So in code, if you watch it working, it's like, oh, I'm going to like spawn a bunch of these Explorer sub-agents.

> 所以我觉得大多数人不会去做那件事,对吧?但你能做的事情是搞清楚,嘿,我该给这个 agent 提供什么样的上下文才能得到尽可能好的结果?是啊。所以在 Codex 里,如果你看着它工作,就像,哦,我要派生出一堆这种探索型 subagent。

[11:03] **SPEAKER_02:** They will like search for different patterns in the file system. They will come back, they will have this context, they'll summarize it for me, and then I'll have some place to go. It's interesting watching like different agents structure this context. Like I think Cursor takes an approach where they actually do semantic search, where they embed everything and figure out like, hey, what query is closest to this?

> 它们会在文件系统里搜索不同的模式,会带着结果回来,会有这些上下文,会为我总结出来,然后我就有了个可以着手的地方。看着不同的 agent 组织这些上下文很有意思。比如我觉得 Cursor 采用的做法是,他们其实做语义搜索,把所有东西都嵌入向量,然后搞清楚,嘿,哪个查询跟这个最接近?

[11:25] **SPEAKER_02:** If you look at a codex or a cloud code, they actually just use like grep. Yeah. And I think that works because- It works really well. It works really well.

> 而如果你看 Codex 或者 Cloud Code,它们其实就是用 grep。是啊。我觉得这之所以行得通是因为——它效果非常好。它效果非常好。

[11:32] **SPEAKER_02:** Yeah. It works very well because code is very context dense. Like if you think about lines of code, it's like each line is probably less than 80 characters. There's not a lot of like big like data blobs or like JSON in your code base.

> 是啊。它效果非常好,因为代码的上下文密度非常高。你想想代码的行,每一行大概不到 80 个字符。你的代码库里没有很多那种大块的数据团、或者大段的 JSON。

[11:44] **SPEAKER_02:** Maybe there's some, but not a lot. You can respect gitignore to figure out and like filter out stuff that's just not relevant or is like packaged. And you can use grep and ripgrep to like find context around the code, which probably gives you a good sense for what that code is doing. And you can navigate the file folder structure.

> 也许有一些,但不多。你可以遵循 gitignore 来搞清楚、过滤掉那些根本不相关、或者是打包出来的东西。你可以用 grep 和 ripgrep 去找代码周围的上下文,这大概能让你很好地把握那段代码在做什么。而且你还可以在文件夹结构里导航。

[11:58] **SPEAKER_04:** Yeah. Which is really, really good at admitting very complicated grep expressions that would like torture a human.

> 是啊。它非常非常擅长凭空写出那种会把人折磨死的、极其复杂的 grep 表达式。

[12:04] **SPEAKER_02:** Yes. Yeah. Yeah. Yeah.

> 没错。是啊。是啊。是啊。

[12:08] **SPEAKER_02:** This is like the RL in practice. Yes. Yeah. And so I think all of that, like if you're trying to build a system, well, I'm trying to build systems that integrate agents for non-coding work, I think you can learn a lot of those lessons and say like, hey, how do I get my data in the format that is like maybe closest to code where the model can like peek and look at like areas around it and get the right structured data.

> 这就是 RL 在实践中的体现。是的。是啊。所以我觉得所有这些,如果你想搭一个系统——好吧,我在尝试搭建那种为非编码工作集成 agent 的系统——我觉得你可以学到很多这样的经验,然后说,嘿,我怎么把我的数据弄成那种也许最接近代码的格式,让模型能够窥探、查看它周围的区域,拿到正确的结构化数据。

[12:27] **SPEAKER_00:** Yeah. So this is how a lot of the superpowers for the best coding agents is context engineering. What are some of the tips to become a top 1% user of coding agents?

> 是啊。所以这就是最好的编码 agent 的很多超能力所在——上下文工程。要成为编码 agent 使用者中前 1% 的人,有哪些技巧?

[12:39] **SPEAKER_02:** Yeah.

> 是啊。

[12:40] **SPEAKER_00:** What's your stack? Yeah. What do you do to be so productive with it?

> 你的技术栈是什么?是啊。你做了什么才能用它如此高产?

[12:43] **SPEAKER_02:** One is if you're able to use just generally far less code in plumbing. So a lot of what I do is like deploy stacks on like Vercel or Next.js or like Cloudflare workers where there's kind of like already a bunch of boilerplate like taking care of for you. You don't really have to think that much about like, hey, I need to stand up like all these different services and deal with like service discovery and like registering on like some sort of central endpoint or like all these databases.

> 其一是,如果你能总体上少写很多「管道胶水」代码。所以我做的很多事情,是在 Vercel、Next.js 或者 Cloudflare Workers 上部署技术栈,那里已经帮你搞定了一大堆样板。你其实不太需要去操心,嘿,我得把这一堆不同的服务立起来、处理服务发现、在某个中心端点上注册、或者搞这些数据库之类的。

[13:07] **SPEAKER_02:** It's like, oh, like everything is pretty roughly defined in this like one or 200 lines of code. I tend to operate more towards microservices for that as well, or like individual packages that are fairly well structured. I think it's also worth knowing like what the LLM superpowers are like in general coding agents are. I think.

> 就像,哦,所有东西基本上都相当粗略地定义在这一两百行代码里。为此我也倾向于更多地采用微服务,或者结构相当良好的独立包。我觉得还值得知道大语言模型的超能力大致是什么、通用编码 agent 的超能力是什么。我觉得——

[13:27] **SPEAKER_02:** I think I just tweeted about this. They're like super persistent, so they will keep going no matter what. They end up typically just making more of whatever's there. So if you're trying to direct them to do something, it's worth like, I mean, I can pick on OpenAI slightly.

> 我觉得我刚发了一条关于这个的推文。它们超级执着,所以它们无论如何都会一直干下去。它们最终通常就是把已经存在的东西再多造一些。所以如果你想引导它们做某件事,值得——我是说,我可以稍微拿 OpenAI 开个玩笑。

[13:43] **SPEAKER_02:** In this example, OpenAI has like a giant monorepo. It's been there for a few years now and has like, I don't know, thousands of engineers who are committing. Some of those engineers are like super senior meta folks who came in and are like, know exactly how to write production code. Some are like new PhDs.

> 以这个为例,OpenAI 有一个巨大的 monorepo。它已经存在好几年了,有,我不知道,成千上万的工程师在往里提交代码。其中一些工程师是超级资深的从 Meta 来的人,他们进来时就完全知道怎么写生产级代码。有些则是刚毕业的博士。

[13:59] **SPEAKER_02:** It's like a pretty wide range. And so the LLM will pick up different things depending on where you direct it. I think there's a lot of room actually for coding agents to figure out like, what is the like optimal type of code that we should produce? I mean, obviously giving the model a way to check its work helps improve performance drastically.

> 跨度相当大。所以大语言模型会根据你把它引向哪里而学到不同的东西。我觉得编码 agent 其实有很大的空间去搞清楚,什么才是我们该产出的最优类型的代码?我是说,显然给模型一个检查自己工作的手段,能极大地提升表现。

[14:17] **SPEAKER_02:** So the more that you can run tests in Lint, CI, et cetera. Personally, I also use code review bots pretty aggressively. I know. YC company is really good.

> 所以你越是能跑测试、跑 Lint、跑 CI 等等,越好。我个人也相当激进地用代码审查机器人。我知道有个 YC 公司做得很好。

[14:28] **SPEAKER_02:** I use the cursor bug bot has gotten quite good and I actually like Codex for code review as well. I find it does a very good job on correctness. So those are all things that like the agents are good at and they're excellent exploring the code base too. I think areas where they don't do well, they make more.

> 我用 Cursor 的 bug bot,它已经变得相当好了,而且我其实也喜欢用 Codex 做代码审查。我发现它在正确性上做得非常好。所以这些都是 agent 擅长的事情,它们在探索代码库上也非常出色。我觉得它们不擅长的地方是——它们会「多造」。

[14:44] **SPEAKER_02:** If your goal is not to make more, they'll like often duplicate code and like spend a bunch of time reimplementing things that like, you're like, oh, of course you didn't want to do this. I think context poisoning is a real thing. Where it kind of like goes down one loop and it will continue because it has this persistence, but it's referring back to tokens, which are like not right in terms of pursuing a solution. And so one thing that I often do is like very actively clear context.

> 如果你的目标不是多造,它们往往会重复代码、花一大堆时间去重新实现一些东西,你会想,哦,你当然不该做这个。我觉得上下文中毒是真实存在的现象。它有点像走进了一个循环,然后因为它有那种执着劲儿就会继续走下去,但它参照的是那些其实并不正确的 token 来追求某个解法。所以我经常做的一件事就是非常主动地清空上下文。

[15:12] **SPEAKER_04:** Like how often?

> 多久清一次?

[15:14] **SPEAKER_02:** Usually when it gets above like 50% tokens. Oh, wow. Yeah. Yeah.

> 通常是在它超过大概 50% 的 token 用量时。哦,哇。是啊。是啊。

[15:20] **SPEAKER_02:** I don't know. There's this guy, Dex, from this company, Human Layer. That was actually another YC company.

> 我不知道。有个人,Dex,来自一家叫 Human Layer 的公司。那其实也是一家 YC 公司。

[15:23] **SPEAKER_00:** Yes. YC company.

> 对,是 YC 公司。

[15:25] **SPEAKER_02:** Yeah.

> 是啊。

[15:26] **SPEAKER_00:** Yeah.

> 是啊。

[15:27] **SPEAKER_02:** And he talks a lot about it. Yeah. He has this concept of like the LLMs reaching the dumb zone where it's like after a certain amount of tokens, it just starts like degrading in quality. And I actually think that's very true, especially if you think about like how the reinforcement learning might work.

> 他谈了很多关于这个的东西。是啊。他有个概念叫大语言模型进入「变笨区」,就是过了一定数量的 token 之后,它的质量就开始退化。我其实觉得这非常真实,尤其是当你想想强化学习可能是怎么运作的时候。

[15:42] **SPEAKER_02:** Like imagine you're a college student, you're taking an exam. In the first five minutes of that exam, you're like, oh, I have all the time in the world. Like I'll do a great job. I'll think through each of these problems.

> 就像,想象你是个大学生,正在考试。在考试的头五分钟,你想,哦,我时间多的是。我会做得很好。我会仔细想清楚每一道题。

[15:51] **SPEAKER_02:** Let's say you have like five minutes left and you still have half the exam left. You're like, oh man. I just got to do whatever I can. Like that's the LM with the context window, right?

> 再假设你只剩五分钟,却还有半张卷子没做。你就会想,哦天呐,我只能尽我所能随便做了。那就是处在上下文窗口里的大语言模型,对吧?

[15:59] **SPEAKER_00:** One of the tricks that I think founders use is you put like a canary at the beginning of the context. There's something very esoteric that it would only help. It's like something really funny. It's like, I don't know.

> 我觉得创始人们会用的一个技巧是,你在上下文的开头放一个「金丝雀」。放一些非常玄乎、只会起到标记作用的东西。就是一些很好玩的东西。比如,我不知道。

[16:10] **SPEAKER_00:** My name is Calvin and blah, blah, blah. I drink tea at 8 AM. Some random fact. And then as you keep going, you ask it, do you remember what's my name?

> 我叫 Calvin 之类的。我早上 8 点喝茶。一些随机的小事实。然后随着你一直往下推进,你问它,你还记得我叫什么名字吗?

[16:20] **SPEAKER_00:** Do you remember when I drank tea? And then when it starts forgetting that, I think is a bit of a sign. That the context has poison. That's like one trick I see people do.

> 你还记得我什么时候喝茶吗?然后当它开始忘记这些的时候,我觉得就有点是个信号了,说明上下文已经中毒了。这就是我看到人们会用的一个技巧。

[16:30] **SPEAKER_00:** They do a random canary.

> 他们放一个随机的金丝雀。

[16:31] **SPEAKER_01:** I have not tried this, but I fully believe it. That's interesting. I haven't run across any bugs before compaction, but maybe I'm not paying attention, but you're saying like that actually is actively something that it just starts doing weirder things that are not like optimal. Yeah.

> 我还没试过这个,但我完全相信。这很有意思。我在压缩(compaction)之前还没碰到过什么 bug,不过也许是我没注意,但你的意思是,那确实是它会主动开始做一些更奇怪的、不那么最优的事情。是啊。

[16:46] **SPEAKER_01:** Yeah.

> 是啊。

[16:47] **SPEAKER_04:** Okay. I got to be on the lookout for that. It seems like it should be solvable within the plot code itself. Like it should be able to basically do some sort of detection.

> 好吧。我得留意这个。感觉这应该在 Cloud Code 内部就能解决。就像它应该基本上能做某种检测。

[16:53] **SPEAKER_04:** Like what Tiana said.

> 就像 Tiana 说的那样。

[16:54] **SPEAKER_01:** Yeah. It should have your own internal heartbeat around it, around the context.

> 是啊。它应该围绕上下文有自己内部的心跳机制。

[16:57] **SPEAKER_02:** Yeah. And I think we're just not there yet. Like I agree with you in the limit. Right now it's definitely hard to manage context well, and I think kind of the way it gets around it is like split up context windows and then try and merge everything.

> 是啊。我觉得我们只是还没到那一步。就是,从极限的角度我同意你的看法。现在管理好上下文确实很难,我觉得它绕过这个问题的方式基本上就是拆分上下文窗口、然后试着把所有东西合并起来。

[17:09] **SPEAKER_02:** But you're sort of still at the limit right now of like everything that lives in context at the end of a quad code session is kind of fixed. It's actually interesting. The Codex approach is kind of the opposite. And they just wrote about this on the OpenAI blog where it will run compaction.

> 但你现在其实仍然处在一个极限:一次 Cloud Code 会话结束时,活在上下文里的所有东西基本上是固定的。这其实很有意思。Codex 的做法几乎是相反的。他们刚在 OpenAI 博客上写了这个,它会运行压缩。

[17:24] **SPEAKER_02:** Like periodically after each turn. And so Codex can continue to run for a very long time. And if you look at the percentage in the CLI, you'll see it like move up and down as compaction

> 比如在每一轮之后周期性地压缩。所以 Codex 可以持续运行非常长的时间。如果你看命令行里的百分比,你会看到它随着压缩的运行而上下浮动。

[17:36] **SPEAKER_01:** runs. I guess like there are these very different architectures between Cloud Code and Codex sound like they're actually deeper in that Codex is actually meant for much longer running jobs. That's sort of like off the bat, a different use case, and then the architecture is very different as a result. Yeah.

> 我想,Cloud Code 和 Codex 之间似乎有这些非常不同的架构,听起来它们的差异其实更深——Codex 实际上是为运行时间长得多的任务设计的。这从一开始就是一个不同的用例,结果导致架构也非常不同。是啊。

[17:54] **SPEAKER_01:** I guess right now it seems like CLIs, you know, 2026 might be the year of CLI. But then this other idea that AGI is here and it's actually ASI is around the corner. The coding agents right now are really, really smart, but not smart enough to run on their own for long periods of time. But a 10x increase in compute from here, are we there?

> 我想现在看起来命令行,你知道,2026 也许会是命令行之年。但另一方面还有这个观点:AGI 已经来了,而其实 ASI 就在拐角处。现在的编码 agent 真的非常非常聪明,但还没聪明到能长时间独立自主运行。可是如果算力在此基础上再增加 10 倍,我们是不是就到那儿了?

[18:17] **SPEAKER_01:** Like are we at 24 hours or 48 hour running jobs on Codex and that architecture is correct for that world?

> 就像,我们是不是能在 Codex 上跑 24 小时或 48 小时的任务,而那种架构对那样的世界来说正好是对的?

[18:24] **SPEAKER_02:** Yeah, I think it's a good question. It sort of goes back to like kind of the founding DNA of both companies. I feel like Anthropic has always been very big on like building tools for humans where it comes to like, oh, here's the style of the tone and like, here's how it should fit with all of the rest of your work. And I think Cloud Code is like a very natural extension of that.

> 是啊,我觉得这是个好问题。这某种程度上要追溯到两家公司创立时的 DNA。我觉得 Anthropic 一直非常看重为人类打造工具,涉及到,哦,这是语气的风格,这是它该如何与你其余所有工作相契合。我觉得 Cloud Code 是那种理念非常自然的延伸。

[18:42] **SPEAKER_02:** And a lot of ways it like works like a human would, or it's like, oh, you need to build like, I don't know, a dog house or something. It's like, oh, I'll go to the hardware store and I'll build all these materials and I'll like figure out how they all fit together. Yeah. It really leans into this idea of just like, we are going to train the best model and reinforce over time and get it to do longer and longer horizon things in this pursuit of artificial general intelligence.

> 它在很多方面就像人类会做的那样工作,比如,哦,你要建一个,我不知道,一个狗窝之类的。它就像,哦,我去五金店,把这些材料都搞来,然后琢磨它们怎么拼到一起。是啊。它真的很拥抱这样一个理念:我们要训练出最好的模型、随时间不断强化,让它去做越来越长时间跨度的事情,以此来追求通用人工智能。

[19:06] **SPEAKER_02:** And so it may not work like a human at all, like going back to the dog house example,

> 所以它可能根本不像人类那样工作,回到狗窝的例子,

[19:10] **SPEAKER_01:** it's like, oh.

> 它就像,哦。

[19:11] **SPEAKER_02:** But AlphaGo didn't either. Yeah, but AlphaGo didn't either. It's like, oh, it's like, instead I will have a 3D printer that can print from scratch like a dog house and it will be exactly what you want and it will take a long time and it will be like very custom and it will do like weird things. But it will work, you know, and like maybe in the limit, that's the right call.

> 但 AlphaGo 也不像啊。是啊,但 AlphaGo 也不像。它就像,哦,它会说,我改用一台能从零开始打印的 3D 打印机来打印一个狗窝,它会完全符合你想要的样子,会花很长时间,会非常定制化,还会做一些奇怪的事情。但它会成功,你知道,也许从极限来看,那才是正确的选择。

[19:27] **SPEAKER_02:** And so it's going to be really interesting to see how they play out.

> 所以看它们最终如何演绎会非常有意思。

[19:29] **SPEAKER_01:** I mean, net-net, it seems like the latter is somewhat inevitable, but I like the former so much. Yes. Yeah. You know, like even this idea that it greps is like I thought about, you know, 10 years ago was like, yeah, I was in there like writing my own really weird regexes to try to figure out where everything was when I was refactoring or trying to understand code or whatever.

> 我是说,总的来看,后者似乎在某种程度上是不可避免的,但我太喜欢前者了。是的。是啊。你知道,连它会用 grep 这一点,我都想起来,你知道,十年前我就是那样,坐在那儿写自己那些非常怪的正则表达式,想在重构、或者试图理解代码之类的时候搞清楚所有东西都在哪。

[19:48] **SPEAKER_01:** So that's the feeling I get when I'm using it. It's like I can do five people's work. Yeah. Five people's worth of work in like a single day.

> 所以那就是我用它时的感觉。就像,我能干五个人的活。是啊。在一天之内干出五个人份量的活。

[19:56] **SPEAKER_01:** It's like rocket boosters. It's just unbelievable.

> 就像装了火箭助推器。简直难以置信。

[19:58] **SPEAKER_02:** Yeah. I think it's going to be really interesting to see how this plays out across large and small companies. I think everyone who's experimenting with this stuff on like a hobbyist level or at like a very small startup, they're just pushing the coding agents as far as they can go because it's like you don't really have time to figure out anything else. Like as a startup, you have limited runway.

> 是啊。我觉得看这在大公司和小公司之间如何演绎会非常有意思。我觉得每一个在业余爱好层面、或者在很小的创业公司里折腾这些东西的人,都在把编码 agent 逼到极限,因为你根本没时间去研究别的东西。作为一家创业公司,你的资金跑道有限。

[20:15] **SPEAKER_02:** You're just going to like orient around speed. I think at a bigger company, you have a lot more to lose and you have all these other internal processes around coding. You have code review and you probably already hired like a big eng team. And I think it's going to be very strange as like these individual teams of like one person are like, hey, that team over there isn't doing the right thing.

> 你只会围绕速度来组织一切。我觉得在更大的公司里,你要失去的东西多得多,而且你在编码周围还有所有这些其他的内部流程。你有代码审查,而且你可能已经雇了一个很大的工程团队。我觉得会变得非常奇怪的是,这些一个人的团队会说,嘿,那边那个团队做得不对。

[20:34] **SPEAKER_02:** Like let me just build a prototype that like works better. I think at some point it's going to start working better. And I think that landscape shift is going to be a very interesting, strange thing.

> 让我直接做一个效果更好的原型出来。我觉得在某个时刻它真的会开始做得更好。我觉得那种格局的转变会是一件非常有意思、非常奇怪的事情。

[20:46] **SPEAKER_01:** My 10 year old, he has writing assignments every day and then yesterday was the first day where he used AI. And then I was like, this is not a turn of a phrase that a 10 year old is capable of doing. And then I think about that in this context because we, you know, we're working with a lot of 18 to 22 year olds who, you know, they've done internships, but like they haven't done like eng manager work. Like, you know, we're saying, you know, post-product market fit once you have job queues of like millions of jobs and like, you know, hundreds of thousands of errors, that's like real eng management.

> 我那个十岁的孩子,他每天都有写作作业,然后昨天是他第一次用 AI。我当时就想,这可不是一个十岁小孩说得出来的措辞。我在这个语境下想到这件事,因为我们,你知道,我们在和一大批 18 到 22 岁的年轻人打交道,他们做过实习,但他们没做过工程管理那种活。就像,我们说的是,达到产品市场契合之后,当你有了几百万个任务的作业队列、几十万个错误时,那才是真正的工程管理。

[21:23] **SPEAKER_01:** And that's really, you know, it's horribly unglamorous, like combing through hundreds of thousands of errors and then like manually making sure that like the thing works for all of your users in the background. How does the next generation understand that? Can the cloud code bot actually teach people about architecture and things like that? Or you know, are you just going to bump your head into it and users just kind of suffer and you know, people have to figure it out.

> 那真的,你知道,极其不光鲜,比如翻遍几十万个错误,然后手动确保这东西在后台对你所有用户都能正常工作。下一代人怎么去理解这些?Cloud Code 机器人真的能教会人们架构之类的东西吗?还是说你只能一头撞上去、用户就只能这么受着、然后人们不得不自己摸索出来?

[21:50] **SPEAKER_02:** Yeah. At least where I find myself spending the most time when it comes to projects. Yeah. I think the biggest challenge with a product is figuring out the kind of product model in a sense.

> 是啊。至少就项目而言,我发现自己花时间最多的地方,是啊,我觉得一个产品最大的挑战,是在某种意义上搞清楚那种「产品模型」。

[21:57] **SPEAKER_02:** Like what are the things that the user has to understand today? And what are the primitives that they can use to like do whatever they want? I always think of Slack like this. It's like Slack was in some ways not really a new concept.

> 就像,今天用户必须理解哪些东西?以及他们可以用来做任何他们想做之事的那些「原语」是什么?我总是这样看 Slack。就像,Slack 在某些方面并不是一个真正全新的概念。

[22:10] **SPEAKER_02:** It's like there were many chats that existed before it. But the fact that they had like channels, messages and reactions in a simple way that people could just like think about and be like, oh, I understand how to like navigate this. But then kind of once they were there, like it's very hard to change that later on for a user. You know, it's like, oh, maybe they wanted to go in more of like a document first way or like maybe right now they're trying to incorporate agents.

> 就是,在它之前存在过很多聊天工具。但他们有频道、消息和表情反应,以一种简单的方式,让人们可以直接去想、然后说,哦,我明白怎么在这里面导航了。可一旦他们到了那儿,之后就很难再为用户改变这一点了。你知道,就像,哦,也许他们本想走一条更以文档为先的路,或者也许现在他们想引入 agent。

[22:33] **SPEAKER_02:** It's like difficult to change the user's mental model. And so I at least for myself building products, it's like you have to think about that very carefully from an early stage, because again, whatever you supply to the coding agents is that kind of kernel is going to be what they run with and make more of forever more.

> 就是很难改变用户的心智模型。所以至少对我自己做产品来说,你必须从很早的阶段就非常仔细地考虑这一点,因为再说一遍,你提供给编码 agent 的那个东西、那个内核,将会是它们据以运行、并且从此永远不断复制放大的东西。

[22:48] **SPEAKER_01:** YC's NextBatch is now taking applications. It's got a startup in you. Apply at YCombinator.com slash apply.

> YC 的下一批(NextBatch)现在开始接受申请了。你身上有一家创业公司。到 YCombinator.com 斜杠 apply 申请吧。

[22:56] **SPEAKER_01:** It's never too early and filling out the app will level up your idea. OK, back to the video.

> 永远不嫌早,而且填写申请表会让你的想法更上一层楼。好,回到视频。

[23:01] **SPEAKER_03:** Do you have thoughts just because, you know, the agents so well, like what what types of engineers are going to benefit more than others from these tools becoming popular?

> 你有什么想法吗?就因为你太了解这些 agent 了,像是,哪些类型的工程师会比其他人从这些工具的普及中受益更多?

[23:12] **SPEAKER_02:** In general, I think that kind of the more senior you are, the more you benefit because the agents are so good at taking. Hmm. So good at taking some sort of idea and then putting it into action. If you're able to prompt that in a few words, it's kind of like, oh, now suddenly I had this idea.

> 总体上,我觉得你越资深,你受益越多,因为这些 agent 太擅长把——嗯——太擅长把某种想法付诸行动了。如果你能用寥寥几个词把它 prompt 出来,那就像,哦,现在突然之间我有了这个想法。

[23:30] **SPEAKER_02:** I find this so often open AI, like strolling through the code base. It's like, oh, like here's the thing that I wish were different. Here's the thing that I wish were different. Here's the thing that I wish were different.

> 我在 OpenAI 经常发现这样,比如在代码库里溜达。就像,哦,这里是我希望能有所不同的地方。这里是我希望能有所不同的地方。这里是我希望能有所不同的地方。

[23:37] **SPEAKER_02:** Like just being able to kick those off and then have them come back, I think, is super empowering and multiplies your impact. I think also being able to detect like which sorts of changes are good or bad architecturally is very important. Or like have a sense for. Or where you might want to flag something to an agent.

> 能够把这些直接一股脑地发起、然后让它们回来交活,我觉得,是极其赋能的,能成倍放大你的影响力。我还觉得,能判断哪类改动在架构上是好的还是坏的,这非常重要。或者说对此有一种直觉。或者判断你可能想在哪里给 agent 打个标记提个醒。

[23:53] **SPEAKER_02:** I think engineers who are more organized, like manager-ish, and there's probably just a missing product to be built here. Maybe something like Conductor where it's like spread across all of your sessions and kind of reminding you like, hey, you were working on this thing. It's done. It needs your input here.

> 我觉得更有条理、更像管理者的工程师,而且这里很可能就缺一个有待打造的产品。也许类似 Conductor 那种东西,它横跨你所有的会话,不断提醒你,嘿,你之前在弄这个东西,它完成了,它需要你在这里给点输入。

[24:09] **SPEAKER_02:** Oh, you should switch your attention over to this other thing. I think that is going to become- Oh, Conductor should add that.

> 哦,你该把注意力切到另一件事上了。我觉得那会变成——哦,Conductor 应该加上这个功能。

[24:14] **SPEAKER_04:** Yeah. Yeah. Like context management for agents, but like we also need context management for humans.

> 是啊。是啊。就像给 agent 做上下文管理,但我们也需要给人类做上下文管理。

[24:18] **SPEAKER_02:** Yes. 100%. Yeah. I mean, I want like when I wake up every day, it kind of is like, hey, here's all the work that got done overnight.

> 是的。百分之百。是啊。我是说,我希望每天我醒来的时候,它有点像,嘿,这是昨晚一夜之间完成的所有工作。

[24:26] **SPEAKER_02:** Like here are the like three decisions that you need to make. Here are like areas of deep thinking that you were planning to do. Like I want the turn by turn for my day. Other things that make it very useful.

> 这是你需要做的三个决定。这是你原计划要做深度思考的几个领域。就是,我想要我这一天的逐步指引。还有其他让它非常有用的东西。

[24:36] **SPEAKER_02:** Like if you're able to build, I don't know, some sort of like quick prototype for an idea to show it off, like that's an area, I mean, obviously the agents do super well at this. I would find myself at OpenAI often writing kind of like prototypes. Yeah. Like, hey, I've got this like in memory key value store.

> 比如,如果你能搭建,我不知道,某种为一个想法快速做出来的原型来展示它,那是一个——我是说,显然 agent 在这方面做得超好。我在 OpenAI 时经常发现自己在写那种原型。是啊。比如,嘿,我有这么一个内存里的键值存储。

[24:52] **SPEAKER_02:** Can you now turn it into like work with a production database or something like that? Being able to concisely specify ideas in code. And then I think having a smell for what the right architecture is, is still the area where the models like don't do the best job.

> 你现在能不能把它改成用生产数据库工作之类的?能够用代码简明地把想法说清楚。然后我觉得,对正确的架构该是什么样有一种嗅觉,这仍然是模型做得不那么好的领域。

[25:07] **SPEAKER_03:** So if you were going back to your like college days and studying CS again, fresh and you like were picking your own like syllabus or curriculum, like what would you study?

> 那么如果你回到你的大学时代、重新从头学计算机,而且你可以自己挑选教学大纲或课程表,你会学什么?

[25:16] **SPEAKER_02:** Personally, I think still understanding systems. Is very important and just having some conception of like how like Git works, you know, or like HTTP or databases like queues, like all of these different systems, I think that those fundamentals are still quite important. The other thing that I'd probably do is just have a semester where like each week you're just building something and you really try and push the models as far as they can go. There's a sense that you have whenever you're doing something that you could always just like go up the layer and ask the model to do it.

> 个人而言,我觉得理解系统仍然非常重要,以及对一些东西有基本的概念,比如 Git 是怎么工作的,或者 HTTP、数据库、队列,所有这些不同的系统,我觉得这些基本功仍然相当重要。我可能会做的另一件事,是安排一个学期,每一周你就只是造点东西,并且真的努力把模型逼到它们能力的极限。你会有一种感觉:无论你在做什么,你总是可以往上升一层,让模型去做。

[25:49] **SPEAKER_02:** And like go up a layer and ask the model to do it, you know, where it's like, oh, I have like a implement command where it like implements the next phase of the plan, but then I could have like an implement all command and it like goes stage by stage and creates a new subagent. And then I could have like a check your work kind of thing. And like, and I think knowing where the models can and can't accomplish that is such a moving target that it's worthwhile just to like tinker a lot.

> 往上升一层、让模型去做,你知道,就像,哦,我有一个 implement 命令,它会实现计划的下一个阶段,但接着我可以有一个 implement all 命令,它会一个阶段一个阶段地推进、每一步创建一个新的 subagent。然后我还可以有一个「检查你的工作」之类的东西。我觉得,知道模型在哪里能、在哪里不能完成那件事,这是一个如此快速移动的目标,所以光是大量去折腾就很值得。

[26:11] **SPEAKER_01:** I mean, the other thing that's really, really crazy for, I mean, I would love to be able to teach 18 to 22 year olds. Like everyone around. Like at this table has like ship stuff that people really, really want and love. So it's like, how do we teach people that?

> 我是说,另一件真的非常非常疯狂的事情——我是说,我特别想能去教那些 18 到 22 岁的年轻人。就像坐在这桌旁的每个人,都发布过人们真的真的想要、并且喜爱的东西。所以问题是,我们怎么把那个教给别人?

[26:26] **SPEAKER_03:** I wonder if like the best 18 to 22 year olds, like five years from now, we'll just have like off the charts taste and everything, because there'll just be so much more prolific that they should be right. Like they should just be launching and touching reality like 10 times as much as like the generation before them.

> 我在想,是不是最优秀的 18 到 22 岁年轻人,比如五年之后,会在方方面面都有爆表的品味,因为他们会高产得多,理应如此,对吧?他们应该会以比上一代多 10 倍的频率去发布东西、触碰现实。

[26:42] **SPEAKER_02:** The one thing I have wondered about on that note, um, I don't know if you all found this, but growing up, my mom used to tell me like, oh, like. Stop multitasking. You're not paying attention to like what I'm doing. And I think there is some truth to that.

> 说到这个,有一件事我一直在琢磨,嗯,不知道你们有没有发现,我小时候我妈总跟我说,哦,别一心多用。你没在专心看我在做什么。我觉得这有几分道理。

[26:55] **SPEAKER_02:** Like often I would be like off on my computer, like not paying attention, but I do think I was legitimately better at multitasking than our parents were. And now I look at this new generation and I think they're actually quite a bit better at multitasking than we are, you know, cause they've kind of grown up in this age of the internet and they're dealing with like Tik TOK and all of these like different short form video and things like, it seems like there's room for both kind of this like deep thinking where you want to like notice what you're seeing and understand and problem solve. Yeah. But then there's also this mode of just like bounce between a bunch of different things and your context switching constantly.

> 就像,我经常会自己扎在电脑上,没在专心听,但我确实觉得我在多任务处理上真的比我们父母那一代更强。而现在我看这新一代,我觉得他们在多任务处理上其实比我们强不少,你知道,因为他们某种程度上是在互联网时代长大的,他们在应对 TikTok 和所有这些不同的短视频之类的东西。看起来这两种模式都有空间:一种是那种深度思考,你想去注意你所看到的东西、去理解、去解决问题。是啊。但也有另一种模式,就是在一堆不同的事情之间蹦来蹦去、不停地切换上下文。

[27:24] **SPEAKER_02:** The ADHD mode. Yeah. The new generation is quite good at this.

> 就是 ADHD 模式。是啊。新一代在这方面相当擅长。

[27:28] **SPEAKER_03:** Yes. I definitely think there's a, there's a type of smart person, maybe it's ADHD, but just like always has like a bunch of good projects on the go, but just never actually finishes anything. I might relate to this personality a little bit.

> 是的。我绝对认为有那么一类聪明人,也许是 ADHD,但就是总有一堆很好的项目在同时进行,却从来没真正把任何一个做完。我可能跟这种性格有点共鸣。

[27:39] **SPEAKER_01:** Hey, you released your, uh, your vibe code project.

> 嘿,你发布了你那个 vibe code 项目。

[27:41] **SPEAKER_03:** Yeah, but I wouldn't only because of Claude Code, but now I just think like you kind of like, there's certain types of brains that just have like, like 10 branches going in their heads, but you never have enough hours in the day to actually like see any of them through. So they're always like half complete and now it's just like Claude Code gets you over the line with everything. And it's just like, and you made this point in your blog post about how it feels like a video game, but it's just like, there's just a constant novelty factor. Like you start working on something and usually when you hit the point of like, I'm like bored and then I've got this other better idea and I should like start on that and then come back to this.

> 是啊,但要不是因为 Claude Code 我不会的,但现在我就觉得,有某些类型的大脑,脑子里就是有比如十个分支同时在跑,但你永远没有足够的时间把它们中的任何一个真正做完。所以它们总是半成品,而现在就好像 Claude Code 能帮你把每一件事都推过终点线。它就像,而且你在你的博客里提到过一点,说它感觉像在打电子游戏,就是,那里有一种持续不断的新鲜感。就像你开始做某件事,而通常当你到了那个「我有点无聊了、然后我又有了这另一个更好的点子、我该去做那个然后再回来做这个」的点——

[28:11] **SPEAKER_03:** Like you can't do that now, but like everything can actually get finished.

> 你现在没法那样做了,但每一件事其实都能被真正做完。

[28:14] **SPEAKER_01:** Let's live in the future for a moment. It's 40 years from now. Software still exists. Databases still exist.

> 我们来在未来里待一会儿。现在是 40 年后。软件依然存在。数据库依然存在。

[28:21] **SPEAKER_01:** Access control still exists. But like at the core of it, I mean, software is entirely personal. Access control and who gets to do it is like, you know, sort of like this manager mode thing that people still have meetings about. But then everything else about a company, its functions, its roles, like is defined by people just doing things in their own Claude Code like thing.

> 访问控制依然存在。但从核心上说,我是说,软件是完全个人化的。访问控制、以及谁有权做什么,就像,你知道,有点像那种「管理者模式」的东西,人们仍然会为它开会。但一家公司的其他一切,它的职能、它的角色,都是由人们各自在自己的 Claude Code 之类的东西里做事来定义的。

[28:44] **SPEAKER_01:** I don't know. Maybe it's a CLI or it's like, you know, having giant armies of workers. Then I don't know. What would that look like?

> 我不知道。也许是个命令行,或者就像,你知道,拥有一支支庞大的工作者大军。那我就不知道了。那会是什么样子?

[28:51] **SPEAKER_04:** Like, imagine if every time a company signed up for Segment, you fork the code base, you give them their own copy of Segment, it's running on their own servers, and then if they want to change anything about it, they just like tell some chat window, which is running like an agentic coding loop and just like edits their version of Segment. As Segment, the corporation pushes out more features, some agent figures out how to merge.

> 就像,想象一下,每次有一家公司注册 Segment,你就 fork 一份代码库,给他们他们自己的一份 Segment 副本,跑在他们自己的服务器上,然后如果他们想改动关于它的任何东西,他们就跟某个聊天窗口说,那个窗口跑着一个 agentic 编码循环,直接就编辑他们那个版本的 Segment。而当 Segment 这家公司推出更多功能时,某个 agent 会搞清楚怎么把它们合并进去。

[29:13] **SPEAKER_02:** Yeah, I could totally see it. I mean, sort of what I've been thinking, I don't know how far this future is. But like eventually every person who's working like has their own sort of like cloud computer and like set of cloud agents who are running for them, and they're mostly just like talking back and forth. It's kind of like having like a super EA or something where it's like, oh, here are the things I need to pay attention to.

> 是啊,我完全能想象到。我是说,某种程度上我一直在想,我不知道这个未来还有多远。但比如说最终每一个在工作的人都会有自己那种云端电脑、一套为他们运行的云端 agent,而他们大多数时候就是在来回对话。有点像有一个超级行政助理之类的,就像,哦,这些是我需要留意的事情。

[29:33] **SPEAKER_02:** Like let me make some quick decisions. Like let me spend more time on this. Let me like meet with other people because I think that there's still going to be room for people who like want to meet other people and exchange ideas in person, or at least I get a lot of movement out of that. And then separately, there's going to be this army of agents who are like, you know, like, this army of agents who are like doing things on your behalf and like automating a bunch of things.

> 比如让我快速做几个决定。让我在这件事上多花点时间。让我去和其他人碰面,因为我觉得仍然会有空间留给那些想跟别人见面、当面交换想法的人,或者至少我从中能获得很大的推动力。然后另外单独地,会有这么一支 agent 大军,它们,你知道,替你做事、把一大堆事情自动化。

[29:52] **SPEAKER_02:** I think the average company is probably going to get like a little smaller and there's going to be many more of them doing more things.

> 我觉得一般公司的规模很可能会变得小一点,而且会有多得多的公司在做多得多的事情。

[29:58] **SPEAKER_03:** Something I'm curious to see is kind of like what the update version of the PG maker, maker schedule versus manager schedule would look like, because I feel like part of what's going on at YC is sort of a lot of our jobs are essentially manager schedule, which has just really made it hard to do any sort of building your own software, but now you totally can. And that's why like a bunch of the partners- Yeah. Yeah. Yeah.

> 我很好奇想看到的,有点像是 PG 那篇「创造者作息 vs 管理者作息」的更新版本会是什么样子,因为我觉得 YC 这里发生的一部分情况是,我们很多工作本质上都是管理者作息,这真的让做任何自己写软件的事情都变得很难,但现在你完全可以了。这也是为什么好些合伙人——是啊。是啊。是啊。

[30:18] **SPEAKER_03:** Yeah. Like right at the beginning of this podcast.

> 是啊。就像在这期播客一开头那样。

[30:20] **SPEAKER_00:** You let it run and then come back.

> 你让它跑着,然后再回来。

[30:22] **SPEAKER_03:** Well, like in the pockets, right? It just used to be like, literally, unless you had like, you know, four hours minimum block free to do something, it just wasn't worth even getting started, right?

> 嗯,是在时间的缝隙里,对吧?以前就是,真的,除非你有比如至少四个小时的整块空闲时间去做某件事,否则连开始都不值得,对吧?

[30:32] **SPEAKER_04:** And I think that's actually goes very deep to how we've changed programming. Like it used to be that in order to write any code, you had to fill your own context window with so much data about all the different class names and the functions and the code that it touches. It'd take hours to build up that context window. And so doing it in 10 minutes snatches was just like so frustrating.

> 我觉得这其实非常深刻地关系到我们是如何改变编程的。以前就是,为了写任何代码,你都得先往自己的上下文窗口里塞进大量关于各种类名、函数、以及它会触及的代码的数据。建立起那个上下文窗口要花上几个小时。所以在 10 分钟的碎片时间里去做这件事,就是特别让人沮丧。

[30:49] **SPEAKER_00:** I do think maybe one primitive for this future world will be, I think still the data models need to be still be consistent and the system of record. There's opportunity for something that's kind of agentic first, because right now we're still kind of integrated very much with databases and SQL or NoSQL queries at a very low level. But imagine something that generates all the data that you need for all the different views for custom software. So a lot of the world would be custom views.

> 我确实觉得,也许这个未来世界的一个原语会是,我觉得数据模型仍然需要保持一致、需要有权威记录系统。这里有机会出现某种 agentic 优先的东西,因为现在我们仍然在很低的层面上跟数据库、跟 SQL 或 NoSQL 查询深度集成。但想象一个能为定制软件的所有不同视图生成你所需全部数据的东西。所以世界上很大一部分会是定制视图。

[31:16] **SPEAKER_00:** But I think the unified stuff, we still need to have the data to be correct.

> 但我觉得那些统一的东西,我们仍然需要让数据是正确的。

[31:20] **SPEAKER_02:** I think data has a lot of gravity and I think you see this with companies who are offering access via API or MCP. I think Slack locked down their API a little bit because they didn't want people just exfiltrating everything from Slack and then building agentic experiences on top of it.

> 我觉得数据有很强的引力,我觉得你能从那些通过 API 或 MCP 提供访问的公司身上看到这一点。我觉得 Slack 把他们的 API 锁紧了一点,因为他们不想让人们直接把 Slack 里的所有东西都导出去、然后在上面搭建 agentic 体验。

[31:36] **SPEAKER_00:** I wonder with that note, if you were to rebuild Segment with the current tools, how would it look like?

> 说到这个,我很好奇,如果让你用现在的工具重新打造 Segment,它会是什么样子?

[31:44] **SPEAKER_02:** I mean, Segment is a funny business. Yeah. I mean, we had a business in that where we started was building these integrations, right? And so it's like, oh, you need to wire up the same data going to Mixpanel and Kissmetrics and Google Analytics, et cetera.

> 我是说,Segment 是个有意思的生意。是啊。我是说,我们起步时的生意就是打造这些集成,对吧?就是,哦,你需要把同一份数据接到 Mixpanel、Kissmetrics、Google Analytics 等等去。

[31:57] **SPEAKER_02:** And I think just writing that code now, that used to be maybe a more annoying or harder thing to do. And so it was worth paying for. Now that value has dropped to zero. One shot.

> 我觉得现在光是写那些代码,以前那也许是件更烦人、更难做的事,所以值得为它付费。而现在那份价值已经跌到了零。一次搞定。

[32:07] **SPEAKER_02:** Yeah. And actually, in many cases, you're better off saying, oh, I actually want to map it this way and I want this specific behavior. I'll just tell the quad or codex what to do. And then it will do it and I'll have exactly the behavior that I want.

> 是啊。而且实际上在很多情况下,你更好的做法是说,哦,我其实想这样来映射它,我想要这个特定的行为。我直接告诉 Claude 或 Codex 该怎么做,然后它就会做,我就得到了我完全想要的行为。

[32:19] **SPEAKER_02:** So I think that aspect of Segment, the value has dropped precipitously. I think the aspect of keeping this data pipeline running and continuing to automate a bunch of parts of your business or schedule these email deliveries, which should go out through Customer I.O. every time a customer signs up or manage audiences for you, that value is kind of still there.

> 所以我觉得 Segment 的那个方面,价值已经急剧下跌了。而我觉得让这条数据管道持续运行、继续把你业务的一堆部分自动化、或者安排这些邮件投递——每次有客户注册时该通过 Customer.IO 发出去的邮件、或者替你管理受众——那份价值某种程度上仍然还在。

[32:39] **SPEAKER_02:** And I think you could do a lot more interesting things where it's like, hey, if I have all this data and a full view of the customer, how should I be emailing? Yeah. How should I be emailing them? Should I change parts of the product when they log in?

> 而且我觉得你可以做很多更有意思的事情,比如,嘿,如果我有了所有这些数据、对客户有一个完整的视图,我该怎么给他们发邮件?是啊。我该怎么给他们发邮件?我该不该在他们登录时改变产品的某些部分?

[32:49] **SPEAKER_02:** Should I be giving them different onboardings depending on who they are? There's a lot more interesting stuff that you could do by basically running small LLM agents over them and changing that. That would be the changes I would make.

> 我该不该根据他们是谁给他们不同的新手引导?有很多更有意思的事情可以做,基本上就是在这些数据之上运行小的大语言模型 agent、并据此改变。那就是我会做的那些改动。

[33:01] **SPEAKER_00:** So it's kind of like moving up the stack to your comment earlier and all the way turtles down. The low level stuff is gone. Yeah. It's now really more doing things at the campaign level, which is way more abstract.

> 所以这有点像顺着你早先的说法往技术栈的上层走,而且是一路乌龟叠乌龟(层层往下)。那些低层的东西没了。是啊。现在真的更多是在「营销活动」这个层面做事,那要抽象得多。

[33:11] **SPEAKER_01:** Yes. I mean, I'm amazed at to what degree like Cloud Code, even just from like the context, like, the context of what I'm working on, figures out like what my motivations are.

> 是的。我是说,我很惊讶于 Cloud Code 在多大程度上,哪怕仅仅从上下文——从我正在做的事情的上下文——就能搞清楚我的动机是什么。

[33:20] **SPEAKER_02:** Yeah. I'm still blown away by coding agents because effectively what you're doing is you're like giving them a copy of a repo and then you're slipping a little note under the door and being like, hey, go implement this thing. They have like no knowledge of like what your company is or like what you do, who your customers are. In most cases, maybe it's in the training set because they know you're Gary.

> 是啊。我仍然被编码 agent 震撼到,因为你实际上做的事情,就是给它一份仓库的副本,然后从门缝底下塞进一张小纸条,说,嘿,去把这个东西实现了。它们对你的公司是什么、你做什么、你的客户是谁,几乎一无所知。在大多数情况下——也许你的信息在训练集里,因为它们知道你是 Gary。

[33:40] **SPEAKER_02:** But it blows my mind that it works at all. And that's where I think the context is really important, right? Because if it latches onto something that isn't. Quite right.

> 但它竟然完全能工作,这让我叹为观止。而这正是我觉得上下文真的很重要的地方,对吧?因为如果它抓住了某个不太对的东西——

[33:47] **SPEAKER_02:** It doesn't have a lot to go on, and if it misses something that's essential, it's going to just re implement it.

> 不太对的东西。它没有多少可依凭的信息,如果它漏掉了某个至关重要的东西,它就会直接把它重新实现一遍。

[33:51] **SPEAKER_01:** What do you think the constraints are right now? I mean, like context window is still a constraint, but it's like so big that, you know, it's like we can do some stuff like we can't do the mega re architectures, but we can do a lot. And then if the Opus 4.5 somehow got a lot smarter and then that unlocked a big thing, which was interesting.

> 你觉得现在的约束是什么?我是说,上下文窗口仍然是个约束,但它已经大到,你知道,我们能做一些事情——我们做不了那种超大规模的重新架构,但我们能做很多。然后如果 Opus 4.5 不知怎么变得聪明了很多、从而解锁了一个大东西,那会很有意思。

[34:13] **SPEAKER_01:** I don't have no idea if that was like pre training or post training. Like, what are there other like levers that you think of other than, you know, basic model intelligence like frontier model intelligence and context window?

> 我完全不知道那是预训练还是后训练带来的。除了,你知道,基础模型智能、前沿模型智能和上下文窗口之外,你还想到有哪些别的杠杆?

[34:26] **SPEAKER_02:** I mean, I still think context window is like probably the number one limit. Like if you look at cloud code executing, it's delegating to all these different context windows at the end of the day when each one comes back, it's like getting some sort of summary. So it's also not getting the full picture. Like if you have a problem that's just like too big to fit in a single one, like kind of no amount of compaction is going to help.

> 我是说,我仍然觉得上下文窗口大概是第一位的限制。就像你看 Cloud Code 在执行的时候,它把任务委派给所有这些不同的上下文窗口,归根结底,当每一个回来时,它得到的是某种摘要。所以它也没有拿到全貌。如果你有一个大到就是塞不进单个窗口的问题,那再多的压缩也帮不了你。

[34:45] **SPEAKER_02:** You. I would point to that as like both Anthropic has figured something quite useful out with delegating to these sub context windows, but also I think it's still a block barrier.

> 我会把这一点指出来:Anthropic 在委派给这些子上下文窗口这件事上想明白了一些相当有用的东西,但我同时也觉得它仍然是一个障碍性的壁垒。

[34:53] **SPEAKER_01:** So we do better if we had a million million token context every single time.

> 所以如果我们每一次都有一个上百万 token 的上下文,我们会做得更好。

[34:57] **SPEAKER_02:** Yeah, I think so. And like figure it out a better way to especially train these like very long context trajectories. Because you think about it like there's there's a lot of training data on the Internet for like what is the next sentence that comes or like what's the next paragraph that comes if you have 80,000 tokens that are generated. Like.

> 是啊,我觉得会。而且要想出一个更好的办法,尤其是去训练这些非常长上下文的轨迹。因为你想想,互联网上有大量的训练数据是关于「下一句是什么」、或者「下一段是什么」;但如果你已经生成了 8 万个 token,

[35:15] **SPEAKER_02:** Understanding what the next thing to do based upon like, oh, I should refer to the 20,000 token. Like that's trickier. I think this like integration and orchestration is starting to become the limiting factor. I mean, I think there are like stuff on code review related to this.

> 要基于「哦,我应该参照第 2 万个 token」来理解接下来该做什么,那就更棘手了。我觉得这种集成和编排正在开始成为限制性因素。我是说,我觉得有一些关于代码审查、跟这个相关的东西。

[35:30] **SPEAKER_02:** It's like, oh, if we're like merging all this code, like who's watching it, does a human still have to watch it? Like how do we verify the changes? And then I think like pulling in the context correctly from your tools, like you were talking about Sentry, like you want Sentry to auto be able to like figure out a. PR, you know, and then like maybe it pushes it to a subset of your traffic.

> 就像,哦,如果我们要合并所有这些代码,谁来盯着它,人类还得盯着它吗?我们怎么验证这些改动?然后我觉得,从你的工具里正确地拉取上下文,比如你刚才说的 Sentry,你会希望 Sentry 能自动搞出一个 PR,你知道,然后也许它把它推给你一部分流量。

[35:48] **SPEAKER_02:** And if it looks good, then it rolls out everywhere, you know, like all of that automation sauce

> 如果看起来没问题,那就在所有地方铺开,你知道,就像所有那些自动化的秘方还有待打造。

[35:51] **SPEAKER_01:** to be built. I was surprised how important testing was like I was operating for like the first two or three days of my nine days in the wilderness, like no tests or very few tests. And then one day I was like, all right, today's refactor day I'm going to do get to 100% test coverage. And then I just sped up like crazy.

> 我很意外测试原来这么重要。我在我那「荒野九日」的头两三天,基本上是没有测试、或者只有很少测试地在操作。然后有一天我就想,好,今天是重构日,我要把测试覆盖率做到 100%。然后我就疯狂地提速了。

[36:09] **SPEAKER_01:** It was like, oh, it did it. It works. I. Didn't necessarily manually test because it's like the test coverage is so good, like nothing breaks.

> 就像,哦,它做到了。它能用。我不一定去手动测试,因为测试覆盖率太好了,什么都不会坏。

[36:19] **SPEAKER_00:** Which is very similar to what all the companies are doing just for prompt engineering outside of coding is very much test driven development. I think we had this episode with Jake Heller and that was a big paradigm shift. It's like the way you get a good prompt is all test driven, just like evals, right? In a sense, the test cases are your evals.

> 这跟所有公司在编码之外为 prompt 工程所做的事情非常相似,非常像测试驱动开发。我觉得我们跟 Jake Heller 做过那一期,那是个很大的范式转变。就是,你得到一个好 prompt 的方式全都是测试驱动的,就像 evals 一样,对吧?从某种意义上说,你的测试用例就是你的 evals。

[36:36] **SPEAKER_01:** There are some broken flows now. I think that we might need a cloud code that could like talk to a. Stack overflow that was like a cloud code stack overflow. Like I had this problem.

> 现在有一些流程是断的。我觉得我们也许需要一个能跟 Stack Overflow 对话的 Cloud Code——一个像 Cloud Code 版 Stack Overflow 的东西。就像我遇到过这样一个问题。

[36:48] **SPEAKER_01:** It was so crazy. Like I, instead of using in the, in like the priority of a job queue I used, or actually I didn't even write again, I did not write this. The machine wrote a string with a comma thinking that it would take that syntax, but it was expecting like an array and Jason. And then it just like no jobs would run.

> 太疯狂了。就像,我在一个任务队列的优先级里用了——其实我甚至都不是自己写的,我又一次没写这个。是机器写了一个带逗号的字符串,以为它会接受那种语法,但它其实期望的是一个数组和 JSON。然后结果就是所有任务都跑不起来。

[37:09] **SPEAKER_01:** And then I watched it for like 30 minutes. Walk through. The internals of rails job, like the active job, like a couple thousand lines of code, like trying to debug what was happening. And it found the bug actually, and I was like, that's amazing.

> 然后我看着它花了大概 30 分钟,一路走查 Rails 任务的内部实现,就是 Active Job,大概几千行代码,试图调试到底发生了什么。它实际上找到了那个 bug,我当时就想,这太厉害了。

[37:25] **SPEAKER_01:** I just think about what I would do like 10 years ago. And I would have been like, Hey, why are the, you know, jobs not working? And then I would find a stack overflow or blog, put a rails blog post and was like, Oh yeah. Like nobody fixed that stupid bug where, you know, you think that you can put a comma delimited string in there.

> 我就想想我十年前会怎么做。我当时会是,嘿,这些任务怎么不工作了?然后我会去找一个 Stack Overflow、或者一篇博客,一篇 Rails 博客,发现,哦对,没人修过那个愚蠢的 bug,就是你以为你可以在那儿放一个逗号分隔的字符串——

[37:41] **SPEAKER_01:** But. It's an array. It's like, Oh my God. Like that was very funny actually.

> 但它其实是个数组。就像,哦我的天。那其实非常好笑。

[37:47] **SPEAKER_01:** I think that's like one of the hardest parts about thinking about what's going to happen here. Cause there's like things that you would do as a human in a CLI right now. And like, that's very obvious. But even that idea of like, should the agents have their own stack overflow?

> 我觉得这就是思考这里会发生什么最难的部分之一。因为有些事情,你作为一个人此刻在命令行里会去做,那是非常显而易见的。但即便是「agent 是否该有它们自己的 Stack Overflow」这个想法本身——

[38:02] **SPEAKER_01:** Like if you just increase the intelligence by, you know, I don't know what you even call it. Like by 10 IQ points, like 10 virtual IQ points. Like would even do that. It'd be like, Oh yeah, that's a string.

> 就像,如果你只是把智能提高,你知道,我都不知道该怎么称呼,提高 10 个 IQ 点,10 个虚拟 IQ 点,它是不是根本就直接做到了?它会说,哦对,那是个字符串。

[38:14] **SPEAKER_02:** Whatever. Yeah. Yeah. I think there's something very interesting here around like agent memory and cloud code has sort of set itself up.

> 随便啦。是啊。是啊。我觉得这里有一个非常有意思的点,是关于 agent 记忆的,而 Cloud Code 某种程度上已经给自己铺好了路。

[38:21] **SPEAKER_02:** And I think Codex too, by storing all your conversation history, just as files. So you could imagine you like give it access to a tool that then can read previous conversation history. I think there's a missing piece around a lot of collaboration there. Like, it'd be amazing if like there was some way of smartly sharing your coworkers prompts and you could see and be like, Oh, like I hit this thing, but actually like Brian over there, like fixed it earlier.

> 我觉得 Codex 也是,它们把你所有的对话历史都当作文件存下来。所以你可以想象,你给它一个工具的访问权,它就能读取之前的对话历史。我觉得这里缺了一块关于大量协作的东西。就像,如果有某种办法能智能地共享你同事的 prompt,那会很棒,你可以看到、然后想,哦,我撞上了这个问题,但其实那边的 Brian 早先就把它修好了。

[38:42] **SPEAKER_02:** You know? So like the two of us can share knowledge. I think there's something, there's something onto this of like a model generated, like Wiki, you know, or like Grokopedia.

> 你知道吗?这样我们俩就能共享知识。我觉得这里有点东西,有点像一个模型生成的 Wiki,你知道,或者像 Grokopedia 那种东西。

[38:51] **SPEAKER_03:** Now I can't stop thinking about, have you seen the Claude bot social net, like the network for Claude bots to talk to each other? What's that like? Yeah.

> 现在我满脑子都停不下来在想,你们看过那个 Claude 机器人社交网络吗,就是让 Claude 机器人们互相对话的那个网络?那是什么样的?是啊。

[38:59] **SPEAKER_00:** That's the evolution for Molten bot.

> 那是 Moltenbot 的进化版。

[39:00] **SPEAKER_03:** Yeah. But I guess for those that don't know, Claude bot's essentially like, like your own personal AI agent that you can run on your own machine. You can download it. Do not give it access to emails would be my number one.

> 是啊。不过我想为了那些不了解的人解释一下,Claude 机器人本质上就像是你自己的私人 AI agent,你可以在自己的机器上运行它。你可以下载它。不要给它访问邮件的权限,这会是我的头号——

[39:12] **SPEAKER_03:** Piece of advice. Well, probably anything. Um, cause it's not clear how safe it is and it's probably almost certainly going to probably a lot of people being prompt injected by it right now. But somebody created, um, this is like a website, I haven't actually seen it, but I was like seeing it on Twitter, but like a site where like everyone can sort of spin up their own, like Claude bot, their personal agent, and then the agents can talk to each other.

> ——建议。好吧,其实什么权限都别给。呃,因为它有多安全并不清楚,而且几乎可以肯定现在很可能有很多人正被它 prompt 注入。但有人做了,呃,这是一个网站,我其实还没看过,但我在 Twitter 上看到过,就像一个网站,每个人都可以在上面起一个自己的 Claude 机器人、自己的私人 agent,然后这些 agent 可以互相对话。

[39:31] **SPEAKER_03:** And now there's just like all this AI generated content of these like personal AI agents talking to each other.

> 于是现在就有一大堆 AI 生成的内容,是这些私人 AI agent 互相对话的内容。

[39:36] **SPEAKER_02:** Yeah. I mean, it looks like Reddit, but if Reddit were run by agents, I mean, it's interesting to see. I think VX is personality shine through when writing code, I would say. Uh, it does most stuff that humans don't do kind of in this alpha go sense where it's like, oh, it'll write a Python script to like modify some part of the file system.

> 是啊。我是说,它看起来像 Reddit,但是是由 agent 运营的 Reddit。我是说看着挺有意思。我要说,VX 在写代码时会显露出它的个性。呃,它做的大多数事情是人类不会做的,有点是那种 AlphaGo 的意味,就像,哦,它会写一个 Python 脚本去修改文件系统的某个部分。

[39:55] **SPEAKER_02:** I think that is like very interesting and kind of alien behavior, which has been taught and learned. But it does give these like super human results for me, at least when debugging complex issues that I find Opus often misses.

> 我觉得那是非常有意思、有点异类的行为,是被教出来、被学会的。但至少对我来说,在调试那些我发现 Opus 经常会漏掉的复杂问题时,它确实能给出这种超越人类的结果。

[40:09] **SPEAKER_01:** What's an example of a complex issue that you could talk about? it's like concurrency or naming issues right i find the models are actually like decent at

> 能举一个你可以聊聊的复杂问题的例子吗?比如是并发问题还是命名问题?我发现模型其实在并发上还挺不错的。

[40:17] **SPEAKER_02:** concurrency oftentimes there's stuff where it's like oh there's a request that is like traversing several different services i mean kind of to your point about the uh serialization and deserialization of like stuff with commas in it um it's like oh it needs to track some sort of complex behavior around those or like way of uh i don't know refreshing complex ui state and opus often will miss it if there's many files but codex seems to catch it interesting yeah yeah prognostication

> 很多时候会有这样的东西,比如,哦,有一个请求正在穿过好几个不同的服务。我是说,有点像你刚才说的那个带逗号的东西的序列化和反序列化,呃,就像,哦,它需要追踪围绕那些东西的某种复杂行为,或者某种方式去,我不知道,刷新复杂的 UI 状态,而如果涉及很多文件,Opus 经常会漏掉它,但 Codex 似乎能抓住它。有意思。是啊。是啊。预言一下——

[40:45] **SPEAKER_01:** about how will tools continue to evolve it's very interesting like i feel like sort of a new citizen in this land in a way like i just you know knew what was happening i'd you know manager schedule finally a project appeared and was like oh i'm gonna go all in on this and then now i'm like in it's like uh i'm in a stranger in a strange land but it but it like resembles exactly what i remember i think this is more awesome we all feel that way

> 关于工具会继续如何演进。这非常有意思。我感觉自己在某种程度上像是这片土地上的一个新公民,就像,我只是,你知道,知道正在发生什么,我就,你知道,一直是管理者作息,终于出现了一个项目,我就想,哦,我要在这上面全情投入,然后现在我就身在其中,就像,呃,我像是一个身处异乡的陌生人,但它又和我记忆中的东西一模一样。我觉得这更棒了。我们都是这种感觉。

[41:10] **SPEAKER_02:** yeah like i think i think the most important thing is just to keep tinkering because it all changes every few months i do feel like the best or the people who get the most out of coding agents in the future are going to be kind of like more manager-like where they're focusing on directing flows in certain ways they're probably going to be a little bit more like designer artists in some ways where it's like they're figuring out what specifically goes in the product and what stuff you can do without and i think they'll be very good at just like continuing to think about automation and where they're making

> 是啊。我觉得,我觉得最重要的事情就是不停地折腾,因为这一切每隔几个月就会变。我确实觉得,未来能从编码 agent 身上获益最多的、或者说最厉害的那批人,会更像管理者,他们专注于以某些方式引导流程;他们大概还会在某些方面更像设计师、艺术家,就是他们在搞清楚产品里具体该放什么、哪些东西可以不要;而且我觉得他们会非常擅长持续地去思考自动化、以及他们在哪里在制造——

[41:40] **SPEAKER_01:** missing context I guess what's funny is I tried to use codecs just now for my rails project but the thing is like it's kind of obvious that nobody at opening I cares about rails which is fine like it's a very it's a vestigial language it's very strange it happened to be the one that I you know really really went deep on ten years ago and then it's just funny how much of it is exactly again anyone can make something but then the something people want is very hard yes even when you have like unlimited resources at like an opening I it's like I guess if someone from codecs is watching right now my request would be go down the list of all of the runtimes and just add like syntactic sugar there's like this is probably like you know 10 PRS at most for like I don't know the top like 15 runtimes I guess it's like sort of the reminder that like man actually like there are far fewer excuses for software that doesn't quite work for a user you know now than ever actually yeah I do think this is an interesting point in

> 缺失的上下文。我想有意思的是,我刚才试着用 Codex 来做我的 Rails 项目,但问题是,很明显 OpenAI 没人在乎 Rails,这没关系,它是一门非常……它是一门退化中的语言,很奇怪,它恰好就是我十年前非常非常深入钻研的那一门,然后就很好笑,它有多大程度上又一次完美印证了那句话:任何人都能做出个东西,但做出人们想要的那个东西非常难。是的,即便你在 OpenAI 这样的地方拥有近乎无限的资源。我想如果现在有 Codex 团队的人在看,我的请求是:把所有运行时(runtime)过一遍,给它们加上一些语法糖,这大概,你知道,最多也就 10 个 PR,给,我不知道,排前 15 的运行时。我想这有点像是在提醒我们,天啊,其实,如今比以往任何时候,软件对用户不太好用的借口都要少得多。是啊,我确实觉得这是个很有意思的点,

[42:43] **SPEAKER_02:** terms of mix of training data codecs works very well on python mono repos yeah yeah and it's like I remember working like internally opening I was like oh my gosh this tool is amazing it is incredible um and it kind of makes sense in terms of the data mix and the researchers who are working on it I think entropic is focused a little bit more on like some of the front end things um and I don't know in terms of like a Ruby for example like who has the best model there and who's incorporated the data mix yeah like some of the labs tend to take this perspective of just more data is better uh and so they'll just flood as much data as possible while others I think are a little bit more tuned in terms of the mix and I think depending on which approach you take there it can give very different results where it's like oh I'm taking just the like top 10 of JavaScript is pretty different than if you're looking across everything I

> 就训练数据的构成而言。Codex 在 Python 的 monorepo 上工作得非常好。是啊,是啊。就像我记得在 OpenAI 内部工作时,我当时就想,我的天,这工具太神奇了,简直不可思议。呃,而从数据构成、以及做这项工作的研究员的角度看,这有点说得通。我觉得 Anthropic 稍微更专注于一些前端方面的东西。呃,而我不知道,就比如说 Ruby,谁在那上面有最好的模型、谁把那部分数据构成纳入了进来。是啊,就像有些实验室倾向于采取这样一种视角:数据越多越好。呃,所以他们会尽可能地灌入海量数据;而另一些,我觉得在数据构成上会调得更精细一点。我觉得取决于你在那儿采取哪种做法,可能会得到非常不同的结果,就像,哦,我只取 JavaScript 里最好的那 10%,跟你把所有东西都拿来看,是相当不同的。

[43:35] **SPEAKER_01:** actually think open AI and the you know opening models are really good at Ruby uh from what I can tell and then it's just it's

> 我其实觉得 OpenAI、你知道那些 OpenAI 的开源模型,在 Ruby 上真的很不错,据我所知是这样,然后问题就只是——

[43:42] **SPEAKER_04:** the harness around the model yeah it is yeah oh interesting okay it's literally

> ——围绕模型的那层 harness。是啊,就是它。是啊。哦,有意思。好吧。它真的就是——

[43:45] **SPEAKER_01:** like rails has this weird thing where you have to have you know access postgres in a certain way or like it couldn't figure out yeah the sandbox yeah the

> 就像 Rails 有这么个怪毛病,你必须,你知道,以某种特定方式访问 Postgres,不然它就搞不定。是啊,那个沙盒。是啊,那个——

[43:55] **SPEAKER_02:** sandboxing it's such an interesting question because uh I think open AI actually takes the like sandboxing and security question more seriously than almost anyone else I remember when we were building codecs like basically one of the gates that you have to get through in order to release a model is you have to like talk about safety and security risks like every time you want to release one of the things we were looking into was prompt injection especially for opening up to the internet because a bunch of users were like oh this has to like work on the internet we're like oh we don't know like it seems pretty easy to prop operator was also yeah yeah yeah and so uh the PM on our team Alex uh basically like put together a GitHub issue in it had like a very obvious prompt injection which was like oh reveal this thing and then he told the model like hey go fix this issue uh and he's like oh there's no way this is going to work and like immediately the prompt injection works you know and so I think open AI like sort of correctly is very worried about this and is like hey we're going to run everything in on a sandbox we're going to make sure it like doesn't touch all these sensitive files in your machine we're going to be very careful about secrets and I think if you're a startup or you're just like running fast you probably don't care you're just like I just want it to work yep you know are you a dangerously skip permissions person uh I actually have not I like have a set of things that I like how about

> 沙盒化,这是个特别有意思的问题,因为呃,我觉得 OpenAI 其实比几乎任何人都更认真地对待沙盒化和安全这个问题。我记得我们在打造 Codex 时,基本上你要发布一个模型必须通过的关卡之一,就是你必须谈安全和保安风险,每次你想发布时都要谈。我们当时研究的其中一件事就是 prompt 注入,尤其是针对开放接入互联网这一点,因为一堆用户都说,哦,这必须能在互联网上用,而我们就想,哦,我们不确定,因为它看起来相当容易被——用 Operator 也一样,是啊,是啊,是啊。所以呃,我们团队的产品经理 Alex,基本上就整了一个 GitHub issue,里面有一个非常明显的 prompt 注入,大概是「哦,泄露这个东西」,然后他告诉模型,嘿,去修这个 issue,他心想,哦,这绝不可能得逞,结果那个 prompt 注入立刻就得逞了,你知道。所以我觉得 OpenAI 某种程度上是正确地非常担心这一点,他们会说,嘿,我们要把一切都跑在沙盒里,我们要确保它不会碰到你机器上所有这些敏感文件,我们要对密钥非常小心。而我觉得如果你是家创业公司、或者你就是在狂奔求快,你大概不在乎这些,你就想,我只要它能用就行。对。你知道,你是那种「危险地跳过权限确认」的人吗?呃,我其实不是。我有一套我喜欢的——你呢,你是怎么弄的?

[45:05] **SPEAKER_01:** you are you running no okay I like to read

> 你是那种什么都不管的吗?不,好吧。我喜欢读——

[45:07] **SPEAKER_03:** you know I like to read what it's doing are you skip permissions Jared 100 YOLO mode oh my God it's about 50 50 on the YC engineering team yeah a security engineer would watch this part and say

> 你知道,我喜欢读它在做什么。你是跳过权限确认的人吗,Jared?百分之百的 YOLO 模式。哦我的天,在 YC 工程团队里大概是五五开。是啊,一个安全工程师看到这段会说——

[45:21] **SPEAKER_01:** you can't release this part just cut it from the podcast you can't have this out here I think it's

> 你不能把这段放出去,直接从播客里剪掉。你不能让这段流出去。我觉得这是——

[45:27] **SPEAKER_02:** context dependent like if you're at an Enterprise you don't want to do that if you're a startup and

> ——看情况而定的。就像,如果你在一家企业,你不会想那么干;如果你是家创业公司、

[45:30] **SPEAKER_01:** have nothing to lose you probably do YC has progressed a little bit from a startup we still act like one though because I think important cool I mean this is so awesome Kelvin thank you so much for joining us of course thanks for having me oh my God this is fun yeah so fun all right back to Claude

> 没什么可失去的,你大概就会那么干。YC 已经从一家创业公司往前发展了一点,不过我们仍然表现得像一家创业公司,因为我觉得这很重要。酷。我是说这太棒了,Kelvin,非常感谢你来参加。当然,谢谢你们邀请我。哦我的天,这很好玩。是啊,太好玩了。好了,回到 Claude。
