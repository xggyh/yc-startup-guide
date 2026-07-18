# 全文转录 · 像指挥家一样管理一群编程 Agent:Conductor CEO 的 AI 编码工作流

> ▶ [YouTube](https://www.youtube.com/watch?v=fQmlML9Lay4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/fQmlML9Lay4.md) &nbsp;·&nbsp; Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_01:** Hello, I am Charlie, the co-founder of Conductor, which is an app that lets you orchestrate a bunch of coding agents on your Mac. And we were YC summer 24, and I'd love to show you my setup. So a recent thing that I can't live without is this gooseneck microphone, $20 on Amazon. We are all trying to talk to our computers more. One issue with having like an open floor plan office is that can be pretty distracting.

> 你好,我是 Charlie,Conductor 的联合创始人。Conductor 是一款可以让你在 Mac 上编排一大批编程智能体的应用。我们是 YC 2024 年夏季批次的,我很乐意给你展示一下我的工作环境。最近有个我离不开的东西,就是这个鹅颈麦克风,在亚马逊上花 20 美元买的。我们都在尝试更多地和电脑对话。开放式办公空间的一个问题是,这样会相当容易打扰到别人。

[00:36] **SPEAKER_01:** So one advantage of these is you can like lean over and whisper into cloud and be like, please merge PR 3475. And it's a little bit less disruptive. We all got these in an attempt to encourage more talking to computers. I spend most of my day in Conductor. We're using Conductor to build Conductor.

> 所以这类麦克风的一个好处是,你可以凑过去,对着 cloud 小声说“请合并 PR 3475”。这样干扰会小一点。我们买这些就是想鼓励大家更多地和电脑对话。我一天里大部分时间都待在 Conductor 里。我们正在用 Conductor 来开发 Conductor。

[00:54] **SPEAKER_01:** One thing that I do is I'm constantly kicking off new tasks. So I'm constantly going command N. That was actually a sneak peek of something we are working on, which is cloud workspaces. But I'll do command N and then I'll speak into my computer. So I'll do command N and then I'll speak into my computer.

> 我经常做的一件事就是不停地启动新任务。所以我一直在按 Command+N。刚才其实是我们正在开发的一个功能的小小预览,叫 cloud workspaces(云工作区)。我会按 Command+N,然后对着电脑说话。我会按 Command+N,然后对着电脑说话。

[01:08] **SPEAKER_01:** And say, can you take a look at the latest linear issue and give me a rough pass at how you'd solve it? Stuff like that. And then press Enter. And then I can see that it's running in the sidebar. And while cloud is working, I'll go to another chat.

> 然后说:你能看一下最新的 Linear issue,粗略地给我一个你会怎么解决它的方案吗?诸如此类。然后按回车。接着我就能在侧边栏里看到它正在运行。趁 cloud 在干活的时候,我会切到另一个对话。

[01:24] **SPEAKER_01:** I'm very into keyboard shortcuts. So I try to make everything have a keyboard shortcut. So in this case, I'll do command shift Y. I can see here that this workspace is ready to merge. So I'll take a look at it, give cloud a quick review.

> 我特别喜欢键盘快捷键。所以我尽量让每个操作都有一个快捷键。比如在这种情况下,我会按 Command+Shift+Y。我在这里能看到这个工作区已经可以合并了。于是我会看一看它,快速给 cloud 做个代码审查。

[01:36] **SPEAKER_01:** In this case, it's a pretty small PR. So it looks good to me. But quite often, cloud won't get things exactly right. And I'll give things a comment, like a GitHub style comment. Say, this looks a little bit weird to me.

> 这个例子里,这是一个相当小的 PR。所以在我看来没什么问题。但很多时候,cloud 不会把事情做得完全正确。这时我会加一条评论,像 GitHub 风格的那种评论。比如说:我觉得这里看起来有点怪。

[01:50] **SPEAKER_01:** Why do we need this? Press Enter, get cloud running, and then go back to a different workspace. A big part of how I use Conductor is experimentation. I'm always kicking off workspaces to try different ideas. Most of them don't make it in.

> 我们为什么需要这个?按下回车,让 cloud 跑起来,然后再切回另一个工作区。我使用 Conductor 很大一部分就是在做实验。我总是启动一堆工作区去尝试各种不同的想法。它们大多数最后都没能进到代码里。

[02:05] **SPEAKER_01:** So you can see we have four PRs here that are in review. But there's a bunch of random ideas that I've tried here that are in progress that may never see the light of day. If I like it, then it might get promoted to an internal setting and then an experimental setting. OK, so something I'm very excited about is on the go. I'm going to just speak into my phone and say, let's add a new feature where I can change the theme to hacker mode.

> 所以你能看到这里有四个正在审查中的 PR。但也有一堆我随手尝试的点子还在进行中,它们可能永远不会有面世的一天。如果我喜欢某个想法,它可能会被提升为一个内部设置,再进一步变成实验性设置。好,有件让我非常兴奋的事就是随时随地都能操作。我可以直接对着手机说:我们来加一个新功能,让我可以把主题切换成 hacker(黑客)模式。

[02:32] **SPEAKER_01:** And then I'm going to click Conduct. And then my computer starts working on it. And I can conduct on the go.

> 然后我点一下“Conduct”(指挥)。接着我的电脑就开始动手做这件事了。这样我就能随时随地进行指挥。

[02:39] **SPEAKER_00:** Do you still write code today?

> 你现在还写代码吗?

[02:41] **SPEAKER_01:** No. Yeah, no. Very occasionally, I will edit Tailwind classes or open up an IDE to change a .env file. We actually added a mode that we call Caveman mode, which is you click this, and you can actually type with your keyboard and make changes in a file.

> 不写了。是的,不写了。非常偶尔,我会改一改 Tailwind 的类名,或者打开 IDE 去改一个 .env 文件。我们其实加了一个模式,叫“Caveman mode”(原始人模式),就是你点一下这里,然后你真的可以用键盘打字,直接在文件里做修改。

[03:03] **SPEAKER_01:** Once in a while, you do need to make a change to a file by hand, but it's called Caveman mode for a reason. Most of the time, if I want small edits, I'll highlight and then tell the AI about my comments. Or I'll just speak into my computer and say, that button looks a little too wide. Can you make it smaller? By the way, this thing is now ready to merge.

> 偶尔你确实需要手动改一个文件,但它被叫做“原始人模式”是有原因的。大多数时候,如果我想做小改动,我会选中一段,然后把我的意见告诉 AI。或者我干脆对着电脑说:那个按钮看起来有点太宽了,你能把它做小一点吗?顺便说一句,这个东西现在已经可以合并了。

[03:25] **SPEAKER_01:** So I just wanted to show you, I can now click Archive. And it's gone from my side panel and merged into the code base. And this one, I can see that there are checks running. And once it's finished, I can just click Merge and get it in. We recently added this thing called, Status, in the left.

> 我就想给你演示一下,我现在可以点“Archive”(归档)。它就从我的侧边栏消失了,并被合并进了代码库。而这一个,我能看到有一些检查正在运行。一旦检查完成,我只要点“Merge”(合并)就能把它并进去。我们最近在左侧加了一个叫“Status”(状态)的东西。

[03:41] **SPEAKER_01:** So when something is kicked off, it's in progress. And then once there's a PR created, it's in review. And then once it's merged, it goes into the Done folder. We have this new concept of a dashboard page, where from one place, you can see what all your agents are working on, and then take them to the next action. But we're still messing around with what the interface should look and feel like.

> 所以当某个任务被启动时,它处于“进行中”状态。一旦创建了 PR,它就进入“审查中”。等它被合并后,就进到“Done”(已完成)文件夹里。我们有一个新概念叫仪表盘页面,你可以在一个地方看到你所有智能体正在做什么,然后把它们推进到下一步操作。但我们还在反复琢磨这个界面应该长什么样、用起来是什么感觉。

[04:04] **SPEAKER_01:** But the ideal is you should feel like the CEO of a little company. And you can see all your agents working for you. And they'll bring you up digestible reports. And then you can point them in the right direction if they need some correction, or just merge it in if it looks good.

> 但理想状态是,你应该感觉自己像一家小公司的 CEO。你能看到所有的智能体都在为你工作。它们会给你呈上易于消化的报告。然后如果它们需要纠正,你可以给它们指明正确的方向;如果看起来没问题,你就直接把成果合并进去。

[04:17] **SPEAKER_00:** What are your other main applications, main software that you use?

> 你还用哪些主要的应用程序、主要的软件?

[04:22] **SPEAKER_01:** I use Telegram a decent amount to talk to my open claw. That's been a recent addition for me. I use Spokenly for text-to-speech. That's what comes up when I press Control-Space. It's actually running a local model.

> 我用 Telegram 用得挺多,用来和我的 open claw 对话。这对我来说是最近才加进来的。我用 Spokenly 做文本转语音(注:实际为语音转文本)。我按 Control+Space 时弹出来的就是它。它其实运行的是一个本地模型。

[04:34] **SPEAKER_01:** It's running Parakeet. I have a really beefed up computer. So it's like 128 gigabytes of RAM. Partly so I can run local models like Parakeet. But as a side note, I have just recently ordered the MacBook Neo, the bottom-of-the-line lowest RAM, lowest memory.

> 它运行的是 Parakeet。我有一台配置非常强悍的电脑。它有大约 128GB 的内存。一部分原因就是为了让我能运行像 Parakeet 这样的本地模型。不过顺带一提,我最近刚订了一台 MacBook Neo,是最低端、最小内存、最小存储的那款。

[04:50] **SPEAKER_01:** I got it basically to force myself to use the lowest spec option.

> 我买它基本上就是为了逼自己去用最低配置的那个选项。

[04:53] **SPEAKER_00:** Are there any tweaks that you do still stand by that are the customizations that actually do matter?

> 有没有哪些你至今仍然坚持的调整,也就是那些真正重要的自定义设置?

[04:58] **SPEAKER_01:** A couple of things. We put a lot of time into our skills files and our Cloud MD. If I open it up, you can see this is probably a few hundred lines. There's some interesting things in here. We say engineering practices.

> 有几样。我们在 skills 文件和 Cloud MD 上投入了大量时间。如果我把它打开,你能看到这大概有几百行。里面有一些有意思的内容。我们写了“工程实践”这一部分。

[05:14] **SPEAKER_01:** We're a startup. You're probably used to writing enterprise code. But that's not how we do things around here. And we have a lot of things like that that we've put into our Cloud MD and our skills files over time. What else do I do?

> 我们是一家创业公司。你(指 AI)可能习惯了写企业级代码。但我们这儿不是这么做事的。诸如此类的东西还有很多,是我们长期以来陆续放进 Cloud MD 和 skills 文件里的。我还做了什么呢?

[05:25] **SPEAKER_01:** I always use Fast Mode. That's not a default. If you're trying to token max, you have to be in Fast Mode. I do use a Context 7 MCP. I think that's pretty helpful to get documentation.

> 我一直用 Fast Mode(快速模式)。这不是默认设置。如果你想把 token 用到极致,你就得开着 Fast Mode。我确实会用一个 Context 7 的 MCP。我觉得它在获取文档方面挺有帮助的。

[05:34] **SPEAKER_01:** But other than that, I use most of the things out of the box. One core thing is that we always run Cloud and dangerously accept all permissions. That is not the default. And that is the default way to run Cloud in Conductor. I think something that's really important to us is having clear boundaries between what we call them slot-free zones and having parts of the code base or parts of the documentation that we know is written by a human.

> 但除此之外,大部分东西我都是开箱即用的。有一个核心点是,我们运行 Cloud 时总是“危险地接受所有权限”。这不是默认设置。而这正是在 Conductor 里运行 Cloud 的默认方式。我觉得对我们非常重要的一点,是要在我们所说的“无 slot 区”之间划出清晰的边界,并且让代码库或文档中的某些部分是我们明确知道由人类编写的。

[06:02] **SPEAKER_01:** It's possible that the AI can contribute to the slot-free zones, but every line has to be read by a human. I think it's actually served us pretty well. Because if you're not careful, the AI can get in a vicious cycle where it sees bad code, and then it writes more bad code as a result. And the same thing can happen in the positive direction. We have some lines in our code base that are like, do not touch if you are an AI.

> AI 有可能会为这些“无 slot 区”做出贡献,但每一行都必须由人类来阅读。我觉得这套做法其实给我们带来了很好的效果。因为如果你不小心,AI 会陷入一种恶性循环:它看到了糟糕的代码,结果就写出更多糟糕的代码。同样的事情在正向上也会发生。我们代码库里有些地方写着:如果你是 AI,请不要碰这里。

[06:31] **SPEAKER_01:** This is for human eyes only.

> 这里只供人类查看。

[06:32] **SPEAKER_00:** What's the Conductor tech stack?

> Conductor 的技术栈是什么?

[06:34] **SPEAKER_01:** It's a Towery app. So it's using the native Safari web renderer. And the backend is technically Rust, but we write almost everything in TypeScript. So it's probably 90%, 95% TypeScript on the desktop app. The web app is Elixir.

> 它是一个 Tauri 应用。所以它用的是原生的 Safari 网页渲染器。后端严格来说是 Rust,但我们几乎所有东西都是用 TypeScript 写的。所以桌面应用里大概 90% 到 95% 是 TypeScript。而网页应用是用 Elixir 写的。

[06:50] **SPEAKER_01:** It's a Phoenix app. It's a very small app, because literally all you can do in it right now is just log in. But I'm a huge Elixir fan, and I am always pushing for more Elixir in our code base when we can. But most of what we're doing is in TypeScript. Another thing we talk about is don't let the AI be your architect.

> 它是一个 Phoenix 应用。这是个非常小的应用,因为你现在在里面能做的事情实际上就只有登录。但我是 Elixir 的铁杆粉丝,只要有机会,我总是在推动我们代码库里用更多的 Elixir。不过我们大部分工作还是用 TypeScript。我们常谈的另一件事是:别让 AI 来当你的架构师。

[07:09] **SPEAKER_01:** Even the concept of a workspace here in the sidebar, which in some ways is just an abstraction around a work tree, at least for right now, that's actually going to change soon. But even that concept of a workspace, we as a human had to think that through. The other thing is design and interface decisions. This concept of having all your chats here on the left and then the chat in the middle and then the right sidebar where you can review code changes or run your app, we put a lot of thought into those decisions. And I think if you let the AI make your UI choices for you, you can end up with something that just doesn't feel crafted.

> 就连侧边栏里“工作区”这个概念——它某种程度上只是围绕 work tree(工作树)的一层抽象,至少目前是这样,而且这其实很快就会改变——即便是工作区这个概念,也得由我们人类来把它想清楚。另一件事是设计和界面上的决策。把你所有对话放在左边、把当前对话放在中间、把右侧边栏用来审查代码改动或运行你的应用,这样的布局概念,我们在这些决策上花了大量心思。我觉得如果你让 AI 替你做 UI 选择,最后你很可能得到一个感觉毫无匠心打磨的东西。

[07:49] **SPEAKER_01:** And it's really important to us that it feels crafted. Even this decision, we thought for a long time about how this Open In button should work, which is kind of funny, because now there's so many apps that have this same pattern. The thing that we were really thinking about is whether we should show the icons in the top. I was pretty against showing the icons. I was pretty against showing icons here at first, because it just feels like, OK, in the top bar of our app, we're advertising a different app.

> 而对我们来说,让它感觉是被精心打磨过的,这一点非常重要。哪怕是这个决定——我们花了很长时间思考这个“Open In”(用……打开)按钮应该怎么工作,这有点好笑,因为现在有那么多应用都采用了同样的模式。我们真正在纠结的是,我们是否应该在顶部显示那些图标。我当时挺反对显示这些图标的。一开始我很反对在这里显示图标,因为那感觉就像:好嘛,在我们应用的顶栏里,我们在给另一个应用打广告。

[08:16] **SPEAKER_01:** But now I really like it, and it's like a clear visual of what's going to happen when you click it. I think something we would do a bit differently is building the core of the app around human-ridden APIs and contracts that the AI wouldn't contribute to as much. And then I think that it's important to have big chunks of your code base have free reign for the AI, where you can just throw a ton of different ideas at it and know that it's not going to affect the core infrastructure. And I think right now, the boundaries are a little murky. And that's the thing we're working on improving.

> 但现在我真的很喜欢它,它清晰地从视觉上告诉你点击后会发生什么。我觉得有一件事我们会做得不太一样,那就是把应用的核心构建在由人类主导编写的 API 和契约之上,而 AI 对这些部分的贡献不会那么多。然后我认为,让代码库里有大块区域可以让 AI 自由发挥也很重要,你可以往里面扔一大堆各种各样的点子,并且知道它不会影响到核心基础设施。而我觉得现在,这些边界还有点模糊。这正是我们正在努力改进的地方。

[08:48] **SPEAKER_01:** I think it's really important to us that we stay a little ahead of the frontier, push people's comfort zones a little bit more than they'd expect. When we first launched Conductor, most of the feedback we got was like, this is crazy. I barely can manage one cloud code or one codex. How am I going to manage three or even five? We also purposely made it so you can't edit files directly.

> 我觉得对我们来说非常重要的一点是,要稍微走在前沿的前面一点,把人们推出舒适区的程度,略微超出他们的预期。我们刚推出 Conductor 时,收到的大部分反馈都是:这太疯狂了。我连一个 cloud code 或一个 codex 都勉强管得过来,我怎么可能同时管三个甚至五个?我们还特意做成了你无法直接编辑文件。

[09:15] **SPEAKER_01:** We made it so that any time a workspace has to be a work tree, and it has to then create a PR, and then you have to merge it. So we really enforced our workflow. I think what's exciting but also hard about where we're at is we have to constantly adapt to where the models are going. So that's one reason we are putting so much work into cloud right now is right now, you're going to shut your laptop, and the agents are going to stop running. But it feels like we're very quickly moving to a world where the agents are going to run for 10 times longer, and they're going to be 10 times smarter, and they're going to need to run in an environment that isn't constrained by your Mac's CPU.

> 我们把它做成:任何一个工作区都必须是一个 work tree,然后它必须创建一个 PR,接着你必须去合并它。所以我们真的把我们的工作流给强制推行了下去。我觉得我们现在所处的位置既让人兴奋又很困难,原因在于我们必须不断适应模型的发展方向。这也是我们现在在 cloud 上投入这么多精力的原因之一:现在你一合上笔记本电脑,智能体就会停止运行。但感觉我们正在非常迅速地迈向这样一个世界——智能体会运行长 10 倍的时间,会聪明 10 倍,而且它们将需要运行在一个不受你 Mac 的 CPU 限制的环境里。

[09:52] **SPEAKER_00:** It seems like you're building Conductor in a very opinionated way. How do you build a conviction behind your decisions?

> 看起来你在用一种非常有主见的方式打造 Conductor。你是如何为自己的决策建立起坚定信念的?

[09:57] **SPEAKER_01:** That's a great question, because especially for our audience, they want a lot of configuration. And I do think it is important for the tool to be flexible and to feel like yours. But the way we build conviction is we force ourselves to use it. Because actually, we don't even force it. Like, we just use it every day.

> 这是个很好的问题,因为尤其对我们的用户群来说,他们想要大量的可配置选项。我也确实认为,让工具保持灵活、让它感觉像是属于你自己的,这很重要。但我们建立信念的方式,就是逼自己去用它。其实我们甚至都不用逼——我们就是每天都在用它。

[10:17] **SPEAKER_01:** And so if it doesn't feel right, we quickly can decide. But we're not big on analytics or looking at our A-B testing. It's very much a gut feel. This feels right. When I click this, it feels right that it opens in the center.

> 所以如果哪里感觉不对,我们能很快做出判断。但我们不太看重数据分析,也不怎么去看我们的 A/B 测试。这在很大程度上是一种直觉。这个感觉对了。当我点这个的时候,它在中间打开,这个感觉是对的。

[10:33] **SPEAKER_01:** And that way, I don't need a separate composer. And I can type messages. I can type messages here.

> 这样一来,我就不需要一个单独的输入框了。我可以打字发消息。我可以在这里打字发消息。

[10:39] **SPEAKER_00:** And it all feels unified. You sound like you default to Cloud Code in a lot of places. But Conductor supports Codecs too.

> 而且整体感觉很统一。听起来你在很多地方默认用的是 Cloud Code。但 Conductor 也支持 Codex。

[10:45] **SPEAKER_01:** When do you reach for Codecs? I've recently actually been using Codecs more. Codecs is like the workhorse. It will power through a specific problem. Or it's not afraid to do a ton of tool calls and debug something with me for a long time.

> 你什么时候会用 Codex 呢?我最近其实用 Codex 用得更多了。Codex 就像是一头任劳任怨的“主力马”。它会一鼓作气啃下一个具体的问题。或者它不怕做大量的工具调用,陪我长时间地调试某个东西。

[10:59] **SPEAKER_01:** Cloud, I'll reach for when I want a little more back and forth. I feel like Opus is just a little more creative, like a little more of a partner. I would say when I'm building out a new feature, I probably would instinctively reach for Opus. And then when I'm like, OK, now we just want to get stuff done, I'll go to Codecs.

> 而当我想要多一点来回讨论的时候,我会选 Cloud。我觉得 Opus 就是更有创造力一点,更像是一个伙伴。我会说,当我在开发一个新功能时,我大概会本能地去用 Opus。然后当我心想“好,现在我们只想把事情做完”的时候,我就会转去用 Codex。

[11:17] **SPEAKER_00:** Why isn't just a terminal good enough?

> 为什么单单一个终端还不够好?

[11:20] **SPEAKER_01:** There's a reason we moved from terminal interfaces to GUI interfaces in the 80s. I think humans are spatial visual creatures. And having a command line interface just feels very restrictive, and I think it maybe works for the AI brains better than the human brains. But I think just like, I want to know that, OK, my chats are over here, and my review panel is here. I can talk to the AI in the middle.

> 我们在 80 年代从终端界面转向图形界面(GUI),是有原因的。我觉得人类是依赖空间和视觉的生物。而使用命令行界面就是感觉很受限,我认为它也许对 AI 的“大脑”比对人类的大脑更管用。但我觉得,就好比,我想知道:好,我的对话在这边,我的审查面板在这里,我可以在中间和 AI 对话。

[11:45] **SPEAKER_01:** I just think, yeah, bottom line, humans are visual, visual creatures. I also think, zooming in a little bit, there's a lot that you can't do in a terminal that you can do with a user interface.

> 我就是觉得,是的,归根结底,人类是视觉动物,是依赖视觉的生物。我还觉得,再具体一点看,有很多事情你在终端里做不到,但用图形用户界面就能做到。

[12:01] **SPEAKER_00:** Let's talk about token maxing.

> 我们来聊聊“把 token 用到极致”(token maxing)吧。

[12:03] **SPEAKER_01:** Yeah.

> 好啊。

[12:03] **SPEAKER_00:** What's your high watermark on lines of code in a day or spend in a month?

> 你在一天的代码行数,或一个月的花费上,最高纪录是多少?

[12:07] **SPEAKER_01:** I think the highest spend was when we were starting out Conductor, like in July 2025. I spent $22,000 on tokens that month. Granted, that was with a previous generation of models. And the lines of code must have been like tens of thousands that month. I'm very big on spending, like on token maxing, like using fast mode, like think extra hard, like high effort all the time.

> 我想最高的花费是在我们刚开始做 Conductor 的时候,大概是 2025 年 7 月。那个月我在 token 上花了 22,000 美元。当然,那用的是上一代的模型。那个月的代码行数肯定得有好几万行。我非常舍得花钱,比如把 token 用到极致,比如用 fast mode,比如让它“格外努力地思考”,一直保持高投入。

[12:33] **SPEAKER_01:** But we're not being on lines of code. We are. We try and keep the lines of code minimal, actually. There's a bunch of reasons for this, but I think you can quickly spiral. Your code base can spiral out of control if you're not careful about the lines of code added.

> 但我们并不追求代码行数。我们……其实我们尽量把代码行数保持在最少。这么做有一堆原因,但我觉得情况会很快失控。如果你不小心控制新增的代码行数,你的代码库可能会失控地膨胀。

[12:46] **SPEAKER_01:** But I think about it very differently if I'm starting up an app versus working in an established code based like Conductor.

> 但如果是从零开始搭一个应用,跟在像 Conductor 这样已经成型的代码库里工作,我对这件事的看法是非常不一样的。

[12:53] **SPEAKER_00:** What's different about your workflows today from, say, six months ago?

> 你今天的工作流程,和比如说六个月前相比,有什么不同?

[12:57] **SPEAKER_01:** On a lot of hard PRs, I would open an IDE and make changes by hand. And I also use GitHub, like the web app. It's a lot less now because I can just review the code changes here in Conductor and add comments here if I need to. We do have a lot of PR checks that run. And so that's why we recently added this Checks tab, which lets us just add comments from GitHub into Conductor.

> 在很多难搞的 PR 上,我以前会打开 IDE 手动做修改。我还用 GitHub,就是那个网页应用。现在用得少多了,因为我可以直接在 Conductor 里审查代码改动,如果需要的话就在这里加评论。我们确实有很多会运行的 PR 检查。所以这也是我们最近加了这个 Checks(检查)标签页的原因,它让我们能把 GitHub 上的评论直接引入到 Conductor 里。

[13:24] **SPEAKER_00:** What's the most surprising thing you've seen someone else do with Conductor?

> 你见过别人用 Conductor 做过的最让你意外的事情是什么?

[13:28] **SPEAKER_01:** One was someone built a mobile version of Conductor by hacking together a bunch of art. I don't actually even really know how it works, but I know it's spoofing IPC calls to our desktop app, which is pretty interesting. I think, honestly, Gary has shown us a lot of what you can do with Conductor. He is really putting it to the test. I think I've learned from him a bit about how hard you can go on skills.

> 有一件是,有人东拼西凑地捣鼓出了一个 Conductor 的移动版。我其实都不太清楚它是怎么工作的,但我知道它在伪造发给我们桌面应用的 IPC 调用,这挺有意思的。说实话,我觉得 Gary 向我们展示了很多用 Conductor 能做到的事情。他真的是在把它推向极限。我觉得我从他那里学到了一点,就是在 skills 上你能玩得多狠。

[13:54] **SPEAKER_01:** Skills are very much like a first class thing in GStack. And there's some interesting ideas there, I think, especially around onboarding. And we've added, actually, a specific mode for him called Gary mode, which, by default, does not collapse any of the tool calls. So you can see all the tool calls are default on collapse. And you can even actually see Gary's face here if you're in Gary's mode.

> 在 GStack 里,skills 非常像是一个“一等公民”。我觉得那里有一些很有意思的想法,尤其是在新手引导方面。我们其实还专门为他加了一个模式,叫“Gary mode”,在这个模式下,默认不会折叠任何工具调用。所以你能看到所有工具调用默认都是折叠状态(注:此处应为“默认展开”)。而且如果你处在 Gary 模式里,你甚至真的能在这里看到 Gary 的脸。

[14:17] **SPEAKER_00:** What feels obvious to you and your team that the rest of the world doesn't fully understand yet?

> 有什么事情对你和你的团队来说显而易见,而世界上其他人还没有完全理解?

[14:22] **SPEAKER_01:** I think there's a lot of cool stuff to explore with collaboration between humans and the AIs. Should you be able to communicate with subagents? Should you be able to have multiplayer chats where multiple people are working on the same thing with the AIs? And then, of course, a metaphor we'll often talk about is feeling like the conductor of an orchestra. You wave the baton, and the instruments are playing in unison.

> 我觉得在人类与 AI 的协作方面,有很多很酷的东西值得探索。你是否应该能够和子智能体(subagents)沟通?你是否应该能进行多人对话,让多个人和 AI 一起协作同一件事?然后,当然,我们经常谈到的一个比喻,就是感觉像是一支管弦乐队的指挥。你挥动指挥棒,各种乐器齐声演奏。

[14:45] **SPEAKER_01:** And then once in a while, you want to go to the trumpet player and be like, OK, you're out of tune. And then you want to zoom out to the string section, and you should play a bit faster. But then most of the time, you're conducting at the orchestra level. Code is almost like sawdust now, in that it used to be that code was the thing you were building. It was the structure.

> 然后偶尔,你会想走到小号手那边,对他说:好,你跑调了。接着你会想拉远,面向整个弦乐组说:你们应该演奏得再快一点。但在大多数时间里,你是在整个乐队的层面上进行指挥。代码现在几乎就像是锯末一样,因为过去代码本身就是你在构建的东西,它是那个结构。

[15:07] **SPEAKER_01:** You were putting time into crafting the code. And now, you're putting time into describing what you want and how you want it to be built. And the code is almost just like sawdust that comes out of that process. And that leads to a lot of interesting conclusions. One of them is really what matters is your prompts.

> 你会把时间花在精雕细琢代码上。而现在,你把时间花在描述你想要什么、以及你想让它怎么被构建出来。代码几乎就只是这个过程中掉出来的锯末罢了。这会引出很多有意思的结论。其中之一就是,真正重要的是你的提示词(prompts)。

[15:26] **SPEAKER_01:** And when the next generation of models come out, you can just rerun your prompts again, and then you'll get new code, and the old code didn't really matter. I think that's one thing that like, the world is slowly waking up to. I think the submit a prompt, like the prompt request feature, is sort of like an early experiment with malleable software. The metaphor that I always think of when I think of malleable software is like video games, and how when you play Call of Duty, the structure of the game is the same for everyone, and the skeleton is the same. But each person can, I don't know, use custom skins, or faster reload speeds, or whatever.

> 而当下一代模型问世时,你只要把你的提示词重新跑一遍,就能得到新的代码,而旧的代码其实并不重要。我觉得这是世界正在慢慢意识到的一件事。我认为“提交一个提示词”,也就是那个 prompt request(提示词请求)功能,某种程度上像是对“可塑软件”(malleable software)的一次早期实验。每当我想到可塑软件,我脑海里浮现的比喻就是电子游戏——比如你玩《使命召唤》时,游戏的结构对每个人来说都是一样的,骨架是相同的。但每个人都可以,怎么说呢,用自定义皮肤,或者更快的换弹速度,或者其他什么。

[16:02] **SPEAKER_01:** And the same way you can mod a video game, I want you to be able to mod Conductor, and build in your own workflows a little bit. It's important that the structure feels the same, and people want software that's been crafted and been really thought through. But I also, video game mods make the game feel more like your own. And I think that's going to happen with software as well.

> 就像你可以给电子游戏做 mod 一样,我希望你也能给 Conductor 做 mod,稍微把你自己的工作流搭建进去。重要的是,整体结构给人的感觉是一致的,人们想要的是经过精心打磨、真正深思熟虑的软件。但我同时也觉得,游戏 mod 会让游戏更有“属于你自己”的感觉。我认为这种情况在软件上也会发生。
