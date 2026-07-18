# 全文转录 · 20X 公司:用内部自动化打赢体量大你 20 倍的对手

> ▶ [YouTube](https://www.youtube.com/watch?v=rWUWfj_PqmM) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/rWUWfj_PqmM.md) &nbsp;·&nbsp; The New Way To Build A Startup

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** If you haven't tried Claude Code in the last month, it's time to give it another shot. And if you have, you know what I'm talking about. It feels like AGI is here. One of Anthropic's own engineers writes, Claude wrote ClaudeCowork. Us humans meet in person to discuss foundational architecture and product decisions, but all of us devs manage anywhere between three and eight Claude instances, implementing features, fixing bugs, or researching potential solutions.

> 如果你在过去一个月里还没试过 Claude Code,那是时候再给它一次机会了。如果你已经用过,你就明白我在说什么。感觉 AGI 已经到来了。Anthropic 自己的一位工程师写道:Claude 写出了 ClaudeCowork。我们这些人类会面对面开会,讨论底层架构和产品决策,但我们所有开发者每个人都管理着三到八个 Claude 实例,让它们去实现功能、修复漏洞,或者研究潜在的解决方案。

[00:30] **SPEAKER_02:** Think about what that means. The team developing one of the most sophisticated AI products in the world, something many of you probably use every day, is using this AI internally to improve their product. I think this points to a fundamental shift in how startups operate.

> 想想这意味着什么。这个正在开发全世界最尖端 AI 产品之一的团队——很多人可能每天都在使用它的产品——正在内部使用这款 AI 来改进他们自己的产品。我认为这预示着创业公司运作方式的一次根本性转变。

[00:49] **SPEAKER_02:** Right now, the best teams aren't automating one or two internal functions. They're automating. They're automating all of them. Often they're tiny teams able to beat huge incumbents thanks to internal automation. Their leanness is their superpower. I've been calling these startups 20X companies.

> 如今,最优秀的团队不是只把一两个内部职能自动化。他们在把全部职能都自动化。这些往往是很小的团队,却凭借内部自动化打败了庞大的行业巨头。精简就是他们的超能力。我一直把这些创业公司称为"20X 公司"。

[01:14] **SPEAKER_02:** Several years ago, my friend Parker Conrad, founder of Rippling and Zenefits, coined the term compound startup to describe companies that build multiple integrated products in parallel rather than focusing narrowly on one thing.

> 几年前,我的朋友 Parker Conrad——Rippling 和 Zenefits 的创始人——提出了"复合型创业公司"(compound startup)这个说法,用来形容那些并行打造多个相互集成的产品、而不是狭隘地只专注于一件事的公司。

[01:30] **SPEAKER_04:** The theory of like the compound software business is that there's this island of product market fit that's kind of over the edge of the horizon line that's sort of harder to get to. But if you can build, you know, multiple parallel applications at once, you can get there and it actually ends up being a much more powerful type of product market fit that's much harder to displace at that point.

> 复合型软件业务的理论是这样的:存在一座"产品市场契合度"的岛屿,它就在地平线的另一侧,相对更难抵达。但如果你能够同时打造多个并行的应用,你就能到达那里,而它最终会成为一种强大得多的产品市场契合度,到那时也就更难被别人取代了。

[01:55] **SPEAKER_02:** The 20X company could be an evolution of Parker's idea, but applied to internal automation. Instead of just narrowly automating a few things like writing code or handling customer support, 20X companies build automations across all internal features. Code, support, marketing, sales, hiring, QA, and more. This makes each of their employees orders of magnitude more powerful than they would be otherwise.

> 20X 公司可以看作是 Parker 这个理念的一种演进,但被应用到了内部自动化上。20X 公司不是只狭隘地把写代码或处理客服等少数几件事自动化,而是在所有内部职能上都构建自动化——代码、客服、市场、销售、招聘、质量保证等等。这让他们的每一名员工都比原本强大好几个数量级。

[02:24] **SPEAKER_02:** It also allows them to postpone hiring additional sales and ops staff. For much... much longer, keeping payroll down and culture from drifting. The phrase 20X company was actually coined by the founders of GigaML, which builds voice-based customer service agents for enterprise to describe how they managed to close DoorDash as a customer going up against incumbents that were literally 20X as large.

> 这也让他们能够把招募更多销售和运营人员的时间往后推——推迟很久很久,从而压低薪资支出,并防止公司文化跑偏。"20X 公司"这个说法其实是 GigaML 的创始人们提出的。GigaML 为企业打造基于语音的客服智能体,他们用这个词来形容自己是如何拿下 DoorDash 这个客户的——他们面对的竞争对手规模足足是他们的 20 倍。

[02:51] **SPEAKER_00:** When we got DoorDash as a customer, we were approximately like four to five engineers going against players who had like 100X engineers. So we kind of like coined the term like, hey, we are a 20X company. We are a 20X company because we are able to beat these much bigger players who are like 20X us by having a better product and better numbers.

> 当我们拿下 DoorDash 这个客户时,我们大概只有四五个工程师,却在跟那些工程师数量是我们 100 倍的对手竞争。所以我们就造了这么个说法:嘿,我们是一家 20X 公司。我们之所以是 20X 公司,是因为我们能凭借更好的产品和更好的数据,打败那些规模是我们 20 倍的更大玩家。

[03:08] **SPEAKER_02:** Giga was able to close DoorDash and several other Fortune 500 companies as customers because of a powerful internal agent they call Atlas.

> Giga 之所以能拿下 DoorDash 以及其他好几家《财富》500 强企业作为客户,靠的是一个他们称之为 Atlas 的强大内部智能体。

[03:17] **SPEAKER_00:** So Atlas can basically do anything within the product which you want to do. So it can use browsers, it can edit the policies, it can write code, it can do anything within the product.

> Atlas 基本上能在产品内部完成你想做的任何事情。它可以使用浏览器,可以编辑各种策略,可以写代码,可以在产品里做任何事。

[03:28] **SPEAKER_02:** Atlas dramatically expands the scope of DoorDash. It automatically expands the range of what each engineer can take on.

> Atlas 极大地扩展了 DoorDash 项目的范围。它自动扩大了每一名工程师所能承担的工作范围。

[03:32] **SPEAKER_00:** So let's say before Atlas, every engineer can probably work on four to five problems at once because they are bottlenecked by all the boilerplate stuff they have to do for the customers, right? Customers have integration. They would have to probably work on that. Now, with AIFTE taking care of all the boilerplate stuff, each engineer's scope is basically doubled or tripled because they don't need to work on the boilerplate code.

> 比方说,在有 Atlas 之前,每个工程师大概同时只能处理四到五个问题,因为他们被那些必须为客户做的样板化(boilerplate)工作卡住了脖子,对吧?客户需要做集成,他们大概就得去做这些。而现在,有了 AI 全职员工(AI FTE)来处理所有这些样板化的活儿,每个工程师能处理的范围基本上翻了一倍或两倍,因为他们不再需要去写那些样板代码了。

[03:54] **SPEAKER_02:** But Atlas doesn't just accelerate Giga's engineers. It also adds to the scope of DoorDash. It acts as a full-time AI employee that works in tandem with a human FTE to service dozens of accounts.

> 但 Atlas 不只是让 Giga 的工程师提速。它还扩大了 DoorDash 项目能覆盖的范围。它扮演着一名全职 AI 员工的角色,与一名人类全职员工协同配合,一起服务几十个客户账户。

[04:07] **SPEAKER_00:** Right now, we have only a single human FTE within the company. As hard as it's to believe, because we have companies like DoorDash using us, we are in pilots with multiple Fortune 500s, 10 plus Fortune 500s, where each of these companies probably have volumes over like 500,000 or a million calls a day. It's only been possible because we have Atlas. And this person can primarily focus on a single company. And this person can primarily focus on just the customer relationships, the ask by the customers, taking customer requests and turning them into feature requests and everything.

> 目前,我们公司里只有一名人类全职员工。虽然难以置信,但因为有 DoorDash 这样的公司在使用我们,我们正在跟多家《财富》500 强企业进行试点合作——十多家《财富》500 强——而这些公司每家每天的通话量可能都超过五十万甚至一百万通。这一切之所以可能,全靠我们有 Atlas。而这名员工可以主要专注于一家公司。这名员工可以主要专注于客户关系、客户提出的诉求,把客户的请求转化为功能需求等等一系列工作。

[04:36] **SPEAKER_02:** Building an AI teammate is one approach. Another is to build an AI integrated source of truth that gives employees instant context across your entire system. Legion Health, which is building an AI native psychiatry network, is one example of how to do this. Legion built a custom internal interface for their care operations team that lets them pull in. It lets them pull in patient history, scheduling availability, insurance codes, and a lot more.

> 打造一个 AI 队友是一种做法。另一种做法是打造一个 AI 集成的"单一事实来源",让员工能够即时获取贯穿整个系统的上下文信息。Legion Health——一家正在构建 AI 原生精神科诊疗网络的公司——就是这么做的一个例子。Legion 为他们的诊疗运营团队打造了一个定制化的内部界面,让他们可以调取信息。它让团队能够调取患者病史、排期空档、保险代码等等许多内容。

[05:04] **SPEAKER_05:** What we're showing you right now is an interface that a vast majority of our care operations team uses in their day-to-day work for anything that actually has not been yet automated. And this includes everything from, as Arthur's kind of showing on his screen, digging into a particular patient or many patients' backgrounds, trying to understand where they're at in their journey. If they need it. If they need a new appointment to be rescheduled, if they're having a prescription issue, if they've sent us a message that in traditional health care might have otherwise gotten lost in the sea of different communications that go back and forth between so many different people. All of that is at a fingertips reach for every single member of our care ops.

> 我们现在给你们展示的这个界面,是我们诊疗运营团队绝大多数成员在日常工作中使用的,用来处理任何还没被自动化的事务。这涵盖了方方面面,正如 Arthur 在他屏幕上演示的那样,比如深入查看某一位患者或很多位患者的背景资料,试图搞清楚他们在整个诊疗旅程中处在哪个阶段。如果他们需要重新预约新的就诊时间,如果他们遇到了处方方面的问题,如果他们给我们发来了一条在传统医疗体系里本可能淹没在众多人之间来回往复的海量沟通里而丢失的信息——所有这些,我们诊疗运营团队的每一位成员都能触手可及。

[05:48] **SPEAKER_02:** This single source of truth interface has let Legion keep its ops headcount flat, even as it's dramatically scaled revenue.

> 这个"单一事实来源"界面让 Legion 得以在营收大幅增长的同时,保持运营人员编制不变。

[05:55] **SPEAKER_01:** So we've grown 4x in the past year. But we have a lot more. We haven't hired a single net new person. We've been able to 4x the number of patients. We're seeing thousands of patients a month. We have dozens of providers.

> 我们在过去一年里增长了四倍。但我们做到的远不止如此。我们没有净增招过哪怕一个新员工。我们已经把患者数量扩大了四倍。我们每个月要接诊数千名患者。我们有几十名医疗服务提供者。

[06:07] **SPEAKER_01:** But we have one clinical lead. We have one patient support person. And we have one billing person. And in a typical health care company, those are all departments. Those are call centers. Those are groups of people sitting around desks doing a ton of things manually.

> 但我们只有一名临床负责人。我们只有一名患者支持人员。我们只有一名账务人员。而在一家典型的医疗公司里,这些都各自是一个部门。它们是呼叫中心。它们是一群群坐在办公桌前手动处理海量事务的人。

[06:19] **SPEAKER_02:** A third approach is actually build custom agents for each employee depending on their workflow and preferences. Phase Shift, which is building agents. to automate accounts receivable, took this approach.

> 第三种做法,其实是根据每名员工的工作流程和偏好,为他们各自打造定制化的智能体。Phase Shift 就采用了这种做法——这家公司正在打造用于自动化应收账款(accounts receivable)的智能体。

[06:31] **SPEAKER_03:** So Phase Shift right now is a 12 person team and we're going up against companies that have been around since 2006 that have hundreds of employees. The key to us as a 12 person team moving so fast is we bring A.I. into every process that is manual and try to automate as much as possible with A.I. agents.

> Phase Shift 现在是一个 12 人的团队,而我们要对抗的是那些自 2006 年就已存在、拥有数百名员工的公司。作为一个 12 人的团队,我们能跑得这么快,关键就在于我们把 AI 引入每一个手动的流程,并尽可能用 AI 智能体去自动化。

[06:47] **SPEAKER_02:** One way Phase Shift does this is by literally asking its employees to document the manual tasks they do and then building custom agents for them.

> Phase Shift 实现这一点的一种方式,就是直接要求员工把自己所做的手动任务记录下来,然后为这些任务打造定制化的智能体。

[06:56] **SPEAKER_03:** So what we do is. Essentially say, what do you spend your time doing throughout the day and we make them document that and then we build quick A.I. agents.

> 我们的做法就是,基本上去问:你一整天的时间都花在做什么上?然后让他们把这些记录下来,接着我们就迅速搭建 AI 智能体。

[07:06] **SPEAKER_02:** And this culture of relentless automation has let Phase Shift delay hiring for entire functions.

> 而这种孜孜不倦追求自动化的文化,让 Phase Shift 得以把整整一些职能的招聘都往后推迟。

[07:12] **SPEAKER_03:** We've actually avoided hiring a design person at the company so far to date. We're about a 12 person company by just leveraging magic patterns and our engineering team uses that to build all front end designs.

> 到目前为止,我们其实一直没有招聘设计人员。作为一家大约 12 人的公司,我们只是借助 Magic Patterns,我们的工程团队用它来完成所有前端设计。

[07:21] **SPEAKER_02:** These approaches aren't mutually exclusive. You can build A.I. teammates, a unified source of truth. And custom agents for each member of your team. The companies that do this are staying lean and setting record high growth rates. This is the new way to build and the startups that figure it out first are going to win.

> 这几种做法并不互相排斥。你可以打造 AI 队友、一个统一的事实来源,以及为团队中每一名成员定制的智能体。那些这么做的公司都保持着精简,并创下了破纪录的高增长率。这就是新的构建方式,而最先想明白这一点的创业公司,终将胜出。
