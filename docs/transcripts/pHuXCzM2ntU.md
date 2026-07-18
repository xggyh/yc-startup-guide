# 全文转录 · 25 岁、零法律背景,如何做成 6.75 亿美元法律 AI 公司(Legora 复盘)

> ▶ [YouTube](https://www.youtube.com/watch?v=pHuXCzM2ntU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/pHuXCzM2ntU.md) &nbsp;·&nbsp; How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_01:** AI is continuously developing super super quickly and that means we need to do the same we're finding that as we go deeper and deeper and deeper in the entire legal software stack we're also seeing that the line between software and service is blurring i think that's been one of our strengths as a company to say we don't know exactly where the future is going but neither do you so let's work together to make sure that we're both winners in whatever happens

> AI 在持续地飞速发展,这意味着我们也必须跟上同样的速度。我们发现,随着我们在整个法律软件栈中钻研得越来越深,软件与服务之间的界限正在变得模糊。我认为这一直是我们公司的优势之一,那就是我们敢说:我们并不确切知道未来会走向何方,但你们也不知道,所以让我们携手合作,确保无论发生什么,我们双方都是赢家。

[00:34] **SPEAKER_02:** today i'm joined by max junius strand he's the ceo and co-founder of legora the gora was in winter 24 and they are the leading ai workspace helping lawyers and legal professionals do their work welcome max hey thanks gustav it's been 13 months since you did the batch it's been a really busy

> 今天与我一起的是 Max Junius Strand,他是 Legora 的 CEO 兼联合创始人。Legora 是 2024 年冬季批次的公司,他们打造了领先的 AI 工作空间,帮助律师和法律专业人士完成工作。欢迎你,Max。嘿,谢谢你,Gustav。距离你们参加批次已经过去 13 个月了,这真是非常忙碌的一年。

[00:49] **SPEAKER_01:** year for you it has it feels like it was a really long time ago i feel like i've aged five years in the last one for those who don't know tell us about the gora yeah what are you guys building at least we've got a bunch of stuff going on in the next couple months we've got a bunch of stuff going on in the next couple months we're building the ai powered workspace for lawyers we're essentially transforming the way that they complete their work everything from reviewing drafting researching essentially within legal you've had this incredibly fragmented software space where there was a lot of point solutions and ai was never good enough to actually work with unstructured text precedent legal documents and when gpt 3.5 got out that just completely changed the game so we were quick to you know build a poc and then now we've scaled that all the way to an enterprise grade system serving tens of thousands of lawyers daily yeah those

> 确实如此,感觉那已经是很久以前的事了,我感觉在过去这一年里我老了五岁。对于不了解的人,请给我们介绍一下 Legora,你们到底在做什么?接下来几个月我们有一大堆事情要做。我们正在为律师打造由 AI 驱动的工作空间,本质上是在彻底改变他们完成工作的方式,从审阅、起草到检索,涵盖法律工作的方方面面。法律领域一直是一个极度碎片化的软件市场,有大量单点解决方案,而 AI 从来都不够好,无法真正处理非结构化文本、先例和法律文件。当 GPT-3.5 发布时,局面就彻底改变了。于是我们迅速做出了一个概念验证,如今我们已经把它扩展成了企业级系统,每天为数万名律师提供服务。

[01:33] **SPEAKER_02:** point solutions were basically workflow tools so what were they before because it's been a history of a legal technology industry that existed before this is not started right now

> 那些单点解决方案基本上就是工作流工具,那么在此之前它们是什么样的呢?因为法律科技行业是有历史的,它在此之前就存在,并不是现在才刚刚起步。

[01:43] **SPEAKER_01:** no i mean legal tech has been a category for a long time but um it was really unsexy for a long time i think and you'd essentially have a broad range of point solutions everything from templating tools where you would sort of codify a contract yeah to special translation tools or headline tools or research tools and all of them work with text somehow and generative ai came into the game and just kind of threw up everything off the table and then when it landed you very clearly saw how you could solve a lot for a lot of these use cases with the same underlying tech so chat

> 是的,我是说法律科技作为一个品类已经存在很久了,但我认为在很长一段时间里它都相当不吸引人。你基本上会看到各种各样的单点解决方案,从可以把合同标准化的模板工具,到专门的翻译工具、标题工具或检索工具,它们全都以某种方式在处理文本。然后生成式 AI 登场了,把桌上的一切都掀翻了,等尘埃落定后你会非常清楚地看到,如何用同一套底层技术为其中许多使用场景解决大量问题。

[02:15] **SPEAKER_02:** dp came uh maybe eight months prior to you guys starting this company describe that moment was that an important moment for the company's founding we were playing around in ai and legal

> ChatGPT 大概在你们创办这家公司前八个月出现。请描述一下那个时刻,那对公司的创立来说是一个重要时刻吗?我们当时已经在 AI 和法律领域里摸索了。

[02:23] **SPEAKER_01:** way before chat tpt and we were using these early models from bert a company from google yeah they were decent in english but they were just horrendously bad in swedish and you know the first observation that kind of sparked the founding of the company was one of the co-founders friend who was a lawyer spent four months during a summer just summarizing court cases for a big law firm we basically saw that gpt 3.5 was released to developers started building i think the first thing that we built was a stock option reader that would explain how a stock option contract works useful right you know as startup founders with no legal background that was seemed reasonable and then very quickly the sort of focus changed to how do we build this more wall-to-wall or end-to-end system that every legal professional wants to work with on a databases and the first product was really quite simple especially building for europe you've got to go through a lot of hassle to kind of conform with all the data processing requirements so you know all data hosted within europe nothing for training no retention exemption from human review when you look at the way azure and aws is structured and we we kind of jumped through all those hoops and just built a system that was compliant for law firms to work with and then very quickly as the general sort of ai platforms continue to develop with chat gpt with cloud with gemini the requirements for what we had to build to be much much better you know continuously increased in

> 那是在 ChatGPT 出现之前很久,我们当时用的是 BERT 这类早期模型,BERT 是谷歌旗下的东西。它们在英语上还算说得过去,但在瑞典语上表现糟糕得可怕。你知道吗,真正点燃公司创立火花的第一个观察是:一位联合创始人的朋友是律师,某个夏天花了整整四个月为一家大型律所总结法院判例。我们看到 GPT-3.5 向开发者开放后就开始动手搭建。我记得我们做的第一个东西是一个股票期权阅读器,它能解释一份股票期权合同是如何运作的。挺有用的吧,作为没有法律背景的创业者,这似乎很合理。然后焦点很快就转向:我们如何打造一个更加端到端、覆盖全流程的系统,让每一位法律专业人士都愿意在数据库上使用它。第一款产品其实相当简单,尤其是为欧洲市场打造,你得经历大量繁琐的流程来满足所有数据处理的要求——所有数据都托管在欧洲境内,不用于训练,不做数据保留,豁免于人工审查。当你研究 Azure 和 AWS 的架构方式时,我们基本上是跳过了所有这些障碍,做出了一个合规、可供律所使用的系统。随后,随着 ChatGPT、Claude、Gemini 这些通用 AI 平台不断发展,我们必须把产品做得越来越好的要求也在持续提高。

[03:49] **SPEAKER_02:** some industries or some some categories like coding or law for example it seems like the models are just magical like like they do things that you can't do in a normal way but you know i like to think of some of the things that i've learned from the major companies like the ima and that the people that were in those industries before could not even imagine be possible. Could you describe sort of like the first time you used Legora to do something that was magical for a customer and how they experienced it?

> 在某些行业或某些品类里,比如编程或法律,这些模型简直就像有魔力一样,它们能做到用常规方式做不到的事情。我喜欢回想自己从那些大公司里学到的一些东西,这些东西是过去身处这些行业的人根本无法想象的。你能不能描述一下,你第一次用 Legora 为客户做出某件神奇的事情、以及他们当时的体验?

[04:10] **SPEAKER_01:** Yes, I think the first time was when we deployed Legora into the biggest law or largest law firm in the Nordics, Mannheimer and Swartling. Their managing partner had a famous saying in the newspaper that AI was more artificial than intelligent, which was back from the early ML models. Yeah, I mean, a lot of firms burnt themselves buying expensive tools that didn't solve anything. And I came into that meeting, you know, I bring up my laptop and I just ask him, you know, put in a query.

> 是的,我想第一次是在我们把 Legora 部署到北欧最大的律所 Mannheimer Swartling 的时候。他们的执行合伙人曾在报纸上有句名言,说 AI 更多是"人工"而非"智能",那还是早期机器学习模型时代的说法。是啊,很多律所都因为买了昂贵却什么都解决不了的工具而吃过亏。我走进那场会议,打开我的笔记本电脑,请他输入一个查询。

[04:37] **SPEAKER_01:** And he puts in this legal research query and we've tied Legora to Swedish legislation with a RAG system and it answers perfectly. And, you know, you kind of see it on his eyes, like it's the aha moment. And now when we're- Is that your aha moment as well? No, I think my personal aha moment was just, using ChatGPT generally, right?

> 他输入了一个法律检索查询,而我们已经用 RAG 系统把 Legora 接入了瑞典的立法,它回答得非常完美。你能从他的眼神里看出来,那是一个"啊哈"顿悟的时刻。那也是你的顿悟时刻吗?不,我个人的顿悟时刻其实就是最初普通地使用 ChatGPT,对吧?

[04:58] **SPEAKER_01:** Like it was amazing. It felt complete sci-fi that you could talk with the computer and it talked back. And, you know, as an entrepreneur, you kind of quickly, you know, from that, you understand that, all right, we can apply it in this space in this way and in that space in this other way. And I think for legal specific, the chat experience I think was always cool.

> 那真是太惊人了。你能和电脑对话,它还会回应你,这感觉完全就是科幻。作为一个创业者,你会很快从中意识到:好,我们可以用这种方式把它应用在这个领域,用另一种方式应用在那个领域。而就法律领域而言,我觉得对话体验一直都很酷。

[05:16] **SPEAKER_01:** But when we took the same models and sort of applied them differently, one of the first use cases we did was due diligence, where you have, you know, hundreds or, you know, a lot of documents that you want to review. And instead of going through them one by one by one, we just made this large grid where essentially every document represented a row and then you could put your queries in the columns, right? And as you then put in, you know, a hundred employment agreements and you ask, does all of them include an IP clause where the company protects its intellectual property? And it just starts to rattle and it goes, yes, yes, yes, yes, no, no, no, yes, yes, yes, yes.

> 但当我们把同样的模型用另一种方式来应用时,我们做的第一批用例之一就是尽职调查。你手头有几百份、甚至大量需要审阅的文件,与其一份一份地逐一过,我们做了一个大网格,本质上每份文件代表一行,然后你可以把查询放到列里。这样当你放进一百份雇佣协议,然后问:它们是否都包含公司保护其知识产权的 IP 条款?它就开始飞快地运转,回答:是、是、是、是、否、否、否、是、是、是、是。

[05:56] **SPEAKER_01:** And it always links back to the citation. You realize like, holy shit, this is transformational. It's taking tasks which used to be, you know,

> 而且它总是会链接回原始出处的引用。你会意识到,天哪,这是颠覆性的。它把那些过去需要花上……的任务

[06:05] **SPEAKER_02:** days or hours and it's turning them into minutes. By the time this is live, you will have announced that you have raised a Series B. How much did you raise?

> ……几天或几小时的任务,变成了几分钟。等这期节目上线时,你们应该已经宣布完成了 B 轮融资。你们融了多少钱?

[06:15] **SPEAKER_01:** We raised $80 million led by Iconic and General Catalyst and, you know, grateful for YC's continued participation as well as Benchmark and Redpoint.

> 我们融了 8000 万美元,由 Iconic 和 General Catalyst 领投,同时也非常感谢 YC 的持续参与,以及 Benchmark 和 Redpoint。

[06:23] **SPEAKER_02:** What is the software like? So, so, as a lawyer using Legora, what does my day-to-day look like?

> 这个软件是什么样的?作为一名使用 Legora 的律师,我的日常工作会是什么样子?

[06:30] **SPEAKER_01:** So it's really broken up into two pieces. The first one is the web application and the second one is our Word add-in. So we integrate directly into Microsoft Word. Right.

> 它其实分成两个部分。第一部分是网页应用,第二部分是我们的 Word 插件,也就是说我们直接集成进了 Microsoft Word。

[06:38] **SPEAKER_01:** So if we start with the web application, the first thing that we had was just a simple chat, chat over your own documents and files. This has quickly developed into its own agent that's able to use a lot of the other end points in the app and also external tools to solve more complex sort of step-by-step workflows. So you could imagine saying, hey, I want to write a memo. And the first step of the memo is to go out and do some research.

> 先说网页应用,我们最初有的只是一个简单的对话功能,让你能针对自己的文档和文件进行对话。这很快发展成了它自己的 agent(智能体),它能够调用应用内许多其他端点以及外部工具,来解决更复杂的分步骤工作流。你可以想象这样说:嘿,我想写一份备忘录。备忘录的第一步是去做一些检索研究。

[07:02] **SPEAKER_01:** The second step is to take all that research and conform it into the standard language of the firm. And the third step is to write the report and then output is a report. And does it do all of that? It does all of that.

> 第二步是把所有这些检索结果整理成符合律所标准用语的文字。第三步是撰写报告,最终输出就是一份报告。它真的能完成这一切吗?它全都能做到。

[07:13] **SPEAKER_01:** Right. And I think we can talk more about it later, but MCP and the way that you can scale the tool usage of these agents is something that I'm super keen on and that we're leaning very heavily into, because a lot of firms have different needs in terms of how they want to adopt the tools to solve for their specific workflows. And it's different if you work in intellectual property or if you work in restructuring or if you work in corporate or if you work in disputes. The second piece outside of the chat is, well, the grid that I talked about before.

> 对。我想我们稍后可以更多地聊这个,但 MCP 以及扩展这些 agent 工具使用能力的方式,是我特别热衷、也在大力投入的方向。因为许多律所在如何采用这些工具来解决他们特定的工作流方面有着不同的需求。你做知识产权、做重组、做公司业务还是做争议解决,情况都各不相同。除了对话之外的第二部分,就是我之前提到的那个网格。

[07:42] **SPEAKER_01:** We call it tabular review. It's essentially input any number of files and then input any number of queries. And we sort of cross-run that across each other. And the big innovation there does not really come from, you know, how do you prompt, and work with a model, but it's how do you make this run at scale?

> 我们称之为表格化审阅。本质上就是输入任意数量的文件,再输入任意数量的查询,然后我们让它们两两交叉运行。这里真正的重大创新其实并不在于你如何写提示词、如何与模型协作,而在于你如何让它大规模地运行。

[07:59] **SPEAKER_01:** How do you run 100,000 queries in parallel at the same time and make sure nothing breaks, all the citations are correct? There's a lot of chunking, sort of rag-searching within the individual documents, because sometimes they're very, very long. And with legal docs, there are certain intricacies where you need to always include things like the definitions. And there might be cross-references within each clause to each other.

> 你如何同时并行运行十万个查询,并确保不出任何差错、所有引用都准确无误?这里面涉及大量的分块处理,也就是在单个文档内部做 RAG 检索,因为有时这些文档非常非常长。而对于法律文件,有一些微妙之处,你必须始终把诸如定义之类的内容包含进来,而且每个条款之间可能还存在相互的交叉引用。

[08:22] **SPEAKER_01:** So taking all of that into consideration, that kind of serves the grid. Looking at the Word add-in, I think you could phrase it as Cursor for lawyers. MARK MANDELMANN, CURSOR FOR LAWYERS Lawyers basically use Word. That's a known fact for a long time.

> 所以把所有这些因素都考虑进去,才能支撑起这个网格功能。再来看 Word 插件,我觉得你可以把它形容为"律师版的 Cursor"。律师基本上都用 Word,这是长久以来众所周知的事实。

[08:34] **SPEAKER_01:** Yeah. They draft and they review contracts in Word or PDF form. And what we really wanted to do is, similar to Cursor, how do we bring generative AI into the existing work environment of a legal professional? And that means integrating in Word.

> 是的。他们在 Word 或 PDF 格式中起草和审阅合同。我们真正想做的,和 Cursor 类似,就是:如何把生成式 AI 带进法律专业人士现有的工作环境?而这就意味着要集成进 Word。

[08:48] **SPEAKER_01:** Now, the difference is you can't fork Word, and you can't take up all the real estate you want. You're basically conformed to this sort of right-hand column. And then you've got to get really creative. It's basically like designing a mobile app, almost, because that's all the real estate you get.

> 不过,不同之处在于你无法 fork(分叉复刻)Word,也没法随心所欲地占用界面空间。你基本上被限制在右侧那一栏里,于是你必须变得非常有创意。这几乎就像是在设计一款手机应用,因为你能拥有的界面空间就那么点。

[09:04] **SPEAKER_01:** And the first thing that we built there was just, how do we integrate an assistant or a chat that's able to not only read the document, but also create edits? So you might say, I want you to renegotiate this MSA for the buyer and do that using this internal checklist that I have or this internal sort of playbook or precedent. And now we've scaled that to not only work in a chat-by-chat basis, but also more extensive workflows. So you can say, here's a contract.

> 我们在那里做的第一件事就是:如何集成一个不仅能读懂文档、还能直接生成修改的助手或对话?于是你可以说,我想让你以买方的立场重新谈判这份 MSA(主服务协议),并且用我这份内部清单、或者这份内部的操作手册或先例来做。如今我们已经把它扩展到不仅仅是一次次对话的层面,还能处理更庞大的工作流。所以你可以说:这是一份合同。

[09:30] **SPEAKER_01:** I want you to take my playbook that consists of 20 different steps and make sure we negotiate from the starting positions and have different fallbacks included.

> 我想让你拿着我这份包含 20 个不同步骤的操作手册,确保我们从各自的初始立场开始谈判,并且把不同的退让备选方案都纳入进来。

[09:39] **SPEAKER_02:** Do you have a specific example of something that was impossible a couple of years ago for a lawyer? Like, literally, you couldn't do it, and now you can do it.

> 你有没有一个具体的例子,是律师在几年前根本不可能做到的事?就是字面意义上你以前做不到,而现在你能做到了。

[09:46] **SPEAKER_01:** MARTIN SPLITT- Yeah, I mean, I think there's a lot of it, right? The early ML models were really bad at legal language. And what they were really bad at was when the language looked different across documents. You could train a system to find, let's say, a change of control clause if it looked the same way across all the documents.

> 是的,我觉得这样的例子有很多。早期的机器学习模型在处理法律语言方面真的很糟糕,而它们最不擅长的,是当同一类内容在不同文档中表述各异的情况。你可以训练一个系统去找出比如"控制权变更"条款——前提是它在所有文档里长得都一样。

[10:05] **SPEAKER_01:** But it was really, frankly, bad at finding, MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 但坦白说,它真的很不擅长去找出……嗯哼,嗯哼,嗯哼,嗯哼。

[10:08] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 嗯哼,嗯哼,嗯哼,嗯哼。

[10:09] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 嗯哼,嗯哼,嗯哼,嗯哼。

[10:09] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 嗯哼,嗯哼,嗯哼,嗯哼。

[10:09] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 嗯哼,嗯哼,嗯哼,嗯哼。

[10:09] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm.

> 嗯哼,嗯哼,嗯哼,嗯哼。

[10:10] **SPEAKER_01:** MARTIN SPLITT- Mm-hmm. MARTIN SPLITT- Mm-hmm. meaning of a change of control if the clause didn't look that way and so what the LLMs have allowed us to do is to just take tasks where especially on like large contracting and large document extraction so how do we pull the insights from this another one is just you know redlining so redlining files within word against a president or playbook completely impossible or take deep research across you know hundreds or thousands of judgments where you need to conform not only to judgments but also pull in things like legislation and regulation right all into the same place yeah okay since the cost of intelligence is going down it also increases the amount of queers we can do right so one pretty cool thing is you know embedding making one search against your own documents and files making another one on the web and making another one against um court cases and judgments and legislation and combining all of it to create effectively like a memo that maybe they couldn't afford to do in the past they just didn't do it no and and similarly with with due diligence when if you go way back it used to be a physical data room yeah that's why it's called a room you used to go into the room you had all the documents and all the contracts and then you'd sit down and read through all of them yeah and you had to mark them with a pen so making and doing a due diligence on a company was really expensive and now it's becoming almost a commodity where you're expected to do it but clients are also not really that excited to pay for very simple contract contract contract review when they know that AI can do you know 99 of it wow yeah so in the time that I've been

> ……如果条款的表述不是那个样子,它就找不出"控制权变更"的含义。所以 LLM 让我们能够去承接那些任务,尤其是在大型合同和大规模文档信息提取方面——我们如何从中提炼出洞见。另一个例子就是红线批注,在 Word 里对照先例或操作手册对文件做红线修改,这在过去完全不可能。或者跨越几百上千份判决做深度检索研究,你不仅要参照判决,还要把立法和法规等内容都拉进来,全都汇聚到同一个地方。好,由于智能的成本正在下降,我们能做的查询数量也随之增加。所以一件相当酷的事情是:同时对你自己的文档和文件做一次检索,再对网络做一次检索,再对法院案例、判决和立法做一次检索,然后把所有这些结合起来,实际上生成一份他们过去或许负担不起、干脆就不做的备忘录。是啊,尽职调查也类似。追溯到很久以前,那曾经是一个实体的资料室,这就是它被叫作"room(房间)"的原因。你以前得走进那个房间,里面摆着所有文档和合同,你就坐下来把它们全部读一遍,还得用笔做标记。所以对一家公司做尽职调查曾经非常昂贵,而现在它几乎快变成了一种大宗商品,大家默认你就该做这件事。同时客户也不太愿意为非常简单的合同审阅付很多钱,因为他们知道 AI 能完成其中大约 99% 的工作。

[11:42] **SPEAKER_02:** away see we have funded some legal software companies but the hardest challenge for all of them was selling to law firms yeah and selling to legal like most of them would end up selling to companies because law firms were just like not possible to sell to that radically changed just like two years ago yeah can you tell us sort of like what do you think changed and how do you do it when you go and sell to law firms is that a big challenge for you or is it a big challenge for you when you go and sell to one of the major law firms in the world so for everybody listening this was

> 你看,我们资助过一些法律软件公司,但对它们所有人来说最难的挑战就是向律所销售。是啊,向法律行业销售——它们中大多数最后都转向卖给企业客户,因为向律所销售几乎是不可能的。而这一点大约在两年前发生了翻天覆地的变化。你能不能告诉我们,你认为是什么发生了改变?当你去向律所销售时你是怎么做的?这对你来说是个巨大的挑战吗?或者当你去向世界上顶级的大律所销售时,这是个巨大的挑战吗?各位听众,这——

[12:09] **SPEAKER_01:** also one of the questions that I remember you pushing really hard on during the interview and I think we were quite contrarian to say you know no it's different this time trust us yep I'm glad we were right I think the way that we approached the problem was always with this idea of we win if you win so let's align our incentives with saying as a law firm this technology is revolutionizing you're you're going to need to adopt it in some sense shape or form and we want to be that long-term partner and somehow they know that well so what happens is um a lot of legal work is low differentiation you know if you're doing a DD from you know law from X or law from Y kind of getting the same deal and so when you have this perfect equilibrium of services and somebody disrupts that by taking a new approach clients are quick to switch yeah I mean clients are under price pressure they want to be effective legal fees are very high and so if this equilibrium breaks you are almost forced to adopt it and you are incentivized it's kind of the same as the lawyers adopted computers right if you're building by the hour you could say well let's have a person walk to the library you know find the right book you know find the right cases or the right president and use that for whatever work we do yeah or you press control F right there's always this dilemma of you want to serve your client in the best way possible because that drives you more revenue over time yeah and for a lot of a lot of the firms that we work with they're you know brand reputation trust as always putting the client first is what matters the most and so a lot of the firms also want to be leaders here yeah you know some of them want to be fast second movers but many want to be first movers because they're understanding if you have this perfect equilibrium and you take a simple type of work that gets disrupted you should get more market share by moving down quicker um but then it's not a race to the bottom right yeah it's a question of okay if we take every country has a ranking of law firms basically yeah right and it's also not a race to the bottom in terms of pricing because if you pull down let's say the cost of a due diligence you free up more time to spend with a board on advising them on you know a really complex merger or a really complex acquisition and so what typically ends up happening is you're under time pressure you could do more work but you just have all this stuff that needs to get done and that's what AI is really good at but it's also serving lawyers in very creative ways I mean we've had use cases where you know we get a call from somebody and they say I played a role role-playing game with legora you know trying to win this argument and I'm asking it to act as the other party right wow there was this amazing uh situation that one of the Spanish um partners at a firm called peretiorca had where he went into court he had put all the evidence and all the documents from the opposing party in legora and he was actively querying it during the hearing and during you know at the time when the other attorney was speaking because then he could immediately interrupt if he found something that was uh that was wrong and he phrased it very nicely he said when when he goes into the battlefield having legora is like having another piece of armor and I thought that was that was very poetically could you use legora to do negotiation on your behalf yeah so the way that we built that is I think the llms by themselves are not good enough for that yet and we can talk about that but it's it's interesting to to build these products knowing that the models will get better yeah and where do you stop yeah right on every feature but so so that feature in the gore is called playbooks a playbook is essentially a collection of rules where you either approve or disapprove something so you might say for the way that you would sign CAs here at YC you always want the definition within a confidentiality agreement to look a certain way so you provide the rule you provide some example language and then you say all right if the opposing party will not accept this definition we have some fallbacks so fallback one and fallback two and you just open a document in agora you open the playbook and you say press play and it goes through every rule and runs it against the contract and it marks it up yeah so it's a really cool thing about this is it scales outside of just legal departments so at legora every sales rep is using legora to negotiate ndas before sending it to our legal team and we just started working with this very large bank in the nordics and it's very quickly moved from you know the legal team to compliance to risk and now to sales because everybody can leverage the system and the cool thing about it is it's not only faster and more accurate but you agree on a standard because the legal team then creates the playbook and that becomes the standard that everybody uses so it actually increases

> 这也是我记得你在面试时非常用力追问的问题之一,而我想我们当时相当反主流地说:不,这次不一样,相信我们。是的,我很高兴我们说对了。我认为我们处理这个问题的方式一贯秉持"你赢我们才赢"的理念,所以让我们把双方的利益绑在一起:作为一家律所,这项技术正在带来革命,你迟早都得以某种形式采用它,而我们想成为那个长期的合作伙伴,他们某种程度上也心知肚明。事情是这样的:很多法律工作差异化程度很低,你找 X 律所还是 Y 律所做尽调,拿到的基本是一样的结果。所以当服务处于这种完美均衡状态,一旦有人用新方法打破它,客户会很快转投。客户面临价格压力,他们想要高效,律师费又非常高昂,所以一旦这种均衡被打破,你几乎是被迫去采用它,而且你也有动力去采用。这就跟当年律师采用计算机是一个道理——如果你按小时计费,你可以说,让一个人走到图书馆去,找到正确的书,找到合适的判例或先例,再用它来做手头的工作;或者你直接按 Ctrl+F。这里始终存在一个两难:你想以最好的方式服务客户,因为长期来看这会带来更多收入。对我们合作的很多律所来说,品牌、声誉、信任、始终把客户放在第一位才是最重要的,所以很多律所也想在这方面当领导者。有些律所想做快速跟随的第二梯队,但许多律所想做先行者,因为他们明白:如果处于完美均衡,而你把某类简单工作率先颠覆,你就应该通过更快地"往下走"来抢占更多市场份额。但这并不是一场逐底竞争,对吧?问题在于——基本上每个国家都有律所排名。而在定价方面它也不是逐底竞争,因为如果你把比如尽职调查的成本压下来,你就腾出了更多时间去陪董事会,为他们在一桩极其复杂的并购或收购上出谋划策。所以通常的结果是:你时间紧张,本来可以做更多工作,但你手头有一大堆必须完成的事,而这正是 AI 特别擅长的。它也在以非常有创意的方式服务律师。我们遇到过这样的用例:有人打电话给我们说,我和 Legora 玩了个角色扮演游戏,想在这场辩论里取胜,我让它扮演对方当事人。哇。还有一个很精彩的情况:西班牙一家叫 Pérez-Llorca 的律所有位合伙人,他上庭时把对方当事人的所有证据和文件都放进了 Legora,并在庭审过程中、在对方律师发言时主动向它发起查询,这样一旦他发现有什么不对的地方就能立刻打断。他有个很妙的说法,他说当他走上战场时,拥有 Legora 就像多披了一件盔甲。我觉得这形容得非常有诗意。你能用 Legora 来替你进行谈判吗?能。我们打造这个功能的方式是——我认为 LLM 本身目前还不足以独立胜任这件事,这个我们可以再聊,但很有意思的是,你在明知模型会越来越好的前提下去打造这些产品,那你在每个功能上到底该止步于何处呢?这个功能在 Legora 里叫作 playbooks(操作手册)。一份 playbook 本质上是一组规则,你对某样东西要么批准要么否决。比如你可以说,就 YC 这里签保密协议的做法而言,你总是希望保密协议里的定义部分是某种特定的样子,于是你提供这条规则,提供一些示例措辞,然后你说:好,如果对方不接受这个定义,我们有一些退让备选方案,备选方案一和备选方案二。你只要在 Legora 里打开一份文档,打开这份 playbook,点击"运行",它就会逐条遍历所有规则,对照合同去运行,并把修改标注出来。很酷的一点是,这不仅仅局限于法务部门。在 Legora,每一位销售代表在把 NDA 发给我们法务团队之前,都会用 Legora 来谈判这份 NDA。我们最近开始和北欧一家非常大的银行合作,它很快就从法务团队扩展到合规、到风险,现在到了销售,因为每个人都能利用这套系统。而它的妙处在于,它不仅更快、更准确,你们还就一个标准达成了一致——因为法务团队创建了 playbook,那就成为了所有人使用的标准,所以它实际上提升了……

[17:15] **SPEAKER_00:** quality and consistency over time YC's next batch is now taking applications got a startup in you apply at ycombinator.com apply it's never too early and filling out the app will level up your idea okay back to the video none of you guys when you started were lawyers no so you still

> ……随着时间推移的质量和一致性。YC 的下一个批次现在正在接受申请,如果你心里有一个创业点子,就到 ycombinator.com 去申请吧。申请永远不嫌早,填写申请表本身就会让你的想法更上一层楼。好,回到视频。你们几个创始人在起步时都不是律师,对吧?对。所以你们仍然——

[17:35] **SPEAKER_02:** are building one of the largest or fastest growing legal ad company in the world how do you do that

> ——正在打造全世界最大或增长最快的法律 AI 公司之一,你们是怎么做到的?

[17:39] **SPEAKER_01:** I think at this point I've become a hobby lawyer but how we approached it was being incredibly humble humble for the fact that we did not know the industry we were quick to create relationships with our early partners where feedback was you know happening daily yeah and I think that's been one of our strengths as a company to say we don't know exactly where the future is going but neither So let's work together to make sure that we're both winners in you know whatever happens and I think now we of course have the privilege of having hired a ton of lawyers into the team that work directly with the product teams and directly with the customers especially in an industry that is now going through such big change it was useful to come in with more niveness if you will saying why does it work this way you know it could work this way instead let's

> 我想到了这个阶段我已经成了一名业余律师,但我们的做法是保持极度的谦逊——谦逊地承认我们不了解这个行业。我们很快就与早期合作伙伴建立起关系,反馈几乎是每天都在发生。我认为这一直是我们作为公司的优势之一,那就是承认:我们并不确切知道未来会走向何方,但你们也不知道,那就让我们携手合作,确保无论发生什么我们双方都是赢家。当然,如今我们也很荣幸招募了大量律师加入团队,他们直接与产品团队、与客户打交道。尤其在一个正经历如此巨大变革的行业里,带着更多的"天真"进来其实很有用,可以问:为什么非得这样做?其实完全可以换成那样做,让我们——

[18:32] **SPEAKER_02:** say you're a founder of watching this right now you're like I want to build a software for logistics for insurance or finance. Is your advice basically you don't need any of my expertise? How do you learn about the things you need to learn though?

> 假设你是一个正在看这期节目的创始人,你想为物流、保险或金融领域打造一款软件。你的建议基本上就是"你并不需要具备我这样的专业背景"吗?那你到底该怎么去学习那些你必须掌握的东西呢?

[18:43] **SPEAKER_01:** I think my advice is learn about them. We went into this, and the first thing I did was I interviewed 100 lawyers. I had this good hack on LinkedIn. I texted them asking if we could have lunch, and I would pay their hourly rate.

> 我的建议是去了解它们。我们进入这个领域时,我做的第一件事就是访谈了 100 位律师。我在 LinkedIn 上有个很好用的小技巧,我给他们发消息问能不能一起吃午饭,并表示我会按他们的时薪付费。

[18:57] **SPEAKER_01:** I could definitely not afford it, and none of them would impose that. They would just say, oh, that's amazing. I'll have the lunch with you anyways. One of the attributes that have been very helpful in my career has been that I'm somebody people want to help.

> 我肯定是付不起的,而他们也没有一个人真的要我付。他们都会说,哦,那太好了,反正我很乐意和你吃这顿午饭。在我职业生涯中一个非常有帮助的特质,就是我是那种别人愿意帮助的人。

[19:16] **SPEAKER_01:** I think that's a very underrated skill. I think there are things you can do to be more like that. You can be a bit fearless in your approach to people, and you can also be very, very thankful and grateful and appreciative of the work that other people help you with. If we hadn't done that.

> 我认为这是一项被严重低估的能力。我觉得你可以通过一些做法让自己更接近那种人:你在与人打交道时可以稍微无所畏惧一点,同时你也可以非常非常地感激、感恩,珍视别人为你付出的帮助。如果我们当初没有这么做——

[19:35] **SPEAKER_02:** But we would not be where we are today. And then how do you conduct a lunch with a lawyer when you're starting a startup and you know not much about law?

> ——我们就不会有今天的成就。那么,当你正在创业、又对法律知之甚少时,你是怎么和一位律师共进午餐、把这顿饭"谈"好的?

[19:42] **SPEAKER_01:** So you'd sit down like this. You'd go to somewhere decently nice because, again, they make a lot of money. It took me some time to even understand that the way that departments work are fundamentally different. A transactional lawyer works nothing the way a lawyer within the corporate department works.

> 你会像这样坐下来。你会挑一个还算不错的地方,因为再说一遍,他们收入很高。我甚至花了一些时间才搞明白,不同部门的工作方式是根本不同的。做交易的律师和公司业务部门里律师的工作方式完全是两码事。

[19:58] **SPEAKER_01:** You just ask them a ton of questions, and I think also giving them something back. So I'd reach out. They see my tech background. And you try to give them nuggets of, oh, that's really cool.

> 你就是不停地问他们大量问题,同时我觉得也要有所回馈。所以我会主动联系他们,他们看到我的技术背景,你就设法给他们一些"哦,这真酷"的小启发。

[20:13] **SPEAKER_01:** What do you think about this? Like, you give them ideas. You make them engaged in wanting to give you advice, and yeah.

> 你对这个怎么看?就是说,你给他们一些点子,让他们参与进来、乐意给你建议。

[20:20] **SPEAKER_02:** And people generally feel good giving founders advice. Of course. Like, it's like something that you should take advantage of. Yeah, and something that I'm really happy to do now from the position where we're at.

> 而且人们普遍乐于给创始人提建议。当然。这是一件你应该好好利用的事。是的,而如今从我们所处的位置出发,这也是我非常乐意去做的事。

[20:31] **SPEAKER_02:** There are some large companies in legal technology. Right? Yeah. Are you going up against all of them?

> 法律科技领域有一些大公司,对吧?是的。你们是要跟它们所有人正面竞争吗?

[20:36] **SPEAKER_02:** Or how do you think about the existing market of legal tech?

> 又或者,你是怎么看待现有的法律科技市场的?

[20:38] **SPEAKER_01:** Right. So there's been a lot of sort of large M&A machines and incumbents in this space for a long time. They're not very popular with the end users. I think they have very kind of far-reaching roots.

> 是这样。长期以来,这个领域一直有很多庞大的"并购机器"和老牌巨头。他们在终端用户中并不太受欢迎。我觉得他们的根基铺得非常广、非常深。

[20:54] **SPEAKER_01:** There's some advantages and data modes and so on that come into play. But effectively, what AI has done is really change the game in terms of how quickly you can ship something. And it's created a new category. So a lot of, again, these existing point solutions were in maybe suites of these M&A machines.

> 里面确实有一些优势、数据护城河之类的东西在起作用。但实际上,AI 真正改变游戏规则的地方,在于你能以多快的速度交付产品,而且它开创了一个全新的品类。所以,重申一遍,很多现有的单点解决方案原本可能只是这些并购机器旗下套件里的一部分。

[21:14] **SPEAKER_01:** And now a lot of it is becoming irrelevant very quickly. And the cost of building software is also going down very, very rapidly. So our ability to out-ship or out-deliver these teams of thousands of engineers with just 30 is insane. And so.

> 而现在这其中很多东西正在非常快地变得无关紧要。同时,构建软件的成本也在极其迅速地下降。所以我们仅凭 30 个人,就能在交付速度和产出上碾压那些拥有数千名工程师的团队,这简直令人难以置信。因此——

[21:35] **SPEAKER_01:** We have instead managed to build a company with, I think at the time of recording, it's about 100, where our velocity is way higher than companies 100 times our size. I think that's interesting in and of itself in terms of how we built the company over the last year. Because when we came out of YC, we were roughly 10 people. And now we're 100.

> ——我们反而打造出了一家公司,录制这期节目时大概有 100 人,而我们的迭代速度远高于那些规模是我们 100 倍的公司。我觉得单就我们过去一年如何搭建这家公司这件事本身而言就很有意思。因为我们从 YC 毕业时大约只有 10 个人,而现在我们有 100 人了。

[21:56] **SPEAKER_01:** And that means we've onboarded, on average, like two people a week. And hiring correctly is really hard. It's a skill you need to learn. Yeah.

> 这意味着我们平均每周入职大约两个人。而正确地招人真的很难,这是一项你必须学会的技能。是的。

[22:05] **SPEAKER_01:** And hiring for velocity, hiring for entrepreneurship and ownership of different products and things, but also scale. Because the company is growing exponentially. So you need your teammates to scale exponentially as well. If people scale linearly, at some point, it's a really large delta.

> 你要为速度而招人,为创业精神、为对不同产品和事务的主人翁意识而招人,但同时也要为规模化而招人。因为公司在指数级增长,所以你需要你的队友也能指数级成长。如果一个人只是线性成长,到某个时点,那个差距就会变得非常大。

[22:23] **SPEAKER_02:** And then things aren't working out anymore. Do these big companies have lock-in, like the big legal tech companies?

> 到那时事情就行不通了。那些大公司,也就是大型法律科技公司,存在客户锁定效应吗?

[22:29] **SPEAKER_01:** So these big companies have a couple of advantages. But I think the disadvantages outweigh. Right. Yeah.

> 这些大公司确实有几项优势,但我认为它们的劣势更大。对,是的。

[22:34] **SPEAKER_01:** The advantages, almost 10 to 1. There were very large data advantages. And being an incumbent where you lock in a large contract. Yeah.

> 劣势与优势几乎是 10 比 1。它们曾经有非常巨大的数据优势,而且作为老牌巨头,你能锁定一份大合同。是的。

[22:45] **SPEAKER_01:** But I think the buyers have also changed aptitude here. So we're not seeing anybody want to lock in a five-year contract. Right. Because the world is moving so fast.

> 但我认为在这一点上,买方的心态也已经改变了。所以我们看不到有谁愿意签一份锁定五年的合同,因为世界变化得太快了。

[22:55] **SPEAKER_01:** Of course. Of course. So we instead see them doing one-year contracts. Sounds like a good motivation for a company who's moving faster.

> 当然,当然。所以我们看到的反而是他们在签一年期的合同。这听起来对一家跑得更快的公司来说是个很好的激励。

[23:02] **SPEAKER_01:** It is, yes. But even law firms, right? I mean, they don't want to be locked in with a vendor. So they're doing one- or two-year contracts.

> 确实如此。但即便是律所也是这样,对吧?我是说,他们也不想被某个供应商锁死,所以他们签的是一到两年的合同。

[23:09] **SPEAKER_01:** And as we see them now coming up in a lot of places, they're also looking outside of their existing alternatives. So you might have made a bet back in 2023 or 2024 when it was experimentation days. But now you're looking at, what are we going to deploy more long term? And there, what I'm seeing is, yes, people look at the technology.

> 而现在我们看到他们在很多地方冒出来时,也在把目光投向他们现有备选方案之外的东西。所以你可能在 2023 或 2024 年那种试验阶段下过一个赌注,但现在你要考虑的是:我们要更长期地部署什么?在这方面我所看到的是,是的,人们会看技术本身。

[23:30] **SPEAKER_01:** But even more so, they're zooming out, and they're looking at your rate of change. They want to work with a partner that's going to get them from point A to point B. And they can be different things. It might be, we want to be AI first and drive our top line.

> 但更重要的是,他们会拉远视角,去看你的变化速率。他们想要一个能带他们从 A 点走到 B 点的合作伙伴。而这个目标可以是不同的东西,可能是"我们想要 AI 优先并推动营收增长"。

[23:43] **SPEAKER_01:** Or we want to drive profitability and streamline our operations. It can be very different motivations. How does your tech stack look like? What's under the hood?

> 或者是"我们想提升盈利能力、精简运营"。动机可以非常不同。你们的技术栈是什么样的?引擎盖底下是什么?

[23:52] **SPEAKER_01:** Internally? Yeah. So building our infrastructure, I think, from the beginning, it was pretty clear that we wanted to be on Azure just because it was the same that our customers were on. And in the beginning, I think OpenAI and GPT was really like, oh, we're going to do this.

> 内部吗?好。在搭建我们的基础设施时,我想从一开始就很清楚我们想用 Azure,原因很简单,那正是我们客户所使用的。而一开始,我觉得 OpenAI 和 GPT 真的就是那种"哦,我们就用这个"的状态。

[24:04] **SPEAKER_01:** This is really the only model that you could serve via Azure. Now we have much more options available to us. So we use AWS, and Cloud, and Gemini, and GPT, and Mistral kind of interchangeably. The biggest thing there has been, how do we build everything in such a way where we can hot swap the models whenever we want, and also build it in such a way that the models become better, everything improves?

> 那时它真的是你唯一能通过 Azure 使用的模型。现在我们可以选择的余地大多了,所以我们会较为灵活地交替使用 AWS、Claude、Gemini、GPT 和 Mistral。其中最关键的一点是:我们如何把一切都构建成想什么时候热切换模型就能切换,同时又构建成随着模型变得更好,整个系统的一切都随之提升?

[24:28] **SPEAKER_01:** And now we've also looked into classification models where if you do a simple query, we'll serve you a simple model. If you do a complex query, we'll serve you a complex model. And that's just to keep the margins down. But also, sometimes you don't need a bazooka when you just need a water gun.

> 现在我们还研究了分类模型:如果你提交一个简单的查询,我们就给你调用一个简单的模型;如果你提交一个复杂的查询,我们就给你调用一个复杂的模型。这一方面是为了压低成本、控制利润率,另一方面也是因为——有时候你只需要一把水枪,根本用不着火箭筒。

[24:46] **SPEAKER_02:** So who is the buyer? My understanding is that law firms have, well, maybe you could explain to me. There's a bunch of partners, and there's other people there, too. How is a law firm or a legal team at a company generally constructed, and who are there, and who buys it, and who uses the software?

> 那么谁是买家?据我理解,律所有——嗯,也许你可以给我解释一下。里面有一群合伙人,还有其他人。一家律所或一家公司的法务团队通常是如何构成的?里面都有谁?谁来买单?谁又在使用这个软件?

[25:01] **SPEAKER_01:** It changes a bit depending on size. Mm-hmm. So if you start with the biggest firms, of course, you have the partner group that kind of runs things. But you very often have an innovation department, which sometimes have more or less influence.

> 这会因规模不同而有所变化。嗯。先从最大的律所说起,当然,你会有一个合伙人团体来主导大局,但你也常常会有一个创新部门,它有时影响力大一些,有时小一些。

[25:14] **SPEAKER_01:** If it's a very strong innovation department, they make their own choices. They procure software, and they're responsible for the entire innovation agenda. I frankly get the most energy out of working with the innovation folks who are really smart about these things, because there's a lot of people that just want to kind of check the AI box. Yeah.

> 如果这是一个非常强势的创新部门,他们就会自己做决定,他们采购软件,并对整个创新议程负责。坦白说,我从和那些真正懂行的创新人士打交道中获得的能量最多,因为有很多人只是想走个过场、把"AI"这个框打上钩而已。是的。

[25:33] **SPEAKER_01:** They just want to push things forward. And the interesting dilemma there is they're basically driving efficiency across the stack or across the firm. Yeah. But they're not the users themselves.

> 他们是真心想把事情往前推。这里有个有意思的两难:他们本质上是在推动整个体系、整个律所的效率提升,但他们自己并不是使用者。

[25:43] **SPEAKER_01:** Right. However, you might often have innovation practitioners that work in the M&A group or the disputes group or arbitration. And then they will work with those teams to drive an upskill. So they will have a very process-minded way of working, and then they might use Legora to build use cases for the M&A group.

> 对。不过,你常常会有一些创新实践者,他们在并购组、争议组或仲裁组里工作,然后他们会与这些团队合作,推动技能提升。所以他们会有一种非常重视流程的工作方式,并可能用 Legora 为并购组构建具体的使用场景。

[26:02] **SPEAKER_01:** Mm-hmm. Yeah. And then they might use the end users. Because when you work in a big law firm, you need to hit your billing targets.

> 嗯。是的。然后他们可能会调动终端用户。因为当你在一家大律所工作时,你必须达成你的计费目标。

[26:07] **SPEAKER_01:** Yeah. They work a lot. Yeah. We grind as startup folks, but lawyers grind as well.

> 是的。他们工作量很大。我们创业者拼命干,但律师也一样拼命。

[26:14] **SPEAKER_01:** And if you know that there's a way to solve something, and it's going to take six hours for you to do that, and you know a way how to do it in six hours, you might not take the chance of exploring a way how you could potentially solve it quicker or with a higher quality. You'll just conform to the way you're used to working. Yeah. So innovation teams have a huge opportunity and, frankly, mission to drive that across the firm.

> 如果你知道有一种办法能解决某件事,而用你熟悉的方式要花六个小时,你已经知道怎么在六个小时内完成它,你可能就不愿意去冒险探索一种也许能更快、或以更高质量解决它的新方法,你会干脆沿用你习惯的工作方式。是的。所以创新团队有一个巨大的机会,坦白说也是一项使命,去在全律所范围内推动这种改变。

[26:41] **SPEAKER_01:** And if you go down a bit, so you have mid-sized firms, more often than not, you might not have an innovation department. And so it's the partners who are making the move or the decision.

> 如果你往下走一点,到了中型律所,更多情况下你可能根本没有创新部门,所以就是由合伙人来采取行动、做出决策。

[26:51] **SPEAKER_02:** And what I've found is it's hard to get the entire partnership to buy in. Go deeper on this point. Yeah. Because I know a lot of founders is asking me, how do I sell to a financial firm or a law firm?

> 而我发现,要让整个合伙人群体都买账是很难的。就这一点再深入讲讲。好。因为我知道很多创始人都在问我:我该怎么向一家金融公司或律所销售?

[27:03] **SPEAKER_02:** Or something like that. And it seems like this is the tricky part. It's like you have to convince everybody.

> 或者类似的问题。而这似乎正是棘手的地方——你好像必须说服每一个人。

[27:07] **SPEAKER_01:** You have to convince everybody or you start smaller. You say, let's work with this partner and their team and make them rock stars. And then everybody else looks at them saying, what's that guy doing? That looks awesome.

> 你要么说服每一个人,要么从更小的范围开始。你可以说,让我们先和这位合伙人及其团队合作,把他们打造成明星。然后其他所有人看着他们,心想:那家伙在搞什么?看起来太厉害了。

[27:22] **SPEAKER_01:** We also want in.

> 我们也想加入。

[27:23] **SPEAKER_02:** And then you expand. But the key here is to sell, not top down, but sell to the senior people first. Right. So it's impossible to do a bottom-up motion.

> 然后你再扩张。但这里的关键是,销售不是自上而下,而是先卖给资深的人。对。所以做自下而上的推广是不可能的。

[27:31] **SPEAKER_01:** Yeah. It's impossible to do a bottom-up motion in our industry because you don't procure software individually. You take it through procurement and you take it through IT. And there's a lot of security checks.

> 是的。在我们这个行业里,自下而上的推广是行不通的,因为你没法以个人身份去采购软件,你必须走采购流程,走 IT 流程,而且要经过大量的安全审查。

[27:43] **SPEAKER_01:** There's a lot of data privacy checks that you need to go through in order to actually serve client data in your systems.

> 你必须通过大量的数据隐私审查,才能真正在你的系统里处理客户数据。

[27:51] **SPEAKER_02:** You were 23 when you co-founded Legora. By then, you've already done a lot. You had some stints at other YC companies, like multiple different ones. Yeah.

> 你联合创办 Legora 时才 23 岁。而在那之前你已经做了很多事,你在其他 YC 公司有过一些短期经历,而且是好几家不同的公司。是的。

[27:59] **SPEAKER_02:** What was your background before you started this company? When I was 18, I was working at a company.

> 在创办这家公司之前,你的背景是什么?我 18 岁时在一家公司工作。

[28:01] **SPEAKER_01:** Yeah. When I was 18 and it was time to apply to college, I actually had two options. I was either going to go down the route of becoming a professional Dota, Dota 2 player, or go to college. I knew this.

> 是的。我 18 岁、到了要申请大学的时候,其实我面临两个选择:要么走上成为职业《Dota》——《Dota 2》选手的道路,要么去上大学。我心里清楚。

[28:14] **SPEAKER_01:** And my thinking at the time was, okay, what's the best case scenario in each of the outcomes? So best case scenario in Dota would be to win the international, the biggest tournament in the world. You make $10 million. That would be amazing.

> 我当时的思路是:好,这两条路各自最好的结果是什么?打 Dota 的最好结果是赢得 The International,也就是世界上最大的赛事,你能赚 1000 万美元,那会非常了不起。

[28:28] **SPEAKER_01:** But then I was thinking, what happens then? Mm-hmm. Yeah. Then life stops.

> 但接着我又想,那之后呢?嗯。是啊,那之后人生就停滞了。

[28:34] **SPEAKER_01:** Yeah. And the best case scenario with going to college was basically this, what I'm doing now. So I decided to go to college. And when you apply to college in Sweden, you go to one school to do one program.

> 是的。而上大学的最好结果基本上就是眼下这个,就是我现在正在做的事。所以我决定去上大学。在瑞典,你申请大学时是去一所学校读一个专业。

[28:45] **SPEAKER_01:** So the engineering university is completely separate from the business university, which I think is really weird. Yeah. Like, we don't mix at all, which is bad. But there was a hack so that you could make an admission to one of the schools and then kind of pull the admission to make another one.

> 所以工程大学和商学院是完全分开的,我觉得这真的很奇怪。是啊,我们之间根本不交叉,这很糟糕。但有个小窍门,你可以先拿到其中一所学校的录取,然后把这个录取"撤掉"再去申请另一所。

[29:01] **SPEAKER_01:** Mm-hmm. Or pull your application to make another one, and then call them and say that you messed it up and you wanted to get it reapplied. So I ended up making it so that I could go to both universities in parallel. It was a really good timing during COVID to do that, because that means when you have two lectures at the same time, you can just have two laptops at one point.

> 嗯。或者撤回你的申请去申另一所,然后打电话给他们说你搞砸了、想重新申请。于是我最后弄成了可以同时在两所大学并行就读。在新冠疫情期间做这件事时机特别好,因为那意味着当你同一时间有两节课时,你可以在同一个地方摆两台笔记本电脑。

[29:21] **SPEAKER_01:** Or record one. Yeah. Yeah. And there were multiple times where I had exams at the same time with both universities.

> 或者把其中一节录下来。是的。有好几次我在两所大学同时有考试。

[29:28] **SPEAKER_01:** And you would kind of sit with one camera over here and one camera over here, pretending that you were just doing one of the exams. And so like one or two years into it, I was working as a programmer. I was building statistical models for esports betting, and that was really fun. But I think I also wanted to kind of see what the business side looked like.

> 你就得这边架一台摄像头、那边架一台摄像头,假装你只在参加其中一场考试。这样大概读了一两年后,我做起了程序员的工作,给电竞博彩构建统计模型,那真的很有意思。但我想我也想看看商业那一面是什么样的。

[29:46] **SPEAKER_01:** So I had the privilege of working at a company called Norsken. It's like YC, but for impact. And it's based in Stockholm. And I think I got a lot of exposure to other entrepreneurs.

> 于是我有幸在一家叫 Norrsken 的公司工作过。它有点像 YC,但专注于社会影响力,总部在斯德哥尔摩。我想我因此接触到了很多其他创业者。

[29:58] **SPEAKER_01:** And what struck me then was, one. Yeah. A few of them were not super ambitious to build companies that we're doing now. But they sort of had this five-year plan to conquer Nordics.

> 当时让我印象深刻的一点是:是的,他们中有一些人并没有那种想打造我们现在这种公司的宏大野心,而是有一个大概"五年征服北欧"的计划。

[30:09] **SPEAKER_01:** So I think immediately I had a different take on it. And then they just short-stint at McKinsey and worked at BAMLO and just one week at Depict.

> 所以我想我马上就对此有了不同的看法。然后我又在麦肯锡短暂待过,在 Bamboo 工作过,还在 Depict 只待了一周。

[30:20] **SPEAKER_02:** Depict was one of those companies, is one of those companies that was an incredible talent magnet. Yeah. Like some incredible people have come out of Depict. Like Anton from Lovable was one of the founders.

> Depict 曾是、现在也是那种极其吸引人才的公司之一。是的。从 Depict 走出了一些非常了不起的人,比如 Lovable 的 Anton 就是创始人之一。

[30:29] **SPEAKER_02:** Yeah. So you're starting with Gora, even though you spent a week there. But it's like kind of cool how you have these magnets that spun off too much about the cool

> 是的。所以你虽然只在那儿待了一周,后来还是创办了 Legora。但挺酷的一点是,你会看到这些"人才磁石"公司孵化出——这些很酷的——

[30:37] **SPEAKER_01:** companies. No, they're amazing. And we're all good friends in Stockholm. It's a small ecosystem.

> ——公司。是啊,他们都很棒。我们在斯德哥尔摩都是好朋友,这是一个小小的生态圈。

[30:43] **SPEAKER_01:** And it's really fun to kind of cheer on each other as well.

> 而且能互相加油打气,真的很有意思。

[30:48] **SPEAKER_02:** And YC ended in April last year. Can you walk us through the company growth and your personal development in this time? Like you were 10. Now you're 100.

> YC 是去年四月结束的。你能带我们回顾一下这段时间公司的成长和你个人的发展吗?你们当时是 10 个人,现在是 100 人。

[30:56] **SPEAKER_02:** What happened?

> 发生了什么?

[30:57] **SPEAKER_01:** We grew really fast. Yeah. Yeah. Yeah.

> 我们成长得非常快。是的,是的。

[31:01] **SPEAKER_01:** So we started with the drag. Yeah. We took the product to market and we would sell it in a demo. And when law firms start to buy things after one demo, you're doing something right.

> 我们是从那个"网格"功能起步的。是的。我们把产品推向市场,通过一次演示就能把它卖出去。而当律所看完一次演示就开始下单时,说明你做对了某些事。

[31:14] **SPEAKER_01:** And so the rationale was like, we should be doing more of this and we want to do it everywhere all at once. And this is also a space where it's kind of obvious that legal and LLM is a good fit. And so there were a lot of other companies in the industry. I like to say there were so many legal AI companies.

> 于是当时的逻辑是:我们应该多做这样的事,而且我们想同时在所有地方一起做。这也是一个法律与 LLM 的契合度相当明显的领域,所以行业里有很多其他公司。我喜欢说,当时法律 AI 公司多如牛毛。

[31:28] **SPEAKER_01:** Yeah. There were so many legal AI systems. And now it just feels like many of them have kind of fallen off and there are emerging a couple of winners. With that rationale, we wanted also to get American capital in the company because we wanted to be able to make the move from Stockholm to the US when the time was right.

> 是的,法律 AI 系统曾经非常之多。而现在感觉它们中许多都掉队了,开始涌现出几家赢家。基于这个逻辑,我们也想引入美国的资本,因为我们希望在时机成熟时能够从斯德哥尔摩迁往美国。

[31:46] **SPEAKER_01:** After we raised the money during our first board meeting, we sat down and I remember the look on some of our board members' faces when I basically said, we're not going to sell for the next four to five months. Yeah. And the reason for that was when we got the chance to onboard a client, it took a lot of work. It took a lot of work to get them to a level of understanding of what they could accomplish in the platform.

> 我们融到钱之后,在第一次董事会上坐下来,我记得当我基本上说出"我们接下来四到五个月都不会去做销售"时,某些董事会成员脸上的表情。是的。原因在于,当我们有机会让一个客户上手时,需要投入大量的工作,要让他们理解自己在这个平台上能完成些什么,是需要下很大功夫的。

[32:10] **SPEAKER_01:** And also the first experience of a legal professional logging in is the one chance you have. If you mess that up, they're not coming back. And we had a couple of situations where we'd onboard a lot of people and we had done some misses and we didn't want to ruin that. Yeah.

> 而且一位法律专业人士首次登录的体验,是你唯一的机会。一旦搞砸了,他们就不会再回来了。我们经历过几次情况:我们让很多人上手,但出了一些差错,而我们不想毁掉这一切。是的。

[32:28] **SPEAKER_01:** So we worked really hard on reliability, scalability, got the system to a place where we could comfortably onboard a thousand lawyers a day. And once we had that, we kind of let it rip. And that's also when we really started to hire. So we were maybe 25 in the beginning of October and just six months later, we're now a hundred.

> 所以我们在可靠性、可扩展性上下了很大功夫,把系统做到了每天能轻松让一千名律师上手的程度。一旦做到了这一点,我们就基本上开足马力了。那也是我们真正开始大量招人的时候。所以十月初我们大概是 25 人,仅仅六个月后,现在就是一百人了。

[32:49] **SPEAKER_01:** So what we did was we said, okay, we're now going to scale across every market in Europe and we're going to start scaling towards the US. And our initial conversations in the US. We decided to fail and we were like, well, we can't come up with a new network. Right.

> 于是我们的做法是说:好,我们现在要在欧洲每一个市场铺开,同时开始向美国扩张。而我们在美国最初的那些洽谈,我们决定让它"失败",我们心想,好吧,我们没法凭空建立起一个新的人脉网络。对。

[33:03] **SPEAKER_01:** So we wanted to go through and we actually took some time because we were small Swedish startup. Um, so I made multiple trips back and forth to New York and now we open up hubs, both in New York, London, Stockholm, and also people locally in Spain, France, and Germany. So we've really gone at it and just said, hey, we want to do everything everywhere all at once and let's do it now. And for you personally?

> 所以我们想把这条路走通,实际上花了一些时间,因为我们是一家瑞典小创业公司。我多次往返纽约,而现在我们在纽约、伦敦、斯德哥尔摩都设立了办事处,在西班牙、法国和德国也有当地的人员。所以我们真的是全力以赴,就是说,嘿,我们想同时在所有地方把所有事情都做了,而且现在就做。那对你个人来说呢?

[33:27] **SPEAKER_01:** Yeah. going from being an IC into delegating and that move you know you know how to do something but you that's not going to scale so you need to teach somebody else to do it and you need to hire people who are way better than you on a lot of different topics so one of the early sort of hires that we made were actually another YC founder and we've ended up Jake yeah and we actually we've scaled the team with a lot of entrepreneurs and that's not only like the skills we're looking for but it's also like the way that we built the company because we're effectively running multiple

> 是的。从一名一线执行者(IC)转变为学会授权,这个转变——你知道怎么做某件事,但那种做法没法规模化,所以你需要教会别人去做,而且你需要招募在许多不同领域都远比你强的人。我们早期招募的其中一人其实是另一位 YC 创始人,最后加入的是 Jake。事实上我们是靠很多创业者来扩充团队的,这不仅仅是我们看重的技能,也是我们构建公司的方式,因为我们实际上是在——

[34:04] **SPEAKER_02:** companies within the company it's sort of like a secret playbook that a lot of YC companies some of the best ones are all following is that the first people you want to hire all former founders yeah and it's kind of actually an advice that I got from Paul Graham back in the days is that sometimes you think you're a founder that I work in this company for three years didn't go well am I less attractive in the job market like if you're here or if you're in a startup Center you're actually more attractive in the job market because people actually want to work with

> ——在公司内部运营着多家公司。这有点像很多 YC 公司、其中一些最优秀的公司都在遵循的一本"秘籍",那就是你最先想招的人全都是前创始人。是的。这其实也是我当年从 Paul Graham 那里得到的一条建议:有时你会觉得,作为一个创始人,我在这家公司干了三年却没成功,那我在就业市场上是不是就没那么抢手了?但其实,如果你在这里、或者你在一家创业公司里,你在就业市场上反而更抢手,因为人们真的愿意和——

[34:28] **SPEAKER_01:** people like you yeah and we want to hire them so yeah um it's been amazing and also the agency and the the attitude to problem solving that's kind of what you're looking for and then sometimes you need to hire for scale right like now we have a significant sales team and you need somebody who's seen the hundred you know 10 million to 500 million because that's the journey that we're

> ——像你这样的人共事。是的,而我们也想招他们,所以这太棒了。还有那种主观能动性、那种解决问题的态度,那正是你要找的。当然有时你也需要为规模化而招人,对吧,比如现在我们有一支相当规模的销售团队,你需要那种见识过从 1000 万到 5 亿这一百倍增长历程的人,因为那正是我们正在——

[34:51] **SPEAKER_02:** on and my learning from Airbnb which probably I'm sure applies to you is the culture in the

> ——经历的旅程。而我从 Airbnb 学到的、我几乎确定同样适用于你们的一点是,公司里的文化——

[34:54] **SPEAKER_01:** company is the people that you hire of course yeah and when we've now scaled the hubs um we always send a person from Stockholm with them it's the best people from the Stockholm office

> ——就是你所招募的那些人。当然,是的。而当我们现在拓展这些办事处时,我们总会从斯德哥尔摩派一个人一同前往,而且是斯德哥尔摩办公室里最优秀的人——

[35:03] **SPEAKER_02:** that then travels and setups the new hubs you seem like the kind of person who embodied the attributes you can just do things so can you tell me how that is reflected in your company

> ——去出差并建立起新的办事处。你看起来就是那种身上体现着"你其实可以直接去做事"这种特质的人。那你能告诉我这一点在你的公司里是如何体现的吗?

[35:11] **SPEAKER_01:** you can't just do things and when we started building this company we didn't know anything about law right I think that was pretty apparent in our first interview and we you know made the right moves from them um from them to the second one where we showed that we could do it you applied for two different batches yeah the first one didn't go as well and so about this attribute it's something I look for in others as well um during a lot of the interviews I do I ask I often ask the question you know what have you done outside of your role for the company yeah and here I'm looking for creativity ability to spot problems and solve them yeah and to take responsibility for more things than just the stuff that you're doing right right and I think in terms of starting companies and you know building the future because frankly we need to reimagine a lot of like the stuff that we're doing we don't want people who are bogged down by your boss telling you to do something right we have a very sort of flat organization where let's say our marketing team we want generalists who are using AI to do 10x more work than they could have done in the past and where you might have needed a person marketing team you now need five and you want those five people then to be complete you know yes sayers and to go out you know above and beyond and that characteristic I think is increasingly important as well in an in an age where if you're really ambitious you can get a

> "你其实可以直接去做事",而当我们开始创办这家公司时,我们对法律一无所知,对吧?我想这在我们第一次面试时就相当明显了,然后我们从第一次到第二次做出了正确的动作,证明了我们能做到。你申请了两个不同的批次。是的,第一次没那么顺利。说到这个特质,它也是我在别人身上寻找的东西。在我做的很多面试中,我常常会问一个问题:除了你分内的职责之外,你还为公司做过什么?在这里我看重的是创造力、发现问题并解决问题的能力,以及为更多事情、而不仅仅是你手头分内之事承担责任的意愿。我觉得就创办公司、构建未来而言——因为坦白说,我们需要重新想象我们正在做的很多事情——我们不想要那种被老板指派任务束缚住的人。我们的组织非常扁平,比如说我们的营销团队,我们想要那种利用 AI 把过去能完成的工作量做到十倍的通才。过去你可能需要一个人组成营销团队,而现在你需要五个人,你希望这五个人是彻头彻尾的"能行者",愿意超额付出、超越预期。我认为在这样一个时代——如果你真的有雄心,你就能获得——这种特质也变得越来越重要——

[36:43] **SPEAKER_02:** lot of leverage out of tools absolutely so if we fast forward like five or ten years uh how does

> ——从工具中获得巨大的杠杆效应。完全正确。那么如果我们快进五年或十年,一名律师的日常工作会——

[36:49] **SPEAKER_01:** the day-to-day job of a lawyer look like that's interesting we think about that a lot right um I'm kind of viewing it as you're more and more entering a workspace of reviewing work than actually doing it and you are managing the expectations from your clients and the expectations and the work from your AI agents right you're effectively instructing them you're watching them go out and do work and you're making sure that everything they're doing is not only correct and sort of at your standard but you're also managing how that work gets delivered to the clients because I think you know you you will always want somebody who knows their stuff yes on this and there's a big reason for why we're working with lawyers and not with the people who might you know use the legal services because the lawyers needed and necessary to deliver the end product but looking five ten years ahead in in these days is also it's hard it's hard right um if I knew where the amls would be 10 years from now yeah we're looking weeks ahead now right yeah it's and and that's funny just with our product roadmap

> ——是什么样子?这很有意思,我们经常思考这个问题。我大致是这样看的:你会越来越多地进入一种审阅工作、而非亲自执行工作的工作状态。你要管理来自客户的期望,也要管理来自你 AI agent 的期望和产出。你实际上是在给它们下达指令,看着它们出去干活,确保它们所做的一切不仅正确、达到你的标准,同时你还要管理这些成果如何交付给客户。因为我觉得,你永远都需要一个真正懂行的人来把关。这也是我们选择与律师合作、而不是与那些可能会使用法律服务的人合作的一个重要原因——因为要交付最终产品,律师是必需且不可或缺的。但要展望五年、十年之后,在如今这个时代也确实很难,很难,对吧?如果我知道 LLM 十年后会走到哪一步就好了。我们现在只能往前看几周。是啊,这挺好笑的,单说我们的产品路线图——

[37:54] **SPEAKER_02:** borders ahead yeah yeah it's hard it's really hard do you think uh that the large al labs are

> ——就只能提前几周规划。是啊,这很难,真的很难。你认为那些大型 AI 实验室会——

[38:01] **SPEAKER_01:** going to try to attempt at doing law maybe not law specifically but I I do feel like they're more and more becoming platform companies rather than model providers I mean Google is building Google workspace with Gemini Anthropic is running very hard on the mcp idea of building kind of a universal entry point into a lot of applications I think the the expectations on companies like us are pretty clear you know whatever comes out of a model lab it's kind of expected and then everything else we're adding on top is kind of like icing on the cake how does it feel to have product market fit I think the feeling is best summarized by almost like this drag feeling or kind of Infinite you've been pulled into the market right um it's like it literally feels like we have infinite demand and I think that's it's coming from a point of the product is working and it's moved from being in this experimental AI bucket yeah into we are reliant on this for core work that we are delivering right now if something breaks you know immediately we get a phone call say hey we can't do this like what's going on right and we fix it it's basically been this point of you start out you hope that what you're doing is the right thing and you try to get early partners excited about what you're doing and in the beginning to be you know really Frank a lot of people got on with us because they wanted to be on the journey and they took a bet yeah and I am so thankful and happy that they did that because now we've taken them from from point A to point B and we're continuously scaling from here so we tell wise

> ——尝试进军法律领域吗?也许不是专门做法律,但我确实感觉它们正越来越多地变成平台型公司,而不只是模型提供商。我是说,谷歌正在用 Gemini 打造 Google Workspace,Anthropic 正大力推进 MCP 这个理念,也就是构建一个通往众多应用的通用入口。我认为对我们这类公司的期望是相当明确的:模型实验室做出来的任何东西,那都是意料之中、理所应当的,而我们在此之上叠加的一切,就像是蛋糕上的糖霜。拥有产品市场契合(PMF)是什么感觉?我想这种感觉最好的概括几乎就是那种被"拖拽"的感觉,或者说一种被市场无限拉扯进去的感觉。真的,字面意义上感觉我们有着无限的需求。我认为这源于产品真正起作用了,它已经从那个"实验性 AI"的桶里,转变为"我们正依赖它来完成当下正在交付的核心工作"。现在一旦出了什么故障,我们立刻会接到电话说:嘿,我们干不了活了,怎么回事?然后我们去修复它。这基本上就是那种历程:一开始你希望自己所做的是正确的事,你努力让早期合作伙伴对你正在做的东西感到兴奋。坦白说,一开始很多人愿意和我们一起干,是因为他们想参与这段旅程,他们下了一个赌注。我非常感激也非常高兴他们这么做了,因为如今我们已经把他们从 A 点带到了 B 点,并且从这里继续持续扩张。所以我们建议——

[39:36] **SPEAKER_02:** companies to move to San Francisco generally uh you decided to not take that advice can you just like tell us a bit about the thinking here and maybe like if you have some pros and cons yeah

> ——公司一般都搬到旧金山去,而你决定没有采纳这个建议。你能不能跟我们讲讲这背后的思考,也许再说说你觉得——是的——

[39:46] **SPEAKER_01:** about not being here yeah the reason why we stayed in Stockholm was um we needed a market to grow in and if you go to the US it's not only more competitive but I think it kind of pushes you into becoming a more narrow company you start building really horizontal and then you realize wait a minute we're really good at this so you start to scale it in other markets and you quickly notice ah we're the best in Finland too we're the best in Denmark and we're the best in Norway and then you scale to Spain France and Germany London and then the States yeah and at that point we had always you know we had already done um in new market entries the algorithm where the the method was already kind of established of course the US is a bigger undertaking but we had also then grown from this small fish in a small

> ——不待在这里(旧金山)有哪些利弊。是的,我们留在斯德哥尔摩的原因是,我们需要一个可以成长的市场。如果你去美国,那里不仅竞争更激烈,我觉得它还会把你推向成为一家更"窄"的公司。你一开始做得很横向(通用),然后你意识到,等一下,我们在这方面真的很擅长,于是你开始把它推广到其他市场,你很快发现,啊,我们在芬兰也是最好的,在丹麦是最好的,在挪威也是最好的,然后你扩张到西班牙、法国、德国、伦敦,再到美国。而到那时,我们在进入新市场方面已经形成了一套算法,方法论已经基本成型了。当然,美国是一项更大的工程,但那时我们也已经从一条小池塘里的小鱼——

[40:37] **SPEAKER_02:** pond to crocodile or a shark in the bigger pond now so you you've raised 80 million dollars like in mid-May you open an office in New York uh you launched with one of the most famous law firms here in the US yeah um it seems like you're trying to position yourself as the category leader of AI

> ——成长为如今更大池塘里的一条鳄鱼或鲨鱼了。所以你在五月中旬融了 8000 万美元,在纽约开设了办公室,和美国这里最著名的律所之一一起上线。看起来你是在努力把自己定位为 AI 法律领域的品类领导者。

[40:54] **SPEAKER_01:** 100 and I think in many aspects we're already there it's for me more of a question around ambition and what's next it's very easy to say hey we see this problem let's go solve it and then you get satisfied but it feels to me like every time we solve a problem a new one emerges right and we're finding that as we go deeper and deeper and deeper in the entire legal software stack we're also seeing that the line between software and service is blurring AI is continuously developing super super quickly and that means we need to do the same and so in my mind the category leader in the space does not only build software they serve as the strategic partner to these large firms and they make them win in this transition because it's a very large transition and that's also why we've basically scaled headcount as as quickly as we've could

> 百分之百,而且我认为在许多方面我们已经做到了。对我来说,更多的是一个关于野心以及"下一步是什么"的问题。你很容易说,嘿,我们看到了这个问题,那就去解决它,然后你就满足了。但对我而言,似乎每次我们解决一个问题,一个新的问题又会冒出来。我们发现,随着我们在整个法律软件栈里钻研得越来越深,软件与服务之间的界限也在变得模糊。AI 在持续地飞速发展,这意味着我们也必须跟上同样的速度。所以在我看来,这个领域的品类领导者不仅仅是构建软件,他们还要充当这些大型律所的战略伙伴,让他们在这场转型中胜出,因为这是一场非常巨大的转型。这也是为什么我们基本上是以尽可能快的速度扩充人员规模——

[41:55] **SPEAKER_02:** maintaining kind of culture urgency and velocity so a lot of founders that I I meet are asking me questions about how you build a vertical AI company that seems like the kind of companies people are building now do you have any general advice you want to give to those founders who are just

> ——同时维持那种文化、紧迫感和速度。我遇到的很多创始人都在问我,如何打造一家垂直领域的 AI 公司,这似乎正是当下人们在创办的那类公司。你有什么想给那些刚起步的创始人的通用建议吗?

[42:07] **SPEAKER_01:** starting out the first kind of obvious tip is don't get locked in with a provider and don't compete with the AI labs the AI labs ship right and so does companies like perplexity and others and so I think you want to be really clear and honest to yourself where you're adding value and where you're adding long-term mode and this is something that we've thought a lot about at laguard like how do we build things as boats so that when the tide rises just everything gets better if you're just starting out you got to realize that you do not have the capacity to

> 第一个比较显而易见的建议是:不要被某个供应商锁死,也不要去和 AI 实验室竞争。AI 实验室在不停地发布新东西,像 Perplexity 这样的公司以及其他公司也是如此。所以我认为你要非常清楚、非常诚实地面对自己:你到底在哪里创造价值,又在哪里构建长期的护城河。这也是我们在 Legora 反复思考的问题:我们如何把东西造成"船",这样当潮水上涨时,一切都会随之变好。如果你刚起步,你必须认识到,你没有能力——

[42:39] **SPEAKER_02:** outperform any of those companies you can't have to find a narrow category to do it where you know

> ——去超越那些公司中的任何一家。你必须找到一个足够窄的细分品类去做,一个你知道——

[42:45] **SPEAKER_01:** the miles won't get to or either that or finding out a way to leverage the models very creatively I mean in a way that others haven't done it I think take AI scribing yeah it's a good idea it's a good one like typical AI scribing is hard to do and you need to embed a lot of like custom prompts and ways to get it right so that it uses the right medical language which is very similar to law like you needed to write clauses in a way that a lawyer would write a clause right not just

> ——那些模型(大厂)不会触及的领域;要么就是找到一种非常有创意地利用这些模型的方法,一种别人还没做过的方法。就拿 AI 医疗记录(AI scribing)来说,这是个好点子。典型的 AI 医疗记录很难做,你需要嵌入大量定制化的提示词和各种方法来把它做对,让它使用正确的医学语言——这和法律非常相似,你需要以律师撰写条款的方式来写条款,而不仅仅是——

[43:12] **SPEAKER_02:** what the model spits out as the most probable answer if I'm watching this video and I'm like I'm thinking about applying for a job at legora yeah uh tell me about what I should expect either from the application process or from working there the things that

> ——照搬模型吐出的那个概率最高的答案。如果我正在看这个视频,心里在想着申请 Legora 的一份工作,那么请告诉我,无论是从申请流程还是从在那里工作,我应该期待些什么?我们所——

[43:25] **SPEAKER_01:** we look for are ambition and the willingness to say we got this huge problem there's this huge mountain how do we climb it and we're also very upfront with candidates that this is not a nine to five and we're not the traditional Swedish working environment we have the good stuff we have the fika but we we have a lot more hunger and you know frankly a lot higher expectations and we we want that not only for ourselves but for each other because we want to grow as people and we want to grow as entrepreneurs and as a company as leaders and I think they're just looking at like our our application process the biggest thing we do is a lot of cases right if you want to come in and work in our go-to-market team you need to come and pitch us our product and you need to do a really strong pitch and you know if you take the engineering team we basically ask you to build a poc of legora and you know we want you to work with AI generated code but we also want you to be able to explain it yeah right and to design systems that scale and I think Stockholm is a small ecosystem and so it's also quite easy to make references and see who's actually good and who's who who's been in a company and made them a success you know not only was there at the right time exactly and another really big piece is we're hiring all over Europe so um we've had people move from Madrid from Amsterdam from Germany from Paris all the way to Stockholm we tend to not onboard them in November when it gets nasty but I feel like we've started to build this sort of AI hub together with many other companies that is not only like super fun but also you know great companies come out of it thank you so much for coming back to YC thanks Gustav

> ——寻找的是野心,以及那种敢于说"我们面前有一个巨大的问题,有一座巨大的山,我们该如何攀登它"的意愿。我们对候选人也非常坦诚:这不是一份朝九晚五的工作,我们也不是传统的瑞典式工作环境。我们保留了好的部分,我们有 fika(下午茶歇),但我们有多得多的饥饿感,坦白说,也有高得多的期望。我们不仅对自己有这样的期望,也对彼此有,因为我们想作为个人成长,想作为创业者、作为一家公司、作为领导者不断成长。再说我们的申请流程,我们做得最多的一件事就是大量的案例实操。如果你想进来加入我们的市场拓展团队,你需要来向我们推介我们自己的产品,而且要做一场非常有力的推介。如果是工程团队,我们基本上会请你构建一个 Legora 的概念验证,我们希望你使用 AI 生成的代码,但我们同时也希望你能够解释它,并且能设计出可扩展的系统。我觉得斯德哥尔摩是一个小生态圈,所以做背景调查、看清谁是真正有能力的、谁曾在一家公司里并让它取得成功——而不仅仅是恰好在对的时间待在那里——也相当容易。没错。另一个非常重要的部分是,我们在全欧洲招人,所以我们有人从马德里、阿姆斯特丹、德国、巴黎一路搬到斯德哥尔摩。我们倾向于不在十一月天气变糟时让他们入职。但我感觉我们已经开始和许多其他公司一起,共同打造起一个 AI 中心,这不仅超级有趣,而且从中还会诞生出伟大的公司。非常感谢你重返 YC。谢谢你,Gustav。
