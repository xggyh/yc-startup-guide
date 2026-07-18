# 全文转录 · 微调的强力替代方案:给 LLM 装上"高跷"的递归自我改进

> ▶ [YouTube](https://www.youtube.com/watch?v=UPGB-hsAoVY) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/UPGB-hsAoVY.md) &nbsp;·&nbsp; The Powerful Alternative To Fine-Tuning

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_04:** The world is changing so quickly. This is probably a little bit obvious, but you should just try things. And like every day, do something with AI. Last summer, I took a weekend and used GPT-5 to help me build an iPhone app. I hadn't done that in a decade.

> 世界变化得太快了。这话说出来可能有点显而易见,但你就应该去动手尝试各种东西。差不多每天都用 AI 做点什么。去年夏天,我花了一个周末,用 GPT-5 帮我做了一个 iPhone 应用。我已经有十年没干过这种事了。

[00:17] **SPEAKER_04:** So fast. Yeah, it's so fast and so easy. And that was, you know, an age ago. That was like eight months ago. Now it's even faster and easier.

> 太快了。是啊,又快又简单。而那已经是很久以前的事了,大概八个月前吧。现在比那时候还要更快、更容易。

[00:24] **SPEAKER_04:** Don't limit yourself. Like anything that you imagine, you should just try to use AI and see how far you can get with it. And you'll be making the world better.

> 别给自己设限。任何你能想象到的东西,你都应该试着用 AI 去做,看看你能借助它走多远。而且你会因此让这个世界变得更好。

[00:40] **SPEAKER_02:** Welcome to another episode of The Light Cone. Ian Fisher is the co-founder and co-CEO of Poetic, which is building recursively self-improving AI reasoning harnesses for LLMs. Previously, he spent a decade as a researcher at Google DeepMind and founded a mobile dev tools company through YC years ago. Welcome, Ian. Thank you. I'm so happy to be here.

> 欢迎收看新一期的 The Light Cone。Ian Fisher 是 Poetic 的联合创始人兼联合 CEO,这家公司正在为大语言模型打造可递归自我改进的 AI 推理框架(harness)。此前,他在 Google DeepMind 做了十年研究员,更早些年还通过 YC 创办过一家移动开发工具公司。欢迎你,Ian。谢谢。我很高兴能来到这里。

[01:01] **SPEAKER_02:** What is Poetic? How's it different than RL? You know, how's it different than context engineering?

> Poetic 是做什么的?它和强化学习(RL)有什么不同?还有,它和上下文工程(context engineering)又有什么不同?

[01:06] **SPEAKER_04:** At Poetic, what we're building is a recursively self-improving system. And so recursive self-improvement is this, you know, kind of the holy grail of AI where the AI is making itself smarter. The core insight that we had is that we could do recursive self-improvement far faster and cheaper than all of the other ways that people had been proposing to do this. And so obviously, I can't go into details about what that is, what our particular approach is. But most of the approaches out there involve, you know, they require you to train a new LLM from scratch.

> 在 Poetic,我们打造的是一个可递归自我改进的系统。递归自我改进可以说是 AI 领域的圣杯——让 AI 不断把自己变得更聪明。我们的核心洞见在于:我们能够以远比其他人所提出的所有方法都更快、更便宜的方式来实现递归自我改进。显然,我没法详细讲我们具体的做法是什么。但市面上大多数方法都要求你从头训练一个全新的大语言模型。

[01:43] **SPEAKER_04:** And training LLMs from scratch costs, you know, hundreds of millions of dollars and takes months of effort. And so the...

> 而从头训练大语言模型的成本高达数亿美元,还要耗费好几个月的功夫。所以说……

[01:49] **SPEAKER_02:** And then Anthropic or OpenAI will come along and just eat your lunch in the next model release.

> 然后 Anthropic 或者 OpenAI 一出手,在下一代模型发布时就把你的饭碗给端了。

[01:53] **SPEAKER_04:** Right, right. And, you know, of course, Anthropic and OpenAI and Google, they're exploring recursive self-improvement, but typically at that level of having the, you know, having to train a new model, they're looking for every step of self-improvement that they do.

> 对,没错。当然了,Anthropic、OpenAI 和 Google 也都在探索递归自我改进,但通常都是在那种得训练一个全新模型的层面上,他们每走一步自我改进都是这么干的。

[02:07] **SPEAKER_02:** I mean, that seems like actually the, like, defining thing that a startup really, really wants. Like, I know that I want to take advantage of whatever the next model is, but the second you're in fine-tuning land, I'm spending, you know, millions to hundreds of millions of dollars. And then guess what? Like, I just lit it on fire because, you know, the next version of the frontier model comes out, and I'll never catch up. Whereas, like, working with your systems means that I will always have the thing that is best for me.

> 我是说,这其实正是一家创业公司真正、真正想要的那种决定性的东西。比如说,我知道我想充分利用下一代模型,不管它是什么;但你一旦进入微调(fine-tuning)那套路子,我就得花上几百万到几亿美元。然后你猜怎么着?这些钱基本等于打了水漂,因为下一版前沿模型一出来,我就永远追不上了。而用你们的系统就意味着,我永远都能拥有对我而言最好的那个东西。

[02:35] **SPEAKER_02:** Better than the thing that's out of box. And that's sort of like the Holy Grail.

> 比开箱即用的那个还要好。这差不多就是圣杯了。

[02:39] **SPEAKER_04:** Yeah, we think that this is incredibly valuable to anybody who's building on top of large language models. And we don't view the, you know, the frontier models as competitors. They're, you know, they're the ones that were using the stilts, you know, building stilts to stand on top of. But if we didn't have that foundational layer, then, you know, Poetic couldn't exist.

> 是的,我们认为这对任何在大语言模型之上做开发的人来说都极具价值。而且我们并不把那些前沿模型视为竞争对手。它们更像是我们踩的高跷——我们造高跷,然后站在它们之上。但如果没有那一层地基,Poetic 也就不可能存在。

[02:59] **SPEAKER_02:** Yeah, I mean, being the smartest model, you know, it's a game of inches, actually. And, like, so those inches matter. They matter a lot. Right, right. How do we actually get started?

> 是啊,我是说,要当最聪明的那个模型,其实是一场以毫厘论输赢的比拼。所以那一点一滴的差距很重要,非常重要。对,没错。那我们究竟该怎么上手呢?

[03:08] **SPEAKER_02:** I mean, you've built something that basically any startup could use that it's sort of like stilts, really.

> 我的意思是,你们做出来的这个东西基本上任何创业公司都能用,它真的就像高跷一样。

[03:15] **SPEAKER_04:** We have built a system that can automatically generate systems for your particular problem that will always outperform the underlying language models. And without kind of the massive expense, as you're saying, about the bitter lesson, where, you know, what would you have done without Poetic? You probably would have said, OK. We're going to first collect a large data set, you know, like tens of thousands of examples for our particular problem that we're working on. And we're going to fine-tune, you know, the best model we can get our hands on.

> 我们打造了一个系统,它能针对你的具体问题自动生成一些系统,而且这些系统总能胜过其底层的语言模型。同时也不会带来你刚才提到的、和"惨痛教训"(the bitter lesson)有关的那种巨额开销。你想想,要是没有 Poetic,你会怎么做?你大概会说:好,我们先收集一个大的数据集,比如针对我们正在攻克的那个具体问题,弄上几万条样本。然后我们再拿手头能搞到的最好的模型来做微调。

[03:45] **SPEAKER_04:** Maybe that's, you know, one of the frontier models, or maybe it's an open weights model. It doesn't particularly matter. You're going to spend a lot of money on that fine-tuning. The compute is so expensive. And then at the end of it, you have something that, you know, works better than the thing that you fine-tuned on top of.

> 也许那是某个前沿模型,也许是一个开放权重(open weights)的模型,这其实无所谓。你会在那次微调上花掉一大笔钱,算力太贵了。到最后,你确实得到了一个比你拿来微调的那个基础模型效果更好的东西。

[04:00] **SPEAKER_04:** But by then, a new model has come out. And it's better than the thing that you fine-tuned on top of. It's better than the thing that you fine-tuned. You know, you fine-tuned, you know, like three years ago on top of GPT-3.5 or whatever.

> 但到那个时候,又一个新模型已经问世了,而它比你拿来做微调的那个基础模型还要好,也比你微调出来的成果还要好。你想想,你可能是三年前在 GPT-3.5 之类的模型上做的微调。

[04:10] **SPEAKER_04:** And then GPT-4 comes out, and it just blows you out of the water. And so are you going to do that again? Or are you going to go out of business? And like, in some cases, the latter. With Poetic, what we end up giving you is a, you know, people are calling these things harnesses now.

> 然后 GPT-4 一出来,直接把你打得溃不成军。那你是要再从头做一遍呢,还是干脆关门倒闭?在某些情况下,结果就是后者。而有了 Poetic,我们最终交付给你的是——现在大家把这类东西叫做 harness(框架/挂载装置)。

[04:26] **SPEAKER_04:** But, you know, or an agentic system, or whatever you want to call it, that sits on top of one or more language models. And it performs better than them. And when the new model comes out, that same harness is perfectly compatible with it. And you don't need to change anything to get the, you know, an even bigger performance bump. Additionally, we can, you know, continue to optimize for this new model, whatever the new model is that you want to use, and, you know, make it even better.

> 或者叫它一个 agent 式的系统,随便你怎么称呼,它架设在一个或多个语言模型之上,而且表现得比这些模型更好。当新模型出来时,同一个 harness 与它完美兼容,你什么都不用改,就能获得更大的性能提升。此外,我们还可以针对这个新模型继续优化——不管你想用的新模型是哪个——把它做得更好。

[04:56] **SPEAKER_04:** But you don't lose out on, you know, hundreds of millions of dollars. In fact, we do this so much more cheaply. Yeah.

> 但你不会因此损失掉几亿美元。事实上,我们做这件事要便宜得多。是的。

[05:03] **SPEAKER_02:** Than fine-tuning would cost, as well. And you've done this actually a bunch of times, right? Like, I remember when you first came out with your paper in December of last year, you shot to the top of Arc AGI v2. And then you've done this a bunch of times for other benchmarks, too. What was that like?

> 也比微调的成本便宜得多。而且你们其实已经这么干过好多次了,对吧?我记得去年十二月你们第一次发表论文的时候,就一举登上了 Arc AGI v2 的榜首。之后你们在其他基准测试上也做到过好几次。那是种什么样的体验?

[05:19] **SPEAKER_04:** Arc AGI v2 was a, this was kind of, you know, us coming out of stealth, letting people know that we could tackle these really hard problems. And in particular, you know, we wanted to show that our system could generate these, you know, these problems. And so, I mean, that was the first step. Yeah. Awesome.

> Arc AGI v2 可以说是我们结束隐身状态、正式亮相的时刻,让大家知道我们能攻克这些真正的难题。特别是,我们想展示我们的系统能够生成这些……嗯,这些解法。所以说,那是第一步。是的。很棒。

[05:32] **SPEAKER_04:** generate these, what we call, you know, we call our system like the poetic metasystem, can generate reasoning systems that are highly effective. Gemini 3, DeepThink had just come out and they were, you know, really quite dramatically at the top of the leaderboard at 45%. And two days later, we released our results where we were showing that we could get

> 生成这些……我们把我们的系统称为 Poetic 元系统(metasystem),它能生成非常高效的推理系统。当时 Gemini 3 DeepThink 刚刚发布,以 45% 的成绩相当惊人地高居排行榜榜首。两天后,我们发布了自己的结果,表明我们能拿到——

[05:57] **SPEAKER_02:** a lot higher than that. So they come out with SOTA and then you come in right above them every single time. Yeah. Like wild to see, honestly. That's what it's like to have stilt, you know, like whatever model comes out, you can be taller than that one with poetic, which is like, that's

> ——比那高出一大截的成绩。所以他们一发布出当前最高水平(SOTA),你们每一次都能恰好压在他们头上。是的。说实话,看着都觉得离谱。这就是有了"高跷"的感觉——不管什么模型出来,借助 Poetic 你都能比那个模型站得更高,这实在是……

[06:13] **SPEAKER_04:** so awesome. Yeah. So the interesting thing is that we were half the cost of Gemini 3, DeepThink because we were building on top of Gemini 3 Pro, which is a much cheaper model. But we still got in the end, a nine percentage point improvement. On the official verification. So they were at 45% and we were and like 70 something dollars and

> ……太棒了。是的。有意思的是,我们的成本只有 Gemini 3 DeepThink 的一半,因为我们是构建在 Gemini 3 Pro 之上的,而那是个便宜得多的模型。但我们最终还是在官方验证上拿到了 9 个百分点的提升。他们是 45%、每题 70 多美元,而我们——

[06:33] **SPEAKER_04:** we were at 54% and $32 per problem. So recently you guys just announced some incredible results

> ——是 54%、每题 32 美元。那么最近你们刚刚公布了一些相当惊人的结果——

[06:40] **SPEAKER_01:** for Humanity's last exam. Can you tell us more about those? Humanity's last exam is a set of

> ——是关于"人类最后的考试"(Humanity's Last Exam)的。能给我们多讲讲吗?"人类最后的考试"是一套——

[06:47] **SPEAKER_04:** 2,500 really, really hard questions written by experts in many different domains. They're meant to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for PhDs in those fields. AI

> ——2500 道真的非常非常难的题目,由许多不同领域的专家出题。它们的设计目标是,即便对那些不会做的人来说也具有挑战性——甚至对那些领域里的博士来说都很有挑战性。AI——

[06:59] **SPEAKER_04:** hasn't passed it yet, but we got to 55%, which is almost two percentage points higher than the the previous state-of-the-art. Which came out just last week from Anthropic with Claude Opus 4.6. They got 53.1% and we got 55% on it. And one thing that Humanity's last

> ——还没能通过它,但我们做到了 55%,比之前的最高水平(state-of-the-art)几乎高出两个百分点。之前那个纪录是上周才由 Anthropic 用 Claude Opus 4.6 创下的,他们拿到 53.1%,而我们在这上面拿到了 55%。还有一点是"人类最后的考试"——

[07:21] **SPEAKER_01:** exam doesn't publish is the cost of getting those results. In your case, this run, run was done with less than around six figure. How much was it?

> ——这个考试没有公布的一件事,就是取得这些成绩的成本。就你们而言,这一次运行的花费不到六位数左右。具体是多少?

[07:31] **SPEAKER_04:** MARK MANDELBACHER- We didn't publish any cost for this, but I can say that the optimization costs us less than $100,000, yeah.

> 这次我们没有公布任何成本,但我可以说,这次优化花掉我们不到 10 万美元,是的。

[07:38] **SPEAKER_01:** MELANIE WARRICK- Which is impressive, because each of these big foundation modeled train runs are in the hundreds of millions of dollars. And you guys, as a company, you're only seven people?

> 这很了不起,因为那些大型基础模型的每一次训练动辄就是数亿美元。而你们整个公司只有七个人?

[07:49] **SPEAKER_04:** MARK MANDELBACHER- That's right, yeah. Seven research scientists and research engineers, yeah.

> 没错,是的。七位研究科学家和研究工程师,对。

[07:53] **SPEAKER_01:** MELANIE WARRICK- That's impressive. And I think the thing that's very interesting about your approach is sort of taking a very scientific approach to the emergent behaviors that a lot of the best founders are doing with models. I think a lot of founders that get very good results for agents, they treat the underlying model as a common layer that you can switch in between. And there's a certain task, for example, for GPT 5.2, like very hard to verify bugs get sent to that, versus architecture that gets sent to clot 4.2.

> 这很厉害。我觉得你们的方法非常有意思的一点在于,你们用一种非常科学的方式,去对待很多顶尖创始人在使用模型时所做的那些"涌现行为"。我想,很多在 agent 上做出很好效果的创始人,都把底层模型当作一个可以来回切换的通用层。比如说,某类任务——像那些很难验证的 bug——会被派给 GPT-5.2,而架构设计则被派给 Claude 4.2。

[08:25] **SPEAKER_01:** Or 4.6. But you're kind of doing this automatically, instead of having a human conducting, is very impressive. I think there's something more special going on underneath. Can you tell us a bit about how it works?

> 或者 4.6。但你们某种程度上是自动完成这种调度的,而不是靠一个人在那儿指挥,这非常了不起。我觉得底下还有些更特别的东西在运作。能给我们讲讲它是怎么工作的吗?

[08:37] **SPEAKER_02:** MARK MANDELBACHER- Yeah, it sounds magical. So what can you tell us?

> 是啊,这听上去很神奇。那你能跟我们透露些什么?

[08:40] **SPEAKER_04:** MARK MANDELBACHER- Right, so you're getting at a core, a really core thing. These harnesses, they are code, prompts, data, built on top of one or more language models. And so this is something that, in principle, you can build by hand. Or with like cloud code, or whatever. But in practice, it takes a lot of work to do these, to have all the insights to make these work well.

> 对,你说到了一个核心、非常核心的点。这些 harness,它们本质上就是代码、提示词(prompt)、数据,构建在一个或多个语言模型之上。所以原则上,这是你可以手工搭建的东西,或者用类似 Claude Code 之类的工具搭建。但实际操作中,要做出这些东西、要具备让它们运行良好所需的全部洞见,是需要投入大量工作的。

[09:07] **SPEAKER_04:** And so the core technology that we've developed at Poetic is recursive self-improvement. So we have a recursively self-improving system, which we call the Poetic Metasystem. The output of that system is systems that solve hard problems, where a hard problem is something that, if you can solve it, you can solve it. If you gave it to GPT-5-2, it would struggle to give you a reliable, robust result, just to use an example. So this is a very big advantage for us.

> 所以我们在 Poetic 开发出的核心技术就是递归自我改进。我们有一个可递归自我改进的系统,我们称之为 Poetic 元系统。这个系统的产出,是一些能够解决难题的系统;而所谓难题,举个例子来说,就是那种如果你把它交给 GPT-5.2,它也很难给出可靠、稳健结果的问题。所以这对我们来说是一个非常大的优势。

[09:35] **SPEAKER_04:** We can generate these systems in a much more automated manner, which means that we can do it much more quickly and much more cheaply than if you hired a team yourself to try to make your own agent to solve your particular task. But not only that, since this is really an automated optimization process. If you already have done that work, you're a startup that's going after a particular vertical, and you think you understand your problem pretty well, you've put together your agent, and maybe it's working pretty well, but you know you can get something better or you really need something better, then you can bring that to us. And we can optimize that entire agent or pieces of that agent. We could optimize just the prompts, just the reasoning strategies.

> 我们能以自动化程度高得多的方式生成这些系统,这意味着相比你自己雇一个团队、去打造你自己的 agent 来解决你那个具体任务,我们能做得快得多、也便宜得多。但不止如此,由于这本质上是一个自动化的优化过程,如果你已经做完了那部分工作——你是一家瞄准某个垂直领域的创业公司,你自认为对自己的问题相当了解,你已经搭好了你的 agent,也许它运行得还不错,但你知道你能拿到更好的效果,或者你确实需要更好的效果——那你就可以把它拿来交给我们。我们可以优化整个 agent,也可以只优化 agent 的某些部分。我们可以只优化提示词,只优化推理策略。

[10:22] **SPEAKER_04:** There's a lot of different things that we can do, depending on your particular needs.

> 我们能做的事情有很多种,具体取决于你的特定需求。

[10:26] **SPEAKER_01:** MELANIE WARRICK- It sounds like this is a complete different paradigm than RL, because we went through the S-curve of regular pre-training, RL with when OpenAI released 01, and now this feels like a new one. It sounds special. It rhymes a lot with RNNs, which is a whole different paradigm than RL, right?

> 听起来这是一种和强化学习(RL)完全不同的范式,因为我们经历过常规预训练的 S 曲线,又经历了 OpenAI 发布 o1 时带来的强化学习那条曲线,而现在这个感觉像是全新的一条。听上去很特别。它和 RNN 有很多相通之处,而 RNN 是一种和 RL 截然不同的范式,对吧?

[10:46] **SPEAKER_04:** JOSE QUINONEZ- It's going to depend on the particular task, the particular type of problem that we're going after, that we're trying to solve, and the underlying models that we're working with. But effectively, you could say like each model or each set of models that we're working with will have their own S-curve. The poetic system, the poetic metasystem itself, is also going to have its own S-curve. And so as a poetic metasystem gets better and as the underlying models get better, you'll find that the S-curve that you're dealing with keeps shifting higher and higher until ultimately either you saturate or like- MELANIE WARRICK- Reach AGI? JOSE QUINONEZ- Yeah, reach AGI, reach super intelligences, yeah.

> 这要看具体的任务、我们所要攻克和解决的具体问题类型,以及我们所使用的底层模型。但从效果上讲,你可以说,我们所用的每一个模型、或每一组模型,都会有它们自己的 S 曲线。Poetic 系统,也就是 Poetic 元系统本身,同样会有它自己的 S 曲线。所以随着 Poetic 元系统变得更好、随着底层模型变得更好,你会发现你所面对的那条 S 曲线不断地向上移动,直到最终要么你达到饱和,要么就像——达到 AGI?——对,达到 AGI,达到超级智能,是的。

[11:24] **SPEAKER_02:** MELANIE WARRICK- Given that it's stilts, you might like hit the ceiling first then.

> 既然它是"高跷",那你可能会先撞到天花板。

[11:27] **SPEAKER_04:** JOSE QUINONEZ- That's the goal, right? JOSE QUINONEZ- Yeah. MELANIE WARRICK- You want to hit the ceiling first with poetic.

> 那正是目标,对吧?是的。你希望借助 Poetic 第一个撞到天花板。

[11:30] **SPEAKER_02:** JOSE QUINONEZ- I think a lot of startups that we work with, and then in my spare time, I do a bunch of context engineering. And then the thing is we're sort of like tuning it, tuning evals, tuning like we're context stuffing ourselves. What does that even feel like to have a recursively self-improving version of prompt engineering and context engineering?

> 我想,很多和我们合作的创业公司都是这样,而我自己在业余时间也做很多上下文工程。问题是,我们基本上是在手动调它、调评测(eval)、自己往里塞上下文(context stuffing)。那么,拥有一个可递归自我改进版本的提示词工程和上下文工程,究竟是种什么样的感觉?

[11:52] **SPEAKER_04:** JOSE QUINONEZ- We don't spend a lot of time looking at the particular data that we're working with. Instead, we're letting the poetic meta system look at that data. And so the meta system, if it thinks that it needs to put more things into context, do more context stuffing or whatever, it'll do that. If it needs to generate a bunch of examples to get better performance, it'll do that for you, right? It was pretty interesting to look at the prompt outputs, and particularly I'd say for ArcAGI, in that I think you can read those and say, well, that's not what a human would have written pretty clearly.

> 我们不会花很多时间去盯着我们手头的具体数据看。相反,我们让 Poetic 元系统去看那些数据。于是,如果元系统认为它需要往上下文里放更多东西、需要做更多的上下文填充之类的,它就会去做。如果它需要生成一批样本来获得更好的性能,它也会替你去做,对吧?看这些提示词的输出挺有意思的,尤其我得说是在 ArcAGI 上,我觉得你读那些内容就会说:嗯,这显然不是人类会写出来的东西。

[12:34] **SPEAKER_04:** And there's some unexpected stuff. And it made some really simple examples. And one of the examples is actually wrong. But we didn't change it. We're like, this is the thing that output.

> 里面有些出人意料的东西。它做出了一些非常简单的例子,而其中有一个例子其实是错的。但我们没有去改它。我们心想:这就是它输出的东西。

[12:47] **SPEAKER_04:** We'll just leave it be. We don't want to go in and monkey around with things. And so historically in machine learning, you do this. You don't want to go in and monkey around with things. And so historically in machine learning, learning you always you know it's like the the rule was you have to know your data set really well um but now we're kind of outsourcing that to the ai itself where the ai is the it's the ai's job to understand the data set and figure out where are the failure modes um and where are the kind of robust reasoning strategies that uh the model that that the agent could uh use um to get

> 我们就让它保持原样。我们不想进去瞎折腾。在机器学习的历史上,一直有这么条规矩:你必须非常了解你的数据集。但现在我们某种程度上把这件事外包给了 AI 本身——理解数据集、找出失败模式(failure modes)、以及找出那些稳健的推理策略(供模型、供 agent 使用以获得更好的表现),都成了 AI 的活儿。

[13:18] **SPEAKER_02:** better performance how much of it is like much the output is much better prompts and then how much of it is like the harness itself uh context stuffing or summarizing in the right way or re-ranking in the right way so that like you have some number of like mega llm calls and then how do you get

> 那么这里面有多少是因为输出的提示词好得多,又有多少是因为 harness 本身——以正确的方式做上下文填充、或做摘要、或做重排序(re-ranking),从而让你有若干次"超大型"的 LLM 调用——那你又是怎样——

[13:34] **SPEAKER_04:** the most out of um each of those calls yeah and so that definitely varies per problem but uh what we've seen uh in fact uh our our last paper at deepmind was not doing this recursive self-improving stuff but we were um we were showing that you could build these harnesses um maybe you could manually to solve really hard problems and what we saw is there is that uh you know we manually optimized the prompts really hard for these very hard problems and that got us a little bit of the way uh in this particular case you know the hardest the hardest task we were working on we got like to five percent performance with gemini 1.5 flash this was a while ago and then when we added on the the reasoning strategies we went from five percent to ninety five percent uh and so uh this is typically what we see you know like everybody's out there kind of doing some amount i wouldn't say everybody but many people are out there kind of doing some amount of automated prop prompt optimization every you know jepa is this very popular paper everybody's kind of re-implementing that that will get you some performance improvements but it's very far from everything that you can get if you actually think about these reasoning strategies that are really going to be written in code rather than in just better prompts so if

> ——从每一次这样的调用中榨取出最大价值的呢?是的,这肯定是因问题而异的。但我们所看到的——事实上,我们在 DeepMind 的上一篇论文并没有做这种递归自我改进的东西,而是表明你可以搭建这些 harness,也许可以手工搭建,来解决真正的难题。我们看到的是:我们为这些非常难的问题手工地、非常卖力地优化提示词,那让我们前进了一小段。在这个具体的例子里,我们当时攻克的最难的那个任务,用 Gemini 1.5 Flash 我们大概只做到了 5% 的表现——这是一段时间以前的事了——然后当我们加上那些推理策略后,我们从 5% 一下子提升到了 95%。所以这通常就是我们所看到的情况。要知道,现在大家都在或多或少地做一些——我不能说是所有人,但很多人都在或多或少地做一些自动化的提示词优化,比如 GEPA 就是一篇非常流行的论文,大家都在复现它,那确实能给你带来一些性能提升,但那离你真正能够获得的全部还差得很远——只要你真的去认真思考这些推理策略,它们其实是要用代码来写的,而不只是靠更好的提示词。所以如果——

[14:51] **SPEAKER_00:** startups want to use poetic to put their agent on stilts what should they do yeah so right now

> ——创业公司想用 Poetic 把他们的 agent 架上"高跷",他们该怎么做?好,那么现在——

[14:58] **SPEAKER_04:** uh we haven't released anything yet but uh if you go to poetic.ai there is a button you can click to get uh sign up for early access and if you're a startup or a company who has a really hard problem and you've tried everything that you can to make it reliable and robust and you just can't get all the way there you you need something more then uh let us know we're looking for problems like that uh so just tell us tell us what it is that you're working on and uh we'll reach out you'll be the first to know when we're when we're ready to work with you

> ——呃,我们还没有正式发布任何东西,但如果你访问 poetic.ai,那里有一个按钮,你可以点击来注册申请抢先体验(early access)。如果你是一家创业公司或企业,手上有一个真正的难题,你已经想尽一切办法让它变得可靠、稳健,可就是没法完全做到位,你需要更强的东西,那就告诉我们——我们正在寻找这样的问题。所以只管把你正在攻克的问题告诉我们,我们会主动联系你。等我们准备好和你合作时,你会是第一个知道的。

[15:30] **SPEAKER_02:** i mean if you're at the top of um humanity's last exam then i mean that's that's pretty big so it's you're all you're already all the way out there at soda and then i guess the stilts basically let any agentic company become soda that's the idea yeah yeah

> 我是说,如果你都能登上"人类最后的考试"的榜首,那这可是件相当了不起的事。所以你们已经一路冲到了 SOTA(当前最高水平)那儿,然后我想,这副"高跷"基本上能让任何做 agent 的公司也变成 SOTA——就是这个意思,对吧?是的,是的。

[15:45] **SPEAKER_04:** and you know we view the rkgi results and the humanities last exam results as showing kind of two different uh capabilities that we have we can really improve your reasoning and we can really improve uh deep knowledge extraction uh from these models and then you're just totally vaccinated

> 而且你知道,我们把 ARC-AGI 的结果和"人类最后的考试"的结果看作展示了我们所具备的两种不同能力:我们能够真正提升你的推理能力,也能够真正提升从这些模型中做深度知识抽取的能力。这样一来,你就彻底"免疫"了——

[16:01] **SPEAKER_02:** against the bitter lesson exactly yc's next batch is now taking applications got a startup in you apply at ycombinator.com apply it's never too early and filling out the app will level up your

> ——对惨痛教训(the bitter lesson)免疫,没错。YC 的下一批正在接受申请。心里有个创业点子?就去 ycombinator.com 申请吧。永远不嫌太早,而且填写申请表本身就会让你的点子更上一层楼——

[16:15] **SPEAKER_03:** idea okay back to the video a slight sort of change change a topic but something i was curious about you arrived at google over a decade ago when they acquired your first yc startup a portable a portable was it's importing mobile apps cross-platform right like android or whatever it's quite different to um recursive self-improving agi um how did you make that leap what happened once you got to google um what made you think that you maybe wanted to shift down do something

> ——好,回到视频。稍微换个话题,不过这是我一直很好奇的一件事。十多年前你加入 Google,当时他们收购了你的第一家 YC 创业公司 Apportable。Apportable 做的是把移动应用跨平台移植,对吧?比如移植到 Android 之类的。这和递归自我改进的 AGI 相当不一样。你是怎么完成这种跨越的?你到了 Google 之后发生了什么?是什么让你觉得也许想要换个方向、去做点——

[16:44] **SPEAKER_04:** different and just would love to hear that story the acquisition was this amazing opportunity to reflect on what i really wanted to be doing next right like google was in the you know itself is a place where you can do so many different things uh so i spent some time thinking about um where uh where i wanted to go next in in uh in my journey i realized that the problems that i was most excited about were really actually ai and uh and robotics and the best people in the world many of them in those fields were at google at the time and so i went and talked to them they let me come join you know a new ai robotics team in google research which was this amazing opportunity for me since that wasn't my background my background was like computer security and then this cross-platform mobile you know it's systems building uh stuff i was able to join this team and i didn't really want to be doing robotics it was more aspirational at that moment uh but i was really um passionate about machine learning so i just i made a very hard switch into just doing machine learning research uh and did that for you know about a decade at google and then google and then deepmind what's maybe some advice that you have today for engineers who want to get

> ——不一样的事情?我很想听听这个故事。那次收购是一个绝佳的机会,让我去反思自己接下来真正想做什么。Google 本身就是一个你可以做许许多多不同事情的地方。所以我花了些时间去思考,在我的旅程中接下来想往哪儿走。我意识到,最让我兴奋的那些问题其实是 AI 和机器人技术,而当时世界上这些领域最顶尖的一批人有很多都在 Google。于是我去和他们聊,他们让我加入了 Google Research 一个新的 AI 机器人团队,这对我来说是个绝好的机会,因为那并不是我的背景——我的背景是计算机安全,后来又做了这种跨平台移动系统的搭建之类的东西。我能够加入这个团队,而其实我并不太想做机器人,那在当时更多是一种憧憬,但我对机器学习是真的充满热情。所以我做了一次非常艰难的转型,一头扎进纯粹的机器学习研究,并在 Google、之后又在 DeepMind 干了大约十年。那么,对于想要进入——

[18:16] **SPEAKER_03:** Maybe some advice that you have today for engineers who want to get into sort of more of the AI side, probably the applied AI and build startups around AI, like how should they think about that?

> 对于那些想更多地进入 AI 这一侧——大概是应用型 AI(applied AI)——并围绕 AI 创办创业公司的工程师们,你今天或许有什么建议?他们应该怎么去思考这件事?

[18:28] **SPEAKER_04:** You know, the world is changing so quickly. This is probably a little bit obvious, but you should just try things and like every day do something, do something with AI, always try to push yourself to find the boundaries of what they're capable of and build the things that you want to build, right? Even for me, you know, last summer, I took a weekend and used GPT-5 to help me build an iPhone app. I hadn't done that in a decade. So fast.

> 你知道,世界变化得太快了。这话说出来可能有点显而易见,但你就应该去动手尝试,差不多每天都做点什么、用 AI 做点什么,始终逼着自己去探索这些模型能力的边界,并去打造你想打造的东西,对吧?就连我自己,去年夏天也花了一个周末,用 GPT-5 帮我做了个 iPhone 应用。我已经有十年没干过这种事了。太快了。

[19:03] **SPEAKER_04:** Yeah, it's so fast and so easy. And that was, you know, that was an age ago. That was like eight months ago. Now it's even faster and easier. Don't limit yourself.

> 是啊,又快又简单。而那已经是很久以前的事了,大概八个月前吧。现在比那时候还要更快、更容易。别给自己设限。

[19:11] **SPEAKER_04:** Like anything that you imagine, you should just try to use AI and see how far you can get with it and you'll be, you know, making the world better.

> 任何你能想象到的东西,你都应该试着用 AI 去做,看看你能借助它走多远——而且你会因此让这个世界变得更好。

[19:19] **SPEAKER_02:** That's all we have time for today. But Ian, thank you so much for giving us all stilts. We can't wait to use it at YC. I can't wait to use it for Gary's list. I mean, there's just so much to do.

> 今天我们的时间就到这里了。不过 Ian,非常感谢你给了我们大家这副"高跷"。我们在 YC 迫不及待想用上它。我都等不及想把它用在 Gary 的清单上了。我是说,要做的事情实在太多了。

[19:30] **SPEAKER_04:** So yeah, thank you for having me. This was a lot of fun.

> 那么,是的,谢谢你们请我来。这真是太有意思了。
