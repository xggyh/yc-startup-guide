# 全文转录 · 前沿论文速览:推理、扩散、世界模型与无限算力

> ▶ [YouTube](https://www.youtube.com/watch?v=wE1ZgJdt4uM) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/wE1ZgJdt4uM.md) &nbsp;·&nbsp; Inference, Diffusion, World Models, and More | YC Paper Club

> 中英对照 · 每段英文原文下附中文翻译

[00:07] **SPEAKER_03:** All right. Hello, everyone. How you guys doing? Welcome to the first ever YC Paper Club. This

> 好的。大家好。你们都还好吗?欢迎来到有史以来第一届 YC 论文俱乐部(Paper Club)。这

[00:17] **SPEAKER_03:** is like a very exciting thing. Absolutely thrilled with the response. We had over a thousand folks that applied to come in. It was a very hard selection. If you guys have

> 真是一件令人非常兴奋的事情。我们对大家的反响感到无比激动。有超过一千人申请参加。这是一次非常艰难的筛选。如果你们有

[00:28] **SPEAKER_03:** friends that didn't make the cut, I'm very sorry. We kind of need to keep it to about 100. And so we selected a very, very cool group. The mission is to create this kind of community of great founders and great researchers and try to pull them together. I guess just

> 朋友没能入选,我非常抱歉。我们大概需要把人数控制在 100 人左右。所以我们挑选了一群非常非常酷的人。我们的使命是打造这样一个由优秀创始人和优秀研究者组成的社区,并努力把他们聚到一起。我想,

[00:48] **SPEAKER_03:** for you guys to get a sense for how cool the people in this room are. Raise your hand if you have at least five citations, 10 citations, a hundred citations, a thousand citations. Wow. This is insane. Okay. 10,000 citations. Oh my God. Okay. All right. This is awesome.

> 为了让你们感受一下这个房间里的人有多厉害。如果你至少有五次引用,请举手,十次引用,一百次引用,一千次引用。哇。这太疯狂了。好的。一万次引用。我的天。好的。好吧。这太棒了。

[01:15] **SPEAKER_03:** I would go up to 300,000, but I think it's like Chris Manning and that's about it. So raise your hand if you've raised at least a million dollars. Raise your hand if you've raised at least $5 million, at least $10 million, at least $50 million. We still got one. We

> 我本来想一直数到三十万次引用,但我觉得也就 Chris Manning 那个级别,差不多就到头了。那么,如果你至少融过一百万美元,请举手。如果你至少融过五百万美元、至少一千万美元、至少五千万美元,请举手。这边还有一位。我们

[01:35] **SPEAKER_03:** still got two over here. All right. Okay. Awesome. The hidden mission that I'll also kind of add on this is we had, Harj and I had this

> 这边还有两位。好的。好吧。太棒了。我还想补充一个隐藏的使命,就是我和 Harj 有过一次

[01:45] **SPEAKER_03:** awesome breakfast in Woodside and this place is so, so unique and special. And we kind of just don't use it enough at YC. So the hidden mission is to make Pioneer great again. And so I went through winter 16 here. It was an unbelievable time. I think 140 companies

> 在 Woodside 的很棒的早餐,这个地方实在是太独特、太特别了。而我们在 YC 却没有好好利用它。所以这个隐藏使命就是让 Pioneer(先锋楼)再次伟大。我是 2016 年冬季批次在这里参加 YC 的。那真是一段难以置信的时光。我记得那一批有 140 家公司

[02:03] **SPEAKER_03:** went through that batch. 10 of the, 15 of them are unicorns. It's an insane number. Happy, Astronautus, Deepgram, all these companies were in the batch. And during that time, Sam

> 参加了那一批。其中有 10 家、15 家成了独角兽。这是个惊人的数字。Happy、Astronautus、Deepgram,所有这些公司都在那一批里。就在那段时间里,Sam

[02:16] **SPEAKER_03:** was still running the show and basically sitting right there would be me, Undercarpathy, Vaj Zaremba, and Greg Brockman, because they were starting this thing called OpenAI. And it was like the very early stages. And there was like not that many AI companies. And so they would ask me and Steve from Deepgram, like, what are you guys, what are you working on? What are the problems you're working on? They're looking for problems. They didn't

> 还在掌管着一切,基本上就坐在那边的是我、Andrej Karpathy、Wojciech Zaremba 和 Greg Brockman,因为他们当时正在创办一个叫 OpenAI 的东西。那还处在非常早期的阶段。当时 AI 公司也没那么多。所以他们会问我和 Deepgram 的 Steve,你们在做什么?你们在研究什么?你们在解决哪些问题?他们在寻找问题。他们甚至

[02:37] **SPEAKER_03:** even know what to research. And so it was such a, such a special time. This place is so special to me in particular, to Harj as well. And we just, it's, we don't really use it enough. So I wanted to kind

> 都不知道该研究什么。所以那真是一段非常非常特别的时光。这个地方对我个人来说非常特别,对 Harj 来说也是。而我们只是……我们真的没有好好利用它。所以我想

[02:49] **SPEAKER_03:** of make this community down here. And I also think that a hundred percent of the AI talent or AI people in the Bay Area, probably about half of them are in the city maybe is a good number. There's Anthropic, there's OpenAI, there's Cursor, there's all this stuff in the city. Then there's a lot that are down here that are not making the trek up to the city to join us. And so he's like, yes, emphatically yes. And so you have Google DeepMind right on the corner.

> 在这边打造这样一个社区。我还认为,湾区所有的 AI 人才、AI 从业者当中,可能大约有一半在旧金山市里,这或许是个不错的估计。市里有 Anthropic、有 OpenAI、有 Cursor,所有这些都在城里。然后还有很多人在南边这一带,他们不会大老远跑到城里来加入我们。所以他(Harj)说,是的,非常肯定地同意。所以你们看,Google DeepMind 就在街角。

[03:14] **SPEAKER_03:** You have Tesla, you have XAI, you have Thinking Machines, you have all these other people in Palo Alto. You have a lot of startups. And so I wanted to kind of like solve six birds with one stone and kind of pull together this community down here as well. And Harj is super excited about it as well. And so thank you very much Harj for letting us do

> 这里有 Tesla、有 xAI、有 Thinking Machines,还有帕洛阿尔托(Palo Alto)所有这些人。这里有很多初创公司。所以我想一石六鸟,把南边这一带的社区也聚拢起来。Harj 对此也非常兴奋。所以非常感谢 Harj 让我们能做

[03:32] **SPEAKER_03:** this. We got five great papers here coming up. The first one is Tanishq Speculative Speculative Decoding. You want to come up? All right.

> 这件事。我们接下来有五篇很棒的论文。第一篇是 Tanishq 讲的“投机性投机解码”(Speculative Speculative Decoding)。你要上来吗?好的。

[03:42] **SPEAKER_04:** It's all yours. Do you want me to pull it on? Yeah, I got you. Cool. I know it looks like maybe I was sloppy and I added an extra word in the title, but

> 交给你了。要我帮你把它调出来吗?好,我来搞定。酷。我知道标题看起来好像是我很马虎,多加了一个词,但

[03:55] **SPEAKER_04:** it is intentional and it'll make sense in a good time. My name is Tanishq. I'm a grad student at Stanford. This is a project I worked on with Trie Dao and Avner May. I'm going

> 那是故意的,到时候你们就会明白了。我叫 Tanishq。我是斯坦福的一名研究生。这是我和 Tri Dao 以及 Avner May 一起做的一个项目。我打算

[04:05] **SPEAKER_04:** to be evangelizing inference for people today. Hopefully you'll be inference enjoyers by the end. Okay. I'm not sure how much I have to motivate to inference. I worked on training before

> 今天向大家“布道”推理(inference)。希望到最后你们都能成为推理的爱好者。好的。我不确定我需要为推理做多少铺垫来说服你们它的重要性。我在做推理之前先做的是训练,

[04:17] **SPEAKER_04:** inference and I sort of, the sort of mental model I had in mind for how inference works was, you know, you do this beautiful craftsmanship during the training process and you get these like, you know, very intricate weights and then you kind of just hand it off and use them to generate tokens. In my mind, it's sort of like you have the weights, just multiply the matrices. It's why do you need a team for it? I was very confused, but there is in fact a lot of subtlety involved. It's a lot of fun. It's a lot of fun. It's a lot

> 我脑子里对推理如何工作的心智模型大致是这样的:你在训练过程中做出这种精美的手工艺,得到这些非常精巧的权重,然后你就把它交出去,用它们来生成 token。在我看来,就好像你有了权重,只要做矩阵乘法就行了。这有什么好需要一个团队的?我当时非常困惑,但事实上这里面涉及很多微妙之处。这非常有意思。非常有意思。非常

[04:43] **SPEAKER_04:** of fun. The algorithms and systems behind inference at scale. I'm not sure I need to spend too long talking about why inference is important. There is one point I want to make that I don't hear people talk about enough. So things you may have heard are that inference

> 有意思。这就是大规模推理背后的算法与系统。我不确定我需要花太多时间来讲为什么推理很重要。但有一点我想强调,我觉得大家谈得还不够。你们可能听说过的是,推理

[05:00] **SPEAKER_04:** costs are high. They dominate training costs when you're serving a model for billions of users or, you know, 10 cloud code power users, that's trillions of tokens. Not only are we inference costs dominating training costs, but even within training, RL is starting to exceed the compute requirements of pre-training. And what is RL but a wrapper on inference? So these are two things you've probably heard before. The third is one I fear isn't really

> 成本很高。当你为数十亿用户,或者说十个 cloud code 的重度用户提供服务时,推理成本会压倒训练成本,那可是数万亿个 token。不仅推理成本压倒了训练成本,甚至在训练内部,强化学习(RL)的算力需求都开始超过预训练了。而 RL 不就是推理外面套了一层壳吗?所以这两点你们大概都听说过。第三点我担心大家其实

[05:30] **SPEAKER_04:** talked about, but it's the reason that I started working on inference. And I use the phrase working on inference lightly. This was the only inference project I've ever done. But the reason I got interested in making inference fast. It was not because of cost or for convenience. It was entirely because of capability. So

> 谈得不够,但正是这一点让我开始做推理的。我说“做推理”其实是说得比较随意——这是我做过的唯一一个推理项目。但我之所以对让推理变快产生兴趣,并不是因为成本或便利,而完全是因为能力(capability)。所以

[05:48] **SPEAKER_04:** the claim I'm going to make, and maybe this is the one thing to take away from the message I'm trying to send in this talk, is that inference today is seen as a sort of like cost or convenience lever. But in one, two, three years, inference is going to be seen as a capability. And what I mean by that is that if you have a method, an algorithm, a system, where its performance scales with the amount of thinking it does. Then fundamentally, the speed at which you can do inference, the tokens per second, is exactly the peak intelligence that you can deliver. So inference should be thought of

> 我要提出的论断——也许这就是我这次演讲想传达的、值得你们记住的那一点——是:今天推理被看作是一种成本或便利的杠杆。但在一到三年内,推理将被看作是一种能力。我的意思是,如果你有一个方法、一个算法、一个系统,它的表现会随着它思考的量而扩展,那么从根本上说,你能做推理的速度,也就是每秒生成的 token 数,恰恰就是你能交付的智能上限。所以推理应该被看作

[06:24] **SPEAKER_04:** as not so much as a cost or convenience factor, but as a capability. And that's why I got interested in it. I wanted to work towards the future where we have an entire data center of 20,000 B200s just working on the Riemann hypothesis. Okay. Yes. That's the future that

> 与其说是成本或便利的因素,不如说是一种能力。这就是我对它产生兴趣的原因。我想朝着这样一个未来努力:我们有一整个数据中心的两万块 B200 芯片,专门用来攻克黎曼猜想。好的,没错。那就是我

[06:43] **SPEAKER_04:** I had in mind. I'm a little outdated because it has an A100 on it. But yeah. Okay. So to motivate things,

> 心里想的那个未来。我这张图有点过时了,因为上面画的是 A100。不过没关系。好的。那么,为了给大家一点直观感受,

[06:51] **SPEAKER_04:** here is an example of fast inference. So I'm going to give you a little demo of three algorithms side by side. We're going to sample a code prompt from VLLM with just normal autoregressive decoding. We're going to use their speculative decoding. And then I'm going to put next to

> 这里有一个快速推理的例子。我要给你们做一个三种算法并排的小演示。我们会用普通的自回归解码,从 vLLM 上采样一个代码提示。我们会用它们的投机解码(speculative decoding)。然后我会在旁边放上

[07:07] **SPEAKER_04:** it the sort of janky hand-rolled inference engine I wrote over a summer for this project, whose main strength is just that it implements a new algorithm. And so you can see them side by side. SSD's on the right. And you can see it is quite a bit faster than what you can get if you tried to use an open-source engine. And it's

> 我为这个项目在一个夏天里手写的、有点简陋的推理引擎,它的主要优势就在于它实现了一个新算法。这样你们就能并排看到它们了。SSD 在右边。你可以看到它比你用一个开源引擎所能得到的要快不少。而且这

[07:24] **SPEAKER_04:** not the systems, it's the algorithm. So, yeah, that's what we want to work towards, understanding both how speculative decoding works as well as the algorithm on the right. Okay. I'll start by introducing what speculative decoding is, how it works, and then we'll move into what speculative speculative decoding is. strong understanding of how speculative decoding works the the problem that ssd is trying to solve

> 不是系统层面的原因,而是算法的原因。所以,是的,这就是我们想要达成的目标:既理解投机解码是如何工作的,也理解右边这个算法。好的。我先介绍一下什么是投机解码、它是如何工作的,然后我们再进入什么是“投机性投机解码”。一旦你对投机解码的工作原理有了扎实的理解,SSD 想要解决的问题

[07:50] **SPEAKER_04:** will feel very motivated and the algorithm should just become clear in good time okay so this is the schematic i'm going to use to explain how vanilla speculative decoding works um it has a small model the tiny llama up top as well as a big model the big llama and our goal is simply to sample fast from the big llama we want tokens generated from the big model and we're going to use a small model as a sort of proxy or an instrument to be able to sample quickly from the big model okay so what the draft is going to be responsible for is basically generating a bunch of tokens one by one one by one is important it's auto-regressive so you need to do three forward passes on the draft or you know however many some constant number and these are going to be guesses for what the draft believes that the big model is going to output next it wants to sort of predict ahead of time the job that the big model has i'm going to call it the target model is very important to verify these guesses what does verification mean verification means doing one forward pass over these generated tokens to see how likely it is that the big model would have generated them the sort of key asymmetry here the reason that speculation works is that it is easier to verify than to generate this is a feature of the transformer architecture where you can get the probabilities for many tokens in a sequence in parallel in one forward pass um but you can't generate them in parallel auto aggressive decoding as uh one at a time so we're leaving the auto regressive decoding which is slow uh to a very quick and small model and then we're doing just one forward pass on these tokens and the way you verify tokens is basically by having the big model look at the probabilities of each of the generated tokens and see how plausible it is that it would have generated those tokens and sort of the intuition here is that we will accept precisely those tokens that the big model could plausibly have generated its probabilities were reasonably high their subtlety isn't exactly what the algorithm is that i'm going to gloss over but that's the way to think about it and then we're going to find a point perhaps where we don't think it's plausible the big model would have generated those tokens and we're going to reject those tokens so in the little schematic on the right there the draft samples three and the big model verifies them and concludes that only the first token was something it would plausibly have generated it will reject the second token onwards and importantly this is a sort of critical but subtle detail of a less speculative decoding because you have the probabilities that each of the sequence positions you can sample an extra token at the point at which you rejected a token for free as in without doing any more forward passes and so that yellow token is what i'm going to call a bonus token that you sample for free this is going to be important in ssd um so yeah that's uh that's an important conceptual point and this sort of sets the stage for how ssd works okay we have our schematic and the way we've set up speculative decoding is that it's a way to exchange flops for latency so speculation in general is not actually something that uh only llms do it's like a deep idea in computer science it's used in cpus as well where the general philosophy is that you pre-compute something ahead of time some of what you pre-compute may be useless because it may be an incorrect prediction of the future but if you're right you get to fast forward in time um and you get lower latency as a result so the the sort of like moral philosophy of ssd is that it's currency exchange the difficulty with normal speculative decoding is that you can't push this arbitrarily far you cannot keep sampling more and more tokens on the draft and keep getting speed ups because at some point you're going to get to a point where you're spending a lot of time drafting and you're not accepting all that many tokens and in particular like a big bottleneck in vanilla speculative decoding is the sequential dependence between the small llama and the big llama the drafting in round t has to take place before the verification of those tokens and the drafting in round t plus one can't take place before you know the outcome of verification of the previous round because you need that as a prefix to draw draft on top of so there's a logical dependency here the goal of ssd is very simple there's a lot of gnarly and subtle details but the high level idea is incredibly simple it is simply to parallelize the sequential operation we want drafting and verification to be happening at the same time normally in speculation they happen on the same hardware and that's fine because there's only one of them happening at a time in our setup they're going to be happening at the same time so we're not going to be co-locating them and the main question basically becomes how do you parallelize this inherently sequential algorithm that has a logical dependency and the way we're going to do that is we are going to have the draft model send back its draft tokens in a certain round so we've sent back a bunch of blue tokens that's now the job of the verifier to do a forward pass over and verify and this is going to take a little bit longer than a while because the verifier is a big model what we on the draft are going to do is basically start anticipating the most likely verification outcomes immediately as soon as we send back like a certain round of speculation and once we we have in mind some of the most likely verification outcomes we are going to start drafting the next round on top of those immediately while verification is taking place if we're right the next time the verifier asks for a draft we'll have it ready immediately we're entirely hiding the latency of drafting if we're wrong well we'll have to figure out a backup strategy and there's uh there's there's there's some subtleties on what you do and how you do it there um so yeah the way that speculative decoding looks like this and perhaps unsurprisingly the analog for ssd is this diagram on the right we're now drafting and verification happen in parallel the the principal difficulty or algorithmic design space in ssd is how do you predict verification outcomes ahead of time i thought verification is where you are leveraging the intelligence of the big model that should by construction be difficult to predict and the intuition for why it's plausible at all is that you can make many guesses on the draft for what a verification outcome is and a verification outcome here is just you know a plausible number of accepted tokens and then a bonus token on top of that now this is hard to predict because the bonus token comes from a vocabulary which has size you know tens to hundreds of thousands um so it's a large space to cover um but it turns out you can do it um reasonably well you can get it right about 80 to 90 of the time which is more than enough to get big speed ups and the way we do that the short of it is basically we use information on the draft to predict what the verification outcome is likely to be when we generated the blue tokens on the draft we had other tokens that we chose not to sample those other tokens are plausible verification bonus token candidates and so you basically use information from the token distributions of the draft model to predict what likely outcomes on the target are and then once you have all of that you can decode them in parallel as just different sequences that you're decoding on top of a shared prefix and voila it uh it gives you speed ups because you get to hide the latency of drafting altogether um there's also a an additional bonus that since verification actually kind of takes a while you get more time to draft uh in the first place you can draft more tokens which increases the expected tokens per round and sort of gives you further speed ups there's a bunch of stuff that we work through in the paper that's uh that sort of reckoning with the the implementation details of this one of it is how you handle cash misses one plausible thing you could do perhaps naively is to just fall back to ordinary speculation just in time it turns out that actually this is not always optimal um there's trade-offs you know as batch size increases you're gonna fail to predict some of the sequences verification outcomes um and so you need different ways to predict and handle cash misses should you be allocating your compute on the draft equally amongst plausible prefix length the short answer is no you can be clever about it and all of this trickery just helps you increase your cash hit rate so to speak the amount of time you're able to correctly predict verification outcomes and there's there's some trade-offs between cash hit rate and the actual quality of the drafting you're doing um and this is totally non-obvious um and and we go into why that exists and how you can navigate it in the paper um I'm happy to talk about it in in QA as well um okay so what do you get for the the price of this uh mind-numbing complexity and pain wrangling an inference engine well you get the privilege of watching a number go up which I guess is the North Star of all AI research and so here we have a bunch of inference algorithms and inference engines the blue ones are sort of uh my inference engine and uh the light blue is just the baseline implementation of speculative decoding the red is SG Lang which is you know of all the inference engines we tried the fastest with speculative decoding and the dark blue is is SSD um and normally speculative decoding um is a is a win for latency but it's sort of unclear whether it's useful for throughput um for us to turn in in this setting it's actually a win for both um and so you get numbers going up and you also get the ability next time you are at a San Francisco house party um to see other people dancing and knowing in the corner that you know what it takes to sample at 300 tokens per second uh for llama 370b on 4H 100s so this is uh sensitive information um but yeah that's that's about it

> 就会显得非常有动机,而这个算法也会在适当的时候自然变得清晰。好的,这是我要用来解释普通(vanilla)投机解码如何工作的示意图。上面有一个小模型,tiny llama,还有一个大模型,big llama。我们的目标很简单,就是要快速地从大模型里采样——我们想要大模型生成的 token,而我们会用一个小模型作为一种代理或工具,来实现从大模型快速采样。好的,草稿模型(draft)负责的基本上就是逐个逐个地生成一堆 token——“逐个”很重要,它是自回归的,所以你需要在草稿模型上做三次前向传播,或者说某个固定次数。这些 token 是草稿模型对大模型接下来会输出什么的猜测,它想提前预测。大模型的工作——我把它叫做目标模型(target model)——非常重要,就是去验证这些猜测。验证是什么意思?验证意味着对这些生成的 token 做一次前向传播,看看大模型有多大可能会生成它们。这里的关键不对称性,也就是投机之所以有效的原因,在于验证比生成更容易。这是 Transformer 架构的一个特性:你可以在一次前向传播中并行地得到序列中很多 token 的概率,但你无法并行地生成它们——自回归解码是一次一个地进行的。所以我们把缓慢的自回归解码交给一个非常快速的小模型来做,然后我们只对这些 token 做一次前向传播。验证 token 的方式,基本上就是让大模型看每个生成 token 的概率,看看它生成那些 token 有多合理。这里的直觉是:我们会恰好接受那些大模型合理地可能生成的 token,也就是概率相当高的那些。其中的细节并不完全等同于真正的算法,我会略过,但你可以这样来理解。然后我们会找到某个点,在那里我们认为大模型不太可能生成那些 token,于是我们就拒绝那些 token。所以在右边那个小示意图里,草稿模型采样了三个 token,大模型验证它们,得出结论只有第一个 token 是它合理地会生成的,它会从第二个 token 起全部拒绝。而且重要的是,这是投机解码一个关键但微妙的细节:因为你已经有了每个序列位置的概率,你可以在拒绝某个 token 的那个点上免费地再采样一个额外 token——所谓免费,就是不需要再做任何前向传播。所以那个黄色的 token,我把它叫做“奖励 token”(bonus token),是你免费采到的。这在 SSD 里会很重要。所以,是的,这是一个重要的概念点,它为 SSD 的工作原理铺好了台。好的,我们有了示意图。我们设置投机解码的方式,本质上是一种用浮点运算量(flops)去换取延迟(latency)的手段。投机总体上其实并不是只有大语言模型才做的事——它是计算机科学里一个很深的思想,在 CPU 里也用到,总体哲学就是你提前预计算某些东西,你预计算的一部分可能没用,因为它可能是对未来的错误预测,但如果你猜对了,你就能在时间上快进,从而获得更低的延迟。所以 SSD 的“道德哲学”就是货币兑换。普通投机解码的困难在于,你无法把它无限推进——你不能在草稿模型上不断采样越来越多的 token,还一直获得加速,因为到某个点你会发现你花了大量时间在草稿上,却没有接受多少 token。特别地,普通投机解码的一个大瓶颈是小 llama 和大 llama 之间的顺序依赖:第 t 轮的草稿必须在这些 token 被验证之前完成,而第 t+1 轮的草稿又不能在你知道上一轮验证结果之前进行,因为你需要那个结果作为前缀来继续起草。所以这里存在一个逻辑依赖。SSD 的目标非常简单——虽然有很多棘手而微妙的细节,但高层思想极其简单——就是把这个顺序操作并行化。我们想让起草和验证同时发生。通常在投机里它们在同一硬件上进行,这没问题,因为同一时刻只有一个在跑;但在我们的设置里它们会同时进行,所以我们不会把它们放在同一处。主要问题基本就变成了:你如何把这个天生顺序、还带逻辑依赖的算法并行化?我们的做法是,让草稿模型在某一轮把它的草稿 token 送回去——我们送回一堆蓝色 token,现在轮到验证器去做一次前向传播来验证它们,而这会比一会儿更久一点,因为验证器是个大模型。而我们在草稿这边要做的,基本上就是在送回某一轮投机之后,立刻开始预判最可能的验证结果;一旦我们心里有了一些最可能的验证结果,我们就会在验证进行的同时,立刻基于这些结果开始起草下一轮。如果我们猜对了,下次验证器来要草稿时,我们已经立刻准备好了——我们就完全隐藏了起草的延迟。如果我们猜错了,那我们就得想个备用策略,关于该怎么做、如何做,这里有一些微妙之处。所以,是的,投机解码看起来是这样,而 SSD 的对应版本大概不出所料就是右边这张图:现在起草和验证并行发生。SSD 里主要的困难,或者说算法设计空间,是你如何提前预测验证结果。我原以为验证正是你利用大模型智能的地方,按理说它应该很难预测。之所以这在某种程度上还算可行,直觉在于你可以在草稿这边对验证结果做很多猜测,而这里的验证结果无非就是一个合理的被接受 token 数量,再加上上面的一个奖励 token。这确实很难预测,因为奖励 token 来自一个词表,其规模是数万到数十万,所以这是个很大的空间要覆盖。但结果证明你可以做得相当好,你能有大约 80% 到 90% 的时候猜对,这已经足够带来巨大加速了。我们的做法,简而言之,基本上就是用草稿这边的信息来预测验证结果大概会是什么。当我们在草稿上生成蓝色 token 时,还有一些我们选择不去采样的其他 token,那些 token 就是合理的验证奖励 token 候选。所以你基本上是用草稿模型 token 分布里的信息,来预测目标模型上可能的结果。一旦你有了所有这些,你就可以把它们作为在共享前缀之上并行解码的不同序列并行解码——瞧,它就给你带来了加速,因为你完全隐藏了起草的延迟。还有一个额外的好处:因为验证其实要花上一会儿,你一开始就有更多时间去起草,你可以起草更多 token,这增加了每轮的期望 token 数,从而带来进一步的加速。论文里我们详细处理了一大堆东西,都是在应对它的实现细节。其中之一是你如何处理“缓存未命中”(cache miss)。一个也许显得很天真的可行做法是,及时地退回到普通投机。结果发现这其实并不总是最优的——存在权衡。随着批大小(batch size)增大,你会预测不出某些序列的验证结果,所以你需要不同的方式来预测和处理缓存未命中。你应该把草稿上的算力在各个合理的前缀长度上平均分配吗?简短的回答是:不。你可以聪明地分配。所有这些技巧都只是帮你提高所谓的“缓存命中率”,也就是你能正确预测验证结果的比例。而缓存命中率和你实际起草的质量之间也存在一些权衡,这完全不是显而易见的,我们在论文里探讨了它为什么存在以及你如何驾驭它。我也很乐意在问答环节聊这个。好的,那么付出这种令人头昏脑涨的复杂度、以及跟推理引擎搏斗的痛苦,你得到什么回报呢?你获得了看着一个数字往上走的特权,我想这大概是所有 AI 研究的北极星。所以这里我们有一堆推理算法和推理引擎:蓝色的算是我的推理引擎,浅蓝色是投机解码的基线实现,红色是 SGLang——在我们试过的所有推理引擎里,它是带投机解码时最快的,而深蓝色就是 SSD。通常投机解码在延迟上是有利的,但它对吞吐量是否有用则不太清楚。而对我们来说,在这个设置下,它实际上对两者都有利。所以你看到数字往上走,而且你还获得了这样一种能力:下次你在旧金山的家庭派对上,看着别人跳舞,而你在角落里知道——你懂得在四块 H100 上让 llama 3 70B 以每秒 300 个 token 采样需要付出什么。所以这是敏感信息。不过,是的,大概就是这样。

[17:23] **SPEAKER_03:** thank you all right that was awesome okay so for this next paper this is um my first experience being scooped the only issue is that he didn't talk to me and he did it six months before me um but uh Isaac can vouch for me on this and maybe Robert as well I basically fell in love with the division policy paper I was like this is definitely like you know a full uh predicting like th Horizon steps for your robotic control um we have these amazing video models why don't we just use the video model to like run this like at test time to like play out the movie and where do I end up and then you have your classic push T and then I started like looking around uh and then d-mind of course already did it so so I wasted like a month and it was not happy but

> 谢谢。好的,那太棒了。好,接下来这篇论文,这是我第一次被人抢先(scooped)。唯一的问题是他没跟我商量,而且他比我早了六个月做出来。不过 Isaac 可以给我作证,也许 Robert 也可以。我基本上是爱上了扩散策略(diffusion policy)那篇论文,我当时想,这绝对是……你懂的,为你的机器人控制完整地预测未来若干步(H 步 horizon)。我们有这些了不起的视频模型,为什么不干脆在测试时用视频模型来跑一遍,把这部“电影”播放出来,看看我最后会落到哪里?然后你有经典的 push T 任务。然后我开始四处打听,结果发现 DeepMind 当然早就做过了。所以我白白浪费了大约一个月,当时挺不开心的,但

[18:25] **SPEAKER_01:** anyway thank you very much please welcome Stanis hi everyone I'm Stanis I'm a staff research scientist at Google DeepMind uh currently I'm co-leading a new project on word modeling for robotics where we try to build general purpose policies on top of video and word models but this is an early work that I did about two years ago so this was before I switched to uh hardcore robotics and going to hardware really scaling up the data but uh you can probably see a lot of very similar ideas early version of the ideas demonstrated on toy problems okay so uh first to give some background what is model predictive control so model predictive control also called the receding Horizon control uses a dynamics model or some people also call it a word model and an action selector mechanism which is a planner to construct regions that can solve a wide variety of tasks by means of maximizing a known objective so the main advantages of model predictive control is it can adapt to normal reward functions at test time so the dynamics model are also easier to learn and generates better than just policies and the action proposal the next model factorization also allows easy adaptation to normal Dynamics so we're going to demonstrate some of these in later experiments but basically here we are showing the overall idea which is extremely simple we have an action proposal which proposes a sequence of actions we have a dynamics model which can evolve these actions and give you the future state and finally we have some objective functions that we are trying to optimize we basically use a planner to optimize that and pick the actions and execute it in the environment so what is the diffusion model operative control so the motivation mainly is uh the number of problems we need to address in order to make MPC effective in practice why the dynamics model needs to be accurate to avoid the problem of compounding errors and two the planning algorithm also needs to be powerful enough to select a good sequence of actions so with dmpc what we did is to use diffusion models to learn both multi-step action proposals and multi-step Dynamics models so the advantages are mainly to reduce compounding errors and we also found that it can simplify the planning algorithm essentially we can just use a very simple sampling based planner and we can already outperform a lot of the previous approaches so before we dive into the details also want to give a hierarchical view of some related works we organized so there are a lot of related works in the literature and we organize it in this way where we basically look at how different approaches so basically all approaches essentially try to build a joint distribution of the states and the actions but they do it in different ways and also use the different components in different ways so for example you can build it in a factorized way where you have row a which is your policy predicting the actions and then condition on the action predicts the state which is a dynamics model and for this you have the dynamic paradigm where you basically learn a model and use the model to also generate data in the imagination you can also do MPC where you essentially use a planner to select the actions and we also have some there are also approaches where you build a joint model of the state and actions and you're essentially also doing MPC and there are also model free approaches where you directly learn a policy I won't dive into the full details but there are basically different trade-offs in terms of runtime plan whether we can do runtime planning and adapting to normal rewards and adapting to normal Dynamics leveraging non-expert data and also the general speed at runtime and there is also the distinction between whether you're doing single step modeling or multi-step modeling okay so coming to the diffusion model diffusion model has enjoyed a lot of successes in generating AI especially for generating images and videos but in recent years they also found a lot of successes in robotics so currently so here I'm also doing a slide where this is a kind of the exploration space for diffusion-based I would call it diffusion-based agents so we of course start with the diffusion policy where we condition on the observation and generate future actions but then we also have this work called diffuser which is you can think of it as a way to joint jointly model observations and the states but in a toy space there are of course these ideas that are poured in tons of different papers but this is just a very simple and conceptual way to describe it and then there's also decision diffuser where we condition on the observations we directly generate future which condition on the history directly generate future observations and then try to separate inverse Dynamics model to derive the actions and finally we have the diffusion model predictive control where we first have an action proposal to propose future actions and use it to evolve it and then use a planner to select the actions there are different trade-offs among these so for example diffusion policy is sold on complex complex control like day-to-day we still rely on it a lot but this requires expert demonstrations so essentially you can't move out of the behavior cloning paradigm for the future it's a jointly modeling state and action so it has the implicit word modeling and also work model-based actions so this is a very simple way to do this the planning and this is actually something that we are trying to explore at a scale as similar ideas but then there's also decision diffuser where you do observation only learning the main benefit of this is it allows you to leverage of video only data to learn from video only data because for robotics the data is a many bottleneck and then finally there's a diffusion MPC which allows us to do runtime adaptation to novel rewards and all dynamics so what does the algorithm look like it actually is extremely simple we have often data set and we have some hyper parameters essentially we are learning a couple of learning a couple of models all from the offline data sets we're learning a policy which given the current observation predicts the actions we're learning a dynamics model which givens givens actions evolves conditions to predict the future states and basically after learning all these at at inference time when we actually deploy it as a policy we sample the action proposal and score it rank it and pick the best but the main difference compared to previous approaches is we adopted a multi-step action proposal which is essentially very similar to a diffusion policy but if you point out more diverse data it can give you more coverage in terms of the action space and we are also using a multi-step dynamics model which allows you to evolve for a long time present without a lot of compounding error and this allows us to and also there's a fact that we leverage a diffusion model which is a really powerful way to model data especially multi-model data and what we observed empirically is the stronger modeling capabilities also allows us to simplify the planning algorithm so that we can just use such a simple planner to do to solve the tasks yeah also contrasting with a few of the representative path works including model-based offline control offline planning and this diffuser work which I mentioned it learns a joint model and uses a classifier free guidance for planning okay uh so yeah next to dive into some results there are lots of numbers but the short answer is we obtain very competitive results in fixed reward single task setups this is just to demonstrate that the approach when you deploy it in a single reward fixed reward single task setup can perform competitively to the current state-of-the-art previous state-of-the-art approaches but I think there are a couple of more interesting properties of the DMPC why is it can adapt to no rewards at runtime here we are showing some examples where essentially we train the model to these are very simple module tasks but we train the model to just local motion tasks run forward and jump Etc but at inference time we can just by changing the reward function to make it exhibit novel behaviors like jumping Etc so here's another example where we show that dmpc can adapt to normal Dynamics while this kind of joint modeling approaches struggle this is really the benefit of the factorization of the action proposal and the dynamics model so that way you get a lot of So here, the idea is we can keep the action proposal the same, but we have scenarios where the dynamics of the environment changed. So, for example, the walker has a broken left ankle, and as a result, when it starts to execute actions, the consequences of the actions change. So in such cases, because of the factorized representation in DMPC, we can simply just adapt the dynamics model on some play data collected in the new environment, and we observe that we can recover a lot of the performance because of the changing dynamics. Finally, we dug into the various components of the DMPC design, and we demonstrated that the different components in DMPC basically contributed to the change in the dynamics of the environment. All right, and that was the last Google DeepMind.

> 总之,非常感谢,请大家欢迎 Stanis。大家好,我是 Stanis,我是 Google DeepMind 的一名资深研究科学家。目前我在共同主导一个关于机器人世界建模的新项目,我们试图在视频模型和世界模型之上构建通用策略。但今天要讲的是我大约两年前做的一个早期工作,那是在我转向硬核机器人、投入到硬件、真正大规模扩展数据之前。不过你们大概能看到很多非常相似的想法,是这些想法在玩具问题上演示的早期版本。好的,首先给点背景:什么是模型预测控制(MPC)?模型预测控制,也叫滚动时域控制(receding horizon control),它使用一个动力学模型(有人也叫世界模型)和一个动作选择机制(也就是规划器 planner),通过最大化一个已知目标来构造能解决多种任务的方案。模型预测控制的主要优势是:它可以在测试时适应新的奖励函数;动力学模型也比策略更容易学习、泛化得更好;而“动作提议 + 下一步模型”的这种分解也允许它轻松适应新的动力学。我们会在后面的实验里演示其中一些。基本上,这里展示的整体思路极其简单:我们有一个动作提议器(action proposal)提出一串动作,我们有一个动力学模型可以演化这些动作、给出未来状态,最后我们有一些想要优化的目标函数。我们基本上用一个规划器来优化它、选出动作,并在环境中执行。那么什么是扩散模型预测控制(DMPC)呢?动机主要是我们要让 MPC 在实践中有效所需解决的一些问题:其一,动力学模型需要足够准确,以避免误差累积(compounding errors)的问题;其二,规划算法也需要足够强大,以选出一串好的动作。在 DMPC 里,我们所做的是用扩散模型来同时学习多步动作提议和多步动力学模型。其优势主要是减少误差累积,而且我们还发现它能简化规划算法——本质上我们只用一个非常简单的、基于采样的规划器,就已经能超过很多以往的方法。在深入细节之前,我还想给出一个相关工作的层次化视角。文献里有很多相关工作,我们是这样组织的:基本上所有方法本质上都在试图构建状态和动作的联合分布,只是它们的做法不同,使用各组件的方式也不同。比如你可以用分解的方式来构建,其中 ρ_a 是你的策略,预测动作,然后在动作的条件下预测状态,也就是动力学模型;基于此有 Dyna 范式,你学一个模型,并用这个模型在“想象”中生成数据;你也可以做 MPC,即用一个规划器来选动作;也有一些方法是构建状态和动作的联合模型,本质上也是在做 MPC;还有免模型(model-free)的方法,直接学一个策略。我不会深入所有细节,但基本上它们在若干方面存在不同权衡:能否进行运行时规划、能否适应新奖励、能否适应新动力学、能否利用非专家数据,以及运行时的总体速度;此外还有单步建模还是多步建模的区别。好的,来到扩散模型。扩散模型在生成式 AI 上取得了很多成功,尤其是在生成图像和视频方面,但近年来在机器人领域也取得了很多成功。这里我做了一张幻灯片,这算是基于扩散的智能体(diffusion-based agents)的探索空间。我们当然从扩散策略(diffusion policy)开始,它以观测为条件生成未来动作;然后还有一个叫 Diffuser 的工作,你可以把它理解为一种在玩具空间里联合建模观测和状态的方式;当然这些想法散见于大量不同的论文,但这只是一个非常简单、概念化的描述方式;还有 Decision Diffuser,它以观测为条件、以历史为条件直接生成未来的观测,然后用一个单独的逆动力学模型来推导动作;最后是扩散模型预测控制,我们先有一个动作提议器提出未来动作,用它来演化,然后用规划器来选动作。这些方法之间有不同的权衡:比如扩散策略在复杂控制上表现出色,像日常任务我们仍然很依赖它,但它需要专家演示,本质上你走不出行为克隆(behavior cloning)的范式;它联合建模状态和动作,所以隐含了世界建模,也有基于世界模型的动作,这是一种非常简单的规划方式,这实际上也是我们正在尝试大规模探索的类似思路;然后还有 Decision Diffuser,你做仅观测的学习,它的主要好处是让你能利用仅有视频的数据来学习,因为对机器人来说数据是一大瓶颈;最后是扩散 MPC,它让我们能在运行时适应新奖励和新动力学。那么算法长什么样呢?其实极其简单。我们有一个离线数据集和一些超参数,本质上我们全都从离线数据集里学习几个模型:我们学一个策略,给定当前观测预测动作;我们学一个动力学模型,给定动作演化并预测未来状态。基本上学完这些之后,在推理时,当我们真正把它作为策略部署时,我们采样动作提议、给它打分、排序,选出最好的。但与以往方法相比的主要区别是,我们采用了多步动作提议,它本质上与扩散策略很相似,但如果你喂给它更多样化的数据,它能在动作空间上给你更大的覆盖;我们还用了多步动力学模型,让你能演化很长时间而不产生大量误差累积。这让我们……而且还有一点是,我们利用了扩散模型,它是一种非常强大的数据建模方式,尤其是对多模态数据。我们在实验中观察到,更强的建模能力也让我们能简化规划算法,以至于我们只用这么简单的规划器就能解决任务。我们还与几个有代表性的过去工作做了对比,包括基于模型的离线控制、离线规划,以及我提到的 Diffuser——它学一个联合模型,并用无分类器引导(classifier-free guidance)来做规划。好的,那么接下来看一些结果。数字很多,但简短的结论是:在固定奖励的单任务设置下,我们取得了非常有竞争力的结果。这只是为了表明,当你把这个方法部署在单一固定奖励的单任务设置里时,它能与当前最先进(以及以往最先进)的方法相媲美。但我认为 DMPC 有几个更有意思的性质。为什么它能在运行时适应新奖励?这里我们展示一些例子,本质上我们把模型训练成……这些是非常简单的运动任务,我们只把模型训练成基本的移动任务,比如向前跑、跳等等,但在推理时,我们只要改变奖励函数,就能让它表现出新的行为,比如跳跃等等。这里还有另一个例子,我们展示 DMPC 能适应新动力学,而这类联合建模的方法在这方面则很吃力。这正是把动作提议器和动力学模型分解开来的好处。这样你就能获得很多……这里的想法是,我们可以保持动作提议器不变,但在某些场景里环境的动力学发生了变化。比如,行走者(walker)左脚踝断了,结果当它开始执行动作时,动作的后果就变了。在这种情况下,由于 DMPC 中的分解式表示,我们可以简单地只在新环境里收集的一些游玩数据(play data)上适配动力学模型,我们观察到即使动力学发生变化,我们也能恢复很多性能。最后,我们深入研究了 DMPC 设计中的各个组件,证明了 DMPC 中不同组件各自的贡献。好的,那就是最后一个 Google DeepMind 的部分了。

[29:52] **SPEAKER_03:** Thank you. All right, guys, is that a good distance? You all can hear me at the back?

> 谢谢。好的各位,这个距离可以吗?后排的各位能听到我说话吗?

[30:25] **SPEAKER_00:** All right, guys, is that a good distance? You all can hear me at the back? Cool, cool. Yeah, I'm enjoying a cool little period in life where I started working on world models a couple of years ago, kind of before they got really hot, and now they're enjoying a moment in the sun. And suddenly everyone wants to talk to me, which is nice.

> 好的各位,这个距离可以吗?后排的各位能听到我吗?好,好。是的,我正享受着人生中一段挺酷的小时光——几年前我开始研究世界模型,那时它们还没真正火起来,而现在它们正风光无限。突然之间大家都想找我聊聊,这挺不错的。

[30:37] **SPEAKER_00:** I'm presenting Lay World Model, which is a call out, of course, out of Yann LeCun's group. QR code here if you want to follow along with the project page, but I'll explain through it. And yeah, really excited to talk to you about this one. Hidden in this presentation is really like a billion-dollar question, and it's not hyperbole. Yann LeCun's raise of $1.03 billion back in March.

> 我要讲的是 LeJEPA 世界模型(Lay World Model),它当然是出自 Yann LeCun 的团队。这里有个二维码,如果你想跟着看项目页面的话,不过我会讲解一遍。是的,我很高兴能和大家聊这篇。这个演讲里藏着一个真正意义上的“十亿美元问题”,而且这不是夸张——Yann LeCun 在今年三月融了 10.3 亿美元。

[30:55] **SPEAKER_00:** Basically, just to train world models is sort of what this presentation is about. I want to get at some of the questions that they're going to be testing. First five slides here, just going to do some basics on world models. I think we've all heard the term, but I want to just make sure we're all on the same page. And then we'll jump into what this paper is really offering and what it means for world models at large.

> 基本上就是为了训练世界模型,这大致就是这次演讲的主题。我想触及一些他们将要检验的问题。前五张幻灯片我会讲一些世界模型的基础。我想我们都听过这个词,但我想确保大家在同一个认知起点上。然后我们会进入这篇论文真正提供了什么,以及它对整个世界模型领域意味着什么。

[31:13] **SPEAKER_00:** But first of all, world models, what are they? Why do we care about them? So really, it's about learning the dynamics of the world, which is to say we're trying to come up with some model. Typically, we're using like a big neural network to predict how a system will change over time based on its inputs. So you have your current state or scenario using S for notation here.

> 但首先,世界模型是什么?我们为什么要关心它们?其实它讲的是学习世界的动力学,也就是说我们试图构造某个模型。通常我们用一个大的神经网络来预测:一个系统会如何随时间根据它的输入而变化。所以你有当前的状态或情景,这里用 S 来表示。

[31:30] **SPEAKER_00:** You're applying some action. Maybe that's like a movement or a command for a robot or a language command for a robot. And then you're trying to predict like what its outcome is going to be, like what scenario will it end up in once it's executed that action. So you're really trying to model the system or the environment that the robot is in, modeling the world. It's a world model.

> 你施加某个动作。也许是一次移动,或者给机器人的一个指令,或者给机器人的一个语言命令。然后你试图预测它的结果会是什么,比如一旦它执行了那个动作,它会落到什么样的情景里。所以你其实是在对机器人所处的系统或环境建模,对世界建模。这就是世界模型。

[31:46] **SPEAKER_00:** These kinds of models are really cool. They enable a few really interesting capabilities. One of them is generating imagined outcomes. We've probably all seen like this sort of. Beard kind of hallucinating imagination sequences coming out of world models over the last couple of years.

> 这类模型真的很酷。它们带来了几种非常有意思的能力。其中之一是生成“想象出来的”结果。过去这几年,我们大概都见过世界模型产出的那种略带诡异、如同幻觉般的想象序列。

[32:00] **SPEAKER_00:** We'll talk more about those and why they're useful. This allows us to get to model based control. I'm glad Stan has kind of explained that in the last talk for me, so I'll skip over it. And the last piece is really cool. Surprise quantification.

> 我们会更多谈谈这些以及它们为什么有用。这让我们能进入基于模型的控制。我很高兴 Stan 在上一个演讲里已经替我解释过了,所以我会跳过它。最后一部分非常酷:惊讶度量化(surprise quantification)。

[32:11] **SPEAKER_00:** I'll get to that later, but a really powerful capability of world models. I wanted to communicate to you all that this is not a new idea at all. It's really just kind of new advertising or packaging on an old idea. So I started going back through Google Scholar and this is a paper that I think is. Older than the average age of this room from Europe's 1990.

> 我稍后会讲到它,但这是世界模型的一个非常强大的能力。我想告诉大家的是,这根本不是什么新想法,它其实只是给一个旧想法换了个新的宣传或包装。所以我回头翻了翻 Google Scholar,这是一篇我觉得比这个房间里平均年龄还老的论文,来自 1990 年的 NeurIPS(Europe's,即 NeurIPS 前身)。

[32:28] **SPEAKER_00:** And of course, Richard S. Sutton, who we know from reinforcement learning, basically describes exactly a modern world model, a black box that takes his input, its situation and its action that it's going to execute and outputs a prediction of its immediate next situation. So really, really old idea. And that's the fly off in Europe's 1990. Great.

> 当然,我们从强化学习里认识的 Richard S. Sutton,基本上就精确地描述了一个现代世界模型:一个黑箱,输入是它当前的情景和它将要执行的动作,输出是对它紧接着的下一个情景的预测。所以这真是个非常非常古老的想法。这就是 1990 年 NeurIPS 上的成果。很好。

[32:45] **SPEAKER_00:** So getting a little bit more explicit and changing the notation from state to observation, just because in real world systems, we typically don't have access to the exact true state. We typically have some observation from sensors. Oh, this is just an example. And I pulled up from some world models that we're training on a quadroder. So as an example, the observation that the quadroder gets might be its current kinematic state position, velocity, this kind of thing.

> 那么说得更明确一点,并把记号从“状态”改成“观测”,只是因为在真实世界的系统里,我们通常无法拿到确切的真实状态,我们通常只有来自传感器的某些观测。哦,这只是一个例子。我调出了我们在一台四旋翼(quadrotor)上训练的一些世界模型。举例来说,四旋翼得到的观测可能是它当前的运动学状态——位置、速度之类的。

[33:04] **SPEAKER_00:** In addition to the images that it's taking from a forward facing camera, the action might be a control input, in this case, a yaw and move back to the left. And then we want to make a prediction that says, well, if you do that action, you're going to end up slightly back in the room and looking to the left. And we actually want to generate what the sensor would result in in this case. So highly dimensional observations, images and also LIDAR. And things like that are completely on the table in world models.

> 除此之外还有它从前置摄像头拍到的图像。动作可能是一个控制输入,在这个例子里是偏航(yaw)并向左后方移动。然后我们想做一个预测:如果你执行那个动作,你会稍微退回到房间里、并朝向左看。我们实际上想生成在这种情况下传感器会得到什么结果。所以高维观测——图像,还有激光雷达(LIDAR)——诸如此类,在世界模型里都完全是可以处理的对象。

[33:28] **SPEAKER_00:** They're really challenging because action sequences can be quite long. And the really big thing is that the minimum in the optimization landscape for these kinds of models may not correspond to the desired behavior and more on that later. But hopefully you'll agree that if you've trained a system that's capable of doing this thing, it must have an internal model of the world and imbuing agents with an internal model of the world is potentially a very useful capability. And that really is the big question. Are we going to have model free or model based policies?

> 它们非常有挑战性,因为动作序列可能相当长。而真正重要的一点是,这类模型的优化地形中的极小值可能并不对应我们想要的行为——这点稍后再说。但希望你们会同意:如果你训练出了一个能做到这件事的系统,它必定拥有一个内部的世界模型;而给智能体赋予一个内部世界模型,可能是一种非常有用的能力。这确实就是那个大问题:我们将采用免模型(model-free)还是基于模型(model-based)的策略?

[33:54] **SPEAKER_00:** All right. Are agents going to have an internal model of the world or are they not? And this is sort of being fought out right now, both in the research community and in like the startup communities on the left model free. The idea is you're taking some observations, you're feeding this into some kind of big neural network, potentially with a bunch of interesting learning tricks there, but you're getting some optimal action out. So it's just mapping between observation and some optimal action.

> 好。智能体到底会不会拥有一个内部的世界模型?这件事眼下正在被激烈争论,既在研究界,也在创业界。左边是免模型:思路是你拿一些观测,把它喂进某种大神经网络(其中可能还有一堆有意思的学习技巧),然后你得到某个最优动作。所以它只是在观测和某个最优动作之间做映射。

[34:15] **SPEAKER_00:** But no point is there an explicit representation of what the future might look like if you execute that action. These kinds of models are pretty good. There is growing evidence to show that. Internal to these neural networks are highly obfuscated and challenging to interpret world models sort of in the in the weights. I will talk about a paper very briefly that speaks to that and maybe someone can present on it in a future week.

> 但在任何环节都没有一个显式的表示,来刻画“如果你执行那个动作,未来会是什么样子”。这类模型其实相当不错。而且有越来越多的证据表明,在这些神经网络内部——在权重里——其实隐藏着高度混淆、难以解释的世界模型。我会非常简短地讲一篇谈到这一点的论文,也许以后某一周可以有人来专门讲它。

[34:37] **SPEAKER_00:** And then over on the other side, model based approaches. Right. So now we're saying we're going to train this world model up explicitly and actually use that in our policy to be able to explicitly predict the outcome of potential actions. So, yeah, totally like two different species of policies, the model free stuff. Some of the weaknesses is they show a little bit of brittleness.

> 然后在另一边,是基于模型的方法。对。所以现在我们说,我们要显式地训练出这个世界模型,并在我们的策略里真正用上它,以便能够显式地预测潜在动作的结果。所以是的,这完全是两种不同物种的策略。免模型那一类,它的一些弱点是:它们在分布外(out of distribution)时会显得有点脆弱。

[34:54] **SPEAKER_00:** Out of distribution. Model based ones are great because you can kind of quantify modeling error. And this is really important when you're deploying things in the real world. We'll talk a little about this. I have a little asterisk here, some biological precedent, which we'll speak to more.

> 分布外的情况下。基于模型的那类很棒,因为你能在某种程度上量化建模误差。当你把东西部署到真实世界里时,这一点真的非常重要。我们会稍微聊聊这个。我这里打了个小星号——有一些生物学上的先例,我们后面会多谈一点。

[35:07] **SPEAKER_00:** And you have to have this additional mechanism, of course, which is a downside where you actually need to propose action candidates to evaluate with the world model, which I spoke to in the previous talk. This is a great paper. I just want to chuck this in there, which talks about how even model free based policies do have world models in them and are really, really cool paper. That. Hopefully can be presented in a future week.

> 当然,你必须有这样一个额外的机制——这算是个缺点——你实际上需要提出一些动作候选,再用世界模型去评估它们,这点我在上一个演讲里提到过。这是一篇很棒的论文,我就想顺便塞进来:它讲的是即便是免模型的策略,内部其实也确实含有世界模型,真是一篇非常非常酷的论文。希望以后某一周可以有人来讲它。

[35:27] **SPEAKER_00:** Just to make it concrete, before we jump into the paper, I wanted to just bring a little toy here just to show you what this looks like. So, of course, went to push T, like all good researchers do. And in push T, we basically just have an image of a little blue ball agent and you're trying to push the blue T into the green slot. The state is comprised of the observation is comprised of that image, plus the 2D position of the end effector and the 2D action of where you're going to move the end effector. So you can make a little architecture that looks like this.

> 为了讲得具体些,在进入论文之前,我想在这里搬出一个小玩具例子,给你们看看这大概是什么样子。当然,我用了 push T,就像所有好的研究者会做的那样。在 push T 里,我们基本上只有一张小蓝球智能体的图像,你要把蓝色的 T 形块推进绿色的槽里。状态由观测构成,观测由那张图像加上末端执行器(end effector)的二维位置、以及你要把末端执行器移动到哪里的二维动作构成。于是你可以搭一个大概长这样的小架构。

[35:50] **SPEAKER_00:** I just whip this up a couple hundred thousand parameters and. Oh. Let's play this. So if that's the actual rollout, this is what the model thinks the action sequence is going to do. So you can see it's a little bit wobbly because it's a tiny model, but we can certainly train up models of these kinds of toy environments and indeed more complex ones.

> 我随手就搭了个几十万参数的模型,然后……哦,我们来放一下这个。如果那是实际的推演(rollout),那么这就是模型认为这串动作序列将会导致的结果。你可以看到它有点晃,因为这是个很小的模型,但我们当然可以训练出这类玩具环境的模型,乃至更复杂的环境的模型。

[36:09] **SPEAKER_00:** So what are the challenges associated with training this kind of model? Well, one is you're trying to learn the representation of the world. So how you're going to compactly represent those highly dimensional images or LIDAR inputs or highly dimensional sensor inputs as the same time as you're trying to learn how actions change that representation. Okay. So you're co-learning representation and dynamics, and there are many solutions in the optimization landscape that will essentially just cause you to do nothing.

> 那么训练这类模型有哪些挑战呢?其一,你要学习世界的表示(representation)。也就是你要如何紧凑地表示那些高维图像、或激光雷达输入、或高维传感器输入,同时你还要学习动作如何改变那个表示。好的。所以你是在同时(co-learning)学习表示和动力学,而优化地形里存在许多“解”,本质上会让你什么都不做(即退化解)。

[36:34] **SPEAKER_00:** So, for example, a local minimum in the optimization landscape is to say, well, every state is just the same. It's a trivial collapse, basically, and there are many techniques in the literature to say, how can you avoid these? So there are solutions of a variety of different kinds that basically say they're a way to avoid the collapse associated with training world models. And that's really where the world model comes in. It says, well, instead of.

> 比如说,优化地形里的一个局部极小值就是“每个状态其实都一样”。这基本上就是一种平凡的坍缩(trivial collapse)。文献里有很多技术在讨论:你如何避免这些?所以有各种各样的解决方案,基本上都在讲如何避免训练世界模型时伴随的坍缩。而这正是这个(LeJEPA)世界模型的切入点。它说,与其……

[36:55] **SPEAKER_00:** Instead of having to use some manner of trick or like special method or a bunch of like hyper parameter tuning schedule, we're instead going to really drastically simplify this and go for a more elegant method. So if you know a little bit about world models, there's some popular ones in the top right here. This is a figure straight out of the paper. So PLDM is planning in with latent dynamic models, dyno, dyno, distillation with no labels, world model, dreamer out of deep mind, and then temporal difference MPC as the final one. So in some way, shape or form, I'll explain this.

> 与其不得不使用某种技巧、或特殊方法、或一大堆超参数调优的日程安排,我们打算把这一切大幅简化,采用一种更优雅的方法。如果你对世界模型稍有了解,右上角这里有一些流行的方法。这是直接从论文里截出来的一张图:PLDM 是“基于潜在动力学模型的规划”(Planning with Latent Dynamics Models),DINO(distillation with no labels,无标签蒸馏)世界模型,DeepMind 出的 Dreamer,以及最后一个时序差分 MPC(temporal difference MPC)。所以以某种形式,我来解释一下。

[37:22] **SPEAKER_00:** They use some kind of trick or. Like challenging to configure design to get away with this collapse to avoid collapse and the world models coming in and saying, basically, we can do this with sort of one hyper parameter and one loss term, which I'll talk about. There's really no time to go through all the different tricks that different world model approaches use because it really is the wild west out there right now. So many different methods, but they basically fall into one of these three categories. So one is you could do some explicit heuristic that stops collapse by like enforcing some special healthiness in like the latent space of your embedding.

> 它们都用了某种技巧,或者说某种难以配置的设计来避开坍缩、避免坍缩。而这个世界模型的做法是说,基本上我们只用大概一个超参数和一个损失项就能做到这件事,这个我等下会讲。真的没有时间把不同世界模型方法用到的各种技巧都过一遍,因为现在这个领域简直就是蛮荒西部,方法五花八门,但它们基本上可以归入这三类之一。第一类是你可以用某种显式的启发式规则来阻止坍缩,比如强制让你嵌入的潜在空间(latent space)具备某种特殊的“健康性”。

[37:55] **SPEAKER_00:** And the language trick is maybe a bit unfair here, but it's what's used in the paper. You could use some foundational methods, so you could take some like existing auto encoder or diffusion model or video model and use that as a basis for your world model and add an action conditioning element in there. Or you could use some privileged data that may not be usually available to the model outside of train time to be able to avoid collapse and lay well model, even though it says that it's doing something very different. I really think it's just offering a new kind of trick, which I'll talk about here. So.

> 用“技巧”(trick)这个词在这里也许有点不公平,但这就是论文里用的说法。第二类,你可以用一些基础模型的方法:比如拿某个现成的自编码器、或扩散模型、或视频模型,把它作为你世界模型的基底,再往里加一个动作条件(action conditioning)的元素。第三类,你可以使用某些特权数据(privileged data),这些数据在训练时之外通常对模型不可用,借此来避免坍缩。而 LeJEPA 世界模型,尽管它宣称自己在做非常不同的事情,我其实认为它只是提供了一种新的技巧,我下面就来讲。那么。

[38:24] **SPEAKER_00:** Jepper is joint embedding predictive architecture. It's sort of Yann LeCun's main work and lay world model is a kind of Jepper model. Basically, the way it works is you're going to take an auto encoder or I should say an image encoder, encode this observation. In this case, it's of a robot doing a push cube task that's going to turn that image into a latent vector in the latent space of this encoder. You're going to train an action condition forecasting module, this predictor, to be able to predict what is the next latent embedding going to look like when I execute this action.

> JEPA 是“联合嵌入预测架构”(Joint Embedding Predictive Architecture)。它算是 Yann LeCun 的主要工作,而 LeJEPA 世界模型是一种 JEPA 模型。基本上它的工作方式是:你拿一个自编码器——我应该说图像编码器——来编码这个观测。在这个例子里,观测是一个机器人在做推方块(push cube)的任务,编码器会把那张图像变成其潜在空间里的一个潜在向量。你要训练一个以动作为条件的预测模块,也就是这个 predictor,让它能够预测:当我执行这个动作时,下一个潜在嵌入会长什么样。

[38:52] **SPEAKER_00:** So not what the next image is going to look like. But what's next? Latent going to look like. And you can use the decoder attached that encoder to decode that back out into a useful image. But for the most part, all the interesting work is going to be done in the latent space.

> 所以不是下一张图像会长什么样,而是下一个潜在向量会长什么样。你可以用附在那个编码器上的解码器,把它解码回一张有用的图像。但绝大部分有意思的工作,都是在潜在空间里完成的。

[39:04] **SPEAKER_00:** And basically what they say is over a batch, all of those latent embeddings should be in a healthy distribution, which they describe as a Gaussian distributed distribution in the latent space. And thus enters the SIGREG regularizer, which is the sort of new term they add. So SIGREG for sketching, as in doing one dimensional passes over a high dimensional data. I for isotropic, so this should look the same when you slice it in any direction. And G for Gaussian distributed SIGREG.

> 基本上他们说的是,在一个批次(batch)里,所有那些潜在嵌入都应当处于一个“健康”的分布中,他们把它描述为潜在空间里一个高斯分布。于是就引入了 SIGReg 正则项(regularizer),这就是他们新加的那个项。SIGReg 里的 S 代表 sketching(草绘),即对高维数据做一维的“切片”遍历;I 代表 isotropic(各向同性),也就是无论你沿哪个方向切,它看起来都应该一样;G 代表 Gaussian distributed(高斯分布)——合起来就是 SIGReg。

[39:30] **SPEAKER_00:** So basically you're taking all of these embeddings of your different predictions, doing a one dimensional slice over each direction, like in that high dimensional space. And then you want each of the curves across those slices to be Gaussian distributed. And if that's true, then your distribution in the latent space must be very healthy. So the idea is you can quite cheaply evaluate how Gaussian distributed your embeddings are and thus how healthy your world model is. And how non-collapsing it is.

> 所以基本上你把不同预测的所有这些嵌入拿来,在那个高维空间里沿每个方向做一维切片,然后你希望这些切片上得到的每条曲线都是高斯分布的。如果这成立,那么你在潜在空间里的分布就一定非常健康。所以思路是:你可以相当廉价地评估你的嵌入有多接近高斯分布,从而评估你的世界模型有多健康、有多不坍缩。

[39:56] **SPEAKER_00:** So essentially I just say instead of training up on the normal, predict the next latent, you add on this additional SIGREG term. So I'd argue that basically this paper is just providing a very elegant kind of regularization. And to finish off, I'll just talk about three capabilities that you get from this. So one is the open loop prediction quality. This is what world models do.

> 所以本质上,我就是说,除了照常训练“预测下一个潜在向量”之外,你再加上这个额外的 SIGReg 项。所以我会主张,这篇论文基本上就是提供了一种非常优雅的正则化。作为收尾,我来讲一讲你能从中获得的三种能力。第一是开环(open loop)预测质量。这正是世界模型所做的事。

[40:14] **SPEAKER_00:** So you feed in like the context, this push T at the top. And you can see the top row is the real example. The bottom is the imagined. And they look about the same. This is good.

> 你输入上下文,顶部这个 push T。你可以看到上面一行是真实的例子,下面一行是想象出来的。它们看起来差不多一样。这很好。

[40:22] **SPEAKER_00:** It means your world model is really good at predicting what your next action is going to be. They do that on push T and then on a slightly, like a 3D analog task, like a push cube. This is all great. I love seeing these plots. But really what matters is how does this actually affect the policy, like for the actual task completion?

> 这意味着你的世界模型很擅长预测你下一步动作会带来什么。他们在 push T 上做了这个,然后在一个稍微 3D 化的类比任务上,比如推方块(push cube)。这些都很棒。我很喜欢看这些图。但真正重要的是:这实际上如何影响策略,也就是对真正的任务完成有何影响?

[40:37] **SPEAKER_00:** How is this useful? And that sort of brings us into how you can use these models for model predictive control. Basically you take your initial observation and a goal observation. I put an asterisk there because how often do you have a goal observation in a robotics task? Like you don't always know exactly the situation that you want to end up in.

> 这有什么用?这就把我们引向了如何把这些模型用于模型预测控制。基本上你拿你的初始观测和一个目标观测。我在那里打了个星号,因为在机器人任务里你有多少时候会有一个“目标观测”呢?你并不总是确切知道你想最终落到什么样的情景里。

[40:54] **SPEAKER_00:** In this case, that's how they frame it. So say the world looks like this right now. I want the world to look like this. You encode both of those. And then you're basically doing a search over the actions that will get you in the latent space from this starting point to this ending point.

> 在这个例子里,他们就是这么设定的。比如说现在世界是这个样子,我想让世界变成那个样子。你把这两者都编码。然后你基本上是在动作上做搜索,寻找能在潜在空间里把你从这个起点带到这个终点的那些动作。

[41:07] **SPEAKER_00:** And there are well-defined optimization methods to achieve that. It works pretty well. I'll make it simple. The world model is better than the competition on these like small 2D tasks. As soon as you go to 3D, dino world model wins.

> 而且有定义良好的优化方法可以实现这一点。它效果相当不错。我说简单点:在这些小型 2D 任务上,这个(LeJEPA)世界模型优于其竞争对手。但一旦你进入 3D,DINO 世界模型就胜出了。

[41:19] **SPEAKER_00:** It does have a big foundational backbone trained on that kind of image data. So you'd expect it to win. They run on a really simple environment called to room and kind of say, you know, we don't do so well on this, but that's because we're promoting like really high dimensional healthy embeddings. And it's a very low dimensional problem. I'm not sure if I truly go for that.

> 它(DINO)确实有一个在那类图像数据上训练的大基础骨干(backbone),所以你会预期它会赢。他们在一个非常简单的、叫“two room”(双房间)的环境上跑,并且大致说,我们在这个上面表现不太好,但那是因为我们在促进非常高维的健康嵌入,而这是个非常低维的问题。我不太确定我是否真的买账这个说法。

[41:38] **SPEAKER_00:** But a good takeaway is that it's about 50 times faster than any of the competition across the board because it's doing all this work in the latent space. And it doesn't have to have any like additional tricks relating to more forward passes or like having two copies of the model in memory. And you can actually boot this thing up. It's like a single card, less than 24 gigabytes of VRAM. And it's only 50 million parameters.

> 但一个不错的收获是:它比所有竞争对手全面地快大约 50 倍,因为它把所有这些工作都放在潜在空间里做。它不需要任何与更多前向传播、或在显存里放两份模型副本相关的额外技巧。而且你真的可以把这东西启动起来:一块单卡,不到 24GB 显存,而且只有 5000 万参数。

[41:56] **SPEAKER_00:** So that is pretty nice. Final piece. This is what I think is a really cool capability of world models. You can quantify the model error. So basically they just come up with some trajectories that kind of screw with the world model.

> 所以这挺不错。最后一部分。这是我认为世界模型一个非常酷的能力:你可以量化模型误差。基本上他们就是设计了一些会“捣乱”世界模型的轨迹。

[42:07] **SPEAKER_00:** So the top one is going from left to right. That's time. So that's just like a nominal example. Everything's normal. Then they take the same example, but they change the color of the T and then they take the same example, but they just teleport the T into a different location.

> 最上面那一条是从左到右,那是时间轴。所以那只是一个正常的例子,一切都正常。然后他们用同一个例子,但把 T 的颜色改了;再用同一个例子,但把 T 直接“瞬移”到另一个位置。

[42:19] **SPEAKER_00:** And this is really cool because you can actually see the moment. When you apply those perturbations, you get a spike in the model error. And this is detectable, which is to say world model enabled agents can quantify how poor their predictions are. They have good estimates of their uncertainty. This is really powerful.

> 这非常酷,因为你真的能看到那个瞬间:当你施加这些扰动时,模型误差会出现一个尖峰。而且这是可检测的,也就是说,配备了世界模型的智能体可以量化它们的预测有多差。它们对自身不确定性有很好的估计。这真的非常强大。

[42:33] **SPEAKER_00:** Model-free based approaches don't natively give you this stuff. This is my last slide. A few discussion points and broader themes maybe we can chat about here. Obviously, you know, are we going to go with model-based? Are we going to go with model-free?

> 免模型的方法本身并不会天然地给你这些东西。这是我的最后一张幻灯片。这里有几个讨论点和更宏观的主题,也许我们可以聊聊。显然,你知道,我们到底会走基于模型的路线,还是免模型的路线?

[42:45] **SPEAKER_00:** What's going to be the best way to enable intelligent agents to do interesting things in the world? Regularization and representation learning. In this paper, they are co-learning the representation of the world that the agent has and the dynamics of the world. Should this be separated? Can we take some bio-inspiration?

> 让智能体在世界中做有趣的事情,最好的方式会是什么?正则化与表示学习。在这篇论文里,他们是在同时学习智能体所拥有的世界表示和世界的动力学。这两者应该分开吗?我们能不能从生物学里获得一些启发?

[43:00] **SPEAKER_00:** Should we use pre-existing like foundation models and stuff like that? And then finally, how can we fight representational collapse elegantly? I think this work does a really great job of that, but the question is still out on what the best way to do it is. So that's my talk. Thanks very much for your attention.

> 我们是否应该使用现成的基础模型之类的东西?然后最后,我们如何优雅地对抗表示坍缩(representational collapse)?我觉得这项工作在这方面做得非常出色,但关于什么才是最好的做法,仍然没有定论。那这就是我的演讲。非常感谢大家的聆听。

[43:21] **SPEAKER_03:** All right. Okay. So for the next two, we're kind of focusing on less world model stuff and more heady high-level stuff that I think is pretty interesting. This is a paper that's going to be presented by Akshay, one of the YC startups here named QLabs. And you're a co-founder, president?

> 好的。好。那么接下来这两个,我们的重点会从世界模型的内容转向更烧脑、更高层的东西,我觉得挺有意思的。这是一篇将由 Akshay 来讲的论文,他来自这里的一家 YC 初创公司,叫 QLabs。你是联合创始人、总裁?

[43:46] **SPEAKER_03:** You're president of QLabs? Is that right? Okay. Welcome, Akshay.

> 你是 QLabs 的总裁?是这样吗?好的。欢迎你,Akshay。

[43:54] **SPEAKER_02:** Hey, everybody. Today, I'm going to be talking through Andrew Gordon Wilson's paper, Deep Learning. Deep learning is not so mysterious or different. We actually work with Andrew on the generalization problem at QLabs, so I'm really excited for more people to know about his work. The current state of machine learning is that we know that scaling models leads to better generalization,

> 大家好。今天我要讲的是 Andrew Gordon Wilson 的论文,《深度学习并没有那么神秘或不同》(Deep Learning is Not So Mysterious or Different)。我们在 QLabs 实际上和 Andrew 一起研究泛化(generalization)问题,所以我非常高兴能让更多人了解他的工作。机器学习目前的现状是:我们知道扩大模型规模会带来更好的泛化,

[44:13] **SPEAKER_02:** but we don't have a mechanistic understanding of why that is the case. Yeah, if we can understand generalization, then we might be able to optimize for it as well. So the payoff to understanding it is actually really, really large. When you talk to people in the field, they often explain that generalization is a mystery, and they point to examples like overparameterization, benign overfitting, and double descent as reasons why we might not be able to understand generalization at all. So Andrew's work here basically dispels those mysteries by using classical theories of generalization,

> 但我们对为什么会这样并没有一种机制层面的理解。是的,如果我们能理解泛化,那么我们或许也能针对它来优化。所以理解它的回报其实非常非常大。当你和这个领域的人交谈时,他们常常会解释说泛化是个谜,他们会举出诸如过参数化(overparameterization)、良性过拟合(benign overfitting)和双下降(double descent)这些例子,作为我们可能根本无法理解泛化的理由。而 Andrew 在这里的工作,基本上是用经典的泛化理论来破除这些谜团,

[44:49] **SPEAKER_02:** which have to date not really been used to explain things like overparameterization thus far. So the first classical theory is generalization. The second classical theory that we'll go through is PAC-BASE. So PAC-BASE basically bounds the test loss, which is the generalization. This is the quantity that we care about with the training loss and a compression term.

> 而这些经典理论迄今为止其实还没有被真正用来解释像过参数化这样的现象。第一个经典理论是关于泛化的。我们要过一遍的第二个经典理论是 PAC-Bayes。PAC-Bayes 基本上给测试损失(也就是泛化,这正是我们关心的量)设了一个上界,这个上界由训练损失和一个压缩项(compression term)构成。

[45:09] **SPEAKER_02:** The thing is, in the past, when people overparameterized models, this compression term tends to dominate. And so in practice, these bounds become loose and vacuous, meaning that we can't use them for anything at all. This was basically due to a misapplication of the bound. You can compute the compression term in an alternative way, which we'll get into sort of later in the talk here. So let's go through the first mystery that Andrew goes through in his paper.

> 问题在于,过去当人们把模型过参数化时,这个压缩项往往会占主导。于是在实践中,这些界变得松弛而空洞(loose and vacuous),意味着我们根本无法拿它们来做任何事。这基本上是由于对这个界的错误应用所致。你可以用一种替代的方式来计算这个压缩项,我们会在这次演讲稍后讲到。那么我们先来过一遍 Andrew 在他论文里讨论的第一个谜团。

[45:35] **SPEAKER_02:** The mystery that he talks about is overparameterization. And this is basically the idea that as you scale up the model parameter size from the bias variance tradeoff, you would expect that you might overfit. But in practice, we see the opposite. The scaling laws tell us that we actually get better generalization. This scaling and the better generalization,

> 他谈到的这个谜团是过参数化。基本上它是这样一个想法:从偏差—方差权衡(bias-variance tradeoff)出发,当你扩大模型的参数规模时,你会预期你可能会过拟合。但在实践中,我们看到的恰恰相反。缩放定律(scaling laws)告诉我们,我们实际上得到了更好的泛化。这种扩展以及更好的泛化,

[45:57] **SPEAKER_02:** overparameterization is due to the massive gains in model capability over the last couple of years. But we still don't really understand why it improves generalization. So the PAC-based framework gives us a pretty useful way to think about the success of overparameterization. The first is with empirical risk. Empirical risk is basically training loss.

> 过参数化,正是过去这几年模型能力大幅提升的原因。但我们仍然并不真正理解它为什么能改善泛化。所以 PAC-Bayes 框架给了我们一种相当有用的方式来思考过参数化的成功。第一点是关于经验风险(empirical risk)。经验风险基本上就是训练损失。

[46:19] **SPEAKER_02:** When you increase the number of parameters, you can fit your data better. So the empirical risk, the first term, goes down. And Andrew's work also finds that when we increase the number of parameters, we also find more compressible solutions. So this is work by LotFi et al. And they develop methods to basically compress the training set and the model.

> 当你增加参数数量时,你能更好地拟合你的数据。所以经验风险,也就是第一项,会下降。而 Andrew 的工作还发现,当我们增加参数数量时,我们也会找到更可压缩(compressible)的解。这是 Lotfi 等人的工作,他们开发了一些方法,基本上是用来压缩训练集和模型。

[46:46] **SPEAKER_02:** And they basically find a negative correlation between the bits required to encode the training set and the number of parameters. And so we find that as we increase the number of parameters, as we increase the model size, we can find more efficient encodings of the training set. So the second term in this bound also gets lower. Another perspective on this model compressibility point is a perspective of flatness. As you increase the number of parameters,

> 他们基本上发现,编码训练集所需的比特数与参数数量之间存在负相关。于是我们发现,随着我们增加参数数量、随着我们增大模型规模,我们能找到训练集的更高效编码。所以这个界里的第二项也会变得更低。关于模型可压缩性这一点,还有另一个视角,就是平坦性(flatness)的视角。当你增加参数数量时,

[47:13] **SPEAKER_02:** it turns out that the volume of flat minima in parameter space exponentially increases. This is the green region. And comparatively, the volume of sharp minima increases much less. And this is interesting. It's useful, the compressibility view,

> 结果发现,参数空间中平坦极小值(flat minima)的体积会呈指数级增长。这就是绿色区域。相比之下,尖锐极小值(sharp minima)的体积增长要少得多。这很有意思。而可压缩性这个视角之所以有用,

[47:30] **SPEAKER_02:** because flat minima are known to be more compressible than sharp minima. And so overparameterization fits within existing theories. And through Andrew's work, we actually see useful bounds on generalization, even for models at like a billion parameter scale. And so we go to the next so-called mystery of deep learning, which is called benign overfitting, which Andrew also dispels in or at least partially explains in his paper. So the idea of benign overfitting is that deep neural networks

> 是因为众所周知,平坦极小值比尖锐极小值更可压缩。所以过参数化其实契合现有的理论。通过 Andrew 的工作,我们真的看到了对泛化有用的界,甚至对十亿参数量级的模型也是如此。于是我们来到深度学习下一个所谓的谜团,叫做良性过拟合(benign overfitting),Andrew 在他的论文里也破除了它,或者至少部分地解释了它。良性过拟合的想法是,深度神经网络

[47:58] **SPEAKER_02:** are able to fit totally random noise, but at the same time, they are able to generalize well when you have structured data. The mystery is how can you have an inductive bias that allows you to generalize well if you can also fit totally random data? I think a regularized polynomial model in Andrew's paper gives us pretty good intuition for how this might be the case. Here you can see that on random data, so section C of the figure, that we have enough parameters to fit the data, and so we can fit the totally random data. But on structured data,

> 能够拟合完全随机的噪声,但与此同时,当你有结构化数据时,它们又能很好地泛化。谜团在于:如果你也能拟合完全随机的数据,那你怎么可能同时拥有一种让你泛化良好的归纳偏置(inductive bias)呢?我认为 Andrew 论文里一个带正则化的多项式模型给了我们相当好的直觉,来理解这为何可能成立。这里你可以看到,在随机数据上,也就是图中的 C 部分,我们有足够的参数来拟合数据,所以我们能拟合完全随机的数据。但在结构化数据上,

[48:30] **SPEAKER_02:** the regularization pushes us to use the lower order terms. And so we are able to both get the flexibility, but also have inductive bias that allows us to generalize. And generally, this is the view to take for neural networks. They are expressive models with a soft inductive bias. We can go through this concept just using this figure right here.

> 正则化推动我们去使用低阶项。于是我们既能获得灵活性,又拥有让我们泛化的归纳偏置。总体上,这就是我们应该对神经网络采取的看法:它们是带有柔性归纳偏置(soft inductive bias)的、表达力很强的模型。我们可以就用这里这张图来过一遍这个概念。

[48:53] **SPEAKER_02:** So on the left-hand side, we have an example of what's like a flexible hypothesis space. And a flexible hypothesis space would allow you to fit the data that you have, but the problem is that you would almost certainly overfit if you do not have a bias towards one solution over the other. But on the other hand, if you have an inductive bias, you would solve this overfitting problem, but instead you wouldn't be able to model all of the details of reality. And so the middle ground is to have a very expressive hypothesis space, but also have a bias towards solutions that might generalize. For example, in the PAC-BASE framework,

> 在左边,我们有一个“灵活假设空间”(flexible hypothesis space)的例子。灵活的假设空间能让你拟合你手上的数据,但问题是,如果你没有偏向某个解而非另一个解的偏置,你几乎肯定会过拟合。但另一方面,如果你有一个归纳偏置,你就能解决这个过拟合问题,可代价是你无法建模现实的所有细节。所以中间地带就是:拥有一个非常有表达力的假设空间,但同时带有偏向那些可能泛化的解的偏置。比如,在 PAC-Bayes 框架里,

[49:29] **SPEAKER_02:** we might want to bias towards more compressible models if we can. And so we see that deep learning so-called mysteries are actually consistent and partially explained by existing theories, such as soft inductive biases and PAC-BASE. And sort of the thing I want to leave you with is that if we can find the right inductive biases building on these theories, we might be able to optimize for them as well. And by the no free lunch theorem, the only way that we get improvements in learning efficiency is through inductive biases. So I think that working on this problem is a really good bet to make.

> 如果可以的话,我们或许会想偏向更可压缩的模型。于是我们看到,深度学习所谓的这些谜团,其实与现有理论(比如柔性归纳偏置和 PAC-Bayes)是一致的,并被它们部分地解释了。我想留给大家的一点是:如果我们能在这些理论的基础上找到正确的归纳偏置,那我们或许也能针对它们来优化。而根据“没有免费午餐”定理(no free lunch theorem),我们获得学习效率提升的唯一途径就是通过归纳偏置。所以我认为,研究这个问题是一个非常好的赌注。

[50:04] **SPEAKER_02:** Given the massive sample efficiency gap between AI and humans, we might actually see massive gains in capability if we work on this problem. And so, yeah, that's where I want to leave you with. Short presentation.

> 考虑到 AI 和人类之间在样本效率(sample efficiency)上的巨大差距,如果我们研究这个问题,我们或许真的会看到能力上的巨大提升。所以,是的,这就是我想留给大家的。一个简短的演讲。

[50:19] **SPEAKER_03:** Okay. So for this last paper, then after this we have some boba for everyone. So sit tight, 15 minutes. This is an idea that, you know, I've been obsessed with back to the sample efficiency thing. I think that like the two major problems we have left really to solve in AI

> 好的。那么这是最后一篇论文了,讲完之后我们给大家准备了珍珠奶茶(boba)。所以再坐稳 15 分钟。这是一个……你知道,我一直着迷的想法,又回到了样本效率这件事上。我觉得,我们在 AI 里真正剩下要解决的两大问题,

[50:36] **SPEAKER_03:** is intelligence per watt and intelligence per sample. And if you compare that to where we're at today compared to humans, I would say that we're still an order or two magnitude off on intelligence per watt. And we're like orders of magnitude off on intelligence per sample. I don't know what percent of the internet that you guys have read, but I have not read the entire internet. In Chris Ray's lab in particular,

> 就是“每瓦智能”(intelligence per watt)和“每样本智能”(intelligence per sample)。如果你把它和我们今天相对于人类的水平对比,我会说我们在每瓦智能上还差一到两个数量级,而在每样本智能上,我们差了好几个数量级。我不知道你们读过互联网的百分之多少,但我可没读过整个互联网。特别是在 Chris Ré 的实验室里,

[50:59] **SPEAKER_03:** we've been obsessed with this idea. That if I have a fixed size amount of data and I have infinite compute, just go nuts. How much generalization can I actually achieve? And so this is exactly the paper that starts to answer that question. And I'm really excited to introduce Kan Wu.

> 我们一直着迷于这样一个想法:如果我有固定大小的数据量,而我有无限的算力,可以尽情挥霍,那我到底能实现多少泛化?而这恰恰就是一篇开始回答这个问题的论文。我非常高兴地介绍 Kan Wu。

[51:19] **SPEAKER_05:** Hi, I'm Kan Wu. This is a paper that I co-led with my amazing collaborator, Suhas, as well as Percy and Patsy. So part of the motivation for this paper, is just the fact that over the past six or seven years, pre-training has continued to improve model capabilities in pretty surprising ways. So in 2020 with GPT-3, we had sort of the emergence of in-context learning. In 2022 with Anthropix RLHF,

> 大家好,我是 Kan Wu。这篇论文是我与我出色的合作者 Suhas,以及 Percy 和 Patsy 共同主导的。这篇论文的部分动机,就在于这样一个事实:在过去六七年里,预训练一直以相当令人惊讶的方式持续提升模型能力。2020 年随着 GPT-3,我们看到了上下文学习(in-context learning)的涌现。2022 年随着 Anthropic 的 RLHF,

[51:54] **SPEAKER_05:** we had sort of the advent of alignment. And maybe most notably in 2024 with both O1 from OpenAI and then later DeepSeq R1, we had the emergence of reasoning. And in fact, even still today, we see that with these newer and bigger pre-training runs, like Mythos and 5.5, the models just continue to keep better. And so because pre-training is very expensive, a lot of the focus on the research side of things has been on how do we improve compute efficiency? And in general, people have found that to improve compute efficiency,

> 我们迎来了对齐(alignment)的到来。也许最引人注目的是在 2024 年,随着 OpenAI 的 o1,以及后来的 DeepSeek R1,我们看到了推理(reasoning)的涌现。而事实上,即便到今天,我们看到这些更新、更大的预训练,比如 Mythos 和 GPT-5.5(4.5),模型仍在持续变好。正因为预训练非常昂贵,研究方面很多关注点都集中在:我们如何提升算力效率(compute efficiency)?总体上,人们发现要提升算力效率,

[52:27] **SPEAKER_05:** you need to scale both the number of parameters in your model and the number of data points that you train your model on. And so these were quantified with the so-called, Chinchilla scaling laws. The problem with compute efficiency is that we're soon going to be constrained by data. And so if you look at these sort of public projections of the rate of growth of internet data, they suggest that the amount of sort of human-generated text on the internet grows by roughly 3% per year. And the amount of compute that we're spending on pre-training

> 你需要同时扩大模型中的参数数量和你用来训练模型的数据点数量。这些被所谓的 Chinchilla 缩放定律量化了。算力效率的问题在于,我们很快就会受到数据的制约。如果你看那些关于互联网数据增长率的公开预测,它们表明互联网上人类生成的文本量大约每年增长 3%。而我们花在预训练上的算力,

[52:55] **SPEAKER_05:** is growing by roughly 4 or 5x per year. And so what this suggests is that as time passes on, the amount of compute that we're willing to spend per data point is going to continue to increase by roughly 4x year over year. And so this sort of motivates the core question in this paper, which is how should you approach pre-training when you're constrained by data, but totally unconstrained by compute? And it's worth maybe spending a few seconds to think for yourself if you haven't already seen this paper, like what would you do in this situation? This is a very different algorithmic regime

> 大约每年增长 4 到 5 倍。所以这意味着,随着时间推移,我们愿意为每个数据点花费的算力将继续大约以每年 4 倍的速度增长。这就引出了这篇论文的核心问题:当你受数据约束、但完全不受算力约束时,你应该如何进行预训练?如果你还没看过这篇论文,也许值得花几秒钟自己想一想:在这种情况下你会怎么做?这是一个与

[53:31] **SPEAKER_05:** from sort of the compute-efficient pre-training world that we've sort of lived in for sort of most of modern time. And it's also worth noting that this question is not that different from how machine learning worked before the modern ALAMER. So for things like classical statistics, where maybe you really care about your rates with respect to the number of points of data you have and you don't care about compute, or even older benchmarks like MNIST and Penn Treebank, where you're sort of implicitly data-constrained because the benchmarks don't have that many data points. And so sort of the core contribution that I'll explain in this paper is that we bring the modern toolkit of scaling laws to sort of answer this problem. And so what we'll show is that we'll propose

> 与我们在现代大部分时间里所处的“算力高效预训练”世界非常不同的算法体制。同样值得注意的是,这个问题与现代大语言模型出现之前机器学习的运作方式并没有那么不同。比如经典统计学,你可能真的很在意你的收敛率相对于你所拥有数据点数量的关系,而并不在意算力;甚至像 MNIST 和 Penn Treebank 这类更老的基准,你其实是隐含地受数据约束的,因为这些基准的数据点并没有那么多。所以我在这篇论文里要解释的核心贡献是:我们把现代的缩放定律工具箱拿来回答这个问题。我们将展示的是,我们会提出

[54:14] **SPEAKER_05:** a few different scaling recipes. And we'll sort of chase scaling recipes that monotonically decrease your IID validation loss, so sort of in distribution generalization. And we'll show that these scaling laws have a really clean functional form and they follow a super clean power law. And when you're able to fit these power laws, what you can do is you can estimate the best possible loss of your recipe by looking at the asymptote of the power law. And this is in some sense a quantification

> 几种不同的缩放配方(scaling recipes)。我们会去追求那些能单调地降低你 IID 验证损失(即分布内泛化)的缩放配方。我们会展示这些缩放定律有非常干净的函数形式,遵循一个极其干净的幂律(power law)。当你能够拟合这些幂律时,你能做的是:通过看幂律的渐近线(asymptote),来估计你这个配方所能达到的最佳可能损失。而这在某种意义上就是对

[54:41] **SPEAKER_05:** of your best possible performance under infinite compute. And our goal in this paper is sort of to think more carefully about what types of algorithms allow you to lower your compute asymptote. And we're sort of going to chase these types of infinite compute ones. And so to start, I'm going to introduce this canonical setting that we referenced in this paper, which is that we're going to simulate a data-constrained world by just constraining the number of points and the number of pre-training tokens we have to be a very small amount. So we're going to assume access to only 200 million tokens

> 你在无限算力下所能达到的最佳性能的一种量化。而我们在这篇论文里的目标,某种程度上是更仔细地思考:什么类型的算法能让你降低这个算力渐近线。我们会去追求这类“无限算力下”的算法。那么一开始,我先介绍这篇论文里引用的这个标准设定(canonical setting):我们通过把数据点数量和预训练 token 数量都限制到一个非常小的量,来模拟一个数据受约束的世界。所以我们假设只能访问 2 亿个 token,

[55:11] **SPEAKER_05:** from DCLM, which is general web data. And what we're going to do is we're going to pre-train larger and larger models, which is the x-axis, using different kinds of pre-training recipes. And the y-axis here is going to be, again, our IID validation loss on DCLM. And our goal is going to be to find recipes that allow us to spend more compute and train larger models while monotonically decreasing our loss. So to start, we can consider sort of the obvious approach

> 这些 token 来自 DCLM,即通用网页数据。我们要做的是,用不同种类的预训练配方去预训练越来越大的模型(这是 x 轴)。这里的 y 轴同样是我们在 DCLM 上的 IID 验证损失。我们的目标是找到一些配方,让我们能花更多算力、训练更大的模型,同时单调地降低我们的损失。那么一开始,我们可以考虑一个相当显而易见的做法,

[55:36] **SPEAKER_05:** that you might take when you're in this setting, which is first to epoch your data, so to train on the same data points over and over again until you start overfitting, as well as scaling up your model, so making your model larger and larger. And what we can do is we can do both of these at the same time, and we can do sort of an exhausted grid search over these parameters until we start overfitting and then we do early stopping. And this is sort of the red line, which is what we call the standard recipe. And what you'll see with the standard recipe is that even if you are willing to spend more compute, as you train more and more overparameterized models, you start to overfit more quickly and your loss starts to increase after a certain point. And so if you see this line,

> 这是你在这种设定下可能会采取的做法:首先对你的数据做多轮(epoch),也就是在同样的数据点上反复训练,直到你开始过拟合;同时扩大你的模型,让模型越来越大。我们可以同时做这两件事,并对这些参数做一个近乎穷尽的网格搜索,直到我们开始过拟合,然后我们做早停(early stopping)。这大致就是那条红线,我们称之为标准配方(standard recipe)。你会看到,采用标准配方时,即使你愿意花更多算力,随着你训练越来越过参数化的模型,你会更快地开始过拟合,超过某个点之后你的损失就开始上升。所以如果你看到这条线,

[56:17] **SPEAKER_05:** sort of the natural instinct you should have is how do we fix this? And one possible approach is to do really aggressive regularization. And so sort of the first baseline in this paper is going to be doing really aggressive regularization by cranking up your weight decay. And so what we do is we show that if you optimally tune your weight decay for each total parameter count, so we're going to optimally tune learning rate, weight decay, and epoch count for each one of these purple points, you can show that your loss follows a really clean power law as you increase the number of parameters in your model. And this is really aggressive regularization.

> 你自然会有的本能反应是:我们怎么修好它?一个可能的做法是做非常激进的正则化。所以这篇论文里第一个基线,就是通过大幅调高你的权重衰减(weight decay)来做非常激进的正则化。我们所做的是:我们展示,如果你为每个总参数量都最优地调节权重衰减——也就是我们会为这些紫色点中的每一个都最优地调节学习率、权重衰减和轮数(epoch count)——你就能证明,随着你增加模型的参数数量,你的损失遵循一个非常干净的幂律。而这是非常激进的正则化。

[56:52] **SPEAKER_05:** So for context, we use weight decays that are something like 30 times larger than the weight decays that people do for compute optimal pre-training. And so on the legend here, you can see sort of the form of this power law. And it has a few nice properties. One is that the exponent on the model parameters, n, is 1, and this is actually predicted by sort of the data constraint theory. The second nice property that it has

> 给个参照:我们用的权重衰减大约是人们做算力最优预训练时所用权重衰减的 30 倍。在这里的图例上,你可以看到这个幂律的形式。它有几个不错的性质。其一是模型参数 n 上的指数是 1,而这实际上是数据约束理论所预测的。它的第二个不错的性质是

[57:17] **SPEAKER_05:** is that the scaling law has an asymptote, which is 3.43 in this case. And this characterizes the performance of the best possible regularized model in this setting if you had, like, infinite compute. So you'll notice that the baseline approaches, because they overfit more quickly, they don't even have a measurable asymptote. And so once we start going down the rabbit hole of regularization and these other types of classical machine learning techniques, there's a whole basket of techniques to get into. And so perhaps maybe the most famous one

> 这个缩放定律有一条渐近线,在这个例子里是 3.43。它刻画了在这个设定下,如果你有无限算力,最佳可能的正则化模型能达到的性能。所以你会注意到,那些基线方法因为过拟合得更快,它们甚至没有一个可测的渐近线。一旦我们开始钻进正则化以及其他这类经典机器学习技术的“兔子洞”,就有一整篮子技术可以深入。也许其中最有名的一个

[57:46] **SPEAKER_05:** is to do ensembling. And so what we show in this paper is that you can bring back ensembling in the modern world of pre-training language models, and they turn out to be incredibly data efficient. So what these light blue points correspond to is they correspond to 300 million parameter models that were ensembling with more and more members. So the fifth point will correspond to 1.5 billion total parameters, which is a five ensemble of 300 million parameter models. We show that you can also fit

> 就是做集成(ensembling)。我们在这篇论文里展示的是,你可以在现代预训练语言模型的世界里把集成重新拿回来,而结果证明它们的数据效率高得惊人。这些浅蓝色的点对应的是 3 亿参数的模型,用越来越多的成员做集成。所以第五个点对应的是总共 15 亿参数,也就是五个 3 亿参数模型的集成。我们展示你也可以拟合出

[58:17] **SPEAKER_05:** really clean scaling laws to ensembles. So you also get a power law that has exponent one in the number of ensemble members, and it also has an asymptote. But most importantly, the asymptote of ensembling is much lower than the asymptote of the regularized recipe. So it's giving you a true data efficiency win if you had an infinite amount of compute. There's also this interesting property,

> 针对集成的非常干净的缩放定律。所以你同样得到一个幂律,它在集成成员数量上的指数是 1,而且它也有一条渐近线。但最重要的是,集成的渐近线比正则化配方的渐近线要低得多。所以如果你有无限算力,它给你带来的是一个真正的数据效率上的胜利。这里还有一个有意思的性质,

[58:39] **SPEAKER_05:** which is that ensemblings, if you do a compute-matched comparison, so the same number of parameters, are actually better than the regularized recipe. So if your goal is just to train the best 1.5 billion parameter model, it's better to train an ensemble of a bunch of small models when you're data constrained than to train one really large model. The last thing we show in this plot is that you can actually compose the benefits of regularization and ensembling. So one way to think about this is that regularization gives you this ability to continue to make the models large and larger, while ensembling introduces this new axis for scaling compute, which is by training more and more models. And so what this gold line,

> 就是如果你做算力匹配(compute-matched)的比较,也就是相同的参数数量,集成实际上比正则化配方更好。所以如果你的目标只是训练出最好的 15 亿参数模型,那么当你受数据约束时,训练一堆小模型的集成,要比训练一个真正巨大的模型更好。这张图里我们展示的最后一点是,你实际上可以把正则化和集成的好处组合起来。理解这一点的一种方式是:正则化给了你把模型不断做大的能力,而集成引入了一个扩展算力的新维度,即通过训练越来越多的模型。所以这条金色的线,

[59:20] **SPEAKER_05:** which we call the joint scaling recipe, is we quantify this hypothetical performance if we were able to train an ensemble, an infinitely large ensemble of infinitely large models. And so the way in which we actually quantify this performance is we fit two scaling laws. So we'll take a double limit. What we'll first do is we'll train ensembles of 150 million parameter models, 300 million parameter models, and so on and so forth. And then we'll look at the asymptotes of the ensembles,

> 我们称之为联合缩放配方(joint scaling recipe)。我们量化的是这样一种假设性性能:如果我们能训练一个集成——一个由无限大模型组成的无限大集成——会怎样。我们实际量化这个性能的方式是拟合两个缩放定律,也就是取一个双重极限(double limit)。我们首先会训练由 1.5 亿参数模型、3 亿参数模型等等组成的集成,然后我们看这些集成的渐近线,

[59:49] **SPEAKER_05:** and then we'll take a second, we'll fit a second scaling law to the asymptotes of these ensembles. And this is essentially taking, the first limit is taking the limit over k, and the second limit is taking the limit over n. And what we find is that if you're willing to sort of go through the effort of training infinitely large models and infinitely many ensembles, you get a huge loss improvement. And so all of these experiments are sort of in this toy data constraint setup of 200 million tokens. And obviously this is very different

> 然后我们再取第二个极限——我们对这些集成的渐近线拟合第二个缩放定律。这本质上就是:第一个极限是对 k(集成成员数)取极限,第二个极限是对 n(参数数量)取极限。我们发现,如果你愿意付出这样的努力,去训练无限大的模型和无限多的集成,你会得到巨大的损失改善。所有这些实验都是在这个 2 亿 token 的玩具式数据约束设定里做的。显然这与

[60:17] **SPEAKER_05:** from sort of the standard regime of pre-training. So what we also do in this paper is we spend some effort on trying to confirm that our recipes scale. So the first way in which we do this is that we build data scaling laws. So what data scaling laws are is that we repeat the exact same set of experiments from the previous slide at four different pre-training token counts, up to 1.7 billion tokens. And so for each slice on the x-axis

> 标准的预训练体制非常不同。所以在这篇论文里我们还花了些功夫,试图确认我们的配方是可扩展的。我们做这件事的第一种方式是构建数据缩放定律(data scaling laws)。所谓数据缩放定律,就是我们在四个不同的预训练 token 数量下(最多到 17 亿 token)重复上一张幻灯片里完全相同的那组实验。所以对于 x 轴上的每一个切片,

[60:40] **SPEAKER_05:** at each seed token count, we're going to quantify the best possible performance of each recipe if we had an infinite amount of compute. So for the red points, they overfit more quickly, so these will be actual models. While for the purple and the gold points, these will correspond to sort of a single limit or a double limit. What these data scaling laws let us do is they let us quantify the data efficiency numbers of our approaches. So one way in which we do this

> 在每一个种子(seed)token 数量下,我们会量化每个配方在拥有无限算力时所能达到的最佳性能。对于红色的点,它们过拟合得更快,所以这些会是实际训练出来的模型;而对于紫色和金色的点,它们对应的是某种单重极限或双重极限。这些数据缩放定律让我们能做的,是量化我们各方法的数据效率数值。我们做这件事的一种方式是,

[61:05] **SPEAKER_05:** is if we have some new recipe that we believe should improve upon the standard recipe that we're using right now, you can take the loss of your new recipe and you can project it onto the data scaling law, so the red line of the standard recipe. And this projection lets you measure essentially the effective number of extra tokens that your algorithmic improvement is buying you. So in this case, what we see is that this joint scaling recipe gives you roughly a 5x data efficiency win over the standard recipe. It's also worth noting that these data efficiency wins are something that we can realize with sort of finite models, not just double limits. So for example, if you're willing to train

> 如果我们有某个新配方,我们相信它应该优于我们现在用的标准配方,你可以把你新配方的损失投影到数据缩放定律上,也就是标准配方的那条红线上。这个投影让你本质上能测量出:你的算法改进给你换来了多少“有效的额外 token 数量”。所以在这个例子里,我们看到这个联合缩放配方相比标准配方大约带来 5 倍的数据效率胜利。同样值得注意的是,这些数据效率的胜利是我们用有限的模型就能实现的,而不只是双重极限。比如,如果你愿意训练

[61:45] **SPEAKER_05:** a 5 ensemble of 1 billion parameter models, this will give you roughly a 3.7x data efficiency win. The other interesting aspect about these data scaling laws is if you look at the functional form in the legend, you'll see that they all have really similar exponents and they all have very similar asymptotes. And so the reason why this matters is because this suggests that even if you repeated these experiments at a much, much larger token scale, if you believe that these data scaling laws extrapolate, this data efficiency win is going to be constant over the actual number of token counts that you have. So this suggests that this double joint scaling law recipe has a 5x data efficiency win even if you are willing to send the seed token count to like 10 trillion tokens or whatever people are doing pre-training at these days. So now I'll go over some methods

> 一个由五个 10 亿参数模型组成的集成,这会给你大约 3.7 倍的数据效率胜利。这些数据缩放定律另一个有意思的方面是:如果你看图例里的函数形式,你会发现它们的指数都非常相似,渐近线也都非常相似。这为什么重要?因为这表明,即使你在大得多的 token 规模上重复这些实验,只要你相信这些数据缩放定律可以外推,这个数据效率胜利在你实际拥有的 token 数量上都会是恒定的。所以这表明,这个双重联合缩放定律配方,即便你愿意把种子 token 数推到 10 万亿 token、或如今人们做预训练用的任何量级,它都有 5 倍的数据效率胜利。那么现在我来讲一些方法,

[62:30] **SPEAKER_05:** to sort of make this data efficiency win perhaps slightly more practical. And so even though these recipes require a lot of training compute, we also show that you can reduce the amount of inference compute you need by using distillation. So the plot on the right here, the purple line corresponds to the same regularized recipe. The light blue points correspond to the same ensemble scaling. So we first show that

> 让这个数据效率胜利也许更实用一些。尽管这些配方需要大量的训练算力,我们也展示了你可以通过蒸馏(distillation)来减少你所需的推理算力。所以右边这张图里,紫色的线对应同一个正则化配方,浅蓝色的点对应同样的集成缩放。我们首先展示的是,

[62:52] **SPEAKER_05:** what you can do is you can take an 8 ensemble, which is roughly 2.4 billion total parameters, and you can distill it into a single dense 300 million parameter model, with a blank star in the bottom. And you can do this while retaining roughly 83% of the loss improvement. So this shows you that data efficiency is not something that you need a large amount of inference compute for. If you're willing to amortize the test time compute during training time, you can get an extremely data efficient model that's still very, very small. The other surprising result we show in this section

> 你可以做的是:你拿一个 8 集成(8-ensemble),总共大约 24 亿参数,把它蒸馏进一个单一的、稠密的 3 亿参数模型里,也就是底部那个空心星标。而你能在保留大约 83% 的损失改善的同时做到这一点。所以这向你表明,数据效率并不是一件需要大量推理算力才能获得的事。如果你愿意在训练时把测试时算力摊销掉,你就能得到一个数据效率极高、却仍然非常非常小的模型。我们在这一节展示的另一个令人惊讶的结果是,

[63:26] **SPEAKER_05:** is that you can do self-distillation to even improve your loss. So with self-distillation, what we're doing is we're starting with the 300 million parameter model at the start of the light blue curve, and then we're distilling this model into a fresh 300 million parameter model, which is the green star. And what we find is very surprisingly, even doing self-distillation gives you huge loss improvement. It even beats the asymptote of the regularized recipe. This is actually pretty counterintuitive,

> 你可以做自蒸馏(self-distillation)来进一步改善你的损失。自蒸馏里我们做的是:从浅蓝色曲线起点处那个 3 亿参数的模型开始,然后把这个模型蒸馏进一个全新的 3 亿参数模型里,也就是那个绿色星标。我们发现,非常令人惊讶的是,即使只做自蒸馏,也能给你带来巨大的损失改善,它甚至超过了正则化配方的渐近线。这其实相当反直觉,

[63:53] **SPEAKER_05:** and we have a longer sort of description of this result in the paper, but it turns out to have pretty surprising connections to ensembling. And there's actually a view from prior work on viewing self-distillation as implicitly training to ensemble. We also show that even though we're only chasing IID val loss in all of our experiments, pretty much all of the trends in this paper directly work on downstream benchmarks. And this was like a fully held out sort of test set where we only looked at the benchmarks at the very end of the paper because advisors told us to. And you can see that everything tracks.

> 我们在论文里对这个结果有更长的描述,但结果发现它与集成有着相当出人意料的联系。事实上,先前的工作里有一种观点,把自蒸馏看作是隐式地训练成一个集成。我们还展示,尽管在我们所有实验里我们只追求 IID 验证损失,这篇论文里几乎所有的趋势都能直接迁移到下游基准(downstream benchmarks)上。而这是一个完全留出的(held out)测试集,我们只在论文的最后才去看这些基准,因为导师让我们这么做。你可以看到一切都能对得上。

[64:29] **SPEAKER_05:** The standard recipe overfits still, model scaling gives you improvements, ensembling is even better, and you can still retain a lot of the benefits through distillation. And finally, we also show that you can do this for other settings beyond pre-training, so things like continued pre-training. So we consider a setup where you're trying to CPT a 3B model, and we assume access to sort of this restricted set of 4 billion math-related tokens, where the whole corpus of data is actually 73 billion tokens. And what we show is that if you're willing to do these data efficiency tricks, like aggressive epocking and things like ensembling, you can match the performance of training on the full 73 billion tokens even using only 4 billion tokens, which is roughly a 17x data efficiency win. So to sort of wrap up this talk,

> 标准配方依然过拟合,模型缩放给你带来改善,集成甚至更好,而且你通过蒸馏仍能保留很多好处。最后,我们还展示了你可以把这套做法用在预训练之外的其他设定上,比如持续预训练(continued pre-training,CPT)。我们考虑一个设定:你要对一个 3B 模型做 CPT,我们假设只能访问这样一个受限的、40 亿数学相关 token 的集合,而整个数据语料其实有 730 亿 token。我们展示的是,如果你愿意用这些数据效率技巧,比如激进的多轮训练(epocking)和集成之类,你即便只用 40 亿 token,也能匹敌在全部 730 亿 token 上训练的性能,这大约是 17 倍的数据效率胜利。那么来给这次演讲收个尾,

[65:16] **SPEAKER_05:** maybe the main point I want to make is that when you're constrained by data and you're unconstrained by compute in this sort of new algorithmic machine, the types of algorithmic choices you make matter a lot, and we should be willing to sort of rethink every aspect of the stack. In this paper, we mostly do this by revisiting a lot of these classical ideas from machine learning and deep learning. Things like regularization, ensembling, distillation have existed for many, many years. And we also introduce this evaluative tool of asymptotes. And maybe the hope is that

> 也许我想强调的主要一点是:当你在这种新的算法体制里受数据约束、却不受算力约束时,你所做的算法选择类型影响非常大,我们应该愿意重新思考整个技术栈的每一个方面。在这篇论文里,我们主要是通过重新审视很多机器学习和深度学习里的经典想法来做这件事。像正则化、集成、蒸馏这些东西已经存在很多很多年了。我们还引入了渐近线这个评估工具。也许我们的希望是,

[65:49] **SPEAKER_05:** if you're willing to chase algorithms that have lower compute asymptotes, these will give you better ideas for data efficiency. But ultimately, what we really want to do is we want these asymptotes to help us develop new and better ideas under infinite compute that don't already exist. And so if you're interested in the details, that's the QR code for the paper. And we've also done some follow-up work on looking at how synthetic data interacts with data efficiency. So feel free to check that out as well

> 如果你愿意去追求那些拥有更低算力渐近线的算法,它们会给你带来关于数据效率的更好想法。但归根结底,我们真正想做的是,让这些渐近线帮助我们在无限算力下开发出尚不存在的、全新且更好的想法。所以如果你对细节感兴趣,这是论文的二维码。我们还做了一些后续工作,研究合成数据如何与数据效率相互作用。所以也欢迎去看看那部分,

[66:15] **SPEAKER_05:** if you're interested. Thanks.

> 如果你感兴趣的话。谢谢。

[66:17] **SPEAKER_03:** All right. Thank you guys so much for coming. This is like a dream come true. I'm in one of my favorite places that was most important places in my life. And now I get to talk about AI here.

> 好的。非常感谢大家的到来。这简直像是美梦成真。我身处我最喜欢的地方之一,它曾是我人生中最重要的地方之一。而现在我竟然能在这里谈论 AI。

[66:33] **SPEAKER_03:** So super, super fun. I think there's a lot of potential for this club. I think I don't have nearly, you know, 1% of all the ideas that we probably have to make this club really great in all of your heads. And so we want to make sure all of you guys get in on the Slack. So I'll make sure that, you know,

> 所以真的非常非常有趣。我觉得这个俱乐部有很大的潜力。我觉得,要把这个俱乐部做得真正出色,你们所有人脑子里的那些点子,我大概连其中的 1% 都还想不到。所以我们想确保你们所有人都加入 Slack。所以我会确保,你知道,

[66:51] **SPEAKER_03:** please send me a note if you're not already on there. And then we can kind of make this thing whatever we want. So it's kind of fun. And I intend to. So like, please come with ideas.

> 如果你还没在上面,请给我发个消息。然后我们就可以把这件事做成我们想要的任何样子。所以这挺好玩的。而且我打算这么做。所以,请带着想法来。

[67:00] **SPEAKER_03:** We want to make this thing that's super fun. Obviously, you know, there's some ground rules. Be respectful. All that kind of stuff. And definitely be involved.

> 我们想把这件事做得超级有趣。当然,你知道,有一些基本规则。要相互尊重。诸如此类。而且一定要积极参与。

[67:07] **SPEAKER_03:** And that's kind of the biggest thing that we really only really ask. That's all I got. That's a wrap. Go get some boba tea. Thank you.

> 而这大概就是我们真正唯一要求的最重要的一点。我要说的就这些了。到此为止。去喝点珍珠奶茶吧。谢谢。
