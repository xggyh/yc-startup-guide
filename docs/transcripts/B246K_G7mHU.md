# 全文转录 · YC 内部 AI 手册:把公司变成"超级智能组织"

> ▶ [YouTube](https://www.youtube.com/watch?v=B246K_G7mHU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/B246K_G7mHU.md) &nbsp;·&nbsp; Inside YC's AI Playbook

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_00:** How do you build super intelligence inside a company?

> 你要如何在一家公司内部构建超级智能?

[00:02] **SPEAKER_01:** Part of the key thing is not to just use AI as a co-pilot. This is the thing where you use it as the building layer for everything and you need to start recording all the artifacts.

> 关键的一点是不要只把 AI 当作副驾驶来用。真正的做法是把它作为一切事物的构建层,而且你需要开始记录下所有的产物。

[00:14] **SPEAKER_03:** It's like a shared organizational brain. It's like the closest thing to us being able to like connect our brains.

> 它就像是一个共享的组织大脑。它几乎是我们能够把彼此的大脑连接起来的最接近的形态。

[00:19] **SPEAKER_02:** If you frame this as a way for everyone in an organization to get better at what they do using the like collective skill and instinct of the people they work with, it's incredibly powerful.

> 如果你把它理解为一种方式,让组织里的每个人都能借助身边同事的集体技能和直觉,把自己的工作做得更好,那它的威力是极其惊人的。

[00:39] **SPEAKER_00:** Today we have a real treat. We have a special guest, general partner at YC, our partner, Pete Kuhman. He created Optimizely, which was one of the first and one of the best ways to do A-B testing for apps and websites. And since then, he has gone on to create all of our agent infrastructure at YC. So literally, all of our agent infrastructure at YC.

> 今天我们有一份大礼。我们请来了一位特别嘉宾,YC 的普通合伙人、我们的搭档 Pete Kuhman。他创立了 Optimizely,那是最早、也是最好的针对应用和网站做 A/B 测试的工具之一。从那以后,他又打造了我们 YC 内部所有的 agent 基础设施。真的是字面意义上 YC 全部的 agent 基础设施。

[01:01] **SPEAKER_00:** So literally, all of our agent infrastructure at YC. All of our harnesses and how we use AI internal to YC. Pete, welcome to The Light Code.

> 真的是我们 YC 全部的 agent 基础设施。我们所有的 harness(运行框架),以及 YC 内部使用 AI 的方式。Pete,欢迎来到 The Light Code。

[01:07] **SPEAKER_03:** Thanks, Gary. For the last few years since ChatGPT, YC has been funding mainly AI companies. And we've been, we've gone through like many different like versions of advice for them about how to build AI native companies that build like mainly AI products. And we've gone on a crazy journey with them learning all of this. I think a lot of people don't realize that internally YC is actually building and using a lot of the same stuff that we're helping our startups build and use themselves.

> 谢谢,Gary。自从 ChatGPT 出现以来的这几年,YC 主要在投资 AI 公司。我们不断给他们提供各种版本的建议,教他们如何打造以 AI 为核心、主要做 AI 产品的公司。我们和他们一起经历了一段疯狂的旅程,把这些东西都学了一遍。我觉得很多人没有意识到,YC 内部其实也在构建和使用许多和我们帮助创业公司构建、使用的一模一样的东西。

[01:37] **SPEAKER_03:** And it's been, I think, a very powerful symbiotic relationship for us to actually be adopting these tools and like transforming our own organization, which was started way, way pre-AI into a super AI native organization ourselves. And Pete has really been leading the charge for that. And so I'm really excited about this episode because I've actually been wanting to talk publicly about all the stuff that we've built internally. And this is the first time I've done this. This is the first time that we're doing it.

> 我认为这形成了一种非常强大的共生关系:我们自己也在采用这些工具,把我们这家远在 AI 时代之前就创立的组织,转型成一个高度 AI 原生的组织。而 Pete 一直在带头推动这件事。所以我对这一期节目特别兴奋,因为我一直想公开聊聊我们内部构建的所有东西。这是我第一次这么做,也是我们第一次这么做。

[02:02] **SPEAKER_03:** So Pete, perhaps to start off, you sort of go back to the beginning and like talk about like there was a particular like moment when we really started adopting these AI tools internally. It was really you who got us started down that path. Sure.

> 那么 Pete,也许我们可以从头讲起,回到最开始,聊聊那个我们真正开始在内部采用这些 AI 工具的特定时刻。其实正是你带着我们走上了这条路。好的。

[02:17] **SPEAKER_02:** Happy to tell the story here. And it's, I like framing it that way because it was a project that I and a few engineers got started about a year ago, maybe a little more, but that has since snowballed into just a whole infrastructure layer that's made it possible for. Yeah. Us to use AI internally at YC in lots of different ways. And that's actually been one of the neatest parts about this is watching the whole engineering team and many partners also just dive in and contribute to this, this infrastructure layer.

> 我很乐意在这里讲讲这个故事。我喜欢这样来描述它,因为这最初只是我和几位工程师大约一年前、也许再早一点启动的一个项目,但后来它像滚雪球一样发展成了一整套基础设施层,让我们能够在 YC 内部以许多不同的方式使用 AI。而这件事最棒的一点,就是看着整个工程团队以及许多合伙人也纷纷投入进来,为这套基础设施层做出贡献。

[02:46] **SPEAKER_02:** We started building our own harness inside of YC or kind of YC specific agents about a year ago. And the original impetus for the project was some of the work that I and a few of the software engineers at YC were doing with our finance team just for a bit, a bit of backstory. So YC has for as long as it's existed, as far as I'm aware, run mostly on our own software in this era, just given us a huge advantage, right? And so with that context, back to this, this moment, maybe a year ago, we were sitting down with the finance team talking through a set of tools that we were going to build for them, uh, just to help them run through some of their finance workflows, booking journal, and, and I'll say this all the time. interviews, uh, entries, uh, logging, priced rounds, like all the sorts of things that, that make YC run.

> 大约一年前,我们开始在 YC 内部构建我们自己的 harness,或者说 YC 专属的 agents。这个项目最初的动因,是我和 YC 的几位软件工程师当时正在和财务团队一起做的一些工作——先交代一点背景。据我所知,YC 自成立以来,在这个时代基本上都是靠我们自己的软件在运转,这给了我们巨大的优势,对吧?带着这样的背景,回到大约一年前那个时刻,我们和财务团队坐在一起,讨论我们准备为他们构建的一套工具,帮助他们跑通一些财务工作流程——记账、录入分录、记录、按估值定价的融资轮次,诸如此类让 YC 得以运转的各种事务。

[03:40] **SPEAKER_02:** Really I was seeing kind of two things at once, like on one hand, uh, we, you know, we had this sort of loop going internally right? Where we'd sit down with the finance team, the finance team would describe to. Our software engineers, how, you know, this complicated financial workflow worked and then software engineers would go and build some purpose built software where there was a deterministic workflow, encapsulating everything that they had been talked about. hold, and then hand it back to the finance team, and so on. And it felt really inefficient.

> 其实我当时同时看到了两件事。一方面,我们内部有这样一个循环,对吧?我们会和财务团队坐下来,财务团队向我们的软件工程师描述某个复杂的财务工作流程是怎么运作的,然后工程师们就去构建一些专用软件,里面是一套确定性的工作流,把他们讨论过的一切都封装进去,再交回给财务团队,如此循环往复。这让人感觉非常低效。

[04:06] **SPEAKER_02:** And then at the same time, this was right around the time when agentic tools were really agentic coding tools were really catching hold, right? And so you had kind of the first generation windsurf and cursor that were well established by this point. I think this right around when cloud code was introduced. I felt like this was giving me superpowers, right? And then kind of watching this sort of old classical way of building software in YC, and then watching how I was doing things on my own machine, it just felt like a bigger and bigger divide between those things.

> 与此同时,这恰好是 agentic 工具——尤其是 agentic 编程工具真正开始流行的时候,对吧?到那时,第一代的 Windsurf 和 Cursor 已经站稳了脚跟。我记得那大概也是 Claude Code 刚推出的时候。我感觉这些东西给了我超能力,对吧?然后一边看着 YC 内部这种老派、经典的软件构建方式,一边看着我在自己电脑上做事的方式,我就觉得这两者之间的鸿沟越来越大。

[04:36] **SPEAKER_02:** And so the original impetus was, why don't we try to build some tools at YC that we could use to run agents that would give the finance team control over their own software, right? Like, remove the software engineers from this crazy loop where they have to sort of understand these complicated workflows and give the finance team the tools that they could use to encode their own workflows, not as, you know. Not as Ruby, but as English, with prompts, right?

> 所以最初的动因就是:我们为什么不在 YC 试着构建一些工具,用来运行 agents,让财务团队能够掌控他们自己的软件呢?对吧?也就是把软件工程师从这个疯狂的循环里解放出来——他们本来得去理解这些复杂的工作流程——转而给财务团队工具,让他们能够自己来编码化他们的工作流,不是用 Ruby,而是用英语、用 prompt,对吧?

[05:03] **SPEAKER_00:** I mean, what's interesting is, like, we all funded companies maybe even, like, two or three years ago when LLMs were out, but, like, agentic coding wasn't a thing yet. And so the first thing actually was not agentic coding. It was LLMs for writing SQL queries. Yes. So that's what I remember from, like, the first versions of what you built was how, like, good it was and how basically it rhymed with, like, these other failed startups that we had funded.

> 有意思的是,我们大概在两三年前,LLM 刚出现、但 agentic 编程还没成为一回事的时候,就都投过一些公司。所以最先出现的其实并不是 agentic 编程,而是用 LLM 来写 SQL 查询。没错。所以我对你最初构建的那些版本的记忆,就是它有多好用,以及它基本上和我们投过的另外那些失败的创业公司如出一辙(却成功了)。

[05:29] **SPEAKER_00:** Yes. Like, each of us probably funded one. At some point, you know, here it was. It was working. And it worked so well that non-technical people, granted very smart people from finance but with no engineering background, could use these tools to ask real questions.

> 是的。我们每个人大概都投过一家这样的公司。而到了某个时刻,它就摆在这里,真的能用了。而且好用到那种程度:非技术人员——当然是财务部门里非常聪明、但没有工程背景的人——都能用这些工具去提出真正的问题。

[05:44] **SPEAKER_02:** I was really surprised, too, to be honest. And so that we started with this kind of purpose-built thing for finance and then rewrote it to even more of a general agent loop, right? And this is now, you see these all over the place now. But the first kind of magical thing, the magical moment that I had was we had this agent loop. And we had a tool registry, a shared tool registry, for kind of YC-specific tools.

> 说实话,我自己也非常惊讶。所以我们一开始做了这个为财务量身定制的东西,然后又把它重写成了更通用的 agent 循环,对吧?这种东西现在到处都能见到。但我经历的第一个神奇的东西、那个神奇的时刻,是我们有了这个 agent 循环,还有一个工具注册表——一个共享的工具注册表,用来存放各种 YC 专属的工具。

[06:09] **SPEAKER_02:** And the first tool that really was an unlock for me was, I think, a tool, looking back, that you actually built, Jared. It gave these agents the ability to run read-only SQL queries against our database. Yes. Right? It was two tools, actually.

> 而对我来说真正打开局面的第一个工具,现在回想起来,Jared,其实是你构建的那个。它赋予这些 agents 对我们数据库运行只读 SQL 查询的能力。对。对吧?其实是两个工具。

[06:23] **SPEAKER_02:** One was running queries against our database. And the other one was the ability to read our model files.

> 一个是对我们的数据库运行查询。另一个是读取我们的模型文件(model files)的能力。

[06:29] **SPEAKER_03:** I remember. I built those tools. And I felt a little bit like I was breaking the rules. Because initially, we started with very limited tools that had very narrowly-scoped domains. And I kept getting frustrated, because they weren't powerful enough to do the things that I wanted.

> 我记得。是我构建了那些工具。而我当时有点觉得自己在破坏规矩。因为一开始我们用的是非常受限、领域范围非常狭窄的工具。我一直很沮丧,因为它们的能力不足以完成我想做的事情。

[06:45] **SPEAKER_03:** And so I was like, what if we just gave the thing, like, access, complete access to the production database, where we could just, like, trample on anything? And I sort of, like, surreptitiously pushed it out, maybe late at night. And it worked. And it worked. It worked extremely well, right?

> 于是我就想:如果我们干脆把整个生产数据库的完全访问权限都给它,让它可以随便折腾任何东西,会怎么样?然后我就有点偷偷摸摸地把它上线了,大概是深夜。结果它成了。它真的成了。它效果好得惊人,对吧?

[07:02] **SPEAKER_03:** Yeah. Perhaps foreshadowing, you know, subsequent things like OpenClaw, where it turns out that, like, the thing that was hampering the world was being worried about security and privacy and all the things that could go wrong. And when you, like, worry a bit less, you're like, oh, my god. These things are unbelievably powerful.

> 是的。这也许预示了后来像 OpenClaw 这样的东西——事实证明,真正束缚这个世界的,是对安全、隐私以及各种可能出错的事情的担忧。而当你稍微少担心一点的时候,你会惊呼:天哪,这些东西的威力简直令人难以置信。

[07:17] **SPEAKER_02:** It's another really good example of this weird split between I'm at work, and I'm kind of operating in this really narrow box. And I'm at home using cloud code or whatever, like OpenClaw, or Hermit, and I can do anything, right? And trying to narrow that gap. So why was this so useful, this ability to run SQL queries against our database? It sounds really simple.

> 这又是一个很好的例子,说明了那种奇怪的割裂感:在公司里,我像是被困在一个非常狭窄的盒子里操作;而在家里用 Claude Code 或者别的什么,比如 OpenClaw、Hermit,我什么都能做,对吧?我们要做的就是缩小这个差距。那么,这个对数据库运行 SQL 查询的能力,为什么这么有用呢?它听起来实在太简单了。

[07:40] **SPEAKER_02:** Well, I think this is where it's important to talk about one of the big advantages that I think YC had coming into this experiment, which is that we run on our own software. And all of that software sits on one Postgres database that has everything that's important to YC's world in it. You know, every company that we funded, there's a company's table. There's a founder's table, right? There's tables for our financial transactions.

> 我觉得这里有必要谈谈 YC 进入这个实验时所拥有的一大优势,那就是我们运行在自己开发的软件上。而所有这些软件都建立在同一个 Postgres 数据库之上,里面装着对 YC 这个世界至关重要的一切。你知道吗,我们投过的每一家公司,都有一张 companies 表。有一张 founders 表,对吧?有记录我们财务交易的表。

[08:06] **SPEAKER_02:** There's tables for the notes that I leave in our little internal CRM, right? All of these functions that I think a lot of other companies farm out to third-party SaaS tools, we've built our own. And as a result, we have this database with every important piece of context that I can now ask questions like, hey, show me all of the investors who invested in a space-related company in the last four batches. Right? It just turns out, when all of that context is in one place, with a little bit of additional information about how the scheme is laid out, an agent can go and ask or answer arbitrary questions about our business.

> 还有记录我在我们那个小小的内部 CRM 里留下的备注的表,对吧?所有这些功能,很多别的公司都会外包给第三方 SaaS 工具,而我们都是自己构建的。结果就是,我们拥有这样一个装着每一条重要上下文的数据库,现在我可以问出这样的问题:嘿,给我看看过去四批(batch)里所有投资过太空相关公司的投资人。对吧?事实证明,当所有这些上下文都在一个地方,再加上一点关于这个数据结构如何布局的额外信息,一个 agent 就能对我们的业务提出或回答任意的问题。

[08:41] **SPEAKER_00:** MARK MANDELBAUM- That was a magic moment, for sure, when I first saw that.

> 我第一次看到那个的时候,那绝对是一个神奇的时刻。

[08:43] **SPEAKER_03:** MARK MIRCHANDANI- Yeah. And the cool thing for me is that it didn't just make it easier to answer questions. It dramatically increased the number of questions that we would ask and dramatically increased the scale and complexity of the questions that we would dare to ask. Where, like, in the old days, back when we were using, like, AI tools, to ask a question like that, you know, like, what investors have invested, like, in space-related companies, that would be, like, several hours of writing SQL. And so, like, unless it was really important, you just wouldn't bother.

> 是的。而对我来说很酷的一点是,它不只是让回答问题变得更容易了。它极大地增加了我们会去提出的问题的数量,也极大地增加了我们敢于提出的问题的规模和复杂度。要知道,在过去,当我们还在用那些(旧的)AI 工具的时候,要问出这样一个问题——比如哪些投资人投过太空相关的公司——那得花好几个小时来写 SQL。所以除非这事真的很重要,否则你根本懒得去查。

[09:10] **SPEAKER_02:** MARK MANDELBAUM- It's just another example of the, you know, this instance of Jeevan's paradox that you get when you remove the amount of back and forth between different teams in order to get a thing done, right? If, in order to ask some kind of complex question about YC, I have to go and knock on, you know, the data science team's door and wait for them to get it through, you know, their backlog, I'm just going to ask far fewer questions.

> 这又是一个例子,体现了当你把不同团队之间为了完成一件事而来回沟通的成本消除掉时所出现的那种杰文斯悖论(Jevons paradox),对吧?如果我为了问一个关于 YC 的复杂问题,得去敲数据科学团队的门,然后等着他们把这件事从待办事项里排上来处理,那我提出的问题自然就会少得多。

[09:36] **SPEAKER_00:** MARK MANDELBAUM- I mean, there are people out there watching this who work in places that still use it. The majority of people live in that world still, and it's 2026, which is a little unfathomable, actually.

> 我是说,看这期节目的人里,肯定有人所在的地方还在用那套老办法。大多数人其实仍然生活在那个世界里,而现在已经是 2026 年了,这想想还真有点难以理解。

[09:46] **SPEAKER_02:** MARK MANDELBAUM- There's a long way to go, I think, which is really exciting.

> 我觉得还有很长的路要走,而这恰恰非常令人兴奋。

[09:49] **SPEAKER_01:** LESLIE KENDRICK- The last one question is, how do companies that live in that old world could get sort of wings to move so quickly? Because the magic for us was, as you said, everything was, the context was in one place. That made it easy.

> 最后一个问题是,那些还生活在旧世界里的公司,要怎样才能长出翅膀、快速前进呢?因为对我们来说,那种神奇之处正如你所说,在于一切、所有的上下文都集中在一个地方。这一点让事情变得容易。

[10:03] **SPEAKER_00:** MARK MANDELBAUM- You know, if you think about data science, historically, one of the first things that the Googlers had to figure out was Bigtable, right? And Bigtable was, you know, instead of schema and joins, you have one Bigtable that can be map-reduced. And so I think that that's happening again, and I would argue that that's happening now with Karpathy-style knowledge LLM wikis with G-Brain. I mean, that's what I'm seeing anyway. Like, you know, obviously, I have an OpenClaw.

> 你知道,如果你想想数据科学的历史,Google 那帮人最早需要搞明白的东西之一就是 Bigtable,对吧?Bigtable 的思路是,不用 schema 和 join,而是用一张可以做 MapReduce 的大表。所以我觉得这件事正在重演,而且我认为它现在正随着 Karpathy 风格的知识型 LLM wiki、随着 G-Brain 而发生。反正这是我所看到的。你知道,显然我有一个 OpenClaw。

[10:35] **SPEAKER_00:** It has access to lots of systems. And then I'm normalizing it to my own schema that's relevant to me and the things that I care about. And it is like denormalization. It's you're taking data and you're putting it into a format that is more or less optimized for OpenClaw or Hermes Agent, like that particular type of harness to be able to ask questions. And it needs retrieval.

> 它能访问很多系统。然后我把这些数据规范化(normalize)成我自己的、与我以及我所关心的事物相关的 schema。这有点像反规范化(denormalization)。你是在把数据整理成一种或多或少针对 OpenClaw 或 Hermes Agent、也就是针对那种特定类型的 harness 提问而优化过的格式。而它需要检索(retrieval)。

[10:58] **SPEAKER_00:** It needs RAG. It needs graph RAG. It needs, you know, hybrid RRF. Like, there's re-ranking in there. Like, you know, all the things that everyone has learned about retrieval is now inside G-Brain.

> 它需要 RAG。它需要 graph RAG。它需要那种混合 RRF(倒数排名融合)。里面还有重排序(re-ranking)。就是说,所有人学到的关于检索的一切,现在都装进了 G-Brain 里。

[11:08] **SPEAKER_00:** And then when you give the agents a soul and you give it the data and it knows you and what you care about, like, suddenly these things have insane wings. Like, I just kind of can't believe how it sees around corners. And you might ask a question, and it'll even, you know, sort of interpret what you are what your question was about and, like, give you a thing that, frankly, like, it would take a human who really knows you well to answer. All that's possible now. And so, you know, your question is, like, all the data is everywhere.

> 然后,当你给这些 agents 一个灵魂,把数据交给它,它了解你、了解你所关心的东西,突然之间这些东西就长出了疯狂的翅膀。我简直不敢相信它能怎样看到拐角之外的东西。你可能问一个问题,它甚至会去揣摩你这个问题到底想问什么,然后给你一个答案——坦白说,那种答案得是一个真正非常了解你的人才能给出的。这一切现在都成为可能了。所以呢,你的问题是:所有的数据到处都是。

[11:41] **SPEAKER_00:** My answer from, like, the OpenClaw Hermes experience with G-Brain is, like, yeah, you basically have to take that you're going to denormalize it and you're going to put it in a format that is optimized for agent retrieval and understanding. You could wrap it in an MCP, but for whatever reason, I just, like. intuitively, I'd be worried. Like, it's still sort of, you know, these things are really good at working with MCP and CLI. They're a little even better with CLI.

> 我从 OpenClaw、Hermes 加 G-Brain 的经验出发给出的答案是:是的,你基本上得接受一件事——你要把这些数据反规范化,把它整理成一种针对 agent 检索和理解而优化的格式。你可以把它包装成一个 MCP,但不知为什么,凭直觉我就是会有点担心。就是说,这些东西确实很擅长使用 MCP 和 CLI,而用 CLI 甚至还要更好一点。

[12:06] **SPEAKER_00:** It seems like you have to denormalize and do the big table thing, but, you know, specifically for the agent.

> 看起来你必须做反规范化、做那套 Bigtable 的事情,只不过要专门针对 agent 来做。

[12:12] **SPEAKER_02:** Looking back over the last year and a half, it feels like we're still kind of in the single-player era of agents, where the harnesses that have gotten really popular, right, CloudCode, Codex, Py, OpenClaw, Hermes, they're all designed to be used by a single human running on a single machine. And it makes a lot of sense, right? Because in that environment, these agents can do just about anything, right? And they make you incredibly powerful. They're a lot of fun to use.

> 回顾过去这一年半,感觉我们仍然处在 agents 的"单人游戏"时代——那些真正火起来的 harness,像 Claude Code、Codex、Py、OpenClaw、Hermes,它们都是为单个人在单台机器上运行而设计的。这很合理,对吧?因为在那种环境里,这些 agents 几乎无所不能,对吧?它们让你变得极其强大。用起来也很有乐趣。

[12:43] **SPEAKER_02:** I think one of the big problems that I don't think has been solved well yet by anybody is the multiplayer harness, right? It's enabling that kind of superpower, but on a team or an organizational level, right? And that's, I think. been the interesting thing to explore with the infrastructure that we've built at YC is watching which primitives that we've created that have enabled individuals and teams to use agents. You asked the question about if you're working inside of a kind of a legacy organization, which is like anyone who's more than two years old, what are the things that you can focus on in order to help enable everybody at your org to use AI to do more?

> 我认为有一个至今还没有人很好地解决的大问题,就是"多人 harness",对吧?也就是把那种超能力赋能到团队或组织的层面上,对吧?我觉得这正是我们在 YC 构建的基础设施里值得探索的有趣之处——观察我们创造的哪些基本原语(primitive)真正让个人和团队用起了 agents。你刚才问,如果你身处一个所谓的"遗留组织"里——也就是任何成立超过两年的组织——你可以聚焦在哪些事情上,来帮助组织里的每个人都用上 AI、做更多的事?

[13:26] **SPEAKER_02:** And we talked about kind of this common context layer, right? And so a data warehouse where just as much of your internal important context lives, it just turns out is extremely useful. There are many tools for connecting individual agent harnesses to other MCP tools, other sources of truth. But just like a coding agent inside a model repo just tends to be much more efficient, watching our agents operating on our single database that has everything in it, in one schema tells me that there's a lot of value at least in getting all of the context into one place. Having an internal tool registry, this is I think the other really important thing that we've built.

> 我们谈到了这个共同的上下文层,对吧?也就是一个数据仓库,让尽可能多的内部重要上下文都汇聚在里面——事实证明这极其有用。现在有许多工具可以把单独的 agent harness 连接到其他 MCP 工具、其他真相来源上。但就像一个在单一代码仓库(monorepo)里工作的编程 agent 往往效率高得多一样,看着我们的 agents 在我们那个装着一切、只用一套 schema 的单一数据库上运作,让我明白:至少把所有上下文集中到一个地方,是很有价值的。拥有一个内部工具注册表——我认为这是我们构建的另一个真正重要的东西。

[14:09] **SPEAKER_02:** So in the beginning, like we were talking about, it was just the whole system was really simple. It was like an agent loop and a simple tool registry and a few other pieces, right? Like a model router underneath. The tool registry is where most of the like YC specific stuff lives, right? Like tool registry is what turns, it turns these agents into something that's useful at work.

> 所以一开始,正如我们刚才说的,整个系统真的非常简单。就是一个 agent 循环,加上一个简单的工具注册表,再加上其他几个部件,对吧?比如底层的一个模型路由器(model router)。工具注册表是绝大多数 YC 专属东西所在的地方,对吧?正是工具注册表把这些 agents 变成了在工作中真正有用的东西。

[14:31] **SPEAKER_02:** And we had like 20 tools at the beginning, including this magical ability to query our SQL database. But over time, teams have added more and more tools. Every time we kind of come upon some piece of work at YC that we think could be improved with an agent, we can just add tools. And there's more than 350 today. I just checked, right?

> 一开始我们大概有 20 个工具,包括那个神奇的查询 SQL 数据库的能力。但随着时间推移,各个团队添加了越来越多的工具。每当我们在 YC 遇到某项我们觉得可以用 agent 来改进的工作,我们就可以直接添加工具。到今天已经有 350 多个了。我刚查过,对吧?

[14:50] **SPEAKER_02:** Every team is adding their own tools. You know, I can do things like manage my office hours. Our finance team can, you know, can book journals. We can do internal entries, right? We can help manage the events that we run.

> 每个团队都在添加自己的工具。你知道,我可以做一些事情,比如管理我的 office hours(答疑时间)。我们的财务团队可以记账。我们可以录入内部分录,对吧?我们可以帮忙管理我们举办的各种活动。

[15:02] **SPEAKER_02:** There's tools for all of the important work that we do at YC. And now once these all exist in one place, you can make them available to these internal agents that we've built. But you can also make them available to Cloud Code, you know, running on our individual machines. So those things above all, I think, were the important pieces that we built that if I were working in any other organization,

> 我们在 YC 所做的所有重要工作都有对应的工具。而现在,一旦这些工具都集中在一个地方,你就可以把它们提供给我们构建的这些内部 agents。但你同样可以把它们提供给运行在我们各自机器上的 Claude Code。所以我认为,以上这些是我们构建的最重要的部件——如果我在任何别的组织工作,

[15:25] **SPEAKER_00:** I would focus on building. I mean, honestly, inspired by what you guys, what you did with tools, like this idea of Skillify in OpenClaw. And then actually the most important, the last part of Skillify, Skillify is like this meta skill that I made in OpenClaw where it's like you just do anything in OpenClaw and Hermes. Hermes actually already has Skillify. They call it something that's like, it makes skills automatically.

> 我都会把重点放在构建这些东西上。说实话,受你们在工具方面所做工作的启发,比如 OpenClaw 里 Skillify 这个想法。而其实最重要的、Skillify 的最后一部分——Skillify 是我在 OpenClaw 里做的一个元技能(meta skill),就是说你在 OpenClaw 和 Hermes 里随便做什么。Hermes 其实已经有 Skillify 了,他们管它叫别的名字,反正它会自动生成技能。

[15:46] **SPEAKER_00:** But the most important thing I think is actually like plugging it into the resolver, which is like your Agents.md with like the list of things that the agents can do. And then like, it links to the, markdown entry point that like lets you use a tool basically and so like this thing keeps coming up in all these different contexts like cloud code has a skill the skill registry in cloud code is actually a resolver our tool registry is actually a resolver and then the weird thing that you have to do on top of that is actually um i have a meta skill called check resolvable that i call all the time so i'm always like i do something that's new or different in uh in my agent and then after it does it and i like it i say skillify it and then it becomes basically like a tool call or method call and then i run check resolvable which is like you know look at all of the other skills and uh tools that exist and is it you know dry don't don't repeat yourself and is it uh m-e-c-e which is you know i'm embarrassed to say a mckinsey term for um the consultants use it for for uh making really good slide decks mutually exclusive collectively exhaustive that's like how you're supposed to do slides if you're a mckinsey consultant but it's useful because it's like an additional layer on top of don't repeat yourself dry and like the models just seem to know what those things are and so if you have a dry and m-e-c-e resolver table anywhere it's actually like the optimal resolver like it's bad to have 10 skills that do all the same thing it's good to have one skill or one tool that has parameters that then let you call them so i don't know i think it's like this is like the wildest time to be alive as like an applied computer scientist because it's like simultaneous like discovery of the same useful applied concepts over and over again and i wonder if like when people are you know developing the first versions of unix or something it's like discovering a stack and a heap it feels like we're right at that moment today like we're just coming up with the new primitives for what i'm doing right now so what an agentic system actually is and you can see it in the parallel sort of development of like we're just trying to do a thing and it might be in cloud code or it might be in our own internal harness or it might be in open claw might be in hermes like these things just keep coming back

> 但我认为最重要的其实是把它接入解析器(resolver),也就是你的 Agents.md 那样列出 agents 能做哪些事的清单。然后它会链接到 markdown 入口点,基本上让你能够使用某个工具。所以这个东西在各种不同的场景里不断出现:Claude Code 有 skill,Claude Code 里的 skill 注册表其实就是一个 resolver;我们的工具注册表其实也是一个 resolver。而你在这之上还得做一件奇怪的事:我有一个叫 check resolvable 的元技能,我一直在用。所以我总是这样——我在我的 agent 里做了某件新的或不一样的事情,等它做完、我觉得满意了,我就说"把它 skillify 掉",于是它基本上就变成了一个工具调用或方法调用。然后我运行 check resolvable,它会去查看所有已存在的其他 skill 和工具,判断它是否符合 DRY(Don't Repeat Yourself,不要重复自己),是否符合 MECE——我不好意思地说,这是个麦肯锡术语,咨询顾问用它来做非常出色的幻灯片,意思是"相互独立、完全穷尽"(mutually exclusive, collectively exhaustive),如果你是麦肯锡顾问,幻灯片就该这么做。但它很有用,因为它是叠加在 DRY 之上的又一层,而且模型们似乎天生就知道这些概念是什么意思。所以如果你在任何地方有一张既 DRY 又 MECE 的 resolver 表,它其实就是最优的 resolver。有 10 个做同一件事的 skill 是糟糕的;有一个带参数、然后让你据此调用的 skill 或工具才是好的。所以我不知道,我觉得对一个应用计算机科学家来说,现在是最疯狂的时代,因为你会一次又一次地同时发现同样有用的应用概念。我在想,当年人们开发最初几个版本的 Unix、或者发明栈和堆这些概念的时候,是不是也是这种感觉。感觉我们今天正处在那个时刻,我们正在为我现在做的事情、为"一个 agentic 系统到底是什么"发明新的原语。你可以从这种平行的发展中看出来:我们只是想做成一件事,它可能是在 Claude Code 里,可能是在我们自己的内部 harness 里,可能是在 OpenClaw 里,可能是在 Hermes 里,而这些东西就是会不断地重现出来。

[18:04] **SPEAKER_04:** over and over again yc startup school is back we're hand selecting the most promising builders in the world and flying them out to san francisco for july 25th and 26th to discuss the cutting edge of tech and startups apply now for your spot

> 一次又一次地重现。YC Startup School 回来了。我们正在从全世界精挑细选最有潜力的构建者,把他们请到旧金山来,参加 7 月 25 日和 26 日的活动,一起探讨科技和创业的最前沿。现在就申请你的名额吧。

[18:20] **SPEAKER_02:** it's really interesting to look at how some of the other companies that are building this stuff uh have built their infrastructure because you see a lot of these same primitives in in each of them right like there's the agent loops there's tool registries there's skill registries looking at at the way that we're using skills now at yc so if you think of skill as a simple abstraction layer over tools we have a handful of sort of shared skills uh that that we all have access to uh through this through this agent system and it's been interesting to watch i think you've talked about this for this progression of like in the beginning you were kind of writing your own system prompts and then skills emerged so you started writing your own skills and then you would start uh meta prompting where you uh where you know

> 观察其他一些在构建这类东西的公司是如何搭建他们的基础设施的,这非常有意思,因为你会在它们每一个身上看到许多相同的原语,对吧?比如都有 agent 循环、工具注册表、skill 注册表。看看我们现在在 YC 使用 skill 的方式——如果你把 skill 理解为在工具之上的一个简单抽象层,我们有那么一小把共享的 skill,是我们所有人都能通过这套 agent 系统访问的。观察这个演进过程很有意思,我记得你谈过:一开始你是自己写系统 prompt,后来 skill 出现了,于是你开始写自己的 skill,再后来你就开始做元提示(meta prompting),也就是——

[19:03] **SPEAKER_00:** you do it again write a skill exactly improve the prompt yes automatically yes seeing us kind of do

> 你再来一次、写一个 skill——没错——改进那个 prompt——对——自动地——对。看着我们这样做——

[19:09] **SPEAKER_02:** the same progression internally where we have a couple skills and now we've gotten to the point where we have these sort of autonomous self-improving loops right uh you know and so

> 在内部经历同样的演进:我们有了几个 skill,而现在我们已经走到了这一步——我们有了这种自主的、自我改进的循环,对吧,你知道,所以——

[19:20] **SPEAKER_00:** we're able to work in a way where we can take a little bit more practice uh that way you can

> 我们能够以一种方式工作,让我们可以多加一点练习,这样你就可以——

[19:24] **SPEAKER_02:** maybe move a little bit more fluidly when you're working on a task and make there's a little bit more feedback but it's also easier to put in place a way to just run through it and be like okay this is a good idea and let's just go ahead and do it one more time and then we can just draw some more data and just work with it and we can figure out how we're going to put the

> 在处理一个任务时也许能更流畅一点,让反馈稍微多一些。但也更容易建立起一套机制,让你能直接跑一遍,然后说:好,这是个好主意,那我们就再来做一次;接着我们可以再获取更多的数据、拿它来处理,然后我们就能想清楚该怎样把这些——

[19:40] **SPEAKER_00:** information in that so that way we can actually put in place the especially in the context that really would be useful uh for the training our scenario so in this case we're going to sort of um be more inclusive in the same way that we would in a different way that we would work with potentially um read all the transcripts and then write them back into the internal uh db into the

> ——信息放进去,这样我们就能真正建立起一套机制,尤其是在那些对训练我们的场景真正有用的上下文里。所以在这种情况下,我们会以一种更兼容并包的方式,就像我们会用另一种方式去处理那样,有可能去读取所有的对话记录(transcript),然后把它们写回到内部的数据库、写回到——

[19:58] **SPEAKER_02:** internal crm on like what we know about people and companies indeed and we there are cool examples of using transcripts actually to make these skills more effective as well one of the shared skills that we have uh is a skill that that partners at yc use to help our companies uh write what we call two sentence descriptions right everybody here has written hundreds of these we should probably

> ——内部 CRM 里,记录我们对人和公司的了解。确实如此。而且我们确实有一些很酷的例子,是利用对话记录来让这些 skill 变得更有效的。我们有一个共享的 skill,是 YC 的合伙人用来帮助我们投的公司写我们所谓的"两句话描述"(two sentence description)的,对吧。在座每个人都写过成百上千条这样的东西。我们大概应该——

[20:23] **SPEAKER_00:** explain what a two sentence description actually sure so a two sentence description is a concise

> ——解释一下"两句话描述"到底是什么。好的。所谓两句话描述,就是一种简洁的——

[20:29] **SPEAKER_02:** way of explaining what your company does in natural language that anyone will understand

> ——用自然语言解释你的公司是做什么的方式,让任何人都能听懂,

[20:33] **SPEAKER_03:** and why it's interesting sounds easy but it's surprisingly hard for founders to actually

> ——以及它为什么有意思。听起来容易,但对创始人来说,真要做到却出人意料地难。

[20:37] **SPEAKER_00:** and also no one does it weirdly weirdly like even the most experienced founders like forget because they have perfect context actually interestingly uh i now realize yc itself is uh context engineering uh sort of process in that like people we're frequently teaching people you have perfect context about what's going on in your brain but great communication is replicating that same context in someone else's brain and that's what a two-sentence pitch is like what is it like i don't even know what the heck this is and then second part is like is it interesting or valuable what you know is it worth my time and so that you know when i when i teach two sentence pitches that's my favorite way to do it do i even know what the heck this is yes because if you don't know what it is you can't even ask a question about it it's like something about computers i guess whatever what what time is lunch again and then the second part is equally important which is like if i've heard that you know there are like 20 companies like there are five other companies in this room that do x like and then i don't understand like why this is noteworthy like again i'm like thinking about my pastrami sandwich again right so so the two sentence pitch like viscerally

> 而且很奇怪,没有人真的会去做。奇怪的是,连最有经验的创始人都会忘了做,因为他们脑子里的上下文太完整了。其实很有意思,我现在意识到 YC 本身就是一个上下文工程(context engineering)的过程。我们经常教人们:你对自己脑子里正在发生的事情拥有完美的上下文,但优秀的沟通,是把这同一份上下文复制到别人的脑子里。而这正是两句话推介所做的事。第一部分是:这到底是个什么东西?我压根不知道这是啥。第二部分是:它有意思吗、有价值吗?它值不值得我花时间?所以当我教两句话推介的时候,我最喜欢的方式就是问:我到底知不知道这是个什么玩意儿?因为如果你连它是什么都不知道,你甚至没法对它提问——大概是跟电脑有关的什么东西吧,随便了,午饭几点来着?然后第二部分同样重要:如果我听完之后觉得,你知道,已经有 20 家公司、这屋里就有另外五家公司在做 X 这件事,而我不明白这为什么值得关注,那我又开始惦记我的熏牛肉三明治了,对吧。所以两句话推介对创始人来说是一种——

[21:49] **SPEAKER_02:** for founders and it's it's a it's a simple kind of atomic thing that every partner at yc has practiced over and over and over again i think tom uh one of one of the partners here wrote a skill that teaches an agent how to uh take some context about a company and can and condense that into a two-sentence description and so that was his sort of handwritten prompt or skill about how that was done and one of the cool things that happened in the last month or two was that a couple of the other partners took a meeting that they had with a group office hours they had with a bunch of the companies in the spring batch and just went through and had every founder try their hand at a two-cent subscription and kind of gave them feedback and input and so kind of the knowledge that lives in a partner's head about how to do this effectively was exchanged back and forth right and and and now lived in the context of of that meeting transcript and handing the agent and saying given you know what you've learned by reading through this context improve the two-sentence description skill and they got noticeably better after that like this thing is now better than i am i would i would argue at writing those this is how super intelligence

> 对创始人来说,它是一种简单的、原子级的东西,而 YC 的每一位合伙人都反复练习过无数次。我记得 Tom——这里的一位合伙人——写了一个 skill,教 agent 如何拿到关于一家公司的一些上下文,把它浓缩成一段两句话描述。所以那是他手写的、关于该怎么做这件事的 prompt 或 skill。而过去一两个月里发生的一件很酷的事情是:另外几位合伙人把他们和春季批次里一群公司开的一次集体 office hours 拿出来,逐一让每位创始人自己动手写两句话推介,然后给他们反馈和意见。于是原本存在于某位合伙人脑子里的"如何高效做这件事"的知识,就这样来回交流了,对吧,而现在它存在于那次会议的对话记录这份上下文里。接着把它交给 agent,说:根据你读完这份上下文所学到的东西,去改进这个"两句话描述"的 skill。之后它明显变好了。我甚至可以说,现在它写这些东西已经比我还厉害了。组织内部的超级智能,就是这样——

[23:04] **SPEAKER_00:** happens inside organizations i mean this two-sentence pitch thing sounds like something kind of small but uh embedded in it is actually something very powerful i'm sure you guys have heard um jack dorsey talk about what he's doing with block he basically is trying to turn block into a mini agi around helping people in the world make payments to one another right uh and then this is actually the micro mechanism by which he's going to do that right like you can look at the operation of any organization as uh the aggregate of you know i mean the two-sentence pitch at yc is that's sort of one of like thousands of things that i would argue we do for founders but you know we just walk through a very concrete way where someone wrote a prompt used it used a bunch more other people used it a bunch of artifacts came off of that around literally like the transcript of using it becomes a thing that can be used to meta prompt and improve in an automated fashion on a daily basis the operation of that one skill and then suddenly that one skill you just said it that skill is now better than any of us individually than bef you know when before we actually had access to that and so this is like a particular like needle pinprick in the fabric of like how any organization does things and then how do you build super intelligence inside a company you do that on everything you do and it's not more complicated than that like you literally just compose everything that you do and any given thing that any given person can do you combine that in aggregate and in this particular process and like you have a super organization it's possible now like every single person watching this is a super organization it's possible now like every single person watching this can do this at any company at their own company they can do it at their job i mean the interesting thing is that's why you should start a startup because people are going to be trapped in organizations with people running organizations that are very powerful and have all these resources and all this capital that do not believe what we just said because they keep all the contacts locked down right because it's unsafe it's unsafe this is one of those things that we

> ——在组织内部发生的。我是说,这个两句话推介听起来像是件挺小的事,但里面其实蕴含着某种非常强大的东西。我相信你们都听过 Jack Dorsey 谈他在 Block 做的事——他基本上是想把 Block 变成一个围绕"帮助世界上的人们彼此付款"的迷你 AGI,对吧。而这其实正是他实现这一目标所依赖的微观机制,对吧。你可以把任何组织的运作看成是一个总和。YC 的两句话推介,只是我可以说我们为创始人做的成千上万件事之一。但你看,我们刚刚走了一遍一个非常具体的过程:有人写了一个 prompt、用了它,更多人也用了它,由此产生了一堆产物——使用它的对话记录本身,就成了一个可以拿来做元提示、以自动化的方式每天改进这一个 skill 运作的东西。然后突然之间,你刚才也说了,这一个 skill 现在比我们任何一个人单独都更强,比我们真正能用它之前更强。所以这就像是在"任何组织如何做事"这块织物上扎下的一个针尖大小的点。那么你如何在一家公司内部构建超级智能?你把这件事应用到你所做的每一件事上,就这么简单,不比这更复杂。你真的就是把你所做的一切、把任何一个人能做的任何一件事,全部组合起来,加总到一起,套进这个特定的过程里,你就拥有了一个超级组织。这现在就能做到——看这期节目的每一个人本身就是一个超级组织,这现在就能做到。看这期节目的每个人,都可以在任何公司、在他们自己的公司、在他们的工作岗位上做到这一点。有意思的地方在于,这正是你应该去创业的原因——因为人们将会被困在一些组织里,而那些运营这些组织的人非常强大、掌握着所有这些资源和资本,却不相信我们刚刚说的这些话,因为他们把所有的上下文都锁得死死的,对吧,因为那"不安全"、"不安全"。这就是我们要谈的其中一件事——

[25:13] **SPEAKER_01:** talk about um how to build that ai native organization right part of the key thing is not to do just use ai as a co-pilot i think that's very 2023 four right this is the the thing where you use it as uh really the the building layer for everything and you need to start recording all the artifacts like people wouldn't have thought of uh meeting recordings and it is one of those reasons why all these uh meeting recorders have been taking off people have been finding them with coaching them on the meetings but it's not just that you could take that and improve all the output for you that you do like writing emails communication planning you have

> ——如何构建那种 AI 原生的组织,对吧。关键的一点是不要只把 AI 当作副驾驶来用,我觉得那非常 2023、2024,对吧。真正的做法是把它作为一切事物的构建层,而且你需要开始记录下所有的产物。比如人们本来不会想到去做会议录音,而这正是所有这些会议记录工具火起来的原因之一——人们发现可以用它们来给会议做复盘辅导。但不仅仅如此,你还可以拿这些记录去改进你做的所有产出,比如写邮件、沟通、做计划——你手里握有——

[25:54] **SPEAKER_05:** the whole context of everything it's funny i remember the dario essay where it's like there's some of the blockers and just the rate of progression of ai are not technical they're just sort of like social cultural things things kind of like a really interesting example two years ago it would have seemed i just remember it felt odd to just like record a meeting or like there was just like people trying to figure out what the like social etiquette around it was and today i just feel like it's almost like default assumed that like most beings are being required especially if they're on zoom but just in general like everyone started recording things now it's a

> ——一切事物的完整上下文。有意思的是,我记得 Dario 那篇文章里说,AI 前进速度的某些阻碍并不是技术性的,而更像是社会、文化层面的东西。有个很有意思的例子:两年前,单是录一场会议就会显得很怪,我记得那种感觉很别扭,大家都在琢磨围绕这件事的社交礼仪该是什么样。而到了今天,我感觉几乎已经默认——大多数会议都被要求录音,尤其是在 Zoom 上的时候,但总体而言,每个人都开始录东西了。现在这——

[26:27] **SPEAKER_02:** little scary but i think if you frame this as a way for everyone in an organization to get better at what they do using the like collective skill and instinct of of the people they work with it's incredibly powerful having a canonical two-sentence description skill is not just a way to like generate a snippet of text for a founder it's a way to help me get better at understanding what makes for effective founder communication right because now i can tap into everything that diana and harge and you two have learned over the many years you've done this job which are now kind of baked into this skill through the conversations that you've had it's like a shared organizational

> ——有点吓人,但我认为,如果你把它理解为一种方式,让组织里的每个人都能借助身边同事的集体技能和直觉,把自己的工作做得更好,那它的威力是极其惊人的。拥有一个标准的(canonical)"两句话描述" skill,不只是给创始人生成一段文字的方式;它是一种帮助我更好地理解"什么才算高效的创始人沟通"的方式,对吧。因为现在我可以调用 Diana、Harge 以及你们俩在这份工作干了这么多年里所学到的一切——这些东西如今都通过你们进行过的那些对话,烘焙进了这个 skill 里。它就像是一个共享的组织——

[27:08] **SPEAKER_03:** brain yes this is very empowering the closest thing to us being able to like connect our brains

> ——大脑。是的,这非常赋能。它几乎是我们能够把彼此的大脑连接起来的最接近的形态,

[27:12] **SPEAKER_02:** right yeah it it totally is right and i can have an agent now come and i can do this sessions with it right i can have it critique my like there there are so many possibilities once you get all of this knowledge into a place where an agent can can work with it uh it's a it's a it's a very empowering thing for every human in the organization there's some subtle interesting

> ——对吧。是的,完全就是这样,对吧。现在我可以让一个 agent 过来,我可以和它做这样的一对一练习,对吧,我可以让它点评我的——一旦你把所有这些知识汇集到一个 agent 能够处理的地方,可能性就多得数不清。这对组织里的每一个人来说都是一件非常赋能的事。这里面有一些微妙而有趣的——

[27:32] **SPEAKER_00:** things around here that like you know other people might get wrong that like i feel like we've gotten right i mean one of them is by default the agent conversation is actually um globally viewable by any full-time employee at yc you know we sort of weren't sure about that decision i mean it felt right and it felt like living in the future but it did not come easily i feel like we had a lot of conversations about like well then everyone sees everything is that okay and like you know what is not okay and then i'm glad we made the choice to keep it open actually because i agree people learned how to use it from

> ——地方,别人可能会搞错,而我觉得我们做对了。其中之一是:默认情况下,agent 的对话其实是全局可见的,任何 YC 的全职员工都能看到。你知道,我们当时对这个决定并不太确定。它感觉是对的,感觉像是活在未来,但这个决定来得并不轻松。我记得我们有过很多讨论:那这样一来所有人都能看到所有东西,这样可以吗?什么才是不可以的?后来我很庆幸我们选择了保持开放,因为我同意——人们正是通过——

[28:08] **SPEAKER_02:** watching how other people used it we used that transparency to solve several problems at the same agent conversation as you mentioned was broadcast internally to a slack channel and anybody could join that slack channel and look and learn right and i remember this is another kind of big unlock one was when you started using it really heavily you were like super creative with with the things you were doing with it and a lot of us watched that it was like oh wow i didn't even you can do that now to use it that way right it allows you to be a little more lenient on internal security right one of the things we talked about earlier was this trade-off where these agents are at their most powerful when they are given unrestricted access to lots of context which runs counter to the way more most organizations work it turns out that by defaulting to public broadcast for these conversations you kind of institute a bit of a social control on what people can do with it uh that as we learned i think has been like reasonably effective uh inside of this high trust environment at keeping private information private

> ——观察别人怎么用它,才学会了怎么用。我们利用这种透明度同时解决了好几个问题。正如你提到的,agent 的对话会被内部广播到一个 Slack 频道里,任何人都可以加入那个 Slack 频道去看、去学,对吧。我记得——这是另一个很大的突破——其中之一是当你开始非常频繁地使用它时,你用它做的那些事情特别有创意,我们很多人看着就想:哇,我都不知道原来可以这么做、原来可以这样用它,对吧。这让你在内部安全上可以稍微宽松一点,对吧。我们前面谈过的一个权衡是:这些 agents 在被赋予不受限制地访问大量上下文的权限时最为强大,而这与大多数组织的运作方式恰恰相反。事实证明,通过默认把这些对话公开广播,你其实就建立起了一层轻微的社会约束,约束着人们能拿它来做什么——而据我们的经验,在这种高信任的环境里,这在保护私密信息不外泄方面,一直相当有效。

[29:15] **SPEAKER_00:** yeah what's interesting is um it it betrays two traits of uh truly agentic like 1000x super intelligent organizations that i would not have necessarily guessed would exist but are now like must exist if you want to create this type of organization you have to be relatively egalitarian and you also have to be trust by default and then neither of those things uh actually are most organizations in the world if you're the founder of an organization you actually have to have those at the core of what

> 是的,有意思的是,它暴露出真正 agentic 的、1000 倍超级智能组织的两个特质——这两点我原本未必会猜到它们会存在,但现在看来,如果你想创造这种类型的组织,它们就必须存在。你必须相对平等(egalitarian),而且你还必须默认信任(trust by default)。而这两点,恰恰都不是世界上大多数组织的样子。如果你是一个组织的创始人,你其实必须把这两点放在你所做一切的核心——

[29:43] **SPEAKER_02:** you're doing and i think like that kind of environment honestly works best at startups right when it's a small group of people that are all aligned and and and

> ——你所做的事情的核心。而我觉得,说实话,那种环境在创业公司里最能发挥作用,对吧,当它是一小群目标一致、并且——

[29:53] **SPEAKER_00:** operating in a high trust environment the other thing you have to do is be willing to spend like ten to a hundred thousand dollars a year on tokens but if you're willing to do it and you invest in the skills and you like actually do everything in an open way with your team that way like basically what i realize is it allows you to live in 2028 right like what you spend a hundred thousand or a million dollars a year on now it will be commonplace in the future for the rest of your life like in in two years right it'll it won't cost a hundred thousand in a year it'll cost ten thousand and the year after that it'll be like a couple hundred bucks right and everyone will do it and we'll call it like this is how companies are now so basically there's a one-time time warp where you can leapfrog every incumbent all fortune 500s all startups that exist by doing

> ——在高信任环境里运作的一小群人。你还必须做的另一件事,是愿意每年花大概一万到十万美元在 token 上。但如果你愿意这么做,愿意在这些 skill 上投入,愿意真的以开放的方式和你的团队一起做每一件事,那么——我基本上意识到——它能让你活在 2028 年,对吧。你现在每年花十万或一百万美元买到的东西,在未来的某个时点会变得司空见惯,在往后你的余生里都是如此——比如两年后,对吧,它不会再花十万美元一年,只要一万;再一年后,大概就只要几百块了,对吧,人人都会用,而我们会说"现在公司就是这么运作的"。所以本质上,存在一个一次性的"时间穿越"窗口,让你可以通过这么做,一举跨越现有的每一个巨头——所有的《财富》500 强、所有现存的创业公司——

[30:40] **SPEAKER_03:** this like I'm imagining in the 90s I wonder if it felt similarly one company started buying computers for their employees yeah they were probably very expensive and probably only certain companies really invested in buying these like expensive flaky computer systems for their employees but like what a superpower to have a computer when your competitors like don't have

> 就像——我在想象 90 年代,不知道当时是不是也是类似的感觉:某家公司开始给员工买电脑。是啊,那些电脑大概非常贵,大概只有某些公司才真正舍得投钱给员工买这些昂贵又不太稳定的计算机系统。但当你的竞争对手都还没有电脑的时候,拥有一台电脑是多么大的一种超能力啊——

[30:59] **SPEAKER_01:** computers I think we're technically how I've seen this effect YC has been raising the floor the floor in a sense what I mean by that is that you could have a new employee joining and maybe would have taken them six months to ramp up but with this it's sort of like they automatically get a lot of the context from the company working and they know how the best people on the star players in the organization do things by apprenticeship automatically with AI instead of that because partner time is expensive or sometimes the best people in an org they're very busy right and you get to kind of run the simulation of what it's like to be like Pete when he does like an awesome job coaching founders on sales or like Gary when he's like talking to founders are giving very specific advice I think it helps all the new new entrants in the organization just be a mini version of

> ——竞争对手都没有电脑。我觉得,从技术上讲,我观察到这种效应的方式是,YC 一直在抬高"下限"。我所说的下限是这个意思:你可能有一位新员工入职,原本也许要花六个月才能上手,但有了这套东西,他们就像是自动地从公司的运作中获取了大量上下文,并且通过与 AI 的自动"学徒制",了解到组织里最优秀的那些明星成员是怎么做事的——而不是原来那样,因为合伙人的时间很贵,或者有时组织里最优秀的人非常忙,对吧。你就得以运行一种模拟,体验一下当 Pete 出色地指导创始人做销售时是什么样,或者当 Gary 和创始人谈话、给出非常具体的建议时是什么样。我觉得这能帮助组织里所有的新加入者,更快地成为你的一个迷你版——

[31:50] **SPEAKER_02:** you a lot faster one of the first things that I appreciated about being able to use a coding agent was that all of the dumb questions I was too embarrassed to ask I had no trouble asking asking the agent and it this is kind of that same thing but at an organizational level right you're a brand new employee you're embarrassed to ask you don't want to bug hard with with a question and now you don't have to write you in which on that means a lot more questions get asked and answered and people ramp up much more quickly after

> ——快得多。能够使用编程 agent 时,我最早欣赏的一点是:所有那些我不好意思问出口的蠢问题,我都能毫无顾虑地拿去问 agent。这其实是同一回事,只不过发生在组织的层面上,对吧:你是一个刚入职的新员工,你不好意思提问,你不想拿一个问题去烦 Harge,而现在你不必这么做了。这意味着更多的问题被提出、被解答,人们上手也快得多。在——

[32:19] **SPEAKER_03:** you had built all of this agent infrastructure at YC it inspired you to write this essay horseless carriages that went like pretty viral on the internet maybe you can like explain the ideas behind horseless carriages I think

> ——你在 YC 构建了所有这些 agent 基础设施之后,它启发你写了《无马之车》(Horseless Carriages)这篇文章,在网上传播得相当广。也许你可以解释一下《无马之车》背后的理念。我觉得——

[32:31] **SPEAKER_02:** there's still very relevant now it was a critique of a lot of the the AI software that I saw being built at the time and to be totally honest I think a lot of it

> ——它到现在仍然非常有现实意义。它是对我当时看到的很多正在被构建的 AI 软件的一种批评,而且说实话,我觉得其中很多——

[32:40] **SPEAKER_00:** still falls in this still like that yeah it didn't change yes I just saw a lot of

> ——现在仍然是这个样子,还是那样,对吧,没有变。对。我当时看到很多——

[32:44] **SPEAKER_02:** examples people are doing a lot of the research and there's no end to it but it of companies building software and adding AI features by sort of slotting a little bit of AI inside of a lot of software, right? And the example that I used at the time was the kind of email writer that the Gmail team had shipped. But the real idea underneath was just kind of that the potential for AI is to shift control of software from the developer to the user, right? And the simple example I started with was basically that all of these kind of like AI as a little feature kept a bunch of prompt context about how the AI should do a job locked away and hidden from the user, which was just this classic example of like, well, it's the developer's job to figure out how all of this stuff should work. So the developer should write that and we should protect the user from that kind of complexity.

> ——例子——人们做了大量研究,而且没有尽头——但那是一些公司构建软件、添加 AI 功能的例子,做法是在一大堆软件里塞进一点点 AI,对吧?我当时用的例子是 Gmail 团队推出的那种邮件撰写功能。但底层真正的想法是:AI 的潜力在于把对软件的控制权从开发者转移到用户手中,对吧?我一开始举的那个简单例子基本上是说,所有这些"把 AI 当作一个小功能"的做法,都把关于"AI 该如何完成一项工作"的一大堆 prompt 上下文锁起来、对用户隐藏起来。这正是那个经典的例子:嗯,搞清楚这些东西该如何运作是开发者的工作,所以应该由开发者来写这些,而我们应该保护用户,让他们不必面对那种复杂性。

[33:37] **SPEAKER_00:** Safetyism, I hate it.

> 安全主义(safetyism),我讨厌它。

[33:38] **SPEAKER_02:** Right. And it's just, again, going back to this contrast between watching... the way that some of these tools work and what it was like to use a coding agent on my computer that could do anything, right?

> 对。这又一次回到了那种对比:一边看着这些工具中的某一些是怎么运作的,一边体验着在我自己电脑上使用一个几乎无所不能的编程 agent 是什么感觉,对吧?

[33:51] **SPEAKER_02:** And feeling like I had superpowers. I think the conclusion that this essay points to is that as we get better at building AI native software, it's going to look a lot more like the agent wrapping software deterministic tools rather than deterministic software wrapping in AI, right? We've done our best to expose that to internal employees with some of these primitives that we've built. But we have a long way to go.

> 那种感觉就像我拥有了超能力。我认为这篇文章指向的结论是:随着我们越来越擅长构建 AI 原生软件,它会越来越像是"由 agent 来包裹确定性的软件工具",而不是"由确定性的软件来包裹 AI",对吧?我们已经尽力通过我们构建的这些原语,把这种能力开放给内部员工。但我们还有很长的路要走。

[34:21] **SPEAKER_05:** The chat as the interface, I just feel something... There's like things going around right now about how there's a need to build a new interface for like AI and what does that look like? And I think that just comes from people who haven't like touched and felt it yet.

> 聊天作为界面(chat as the interface),我总觉得有点什么……现在有一些说法在流传,说需要为 AI 构建一种新的界面,那会是什么样子?我觉得这种说法只是来自那些还没有真正上手、亲身感受过它的人。

[34:33] **SPEAKER_05:** Chat is actually pretty good because like you trust the agent, you increasingly trust the agent to do more of the work and you trust its decisions and you don't actually need to like have too much of a UI. Right. To go in and like review the things it's doing.

> 聊天其实相当不错,因为你信任这个 agent,你越来越信任它去完成更多的工作,你信任它的决定,于是你其实并不需要太多的 UI 去介入、去审查它正在做的事情。对。

[34:46] **SPEAKER_00:** It's time for just-in-time software.

> 即时软件(just-in-time software)的时代到了。

[34:47] **SPEAKER_05:** Yeah, basically, right? Like, yes, occasionally you want it to present you like maybe like a specific view of something, but...

> 是啊,基本上就是这样,对吧?当然,偶尔你会希望它给你呈现某样东西的一个特定视图,但是……

[34:54] **SPEAKER_00:** And it could make the software and build it as a single page JavaScript just purposely built for you at that moment. Yeah. And it could be a skill file that could be like called anytime you want.

> 而它可以现场制作那个软件,把它构建成一个单页的 JavaScript,就在那一刻专门为你打造。是的。而且它可以是一个 skill 文件,任何你想要的时候都能调用。

[35:04] **SPEAKER_01:** I was thinking a lot about this because I used to be in the camp that, oh, perhaps when ChatGPT came out and it was 2023, that perhaps chat was not going to be the UI for all these AI applications. And I've definitely changed my mind. Part of it is like after experiencing all these tools and I think the more I reflect upon it, why chat is probably the better interface is because it's the closest thing to human language and human language and writing is basically the closest thing to expression of thinking. So chat is the closest stepping stone to clear intelligence.

> 我一直在琢磨这件事,因为我原来是站在另一派的:哦,也许——在 ChatGPT 刚出来的 2023 年——也许聊天并不会成为所有这些 AI 应用的界面。而我现在肯定是改变了看法。部分原因是在体验了所有这些工具之后,我越是反思,越觉得聊天大概是更好的界面,因为它最接近人类语言,而人类语言和写作基本上又是最接近思维表达的东西。所以聊天是通向清晰智能的最近的一块垫脚石。

[35:36] **SPEAKER_00:** Yeah.

> 是的。

[35:37] **SPEAKER_01:** So you can't just put it in a box. I think it just constrained us too much to have that very specific box. So that's why I thought it's like, okay, all in with chat interfaces. I used to be in the other camp and it's like.

> 所以你没法把它硬塞进一个盒子里。我觉得那个非常具体的盒子把我们限制得太死了。所以我才想:好吧,全力押注聊天界面。我以前是站在另一派的,而现在就是——

[35:49] **SPEAKER_05:** That is multimodal. I know we've talked about like Telegram is not ideal, but I actually really- It's pretty good. Yeah, it's pretty good.

> 而且它是多模态的。我知道我们聊过 Telegram 并不理想,但我其实真的挺——它相当不错。对,相当不错。

[35:55] **SPEAKER_00:** I mean, the voice memos, sometimes when I don't want to type, you just do the voice memo and it feels like I'm talking to me from you.

> 我是说那些语音备忘,有时候我不想打字,就直接发个语音备忘,那感觉就像我在跟自己说话一样。

[36:01] **SPEAKER_05:** I can give it text, I can give it voice, I can give it pictures of things, I can give it files. Like it's like pretty good.

> 我可以给它发文字,可以给它发语音,可以给它发东西的照片,可以给它发文件。真的相当不错。

[36:07] **SPEAKER_00:** Yeah, I just experienced this. So like January, I think the last episode we did, I just talked about this. Like I spent January through February building a half a million lines of code for a Rails app, which was Gary's list. And it was like, you know, I know people make fun of me for like, it was a blog, but it was like, I built the blog in like the first week. Like I spent a month and a half building a full agentic framework that did like my own version of deep research and like fact checking.

> 是的,我刚刚就经历了这个。大概在一月份,我想我们上一期节目我就聊过这个。我从一月一直到二月,给一个 Rails 应用写了五十万行代码,那就是 Gary's List。你知道,我知道有人拿我打趣说那不就是个博客嘛,但其实我第一周就把博客部分做完了。我花了一个半月构建了一整套 agentic 框架,做了我自己版本的深度研究和事实核查。

[36:35] **SPEAKER_00:** But the thing is I built it the way I would have built software in 2013, the last time I wrote code. It was like the web 2.0 version of this. And Cloud Code lets you do that. And what's crazy to connect is like, I'm working like, I don't know, I think I wrote like 40,000 lines of code the last three days just for G-Brain.

> 但问题是,我是用我在 2013 年——也就是我上一次写代码时——会用的方式来构建它的。那像是这套东西的 Web 2.0 版本。而 Claude Code 让你能这么做。而联系起来看很疯狂的一点是,我现在——我也说不好——我觉得过去三天光是为 G-Brain 我就写了大概四万行代码。

[36:54] **SPEAKER_00:** And G-Brain is basically Gary's list 2.0, but it's totally open source, right? So everything I had to write for agentic retrieval, everything I had to do for voice extraction, everything I had to do for fact checking, all of that now exists inside G-Brain. And I just gave it to my Gary's list team yesterday as their own OpenClaw instance. And they're flying now, right?

> 而 G-Brain 基本上就是 Gary's List 2.0,只不过它是完全开源的,对吧?所以我为 agentic 检索所写的一切,为语音提取所做的一切,为事实核查所做的一切,现在全都存在于 G-Brain 里。我昨天刚把它作为他们自己的 OpenClaw 实例交给了我的 Gary's List 团队。而他们现在飞起来了,对吧?

[37:19] **SPEAKER_00:** Like they were complaining about like, I had made this monolithic writer chat interface and it was like full of bugs because I was like re-implementing things that OpenClaw and Telegram already do. And now they just use OpenClaw, Telegram and my retrieval system with like all the same data that I extracted it out and with our MCP. And it's working great. Like basically, you know, Gary's list 2.0, the next rewrite, thankfully, is not half a million lines of Rails code that is like insane to actually, you know, it's rigid.

> 他们本来一直在抱怨,说我做的那个单体式的写作聊天界面到处都是 bug——因为我等于是在重新实现 OpenClaw 和 Telegram 本来就已经做了的功能。而现在他们只需用 OpenClaw、Telegram 加上我的检索系统,配上我抽取出来的那同一批数据,再加上我们的 MCP。它运行得好极了。基本上,你知道,谢天谢地,Gary's List 2.0——也就是下一次重写——不再是五十万行 Rails 代码那种真的很离谱的东西,你知道,那玩意儿太僵硬了。

[37:52] **SPEAKER_00:** It takes a long time. It like takes like 10 times longer, you know, even though it was one 100th the amount of time to do it like by hand, you don't have to do it by hand. Like that half a million lines of code in Rails is easily like 10,000 lines of like TypeScript and like maybe 2000 lines of Markdown. And all of that is way more dynamic. Like you could just say like, actually, for the second paragraph, I really like including a biography of like the politician we're focusing on.

> 它花的时间很长。要多花大概 10 倍的时间,你知道,即便相比手写只用了百分之一的时间——你根本不必手写。那五十万行 Rails 代码,轻轻松松就能用大约一万行 TypeScript 加上也许两千行 Markdown 来实现。而这一切要动态得多。比如你可以直接说:其实呢,在第二段里,我很想加入我们正在关注的那位政客的一段简介。

[38:22] **SPEAKER_00:** And it's like, I don't have to code that in Rails. I don't even have to write that into a Ruby file that then gets evaled in like, you know, my complex eval infrastructure. Like OpenClaw just knows that and I have an eval skill. My editor-in-chief can just change it on the fly and I didn't touch it. And it's like, this is insane, actually.

> 而这意味着,我不必在 Rails 里把它编码进去。我甚至不必把它写进一个 Ruby 文件、再让它在我那套复杂的评估(eval)基础设施里被求值。OpenClaw 就是知道该怎么做,而我有一个评估 skill。我的主编可以直接现场改动它,而我根本没碰过它。这真的,太疯狂了。

[38:43] **SPEAKER_00:** This is actually the dawn of just-in-time software, and I can see it right now.

> 这其实就是即时软件时代的黎明,而我现在就能亲眼看到它。

[38:46] **SPEAKER_02:** The best AI software that I've used, whether it's inside of YC or tools that others have built, tend to be very small and just add kind of the smallest amount of code ahead of time that you need in order to let the model shine. And you can build an awful lot with that, right? I can write tens of thousands of lines of code, like you're saying. But the ability to start at this extremely simple thing that I need to understand very little in order to use is incredibly powerful, and I think most software in the future is

> 我用过的最好的 AI 软件,无论是 YC 内部的,还是别人构建的工具,往往都非常小巧,只在事先加入那么一丁点为了让模型大放异彩所需要的代码。而你能用这一点点东西构建出海量的成果,对吧?我可以写几万行代码,就像你说的那样。但那种能够从一个极其简单、我几乎不需要理解就能上手使用的东西开始的能力,是极其强大的。我认为未来大多数软件——

[39:23] **SPEAKER_05:** going to look like that. We were talking about this earlier, but I think that is what OpenCore did really well. There were a few things that you wanted. You wanted some ability to give it a bit of personality. You wanted it to persist and last for a long time and have some concept of memory.

> ——都会是这个样子。我们之前聊过这个,但我觉得这正是 OpenCore 做得特别好的地方。有那么几样你想要的东西:你想要某种能力,给它注入一点个性;你想要它能持续存在、维持很长时间,并且有某种记忆的概念。

[39:36] **SPEAKER_05:** It's not perfect. But... That's actually good enough for that use case.

> 它并不完美。但是……对那个使用场景来说,这其实已经足够好了。

[39:41] **SPEAKER_03:** Cloud code, too. Every time Boris comes and speaks at YC, he spoke with Diana earlier this week. One of the things that really stands out is how obsessed he is with simplicity and with just making the product as small as possible.

> Claude Code 也是。每次 Boris 来 YC 演讲——他本周早些时候和 Diana 聊过——真正让人印象深刻的一点,是他对简洁的痴迷,以及把产品做到尽可能小的执念。

[39:55] **SPEAKER_02:** My favorite example of this is this open-source harness called Pi, which is a project... That's what OpenCore uses as an out-of-the-box coding agent. It's this beautiful piece of software, which is just the smallest possible coding agent.

> 我最喜欢的例子是一个叫 Pi 的开源 harness,这是一个项目……那正是 OpenCore 拿来作为开箱即用的编程 agent 的东西。它是一件优美的软件,就是一个尽可能小的编程 agent。

[40:09] **SPEAKER_02:** You can use Pi to modify and extend Pi, right? And it's this kind of idea of self-extending and self-referential software. It's really fascinating. And you're right. OpenCore was built on top of that.

> 你可以用 Pi 来修改和扩展 Pi 本身,对吧?这是一种自我扩展、自我指涉的软件理念。真的非常引人入胜。而你说得对,OpenCore 就是建立在它之上的。

[40:20] **SPEAKER_02:** One of the things I'm very curious to see is how many other pieces of classic software emerge in this form as this kind of minimal thing that you start with and then use an agent to extend over time. I think more and more... I mean, looking at, honestly, the benefits that we've gotten from having our own customizable software, I suspect that a lot of commercial software will come with this capability out of the box in the future.

> 我非常好奇想看到的一件事是:将会有多少其他经典软件以这种形态出现——作为一个你从中起步的极简东西,然后随时间用一个 agent 去逐步扩展它。我觉得会越来越多……说实话,看看我们从拥有自己可定制软件中获得的好处,我怀疑未来很多商业软件都会开箱即带这种能力。

[40:45] **SPEAKER_00:** There's a really interesting subtle thing that I wanted to talk about around what I learned from your essay, which is AI can either be centralizing or decentralizing. And the Google, Gmail, I can't change the prompt thing is the perfect example of that. We basically have a choice to be made over the next...

> 有一件非常有意思、也很微妙的事情,我想聊聊,是我从你那篇文章里学到的:AI 既可以是中心化的,也可以是去中心化的。而 Google、Gmail 那个"我改不了 prompt"的例子,正是中心化的完美写照。我们基本上要在接下来的——

[41:04] **SPEAKER_00:** I don't think it's even that long. I think it's 18 to 24 months. It might take a while. It might take five years, but there are sort of two scenarios. And what comes to mind is literally the 1984 Macintosh commercial by Apple, where it's like, is 2034 going to be like 1984?

> 我觉得甚至用不了那么久。我认为是 18 到 24 个月。它可能需要一段时间,可能要五年,但大致有两种情景。而我脑海里浮现的,正是苹果 1984 年那支麦金塔广告——问题是:2034 年会变得像《1984》里那样吗?

[41:23] **SPEAKER_00:** And the 1984 case would be, we have centralized control, there are five kings, there's only... One of them maybe wins. They have the most advanced AI.

> 而"《1984》式"的情景会是:我们处于中心化的控制之下,有五个"国王",而最终只有……其中或许一个胜出。他们掌握着最先进的 AI。

[41:33] **SPEAKER_00:** They have end run around all compute and power. They have all the space data centers, because you can't build any terrestrial data centers in America anyway. There's this centralization of control. And not only that, they don't let you run your own prompts. They literally do the Gmail thing, but for your whole computing existence, right?

> 他们绕开一切、垄断了所有的算力和电力。他们拥有所有的太空数据中心,因为反正在美国你也没法在地面上建任何数据中心。存在着这样一种控制权的中心化。不仅如此,他们还不让你运行你自己的 prompt。他们真的就是把 Gmail 那套做法,套用到你整个计算生活的方方面面,对吧?

[41:55] **SPEAKER_00:** And this would be as if personal computers never existed and there were only mainframes and mini computers. This is sort of lost to the sands of time, but in the 1960s and 70s, when computers first came out... You couldn't go to the store like you can today.

> 这就好像个人电脑从未存在过,世界上只有大型机和小型机。这段历史多少已经湮没在时间的沙尘里了,但在 1960 和 70 年代,当计算机刚出现时,你没法像今天这样走进商店。

[42:09] **SPEAKER_00:** You couldn't go to an Apple store and just buy an iPhone, let alone a Mac. You had to get access to this thing that was worth hundreds of thousands of dollars to millions of dollars.

> 你没法走进一家苹果商店就买一部 iPhone,更别说买一台 Mac 了。你必须设法去接触那种价值几十万乃至数百万美元的东西。

[42:22] **SPEAKER_03:** And the only... And it was tightly locked down by corporate policies, you're right. And the thing that really spurred the computing revolution was when people started having personal computers that they could experiment on.

> 而且唯一的……它还被企业的各种政策牢牢锁死,你说得对。而真正点燃计算革命的,是当人们开始拥有可以自己拿来做实验的个人电脑的时候。

[42:33] **SPEAKER_00:** Yeah. And just like the priesthood, right? There was a small priesthood. There was a small priesthood and an institutional base that controlled capital, literally the means of production. And so this is like a coherent future that we could live in that I don't want to live in.

> 是的。就像一个"祭司阶层",对吧?存在一个小小的祭司阶层。有一个小小的祭司阶层和一个掌控着资本——字面意义上的生产资料——的建制基础。所以这是一个我们可能会置身其中、而我并不想生活于其中的、自洽的未来。

[42:49] **SPEAKER_00:** And the alternative to that is actually embedded in the homebrew computer club. It's embedded in the revolution that Steve Jobs and Steve Wozniak gave us when they were in the garage in Mountain View, literally soldering together breadboards and like sold 500 of these Apple ones. Yeah. So we're at the Apple one moment right now. We are coming up with the primitives.

> 而它的另一种可能,其实就蕴含在自制电脑俱乐部(Homebrew Computer Club)里。它蕴含在 Steve Jobs 和 Steve Wozniak 当年在山景城车库里——真的用烙铁把面包板焊在一起、卖出 500 台 Apple I——所带给我们的那场革命里。是的。所以我们现在正处于"Apple I 时刻"。我们正在发明那些基本原语。

[43:09] **SPEAKER_00:** We're learning how do these things work and how do we sell it and how do we package it? But then there's like a lot of choices right now, right? Like most people, the mass, you know, a billion users use ChatGPT and ChatGPT like gives you a little access, but MCP is really locked down. You actually, you know, can't hook things up to your own databases that easily. And, you know, for what?

> 我们在摸索:这些东西是怎么运作的?我们该怎么把它卖出去?怎么把它打包?但现在其实有很多选择,对吧?大多数人、大众——你知道,十亿用户都在用 ChatGPT——ChatGPT 给你开放了一点点权限,但 MCP 被锁得很死。你其实没法那么容易地把东西接到你自己的数据库上。而这,你知道,是为了什么呢?

[43:35] **SPEAKER_00:** Safety, like I would argue Claude is like a little bit more open, but not really. Perplexity Computer is probably the best version of it, but it's still like, you know, pretty limited compared to what you could do with OpenClaw and Hermes Agent. And so what does the revolution look like that is like the true personal AI moment? And that's what I hope that we are building with things like G-Brain and, you know, Hermes Agent and OpenClaw. Like the ability to run your own.

> 为了安全。我会说 Claude 稍微开放一点,但也没开放到哪去。Perplexity Computer 大概是这方面最好的版本,但相比你用 OpenClaw 和 Hermes Agent 能做到的,它仍然,你知道,相当受限。那么,那场真正意义上的"个人 AI 时刻"的革命,会是什么样子?这正是我希望我们通过 G-Brain、Hermes Agent、OpenClaw 这些东西所要构建的。也就是运行你自己的——

[44:04] **SPEAKER_00:** Software to change your own prompts, to test all of it, to have your own private repo that like, you know, is only yours to be able to choose which model to use. And maybe it's an open weight model. Like to me, that's sort of the white pill for AI is we could have corporate control, no control of your own prompts and like literally the AI happens to you, you know, you're under the API line or like there's this other alternative where. I want like a billion people to actually control and program for themselves. What are these things?

> ——软件的能力,更改你自己的 prompt,把它全部测试一遍,拥有你自己的私有代码仓库——你知道,那是只属于你的——能够选择使用哪个模型。也许那是一个开放权重(open weight)的模型。对我来说,这算是 AI 的"白色药丸"(white pill,乐观愿景):我们可能会走向企业控制的那种局面,你无法掌控自己的 prompt,AI 字面意义上是"发生在你身上"的,你被压在 API 那条线之下;又或者存在另一种可能——我希望有大约十亿人能够真正为自己掌控、为自己编程,去定义这些东西到底是什么。

[44:42] **SPEAKER_00:** This should be an extension of yourself and what you care about, not what, you know, meta or alphabet or even opening our anthropic care about.

> 它应该是你自身、以及你所关心之事的延伸,而不是 Meta、Alphabet,乃至 OpenAI 或 Anthropic 所关心之事的延伸。

[44:51] **SPEAKER_02:** I always really bristle when I see AI framed as a way to replace people because it just doesn't match the way that I have experienced it in the way that so many of the people around me have experienced it. Not as a replacement. Not for humans, but as a thing that empowers. If you look at, at, at kind of how tech has developed since the era of, of mainframes to PCs, to the internet, which gave everyone like a publishing platform, like it's, it's a story overall above all of individual empowerment. And I think AI is going to play out the same way.

> 每当我看到 AI 被描述成一种取代人的手段,我都会感到强烈的抵触,因为这根本不符合我亲身体验它的方式,也不符合我身边那么多人体验它的方式。它不是一种替代品——不是对人类的替代,而是一种赋能的东西。如果你回顾科技从大型机时代到 PC、再到给每个人一个发布平台的互联网是如何发展的,你会发现,这归根结底、首先是一个关于个体赋能的故事。而我认为 AI 也会以同样的方式展开。

[45:22] **SPEAKER_02:** I think it is going to enable us to do more than we could before. I think it's going to eliminate kind of the drudgery style work that like made a lot of my job painful in the past.

> 我认为它会让我们能够做到比以前更多的事情。我认为它会消除掉那种苦役式的工作——过去正是这类工作让我的工作中很大一部分变得痛苦。

[45:33] **SPEAKER_00:** To me, it's like. To make choices to do so by default, like a company is not open by default. A company is a command and control by default. Maybe the leadership gets access to these tools, but like the, you know, line level people, the staff people don't right. And like you, we need like a radically different type of organization and we need to actually offer computing in a different way.

> 对我来说,这就是——要主动做出选择,让它默认如此,因为一家公司默认并不是开放的。一家公司默认是命令与控制式(command and control)的。也许领导层能用上这些工具,但一线的、基层的员工用不上,对吧。而我们需要一种截然不同的组织类型,我们需要真正以一种不同的方式来提供计算能力。

[45:56] **SPEAKER_00:** And these are all choices and the people who are watching are going to be the people who build all these things in society. So. We better choose well, well, that's all the time we have for today. I mean, I think we covered some pretty heavy stuff, but Pete, thanks for joining us. Thanks.

> 而这些全都是选择,正在观看这期节目的人,将会是那些在社会上构建所有这些东西的人。所以,我们最好选对了。好,今天的时间就到这里了。我是说,我觉得我们聊了一些相当有分量的话题,不过,Pete,谢谢你来参加我们的节目。谢谢。

[46:13] **SPEAKER_00:** Thank you. Thank you. Thanks for watching guys. We'll see you guys on the next one.

> 谢谢。谢谢。谢谢大家的观看。我们下期再见。
