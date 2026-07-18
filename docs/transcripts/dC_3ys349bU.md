# 全文转录 · 每个创始人都该懂的机器学习技术:扩散模型

> ▶ [YouTube](https://www.youtube.com/watch?v=dC_3ys349bU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/dC_3ys349bU.md) &nbsp;·&nbsp; The ML Technique Every Founder Should Know

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_00:** Welcome back to another episode of Decoded. Today, I'm sitting down with YC visiting partner Francois Chaubard to talk about one of the most important topics in AI today, diffusion. Francois has been doing computer vision since 2012 when he started in Fei-Fei Li's lab. And after a decade running focal systems, he's currently back at Stanford finishing his PhD, working on diffusion-based world models for AGI.

> 欢迎回到新一期的 Decoded。今天,我请到了 YC 访问合伙人 Francois Chaubard,来聊聊当下 AI 领域最重要的话题之一——扩散(diffusion)。Francois 从 2012 年就开始做计算机视觉,当时他在李飞飞的实验室起步。在经营 Focal Systems 十年之后,他目前回到斯坦福完成博士学业,研究面向 AGI 的、基于扩散的世界模型。

[00:19] **SPEAKER_00:** We're going to break down what diffusion is, how it's evolved over the past decade, and how it's used today. Francois, thanks for being here.

> 我们会拆解一下什么是扩散、它在过去十年里如何演进,以及如今它是怎么被使用的。Francois,谢谢你来。

[00:32] **SPEAKER_01:** Thank you for having me.

> 谢谢你邀请我。

[00:33] **SPEAKER_00:** Well, we just got back from NeurIPS. We just spent a lot of time talking to researchers and thinking about all the newest models out there. I think we saw diffusion pop up over and over and newer versions of this type of approaches that are not autoregressive LLMs. And so I wanted to talk to you about those today.

> 我们刚从 NeurIPS 回来。我们花了很多时间和研究者交流,思考外面各种最新的模型。我感觉扩散一次又一次地冒出来,还有这类方法的新版本——它们不是自回归的大语言模型。所以我今天想和你聊聊这些。

[00:49] **SPEAKER_00:** So first, why don't we start by defining what is diffusion?

> 那么首先,我们不妨从定义什么是扩散开始?

[00:53] **SPEAKER_01:** Diffusion is a very fundamental machine learning framework that allows you to learn any p-data, any probability of data for any domain as long as you have the data.

> 扩散是一个非常基础的机器学习框架,只要你有数据,它就能让你学到任意的 p-data——任意领域的数据概率分布。

[01:03] **SPEAKER_00:** So you're trying to learn some data distribution. That's right. Now, in a sense, all LLMs or all machine learning models are about learning data distributions. That's true.

> 也就是说,你是在试图学习某个数据分布。没错。从某种意义上说,所有的大语言模型、所有机器学习模型都是在学习数据分布。确实如此。

[01:11] **SPEAKER_00:** How does diffusion in particular, what stance does it take or what approach does it take to being able to learn distribution?

> 那么扩散具体是怎么做的,它采取什么样的立场或方法来学习分布?

[01:16] **SPEAKER_01:** Yeah, I mean, I think you can use diffusion to always do that. The thing where it stands out in particular is mapping from high dimensions to high dimensions, especially in low data regimes. So say I only have 30 images of Gary, which I actually have some code that we're going to walk through. Cool.

> 是的,我觉得你总能用扩散来做到这一点。它特别突出的地方在于从高维到高维的映射,尤其是在数据量很少的情况下。比如说我只有 30 张 Gary 的图片——待会儿我确实有一些代码会带大家过一遍。很好。

[01:31] **SPEAKER_01:** I only have 30 images of Gary. And again, we're in this thousand by one, thousand by three dimensional space, and I want to map to another three million dimensional space with only 30 training samples and I can still do it. And it's pretty powerful in that way.

> 我只有 30 张 Gary 的图片。再说一遍,我们处在一个 1000 乘 1000 乘 3 维的空间里,而我想只用 30 个训练样本就映射到另一个三百万维的空间,我依然能做到。从这个角度看它相当强大。

[01:48] **SPEAKER_00:** Okay, cool. So you have this ability to use relatively small amounts of data compared to the dimensionality to learn a p-data. That's right. What's the basic process by which diffusion works?

> 好,很酷。所以相对于维度而言,你能用相对少量的数据来学到一个 p-data。没错。那扩散工作的基本流程是什么?

[01:58] **SPEAKER_00:** Like just walk through, like at a very high level, and we'll walk through the math a little bit later, but at a very high level, how does this process actually work?

> 就先高层次地讲一遍,数学部分我们稍后再过,但从很高的层面来看,这个过程到底是怎么运作的?

[02:04] **SPEAKER_01:** We take some sample of the data, an image of Ankit, an image of Gary, and we just hit it with noise, and then we just keep hitting it with noise, and we create this train of noised up images. It's very easy to create noisy images, right? It's hard to walk backwards and create from noise images of you or Gary. And so then we flip it, and then we try to teach the model to reverse that process.

> 我们取数据的某个样本,比如一张 Ankit 的图、一张 Gary 的图,然后不断往上加噪声,一直加,于是就造出一串越来越有噪声的图像。制造有噪声的图像很容易,对吧?但要反过来,从噪声还原出你或 Gary 的图像就很难。所以我们把它翻转过来,试图教模型去逆转这个过程。

[02:31] **SPEAKER_01:** And that's basically it.

> 基本上就是这样。

[02:32] **SPEAKER_00:** Okay, cool. So it's basically a noise-reversal process. A de-noiser and a de-noiser, and the de-noiser is the model that you end up training. Exactly, yeah. You will basically teach your force

> 好,很酷。所以它本质上是一个噪声逆转的过程。一个去噪器,去噪器就是你最终要训练的模型。完全正确。你基本上是在教你的……

[02:40] **SPEAKER_01:** and give it noised up images, and then have it learn intermediate representations to get back to p-data.

> ……喂给它加了噪声的图像,然后让它学到中间的表示,从而回到 p-data。

[02:48] **SPEAKER_00:** Cool, nice. And what kinds of stuff is diffusion used for today? What are some applications that it's widely deployed in?

> 很好,不错。那如今扩散都被用来做哪些事情?有哪些它被广泛部署的应用?

[02:53] **SPEAKER_01:** It's honestly surprising how applicable this process is. I think the original 2015 Joshua-Sold-Dixie paper was on CIFAR-10, which is just images. And I think it has its roots in images, but it is far more sprawling than just images. As you've seen, DeepMind just won the Nobel Prize for doing this exact procedure on protein folding.

> 说实话,这个过程的适用范围之广令人惊讶。我记得 2015 年 Joshua Sohl-Dickstein 最初的论文用的是 CIFAR-10,也就是图像。它的根基在图像,但它的触角远远不止图像。就像你看到的,DeepMind 刚刚因为把完全相同的流程用在蛋白质折叠上而获得了诺贝尔奖。

[03:20] **SPEAKER_01:** You can drive cars with this, with the diffusion policy paper, which is like an insane result. You can predict the weather. There's really no limit to the things that this can do.

> 你可以用它来开车,就是那篇 diffusion policy 的论文,那简直是个疯狂的成果。你可以用它预测天气。它能做的事情真的没有边界。

[03:32] **SPEAKER_00:** Yeah, it's pretty incredible to see. I mean, you have these image and video generation models that seem to be really advancing over the last few years. Stable diffusion is the one that I think many people have heard of, and then newer versions of it seem to be using this as well. And then, yeah, in the world of life sciences that my company was in too, I think we see this newest generation of life sciences, AI companies are heavily investing in this set of technologies.

> 是的,看到这些确实很不可思议。我是说,过去几年里这些图像和视频生成模型看起来在飞速进步。Stable Diffusion 是很多人都听说过的一个,它的新版本似乎也在用这套方法。然后,在我自己公司所处的生命科学领域里,我觉得我们看到最新一代的生命科学 AI 公司正在大力投资这一套技术。

[03:52] **SPEAKER_00:** There's a model called DiffDoc that works really well for predicting small molecule binding to proteins. And then, yeah, AlphaFold, especially the newest AlphaFold versions use diffusion pretty heavily. It's really cool to see the same core, piece of technology applied to so many different domains. Yeah, yeah.

> 有一个叫 DiffDock 的模型,在预测小分子与蛋白质结合方面效果非常好。还有 AlphaFold,尤其是最新版本的 AlphaFold,相当大量地使用了扩散。看到同一项核心技术被应用到这么多不同领域,真的很酷。是的,是的。

[04:06] **SPEAKER_00:** This class of models has evolved over the years, and there's a whole slew of papers someone could read. So you should probably go read the papers to learn all the details. But maybe at a high level, we can try to trace out a few of the key innovations that happened, starting with the paper you already mentioned that now led to the newest versions of these models. So how would you map those out?

> 这一类模型这些年一直在演进,有一大堆论文可以读。所以要了解所有细节,你大概应该去读那些论文。但也许在高层次上,我们可以试着梳理出其中几个关键创新,从你已经提到的那篇、后来催生了这些模型最新版本的论文开始。你会怎么勾勒这条脉络?

[04:24] **SPEAKER_00:** Like, what was the first kind of turn of the crank from this very high level diffusion process you outlined? What was the first version of that that started to work?

> 比如说,从你刚才勾勒的这个非常高层次的扩散过程出发,第一次"摇动曲柄"是怎样的?它第一个开始奏效的版本是什么样子?

[04:33] **SPEAKER_01:** Yeah. So I think the 2015 original Joshua paper is it put up all the key pieces, all key components of modern diffusion. And so like now we're just playing with different things. So the scheduler, how do we add noise?

> 是的。我觉得 2015 年 Joshua 最初那篇论文,已经把现代扩散所有的关键部件、所有关键组件都搭好了。所以现在我们只是在摆弄不同的东西。比如调度器(scheduler)——我们怎么加噪声?

[04:47] **SPEAKER_01:** At what weight? Like that's a whole part that we can discuss. What's the loss function? Should I predict, should the deep learning model condition upon X of T predict the actual data, X of T minus one?

> 以什么权重加?这本身就是可以专门讨论的一大块。损失函数是什么?我该预测什么——深度学习模型在给定 X_t 的条件下,应该预测真实数据 X_{t-1} 吗?

[04:58] **SPEAKER_01:** Or should it predict the error that was just added to it? Or should it predict the velocity? Which is the error divided by the time. Should it predict the velocity of the start and the end?

> 还是它应该预测刚刚加上去的误差?还是应该预测速度(velocity)?也就是误差除以时间。它该预测从起点到终点的速度吗?

[05:10] **SPEAKER_01:** That's called flow matching. There's all these different plays on what the loss function is.

> 那就叫流匹配(flow matching)。围绕损失函数是什么,有各种各样不同的玩法。

[05:14] **SPEAKER_00:** So in all of those, the idea is still to do denoising. Yes. But the objective for each of them is somewhat different from each other. And they're all pretty closely related, whether it's basically a delta between two things, or the previous step, or the first step.

> 所以在所有这些方案里,核心思路仍然是做去噪。是的。但它们各自的目标彼此有些不同。而它们又都相当密切地相关——不管是两个东西之间的差值,还是上一步,还是第一步。

[05:27] **SPEAKER_00:** How do these all actually come together? But these are series of papers that happened one after another?

> 这些是怎么真正汇聚到一起的?它们是一篇接一篇出现的一系列论文吗?

[05:32] **SPEAKER_01:** Yeah. Okay. Yeah. I think.

> 是的。嗯。对。我觉得……

[05:33] **SPEAKER_01:** We just kind of hill climbed on this Farashay inception distance metric. That's kind of a kooky, weird measure to see how good an image is. But we just kept getting better and better and better on it, by doing these little tricks. And so it turns out that predicting the actual data itself is actually quite hard.

> ……我们基本上就是在 Fréchet Inception Distance(FID)这个指标上做爬山优化。这是个有点古怪、奇特的度量,用来衡量一张图像有多好。但通过这些小技巧,我们在它上面越做越好、越来越好。结果发现,直接预测真实数据本身其实相当难。

[05:50] **SPEAKER_01:** And maybe predicting the error is actually easier. And then predicting the velocity was even easier than that. And then predicting the global error across the entire diffusion schedule is even easier than that. And just kept.

> 也许预测误差反而更容易。然后预测速度比那还更容易。再然后,预测整个扩散调度上的全局误差又比那更容易。就这样一直……

[06:02] **SPEAKER_01:** Finding easier and easier ways to basically sample from noise to data.

> ……找到越来越简单的方法,本质上就是从噪声采样到数据。

[06:09] **SPEAKER_00:** And here when you say easier, was the ease largely driven by it was mathematically simpler? Or it was easier to implement an engineer? Or simpler to reason about? Or what got easier really?

> 这里你说"更容易",这个容易主要是因为数学上更简单吗?还是更容易实现和工程化?还是更容易推理?究竟是什么变容易了?

[06:22] **SPEAKER_01:** It actually is that too, but I didn't mean it that way. What I actually meant was it's easier for the model to learn. But it is also, and we'll go through some coding examples, the math actually got easier. And the code got smaller, which is actually oppositely true in most of the case in most machine learning.

> 其实那些也都成立,但我本来不是那个意思。我真正想说的是,它对模型来说更容易学。不过——我们也会过一些代码例子——数学确实变简单了,代码也变短了,而这在大多数机器学习的情形里恰恰是反过来的。

[06:41] **SPEAKER_01:** Actually, things get more complicated. I think we started with UNETs, and that was the predominant architecture. We didn't really talk about architectures that much, but then we got into these diffusion transformers, and this cross-attention mechanism, and things like that. And so, yeah, we just kept getting better and better at reducing FID.

> 通常事情会变得更复杂。我们一开始用的是 UNet,那是当时主流的架构。我们其实没怎么谈架构,但后来我们进入了这些扩散 Transformer、这种交叉注意力机制之类的东西。所以是的,我们在降低 FID 上越做越好。

[07:00] **SPEAKER_01:** Hmm, interesting. Dive into some code examples? Let's do it. Let's do it.

> 嗯,有意思。要不要深入看几个代码例子?来吧。开始吧。

[07:03] **SPEAKER_01:** I'll walk you through, I made about one, two, three, four, five, six, seven of these that I implemented with varying levels of success. But all the structures are going to be the same. So the Joshua paper, the non-equilibrium thermodynamics paper, you can see here are some nice images of Gary, you can see here. Very nice.

> 我带你过一遍,我大概做了一、二、三、四、五、六、七个这样的实现,成功程度各不相同。但所有的结构都是一样的。那么这是 Joshua 那篇论文,即"非平衡热力学"那篇——你可以看到这里有几张不错的 Gary 的图像。非常好。

[07:24] **SPEAKER_01:** This is what I could find online. Nice. And then-

> 这是我在网上能找到的。不错。然后……

[07:27] **SPEAKER_00:** So those are images of Gary that you've down sampled so that they're 1,000 by 1,000, or they're smaller, I think. Yeah, I think these are 64 by 64. 64 by 64. Yeah, they're really small.

> 所以这些是你降采样过的 Gary 的图像,让它们变成 1000 乘 1000,或者更小,我猜。对,我想这些是 64 乘 64。64 乘 64。对,它们真的很小。

[07:36] **SPEAKER_01:** This is just a very small example. Yeah. 64, and then I randomly augmented to create more data. Great.

> 这只是个非常小的例子。对。64,然后我做了随机增广来造出更多数据。很好。

[07:41] **SPEAKER_01:** Because I was lazy, and that was easier than downloading more images of Gary. Okay, cool. Didn't want to get a security call on you. Exactly.

> 因为我懒,而且那比再去下载更多 Gary 的图片更省事。好,很好。不想害你接到安保部门的电话。正是如此。

[07:49] **SPEAKER_01:** So, and then I implemented this diffusion schedule, and this is probably one of the most important, like of all the parts of diffusion that's difficult to comprehend, I would say that the noise schedule is actually the hardest part, to understand, that I really, like, I struggled with myself. And so, if you can see here, the noise that's added from time step 0 to 10 to 25, all the way to 100, it's clearly destroying the structure. Yes. And then we want to train the model.

> 然后我实现了这个扩散调度,而在扩散所有难以理解的部分里,这可能是最重要的之一——我要说,噪声调度其实是最难理解的部分,我自己也确实为它挣扎过。你可以看到这里,从时间步 0 到 10 到 25,一直到 100 所加的噪声,它显然在摧毁结构。是的。然后我们想训练模型。

[08:16] **SPEAKER_00:** Where you end is basically random static.

> 你最后到达的地方基本上就是随机的雪花噪点。

[08:18] **SPEAKER_01:** Exactly. And we want to basically reverse this, and from here, get to here, and have the model get to that point, get to this point, get to that point, et cetera, et cetera. And so, the interesting part, and this is Joshua really, you know, implemented almost everything that we needed for diffusion. And there was just a few little tweaks that were missing, and he didn't scale it up.

> 正是。我们基本上想把这个过程逆转,从这里回到这里,让模型走到那个点、这个点、那个点,以此类推。有意思的是,Joshua 其实几乎实现了我们做扩散所需要的一切。只是缺了几个小的调整,而且他没有把它规模化放大。

[08:39] **SPEAKER_01:** That's, to me, the parts that we're missing. And if you see here, the noise schedule. So, it would make sense to me that I would have linear interpolation between the image and the noise. And I would start with like one and zero.

> 在我看来,那就是当时缺失的部分。你看这里,噪声调度。直觉上,我会觉得在图像和噪声之间做线性插值是合理的。我会从大概 1 和 0 开始。

[09:00] **SPEAKER_01:** Sure. One being the image, and zero being the noise. And you gradually add it. And I linearly add it.

> 当然。1 代表图像,0 代表噪声。然后你逐渐加进去。我是线性地加。

[09:05] **SPEAKER_01:** But if you do that, it actually is massively unstable. Because the instantaneous amount of error that you're adding is very small in the beginning. Right. If you think about like an image.

> 但如果你那样做,它其实极其不稳定。因为一开始你瞬时加进去的误差量非常小。对。如果你想象一张图像。

[09:15] **SPEAKER_01:** Like on a relative basis. On a relative basis. And then at the end, you have to destroy all the, to get to a complete noise, you need to add a lot of error. Yeah.

> 相对而言。相对而言。而到最后,你得摧毁全部——要达到完全的噪声,你需要加入大量误差。是的。

[09:23] **SPEAKER_01:** And so like, if you're a model, and you're just looking at this little chunk of the noise schedule, then you have to handle a lot of error, in one step. And on this side of the schedule, you need to handle such small amounts of error. And what you actually want is constant, like relatively constant amount of error being introduced every single time step. Right.

> 所以如果你是模型,只看噪声调度里这一小块,那么你就得在一步之内处理大量误差。而在调度的这一侧,你要处理的误差又非常小。你真正想要的是,每一个时间步引入的误差量是恒定的、相对恒定的。对。

[09:43] **SPEAKER_01:** And that, the cumulative sum of all that error actually ends up looking like this, like this curve here.

> 而所有这些误差的累积和,最终看起来就是这样,就是这里这条曲线。

[09:50] **SPEAKER_00:** That's the pink curve. Yeah.

> 就是那条粉色的曲线。对。

[09:52] **SPEAKER_01:** And so, they call this a beta schedule. Beta is the diffusion rate. The rate of diffusion that I'm doing while I'm rolling this. This thing out from time zero to time T, capital T, and so you can see here, the beta schedule.

> 他们把这个叫做 beta 调度。beta 是扩散率——我在从时间 0 展开到时间 T(大写 T)的过程中所进行的扩散速率。所以你可以在这里看到 beta 调度。

[10:07] **SPEAKER_01:** So, we usually have some beta min to beta max. And then, one minus that is the alpha. And you can think about the beta as like, how much noise I'm adding at every time step. Yup.

> 我们通常有一个从 beta 最小值到 beta 最大值的范围。然后 1 减去它就是 alpha。你可以把 beta 理解为:我在每个时间步加了多少噪声。对。

[10:18] **SPEAKER_01:** And you think about the alpha as how much. How much data is lost, basically? Yeah. Being retained.

> 而 alpha 你可以理解为……基本上就是丢失了多少数据?对,是保留了多少。

[10:23] **SPEAKER_01:** And then, the term that really matters is the alpha bar, and these are the weights that are used and it has this kind of, like, one minus sigmoid looking thing. But that's basically the noise schedule. And once you get that right, really this part here, then everything else just works. And then I train some model and then we can actually.

> 然后,真正重要的那一项是 alpha bar,它就是所用的权重,长得有点像"1 减 sigmoid"那种形状。但这基本上就是噪声调度。一旦你把它——真的就是这一部分——弄对了,其他一切就都顺理成章地成立了。然后我训练某个模型,接着我们就可以实际……

[10:45] **SPEAKER_00:** So there, what was the training objective again? So you're adding this noise and the training objective was to do what exactly?

> 那么,训练目标再说一遍是什么?你在加这些噪声,那训练目标究竟是要做什么?

[10:51] **SPEAKER_01:** In this case, it's to minimize the KL divergence between the real distribution and the distribution that I'm learning. And so, I won't go through the code for this one, because it's a little bit hairier, but you can kind of see the result on these generated images after 100 diffusion steps at inference time. And you can see that that Farashay inception distance is 222, which is like extremely high today. Like modern day would be like maybe like eight or 10 or something.

> 在这个例子里,是最小化真实分布与我正在学习的分布之间的 KL 散度。这个我就不过代码了,因为它有点更麻烦,但你大致可以在这些生成图像上看到结果——在推理时经过 100 个扩散步之后的效果。你可以看到那个 Fréchet Inception Distance 是 222,以今天的标准来说这极其高。现在的水平大概会是 8 或 10 之类的。

[11:19] **SPEAKER_00:** And what's interesting here, I mean, you kind of scroll through it there, but it's, you mentioned it, there's quite a lot of code that it actually takes to do that KL divergence base loss. I suspect that in these later models, you're going to show, it gets significantly simpler. So, I'm just mentally noting that because I suspect there's going to be an interesting contrast to draw between these two.

> 这里有意思的是——你刚才快速划过去了,但你也提到了——要实现那个基于 KL 散度的损失,实际上需要相当多的代码。我猜在你接下来要展示的后期模型里,它会显著变简单。所以我先在心里记一笔,因为我怀疑这两者之间会有个有趣的对比可以拿来讲。

[11:37] **SPEAKER_01:** Yeah. So, the next one I would like to show is flow matching, which is just so beautiful and simple. And this was out of Meta, Yaron Lipman, where he basically said, we don't need a lot of this stuff. What we need to do, forget the, if you think about the noising process as being this, like I start from data, I randomly sample a vector of noise, and I just go in this direction, and then I do it again.

> 是的。接下来我想展示的是流匹配,它简直美得又简单。这出自 Meta 的 Yaron Lipman,他基本上说,我们不需要这么多东西。我们要做的——先别管那些——如果你把加噪过程想象成这样:我从数据出发,随机采样一个噪声向量,朝这个方向走一步,然后再来一次。

[12:05] **SPEAKER_01:** I go in this direction, and I do it again, I go in that direction, I go in this direction, that direction, and then I'm here at noise. And then you have to teach the thing to go in the exact opposite path and you have to do this very circuitous path. And so, at test time, it's actually quite expensive. You have to do, we've all waited for ChatGPT or Midjourney to like make an image, and it takes a while.

> 我朝这个方向走,再来一次,朝那个方向走,这个方向、那个方向,然后我就到了噪声这里。接着你得教这个东西沿着完全相反的路径走回去,而且你得走这条非常曲折的路。所以在测试时,这其实相当昂贵。我们都等过 ChatGPT 或 Midjourney 生成一张图,那要花上一会儿。

[12:25] **SPEAKER_01:** Right. What it's doing is like a thousand calls to the model, again and again, iterating through to get to that point of pData. Right. Instead.

> 对。它其实是在对模型做上千次调用,一次又一次地迭代,才走到 p-data 那个点。对。而作为替代……

[12:32] **SPEAKER_00:** And like intuitively, it's like, okay, we're doing the circuitous path, but surely there's a shorter path between those two.

> 而且直觉上会觉得,好吧,我们在走这条曲折的路,但这两点之间肯定有一条更短的路。

[12:38] **SPEAKER_01:** Yes. And so, that's what makes flow matching so cool, to me at least, is that they said, forget all of that intermediary results. There is a velocity, a global velocity between the noise and the data, and it's just this direction, and it's just this straight line. And I don't care where you are, go in that line, wherever you are, you're over here, go in that line and teach it to go in that line.

> 对。所以流匹配之所以酷——至少对我来说——就在于他们说:忘掉所有那些中间结果吧。噪声和数据之间存在一个速度、一个全局速度,它就是这个方向,就是这条直线。我不在乎你在哪儿,就沿这条线走;无论你在哪儿,你在这边,就沿这条线走,并且教它沿这条线走。

[13:01] **SPEAKER_01:** And that's what flow matching does. And so, I'll show you the code. Yeah, let's see that in the code. Yeah, but it's like five lines of code.

> 这就是流匹配所做的事。我给你看代码。好,来看看代码里是怎样的。对,但它大概就五行代码。

[13:05] **SPEAKER_01:** It really is quite simple. And so, this is pretty cool. So, here you go. You basically have like 10, 15 lines of code that is the most powerful machine learning procedure ever.

> 它真的相当简单。所以这挺酷的。看,就是这样。你基本上用大约 10 到 15 行代码,就得到了有史以来最强大的机器学习流程。

[13:19] **SPEAKER_01:** So, I have some data, an image of Gary. Yeah. I have some noise, some isotropic Gaussian noise that I sample from. Yeah.

> 我有一些数据,一张 Gary 的图。对。我有一些噪声,一些我从中采样的各向同性高斯噪声。对。

[13:28] **SPEAKER_01:** There's some time that I'm trying to index into in the diffusion schedule, and I create xt, which is the image at the noised up image that's somewhere between extremely noisy and not noisy at all.

> 有一个我要在扩散调度里索引到的时间点,然后我构造出 x_t,也就是加了噪声的图像——它介于极度嘈杂和完全无噪之间的某处。

[13:41] **SPEAKER_00:** And that's basically just the sampling procedure. It's t times data plus one minus that times noise.

> 而这基本上就是采样的过程。它是 t 乘以数据,加上(1 减 t)乘以噪声。

[13:47] **SPEAKER_01:** That's right. And then I compute the velocity which is independent of the time. I don't care where you are, it's just this global velocity, which is just the noise minus the data, and then it, I return that back to my training loop, which is the shortest amount of code training loop I've ever written, which is five lines of code. I have my batch, I have some time, I sample from that function I just explained before, and then I have my prediction from the model.

> 没错。然后我计算速度,它与时间无关。我不在乎你在哪儿,它就是这个全局速度,也就是噪声减去数据,然后我把它返回给我的训练循环——那是我写过的最短的训练循环,只有五行代码。我有我的批次,有某个时间,我从我刚才解释过的那个函数里采样,然后得到模型给出的预测。

[14:17] **SPEAKER_01:** I feed it in this some noise up image, somewhere between lots of noise and little noise, x of t, let's call it. And I just want it to predict the velocity that I want to go.

> 我把这张加了噪声的图喂给它——介于大量噪声和少量噪声之间的某处,就叫它 x_t 吧。而我只想让它预测出我想要前进的那个速度。

[14:29] **SPEAKER_00:** And this is also really powerful because here, you know, you have model abstracted, but that model can be any model. That's right. So, you can put in whatever the relevant model is for your distribution, whether that's a protein model for proteins, or if it's an LLM for text, or an image-based model for images, that is a very clean abstraction, as long as you can then predict this velocity and then move in that direction.

> 而这也非常强大,因为在这里,你把模型抽象出来了,但那个模型可以是任何模型。没错。所以你可以放进任何与你的分布相关的模型——不管是用于蛋白质的蛋白质模型,还是用于文本的大语言模型,还是用于图像的基于图像的模型——这是一个非常干净的抽象,只要你随后能预测出这个速度,并朝那个方向移动。

[14:51] **SPEAKER_01:** That's right. This code here has nothing to do with images. It could be weather data, it could be, you know, a stock market data, it could be trajectories from a robotics and a tele-ops setup, it could be proteins, it could be DNA, it doesn't really matter. It's all the exact same code.

> 没错。这里这段代码和图像毫无关系。它可以是天气数据,可以是股市数据,可以是来自机器人和遥操作装置的轨迹,可以是蛋白质,可以是 DNA,都无所谓。全都是完全相同的代码。

[15:08] **SPEAKER_01:** And so, and then also we haven't talked about the architecture. So, like this model here could be anything you want it to be. Like it could be a RNN, it could be a UNET, which is typically, you know, traditionally is, and modernly, they use these diffusion transformers doing this cross attention mechanism. And so, it can be whatever you want.

> 而且,我们还没谈到架构。这里这个模型可以是你想要的任何东西。它可以是 RNN,可以是 UNet(传统上通常就是这个),而现代做法里,他们用这些做交叉注意力机制的扩散 Transformer。所以它可以是任何你想要的东西。

[15:29] **SPEAKER_01:** But all that is independent from whether or not you're doing flow matching or not.

> 但所有这些,都和你是否在做流匹配无关。

[15:34] **SPEAKER_00:** I think this is like a really profoundly interesting result in that, especially this thing we often assume as models have gotten more sophisticated, that they become less accessible for people to understand. But this is quite literally 10 lines of code. Right. That explains essentially all of the most important kind of mathematical and fundamental foundations of the models that we all see, as generating basically like magical AI results on our phones.

> 我觉得这是个极其有意思的结果,尤其是我们常常有个假设:随着模型变得更复杂,它们对人们来说就变得更难理解。但这真的就是字面意义上的 10 行代码。对。它基本上解释了我们所看到的那些模型——就是在我们手机上生成那种近乎魔法般 AI 结果的模型——最重要的数学与根本基础。

[16:00] **SPEAKER_00:** Of course, there's lots of engineering how you scale them up. Right. That model could be a 100 billion parameter. Across a thousand data centers.

> 当然,如何把它们规模化放大有大量的工程工作。对。那个模型可能是一千亿参数的。分布在上千个数据中心里。

[16:07] **SPEAKER_01:** Totally.

> 完全正确。

[16:08] **SPEAKER_00:** You know, GPUs. Totally.

> 你懂的,GPU。完全正确。

[16:09] **SPEAKER_01:** Yeah, 100 percent.

> 是的,百分之百。

[16:09] **SPEAKER_00:** So, it's the engineering that's the really hard part there, but a lot of the basic machine learning math is actually quite straightforward.

> 所以那里真正难的部分是工程,但很多基础的机器学习数学其实相当直接明了。

[16:15] **SPEAKER_01:** That's right. Yeah. And so, there's a bunch of these like tangent fields to diffusion that all have some different interpretation on what's actually happening, but it's all the same exact math. And most people learning diffusion actually get quite confused, because if you talk to some probabilistic graphical model people, they're saying, oh, this is a probabilistic graphical model, and what's actually, this is a hidden Markov model, and what we're doing is we're learning this like Markovian thing or whatever.

> 没错。是的。围绕扩散有一堆这样的旁支领域,它们对实际发生的事各有不同的解读,但底层数学完全相同。大多数学扩散的人其实相当困惑,因为如果你去找一些搞概率图模型的人,他们会说,哦,这是个概率图模型,实际上这是个隐马尔可夫模型,我们在做的是学习这种马尔可夫式的东西之类的。

[16:43] **SPEAKER_01:** It's like, okay, fine. But like, it's just noise minus data. And like, you should just show that first. And then like, if you think about it from like a physics perspective, and there's all this stat mech people that have that interpretation there's a whole bunch of different interpretations.

> 那就像,好吧,行。但它其实就是噪声减数据。你应该先把这个讲出来。然后,如果你从物理的角度去想,还有一堆搞统计力学的人持那种解读——总之有一大堆不同的解读。

[17:00] **SPEAKER_01:** I think it gets a little bit confusing. And the whole stochastic differential equation people like thinking about this as an SDE, and I think that's all fine. It probably is helpful to think about, but in terms of teaching it, it's actually quite, quite simple, which is powerful. Cool.

> 我觉得这就有点让人糊涂了。还有一整拨搞随机微分方程的人,喜欢把它当作 SDE 来思考,我觉得这些都挺好。这样想大概是有帮助的,但就教学而言,它其实相当、相当简单,而这正是它强大的地方。很好。

[17:15] **SPEAKER_01:** So, if we go back to here, you can see that this is literally predicting the velocity. Your goal is to have the model predict.

> 那么,如果我们回到这里,你可以看到这就是字面意义上在预测速度。你的目标是让模型去预测。

[17:22] **SPEAKER_00:** You're minimizing the loss between predictive velocity and velocity.

> 你是在最小化预测速度和真实速度之间的损失。

[17:24] **SPEAKER_01:** And the actual velocity. That's it. And that's super stable. And it's, it's really clean.

> 和真实速度。就是这样。而这非常稳定。它真的很干净利落。

[17:30] **SPEAKER_01:** And then at test time for the physics people, this is like a Euler step kind of thing that you're doing where you call the model a bunch of times. And you iteratively refine. So, back to the hill climb that we were talking about. I'll grab some random noise here, x.

> 然后在测试时,对搞物理的人来说,这就像是你在做欧拉步(Euler step)之类的事,你调用模型很多次,并迭代地精修。所以回到我们之前说的爬山。我在这里抓一些随机噪声,x。

[17:50] **SPEAKER_01:** And I just do, and I call basically reverse that, that noising process. To de-noise, de-noise, de-noise, and.

> 然后我就做——我基本上是调用去逆转那个加噪过程。去噪、去噪、去噪,然后……

[17:58] **SPEAKER_00:** It's literally Euler's method. Like you're using the velocity to point in the direction you want to go.

> 这真的就是欧拉法。就是你用速度来指向你想去的方向。

[18:02] **SPEAKER_01:** Point in the direction and just keep going, keep going, keep going until you've done the number of steps. The one thing that I really don't like about diffusion as it's done today, is that I can't keep calling it beyond, if I only trained on 100 diffusion steps in my diffusion schedule, if I change that at test time, it doesn't work. And so, you can't like, oh, I want it even better. So, I'll call it even more. That doesn't, you can't.

> 指向那个方向,然后一直走、一直走、一直走,直到你走完了那个步数。关于如今扩散的做法,我真正不喜欢的一点是:我没法继续超额调用它——如果我在扩散调度里只训练了 100 个扩散步,那我在测试时改动它就不行。所以你不能说,哦,我想让它更好,那我就多调用几次。那样不行,你做不到。

[18:26] **SPEAKER_01:** I've tried it, it doesn't work.

> 我试过,不行。

[18:27] **SPEAKER_00:** Yeah, there's various tricks people try there, but yeah.

> 是的,人们在那儿会尝试各种技巧,不过嗯。

[18:29] **SPEAKER_01:** Yeah, and so like, there's games played that is actually quite exciting. All the expense.

> 是的,所以这里有一些玩法,其实相当令人兴奋。全部的开销。

[18:35] **SPEAKER_00:** But sorry, to be clear, here you're saying that's not relevant, right? It's not relevant. Because in this type of model, you don't have this time dependency.

> 不过抱歉,说清楚一点,你这里是说那不相关,对吧?不相关。因为在这类模型里,你没有这种时间依赖。

[18:41] **SPEAKER_01:** Well, so you do. So, at this time, if you change, for example, the number of steps, if you double it, let's say that, and you expect to get even higher resolution images, it actually will just turn into like white. Like it actually just like doesn't work at all. So, you can't step beyond that.

> 呃,其实你是有的。所以在这时候,如果你改变,比如说步数,如果你把它翻倍,并且期望得到分辨率更高的图像,它其实只会变成一片白。它根本就完全不工作。所以你不能越过那个界限继续步进。

[18:55] **SPEAKER_01:** You can't step beyond number of steps that was trained. That's an important detail. There are tricks that people are doing to try to compress that representation. So, like if at train time, I train for 100 steps, and at test time, I want to do 10 steps.

> 你不能超过训练时的步数继续步进。这是个重要的细节。人们在用一些技巧来试图压缩那个表示。比如说,如果训练时我训练了 100 步,而测试时我想做 10 步。

[19:10] **SPEAKER_01:** Then what you can do is you can do distillation into the model to try to have the 10-step model learn the 100-step models thing. But then you still got to train with 10 steps. And so, like if you're training with X steps, you have to be using X steps at test time. I see. Interesting.

> 那你能做的是,对模型做蒸馏,试图让 10 步的模型学到 100 步模型的那套东西。但那你仍然得用 10 步来训练。所以,如果你用 X 步训练,你在测试时就必须用 X 步。我明白了。有意思。

[19:25] **SPEAKER_00:** Yeah. So, you talked about this concept of a squint test. Why don't you define the squint test for a second? Tell me a little about where this comes from.

> 是的。你之前谈到过一个"眯眼测试"(squint test)的概念。不如你花点时间给它下个定义?跟我讲讲它是从哪儿来的。

[19:31] **SPEAKER_00:** And then I'd be curious to hear how you think about diffusion models in the context of general intelligence broadly.

> 然后我很好奇,想听听你在广义通用智能的语境下是怎么看待扩散模型的。

[19:36] **SPEAKER_01:** Yann LeCun has this like interesting lecture where he talks about our discovery of flight and that we didn't need flapping wings. We kept trying to mimic a bat and how that was a waste of time. And to that, I say you're 100% right. However, we did need two wings.

> Yann LeCun 有一场很有意思的演讲,他讲到我们对飞行的发现,说我们并不需要扑动的翅膀。我们一直试图模仿蝙蝠,而那是浪费时间。对此我说,你百分之百正确。然而,我们确实需要两只翅膀。

[19:53] **SPEAKER_01:** And you look at the Wright Brothers original plane and you squint and you look at a bird. You're just like, hmm, while we have helicopters and we have jets and things like that and rockets, like we got there eventually. And so, there's many elements in the set of things that can achieve flight and they have different pros and cons. And there are many elements in the set of things that can achieve intelligence.

> 你看看莱特兄弟最初的飞机,眯起眼睛,再看看一只鸟,你就会觉得,嗯……虽然我们后来有了直升机、有了喷气机之类的东西、有了火箭,但我们最终是到达了。所以,能实现飞行的那一"集合"里有很多元素,它们各有利弊。而能实现智能的那个集合里,也有很多元素。

[20:15] **SPEAKER_01:** We are the only existence proof of it at all. And like I'm sure there will be more elements in the set. And maybe LLMs, broadly speaking, can get there. But if I squint and I look at LLM setup, which I see this monolithic stack transformers, the same thing, stack, stack, stack.

> 我们是它唯一的存在性证明。我确信这个集合里将会有更多元素。而广义地说,大语言模型或许也能到达那里。但如果我眯起眼睛去看大语言模型的架构,我看到的是这种单一整体式的堆叠——Transformer,同样的东西,堆、堆、堆。

[20:33] **SPEAKER_01:** And there's three stages of training. We do this pre-train, SFT, post-train, and then no learning at all beyond that. And it produces exactly one token at a time. Right, so an iterative token.

> 而且训练有三个阶段。我们做预训练、SFT(监督微调)、后训练,之后就完全没有学习了。而它一次恰好只产生一个 token。对,就是逐个迭代地产出 token。

[20:46] **SPEAKER_01:** Iterative token at a time. And it never goes backwards. And then you look at a brain, massive amounts of recursion. You have one learning procedure the whole time.

> 一次一个 token 地迭代。而且它从不往回走。然后你看看大脑,有海量的递归。你自始至终只有一套学习机制。

[20:55] **SPEAKER_01:** You have these two lobes with a corpus callosum between them that's going back and forth like this. And we think. And then I definitely don't think in one token at a time. When I write code, I don't write one little character at a time.

> 你有这两个脑半球,中间隔着胼胝体,信息像这样来来回回。然后我们思考。而我思考时绝对不是一次一个 token。我写代码时,不是一次写一个小小的字符。

[21:05] **SPEAKER_01:** I never go backwards. And I'm going backwards. I'm recursively improving. I'm going backwards again and again.

> ……(不是)从不回头。我是在往回走,我在递归地改进,我一次又一次地往回走。

[21:12] **SPEAKER_01:** I'm thinking in concepts.

> 我是在用概念来思考。

[21:13] **SPEAKER_00:** There's this dynamic process that's emitting concepts and then higher level concepts and then lower level manifestations of them.

> 有这样一个动态过程,它先产出概念,再产出更高层次的概念,然后是它们更低层次的具体表现。

[21:19] **SPEAKER_01:** And I'm sure that may be happening inside the LLM, but it's almost like, it's almost like stuck. It can't do more than in one step, even though it might want to. Right. Because it has to.

> 我确信这在大语言模型内部也许正在发生,但它几乎像是……几乎像是被卡住了。即便它可能想做,它也没法超出一步去做更多。对。因为它不得不这样。

[21:29] **SPEAKER_01:** That's the way that we trained it.

> 因为我们就是那样训练它的。

[21:31] **SPEAKER_00:** Right, like it might have all that in the LLM, but then it's sort of bottlenecked ultimately. It's action space. It's action space is one.

> 对,就是说它在大语言模型内部也许具备这一切,但最终它有点被瓶颈卡住了。它的动作空间。它的动作空间是一。

[21:37] **SPEAKER_01:** Is one token at a time. And so I think that that's where I think about diffusion. There's like two main things that diffusion gives me. It doesn't get me all the way to pass my squint test, but it gives me two things that for sure the brain is doing.

> 是一次一个 token。所以我觉得,这正是我想到扩散的地方。扩散给了我两样主要的东西。它没能让我完全通过我的眯眼测试,但它给了我两样大脑肯定在做的事。

[21:48] **SPEAKER_01:** Number one, all of biology and nature is randomness. Randomness is good. And what is diffusion doing? It's leveraging randomness.

> 第一,所有的生物学和大自然都是随机性。随机性是好东西。而扩散在做什么?它在利用随机性。

[21:57] **SPEAKER_01:** If you give me data, I noise it up, and from that I can learn about the data. And like, can the brain add noise to input data? Absolutely. Like absolutely.

> 如果你给我数据,我把它加上噪声,然后从中我就能学到关于这些数据的东西。那大脑能对输入的数据加噪声吗?绝对可以。绝对可以。

[22:08] **SPEAKER_01:** Like neurons are massively random. There's log normal distributions, spike patterns, and things like that. And the other one is this emission of one thing at a time versus thinking in concepts and then decoding into a big chunk of text and thought and visioning of the previous thoughts and things like that. And so I think diffusion gives me both of those things for sure.

> 神经元是高度随机的。有对数正态分布、放电脉冲模式之类的东西。另一样是:相对于一次产出一个东西,而是先用概念思考、再解码成一大块文本和思想,并对先前的想法进行可视化之类的。所以我认为扩散确实给了我这两样东西。

[22:27] **SPEAKER_00:** People have probably heard of stable diffusion as a very common application of this. It's an image generation model that was pretty widely available for the last few years. What people may not be so aware of is all the other ways that diffusion is used in the last few years in products that people are widely using. So what are some of the areas in which diffusion is most widely accessible?

> 人们大概听说过 Stable Diffusion,把它当作这个技术非常常见的一个应用。它是一个图像生成模型,过去几年里相当普及。人们也许没那么清楚的是,过去几年扩散在大家广泛使用的产品里还有各种其他用法。那么,扩散最广泛可及的领域有哪些?

[22:47] **SPEAKER_01:** Yeah, it's really any mapping from very high dimensional P data to very high dimensional action spaces or P data that you may want to map to. And so I mean, yeah, of course everyone knows generating images because we've done mid-journey and things like that and even more modern versions of that with Sora and VO and Flux and SD3 now and things like that. And we've generating videos which is just images stapled together and video gen and image gen and things like that. However, there's so many more applications that now we're seeing.

> 是的,它其实适用于任何从非常高维的 p-data 到非常高维的动作空间、或你想映射过去的 p-data 的映射。当然,大家都知道生成图像,因为我们用过 Midjourney 之类的,还有更现代的版本,比如现在的 Sora、VO、Flux、SD3 之类的。我们还在生成视频,视频不过就是把图像拼接在一起,视频生成、图像生成之类的。然而,现在我们看到的应用远不止这些。

[23:19] **SPEAKER_01:** That's the most exciting part in my view of all the new applications. And so whether or not you're now creating sentences, I mean, diffusion LLMs was one of the biggest topics that we saw in EurIPS, whether it's continuous diffusion LLMs or discrete diffusion LLMs. It's writing code now. It's creating proteins.

> 在我看来,所有这些新应用才是最激动人心的部分。所以,不管是现在用它来生成句子——我是说,扩散大语言模型是我们在 NeurIPS 上看到的最热门话题之一,无论是连续扩散的大语言模型还是离散扩散的大语言模型。它现在在写代码。它在创造蛋白质。

[23:39] **SPEAKER_01:** I mean, DeepMind has won the Nobel Prize for that. There is robotic policies, this diffusion policy thing, which I think might actually be one of the biggest uses of it and will result in like robotics. It's actually working. It was the robot actually working.

> 我是说,DeepMind 因此拿了诺贝尔奖。还有机器人策略,就是这个 diffusion policy,我觉得它其实可能是扩散最大的用途之一,并且会催生出机器人技术。它真的能用了。那机器人真的动起来、能用了。

[23:54] **SPEAKER_01:** There's weather forecasting for the GenCast. It's the most accurate weather forecasting system in the world. It's really anything. And even like I mentioned, Harrison working on the diffs diffusion for failure sampling, just like sampling for failures and like bad things that could happen.

> 还有 GenCast 用于天气预报。它是世界上最准确的天气预报系统。它真的什么都能干。甚至像我提到的,Harrison 在研究用扩散做故障采样,就是对故障、对可能发生的坏情况进行采样。

[24:10] **SPEAKER_01:** We can do that as well.

> 我们也能做那个。

[24:11] **SPEAKER_00:** So a lot of the products where we see people actually using AI, especially for things other than just text-based chat, a lot of them are using diffusion, especially our images, videos, increasingly now things like code and the life sciences. So yeah, pretty wide berth of things. Yeah.

> 所以,在我们看到人们实际使用 AI 的很多产品里,尤其是那些不只是基于文本聊天的用途,很多都在使用扩散,特别是图像、视频,以及现在越来越多的代码和生命科学之类的东西。所以是的,涵盖面相当广。是的。

[24:26] **SPEAKER_01:** In fact, I would say the only two holdouts right now where state-of-the-art is not diffusion, diffusion has eaten all of AI except two. AR LLMs still are outperforming and gameplay and things like AlphaGo. And so MCTS is still state-of-the-art for those types of things. And so we haven't seen diffusion really take a step in those two areas, but more research is needed.

> 事实上,我要说,目前只有两个坚守的阵地——最先进的技术还不是扩散;扩散已经吞并了除这两者之外的整个 AI。自回归的大语言模型仍然表现更优,还有游戏博弈以及像 AlphaGo 这类的东西。所以对那类任务,MCTS(蒙特卡洛树搜索)仍然是最先进的。我们还没看到扩散在这两个领域真正迈出一步,但还需要更多研究。

[24:48] **SPEAKER_00:** So to bring the conversation to a head now, how should people think about this research area, either as researchers contributing to the field or as founders looking to build a new product?

> 那么,把这场对话推向一个总结,人们应该如何看待这个研究领域——无论是作为为该领域做贡献的研究者,还是作为想要打造新产品的创业者?

[24:58] **SPEAKER_01:** Yeah. I mean, I would think about maybe this falls in two camps. If you're training models yourself or if you're using models and not in the business of training models. If you're in the business of training models, I would seriously look at diffusion.

> 是的。我觉得这大概可以分成两个阵营。要么你自己在训练模型,要么你在使用模型、而不从事训练模型这门生意。如果你从事的是训练模型这门生意,我会认真地去研究扩散。

[25:12] **SPEAKER_01:** I don't care what your application is. You should be looking at this procedure, even if it's just to get a latent space that you can then train off of. And so there's no application in machine learning that I don't think you should be heavily looking at diffusion procedures as a fundamental piece of your training loop. In the case of people who are not training models, I would just update your prior on how good these things are getting.

> 我不在乎你的应用是什么。你都应该研究这个流程,哪怕只是为了得到一个你随后可以据以训练的隐空间。所以在机器学习里,我想不出有哪个应用你不该把扩散流程当作训练循环的一个基础组成部分来重点考察。至于那些不训练模型的人,我会说,更新一下你对这些东西正在变得多好的先验判断。

[25:40] **SPEAKER_01:** And if you just look at in the last five years on how good image generation got from mid-journey when we first came out to VO and Sora and Flux and SD3 now, it's like a thousand times better, right? The answer was just scale it up. And that takes time and that takes money and all those things and data. And now you apply that to proteins.

> 如果你只看过去五年,图像生成从 Midjourney 刚问世,到现在的 VO、Sora、Flux 和 SD3,变好了多少——大概好了一千倍,对吧?答案就是把它规模化放大。而那需要时间、需要钱、需要那一切以及数据。现在你把这套用到蛋白质上。

[26:00] **SPEAKER_01:** You apply that to DNA. You apply that to robotics policies, self-driving car. I mean, skate to where the puck's going to go. All these things are going to work.

> 你把它用到 DNA 上。你把它用到机器人策略、自动驾驶汽车上。我是说,滑向冰球将要去的地方(要有前瞻性)。所有这些东西都会奏效。

[26:09] **SPEAKER_01:** And we're watching it happen. It may cost money and time and those kinds of things. But those are solvable things. Those are tractable problems that we can go solve.

> 而我们正在亲眼看着它发生。它也许要花钱、花时间之类的。但那些都是可以解决的问题。那些是我们能够去解决的、可处理的问题。

[26:19] **SPEAKER_01:** And also the core procedure of diffusion is getting better. That's another major factor. A lot simpler. A lot simpler.

> 而且扩散的核心流程本身也在变好。那是另一个重要因素。简单得多。简单得多。

[26:25] **SPEAKER_01:** And it's getting like it's just working better. And so skate to where the puck's going to go. Bet that rows of the robot will work in people's homes. Bet that the protein folding is only going to get better and now we're going to apply that to DNA and all these other metabolomics and things like that.

> 而且它就是在变得更好用。所以要滑向冰球将要去的地方。押注机器人会在人们家里工作。押注蛋白质折叠只会越来越好,而现在我们要把它用到 DNA 以及所有这些代谢组学之类的东西上。

[26:39] **SPEAKER_00:** We see founders develop new models for robotics or for text generation or for video using diffusion. And we see founders who are using all of these methods coming from other places build companies on top of them. And it seems like there's this whole new wave of companies that can be built on either end of this now. Right. I think it's going to redefine the entire economy.

> 我们看到创业者用扩散为机器人、文本生成或视频开发新模型。我们也看到创业者从别处借用所有这些方法,在其之上构建公司。看起来现在这一头或那一头都可以催生出一整波全新的公司。对。我认为它将会重新定义整个经济。

[26:56] **SPEAKER_00:** Thanks so much for joining us. We're going to keep digging in on topics related to machine learning research like diffusion. Can't wait to see you at the next one.

> 非常感谢你的参与。我们会继续深入探讨像扩散这样与机器学习研究相关的话题。期待在下一期见到你。
