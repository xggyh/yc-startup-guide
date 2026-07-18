# 全文转录 · 把 Claude Code 变成你的 AI 工程团队

> ▶ [YouTube](https://www.youtube.com/watch?v=wkv2ifxPpF8) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/wkv2ifxPpF8.md) &nbsp;·&nbsp; How to Make Claude Code Your AI Engineering Team

> 中英对照 · 每段英文原文下附中文翻译

`[00:08]` Hi, I'm Gary, president and CEO of Y Combinator. I'm also an engineer who spent the first decade of my career building software full-time. I studied computer systems engineering at Stanford, then was employee number 10 at Palantir, where I was an engineer, designer, and product manager all at once. I co-founded Posterous, a microblogging platform that sold to Twitter. And I also built the first version of Bookface, YC's internal social platform and knowledge base.

> 大家好,我是 Gary,Y Combinator 的总裁兼 CEO。我同时也是一名工程师,职业生涯的头十年都在全职做软件开发。我在斯坦福学的是计算机系统工程,之后成为 Palantir 的第 10 号员工,在那里我一个人身兼工程师、设计师和产品经理三职。我联合创办了 Posterous,一个后来卖给 Twitter 的微博客平台。我还打造了 Bookface 的第一个版本,也就是 YC 内部的社交平台和知识库。

`[00:40]` Basically, I've written a lot of code in my career, and I'm here to tell you we are in a completely new era of building software, the agent era. It turns out the way to get agents to do real work is the same way humans have always done it, as a team, with roles, with process, with review. I built GStack to encode this three weeks ago, and now it has more GitHub stars than Ruby on Rails. In this video, I want to explain how it can help you build with agents. I've coded more in the past two months than I did in all of 2013,

> 说白了,我这辈子写过很多代码,而我今天要告诉你,我们正处在一个全新的软件开发时代——智能体(agent)时代。事实证明,让智能体真正干活的方式,和人类一直以来的做法是一样的:以团队形式协作,有角色分工、有流程、有评审。三周前我打造了 GStack 来把这套方法固化下来,如今它在 GitHub 上的星标数已经超过了 Ruby on Rails。在这个视频里,我想讲讲它如何帮助你用智能体来做开发。过去两个月我写的代码,比我 2013 年一整年写的还多,

`[01:17]` which is the last time I worked really, really hard as an engineer. I started playing with cloud code back in January, after hearing people like Andrej Karpathy and Boris Cherny say they weren't manually writing any code anymore. And I got completely hooked. Along the way, I've essentially built all of Posterous, which took two years to build with a co-founder and a team of 10 engineers. I've essentially built all of my startup, Posterous, which took two years, $10 million, and 10 engineers to build.

> 而 2013 年是我上一次作为工程师拼命干活的时候。我从一月份开始玩 Claude Code,起因是听到 Andrej Karpathy、Boris Cherny 这些人说他们已经不再手写任何代码了。然后我就彻底上瘾了。在这个过程中,我基本上把整个 Posterous 都重建了一遍——当年那个产品可是我和一位联合创始人加上 10 名工程师花了两年才做出来的。我几乎凭一己之力重建了我的创业公司 Posterous,而当初它花了两年时间、一千万美元和 10 名工程师才做成。

`[01:51]` Out of the box, the model wanders. It doesn't know your data well, so it guesses. And guessing at that scale is how you get plausible-looking code that silently breaks. The bottleneck here is not the code itself. The bottleneck here is not the model's intelligence.

> 开箱即用的情况下,模型会"乱走"。它不了解你的数据,所以只能猜。而在那种规模上靠猜,就会产出一堆看似合理、却会悄无声息出问题的代码。这里的瓶颈不在代码本身。瓶颈也不在模型的智能水平。

`[02:04]` As long as you set the models up right, they are already smart enough to do extraordinary work on your code base. This is backwards. The scaffolding should be trivially thin. GStack is my implementation of the thin-harness, fat-skills approach. It's an open-source repo that I built that turns cloud code into an AI engineering team for you.

> 只要你把模型配置得当,它们已经足够聪明,能在你的代码库上做出非凡的工作。很多人的思路是反的。真正的脚手架(scaffolding)应该薄到几乎可以忽略。GStack 就是我对"薄外壳、厚技能"(thin-harness, fat-skills)这一理念的实现。它是我做的一个开源仓库,能把 Claude Code 变成一支为你服务的 AI 工程团队。

`[02:29]` Skills that act like a team of specialists. Office hours. Is one of those skills. It's actually modeled exactly after what we go through at YC as a partner doing office hours with startups. It starts by asking six forcing questions for you to reframe your product before you start building.

> 这些技能(skills)就像一支由各领域专家组成的团队。Office Hours(答疑时间)就是其中一项技能。它其实完全仿照了我们在 YC 作为合伙人给创业公司做 office hours 的流程。它一开始会抛给你六个"逼问式"的问题,让你在动手开发之前先重新审视、重构你的产品。

`[02:48]` Let me show you how it works. The best way to get started with GStack is actually conductor. And so we're gonna go in Quick Start and GStack is actually built into conductor right now. You just click GStack, and today, you're going to see a lot of work right here. That's what I'm going to do.

> 让我给你演示一下它怎么用。上手 GStack 最好的方式其实是通过 Conductor。所以我们进到 Quick Start(快速开始),GStack 现在已经内置在 Conductor 里了。你只要点一下 GStack,今天你就会看到大量的工作在这里展开。接下来我就来做这个。

`[03:02]` we're going to make a tax app. It's going to go into your Gmail and fish out all of your 1099s because it's tax day as of today. GSTACK is actually a set of skills. And the first one that we're actually going to use is called Office Hours. This is actually the distilled version of what is thousands and tens of thousands of hours that the 16 YC partners have spent many, many years honing and perfecting. And this is a distilled down 10% strength version of what we do

> 我们要做一个报税应用。它会进到你的 Gmail 里,把你所有的 1099 表格都捞出来——因为今天正好是报税截止日。GStack 本质上是一套技能的集合。我们首先要用到的这一项叫 Office Hours。它其实是把 16 位 YC 合伙人多年来花费成千上万小时打磨、锤炼出来的东西提炼浓缩后的版本。这是我们每天在 YC 所做工作的一个"10% 强度"的精简版。

`[03:39]` at YC every day. So as you can see, Conductor actually just drops you right in there. We're in YC Office Hours now, and I'm trying to do a startup to create, to help people get all their 1099 ints out of their YC. So we're going to go to our Gmail and Financial Institutions. Many banks will email you with new tax documents, but some won't. So we need to both search the user's inbox and accept URLs to go and

> 如你所见,Conductor 直接就把你带到这个界面里了。我们现在就在 YC Office Hours 里,我想做一个创业项目,来帮人们把他们所有的 1099-INT 表格弄出来。所以我们要去连他们的 Gmail 和各家金融机构。很多银行会给你发邮件通知新的税务文件,但有些不会。所以我们既需要搜索用户的收件箱,也需要接受用户提供的网址,去

`[04:23]` search and download the 1099 int PDFs. Cool. That's our startup idea. It's just something to help people with their taxes. And it's something that I had to deal with just yesterday. So the user wants to do Office Hours about a startup idea. And it's starting

> 搜索并下载 1099-INT 的 PDF 文件。挺好。这就是我们的创业点子。它就是帮人们搞定报税的一个工具。而且这正是我昨天刚不得不亲自处理的事情。所以现在,用户想就一个创业点子做一次 Office Hours。它已经开始

`[04:41]` on Office Hours. So one of the things you'll notice is we have Geary mode on. And what that does is it actually shows you all of the reasoning traces. So that's one of the things I really like about using GSTACK. It actually, with Conductor, you actually get to see exactly what the money is.

> 进入 Office Hours 了。你会注意到,我们开启了 Gary 模式(Geary mode)。它的作用是把模型所有的推理过程(reasoning traces)都展示给你看。这也是我特别喜欢用 GStack 的一点。配合 Conductor,你能真真切切地看到模型到底在想什么。

`[05:01]` The model is thinking as it does it. Right now, it's just sort of getting started. But now it's starting to do some context. Okay, this is a fresh project with an initial commit. No prior design docs. We're in startup mode. Oh, and here, this is sort of the first thing that happens. Your model

> 模型是边做边思考的。现在它才刚开始起步。但它已经开始梳理一些上下文了。好,这是一个全新的项目,只有一个初始提交,没有任何先前的设计文档,我们处于"创业模式"。哦,看这里,这基本上就是第一步会发生的事情。你的模型

`[05:19]` with the skill of Office Hours does a lot of thinking. It searches the web sometimes and figures out, well, what are you trying to do? Here's the question that determines everything else. What's the strongest evidence? That you have that someone actually wants this? This is actually one of the most important

> 在 Office Hours 这项技能的加持下,会做大量的思考。它有时会去搜索网络,弄清楚:你到底想做什么?这就是那个决定其他一切的关键问题——你手上最有力的证据是什么,能证明真的有人想要这个东西?这其实是最重要的

`[05:35]` questions to ask yourself when you're trying to decide, should I work on Project X or work on that startup? I actually just experienced this recently. So I'm going to click that. I have this experience just the other day. So what happened exactly? How many bank accounts do we have? And

> 你在决定"我该不该去做 X 项目,或者去做那个创业公司"时应该问自己的问题之一。我自己最近就刚刚经历过这个。所以我要点这个。我前几天就有过这样的经历。那么具体发生了什么呢?我们有多少个银行账户?

`[05:53]` which one sent 1099? Well, I have a few and then the process of hunting down is actually quite painful. Okay, the pain is real, but the consequence is friction and annoyance, not actual penalties. Well, I mean, frankly, my accountant sends me annoyed emails. And sometimes they get a phone call because they're just trying to do my their job. And I'm supposed to be there to help them. And so I

> 又是哪一个给我发了 1099?嗯,我有好几个账户,而挨个去找的过程其实相当痛苦。好,痛点是真实存在的,但它带来的后果是麻烦和烦躁,而不是真正的罚款。呃,说实话,我的会计师会给我发那种不耐烦的邮件。有时候他们还得打电话来,因为他们只是想把工作做好。而我本该配合他们才对。所以我

`[06:19]` do have more than five accounts. This is actually a really interesting thing. It points out TurboTax and HR in our block actually have 1099 import features and Plaid connects to banks. Why aren't those solving it for you? So I answered and said, Well, the users thinking bigger than a document aggregator, they're seeing this as a funnel, the hook is we'll find all your 1099 ins for you solving an immediate pain. But the

> 确实有五个以上的账户。这里有个非常有意思的点。它指出 TurboTax 和 H&R Block 其实已经有 1099 导入功能了,而 Plaid 能连接各家银行。那为什么这些方案没能替你解决问题呢?于是我回答说:嗯,用户想的其实比一个"文档聚合器"更大,他们把这看成一个漏斗——诱饵是"我们帮你把所有 1099-INT 都找出来",解决一个眼前的痛点。而

`[06:41]` expansion is now that you have your docs, let's actually get your taxes prepared, which is matchmaking and lead gen for tax preparers. And it's a classic wedge strategy. It's actually a more interesting business model than just the document aggregation alone, which is right, but you could probably charge two or $5 a month, or two or $5, maybe an entire year for 1099 in integration. But you can actually charge a percentage of the transaction that ends up happening with a tax preparer, which might be 10x more, this is actually a very cool part of office

> 后续的扩展则是:既然你已经拿到了你的文件,那我们干脆帮你把税也报了吧——这其实就是为报税代理人做撮合和获客(lead gen)。这是一个经典的"楔子"策略(wedge strategy)。它确实是一个比单纯做文档聚合更有意思的商业模式。文档聚合本身没错,但你大概只能收每月两三五美元,或者说一整年就收个两三五美元来提供 1099 整合服务。而如果你抽取用户最终和报税代理人之间成交金额的一个百分比,收入可能会高出 10 倍。这其实是 Office Hours

`[07:15]` hours. I might just build this for myself just for fun, because I do have to do this every single year. And this is actually one of the most fun parts about using office hours. And G Stack is it's this sort of on rails thing it's more like a conversation with your model and so if you just came in and gave instructions to the model as it is if I just type the original thing which is I need to go and find my 1099s it'll go do that it will just literally do it but it won't think about who's the user what is

> 里非常酷的一部分。我搞不好真会纯粹为了好玩给自己做一个,因为我每年都得干这件事。这也确实是用 Office Hours 最有意思的地方之一。GStack 是那种有点"顺着轨道走"的东西,它更像是你和模型之间的一场对话。所以,如果你就这么进来,直接给模型下指令——如果我一上来就打"我要去找我的 1099 表格",它就会去做,它真的就照做了,但它不会去思考:谁是用户?这是什么?

`[07:45]` this what is the business model who wants this what's the pain point how does it work right like this is the kind of stuff that we get to do every day with lots and lots of founders in office hours and we're pretty good at it but so is this skill revised AI browser automation g-stack browser style lets the user login then AI navigates to tax docs and downloads PDFs the user watches it happen I think that's correct let's see I mean this is a very interesting thing for me I mean I feel like I learned about the process of building a

> 商业模式是什么?谁想要这个?痛点在哪?它怎么运作?对吧,这正是我们每天在 Office Hours 里和一大堆创始人一起做的事情,我们相当擅长这个——而这项技能同样擅长。它修订出这样的方案:AI 浏览器自动化,GStack Browser 风格,让用户先登录,然后由 AI 导航到税务文件页面并下载 PDF,用户全程看着它发生。我觉得这是对的。我们看看。对我来说这真是件很有意思的事,我感觉我自己都从这个开发过程里学到了点东西——尽管我天天都在给人做 Office Hours。

`[08:14]` little bit even though I do office hours with people all the time this is sharp pushback on premise 3 you're right I do have g-stack browser and the approach you're describing here is a little bit different from what you're describing is genuinely clever the model would be user logs in AI takes over navigates to tax docs finds the 1099 ince downloads it no plaid no stored credentials the user watches the whole thing happen in the visible browser I mean what I like about it is it can happen on their actual browser it's not happening in the

> 它对第三条前提提出了尖锐的反驳:"你说得对,我确实有 GStack Browser,而你这里描述的方法有点不一样"——它说这个思路是真的很巧妙:流程是用户登录,然后 AI 接管,导航到税务文件页面,找到 1099-INT,把它下载下来,不用 Plaid,不存储任何凭据,用户就在可见的浏览器里看着这一切发生。我喜欢它的一点是,这可以在用户自己真实的浏览器里进行,而不是发生在

`[08:39]` cloud the cloud is just someone else's computer one of the cool things that g-stack does increasingly is it lets you use codecs to actually sort out all of the crazy bugs that might be in here I'm not gonna do it right now but it is something that you can do when you're at home working on it yourself the way to think about Claude code is that by default it uses Claude and I think Opus 4.6 is sort of ADHD CEO he's the guy you want to get a beer with and he's got a billion ideas but when the going gets tough you got to call in your autistic

> 云端。所谓云,不过是别人的电脑罢了。GStack 越来越酷的一点是,它能让你用 Codex 去真正排查这里面可能藏着的各种离谱 bug。我现在不演示这个,但这是你自己在家里做项目时可以做的事。理解 Claude Code 的方式是:它默认用的是 Claude,我觉得 Opus 4.6 有点像一个"多动症 CEO"——他是那种你很想约出去喝一杯的家伙,脑子里有一亿个点子;但当情况变得棘手时,你就得把你那位"自闭症

`[09:13]` CTO and that's codecs all right we're gonna skip for now because we're actually pretty close I feel like basically we're in plan mode and office hours helps us start off with a plan that has a lot of the things thought through so here's actually a really cool example it actually thinks through and here's three different approaches the first approach is gmail ath then search for tax doc notification and output a checklist of banks which issued 10 99s there's no browser automation initially the effort is small and the risk is small you know

> CTO"请出来——那就是 Codex。好,我们暂时先跳过这一步,因为其实我们已经很接近了。我感觉我们基本上进入了 plan 模式(计划模式),而 Office Hours 帮我们以一个已经把很多事情都想清楚了的计划作为起点。这里有个非常酷的例子:它把问题想透了,给出了三种不同的方案。第一种方案是先做 Gmail 授权,然后搜索税务文件的通知邮件,输出一份"哪些银行开具了 1099"的清单,初期完全不涉及浏览器自动化,工作量小、风险也小。

`[09:48]` when I look at that and it's like that sounds interesting but it doesn't sound big enough even work on this like I could do that myself next is full stack Gmail and AI browser automation using and a CPA marketplace this sounds like what I want actually and then it sort of thinks out of the box it says okay what about approach see CPA first flip the go to market you know I would say B sounds right and then actually I sometimes I like to add this extra thing which is like when I have an idea when I one of the approaches speaks to me but then I

> 我一看,心想这听起来挺有意思,但感觉不够大,都不值得去做,我自己就能搞定。接下来是方案二:全栈方案,Gmail 加上 AI 浏览器自动化,再加一个注册会计师(CPA)市场——这个听起来其实才是我想要的。然后它还跳出框框想:好,那方案三呢?"CPA 优先",把进入市场的顺序(go-to-market)整个翻转过来。我会说方案 B 听起来是对的。然后其实我有时喜欢再加上这么一层:当我有了一个想法,当其中某个方案打动了我,但我又

`[10:21]` think about something else I'm like okay well I like B but actually we could use the browser interaction to skip Google Oh off entirely and just have the user open Gmail and a version of g-stack browser could just use Gmail to find the 1099 ought to search for automatically simultaneously to that it could also ask the user what other banks they have also and this is what happens for me if they already have a CPA you can find out from email and if you're me you probably already have a bunch of emails from your CPA bugging

> 想到了别的:我心想,好吧,我喜欢 B,但其实我们可以利用浏览器交互,完全绕过 Google OAuth,直接让用户打开 Gmail,由某个版本的 GStack Browser 就用 Gmail 去自动查找和搜索那些 1099。与此同时,它还可以问用户:你还有哪些别的银行?对我来说情况就是这样。如果用户已经有 CPA 了,你也能从邮件里看出来;而如果你是我这种人,你的收件箱里大概早就堆着一堆你的 CPA 发来的邮件,

`[11:15]` you for the specific accounts we're sort of at the end of office hours but as you can see we already went from sort of a half baked rough idea for something that we might want to do I'm not saying this is actually a good startup idea but you can see how this got farther along we started with something that might start with Oh off and then CPAs nagging emails but in the end we realized well we have a browser and the browser could be used with browser automation to search the inbox find all of the 1099s that you

> 在催你提供那些具体账户的信息。我们差不多到了 Office Hours 的尾声,但如你所见,我们已经从一个半生不熟、粗糙的、"也许想做"的点子出发,走了很远。我不是说这真的是个好的创业点子,但你能看到它是怎么一步步深化的。我们一开始的方案可能是从 OAuth 起步,再加上 CPA 那些催命的邮件;但到最后我们意识到:嘿,我们有浏览器啊,可以用浏览器自动化去搜索收件箱,找到你需要

`[11:51]` need to download thickening we start to COD a bunch of memory pods and we It can also, using LLMs, ask you which bank portals you need to add to, and it can go log in with your account and actually download the PDFs for you and then send an email to the CPA. So I really like this. Browser automation is a very out-of-pocket, sort of unusual way to solve this problem. And the wild thing about coding models is, you know, a year ago, two years ago, even like three months ago, it's not clear to me that anyone would even try this.

> 下载的所有 1099。它还可以借助大语言模型(LLM)来问你:你需要接入哪些银行门户网站?然后它就能用你的账户登录,真的替你把 PDF 下载下来,再给 CPA 发一封邮件。所以我真的很喜欢这个方案。用浏览器自动化来解决这个问题,是一种非常出人意料、相当不寻常的思路。而编程模型最疯狂的一点在于——你知道吗,一年前、两年前,甚至就在三个月前,我都不确定会有谁愿意去尝试这种做法。

`[12:23]` I think that's the most interesting thing about our time right now. You're able to have an idea and then get farther along with it than you ever would be. Frankly, sometimes I use office hours and maybe one in three times I get to the end of it and I say, you know what? This isn't something that makes sense. You'll notice that there's actually a feasibility aspect of office hours, and that's one thing I really pride myself on in office hours working with.

> 我觉得这是我们当下这个时代最有意思的地方。你能有一个点子,然后把它推进到远超以往可能达到的程度。老实说,有时候我用 Office Hours,大概每三次里就有一次走到最后我会说:你知道吗?这事儿其实说不通。你会注意到,Office Hours 里其实包含一个"可行性"的评估环节,而这正是我在给人做 Office Hours 时特别引以为傲的一点。

`[12:47]` I have a very strong opinion about how the world works and what might work. And it's just very interesting to see Opus 4.6 mirror that in trying to help you figure out what your startup or product idea might be. Now what it's doing is a multi-step adversarial review. It's trying to put your idea through the paces.

> 我对这个世界如何运转、什么东西可能行得通有着非常强烈的看法。而看到 Opus 4.6 在帮你厘清你的创业或产品点子时,能把这种判断力镜像复刻出来,真的很有意思。它现在正在做的是一个多步骤的对抗性评审(adversarial review)。它在设法让你的点子经受各种考验。

`[13:08]` And as you can see, it's already found a bunch of things and it's going to try to auto-fix it. There's no failure handling. There's no privacy section. 2FA handoff. Has no proposed solution.

> 如你所见,它已经找出了一堆问题,而且它会尝试自动修复。比如:没有失败处理机制;没有隐私相关的章节;双因素认证(2FA)的交接;这一项还没有提出解决方案。

`[13:19]` It actually tries to auto-fill out these things. And if it can, it does. And so our doc survived two rounds of adversarial review, and it automatically caught and fixed 16 issues. So we're going to approve this design doc. So as you can see, the adversarial review improved the score from 6 out of 10 to 8 out of 10, with three remaining issues that we can worry about later.

> 它实际上会尝试自动把这些内容补全。只要它能补,它就会补。就这样,我们的文档挺过了两轮对抗性评审,它自动发现并修复了 16 个问题。所以我们要批准这份设计文档。如你所见,对抗性评审把评分从 10 分制的 6 分提高到了 8 分,还剩三个问题,我们可以留到以后再操心。

`[13:43]` Now that we've locked in the adversarial review. And. Addressed. All these issues, normally what I would do is run plan CEO review, but instead, I think what we're going to do is jump directly to design shotgun, which is one of my most fun ways to use this. And this is just one of a bunch of different design tools that are in the bag.

> 既然我们已经敲定了对抗性评审,并且处理好了所有这些问题——通常接下来我会去跑 plan CEO review(计划的 CEO 评审),但这次我想我们直接跳到 Design Shotgun(设计霰弹枪),这是我用得最开心的功能之一。而它只是这一整套设计工具中的其中一个。

`[14:06]` So it figured out here's a bunch of different views. What do you want to actually design? And let's just do the main checklist dashboard design shotguns, my visual brainstorming tool. So. So it'll actually generate multiple AI versions and then ask us questions about it.

> 它已经想好了这里有一堆不同的页面视图。你到底想设计哪一个?我们就设计主清单仪表盘(checklist dashboard)吧。Design Shotgun 是我的可视化头脑风暴工具。它会实际生成好几个 AI 版本,然后就这些版本向我们提问。

`[14:22]` These are three directions. It takes about 60 seconds. It actually farms it out to open AI codecs, which is able to use image gen. So, all right, let's there's three versions command center, friendly progress and split view. Let's take a look.

> 这是三个不同的方向。大概需要 60 秒。它其实会把任务外包给 OpenAI 的 Codex,因为 Codex 能调用图像生成(image gen)。好,那么,这里有三个版本:指挥中心(command center)、友好进度(friendly progress)和分屏视图(split view)。我们来看看。

`[14:36]` All right. So let's let the agents cook and we'll be back in about five minutes. Great. The agents are done cooking and this is what we we got back. We got three different options.

> 好,那我们就让这些智能体自己去"炖"一会儿,大约五分钟后回来。太好了,智能体们已经"炖"好了,这就是我们拿到的结果。我们得到了三个不同的选项。

`[14:47]` For the actual page that shows up in the command center for tracking down our tax documents. So let's look at them one by one. There's option a, B and C. All right. Here's one command center.

> 这些是我们那个用来追查税务文件的指挥中心里实际会显示的页面。我们一个一个来看。这里有选项 A、B 和 C。好,这是第一个,指挥中心。

`[15:00]` There's a dashboard. Here's all the specific. I mean, this looks pretty good. If you can extract here, all the banks and here are all the 10 99s and where are they coming from? Um, and what their status is.

> 这里有一个仪表盘。这里是所有具体的信息。我是说,这看起来相当不错。如果你能在这里把所有银行都提取出来,这里列出所有的 1099,它们分别来自哪里,呃,以及它们各自的状态。

`[15:12]` That's pretty good. I like that. I'm going to give that a four out of five stars. Okay. All right.

> 这挺不错的。我喜欢这个。我给它打五颗星里的四颗。好的。行。

`[15:16]` And so there's option B is like much more friendly. So option a is sort of like if you're a Linux hacker, I bet you would really like this, but option B, I think it's more friendly for just normal people. So I kind of like I might put that as a five. That might be a pick. And then let's see.

> 然后是选项 B,它要友好得多。选项 A 有点像是——如果你是个 Linux 黑客,我敢打赌你会特别喜欢它;但选项 B,我觉得它对普通人来说更友好。所以我挺喜欢的,可能会给它打五颗星。这或许就是入选的那个。然后我们再看看。

`[15:34]` Option C. This makes it way more complicated than it needs to. So I really wouldn't do that. Let's go with option B. And then the cool thing is, if you don't like it, you can enter.

> 选项 C。这个把事情搞得比实际需要的复杂太多了。所以我真的不会选它。我们就选选项 B。而酷的地方在于,如果你不喜欢,你还可以输入

`[15:46]` you know any of your feedback you can click regenerate, but in this case, we're just gonna run with option B and continue so that comes back in and You know as you can see we're gonna go ahead and select option B and there it is So a friendly card based approach with progress and the progress ring good instinct variant B is locked in so while I have you I mean that is just two of 28 different commands we've got more than 70,000 Stars now and some of the people who use it like they actually talk about how when they're using cloud code

> 你的任何反馈,然后点击重新生成(regenerate)。但在这个例子里,我们就直接采用选项 B 继续下去。它把结果拿回来了,如你所见,我们就选定选项 B,就是它了——一个友好的、基于卡片的设计,带有进度显示和进度环。"直觉不错,B 版本已锁定。"趁你还在听我讲:要知道,这才不过是 28 个不同命令中的两个而已。我们现在已经有超过 70,000 个星标了,一些使用它的人还会聊到,他们用 Claude Code 的时候

`[16:22]` They spend 80 to 90 percent of their time in office hours plan CEO review and auto plan This is sort of a rough view of how that sprint process actually works We already talked about office space But if you don't want to do a lot of back and forth if you don't want to be in the weeds I did create auto plan which gets you through CEO engineering design and developer experience review using basically my default Recommendations like these are sort of programmed to be what I would do if I were you There are a bunch of design skills that you can use after the code is actually done

> 有 80% 到 90% 的时间都花在 Office Hours、plan CEO review 和 auto plan(自动计划)上。这大致就是那个冲刺(sprint)流程实际运作方式的一个粗略概览。我们已经聊过 Office Hours(他这里口误说成 office space)。但如果你不想来来回回折腾,不想陷进细节里,我还做了 auto plan,它会用基本上是我的默认建议,带你走完 CEO 评审、工程评审、设计评审和开发者体验评审——这些都被"编程"成了如果我是你我会怎么做。等代码真正写完之后,还有一堆设计技能可以用。

`[16:59]` Cloud code will actually build when you click approve on the plan and then after it's done writing the code You can run review which does a staff level bug catching service that goes through puts the Work through the paces full code review Finding bugs that might not have been in the plan mode and then the coolest part I think that is actually an incredible amount of code is I wrote a CLI around playwright and chromium So there's actually an entire headed and headless browser in there And that was a real magic moment for me as I was using cloud code as I sped up

> 当你在计划上点击"批准"后,Claude Code 就会真的开始构建;等它写完代码,你可以运行 review(评审),它提供的是一种"资深工程师级别"的抓 bug 服务,会把整份代码全面走一遍、反复考验,做一次完整的代码评审,找出那些在 plan 模式里可能没被发现的 bug。然后我觉得最酷的部分——它本身其实就是一大堆代码——是我围绕 Playwright 和 Chromium 写了一个命令行工具(CLI)。所以里面其实内置了一个完整的有头(headed)和无头(headless)浏览器。这在我使用 Claude Code、不断提速的过程中,对我来说真是一个奇迹般的时刻。

`[17:38]` There's this idea of trying to get a look to a level 8 I'm not sure if I can do that. I'm not sure if I can do that But I do think it gets you to level 7 and that's where I can run multiple Conductor windows on different projects and sometimes three or four all on the same project all at the same time. These are parallel PRS with parallel branches and parallel Different features that all can land more or less simultaneously And one of the bottlenecks I ran into was that you know? Once the agent was doing all the work of planning and design and coding it

> 有这么一个说法,叫努力做到"第 8 级"。我不确定我能不能做到,我不确定自己能不能达到那个程度。但我确实认为它能让你达到第 7 级——也就是我可以在不同项目上同时开好几个 Conductor 窗口,有时候是三四个,甚至全部都开在同一个项目上、同时进行。这些是并行的 PR、并行的分支、并行的不同功能,它们全都能差不多同时合并落地。而我遇到的一个瓶颈是,一旦智能体把计划、设计和编码的所有活儿都干完了,

`[18:18]` I found myself sitting there doing QA probably the least fun part of software development So that made it very very important for me to try to automate that and when I did Claude in Chrome MCP is One of the worst pieces of software I've ever used, you know Every time it would try to do an action it would think and think and think there was crazy context bloat often It wouldn't even do anything but it would take two to three seconds even when it was working to be able to take an action and I was amazed that

> 我就发现自己坐在那儿做 QA(质量测试)——大概是软件开发中最没意思的部分。所以对我来说,把这一步自动化就变得极其极其重要。而我去尝试的时候发现,Claude in Chrome 那个 MCP 是我用过的最糟糕的软件之一。你知道吗,它每次想执行一个操作时,都要想啊想啊想,常常会出现夸张的上下文膨胀(context bloat),很多时候它压根什么都没做;就算在正常工作时,执行一个操作也要花两到三秒。而让我惊讶的是,

`[18:49]` I could use all of my other skills in g-stack to create the slash QA and slash browse tool I basically wrapped playwright at the CLI level and Now your Claude code and any agent now can actually just use the browser And so, you know, not only could it use the browser it could take screenshots it can do complex Interactions it can click on things that can fill things out now it can even download media run eventually full regression tests and update CSS and Assess real browser bug issues, whether it's JavaScript or CSS and finally there's a ship tool

> 我竟然可以用 GStack 里我所有的其他技能,做出了 /QA 和 /browse 这两个工具。我基本上就是在命令行(CLI)这一层把 Playwright 封装了一下。现在你的 Claude Code 以及任何智能体,都能直接使用浏览器了。所以你知道,它不仅能用浏览器,还能截图、能做复杂的交互、能点击各种东西、能填写表单,现在它甚至能下载媒体文件,最终还能跑完整的回归测试(regression tests)、更新 CSS,并评估真实浏览器里的 bug 问题——无论是 JavaScript 还是 CSS 的问题。最后还有一个 ship(发布)工具。

`[19:30]` So it's sort of the last step before to make sure that your PR is ready to land on main And this is actually how I work. I run 10 to 15 parallel Claude code sessions all at the same time I'm I might in one session be running office hours on a brand new idea and I actually now have multiple open source projects with tens of thousands of stars and I'm probably sitting on about 400 Prs to review right now And so I almost always have one or two sessions active for each project Just evaluating and bringing in all the open source fixes that I'm getting from the community and I evaluate it in waves

> 它算是最后一步,用来确保你的 PR 已经准备好合并到主分支(main)上。而这其实就是我的工作方式。我会同时并行运行 10 到 15 个 Claude Code 会话。我可能在其中一个会话里针对一个全新的点子跑 Office Hours;而我现在其实已经有好几个星标数达数万的开源项目了,此刻我手上大概有约 400 个待评审的 PR。所以我几乎总是给每个项目开着一两个活跃的会话,专门用来评估并合入社区提交给我的各种开源修复,我是分批次(一波一波地)去评估的。

`[20:13]` One of the things that's been really scary in AI coding right now is supply chain attack So I'm really really paranoid about it But the great thing is I have G stack that has my back so I don't have a to-do list anymore one of the things that has emerged is I actually Click on whenever I have an idea or I get a bug report from a user or I see something on X where someone's Frustrated with what G stack or G brain does I just click the plus icon in conductor It creates a new work tree and each one of these things

> 现在 AI 编程领域里一件真正让人害怕的事情是供应链攻击(supply chain attack)。所以我对此极其极其警惕。但好消息是,我有 GStack 给我撑腰。因此我已经不再需要待办事项清单了。慢慢形成的一种工作方式是:每当我有个想法,或者收到用户的 bug 报告,或者在 X 上看到有人对 GStack 或 GBrain 的某个行为感到不满,我就直接在 Conductor 里点一下那个加号图标。它会创建一个新的工作树(work tree),而这里面每一个

`[20:42]` things is a new work item and all i have to do is run office hours ceo review end review adversarial review and then i just run my normal process when it's ready to land it lands and i can do 10 15 20 sometimes 50 prs in any given day depending on the number of meetings i have in that day so that's it gstack is available right now just go to github.com gary tan gstack when you run slash office hours you're getting a version of the real product thinking we do at yc with founders similar pushback and similar reframing before you ever meet us give it a try

> 都是一个新的工作项。我要做的就是运行 Office Hours、CEO review、review(评审)、adversarial review(对抗性评审),然后走一遍我的常规流程;等它准备好合并了,它就合并落地。视我那天开会的多少而定,我在任意一天里能处理 10 个、15 个、20 个,有时甚至 50 个 PR。就是这样。GStack 现在就可以用了,直接去 github.com/garytan/gstack。当你运行 /office hours 时,你得到的就是我们在 YC 与创始人打交道时那种真实的产品思考的一个版本——同样的尖锐反驳,同样的重新审视,而且是在你还没见到我们本人之前就能获得。来试试吧,

`[21:25]` and let me know what you think this is the most incredible time in history to build software the barrier to building just collapsed the only question left is what are you gonna build it's time to let it rip go make something people want

> 然后告诉我你的想法。这是有史以来做软件最不可思议的时代,开发的门槛刚刚轰然崩塌。现在唯一剩下的问题就是:你打算做点什么?是时候放手大干一场了。去做出人们真正想要的东西吧。
