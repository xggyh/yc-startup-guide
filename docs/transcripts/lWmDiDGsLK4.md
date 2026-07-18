# 全文转录 · 软件创造的未来:Replit CEO 谈应用软件价值归零与 Agent 栖息地

> ▶ [YouTube](https://www.youtube.com/watch?v=lWmDiDGsLK4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/lWmDiDGsLK4.md) &nbsp;·&nbsp; The Future of Software Creation with Replit CEO Amjad Masad

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_00:** I was asked to talk about the future of software. So a lot of this talk is going to be about what we're doing at Replit, where we think the future of software is headed, and some kind of trying to make some predictions or try to think out loud about really what the future holds. My mental model for our business and really for the moment we're in today, if you think back on the history of computing, mainframes were kind of the first mainstream computing devices, as mainstream as it gets back then. And to use a mainframe, you needed to be an expert. And then PCs came around, and initially PCs were kind of toys.

> 有人请我来谈谈软件的未来。所以这次演讲很大一部分会讲我们在 Replit 正在做的事、我们认为软件的未来将走向何方,以及尝试做一些预测,或者说把对未来真正走向的思考大声地讲出来。关于我们的业务、也关于我们今天所处的这个时刻,我的思维模型是这样的:如果你回顾计算的历史,大型机算是第一批主流计算设备——在当时它已经是最主流的了。而要使用大型机,你必须是专家。后来个人电脑出现了,一开始个人电脑有点像玩具。

[00:45] **SPEAKER_00:** You bought a Mac and you did Mac paint and things like that. There wasn't a real business use case. I mean, people made fun of Apple at the time until the exception. And then there was the Excel sheet. The Excel sheet was the first software that was actually useful on computers.

> 你买了一台 Mac,用它玩 MacPaint 之类的东西。并没有真正的商业用途。我是说,当时人们一直取笑苹果,直到出现了那个例外。然后 Excel 表格出现了。Excel 表格是电脑上第一款真正有用的软件。

[01:04] **SPEAKER_00:** And now PCs run the world economy. Like they actually, if you go to a data center, it's also only PCs. It's x86 computers. So you go from something that was used by a small group of experts that had to have a lot of training to something that started sort of as a toy and is used by everyone. Same thing with software engineering.

> 而如今个人电脑驱动着整个世界经济。真的,如果你去数据中心看看,里面也全是个人电脑,都是 x86 计算机。所以你看,一样东西从被一小群受过大量训练的专家使用,变成了一开始像玩具、如今人人都在用的东西。软件工程也是同样的道理。

[01:29] **SPEAKER_00:** Like the modern software engineering career, you can sort of trace it back to the seventies with the rise of maybe Unix and the C programming language. That's when people started kind of being trained to become software engineers. You still needed four or five, six years of college education. You needed another two or three years of training on the job, to be able to actually do the job very well. I think today software is going through the same transition from something that only experts do to something that anyone can do.

> 现代软件工程这门职业,大致可以追溯到七十年代,随着 Unix 和 C 语言的兴起而出现。那时候人们开始接受培训、成为软件工程师。你仍然需要四五、六年的大学教育,还需要再花两三年在工作中训练,才能真正把这份工作做得很好。我认为今天软件正在经历同样的转变——从只有专家才能做的事,变成任何人都能做的事。

[02:13] **SPEAKER_00:** And this is what we're really building Replit for. I've been working at Replit for like almost nine years now. And our vision has always been to solve programming, to like make programming, make it so that anyone can write software. So we built an IDE. We built language runtimes.

> 而这正是我们打造 Replit 的初衷。我在 Replit 已经工作快九年了。我们的愿景一直是"解决编程这件事",让编程变得人人都能写软件。所以我们做了一个 IDE,做了各种语言运行时。

[02:35] **SPEAKER_00:** We built like a online sandbox environment. We built deployments. We built cloud services around all of that. And then when AI came on the scene, we realized that the ultimate expression of our mission is to make it so that you don't have to code. Code is the sort of bottleneck to actually getting a lot more people making software.

> 我们做了一个在线沙盒环境,做了部署功能,还围绕这一切构建了云服务。后来当 AI 登场时,我们意识到我们使命的终极表达,是让你根本不必写代码。代码其实是让更多人能做软件的那个瓶颈。

[02:55] **SPEAKER_00:** So around, you know, late 23, early 24, we decided to put all of our work, all of our resources into Agents. At the time, Agents sort of barely worked, but you could tell by looking at a few benchmarks that were headed there. So SWE Bench is a software engineering benchmark. It is basically a collection of issues on GitHub from major repositories and the unit tests and pull requests sort of end state of those issues. And the way you test an agent is you put it in an environment and have it solve some of those issues.

> 所以大概在 23 年底、24 年初,我们决定把所有的工作、所有的资源都投入到智能体(Agents)上。当时智能体勉强能用,但你从几个基准测试就能看出趋势正朝那个方向走。SWE Bench 是一个软件工程基准测试,基本上就是从主要代码仓库收集的一批 GitHub issue,以及这些 issue 对应的单元测试和 pull request 的最终状态。测试一个智能体的方式,就是把它放进一个环境里,让它去解决其中一些 issue。

[03:29] **SPEAKER_00:** You could tell. Like in 22, sort of, it barely worked. 23, it started sort of working. And you could tell early, sort of early 24, where we're on this trend, where you could tell that software engineering is getting automated, or like big parts of software engineering is getting automated. And now we're probably, I think this is like a little outdated.

> 你能看得出来。比如 22 年,它勉强能用;23 年,开始有点能用了。到 24 年初,你就能早早看出这个趋势——你能看出软件工程正在被自动化,或者说软件工程的很大一部分正在被自动化。而现在我们大概,我觉得这个数字有点过时了。

[03:48] **SPEAKER_00:** We're like at 70, 80% SWE Bench. Now, if this benchmark gets saturated, doesn't mean that we automated all of software engineering, but we're on our way to make really useful, arguably it's already here, really useful software engineering agents. And by the way, this is true of any agent. If any of you are building sort of agents, startups, just like really believe that it's coming. Really, really like, I keep telling my team, we need to be okay with building crappy products today because two months down the line, the models will get better and your business, your product will suddenly become viable.

> 我们大概在 SWE Bench 上达到 70%、80% 了。当然,即便这个基准被"刷满",也不代表我们把全部软件工程都自动化了,但我们正走在打造真正有用的软件工程智能体的路上——甚至可以说它已经到来了。顺便说一句,这对任何智能体都成立。如果你们当中有人在做智能体、做创业,就真的要相信它正在到来。真的,我一直跟我的团队说,我们得能接受今天做出很烂的产品,因为两个月后模型会变得更好,你的业务、你的产品会突然就变得可行了。

[04:28] **SPEAKER_00:** So today's kind of, the moment for agents. So Replit kind of went all in on agents, but agents that can write code is actually the easy part. The hard part is the infrastructure around it. Sometimes I call it the habitat for which the agent lives in. So what you need is you need a virtual machine, ideally in the cloud, ideally not on your computer, because agents can actually also mess up your computer.

> 所以今天可以说是智能体的时刻。Replit 算是全力押注在智能体上,但能写代码的智能体其实是简单的部分。难的部分是它周围的基础设施。我有时把它称作智能体所栖居的"栖息地"。你需要的是一台虚拟机,最好在云端,最好不在你自己的电脑上,因为智能体其实也可能把你的电脑搞坏。

[04:58] **SPEAKER_00:** They could do a lot of, scary things. So it needs to be sandboxed. It needs to be scalable. If you're running a product like Replit, you need to be able to scale up to like millions of users. And you need to be able to support every language out there, every package out there.

> 它们可能做很多吓人的事。所以它需要被沙盒隔离,需要可扩展。如果你运营的是像 Replit 这样的产品,你得能扩展到数百万用户的规模。而且你得能支持世界上每一种编程语言、每一个软件包。

[05:18] **SPEAKER_00:** The way software engineering agents are trained today is they're trained on standard Linux environment. They need to be able to use the shell. They need to be able to write to files, read files. They need to be able to write to files, read files. But they also need to be able to install packages, either system level packages, Linux packages, but also language packages.

> 如今软件工程智能体的训练方式,是在标准 Linux 环境中训练的。它们需要能使用 shell,需要能写入文件、读取文件。它们需要能写入文件、读取文件,但同时也需要能安装软件包——既包括系统级的包、Linux 包,也包括语言层面的包。

[05:37] **SPEAKER_00:** In many cases, agents want to actually use more programming languages. And so a lot of environments today where people are trying to build agents are very constrained. But what you want is an environment as open as possible, similar to the kind of environments that software engineers work in. So what kind of other things you need to ship real software? You need deployments.

> 在很多情况下,智能体其实想使用更多的编程语言。所以如今很多人搭建智能体所用的环境都很受限。但你想要的是一个尽可能开放的环境,类似于软件工程师工作时所处的那种环境。那么要交付真正的软件,你还需要哪些东西?你需要部署能力。

[05:58] **SPEAKER_00:** You need databases. Really think about everything you do as a software engineer. And all those tools need to be accessible to software engineering agents. So actually, I saw earlier today, if you were at Karpathy's talk, he talked about how the coding part is the easy part, so similar to the points I'm making. But he talked about all the different things that are really unsolved.

> 你需要数据库。真的,想想你作为软件工程师所做的一切,所有那些工具都需要对软件工程智能体开放可用。其实我今天早些时候看到,如果你在场听了 Karpathy 的演讲,他讲到写代码是简单的部分,和我讲的观点类似。但他谈到了各种真正还没解决的问题。

[06:21] **SPEAKER_00:** But in reality, we actually solved a lot of them. So Repl.it out of the gate comes with auth. Agents are actually not very good at authentication. It's better to use a service, built-in service.

> 但实际上,我们已经解决了其中很多。Replit 一开箱就自带身份认证功能。智能体其实并不太擅长做认证。更好的做法是用一个服务、一个内置的服务。

[06:31] **SPEAKER_00:** So Repl.it, actually, one line of code, we turn on auth. So when asked Repl.it agent to integrate auth, it will actually just use Repl.it auth.

> 所以在 Replit 上,其实只要一行代码,我们就能开启认证。所以当你让 Replit 智能体集成认证时,它其实就会直接用 Replit 自带的认证。

[06:42] **SPEAKER_00:** It will just basically turn on a setting. And then you have user authentication. You have user management. Those users' information are being stored in the database. You can also, obviously, deploy the app.

> 它基本上只需打开一个开关。然后你就有了用户认证,有了用户管理,这些用户的信息会被存进数据库。当然,你也可以直接部署这个应用。

[06:55] **SPEAKER_00:** You can link a domain to it. We have secrets management. Secure. Ways of using API keys. We have background jobs.

> 你可以给它绑定一个域名。我们有密钥管理,有安全地使用 API 密钥的方式。我们还有后台任务功能。

[07:04] **SPEAKER_00:** A lot of applications need to be able to run continuously in the background, especially in this era of agents. Storage, again, agents need to be able to store things. They need to be able to grab things from the web, images, documentation, whatever, and store them for the application to use them in the future. Few other things on the roadmap, universal model access. So it's really a pain right now to ask the model to ask for an application that can generate and they can do something with it, images or videos.

> 很多应用需要能在后台持续运行,尤其是在这个智能体时代。还有存储,同样地,智能体需要能存储东西。它们需要能从网上抓取东西——图片、文档,不管是什么——把它们存下来供应用日后使用。路线图上还有几件事,比如通用模型访问。现在要让模型去请求一个能生成图片或视频、并能对其做处理的应用,真的很麻烦。

[07:33] **SPEAKER_00:** You have to figure out which model to use. You have to go get an API key and do all of that. Pretty soon, any model that you ask for at Repl.it, they'll be just available in your app directly. We'll handle the billing and the API integration, all of that.

> 你得搞清楚该用哪个模型,得去弄一个 API 密钥,还要做一大堆这些事。很快,在 Replit 上你所要的任何模型,都会直接在你的应用里就能用。计费、API 集成这些事我们都会替你处理好。

[07:47] **SPEAKER_00:** Payments is very important. Payments not just for your users to pay for your application. Say you're building a startup on Repl.it, you're an entrepreneur. You obviously need to collect.

> 支付非常重要。支付不只是为了让你的用户为你的应用付费。假设你在 Replit 上做创业,你是个创业者,那你显然需要收款。

[07:59] **SPEAKER_00:** You need to collect user payments. But also, I think sometime in the future, you would want your agent to have some kind of wallet to be able to go pay for services. So let's say your agent decides that it needs a Toolio integration in Repl.it or whatever system you're using doesn't have a Toolio integration. It should be able to go put in its credit card and provision that service in the background.

> 你需要收取用户的付款。但同时我觉得在未来某个时候,你会希望你的智能体拥有某种钱包,能够去为各种服务付费。比如说,你的智能体判断它在 Replit 里需要一个 Twilio 集成,或者你用的系统里没有 Twilio 集成,那它应该能自己填上信用卡、在后台把那个服务开通好。

[08:26] **SPEAKER_00:** A more radical idea is that your agent needs to be able to hire people. For example, if it hits a captcha and it doesn't know how to solve a captcha, it should go and task grab it and ask a human to go solve the captcha for it. Whatever it is, there's a lot of tasks that you still need humans for, and you would want your agent to be able to have money to pay for services. And similarly, agent-to-agent, you would want your agent to be able to go on the market and find other agents it can hire. So many YC startups are black ops.

> 一个更激进的想法是,你的智能体需要能雇人。比如说,如果它遇到一个验证码而它不知道怎么解,它就应该去找个众包任务平台,请一个人来替它解这个验证码。不管是什么,还有很多任务仍然需要人来做,你会希望你的智能体能有钱去为这些服务付费。同样地,智能体对智能体,你也会希望你的智能体能够到市场上去找它可以雇用的其他智能体。有很多 YC 创业公司都在悄悄地……

[08:59] **SPEAKER_00:** building agents, sort of agents for accounting, agents for sales. And so you need your software engineering agents to be able to integrate those agents as well. So I know a lot of people think of MCP as such an agent-to-agent tool, but actually MCP is a more traditional RPC protocol. So it's not really going to solve this. Another model on our sort of business or technology is think about sort of the level of autonomy.

> ……做各种智能体,比如做会计的智能体、做销售的智能体。所以你需要你的软件工程智能体也能集成那些智能体。我知道很多人把 MCP 当作这样一种智能体对智能体的工具,但其实 MCP 更像是一种传统的 RPC 协议,所以它其实解决不了这个问题。理解我们业务或技术的另一个模型,是思考"自主等级"。

[09:25] **SPEAKER_00:** So when I started working on what Replit would become like years ago, perhaps decades ago, the state-of-the-art code assist was a language server, right? That's IntelliSense if we're using VS Code. And you can think of it as level one autonomy. If you think about the sort of drive assists in self-driving cars or like in cars, you know, it would be kind of the lane assist. That would be the first level.

> 多年前——也许几十年前——当我开始做后来成为 Replit 的这个东西时,当时最先进的代码辅助是语言服务器,对吧?如果你用 VS Code,那就是 IntelliSense(智能感知)。你可以把它看作第一级自主。如果类比自动驾驶汽车里的那种驾驶辅助,它大概就相当于车道保持辅助,那算是第一级。

[09:50] **SPEAKER_00:** AI code completion, co-pilot, that would be level two. Level three. Level three is what we worked on when Replit agent first launched. Agent V2, I would call it almost 3.5.

> AI 代码补全,也就是 Copilot,那算第二级。第三级——第三级就是我们在 Replit 智能体最初发布时所做的。到了 Agent V2,我会把它称作接近 3.5 级。

[10:05] **SPEAKER_00:** It can work up to 10, 15 minutes on its own, but it still needs your input every now and then to test the app and make sure the app is working. And right now we're working on V3. I'll talk a little bit more about V3 in a second, but V3 is sort of level four, right? Like you're almost there. It still needs some of your attention.

> 它能自主工作长达 10 到 15 分钟,但仍然时不时需要你的介入去测试应用、确保应用能正常运行。而现在我们正在做 V3。我待会儿会多讲一点 V3,但 V3 大概算是第四级,对吧?就是说你已经快到那一步了,但它仍然需要你分出一些注意力。

[10:24] **SPEAKER_00:** But it kind of works fully autonomously or plus, which I assume we're going to get to in the next couple of years, you can really spin up a thousand agents, give them a lot thousand problems and reliably be confident that like 95% of them is going to work. Like we're going to have a really higher liability rate. Any kind of engineer or product manager, really anyone can spin up hundreds, if not thousands of agents. So we're going to have a lot of engineers to do work on their behalf. So they need very little supervision and therefore you can increase your impact exponentially as a programmer.

> 但它可以说是完全自主运行了。再往上一级(我猜我们在未来几年就会达到),你真的能一次启动一千个智能体,给它们一千个问题,并且可以可靠地相信其中大约 95% 会成功。也就是说我们会有非常高的可靠率。任何工程师或产品经理,真的说任何人,都能一次启动几百、甚至上千个智能体。所以我们会有大量的"工程师"替我们干活。它们几乎不需要监督,因此作为程序员,你的影响力可以指数级地放大。

[11:03] **SPEAKER_00:** So what we're working on right now with Agent V3 is that, you know, it's based on basically three pillars. One is end-to-end testing. So today, computer use is in models. What's called computer use, if you've used OpenAI operator, it's the idea that models can go into a computer, you know, click around and use a computer like a human does. They're slow, they're expensive, they're not very good.

> 我们现在做 Agent V3,基本上建立在三大支柱之上。第一个是端到端测试。如今,模型里已经有了"计算机使用"能力。所谓"计算机使用",如果你用过 OpenAI 的 Operator,就是指模型能够进入一台计算机,像人一样点来点去、操作电脑。它们目前又慢、又贵、又不太好用。

[11:39] **SPEAKER_00:** But this is what I talked about earlier. You want to build a product at the edge of what's possible. Right now, the edge of what's possible is like computer use, in my opinion, is really at the frontier of what these models could do. Right now, the edge of what's possible is like computer use, in my opinion, is really And I think, you know, I think it's going to be a lot of work. And I think, you know, I think it's going to be a lot of work.

> 但这正是我前面说的:你要在"可能性的边缘"去做产品。目前可能性的边缘就是计算机使用,在我看来,它真的处于这些模型能力的最前沿。目前可能性的边缘就是计算机使用,在我看来,它真的……而且我觉得,这还需要做大量的工作。我觉得这还需要做大量的工作。

[11:53] **SPEAKER_00:** I think over the next three to six months, they're going to get a lot better. And it's going to enable an entire new market and also probably start to automate a lot of real jobs. Once we have app testing, you know, this kind of annoying thing that ReplitAsian does where it keeps asking you to do QA for it, it'll start doing QA on its own. And that will allow it to work, you know, 30, 40, up to an hour, maybe two hours of work. So the hype today is test time.

> 我觉得在接下来的三到六个月里,它们会变好很多。它将催生一个全新的市场,可能也会开始自动化很多真实的工作岗位。一旦我们有了应用测试能力,Replit 智能体现在那件烦人的事——老是让你替它做 QA(质量检验)——它就会开始自己做 QA。这将让它能连续工作 30、40 分钟,长达一小时,甚至可能两小时。所以如今大家热议的是"测试时算力"(test time)。

[12:23] **SPEAKER_00:** If you think about the sort of O3 or like O-series models or DeepSeek R1, the kind of main insight there is the more tokens the model is able to consume or produce, the more intelligent it gets. Now, today, with something like O3, the model is generating a lot of tokens and trying to reason, but a lot of it is sort of solipsistic. It doesn't get feedback from the environment. It's almost like it's just sitting in place and thinking. What you'd want in a real computer environment is for the model to generate hypothesis and test this hypothesis in real time.

> 如果你想想 O3 这类、或者说 O 系列模型、又或者 DeepSeek R1,其核心洞见在于:模型能够消耗或产生的 token 越多,它就变得越聪明。而如今,像 O3 这样的模型,会生成大量 token 去尝试推理,但其中很多是"自说自话"式的,它不会从环境中得到反馈,几乎就像它只是原地坐着空想。而在真实的计算机环境里,你想要的是让模型提出假设,并实时地去检验这个假设。

[13:06] **SPEAKER_00:** So at Replit, we built a fully transactional, reversible file system. So when you're on Replit, every edit you make to the file system is an atomic snapshot in time. And that allows us to have... We have very cheap copy and write forks of the file system, and so our idea for this is that anytime there's a tough problem, or basically if you have a lot of budget, you can have it on all the time, but every time the agent is making a big change, it forks itself and the environment a number of times to solve this problem in different ways and then find the best solution. And then take that solution and merge it into the main branch.

> 所以在 Replit,我们构建了一个完全事务化、可回滚的文件系统。当你在 Replit 上时,你对文件系统所做的每一次编辑,都是某个时间点上的一个原子快照。这让我们能够拥有……我们有非常廉价的写时复制(copy-on-write)文件系统分叉。我们的设想是,每当遇到一个棘手的问题时——或者基本上如果你预算充足,你可以一直开着这个功能——每次智能体要做一个大改动,它就会把自己和环境分叉出好几份,用不同的方式去解决这个问题,然后找出最好的方案,再把那个方案合并回主分支。

[13:57] **SPEAKER_00:** So think about, you know, the idea of simulations. Like, when you're thinking about the problem, you're often simulating different branches of things that you could do. You have different hypotheses you want to test. And so we want to also give agents the ability to do that. So at any given problem, generating a ton of different ways of doing it, and then testing all of them in parallel.

> 所以想想"模拟"这个概念。当你在思考一个问题时,你常常会在脑中模拟你可以采取的不同分支路径,你有想要检验的不同假设。所以我们也想赋予智能体这样的能力:对任何给定的问题,生成一大堆不同的解法,然后并行地把它们全部测试一遍。

[14:23] **SPEAKER_00:** This will bring up reliability of agents by, I think, two to three folds. So that's sampling and simulations. And then finally is for the model to be able to generate tests for every feature that it creates. Today, Repl. Agent often creates a feature and then later on breaks that feature, but also true of Clot Code and Cursor and all the others.

> 我认为这会把智能体的可靠性提升两到三倍。这就是"采样与模拟"。最后一点,是让模型能够为它所创建的每一个功能生成测试。如今,Replit 智能体经常做出一个功能,然后过一会儿又把这个功能弄坏了——不过这对 Claude Code、Cursor 以及其他所有工具也都成立。

[14:51] **SPEAKER_00:** So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent...

> 所以我们想做到的是,一旦智能体……一旦智能体……一旦智能体……一旦智能体……一旦智能体……

[14:53] **SPEAKER_00:** So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent... So we want to make it so that once the agent makes a set of changes or a feature, it always has tests that it runs on every change to make sure it's not breaking the software.

> 所以我们想做到的是,一旦智能体……一旦智能体……一旦智能体……一旦智能体……一旦智能体做出一组改动或一个功能,它总会有测试,并在每次改动时都运行这些测试,以确保它没有把软件弄坏。

[15:02] **SPEAKER_00:** This is actually harder than it sounds. It sounds like, okay, write tests and let's run them, but often actually models are pretty bad at generating unit tests. So there's still a lot of work to do there. It needs to be fast as well so that it happens on every change. So that's what we're working on with v3.1.

> 这其实比听起来要难。听上去好像就是"好,写测试,然后跑一下嘛",但实际上模型在生成单元测试方面往往相当差。所以这方面还有很多工作要做。它还需要足够快,才能在每次改动时都执行。这就是我们在 V3.1 里正在做的事。

[15:23] **SPEAKER_00:** V3, that's a lot of infrastructure work. We want to create the best habitat for agents to live in and be able to be the most reliable possible. But let's fast forward to what I talked about with level five autonomy. Really the most autonomous system we can think of.

> V3 涉及大量的基础设施工作。我们想为智能体打造最好的栖息地,让它们能够尽可能地可靠。不过让我们快进到我前面提到的第五级自主,也就是我们所能设想的最自主的系统。

[15:42] **SPEAKER_01:** YC's next batch is now taking applications. Got a startup in you? Apply at YCombinator.com slash apply. It's never too early and filling out the app will level up your idea.

> YC 的下一批(batch)现在开始接受申请了。你心里有一个创业想法吗?到 YCombinator.com/apply 去申请吧。永远不嫌太早,而且填写申请本身就会让你的想法更上一层楼。

[15:54] **SPEAKER_01:** Okay, back to the video.

> 好,回到视频。

[15:56] **SPEAKER_00:** My prediction is that all application software will go to zero. In other words, software will be dirt cheap. That no one will be making money on the traditional type of SaaS software. I'm not saying this will happen tomorrow or even next year. I gave up on the trying to predict timelines.

> 我的预测是,所有应用软件的价值都会归零。换句话说,软件会变得极其便宜,没有人能再靠传统那种 SaaS 软件赚钱了。我不是说这明天、甚至明年就会发生。我已经放弃去预测具体的时间线了。

[16:16] **SPEAKER_00:** I know it's going to happen on the order of years. If anyone with one prompt can generate any kind of software of any type of complexity, then the value of applications will go down to almost zero. So what does that actually look like? So today, in the startup ecosystem, in the tech ecosystem, there's all these generic SaaS, vertical SaaS software. And any of you who's running a small business or even a bigger business, you probably have bought dozens and dozens of SaaS software just to run your business.

> 我知道它会在若干年的时间尺度上发生。如果任何人只用一句提示词就能生成任何类型、任何复杂度的软件,那么应用的价值就会降到几乎为零。那这实际上会是什么样子?如今在创业生态、科技生态里,有各种通用 SaaS、垂直 SaaS 软件。你们当中任何一个在经营小生意、甚至更大生意的人,很可能仅仅为了运营业务就买了几十款 SaaS 软件。

[16:55] **SPEAKER_00:** Even today, you're able to replace large parts of those software by using something like Replit Agent or writing your own software. I think in the next few years, again, this will go from maybe 15% replaceable to 100% replaceable. So this will really fundamentally change the software market. Just to give you a story, one of our colleagues at Replit, Kelsey, she works in HR. She's never written a line of software in her life.

> 即便是今天,你也已经能用像 Replit 智能体这样的工具,或者自己写软件,来替换掉那些软件的很大一部分。我认为在接下来几年里,这个比例会从大约 15% 可替换,提升到 100% 可替换。所以这会真正从根本上改变软件市场。给你讲个故事:我们 Replit 有位同事叫 Kelsey,她在人力资源部门工作,这辈子从没写过一行代码。

[17:26] **SPEAKER_00:** And she wanted an org chart software. She had a few bespoke needs. Like she wanted to connect it to ADP, our sort of payroll software. And she had a few features that she wanted. And she went on the market, and she couldn't really find an org chart software that exactly fits her needs.

> 她想要一款组织架构图软件。她有一些定制化的需求,比如她想把它和 ADP(我们用的薪资软件)对接起来,她还想要一些别的功能。她去市场上找,却实在找不到一款完全符合她需求的组织架构图软件。

[17:47] **SPEAKER_00:** They were very expensive. They were going to cost tens of thousands of dollars a year. So she decided to make it. She took a week, less than a week, three days. And she made an org chart software that we're using today that we can go out on the market and sell it as a SaaS product for tens of thousands of dollars a year.

> 那些软件都很贵,一年要花好几万美元。于是她决定自己做一个。她花了一周,不到一周,三天时间,就做出了一款组织架构图软件,我们今天还在用它。这款软件我们完全可以拿到市场上,作为一款 SaaS 产品以每年几万美元的价格出售。

[18:05] **SPEAKER_00:** So that's like mind-blowing, right? I mean, it's HR professional can make software to run their work. That's happening today. Try to project that out a couple of years later. Like the software business fundamentally changes, gets disrupted.

> 这简直令人震撼,对吧?我是说,一个人力资源专业人士竟然能做出软件来支撑自己的工作。这就发生在今天。试着把这个趋势往后推几年:软件这个行业会发生根本性的改变,会被颠覆。

[18:21] **SPEAKER_00:** Not only software, but I think how we work, how businesses work, how corporations work, will fundamentally change. Today, we have these roles, you know, companies like to specialize. Since the industrial revolution, when factories, you know, became the main mode of creation, the sort of modern... you know, specialization in the economy kind of emerged where one person is making one part of the product. It goes on a factory sort of assembly line.

> 不只是软件,我认为我们工作的方式、企业运作的方式、公司运转的方式,都会发生根本性的改变。如今我们有各种岗位角色,公司喜欢专业化分工。自工业革命以来,当工厂成为主要的生产方式后,现代经济中的这种专业化分工就出现了——一个人只做产品的一个部分,它在工厂的流水线上流转。

[19:00] **SPEAKER_00:** And another person is responsible for testing it. Another person is responsible for assembling it. And so this specialization has been the way the economy has been trending for a long time. And it sort of makes sense, right? You want to specialize people as much as possible.

> 另一个人负责测试它,再另一个人负责组装它。所以长期以来,经济一直朝着这种专业化分工的方向发展。这在某种程度上是合理的,对吧?你希望让人们尽可能地专精化。

[19:16] **SPEAKER_00:** You want them to be as replaceable. And so this is how the modern economy is built. But once your HR professional is also a software engineer, is also potentially a marketer, is also potentially anything because they can learn anything. There are AI agents that can do anything for them. Really, you know, you go into the world where jobs will become less specialized, less siloed.

> 你希望他们尽可能可被替换。现代经济就是这样构建起来的。但一旦你的人力资源专业人士同时也是软件工程师,也可能是营销人员,也可能是任何角色——因为他们能学会任何东西,有 AI 智能体能替他们做任何事——那你就进入了一个工作变得不那么专业化、不那么各自为政的世界。

[19:43] **SPEAKER_00:** And in fact, we started... We're seeing it today and we're... At Replit, the way we're structuring our org chart and our business based on this idea, we're building... For the first time, we're building like an actual product team, product management team. And our product team is actually made of designers, engineers, and product managers, almost always in the same person.

> 事实上,我们已经开始……我们今天就看到了这一点,而且我们……在 Replit,我们正基于这个理念来构建我们的组织架构和业务。我们第一次组建了真正意义上的产品团队、产品管理团队。而我们的产品团队实际上是由设计师、工程师和产品经理组成的——而且几乎总是集于同一个人身上。

[20:06] **SPEAKER_00:** So we're trying to merge a lot of roles together and create this generalist employee. So the org chart will start to look more like a network than a hierarchy. So it'll look more like an open source project. Then it will look like a traditional company hierarchy with a marketing department, sales department. Every employee will like wake up in the morning and their mandate would not be write this marketing email or, you know, make this, optimize this button.

> 所以我们试图把很多角色融合到一起,打造这种"通才型"员工。于是组织架构会开始更像一张网络,而不是一个层级结构;它会更像一个开源项目,而不像有市场部、销售部的传统公司层级。每个员工早上醒来,他们的任务不会是"写这封营销邮件"或者"做这个、优化这个按钮"。

[20:40] **SPEAKER_00:** Their mandate would be make the business work, generate value for the business. So everyone is sort of an entrepreneur. And that would really disrupt them. Fundamentally change how companies work. It's a model that really we haven't...

> 他们的任务会是"让业务运转起来,为业务创造价值"。所以每个人在某种程度上都是创业者。这会真正颠覆它们,从根本上改变公司的运作方式。这是一种我们真的还没有……的模式。

[20:54] **SPEAKER_00:** No one has really embraced or even started to talk about. But really, you know, think it through. If everyone has access to a general purpose software engineering agent and sort of agent for every possible role, obviously domain expertise is still important, but it's not as important as it used to be. It's exponentially less important. And this also affects how people build businesses.

> 还没有人真正拥抱、甚至开始讨论这种模式。但你真的仔细想一想:如果每个人都能用上一个通用的软件工程智能体,以及几乎每一种可能角色的智能体,那么显然领域专长仍然重要,但它已不像从前那么重要了,它的重要性呈指数级下降。而这也会影响人们创业建业的方式。

[21:19] **SPEAKER_00:** It affects the... The opportunities that are available for us in the future. One really interesting book that I read, this book is was written in the 80s, which is insane given how good the predictions were. So I'm just going to read this. Ideas will become wealth.

> 它影响着……我们未来可获得的机会。我读过一本非常有意思的书,这本书写于八十年代,考虑到它的预测有多准,这简直令人难以置信。我就直接念一段:"思想将成为财富。"

[21:39] **SPEAKER_00:** Merits, wherever it arises, will be rewarded as never before. And in environments where the greatest source of wealth will be the ideas you have in your head rather than the physical capital alone, rather than the physical capital alone, anyone who thinks clearly will potentially be rich. The information age will be the age of upward mobility. The brightest, most successful and ambitious of these will emerge as truly sovereign individuals. Now, some of this is a bit dated, the information age, perhaps we call the intelligence age today.

> "才能,无论出现在何处,都将得到前所未有的回报。在一个最大的财富来源是你脑中的想法、而非仅仅是有形资本的环境里——而非仅仅是有形资本——任何能清晰思考的人都有可能致富。信息时代将是向上流动的时代。其中最聪明、最成功、最有抱负的人,将崛起成为真正的'主权个体'。"当然,这里有些说法有点过时了,"信息时代"如今我们或许该称之为"智能时代"。

[22:09] **SPEAKER_00:** But this book predicted things like crypto, remote work, all sorts of things like that. And this idea of like a sovereign individual, someone so empowered by technology, so empowered by these agents that is able to create enormous amount of wealth individually, is going to be the norm. Think about someone like Satoshi. Satoshi created, a single person created a trillion dollars worth of value. I don't know what the market cap exactly, perhaps it's more than trillion dollars of Bitcoin.

> 但这本书预言了诸如加密货币、远程办公等等各种事情。而这种"主权个体"的理念——一个被技术、被这些智能体赋能到如此程度,以至于能凭一己之力创造巨额财富的人——将会成为常态。想想中本聪这样的人。中本聪一个人就创造了价值上万亿美元的东西。我不知道确切的市值是多少,也许比特币的市值已经超过一万亿美元了。

[22:49] **SPEAKER_00:** But like, that's a single person, they wrote the paper, they wrote the software, they put it out there, and it became a big thing. Obviously, there's a lot of people, it's a big market right now, but it was created by a single person, and we don't know who they are. And I think that's going to be a common occurrence in the future. The really great thing about it is really, the access to opportunity will be universal. The idea of merit being rewarded, wherever it arises, doesn't matter if you're in Silicon Valley or anywhere else in the world.

> 但你看,那就是一个人:他写了论文,写了软件,把它发布出去,然后它就成了一件大事。当然,现在有很多人参与,它已经是个巨大的市场,但它最初是由一个人创造的,而我们还不知道那个人是谁。我认为这在未来会成为常见的事。它真正了不起的地方在于,获得机会的途径将是普世的。才能会得到回报,无论它出现在何处——不管你是在硅谷,还是在世界上任何其他地方。

[23:20] **SPEAKER_00:** If you can think clearly, and you can use some of this technology, if you think clearly and generate good ideas, go into Replit, put in those ideas, make the first version of software, today, you can start to become more like a sovereign individual. Again, the way collaboration work will be seamless. You know, everyone's talking about the, you know, $1 billion single person company, but I think that really kind of misses the point a little bit. What's really interesting about it is that you'll be able to assemble, groups of people really quickly. You'll also be able to assemble groups of agents really quickly.

> 如果你能清晰地思考,又能使用其中一些技术,如果你思路清晰、能产生好点子,那就进入 Replit,把这些点子放进去,做出软件的第一个版本——今天,你就可以开始变得更像一个主权个体了。同样地,协作的方式将变得无缝。大家都在谈论那种"十亿美元的单人公司",但我觉得那其实有点没抓住重点。它真正有意思的地方在于,你将能够非常快地组建起一群人,你也将能够非常快地组建起一群智能体。

[23:56] **SPEAKER_00:** You'll be able to assemble these companies and also unwind them. You can create mission purpose, you know, companies or like projects and unwind them really quickly. And in some cases it could happen in a day or two. And sometimes you might be, you might think you're working with another human on the internet, but they're actually an agent built by someone else who's out there doing work for them. So the way we work, and the way people build startups will fundamentally change.

> 你将能够组建这些公司,也能够解散它们。你可以创建为某个使命目的而生的公司或项目,然后很快地把它们解散,在某些情况下这可能一两天内就完成。而且有时候,你可能会以为自己是在网上和另一个人合作,但对方其实是别人做出来、替他在外面干活的智能体。所以我们工作的方式、人们创业的方式,都会发生根本性的改变。

[24:24] **SPEAKER_00:** As the cost of transaction goes down, goes down to zero, then the reason to hire an employee full time, you'll have less of a reason to hire full time employees. So think about like getting an Uber today. The transaction costs, the kind of effort of getting an Uber is just one button on your phone. I think the same thing will be in the future, to get a developer, whether it's a software agent or another human being. It'll be just like one button.

> 随着交易成本下降、降到零,那么全职雇用一名员工的理由,你雇用全职员工的理由就会变少。想想今天叫一辆 Uber:交易成本、叫车所花的那点力气,不过就是手机上按一个按钮。我认为未来找一个开发者也会是一样——不管是一个软件智能体,还是另一个人,都会像按一个按钮那么简单。

[24:57] **SPEAKER_00:** I want this problem solved. You'll be able to, maybe your agent will be able to go find and interview a lot of different people or agents on the internet and be able to find the best thing to solve that problem. And so you'll be able to like build businesses really at the speed of light. Now, you know, I talked about how kind of application software, software goes to zero. That doesn't mean that all software goes to zero.

> "我想解决这个问题。"你将能够——也许你的智能体将能够——到互联网上去寻找并面试许许多多不同的人或智能体,从中找到解决那个问题的最佳选项。于是你将能够以近乎光速的速度去创建业务。我前面讲到应用软件、软件的价值归零,但这并不意味着所有软件都归零。

[25:22] **SPEAKER_00:** Today, you know, Replit agents or others, the way it works is the agent makes a piece of software. The user uses the software to solve problems. You can think of those things as intermediate steps. Instead, agents can just solve problems. And for Replit, and I'm sure a lot of other businesses to survive, at some point Replit needs to stop being focused on making applications, and start being focused on solving problems with software.

> 如今,Replit 智能体或其他工具的运作方式是:智能体做出一款软件,用户用这款软件去解决问题。你可以把这些都看作中间步骤。而其实,智能体可以直接去解决问题。对 Replit 而言——我相信对很多其他企业要想活下去也是如此——在某个时刻,Replit 需要不再把焦点放在"做应用"上,而开始把焦点放在"用软件解决问题"上。

[25:54] **SPEAKER_00:** So I want to leave ample time for questions. So I'll end here and open it up.

> 我想给提问留出充足的时间。所以我就讲到这里,把时间交给大家提问。

[26:00] **SPEAKER_09:** My name is Chinat from Stanford. Nice to meet you. My first question is in this future, do you see there potentially humans engaging with multiple agents or will there be a unilateral agent? And if it's in the case of like multiple agents, how would we deal with the fragmentation of like data, memory and context? Across all these different agents?

> 我叫 Chinat,来自斯坦福,很高兴见到你。我的第一个问题是:在这样的未来里,你觉得人类可能是和多个智能体打交道,还是会有一个单一的智能体?如果是多个智能体的情形,我们该如何处理数据、记忆和上下文在所有这些不同智能体之间被割裂、碎片化的问题?

[26:21] **SPEAKER_00:** I think multiple agents. And the reason I think that's true is because let's say I'm someone with true unique domain expertise. Let's say I'm a lawyer who is top in the world at solving certain cases that are very rare. And so I have this domain expertise that I'm not going to share in the future. I'm not going to be open source.

> 我认为是多个智能体。我之所以这么认为,是因为——假设我是一个拥有真正独特领域专长的人。比如我是一名律师,在处理某些非常罕见的案件方面是世界顶尖的。那么我拥有这种领域专长,在未来我是不会把它分享出去的,我不会把它开源。

[26:51] **SPEAKER_00:** I'm not going to sell to scale AI so that they can sell to open AI or Google, all of those. I'm just going to keep this resource to myself. But the way I would monetize it, instead of myself going and selling my services directly, I would like imbue this knowledge into an agent that becomes this very specialized agent in this very specialized domain. And then I can scale myself. And so I think people will be building these agents on their behalf.

> 我不会把它卖给 Scale AI,让他们再卖给 OpenAI 或谷歌之类的公司。我只会把这份资源留给自己。但我将它变现的方式,不是我自己去直接出售我的服务,而是把这份知识注入到一个智能体里,让它成为这个非常专门领域中的一个高度专业化的智能体。这样我就能把自己"规模化"了。所以我认为人们会去打造这些代表他们自己的智能体。

[27:20] **SPEAKER_00:** And then there's going to be agents that go out there and assembles these teams of agents. And then there's going to be obviously software development agents. And maybe you're running all this through ChatGPT or whatever main interface you have. But I think it's going to be a multi-agent world with different contacts, similar to what we have in the world today. When I go to a lawyer, I need to give them my contacts.

> 然后会有一些智能体,它们到外面去把这些智能体组建成团队。当然还会有软件开发智能体。也许你是通过 ChatGPT 或者你所拥有的某个主界面来运行这一切。但我认为这将是一个多智能体的世界,各自拥有不同的上下文,和我们今天现实世界的情形类似。当我去找一位律师时,我需要把我的相关背景信息告诉他。

[27:48] **SPEAKER_00:** And maybe there are protocols. And this is why I talked about how MCP really doesn't solve the agent-to-agent problem. I think there needs to be more interesting protocols in this space. And maybe this is a startup someone builds.

> 也许会有一些协议。这正是我为什么说 MCP 其实并没有解决智能体对智能体的问题。我认为这个领域需要更有意思的协议。也许这就是某个人可以去做的一家创业公司。

[28:02] **SPEAKER_04:** Hi, thank you for the insightful talk. My question is as follows. In the not-so-viral future, where we are going to have AI systems that can automate most, if not all, of meaningful physical and cognitive tasks, and there's increasing delegation, to agents that work on your behalf and talk to other agents that are working on other people's behalf, then what is left for humans to do? What will our human condition look like? Because our physical and cognitive aspects can all be done by intelligences.

> 你好,感谢你这场很有启发的演讲。我的问题是这样的:在不太遥远的未来,我们将拥有能够自动化大部分——如果不是全部——有意义的体力和认知任务的 AI 系统,而且越来越多地把事情委托给替你做事的智能体,而这些智能体又和替别人做事的其他智能体交流。那么,还剩下什么留给人类去做呢?我们人类的处境会变成什么样?因为我们的体力和认知层面都能被智能体完成。

[28:33] **SPEAKER_00:** I think it fundamentally depends on your worldview and belief of the limits of AI versus the uniqueness and primacy of what humans can do. So it becomes a bit of a religious discussion. But my view is there's something special about humans. And my view is that there's a fundamental limitation with how we do AI today. And maybe this gets solved.

> 我认为这从根本上取决于你的世界观,取决于你对"AI 的极限"与"人类所能做之事的独特性和首要性"这二者的信念。所以这多少变成了一场近乎宗教的讨论。但我的看法是,人类身上有某种特别之处。我的看法是,我们今天做 AI 的方式存在一个根本性的局限。也许这个局限会被解决。

[29:03] **SPEAKER_00:** But AI today can't truly generalize out of distribution. Everything AI can do needs to be represented in the data. So I go back to this example of this lawyer that is expert in the world at very rare cases. Again, this is something that no one else knows how to do or can do. Or whenever there's like a truly novel problem, truly novel case, you still need human ingenuity to solve that problem.

> 但今天的 AI 无法真正做到"分布外泛化"。AI 所能做的一切,都必须在数据中有所体现。所以我再回到那位律师的例子——他在处理极为罕见的案件方面是世界级的专家。再说一次,这是别人不知道怎么做、也做不到的事。或者说,每当出现一个真正全新的问题、真正全新的案件时,你仍然需要人类的独创性去解决那个问题。

[29:34] **SPEAKER_00:** And so I think humans will be more in the creative seat. And I think agents can be creative as well, but their type of creativity are not net new knowledge. It's more like about, which is a lot of what creativity is, bringing a lot of different things together. But this idea of ideas become wealth is what gets really exciting about it. People can generate novel ideas and test them out really quickly, which I don't think we're going to get to a point where you can go tell an agent, hey, go find me a business idea and go test all of them.

> 所以我认为人类将更多地坐在"创造者"的位置上。我也认为智能体可以有创造力,但它们那种创造力并不是净新增的知识,而更像是——这也确实是创造力的一大部分——把许多不同的东西组合到一起。但"思想成为财富"这个理念才是真正令人兴奋的地方。人们能够产生新颖的想法,并且非常快地把它们检验一遍。而我并不认为我们会走到那样一步:你可以对一个智能体说"嘿,去帮我找一个商业点子,然后把它们全都测试一遍"。

[30:12] **SPEAKER_00:** I don't think we'll get there anytime soon.

> 我不认为我们短期内会走到那一步。

[30:14] **SPEAKER_08:** Thanks for your talk. I've been following Repl.it for many years, and that's actually where I learned how to code as well was on Repl.it. So you mentioned the value of clear thinking and ideas being the future.

> 谢谢你的演讲。我关注 Replit 很多年了,其实我当初就是在 Replit 上学会写代码的。你提到了清晰思考的价值,以及"想法就是未来"。

[30:24] **SPEAKER_08:** Do you see this as an argument more towards the favor of a liberal arts critical thinking model of education instead of a more STEM skills-based focus?

> 你是否认为这更像是在支持一种以博雅教育、批判性思维为核心的教育模式,而不是更侧重 STEM 技能的教育模式?

[30:33] **SPEAKER_00:** I don't think they're mutually exclusive, but I do think that the liberal arts will become more valuable. I think today engineers tend to be a little more parochial than they can afford to be in the future, because what I showed with the model for what the future company could look like, everyone becoming more of a generalist, I think today engineers can afford to not understand even the business they're in. A lot of engineers are just focused on very narrow domains. So I think people need to have a more broadened worldview and set of skills. But I don't think they're mutually exclusive.

> 我不认为二者是互斥的,但我确实认为博雅教育会变得更有价值。我觉得今天的工程师往往比他们在未来所能承受的更狭隘一些,因为正如我用未来公司可能的样子那个模型所展示的——每个人都变得更像通才——我觉得今天的工程师甚至可以不了解他们所在的业务而照样过得去。很多工程师只专注于非常狭窄的领域。所以我认为人们需要拥有更开阔的世界观和更广的技能组合。但我不认为它们是互斥的。

[31:18] **SPEAKER_00:** You know, being scientifically minded, I think is going to be important.

> 你知道,具备科学的思维方式,我认为将会很重要。

[31:23] **SPEAKER_02:** Hi. So I was more curious as to where in the tech stack is Repl.it making a lot of progress? Because as you said, Repl.it can do tasks for one hour.

> 你好。我比较好奇的是,Replit 在技术栈的哪个层面取得了大量进展?因为正如你所说,Replit 能够连续工作一小时来完成任务。

[31:38] **SPEAKER_02:** So given that Repl.it uses probably closed source models which have no access to pre-training and post-training, where in the tech stack are you making that amazing kind of innovation that gets your models to work autonomously for like an hour?

> 那么,既然 Replit 用的很可能是闭源模型、你们无法接触到预训练和后训练环节,那你们究竟是在技术栈的哪个层面做出了那种了不起的创新,让你们的模型能够自主工作长达一小时?

[31:58] **SPEAKER_00:** It's what I was calling the habitat of the model. So, you know, the commercial models can train really great models. They can train them to be as autonomous as possible, to be coherent over a long period of time. But us, or really any agent company, needs to be able to provide the infrastructure for that agent to exist in. And so all these components that I talked about, so one really crucial thing about Repl.it

> 就是我一直说的那个"模型的栖息地"。你知道,那些商业模型公司能训练出非常出色的模型,他们能把模型训练得尽可能自主、能在很长一段时间里保持连贯。但我们——或者说其实任何一家做智能体的公司——都需要能提供那个智能体赖以存在的基础设施。所以我前面讲到的所有这些组件……关于 Replit,有一件非常关键的事……

[32:30] **SPEAKER_00:** is this idea of, you could call it being transactional or atomic. Every mutation to the Repl.it computer environment happen in sync with every other component of the system. So right now in Repl.it, if you go to your history, you can see previous checkpoints and you can actually go to any one of them and reboot the application in that state.

> ……就是这个理念,你可以称之为"事务化"或"原子化"。对 Replit 计算环境的每一次改动,都与系统的其他每一个组件保持同步。所以现在在 Replit 里,如果你打开你的历史记录,你能看到之前的各个检查点(checkpoint),而且你其实可以回到其中任意一个,让应用在那个状态下重新启动。

[32:59] **SPEAKER_00:** And so we think that infrastructure is going to be really crucial for how to make the models more and more reliable. I think there's a limit on how much the training can increase reliability. But I think the environment feedback and the ability to try things really fast is the way to get to the upper echelon of reliability. So that's what we're focused on.

> 所以我们认为,这套基础设施对于如何让模型变得越来越可靠将至关重要。我认为训练本身能提升的可靠性是有上限的。但我认为,来自环境的反馈,以及能够非常快速地尝试各种方案的能力,才是达到可靠性最高层级的途径。所以这就是我们所专注的方向。

[33:22] **SPEAKER_03:** Hi. So you talk about the generalist employee and how that's the sort of future of companies. I totally agree with this vision, but where I find myself stuck is finding roles today that set me up for that kind of future. What kind of opportunities should we look out for? What kind of positions should we look out for in startups and companies that would prepare us with the skills that are necessary in order to be a generalist, good employee, five years down the line, when that finally becomes a thing?

> 你好。你谈到了"通才型员工",以及这是公司的某种未来。我完全认同这个愿景,但让我感到困惑的是,如何在今天找到能为那种未来做好铺垫的岗位。我们应该留意哪些机会?我们应该在创业公司和企业里留意哪些职位,才能让我们具备必要的技能,以便在五年后——当那一天终于到来时——成为一名优秀的通才型员工?

[33:48] **SPEAKER_03:** I know being a founder is one option, but not all of us want to take that career plunge immediately. Some of us want to work with other people, build teamwork skills, and learn all of those other things as well. How do we go about that?

> 我知道当创始人是一个选择,但并不是我们所有人都想立刻纵身跃入那种职业冒险。我们当中有些人想和别人一起工作、培养团队协作的能力,并且学习所有那些其他的东西。我们该怎么做才好?

[34:01] **SPEAKER_00:** Join startups as early as possible. Like, obviously, you can think of it as a sort of exponentially decaying curve where like being the first, being the founder, you get the most generalist experience, being the, you know, first employee, and then by the time you get to the 100th, I don't know, like to the maybe 100th employee, you're sort of like, you're not getting as much of that generalist experience. But like, just join as early as you can, depending on your risk profile and all of that. But even like number 20 at like a Series B company, I think you will get a lot more experience than at a Fang or something like that. Even if you join that startup, you need to be seeking those generalist opportunities.

> 尽可能早地加入创业公司。显然,你可以把它想成一条指数衰减的曲线:作为第一个人、作为创始人,你获得的通才经验最多;作为第一号员工次之;而当你成为第 100 号——我不知道,大概第 100 号员工时,你能获得的那种通才经验就没那么多了。但总之,根据你自己的风险偏好等等,尽你所能早地加入。不过,即便是在一家 B 轮公司里当第 20 号员工,我认为你也会比在一家 FAANG 大厂之类的地方获得多得多的经验。而且即便你加入了那家创业公司,你也需要主动去寻找那些能锻炼通才能力的机会。

[34:48] **SPEAKER_00:** So don't sit there waiting for people to give you tasks. You have that mindset of I'm waking up in the morning. I'm not looking at a to-do list. I'm looking at a mission. And my mission is to make this company succeed or be more valuable.

> 所以别坐在那儿等着别人给你派任务。你要有这样一种心态:我早上醒来,我看的不是一张待办清单,我看的是一项使命,而我的使命就是让这家公司成功、让它更有价值。

[35:02] **SPEAKER_05:** Hi, my name is Shivam. I also wanted to ask about the one hour of autonomous like agent development. Specifically, like, could you like elaborate a little more on how like you and your team approach how long of a time horizon is worth pursuing as opposed to improving reasoning for shorter time horizons?

> 你好,我叫 Shivam。我也想问问那个"一小时自主智能体开发"的事。具体来说,你能不能再详细讲讲,你和你的团队是如何权衡的:多长的时间跨度才值得去追求,而不是转而去改进在较短时间跨度上的推理能力?

[35:22] **SPEAKER_00:** So I think what you're talking about with shorter time horizons is more like, let's work on reliability. And then longer time horizons, like let's work on autonomy, removing the human in the loop and the burden of the human to continue to test and get feedback. So we're doing both. When I'm talking about reliability, this is more investing in reasoning and more investing in this parallel agent trial and error that I was talking about, what we're calling sampling and simulations. And then for long horizon, it's more about testing, making sure that, because as you go longer, there's like a gold drift.

> 我想你说的较短时间跨度,更像是"我们来提升可靠性";而较长的时间跨度,则更像是"我们来提升自主性"——去掉回路中的人,减轻人不断去测试、给反馈的负担。所以这两件事我们都在做。我说可靠性时,更多是指投入到推理上,以及投入到我前面讲的那种并行智能体试错上,也就是我们所称的"采样与模拟"。而对于长时间跨度,则更多是关于测试,确保……因为随着时间越拉越长,会出现一种"目标漂移"(goal drift)。

[36:08] **SPEAKER_00:** The agent might start doing things that you don't like, but having those guardrails of testing along the way will make it so that it stays more coherent over time. And then as we collect more data about what fails and what doesn't work, you can either like go and fine tune that or you can just like continue to improve the prompts and add more guardrails to make it better. So I think both are important.

> 智能体可能会开始做一些你不喜欢的事,但一路上有那些测试构成的护栏,就能让它随着时间推移保持更连贯。然后,随着我们收集到更多关于什么会失败、什么行不通的数据,你既可以去做微调,也可以持续改进提示词、增加更多护栏来把它做得更好。所以我认为这两方面都很重要。

[36:36] **SPEAKER_10:** Hi, I'm Sophia. I've been thankful for your talk and I've been following you. I met at AI for Developers when you were talking about Ghostwriter and the work behind it. But I'm curious to hear more about how agents are kind of over-saturating certain sectors and whether or not that should kind of, you should consider that when you're working on them or joining a startup that's working on something.

> 你好,我是 Sophia。我很感谢你的演讲,我一直在关注你。我在"AI for Developers"活动上见过你,当时你在讲 Ghostwriter 以及它背后的工作。不过我很想多听你讲讲,智能体是如何在某些领域出现过度饱和的,以及在你着手开发它们、或加入一家做某个方向的创业公司时,是否应该把这一点考虑进去。

[37:04] **SPEAKER_00:** I think certainly software is like really tricky, software engineering agents. There's like, there's a lot of people that want to do that. And if you're coming in late, you want to have a truly novel idea to be able to like compete there. But you know, there's a lot of things like who's building the agent for HR or finance? I know one company is doing accounting.

> 我觉得软件——软件工程智能体——确实很棘手。有很多人都想做这个。如果你入场晚了,你就得有一个真正新颖的想法,才能在那里竞争。但你知道,还有很多别的方向,比如谁来做人力资源或财务的智能体?我知道有一家公司在做会计。

[37:27] **SPEAKER_00:** There's a lot of companies doing SDR for whatever reason that's very crowded. What I would start with is what are you interested in and where do you have domain knowledge? So the best way to start an agent company, is that if you yourself, you yourself, you're like a compliance officer, you start a compliance officer or you're passionate about compliance. I don't know who's passionate about compliance. But if you're passionate about compliance, go start an agent company because you're going to learn the most about it and you're going to have the most domain knowledge.

> 有很多公司在做 SDR(销售开发代表),不知为何那个赛道非常拥挤。我会从这里入手:你对什么感兴趣?你在哪个领域拥有专业知识?所以创办一家智能体公司最好的方式是——如果你本人,你本人就是一名合规官,那你就做合规官方向;或者你对合规充满热情。我不知道谁会对合规充满热情。但如果你真对合规充满热情,那就去创办一家智能体公司,因为你会在这方面学到最多,也会拥有最多的领域知识。

[38:01] **SPEAKER_00:** And domain knowledge is the most important thing to build an agent company.

> 而领域知识,是创办一家智能体公司最重要的东西。

[38:04] **SPEAKER_06:** Hey, so if the cost of software and building software is going to zero, then by extension, the platforms which build software, like Replit, like the value capture will be going down to zero. So how are you planning to make money long term and how are you going to compete with like the other competitors like Bolt and Lovable?

> 嘿,那么如果软件以及构建软件的成本正在归零,那么由此推论,像 Replit 这样构建软件的平台,其能捕获的价值也会趋于零。所以你打算长期怎么赚钱?你又打算如何与 Bolt、Lovable 这样的其他竞争对手竞争?

[38:22] **SPEAKER_00:** Yeah, so notice that I said not old software, I said like application software specifically. So I think software will continue to run our lives, but a lot of it will be autonomous. So for example, I build a lot of personal software using Replit. And a lot of it is around managing my life. And my family and like, you know, doing a lot of quantified self stuff, a lot of like, you know, data about my sleep and all of that stuff.

> 是的,请注意我说的不是所有软件,我特指的是应用软件。所以我认为软件会继续主宰我们的生活,但其中很大一部分将是自主运行的。举个例子,我用 Replit 做了很多个人软件,其中很多是围绕管理我的生活、我的家庭,还有做很多"量化自我"的事情,比如关于我睡眠的各种数据等等。

[38:52] **SPEAKER_00:** And then I spend a lot of time like plotting that data and doing all of that stuff. Like instead, I should be able to tell Replit agent, here are my goals. You figure out what kind of software that needs to be built and you figure out how to operate it. And you tell me what wearables I need to buy and what, and what do I need to log in the morning? What do I need to do?

> 然后我花了大量时间去把这些数据画成图表、做所有这些事。而其实,我应该能够直接告诉 Replit 智能体:这些是我的目标,你来搞清楚需要构建什么样的软件,你来搞清楚怎么运行它。然后你告诉我需要买哪些可穿戴设备,以及早上我需要记录什么、我需要做什么。

[39:14] **SPEAKER_00:** And should be able to go make the software, acquire the things that I need in my home, what kind of sensors, and then solve the problem for me. I think Replit needs to become a universal problem solver for our company to survive. And I think for a lot of the others, you know, I think it's already, especially the companies that you talk about in the prototyping space, it's already getting really crowded there. I think what Replit, where really Replit excels today is the fact that it's full stack. It can go from idea to a deployed and scaled software.

> 它应该能够去做出软件、采购我家里需要的东西、需要什么样的传感器,然后替我把问题解决掉。我认为为了我们公司能活下去,Replit 需要成为一个通用的问题解决者。至于其他很多家公司,我觉得已经——尤其是你提到的那些做原型设计的公司——那个领域已经变得非常拥挤了。我认为 Replit 如今真正出色的地方在于它是全栈的:它能从一个想法一路走到一个已部署、可扩展的软件。

[39:46] **SPEAKER_11:** Hi, my name is Emma and I'm really intrigued by your vision of this future where all code is written by agents. But I'm also kind of concerned because there is this kind of known problem where if you train a generative model on data that is generated by another model, you get an issue of like accumulating error, accumulating noise. So my question is, in this future where code is written by agents, is tested by agents, is approved by agents, how do we kind of prevent this exploding error problem while still allowing these models to grow and evolve?

> 你好,我叫 Emma,我对你描绘的这个"所有代码都由智能体编写"的未来愿景非常着迷。但我也有点担心,因为有一个已知的问题:如果你用另一个模型生成的数据去训练一个生成式模型,就会出现误差不断累积、噪声不断累积的问题。所以我的问题是:在这个代码由智能体编写、由智能体测试、由智能体审批的未来里,我们该如何防止这种误差爆炸的问题,同时又仍然让这些模型能够成长和演进?

[40:13] **SPEAKER_00:** My bet is that pretty soon we're going to move into more of the alpha zero style of training where you have a more traditional LLM that's trained on all of the internet. But then the way to train the next generation of it would be to give it a reinforcement learning environment where it's generating a lot of problems and doing like self play where solving these problems, getting feedback on them, and doing it in this like massively parallel way. I think this is how we're going to get the next generation of software agents. It's not going to be trained on human code because like you said, there's not going to be human code. And so we have to solve this.

> 我押注的是,很快我们就会转向更接近 AlphaZero 那种风格的训练方式:你有一个比较传统的大语言模型,它是在整个互联网上训练出来的;但训练它下一代的方式,则是给它一个强化学习环境,让它生成大量问题、进行类似"自我博弈"(self-play)的过程——去解决这些问题、从中获得反馈,并以这种大规模并行的方式来进行。我认为这就是我们获得下一代软件智能体的方式。它不会是用人类代码训练出来的,因为正如你所说,那时将不再有人类代码。所以我们必须解决这个问题。

[40:55] **SPEAKER_00:** Otherwise, we'll plateau very hard.

> 否则,我们会非常严重地陷入停滞、遇到瓶颈。

[40:58] **SPEAKER_07:** Hi. I'm quite interested in some of the systems report support required for these agents. And I find the universal framework and the universal package manager that you've released and your use of Nix quite interesting. And you mentioned this copy on write snapshotting and forking and merging. And I'm working on a similar thing.

> 你好。我对这些智能体所需的一些系统层面的支持很感兴趣。我觉得你们发布的那个通用框架、通用包管理器,以及你们对 Nix 的使用,都相当有意思。你还提到了写时复制的快照、以及分叉和合并。我自己也在做类似的东西。

[41:23] **SPEAKER_00:** Well, you should come work on our upload.

> 那,你应该来我们这儿一起做。

[41:25] **SPEAKER_07:** I was wondering if any of this is publicly available or something you might be thinking about open sourcing.

> 我想问的是,这些东西有没有哪些是公开可获取的,或者是你们可能会考虑开源的?

[41:30] **SPEAKER_00:** Yeah, I mean, we open sourced some of our package manager work. We're big contributors to NixOS. So we use NixOS, which is a transactional operating system and some of the drives that we use. And we build it all ourselves. You should come over, I think, three or four times and we'll certainly talk about this.

> 是的,我们开源了一部分包管理器方面的工作。我们是 NixOS 的重要贡献者。我们使用 NixOS,它是一个事务化的操作系统,还有我们用的一些存储驱动。这些我们都是自己构建的。我觉得你应该过来找我们聊三四次,我们肯定会谈到这个。

[41:50] **SPEAKER_00:** It's the best way I can describe it. And possibly the filesystem stuff

> 这是我能给出的最好的描述方式了。至于文件系统那部分,可能……

[41:55] **SPEAKER_07:** we'll at minimum talk about it.

> 我们至少会聊一聊它。

[41:57] **SPEAKER_00:** But this is active work right now.

> 但这是我们目前正在进行中的工作。

[42:01] **SPEAKER_?:** But, yeah, come intern at Repl.it and learn all this stuff and then go build it yourself. Thank you. All right. Thank you, everyone.

> 不过,是的,来 Replit 实习吧,把这些东西都学会,然后自己去把它做出来。谢谢。好的,谢谢大家。
