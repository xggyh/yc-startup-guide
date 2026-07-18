# 全文转录 · 从零开始用 AI 搭建一家公司

> ▶ [YouTube](https://www.youtube.com/watch?v=EN7frwQIbKc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/EN7frwQIbKc.md) &nbsp;·&nbsp; How To Build A Company With AI From The Ground Up

> 中英对照 · 每段英文原文下附中文翻译

[00:09] I'm Diana, and I'm a partner at YC. Over the past few months, it's become clear to me that AI is not just going to change how quickly software gets built or what workflows get automated. It's going to fundamentally change the way startups should be run, from what roles will exist to what products are possible to build. In this episode, I'm going to discuss how founders should think about building an AI native company, what roles their team should have, and what concrete internal practices they can adopt right now to move much faster.

> 我是 Diana,YC 的合伙人。过去几个月里,我越来越清楚地认识到,AI 改变的不只是软件构建的速度或哪些工作流程会被自动化。它将从根本上改变创业公司的运营方式——从会存在哪些岗位,到能够构建出哪些产品。在这一期节目里,我将探讨创始人应如何思考打造一家 AI 原生公司,团队应该设置哪些角色,以及他们现在就可以采用哪些具体的内部实践,从而大幅提速。

[00:40] Currently, most people talk about AI in terms of productivity. They'll talk at length about how it can make engineers more productive, or say we need to add co-pilots to existing workflows and ship more features. This framing misses the shift we're currently seeing, which is less about productivity boosts than entirely new capabilities. The right person with AI tools can now build features that used to require an entire team, or, were just impossible. Thinking about AI in terms of new capabilities has several implications for how founders should run their companies.

> 目前,大多数人谈论 AI 时都是从生产力的角度出发。他们会长篇大论地讲 AI 如何让工程师更高效,或者说我们需要给现有工作流加上副驾驶(co-pilot)、多交付一些功能。这种框架忽略了我们当下正在见证的转变——它与其说是生产力的提升,不如说是全新能力的诞生。如今,合适的人配上 AI 工具,就能构建过去需要一整个团队才能完成、甚至根本无法实现的功能。以新能力的视角看待 AI,对创始人应如何经营公司有着多方面的启示。

[01:15] At a high level, the way to think about AI is that it should not be a tool your company just uses. It should be the operating system your company runs on. Every workflow, every decision, and every process should flow through an intelligent layer that is constantly learning and improving. What this means concretely is every important process in your company should be captured by an intelligent closed loop. A closed loop captures information, feeds it back into an intelligent system, and improves the process over time.

> 从宏观上讲,思考 AI 的正确方式是:它不应只是公司使用的一个工具,而应成为公司赖以运行的操作系统。每一个工作流、每一个决策、每一个流程,都应流经一个不断学习和改进的智能层。具体来说,这意味着公司里每一个重要流程都应被一个智能的闭环所捕获。闭环会采集信息,将其反馈回智能系统,并随时间推移不断改进该流程。

[01:47] If you've ever studied controlled systems, you'll be familiar with the difference between an open loop and a closed loop system. Open loops are controlled systems without feedback loops. In the old world, companies basically ran as open loops. You made a decision, executed it, and didn't always systematically measure the outcome and adjust the process. Open loops are inherently lossy. A closed loop, on the other hand, is self-regulating. It continuously monitors its output and adjusts its process to better meet the stated goal. Closed loops are extremely powerful for correctness and stability. With self-improving agents, your company should run as a closed loop.

> 如果你学过控制系统,就会熟悉开环系统和闭环系统的区别。开环是没有反馈回路的控制系统。在过去的世界里,公司基本上都是以开环方式运作的:你做出一个决策,执行它,却并不总是系统性地衡量结果并调整流程。开环本质上是有损耗的。相反,闭环是自我调节的。它持续监测自己的输出,并调整流程以更好地达成既定目标。闭环在保证正确性和稳定性方面极其强大。有了能自我改进的智能体,你的公司就应当以闭环方式运行。

[02:26] To build these closed loops, you will need to make your entire company queryable. In other words, the whole organization should be legible to AI. Every important action should be legible to AI. Every action should produce an artifact that the intelligence at the center of the company can learn from and use to self-improve. This means recording your meetings with an AI note-taker, minimizing DMs and emails, and embedding agents throughout communication of all channels. It also means building custom dashboards with everything in the company. Revenue, sales, engineering, hiring, ops, everything.

> 要构建这些闭环,你需要让整个公司变得可查询。换句话说,整个组织都应对 AI 可读。每一个重要行动都应对 AI 可读。每一个行动都应产出一份产物(artifact),供公司中枢的智能从中学习并用以自我改进。这意味着用 AI 记录员记录会议,尽量减少私信和邮件,并在所有沟通渠道中嵌入智能体。它还意味着为公司里的一切构建定制化仪表盘——营收、销售、工程、招聘、运营,方方面面。

[03:00] Here's a concrete example of how it could work. Take engineering, management, and sprint planning. If you have an agent that has access to your linear tickets, all your Slack engineering channels, all customer feedback from emails or tools like Pylon and GitHub, high-level plans in a Notion or Google Doc, sales calls and recordings from daily stand-ups, then the agent can analyze what was actually shipped in your previous sprint and how well they met customers' needs for real.

> 这里有一个它如何运作的具体例子。以工程、管理和冲刺(sprint)规划为例。如果你有一个智能体,能够访问你的 Linear 工单、所有 Slack 工程频道、来自邮件或 Pylon、GitHub 等工具的全部客户反馈、Notion 或 Google 文档里的高层规划、以及销售通话和每日站会的录音,那么这个智能体就能分析上一个冲刺实际交付了什么,以及它们究竟在多大程度上真正满足了客户的需求。

[03:29] From there, you can go a step further. With full visibility into what shipped, what worked, and what didn't, agents can start looking ahead. They can propose sprint plans for engineers that are way more predictable and accurate and on track. The days of eng-manager status roll-ups that are super lossy are gone. Having managed engineering teams myself, and now seeing this across multiple YC companies, this is a game changer. What used to require constant coordination becomes legible and queryable by default. I've seen teams that do this cut their engineering sprint time in half and get close to 10x more than in that time.

> 在此基础上,你还能更进一步。有了对已交付内容、哪些有效、哪些无效的全面可见性,智能体就可以开始展望未来。它们能为工程师提出更可预测、更准确、更贴合进度的冲刺规划。工程经理那种损耗极大的状态汇总时代已经一去不复返了。我自己带过工程团队,如今又在多家 YC 公司看到这一点,这是彻底的变革。过去需要持续协调才能完成的事情,如今默认就变得可读、可查询。我见过采用这种做法的团队把工程冲刺时间缩短了一半,并在同样的时间里做到接近 10 倍的产出。

[04:09] The overarching principle here is that to get their full capabilities, you need to provide models with as much context as you would provide an employee. When you do this, your company stops operating as an open loop, where information is fragmented and manually interpreted. It becomes instead a closed-loop system. Status, decisions, and outcomes are continuously captured and fed back into this intelligence layer. The result is a system that always has to work. This has an up-to-date view of what's actually happening.

> 这里的总体原则是:要充分发挥模型的全部能力,你需要像给员工提供上下文那样,给模型提供同样多的上下文。当你这样做时,你的公司就不再以开环方式运作——那种信息碎片化、需要人工解读的状态。它转而变成一个闭环系统。状态、决策和结果被持续捕获,并反馈回这个智能层。其结果是一个始终必须运转的系统,它对实际正在发生的事情保有最新的全貌。

[04:39] There's also a new paradigm emerging for how the highest velocity companies build product. AI software factories. If you're familiar with the test-driven development, or TDD, this is the next evolution of that. With software factories, humans write a spec and a set of tests that define success. And then AI agents generate the implementation code and iterate until the tests pass. The human defines what to build and judges the output. The actual code is the agent's job. Some companies have already pushed this to the point where their repos contain no handwritten code, just specs and test harnesses.

> 关于速度最快的公司如何构建产品,还有一种新范式正在兴起:AI 软件工厂。如果你熟悉测试驱动开发(TDD),这就是它的下一步演进。在软件工厂里,人类编写一份规格说明(spec)和一组用于定义成功标准的测试。然后由 AI 智能体生成实现代码,并不断迭代直到测试通过。人类负责定义要构建什么并评判输出结果,真正的代码则是智能体的工作。有些公司已经把这一点推进到了这样的程度:他们的代码仓库里没有任何手写代码,只有规格说明和测试框架。

[05:24] StrongDM's AI team is an example of how to do this. Their end goal was a system that essentially eliminated the need for a human to write or review code. And so they built their own software factory where specs and scenario-based rules and validations, drive agents to write, test and iterate on code until it meets a probablistic satisfaction threshold. And it works. This is how you achieve the thousand x engineer that Steve Yege talks about by surrounding a single engineer with a system of agents that enable them to build things they would've never been able to build before. The era of the thousand or the century pushes fighting. or even 10,000 ex-engineer is here.

> StrongDM 的 AI 团队就是一个如何做到这一点的例子。他们的最终目标是打造一个系统,基本上消除人类编写或审查代码的需要。于是他们构建了自己的软件工厂,由规格说明、基于场景的规则和校验驱动智能体去编写、测试并迭代代码,直到达到某个概率化的满意度阈值。而且它确实奏效。这正是你实现 Steve Yegge 所说的「千倍工程师」的方式——用一套智能体系统环绕单个工程师,使其能够构建以前根本无法构建的东西。千倍、乃至一万倍工程师的时代已经到来。

[06:01] One implication of building your company this way with AI loops everywhere, a queryable organization and software factories is that the classic management hierarchy no longer makes sense. In the old world, you needed middle managers and coordinators to route information inefficiently up and down an organization. In the new world, the intelligence layer serves that purpose. If your company is queryable, artifact-rich, and legible to an AI, you should have almost no human middleware. This matters because your company's velocities is only as fast as its information flow. Every layer of human routing you can remove is the direct speed gain.

> 以这种方式构建公司——处处都是 AI 闭环、组织可查询、拥有软件工厂——所带来的一个影响是:传统的管理层级不再有意义。在旧世界里,你需要中层管理者和协调者在组织里低效地上下传递信息。在新世界里,智能层承担了这个职能。如果你的公司可查询、产物丰富、且对 AI 可读,那么你几乎不需要任何人类中间件。这一点很重要,因为公司的速度取决于其信息流动的速度。你每去掉一层人为的信息中转,就是一次直接的提速。

[06:52] A great example is what Jack Dorsey is doing over at Block. After going deep on the tools, he's come to the same conclusion many have. This is about more than just incremental productivity gains. His view is that if you keep the same org chart and management structure, you'd miss the shift entirely. The company itself has to be rebuilt as an intelligence layer, with humans at the edge guiding it rather than routing information through it. Going forward, Jack suggests every company will have three employee archetypes.

> 一个绝佳的例子是 Jack Dorsey 在 Block 所做的事。在深入研究这些工具之后,他得出了和许多人相同的结论:这远不只是渐进式的生产力提升。他的观点是,如果你保持相同的组织架构和管理结构,就会彻底错过这场转变。公司本身必须被重建为一个智能层,人类处于边缘去引导它,而不是让信息穿过人类来中转。展望未来,Jack 认为每家公司都将拥有三种员工原型。

[07:19] The first is the individual contributor, or IC, basically the builder operator. This is someone who directly makes and runs things. In an AI-native company, this is not limited to engineers. Everyone builds. Eng, ops, support, sales. Everyone comes to meetings with working prototypes, not pitch techs. Second is the DRI, the directly responsible individual, focused on strategy and customer outcomes. This is not a classic manager. It's the person with a clear responsibility for the result. One person, one outcome, no hiding.

> 第一种是个人贡献者(IC),基本上就是「构建者兼运营者」。这是直接动手做东西、并让它跑起来的人。在 AI 原生公司里,这不限于工程师。人人都在构建——工程、运营、客服、销售。每个人开会时带来的是可运行的原型,而不是演示 PPT。第二种是 DRI,即直接责任人,专注于战略和客户成果。这不是传统意义上的经理,而是对结果负有明确责任的人。一个人,一个成果,无处推诿。

[07:59] The third is the AI. Founder type. This person still builds, still coaches, and leads by example. If you're the founder, this needs to be you at the forefront, showing your team what massive capability gains look like, not delegating your AI strategy to someone else. With this structure, companies will be able to get outsized results with much smaller teams. Maximizing token usage, not headcount, will be the critical shift. The best companies will be the ones that are token maxing.

> 第三种是「AI 创始人型」。这样的人依然亲自构建、依然亲自指导,并以身作则地带领团队。如果你是创始人,那么站在最前沿的必须是你本人,向团队展示能力的巨大跃升是什么样子,而不是把你的 AI 战略外包给别人。有了这种结构,公司就能以小得多的团队取得超乎寻常的成果。关键的转变将是最大化 token 用量,而非最大化人头数。最优秀的公司将是那些「token 拉满」的公司。

[08:30] Think of the trend. The trade-off this way. One person with AI tools can be the equivalent of what used to take a large engineering team at a pre-AI company. That means dramatically leaner engineering, design, HR, and admin teams. And so you should be willing to run an uncomfortably high API bill because it's replacing what would have taken a far more expensive and inflated headcount.

> 这样来看这个趋势和其中的取舍。一个人配上 AI 工具,就能顶得上前 AI 时代一家公司里一整支庞大工程团队的产出。这意味着工程、设计、人力资源和行政团队都可以大幅精简。因此,你应该愿意承担一笔高得让人不太舒服的 API 账单,因为它所替代的,是本来需要花费更昂贵、更臃肿的人力成本才能完成的工作。

[08:55] But don't just take my word for any of this. You cannot outsource. It's your conviction on the power of these tools. You need to develop it yourself by actually sitting with coding agents and using them until you start to break your own priors about what is now possible to build. If you are an early stage founder, you have a huge advantage in getting ahead on this. You don't have legacy systems, entrench org charts, or thousands of people to retrain. You are small enough to build your company right from day one.

> 但不要仅仅听我一面之词。你对这些工具威力的信念,是无法外包的。你需要亲自去培养这种信念——真正坐下来使用编码智能体,一直用到你开始打破自己对「如今能构建什么」的旧有成见为止。如果你是早期阶段的创始人,你在抢占先机上拥有巨大优势。你没有遗留系统,没有根深蒂固的组织架构图,也没有成千上万需要再培训的员工。你足够小,从第一天起就可以把公司建对。

[09:26] The opposite is the case for existing companies. They have to maintain. And grow. a live product while unwinding years of standard operating procedures and core assumptions about how software gets built some companies can achieve this by spinning up small internal skunk work teams that can build ai native systems from scratch separate from the core business mutiny is a great example of this but for most every change to their core processes risk breaking something that already works so by their nature these large companies will have a much harder time going ai native startups don't have that constraint and that's a major edge to take advantage of you can design your systems workflows and culture around ai from the start and as a result operate thousand times faster than the incumbents

> 对现有公司来说情况恰恰相反。它们必须一边维护并发展一款正在运行的产品,一边拆解多年来形成的标准操作流程以及关于软件如何构建的核心假设。有些公司可以通过组建小型内部「臭鼬工厂」团队来实现这一点——这些团队独立于核心业务,从零开始构建 AI 原生系统;Mutiny 就是一个很好的例子。但对大多数公司而言,对核心流程的每一次改动都有可能破坏某些已经运转良好的东西。因此,就其本质而言,这些大公司要转向 AI 原生会困难得多。而创业公司没有这种束缚,这正是值得充分利用的重大优势。你可以从一开始就围绕 AI 来设计你的系统、工作流程和文化,并因此比那些老牌企业运转快上一千倍。
