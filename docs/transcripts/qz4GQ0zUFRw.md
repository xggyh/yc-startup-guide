# 全文转录 · 人脑真正独有、AI 正拼命追赶的那个东西:世界模型

> ▶ [YouTube](https://www.youtube.com/watch?v=qz4GQ0zUFRw) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/qz4GQ0zUFRw.md) &nbsp;·&nbsp; The Key Thing Human Brains Have That AI Is Trying To Learn

> 中英对照 · 每段英文原文下附中文翻译

`[00:00]` **SPEAKER_01:** One of the biggest open problems in AI right now is how to solve sample efficiency. That is, how do you get models to quickly learn new tasks or skills from relatively small amounts of training data?

> 目前 AI 领域最大的未解难题之一,就是如何解决样本效率问题。也就是说,如何让模型能够从相对少量的训练数据中快速学会新任务或新技能?

`[00:08]` **SPEAKER_02:** Humans do this incredibly well. We can learn new games, concepts, and skills, often after just a handful of tries. Our best models, on the other hand, often need tens of thousands of data points just

> 人类在这方面做得非常出色。我们往往只需尝试几次,就能学会新游戏、新概念和新技能。而我们最好的模型,却常常需要数以万计的数据点才能

`[00:18]` **SPEAKER_01:** to learn. So today we're going to discuss what many top researchers believe is the most promising path to closing that gap, world models.

> 学会。所以今天我们要讨论的,是许多顶尖研究者认为最有希望弥合这一差距的路径——世界模型。

`[00:24]` **SPEAKER_02:** We're going to discuss the motivation and math behind world models, current applications, and why this approach might be the key to unlocking AGI.

> 我们将讨论世界模型背后的动机和数学原理、当前的应用,以及为什么这种方法可能是开启通用人工智能(AGI)的关键。

`[00:39]` **SPEAKER_01:** You and I have talked a lot about the various ways people are training models and the sample efficiency of them. Why don't we start by just defining sample efficiency and how we intuitively think about it as humans?

> 你我已经聊过很多人们训练模型的不同方式以及它们的样本效率。我们不如先从定义样本效率开始,谈谈作为人类我们是如何直观地理解它的?

`[00:49]` **SPEAKER_02:** Yeah. So I think from my perspective, the two major problems that we have left to solve is intelligence per watt and intelligence per sample. Intelligence per watt is like how many valve perplexity points we get per watt of spend. And then intelligence per sample is basically...

> 好的。在我看来,我们还剩下两大问题要解决:每瓦智能和每样本智能。每瓦智能指的是我们每花费一瓦能量能获得多少困惑度(perplexity)的降幅。而每样本智能基本上就是……

`[01:05]` **SPEAKER_02:** If I have one addition... If I have one additional sample in my data set, how much more intelligent am I getting? And so if I imagine I have a new task, like RKGI, for example, I think really, François Chollet has been on the forefront of this thinking and talking about intelligence as a rate of skill acquisition versus skill acquisition. And that's very different.

> 如果我的数据集里多了一个样本,我能变得更聪明多少?所以设想我面对一个新任务,比如说 ARC-AGI,我认为 François Chollet 一直走在这一思考的最前沿,他把智能理解为"技能获取的速率",而不是"已获取的技能本身"。这两者是截然不同的。

`[01:24]` **SPEAKER_02:** And so how fast do we get smarter with more and more samples? And these things are incredibly poor at getting smarter with fewer and fewer samples.

> 也就是说,随着样本越来越多,我们变聪明的速度有多快?而这些模型在"用越来越少的样本变聪明"这方面表现得极其糟糕。

`[01:33]` **SPEAKER_01:** And for context, the RKGI test... Yeah. The RKGI test sets are a really good example of cases where humans are intuitively very good at them. Most humans can intuitively solve those puzzles with some amount of thinking and effort.

> 补充一下背景,ARC-AGI 测试……是的,ARC-AGI 测试集是一个很好的例子,人类凭直觉就非常擅长解这类题。大多数人只要稍加思考和努力,就能凭直觉解出那些谜题。

`[01:45]` **SPEAKER_01:** But our current state-of-the-art AI systems, what people consider frontier intelligence, basically can't do them. Right.

> 但我们当前最先进的 AI 系统,也就是大家认为的前沿智能,却基本上做不到。是的。

`[01:52]` **SPEAKER_02:** I mean, we come into new problems with such inductive bias from K through 12, like all these math in school that we've had, that these models are kind of getting from the entire... Yeah. The entire internet. And so when we come in, we're not coming in tabula rasa, just bare bones, but even so that they have...

> 我是说,我们在面对新问题时,带着从幼儿园到高中积累的巨大归纳偏置,比如学校里学过的所有数学,而这些模型某种程度上是从整个……对,整个互联网上获取这些的。所以当我们上场时,并不是白板一块、一无所有;但即便如此,它们已经拥有了……

`[02:11]` **SPEAKER_02:** I don't know what percent of the internet you've read. I've read very little percent of the internet. But despite that, and having read the entire internet, it still can't really do well in generalizing to these new tasks.

> 我不知道你读过互联网的百分之几。我读过的比例非常小。但尽管如此——而它读遍了整个互联网——它在泛化到这些新任务上仍然做得不太好。

`[02:22]` **SPEAKER_01:** So now let's think about this in the extreme cases. In the extreme case where let's say we were perfectly sample efficient, we were as sample efficient as possible. What would that mean in terms of a... A model that is taking a set of actions in the world?

> 那我们从极端情况来思考。设想在极端情况下,我们达到了完美的样本效率,尽可能高的样本效率。这对于一个在世界中采取一系列行动的模型来说,意味着什么?

`[02:37]` **SPEAKER_02:** Well, I guess the perfect sample efficiency would be zero samples. And there are examples of this, and that sounds absurd to say, and the hypothetical I'll give on this is imagine I had a perfect world model, then I should never go to the environment to go and collect samples to train on. And well, that can't possibly happen. No, it actually can happen.

> 嗯,我想完美的样本效率应该是零样本。这方面确实有例子,虽然这么说听起来很荒谬。我给出的假设是:设想我拥有一个完美的世界模型,那我就完全不需要跑到环境里去收集样本来训练。你可能会说,这不可能发生。不,其实它真的可以发生。

`[03:02]` **SPEAKER_02:** We do it all the time. It's called Newton's second law of motion. It's like Newton mechanics. We basically know how to get an object from point A to point B with a rocket quite easily

> 我们一直在这么做,这叫牛顿第二运动定律,也就是牛顿力学。我们基本上知道如何轻松地用火箭把一个物体从 A 点送到 B 点,

`[03:12]` **SPEAKER_01:** just by following Newton's laws of motion. Yeah. When NASA plans to intercept an asteroid and is planning it years in advance and can set it off in a trajectory where it just glides to the right thing and intersects to the right point, that is an example of a perfect world model we've built where we're then just letting that world model act. And that system does not need to intelligently...

> 只要遵循牛顿运动定律就行。是的。当 NASA 计划拦截一颗小行星,提前数年做规划,并能让它沿着一条轨迹出发,滑行到正确的目标、在正确的点交会,这就是我们构建的完美世界模型的一个例子,之后我们只需让这个世界模型去运作。而这个系统并不需要智能地……

`[03:32]` **SPEAKER_01:** Yeah. It can intelligently collect new samples from the environment to decide which direction to go next. It's already been pre-programmed and it can perfectly do it.

> 是的,它不需要智能地从环境中收集新样本来决定下一步往哪个方向走。它已经被预先编程好了,可以完美地完成任务。

`[03:39]` **SPEAKER_02:** Yeah. Can you imagine if we needed to collect 1 million training examples of us shooting spaceships to the moon to know how to do it? Right. We definitely wouldn't have the Apollo missions, right?

> 是啊。你能想象吗,如果我们需要收集 100 万个把飞船发射到月球的训练样本才能学会怎么做?那我们肯定就不会有阿波罗计划了,对吧?

`[03:52]` **SPEAKER_02:** But we do have that ability because the real world is differentiable and we can do something called model predictive control that we're going to talk about in a little bit. But even in our own brain... I was just thinking about this on the drive up, but there's so many ways that I can basically think about the things that you are going to say or what a VC is going to say when I was pitching them or what a customer might say, and even product, having taste. What is taste?

> 但我们确实具备这种能力,因为真实世界是可微分的,我们可以做一种叫"模型预测控制"的事情,稍后我们会讲到。但即便是在我们自己的大脑里……我刚开车过来时还在想这个问题:我有太多方式可以去预判你要说什么,或者我向风投推介时他们会说什么,或者一个客户可能会说什么,甚至在做产品时的"品味"。什么是品味?

`[04:19]` **SPEAKER_02:** It's like predicting that other people are going to like this thing. And so we've built this world model over years of entrepreneurship, 10 years of like getting it wrong, right? That maybe Bill Gates, Steve Jobs, and Jensen... Yeah.

> 品味就像是在预测别人会喜欢这个东西。所以我们通过多年的创业、十年不断试错,建立起了这样一个世界模型,对吧?也许像 Bill Gates、Steve Jobs 和黄仁勋……是的。

`[04:31]` **SPEAKER_02:** Yeah. ...couldn't have 50 years of world modeling experience to know what people want. And basically, this is actually proven in the 1967 COGSI study by Richardson, that basically showed that if you take a cohort of three groups of people and you have one go practice layups in basketball, and they go and they shoot, they improve...

> 是的……有着长达五十年的世界建模经验,才知道人们想要什么。而且基本上,这在 Richardson 1967 年的一项认知科学研究中得到了证实:如果你取三组人作为一个队列,让其中一组去练习篮球上篮,他们投篮练习,水平会提高……

`[04:56]` **SPEAKER_02:** For one hour, they've improved by... I think it was like 24% or something like that. And then if you take the other one... they just blindfold them and they imagine laying up a basketball they improve it 23 interesting against the control i mean that's insane it means that we have this crazy good world model and there's this neuroscientist at stanford named shaw drachman who basically is of the view that the entire point of the growing neocortex for the during the great cortical expansion 10 million years ago was to get better and better and better and better world modeling and having just like my little vla which we'll define of doing the next predicting next action is not as good as having a world model to lean on either for training for training purposes or for test time adaptation yeah what it fundamentally comes down

> 练习一小时,他们提高了……我记得大概是 24% 左右。然后再取另一组……只是把他们蒙上眼睛,让他们在脑海里想象上篮,结果他们提高了 23%,很有意思,这是相对于对照组而言的。我是说这太疯狂了,这意味着我们拥有一个好得离谱的世界模型。斯坦福有位神经科学家叫 Shaul Druckmann,他基本上认为:一千万年前那次"大脑皮层大扩张"中不断增大的新皮层,其全部意义就在于让世界建模变得越来越好、越来越好。仅仅拥有一个像我说的小 VLA(我们稍后会定义,即预测下一个动作),远不如有一个世界模型可以依靠——无论是用于训练目的,还是用于测试时适应。是的,归根结底,

`[05:41]` **SPEAKER_01:** to is you know we as humans we think about our intuitive ability to think as coming from some implicit world model we have in our heads encoded by genetics and our ability to learn and whatever else it seems like models can do surprisingly intelligent things despite not having an explicit world model when it comes to natural language when they're just talking it seems like you know maybe under the hood deep inside the weight somewhere there's some kind of implicit understanding of the world but there isn't an explicit representation of that but it seems like in certain domains especially in robotics and self-driving as we'll talk about that sort of breaks down and um you know maybe it would be helpful now to just think a little bit about and sort of define some of the pieces of what makes it challenging in these different domains and then we can use that to kind of build up to why it's particularly hard in things like robotics to get these types of predictive models to work yeah let's do it so let's actually like

> 就在于:作为人类,我们认为自己那种直觉式的思考能力来自脑中某个隐式的世界模型,它由基因编码,加上我们的学习能力等等。似乎模型在自然语言方面能做出令人惊讶的智能行为,尽管它们并没有显式的世界模型——当它们只是在说话时,似乎在其内部、在权重深处的某个地方,存在着某种对世界的隐式理解,但并没有对此的显式表示。然而在某些领域,尤其是我们接下来要谈的机器人和自动驾驶,这种方式就有点行不通了。嗯,或许现在我们不妨稍微思考一下,并定义一些要素,看看是什么让这些不同领域变得如此有挑战性,然后我们可以以此为基础,逐步说明为什么在机器人这类领域中,让这类预测模型奏效尤其困难。好,那就开始吧,我们实际上不如……

`[06:35]` **SPEAKER_02:** take a step back and just talk about like control reinforcement learning and define some define some common terms so typically in um we teach a course called decision making under uncertainty which is like the main reinforcement learning course at stanford i like to show a specific example of let's say i have some drone and this is my poor little drone here and it has some mass m and we have some uh some sort of uh like gravity g is pulling down on it and it's currently at position uh t with velocity t which we will collectively call the state and to be really clear this is going to be p x p y p z t t t and v x v y z v z it's like the six-dimensional state vector yep and we have uh some thrust vector u and we're trying to get to some point p star and v star which is v star is typically zero and so you have some platform that i want this thing that's drawn to land on this is this control problem right and so uh let's say this is like and we'll go through optical or optimal optimal optimal control so how would i actually solve this so the first thing i need to know is my transition function and so this is my state transition function which is st plus one given the previous given st and my action which which i control is ut and so this is my state transition or dynamics function or a world model this is a world model this is like a very fundamental for

> 退一步,先来聊聊控制和强化学习,并定义一些常用术语。通常在——我们教一门叫"不确定性下的决策"的课程,这算是斯坦福主要的强化学习课程——我喜欢举一个具体的例子:假设我有一架无人机,这是我可怜的小无人机,它有一定质量 m,还有重力 g 向下拉着它。它当前处于位置 (在时刻 t),速度也在时刻 t,我们统称为"状态"。说清楚一点,这个状态是 pₓ、p_y、p_z 和 vₓ、v_y、v_z,是个六维状态向量。对。我们有一个推力向量 u,我们想到达某个点 p*、v*,其中 v* 通常为零。所以有一个平台,我想让画的这个东西降落在上面,这就是一个控制问题,对吧。那么假设这是——我们来走一遍最优控制。我到底该怎么解这个问题?首先我需要知道我的转移函数,也就是我的状态转移函数:给定前一状态 sₜ 和我控制的动作 uₜ,得到 sₜ₊₁。这就是我的状态转移函数,或者叫动力学函数,或者叫世界模型。这就是一个世界模型,它是非常基础的,

`[08:17]` **SPEAKER_01:** for context you know this this equivalent to the transition function you would think about in rl in

> 补充背景一下,这等价于你在强化学习中会想到的那个转移函数,

`[08:21]` **SPEAKER_02:** general exactly and so uh and then what i'm trying to learn is something called a policy which is like what ut should i uh uh emit given some st yep and so this is the ultimate question what should i do what action should i take given some state st and so uh the way that we'll solve this and luckily we have a world model that is perfect it's called newtonian physics newtonian physics this is like newton's second law of motion which is f equals ma and so we know that the position p t plus one is going to equal p t plus uh delta t vt plus one half delta t squared so everyone's taking high school high school physics and the same thing for the velocity and then my acceleration is the sum of some of the for some of the forces uh which is going to be my uh ut i think i divide by the mass and g and so that's it and now i have my transition function now how do i get to a policy and i'm going to apply something called model predictive control or real-time model predictive control which is like the way that spacex lands the rocket on uh on some platform in the ocean and what you're going to do is you're going to set up your loss function you're going to minimize sum over all t you have ut to infinity and i'm going to minimize my p star minus pt plus v star minus vt and usually you add this little lambda ut which is like how much energy you're exerting and you can't have infinite thrust so you typically will have to say ut u max thrust yeah that can be achieved and so this is easily solvable with comics optimization and so this is convex this is convex this is convex the sum of convex functions is convex this constraint and so i dcp discipline convex programming means that i can put this into cvx pi and it will just give me out my policy which will be the solution will be the optimal

> ——一般意义上的,没错。而我想要学的东西叫"策略",也就是:给定某个状态 sₜ,我应该发出什么样的 uₜ。对。所以这就是终极问题:给定某个状态 sₜ,我该做什么、该采取什么动作。我们求解的方式——幸运的是,我们有一个完美的世界模型,叫牛顿物理学。牛顿物理学,也就是牛顿第二运动定律,F = ma。于是我们知道,位置 pₜ₊₁ 等于 pₜ 加上 Δt·vₜ 加上 ½Δt²(乘以加速度)——这都是高中物理——速度也是同理。而我的加速度是各作用力之和,也就是我的 uₜ 除以质量,再加上 g,就这样。现在我有了转移函数。那我怎么得到策略呢?我要应用一种叫"模型预测控制"(或实时模型预测控制)的方法,这就是 SpaceX 让火箭降落在海上某个平台上的方式。你要做的是设定损失函数:对所有从 uₜ 到无穷的时间步求和进行最小化,我要最小化 (p* − pₜ) 加上 (v* − vₜ)。通常你还会加上一个小小的 λuₜ 项,表示你消耗了多少能量;你不可能有无限推力,所以通常必须约束 uₜ ≤ u_max(可实现的最大推力)。于是这就可以用凸优化轻松求解。这是凸的,是凸的,凸函数之和是凸的,这个约束也是凸的。所以通过 DCP(规范化凸规划)我可以把它丢进 CVXPY,它就会直接给我输出策略,而这个解将是最优的

`[10:47]` **SPEAKER_01:** ut plus one all the way to infinity so we can solve this in closed form basically we can because we have this world model of newtonian physics we can say at every step exactly how this drone should fly so that it lands on the appropriate thing exactly under a set of constraints

> uₜ₊₁ 一直到无穷。所以我们基本上可以用闭式解求出来。我们之所以能做到,是因为我们有牛顿物理学这个世界模型,可以在每一步精确地说出这架无人机应该怎么飞,以便在一组约束条件下精确降落在合适的位置上。

`[11:03]` **SPEAKER_02:** Exactly. You'll run your log barrier, interior point, whatever, to some solver on this, and it will give me my optimal, and this would be literally the optimal path that this thing can take to get to this state. And that will minimize, and I can increase this if I want it to do the least energy path, and I make that zero if I want it to be the fastest. And so that's typically the way that you would do what I would call deterministic differentiable control.

> 没错。你会用对数障碍法、内点法之类的求解器来跑,它会给出最优解,而这将是这个东西为到达该状态所能采取的字面意义上的最优路径。这会做最小化;如果我想让它走最省能量的路径,我可以调大那一项;如果我想让它最快,我就把那一项设为零。所以这通常就是我所说的"确定性可微控制"的做法。

`[11:38]` **SPEAKER_02:** And why differentiable? Because I can form the Lagrangian by taking this minus this constraint and take the gradient of it, and I can do monorobins.

> 为什么是可微的?因为我可以通过把目标减去约束来构造拉格朗日函数,再对它求梯度,然后就能做优化(如牛顿法/梯度下降)。

`[11:50]` **SPEAKER_01:** You use the fact that it's differentiable to do the optimization. Exactly.

> 你利用它可微这一事实来做优化。没错。

`[11:54]` **SPEAKER_02:** If this is non-differentiable, you cannot do convex optimization, and you cannot do SGD. Even if it's non-convex, you could still solve and get a pretty good solution, as we do in deep learning, but if it's non-differentiable, you kind of can't. There's nothing you can do.

> 如果它是不可微的,你就没法做凸优化,也没法做随机梯度下降(SGD)。即便它是非凸的,你仍然可以求解并得到相当不错的解,就像我们在深度学习中做的那样;但如果它是不可微的,你基本上就无能为力了,什么办法都没有。

`[12:08]` **SPEAKER_01:** So, yeah, let's have an example then of how you could make this non-differentiable. Like, well, what's a scenario, I guess, even in like this drone scenario where it now becomes non-differentiable.

> 那好,我们举个例子,说说怎样会让它变得不可微。比如说,在这个无人机的场景里,什么情况下它会变得不可微?

`[12:16]` **SPEAKER_02:** Yeah. So I'll put this adversary named Ankit. Okay. And your job is to, you have another drone, let's say, Ankit's drone is to try to hit me and stop me from getting there.

> 好。我放进一个对手,叫 Ankit。好。你的任务是——你有另一架无人机,比如说 Ankit 的无人机,任务是撞我、阻止我到达目标。

`[12:28]` **SPEAKER_01:** Now, from the position of your drone, you don't know what actions I'm going to take. Right.

> 现在,从你这架无人机的角度看,你并不知道我会采取什么动作。对。

`[12:32]` **SPEAKER_02:** And so now, let's just call this the, this would be now, we're definitely not deterministic, we're stochastic, and stochastic and non-differentiable. And in this case, my state transition, what is ST plus one? It's going to be my, say, I'm in now, my thrust, and what Ankit's going to do. Right.

> 那么现在,我们就把它称作——现在我们肯定不是确定性的了,而是随机的,既随机又不可微。在这种情况下,我的状态转移——sₜ₊₁ 是什么?它取决于我现在所处的状态、我的推力,以及 Ankit 将要做什么。对。

`[13:00]` **SPEAKER_02:** And these, it was all differentiable until this new variable. Yeah. And I can't like back prop through your brain to say what you're going to do with your little drone controller. Right.

> 在引入这个新变量之前,这一切都是可微的。是的。我没法通过反向传播穿透你的大脑,来推断你会用你的小无人机控制器做什么。对。

`[13:09]` **SPEAKER_02:** It's completely non-differentiable now. And I'm resorting and I have to resort to this awful area called reinforcement learning, which is just super brutal and it's sprawling and there's so many different things. And you'll hear things like when you study initial reinforcement learning called value iteration or policy iteration. And there's DQN or deep Q-learning or just Q-learning, there's actor-critic, there's all this bag of stuff.

> 现在它完全不可微了。于是我不得不求助于一个可怕的领域,叫强化学习,它极其残酷、庞杂,有太多五花八门的东西。当你初学强化学习时,会听到诸如价值迭代、策略迭代之类的概念;还有 DQN、深度 Q 学习或普通 Q 学习、演员-评论家(actor-critic),一大堆这样的东西。

`[13:40]` **SPEAKER_01:** And all of this stuff ultimately comes down to ways to estimate, to model this non-differentiable stochastic process. Exactly.

> 而所有这些东西归根结底,都是用来估计、建模这个不可微随机过程的方法。没错。

`[13:50]` **SPEAKER_02:** Yeah. And so that's basically the main thing is you're going to start talking about this as a model where I'm going to introduce this psi to say that this is going to be stochastic. This is going to be some model that's going to take in these things and then output this and that we're going to train it over many, many instantiations of this. And that's to get a better and better world model.

> 是的。所以核心大致就是:你会开始把它当作一个模型来讨论,我会引入一个 ψ,表示这将是随机的。这会是一个模型,接收这些输入,然后输出结果,我们要在非常非常多次的实例上训练它。目的就是得到一个越来越好的世界模型。

`[14:10]` **SPEAKER_02:** And then I need to train some policy, A-T-S-T. And then typically you also need a value function. Yeah. And that is the value of some state.

> 然后我需要训练某个策略,即给定 sₜ 输出 aₜ。此外通常你还需要一个价值函数。对。它表示某个状态的价值。

`[14:21]` **SPEAKER_02:** And to discern between the value of different states. And in this case, I don't know what a valid state is. But let's just say I was doing... SpaceX with launching rockets and landing rockets in Florida.

> 用来区分不同状态的价值高低。在这个例子里,我不清楚什么算是有效状态,但假设我在做……SpaceX 那样在佛罗里达发射和回收火箭的事。

`[14:35]` **SPEAKER_02:** Let's just say that there's different... If I have my launch pad here and I have a whole bunch of houses here, let's just say the path going from here to here, I may think that doing this and then coming across here and burning all these houses alive may be not highly valued. So I might say, as an example, they typically call this some kind of a cone. And I might say it's low value to be here and it's very high value to be in this cone or something.

> 比如说有不同的……如果我的发射台在这里,而这边有一大片房子,假设从这里到那里的路径——我可能会认为这样飞、然后横穿过来把这些房子统统烧掉,应该不算高价值。所以举个例子,他们通常把这称作某种"锥形"区域。我可能会说:处在这个位置价值很低,而处在这个锥形区域内价值就非常高,诸如此类。

`[15:07]` **SPEAKER_01:** In a sense, the value gives you some expectation of future rewards, like the sum of future rewards you're getting. And so if you're in a bad space, you would set the value to zero or negative infinity or something like that.

> 某种意义上,价值给了你对未来奖励的某种期望,也就是你将获得的未来奖励之和。所以如果你处在一个糟糕的区域,你会把价值设为零、负无穷之类的。

`[15:18]` **SPEAKER_02:** Yeah, so we should introduce R-T as well. And so typically, if you're playing Go or chess, winning the game, you can say winning the game is plus one, minus one for losing, draw zero. That's what's done in AlphaGo. In chess, we have these heuristics, like a pawn is worth one point, a rook is worth five, et cetera, et cetera.

> 对,那我们也应该引入 Rₜ(奖励)。通常,如果你在下围棋或国际象棋,赢棋可以记作 +1,输棋 −1,和棋 0。AlphaGo 就是这么做的。在国际象棋里,我们有一些启发式规则,比如一个兵值 1 分,一个车值 5 分,等等。

`[15:39]` **SPEAKER_02:** So you can already have reward is the difference in board state. And then this, yes, will be the sum of my discount. I should just do T of R-T. Yeah.

> 所以你已经可以把奖励定义为棋盘局面的差值。而价值就是我折扣奖励之和,也就是对 t 求和的折扣 Rₜ。对。

`[15:56]` **SPEAKER_02:** And it's important also to use this nomenclature. The pie. And the reason why that's important is because what's actually happening here is this is the discounted reward following policy pie. And that means that when I'm in this state, I will take this action, and then I'll end up in this to SC plus one, and then I'll take this action, and it's taking it greedy.

> 使用这套记号也很重要,即 π(策略)。之所以重要,是因为这里实际发生的是:这是"遵循策略 π"的折扣奖励。意思是当我处在这个状态时,我会采取这个动作,然后到达 sₜ₊₁,再采取下一个动作,而且是以贪婪的方式来选取。

`[16:19]` **SPEAKER_02:** And so that's the value with respect to pie.

> 所以这就是相对于策略 π 的价值。

`[16:20]` **SPEAKER_01:** And so ultimately, what it comes down to is we are trying to still find a new policy pie. And along the way, we will use the learning models in various capacities. This is standard RL to estimate the value function given the rewards we're receiving. And then where world models come in is a way of incorporating all of those into some sort of joint modeling of the state and action distribution so that we can make more intelligent policies off of it.

> 所以归根结底,我们要做的仍然是寻找一个新的策略 π。在此过程中,我们会以各种方式使用学习到的模型。这就是标准的强化学习:根据我们获得的奖励来估计价值函数。而世界模型的用武之地在于:它是一种把所有这些整合进某种对状态和动作分布的联合建模的方法,从而让我们能基于它制定更智能的策略。

`[16:48]` **SPEAKER_02:** And so your standard kind of setup for this is what I'm always trying to get to at the end of the day is some joint distribution, which would be SC plus one, given where I'm at now. And then this factorizes with chain rule, simply to my pie, my policy, AT given ST, and my world model. This is usually represented with theta. And this is my world model, which would be ST plus one, given ST and AT.

> 所以这方面的标准设定是——我最终一直想得到的是某个联合分布,也就是给定我当前所处的位置,得到 sₜ₊₁。然后用链式法则,它可以简单地分解为:我的策略 π(给定 sₜ 得到 aₜ),以及我的世界模型(通常用 θ 表示),也就是给定 sₜ 和 aₜ 得到 sₜ₊₁。

`[17:25]` **SPEAKER_02:** And these are typically learned separately. And you can imagine, in fact, actually, you can actually learn this. This is a video generation model. And I have the frame ST, and I predict the next frame ST plus one.

> 而这两者通常是分开学习的。你可以想象——事实上你确实可以学出这个:这就是一个视频生成模型。我有当前帧 sₜ,我预测下一帧 sₜ₊₁。

`[17:39]` **SPEAKER_01:** And we'll get into this. For those of us who kind of saw our diffusion model series, often people these days use video diffusion for exactly this.

> 我们稍后会深入讲。对于看过我们扩散模型系列的人来说,如今大家常常正是用视频扩散来做这件事。

`[17:47]` **SPEAKER_02:** And then what you can do, and this is like the in vogue thing to do since Danijar and the Dreamer paper series from V1 to V4 is do action conditioning later, like similar to clip. Where we will inject this like input head, input tail to come into the model to influence and enable the world model to have embodiment. What does that mean? It means that not only can I predict like as a plant or tree growing on the side of the building, I can like see the world passing by, but I can actually influence it.

> 接下来你可以做的——这也是自 Danijar 和 Dreamer 系列论文(从 V1 到 V4)以来很流行的做法——就是稍后再做"动作条件化",有点类似 CLIP。我们会注入一个输入头/输入端,让它进入模型,去影响并赋予世界模型"具身性"。这是什么意思?意思是我不仅能像长在楼房侧面的一株植物或一棵树那样被动地看着世界从眼前流过、进行预测,我还能真正去影响它。

`[18:21]` **SPEAKER_02:** And I can change the world, and I can learn that with AT. And that's far fewer samples to do this post action conditioning. Right. I already have a really good ST to ST plus one world model.

> 我可以改变世界,并通过动作 aₜ 学会这一点。而做这种事后的动作条件化,所需的样本要少得多。对。因为我已经有了一个非常好的"从 sₜ 到 sₜ₊₁"的世界模型。

`[18:35]` **SPEAKER_01:** And so here you're saying, you know, what's also in vogue now is jointly training these versus separately training them. Exactly.

> 所以你的意思是,现在也很流行把这些联合训练,而不是分开训练。没错。

`[18:42]` **SPEAKER_02:** And so this is called, that is called a world action model where some of the issues here is one, there's all these training dynamics. If these things are just disparate training on different sets and things like that. The other issue is plainly obvious. What I have to do to actually do test time planning is I'll have to sample my.

> 这就叫"世界-动作模型"。这里存在一些问题:其一,有各种训练动力学问题——如果这些东西只是在不同的数据集上各自分开训练之类的。另一个问题也显而易见:要真正做测试时规划,我必须先采样我的……

`[19:01]` **SPEAKER_02:** With model one, invoke theta and then pass that sampled action into here and then roll it out to ST plus one and it's very expensive and it's a very not real time to major issues and why, like, why can't we just scale up alpha go to like solve all the problems is because it's because of this property. If I have one invocation to the model and it gives me both, here's the action I should take. And here's the ST plus one that'll end up much, much cheaper and much, much faster.

> 用第一个模型,调用 θ,然后把采样得到的动作传进来,再推演到 sₜ₊₁——这非常昂贵,而且非常不实时,两大问题。为什么我们不能直接把 AlphaGo 放大来解决所有问题?正是因为这个特性。如果我一次调用模型就同时得到"这是我应该采取的动作"和"这是随之而来的 sₜ₊₁",那就会便宜得多、快得多。

`[19:29]` **SPEAKER_01:** Okay. So I think that's. Really good segue. I think, why don't we now motivate everything we just described through a series of increasingly complex environments.

> 好的,我觉得这是个很好的过渡。我们不如现在通过一系列复杂度递增的环境,来为我们刚才描述的一切提供动机。

`[19:40]` **SPEAKER_01:** So I'll contend that I think the right set of environments for us to consider is chess followed by go, followed by self-driving followed by robotics.

> 我认为,我们应该考虑的一组恰当环境是:国际象棋,接着是围棋,然后是自动驾驶,最后是机器人。

`[19:48]` **SPEAKER_02:** Um, all right. So let's go through a couple examples of problems that we want to apply, uh, reinforcement learning to. So chess is, is a pretty easy one. There's an eight by eight grid.

> 嗯,好。那我们来过一遍几个我们想应用强化学习的问题例子。国际象棋是个相当简单的例子,棋盘是 8×8 的格子。

`[19:58]` **SPEAKER_02:** Um, and so typically when you, when you, uh. Approach any, uh, RL problem, you're going to look at, uh, star. And so this, this, the size of the state, uh, the number of states I can be in. So if I have these eight here and these eight, so this would be eight, 1632.

> 通常当你着手任何强化学习问题时,你会看 STAR(状态 S、转移 T、动作 A、奖励 R)。首先是状态的大小,也就是我可能处于的状态数量。如果这边有 8、那边有 8,就是 8、16、32……

`[20:17]` **SPEAKER_02:** So it'd be 32 to the 64. Yes. Quite large, quite large. Then, uh, my transition function is.

> 所以状态数量大约是 32 的 64 次方。对,相当大,相当大。然后,我的转移函数是……

`[20:26]` **SPEAKER_02:** Stochastic and non-differentiable. Cause you can, you don't know what the other player is going to do. Yeah. So if I'm like.

> 随机的、不可微的。因为你不知道对手会怎么走。是的。所以如果我……

`[20:31]` **SPEAKER_02:** In, uh, playing chess.com at my house, I move and then something happens and it comes back and, and then now you moved and the board has changed. So I can't really differentiate through what the other player, uh, is doing. The car line, my action space is actually quite small.

> 在家里玩 chess.com,我走一步,然后发生了些什么,轮回来时你已经走了,棋盘变了。所以我没法对对手的行为进行微分。而动作空间的基数其实相当小。

`[20:46]` **SPEAKER_02:** Um, even though there's 32, uh, uh, pieces and all that stuff that there's only eight possible moves in expectation that you can actually, that are legit moves.

> 尽管有 32 个棋子之类的,但期望上真正合法、你实际能走的着法大概只有 8 种左右。

`[20:55]` **SPEAKER_01:** So like in any, in any given state, there's only eight ish moves you could do.

> 也就是说,在任意给定的状态下,你大概只有 8 种左右的着法可选。

`[20:59]` **SPEAKER_02:** Let's just say in the beginning I can move all my pawns. I can move my horses. So that's tent. Yeah.

> 就说开局吧,我可以动所有的兵,可以动马,那大概也就十来种。对。

`[21:03]` **SPEAKER_02:** That's like not that much. So this is extremely small. And then my reward, we can use the heuristic based approach, or we can just say, you know, plus one, zero or minus one. If I lose plus one, if I win.

> 这没多少。所以动作空间极其小。至于奖励,我们可以用基于启发式的方法,或者干脆就用 +1、0、−1:输了 −1,赢了 +1。

`[21:14]` **SPEAKER_01:** And, uh, so this is very tractable. You say it's tractable, even though there's a really big state space here. Yeah. But why don't we talk about that for just a second?

> 所以这非常可解。你说它可解,尽管这里状态空间非常大。是的。但我们不如就此稍微聊一下?

`[21:22]` **SPEAKER_01:** I think this is a really important point. When you say it's tractable, you're specifically referring to the action space being small because it affects the kind of like color. This is the combinatorial expansion here. Should we talk about that for just a second?

> 我觉得这是一个很重要的点。当你说它可解时,你具体指的是动作空间很小,因为它影响到这里的……组合爆炸。我们要不要就这点稍微谈一下?

`[21:34]` **SPEAKER_01:** Yeah. Or maybe we can add go and then kind of contrast the two.

> 好。或者我们可以加入围棋,然后把两者对比一下。

`[21:37]` **SPEAKER_02:** Yeah. So why don't we do that? Because, um, it's because I want to get to the alpha go, uh, uh, the way that they solve this and you're right. So if I were to do this naively and I just took, um, and my ST plus one and I want to do look aheads.

> 好,那我们就这么做吧,因为我想讲到 AlphaGo 以及他们求解的方式。你说得对。如果我要天真地这么做,我取当前状态,考虑 sₜ₊₁,想做前瞻(look-ahead)。

`[21:50]` **SPEAKER_02:** Uh, what I would do is I would take all of the actions I can take. So there's eight. So I would do action one, action, two action, eight. Bop.

> 我会做的是:枚举所有我能采取的动作,一共 8 个。所以我会走动作一、动作二……一直到动作八。啪。

`[21:59]` **SPEAKER_02:** Bop. Bop. Bop. these i need to expand it for all possible states and so now i need to do cardinality s which we just said is this huge freaking number and so i have to do that eight times and i have to do it again i have to do it again so just doing looking forward one move is like quite intractable although

> 啪、啪、啪。对这些,我需要针对所有可能的状态展开,所以现在我要处理状态基数 |S|,我们刚说了那是个巨大得离谱的数字。我得这么做八次,然后再做一次,再做一次。所以哪怕只是往前看一步,都相当难以处理。不过,

`[22:19]` **SPEAKER_01:** at the same time you know the you everyone starts at the same starting position and while it is a really large space you know it there isn't an infinity number of potential there's actually a really really small number of game boards even four moves into the game right as opposed to a game where you could start in any permutation for example of initial game state and right what

> 与此同时,你知道,每个人都从同一个起始局面出发。虽然它是个非常大的空间,但潜在局面并不是无穷多。实际上,即便下到第四步,可能的棋盘局面数量其实非常非常少——这与那种可以从任意初始排列开始的游戏形成对比。对。

`[22:41]` **SPEAKER_02:** a few states down yeah so this is like definitely over uh um done because there's there's it's it's much much less than this in practice yes but just naively like looking at you know uh what possible game states could be in a game where you could start in any permutation you could start in any could be uh as a rough math here but this is roughly the idea and then each one of these leaves i need to invoke my value function right uh which is the value of that state t plus one and so i have to do that all many times and we'll get this off a go but like this ends up being estimating the leaf node uh because at the end of the day my policy atst i want to pick on the arg max of like the value of the the following action i guess it would be yeah a exactly yeah the arg max over a of the value of the state of the of the end state st plus n let's say it's like that's the the main goal here um and so for me to do that i need to roll all this out estimate the value and then pick the best one and so this this quickly grows um however and we'll see this about how we go which is actually actually has an even bigger state space um so i'm going to do that and then i'm going to do that so i think it's 19 by 19. um apparently i think it's spot right now so you have this 19 by 19 grid you can in each one it can be black white or or nothing there so i have three uh so let's do our star again so the cardinality of the state i think is going to be s uh two or three my ternary thing here to the 19th squared i think it's 361. yeah something like that 361. um my transition same issue i don't know if it's going to be the same issue i don't know if it's going to be the same issue i don't know uh my action space is going to be 361 let's say so it's a good amount

> 往下走几步就是了。所以这个数字肯定是高估了,因为实际中它比这少得多。是的。但天真地看,在一个可以从任意排列开始的游戏里,可能的局面数会是——这里只是粗略估算,但大致就是这个意思。然后对每一个叶子节点,我都需要调用我的价值函数,对吧,也就是那个 t+1 状态的价值。所以我得做很多很多次。我们讲 AlphaGo 时会看到,这最终归结为估计叶子节点的价值。因为归根结底,我的策略在状态 sₜ 下,想选取使后续价值最大的那个动作的 arg max——对,就是对动作 a 取 arg max,使得终局状态 sₜ₊ₙ 的价值最大,这就是这里的主要目标。要做到这点,我需要把这一切都推演出来、估计价值,然后挑最好的。这样很快就会膨胀。不过——我们讲围棋时会看到,它的状态空间其实更大。围棋是 19×19,好像现在是这样。你有一个 19×19 的格子,每个交叉点可以是黑、白或空,所以有三种。那我们再走一遍 STAR:状态的基数大约是 3(三元)的 361 次方(19 的平方是 361)。对,大概 361 这样。转移函数也是同样的问题。动作空间大约是 361,所以相当

`[24:31]` **SPEAKER_01:** bigger than chess much bigger but it's still not uh enormous yeah as we'll see in a second yeah

> 比国际象棋大,大很多,但仍然不算庞大到极致——我们马上会看到。是的。

`[24:38]` **SPEAKER_02:** and so basically what they do they call this z which is kind of annoying but let's call it r and it's the terminal it's the terminal when they won the game and they basically you know you have your trajectory which is um s zero a zero r zero um then all the way to the end of the game yep s n a n r n and if you won then all of these uh all the moves that black if black won all the moves that black did get plus all the moves that white did were minus one and they just that's how they create their um their rollouts rollout refers

> 所以他们基本上是这么做的:他们把这个叫作 z(有点烦,不过我们就叫它 r),它是终局奖励,是他们赢下这盘棋时的终局。基本上,你有一条轨迹:s₀、a₀、r₀,一直到棋局结束的 sₙ、aₙ、rₙ。如果你赢了——比如黑棋赢了,那么黑棋走的所有着法都得 +1,白棋走的所有着法都得 −1。他们就是这样生成"rollout(推演)"的。rollout 指的是

`[25:20]` **SPEAKER_01:** to a taking n steps of play of all players one after another yeah of moves under a specific policy at the at the particular instantiation of it

> 在某个特定策略(其某个具体实例化版本)下,让所有玩家一个接一个连走 n 步的过程。

`[25:32]` **SPEAKER_02:** right so let's just let's probably under this policy p theta t and we're gonna overload t but like this is that instantiation we froze that model we froze that model and we play i think it's like 70 games and we like treat all of those and we're going to sub sample a bunch of um of these uh state action results state action results to train our to update our policy in our um in our world model our transition model and what it's actually doing is we we take in an st we give it to some theta and it wants to output um the probability of st plus one being played which is our transition function and uh the uh value of the current state and how do we get the velocity and so the value of the current state uh well both of them are coming out of the model but basically the loss function l theta is going to equal and it's going to be really close to this control problem one is we have some v theta minus this z which we'll just call it r here um squared and then plus uh actually so it's minus this pi which i'll explain in a second log p theta and i think they everyone includes this but they include it in the paper so i'll include it there as well which is the um weight decay yep and so um so this is basically what uh our loss function is then we'll play a bunch of these games and let's try to be a little bit organized here and uh and so this is our setup this architecture and now the most once we train this thing we do an insane insanely expensive task of uh of test time planning and so this trend in rl is just called test time planning and the specific algorithm they use here for this is monte carlo research mcts and so this is one of the possible things that you could do uh it ends up working extremely well if you have small action spaces yeah so let's let's like very intuitively

> 对。就说在这个策略 p_θ 下(我们这里会重载 t 这个符号,但意思是那个实例化版本),我们冻结了那个模型,冻结了那个模型,然后下大约 70 盘棋,把所有这些棋局都拿来,从这些状态-动作结果中子采样一批,用来训练、更新我们的策略以及我们的世界模型(转移模型)。它实际做的是:我们输入一个 sₜ,把它交给某个 θ,它希望输出下一步 sₜ₊₁ 被走出的概率(这是我们的转移函数),以及当前状态的价值。这两者都从模型里出来。基本上,损失函数 L(θ) 等于——它非常接近前面那个控制问题:一项是 (V_θ − z)²(这里我们把 z 叫作 r),再加上——其实应该是减去这个 π——待会儿我解释——log p_θ,而且大家都会加上、论文里也加了,所以我这里也加上,那就是权重衰减项。所以这基本上就是我们的损失函数。然后我们下一大堆这样的棋,尽量把它组织得有条理些。这就是我们的架构设定。一旦我们训好这个东西,我们就要做一件极其昂贵的事情——测试时规划。强化学习里的这个趋势就叫测试时规划,他们这里用的具体算法是蒙特卡洛树搜索(MCTS)。这是你可以采用的方案之一,在动作空间较小时,它效果极好。那我们非常直观地

`[27:47]` **SPEAKER_01:** talk about what mcts does a lot of people have heard about monte carlo research because alpha goal was such a you know big moment yeah how exactly does that map into our star and value

> 聊聊 MCTS 到底做了什么。很多人听说过蒙特卡洛树搜索,因为 AlphaGo 是那么重大的一个时刻。是的。它究竟如何对应到我们的 STAR、价值

`[27:57]` **SPEAKER_02:** function and policy yep so i'll take this as t this will give me uh 361 uh uh numbers that sum to one and so i'll have some probability of uh of where these things are gonna go for the of where my my opponent will play um here so these are like the sets of actions yeah so i'm here so that i have all my st plus ones i'll have 361 of

> 函数和策略。好。我把这个作为输入,它会给我 361 个加起来等于 1 的数字,于是我得到一个概率分布,表示这些棋子会走向何处、我的对手会在哪里落子。这些就是各组动作。对。我在这里,所以我有所有的 sₜ₊₁,共有 361 个

`[28:23]` **SPEAKER_01:** these things um and then to be clear this is like action one action two all the way to action yeah

> 这样的东西。说清楚一点,这就是动作一、动作二,一直到动作 361。对。

`[28:30]` **SPEAKER_02:** exactly yeah and the um we have to estimate the value of each one of these and so then we have to invoke the model all 361 times to give me values for each one of these things and then i will select i'll select it based on the the ucb the upper confidence bound which is this equation that is roughly something like um balancing uh my value function of st plus one which they're gonna in the literature would be called the q value because it's actually the difference between a value function and q value is just that i have the action as well yep so it'd be st then at um so we'll just call that q value which is my um exploitation term and then my exploration term will be something like uh it's this funky square root of n uh so it's the arg max of a of my q and then i have this which is the probability of this this move being played which we have from here of of s let's just call it st plus one and then i have this term which is this sum over uh n s b divided by n sa and yeah what's what what's the intuition yeah this term so these ends is is the the v So this whole tree, I'm going to, so this tree could get really big, right?

> 没错。我们必须估计其中每一个的价值,所以要把模型调用全部 361 次,给我这些东西各自的价值。然后我会基于 UCB(置信上界)来选择,那是一个大致这样的方程:平衡我对 sₜ₊₁ 的价值函数——在文献里这叫 Q 值,因为价值函数和 Q 值的区别其实就在于 Q 值还带上了动作——所以是 (sₜ, aₜ),我们就叫它 Q 值,这是我的利用(exploitation)项;然后我的探索(exploration)项大致是那个古怪的根号 N 的表达式。所以是对动作 a 取 arg max,先是 Q,再加上这个这一步被走出的概率(我们从 s——就叫 sₜ₊₁ 这里得到),再加上这一项:对访问计数求和 N(s,b) 除以 N(s,a)。直觉是什么?对,这一项——这些 N 就是……那么整棵树,这棵树可能会变得非常大,对吧?

`[30:08]` **SPEAKER_01:** It's three 61 per thing, depth of 30. So you can't visit every single week though.

> 每一层是 361 个,深度是 30。所以你没法访问每一个节点。

`[30:14]` **SPEAKER_02:** Exactly. And so you want to keep track of which, uh, which state did you end up in? And what action did you take when you were in that state? And you want to make sure that you, you have good exploration, right?

> 没错。所以你要记录:你最终落到了哪个状态?你在那个状态下采取了什么动作?并且你要确保有良好的探索,对吧?

`[30:26]` **SPEAKER_02:** And so the way you keep track of the way you ensure that you have good exploration is you want to not just be greedy and always pick the highest value one, because that could be local, very myopic. And so what you'll do is during this MCT process, you'll start this dictionary, which will be all zeros of the visit count of being in this state and taking this action, and then once you go through your first rollout, you'll do, you'll go here. You'll all these things will be an edit to zero. You'll have some probability.

> 你确保良好探索的方式是:不要只顾贪婪、总是挑价值最高的那个,因为那可能是局部的、非常短视的。所以在 MCTS 过程中,你会初始化一个字典,记录"处于该状态并采取该动作"的访问计数,一开始全为零。当你走完第一次 rollout,你会来到这里,这些计数最初都是零,你会有某个概率。

`[30:56]` **SPEAKER_02:** What we're going to do is we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to bias it towards the higher probability of places to go. And then we'll go, we'll expand those trees. And then we will, um, update the counts that we visited this and that will basically reduce the amount of, uh, uh, probably that we're going to select it again, because this, this will reduce my, my exploration term. And if it's highly valued, then we're going to increase the Q on this.

> 我们要做的是:把选择偏向那些概率较高的落子位置。然后我们展开这些树,接着更新我们访问过这些节点的计数,这基本上会降低我们再次选中它的概率,因为这会减小我的探索项。而如果它价值很高,我们就会增大它的 Q 值。

`[31:25]` **SPEAKER_02:** Cause this is the expected value of going down this, this, this path.

> 因为这就是沿着这条路径走下去的期望价值。

`[31:29]` **SPEAKER_01:** So the gist of it is fundamentally. You want to take the optimal ish path, but have enough exploration in this really expensive, uh, step you're doing here so that you are making sure you're getting a decent chunk of the other potential leaf nodes you could traverse to right in these 30 step rollouts.

> 所以其要旨从根本上说是:你想走一条大致最优的路径,但又要在这个极其昂贵的步骤中保持足够的探索,以确保在这些 30 步的推演中,你能覆盖到相当一部分其他可能遍历到的叶子节点。

`[31:51]` **SPEAKER_02:** And so I'm going to do this, this MCTS simulation 800 times here. And then for all 800, I have to go through this whole process and I have to invoke them. The model, like at least 30 times to get through all of here. And so that's, you know, 27,800 times 30.

> 所以我要在这里做 800 次 MCTS 模拟。而这 800 次里的每一次,我都要走完整个过程,并且至少要调用模型 30 次才能把这里全部走完。所以那就是 800 乘以 30。

`[32:09]` **SPEAKER_01:** Yeah.

> 是的。

`[32:09]` **SPEAKER_02:** And so, uh, 24,000, uh, invocations of the model to, to develop this tree. And then once I have it per step, per step, just to do one action into the game. A lot of people don't understand that this is like, you don't like store this MCTS tree, you like you throw it away after, uh, you, you make the move. Um, but once it's very expensive to develop this MCTS tree.

> 所以是 2.4 万次模型调用,才能构建出这棵树。而且这是每一步都要做——每一步,只为在棋局里走出一个动作。很多人不理解这一点:你并不会保存这棵 MCTS 树,你走完这步之后就把它扔掉了。但构建这棵 MCTS 树的代价非常昂贵。

`[32:31]` **SPEAKER_02:** And once you have it, the probabilities of traversal are actually extremely useful for training. And then you end up biasing it and you train it with the MCTS tree, which is like a little bit, seems like circular motion or something like that. Like, uh, but you end up treating that as, as the pie that you'll train in your loss function. Um, so you, we have the R of, did we win or lose?

> 而一旦你有了它,遍历的概率其实对训练极其有用。于是你会用这棵 MCTS 树来对模型进行偏置并训练它,这看起来有点像循环往复。但你最终会把它当作损失函数里要训练的那个 π。所以我们有了 R——我们是赢了还是输了?

`[32:55]` **SPEAKER_02:** We have the pie of, of what was the end result of this whole expensive process. Um, and then at test time, we are going to do these 24,000 steps, every single, um, uh, every single move to pick the arg max, uh, that gives that, that satisfies both exploration and exploration and exploitation.

> 我们有了 π——这整个昂贵过程的最终结果。然后在测试时,我们对每一步、每一个着法都要做这 2.4 万步计算,来挑出那个同时满足探索和利用的 arg max。

`[33:18]` **SPEAKER_01:** In this case, you know, this still feels somewhat tractable though, because the action space is small enough where this like kind of works. Exactly. But now like, let's say hypothetically, maybe we can draw like an imaginary go, a game, a game of go where it's like, you know, let's, let's, let's say this game of go was like a thousand by a thousand. And so now you have a equals, uh, you know, more or less, uh, a million.

> 在这个例子里,这仍然感觉多少还算可解,因为动作空间足够小,这套方法勉强能行。没错。但现在假设一下——我们可以设想一个虚构的围棋,一盘围棋,比如说这盘棋是 1000×1000 的。那现在你的动作空间 A 差不多就等于一百万。

`[33:44]` **SPEAKER_01:** And now this, this tree, uh, we're drawing here that has to take here. This has cardinal or like, you know, with, I guess 1 million. Right. And there's like S zero through S 1 million.

> 而现在我们这里画的这棵树,每一步都要展开一百万个分支,对吧。而且有 s₀ 一直到 s(百万)。

`[34:00]` **SPEAKER_01:** And the number of, uh, you know, steps you would have to take here, presumably will have to be way more than 800 in order to get any reasonable, uh, kind of sampling of this. And so you're probably multiplying the test time cost of doing a rollout or of doing a next step prediction astronomically. If the game was even, let's say, you know, this is only a hundred X bigger than the current game, not even 50 X bigger than the current game. Everyone was very excited about alpha go.

> 而你在这里必须做的模拟步数,想必得远远超过 800,才能对它做出任何合理的采样。所以你做一次 rollout 或做一次下一步预测的测试时开销,很可能会以天文数字般的倍数增长。哪怕这个游戏只比现有游戏大一百倍、甚至还不到五十倍。当年大家都对 AlphaGo 非常兴奋。

`[34:29]` **SPEAKER_02:** And at the time in what was this? 2017, uh, 2016. Uh, everyone's very excited about this. And the important thing to pick up is that we did 800, uh, MCTS simulations and to cover 361 possible actions on average.

> 那时候是哪一年来着?2017、2016 年。大家都对此非常兴奋。要抓住的重点是:我们做了 800 次 MCTS 模拟,平均去覆盖 361 个可能的动作。

`[34:46]` **SPEAKER_02:** So that gives us about two samples, roughly on an expectation for every single action. So here you need like 2 million of them for a similar depth for, for a similar depth. And then that's still to do a depth of 30. I would still have to do this times 30.

> 所以期望上,每个动作大约能分到两次采样。那么在这里(百万级动作空间),要达到相似的采样密度,你需要大约 200 万次模拟。而且这还只是深度为 30 的情况,我仍然得把这个数乘以 30。

`[34:59]` **SPEAKER_02:** This would be 60 million, uh, invocations of the model. So that better be a small amount. Right. That's a lot.

> 那就是 6000 万次模型调用。所以那模型最好非常小才行。对,这数量太大了。

`[35:04]` **SPEAKER_02:** Um, so yeah, so that's to do a single action to be clear. Yeah, so exactly to do one action. So just imagine, uh, so why alpha go, uh, doesn't scale.

> 嗯,所以说清楚,这还只是为了走出一个动作。对,就是为了走一步。所以你就能想象为什么 AlphaGo 无法规模化。

`[35:15]` **SPEAKER_?:** Yeah.

> 是的。

`[35:16]` **SPEAKER_02:** To me, there's one, uh, the carnality of the action space must be extremely small. If it's big, sad, uh, to the, um, I need a perfect, uh, deterministic environment, right? Like this, this, this. This doesn't change.

> 在我看来:第一,动作空间的基数必须极其小,如果它很大,那就糟糕了。第二,我需要一个完美的、确定性的环境,对吧?就像这样——这不会改变。

`[35:37]` **SPEAKER_02:** The rules of this game don't change, but like the rules of the stock market change all the time. The rules to like venture change all the time. Like the real world changes quite often. So, uh, like, uh, homeless could ask this stick, uh, and real time.

> 这个游戏的规则不会变,但股市的规则一直在变,风险投资的规则一直在变,真实世界经常变化。所以,而且还要实时。

`[35:55]` **SPEAKER_02:** If you saw the movie, the documentary is such an amazing documentary. I'd highly recommend it to anyone that watches it. Um, the guy is sitting there for like 60 seconds, maybe five minutes waiting for the computer to like decide. And, and it's kind of like.

> 如果你看过那部电影——那部纪录片(《AlphaGo》)真是太精彩了,我强烈推荐给任何观看的人——那个人坐在那儿,大概 60 秒、也许 5 分钟,等着计算机做决定。这有点像……

`[36:09]` **SPEAKER_02:** Imagine that we were driving a car and like, you took like 60 seconds to like turn the steering wheel. Everyone's dead. Like the whole car is dead. And so like, you know, uh, now let's talk about, uh, robotics and self-driving car.

> 想象一下我们在开车,而你花了 60 秒才去转一下方向盘。那所有人都死了,整车人都完了。所以,现在我们来聊聊机器人和自动驾驶汽车。

`[36:23]` **SPEAKER_02:** Um, and why this, why that approach kind of can't scale.

> 以及为什么那种方法基本无法规模化。

`[36:26]` **SPEAKER_01:** Yeah. I think the really good contrast here, because intuitively, uh, I think in thinking through this exact star layout, it actually really changed how I think about the kind of problem space of both of these two. So like. And let's take self-driving car as an example.

> 是的。我觉得这里的对比非常好,因为凭直觉——在按这个 STAR 框架逐项思考的过程中,它其实大大改变了我对这两类问题空间的看法。那我们就以自动驾驶汽车为例。

`[36:41]` **SPEAKER_01:** This is one, you know, many people have started to experience for the first time, because we have some self-driving cars that actually work. You have Waymo and Tesla, FSD and whatnot that seem like they kind of work. So like, let's maybe apply your same star framing here. Um, I would contend that the state space of self-driving car is enormous and it's actually not intuitive to me whether it's more or less large than this one.

> 这是很多人最近才第一次亲身体验到的,因为我们已经有一些真正能用的自动驾驶汽车了。有 Waymo、特斯拉 FSD 之类的,看起来还挺管用。那我们把你那套 STAR 框架用在这里。我认为自动驾驶汽车的状态空间极其庞大,而且它到底比围棋的状态空间大还是小,对我来说其实并不直观。

`[37:04]` **SPEAKER_01:** Right. I mean, in a sense, the chess and AlphaGo state space is already like more than a number of atoms. In the universe or something to that effect. Right.

> 对。我是说,某种意义上,国际象棋和 AlphaGo 的状态空间已经超过了宇宙中的原子数量之类的了,对吧。

`[37:10]` **SPEAKER_01:** But like, just to emphasize that here, you know, you are considering, you know, surroundings, the vehicle state. Yep. Uh, like, you know, camera, like weather, weather. I guess the point is like road conditions.

> 但要强调一下,在这里你要考虑周围环境、车辆状态。对。还有摄像头、天气,路况等等。

`[37:28]` **SPEAKER_01:** It's like massive. This is massive. It is infinite. It's like, yeah.

> 它极其巨大。这非常巨大。它是无限的。对。

`[37:32]` **SPEAKER_01:** For all intents and purposes, it is infinite. Correct. Yeah.

> 就一切实际意义而言,它是无限的。没错。对。

`[37:34]` **SPEAKER_02:** Um, and, and so is the, uh, space of pixels. Like. Yeah. You know, like what can I put in an image?

> 而像素空间也是如此。对。你想想,我能往一张图像里放进什么?

`[37:41]` **SPEAKER_02:** I can take a picture, an image of anything. Yes, true. Um, and so we're able to handle it and the same thing here where we compress from the board state, we don't represent the board state. We compress it with a calm net.

> 我能拍下任何东西的照片、图像。是的,没错。而我们之所以能处理它,和这里是一样的:我们从棋盘局面进行压缩,我们并不直接表示原始棋盘局面,而是用卷积网络(convnet)把它压缩。

`[37:53]` **SPEAKER_02:** So they have some deep, some, some, some deep calm net that actually takes this state and converts it into a latent. Right. And that latent compression is sufficient to kind of like do pattern matching, do, do some type of like symmetric, symmetric, uh, uh, equal variance kind of things. And same thing with this and even better with JPA, which we can talk about at the end there, which is like basically taking some type of state space and doing all of our optimization in the latent space, which stable diffusion did, uh, that worked extremely well, which reduces our state space dramatically because I'm in some latent high dimensional space.

> 所以他们有一个很深的卷积网络,把这个状态转换成一个潜在表示(latent)。对。而那种潜在压缩就足以做模式匹配、做某种对称、等变(equivariance)之类的处理。这里也一样,用 JEPA 甚至更好——我们最后可以聊聊——它基本上就是取某种状态空间,把我们所有的优化都放在潜在空间里进行,这正是 Stable Diffusion 所做的,效果极好,它极大地缩小了我们的状态空间,因为我处在某个潜在的高维空间里。

`[38:27]` **SPEAKER_01:** So like the, the, the key thing there is that, yeah, despite this state space being effectively infinite, we've actually gotten really good at compressing this. Yeah. And we'll, we'll talk more about some of the tricks for how we actually do this in practice here. But the TLDR is, you know, where there's like 10 years of deep learning work that basically makes us extremely good at compressing that very fast.

> 所以那里的关键点是:尽管这个状态空间实际上是无限的,我们其实已经非常擅长压缩它了。是的。我们稍后会更多地聊聊我们在实践中具体是怎么做的一些技巧。但一句话总结:有大约十年的深度学习工作,基本上让我们变得极其擅长快速压缩它。

`[38:48]` **SPEAKER_01:** Exactly. Right. Exactly. T seems to have a similar problem as before.

> 完全正确。是的,没错。转移函数 T 似乎和之前有类似的问题。

`[38:51]` **SPEAKER_01:** Right. In fact, maybe even more extreme. There's like infinity other variables around you. Right.

> 对。事实上,也许更极端。你周围有近乎无限多的其他变量。对。

`[38:55]` **SPEAKER_02:** In some ways you'd think that it's, this is physics. Newton's laws, laws of motion should apply. If I turn the steering wheel like this and I hit the gas, I should be able to really easily model this. But what is non differentiable is that I have.

> 某种程度上你会觉得,这是物理学,牛顿定律、运动定律应该适用。如果我这样打方向盘、踩油门,我应该能很容易地对它建模。但不可微的地方在于……

`[39:09]` **SPEAKER_02:** If I'm going into a, a circle, right. It's like the most, the biggest issue that, that we, we faced in, when I was doing self-driving car is like, you were imposing your will onto maybe driving in India. I think you're imposing your will onto the environment and like people just kind of adapt naturally. Like if you were doing Newton's law of motion, you were gonna, gonna collide.

> 如果我要驶入一个环岛,对吧。这就是我做自动驾驶汽车时遇到的最大问题:你是在把自己的意志强加给环境——比如在印度开车,你把自己的意志强加给环境,而其他人会自然而然地做出适应。如果你只按牛顿运动定律来,你就会撞上去。

`[39:29]` **SPEAKER_02:** And so that the optimal policy, if you were doing strict Newtonians here would be like, don't move because anything you do, you're gonna crash, but it's not true like that. Then we wouldn't function. Like cars wouldn't go down the road. Um, and so you have to model the, the environment, you have to include other people in the environment and, uh, understand the embodiment of like how your action will change other people's actions.

> 所以如果你严格按牛顿力学来,最优策略就会是"别动",因为你做什么都会撞车。但事实并非如此,否则我们根本无法运转,车子也开不上路。所以你必须对环境建模,必须把环境中的其他人纳入考虑,并理解具身性——即你的动作会如何改变别人的动作。

`[39:51]` **SPEAKER_00:** YC's next batch is now taking applications, got a startup in you apply at ycombinator.com slash apply. It's never too early and filling out the app will level up your idea. Okay.

> YC 的下一批正在接受申请。如果你心中有一个创业想法,就到 ycombinator.com/apply 申请吧。任何时候申请都不算早,填写申请表本身就会让你的想法更上一层楼。好。

`[40:04]` **SPEAKER_00:** Back to the video.

> 回到视频。

`[40:05]` **SPEAKER_01:** Now let's talk about the action space. You know, like one way to look at the. Action space is that it seems relatively small. It seems like, well, you know, you turn the steering wheel left to right.

> 现在我们来谈谈动作空间。看待动作空间的一种方式是:它看起来相对较小。似乎就是,你把方向盘往左往右打。

`[40:14]` **SPEAKER_01:** You hit the break, you hit the, you hit the gas. Doesn't seem that big, but like how big is it actually? Like, how do we actually represent these action spaces when it comes to a realistic self-driving car scenario?

> 你踩刹车,你踩油门。看起来没那么大,但它实际到底有多大?在真实的自动驾驶场景里,我们究竟该怎么表示这些动作空间?

`[40:23]` **SPEAKER_02:** Yeah, I, I don't know how they, how they do this nowadays. Um, they, they're doing a whole bunch of like bird's eye view, different things like that.

> 是啊,我不太清楚他们现在是怎么做的。他们在搞一大堆鸟瞰图之类不同的东西。

`[40:30]` **SPEAKER_01:** That's considered even just like a very simplified case.

> 就算只考虑一个非常简化的情形也行。

`[40:32]` **SPEAKER_02:** But what, what do you have? You have a steering wheel that you can turn left, right. You have, uh, a brake pad. Yeah.

> 但你都有什么?你有一个可以左右打的方向盘,你有一个刹车踏板。对。

`[40:38]` **SPEAKER_02:** And you have the gas. Yeah.

> 你还有油门。对。

`[40:40]` **SPEAKER_01:** And so this thing is like 365 degrees. Yeah. So it's like a one to three 65, let's say zero to three 65. Yep.

> 所以这个方向盘大概是 365 度(注:应为 360 度)。对。就是从 1 到 365,或者说从 0 到 365。对。

`[40:49]` **SPEAKER_01:** And you, let's just say you break this up into 10 different, uh, uh, severities. You're already, uh, even with just this oversimplified model, your action space cardinality is 365,000. So that's like a hundred X bigger than alpha. It's in fact, it's about the size of the example.

> 假设你把它(刹车/油门)分成 10 个不同的力度等级。那么即便只用这个过度简化的模型,你的动作空间基数就已经是 365,000 了。这大概比 AlphaGo 大一百倍。事实上,它大约相当于我们举的那个例子的规模。

`[41:07]` **SPEAKER_01:** It's in fact a decent amount smaller than the size we said, which is brake and CTS.

> 事实上,它比我们说的那个规模还要小不少,涉及刹车之类的。

`[41:11]` **SPEAKER_02:** And so, yeah, so 36,000 action space is very large. And then even worse, unless you're Tesla, we have a bunch of video of people driving cars. We don't have video of like dash cams and like that. Like you actually don't have, again, only Tesla has this of the action as well.

> 所以是的,3.6 万的动作空间已经非常大了。更糟的是,除非你是特斯拉,我们只有一堆人开车的视频,却没有像行车记录仪那样的视频。你实际上没有——再说一遍,只有特斯拉同时拥有动作数据。

`[41:27]` **SPEAKER_02:** And so the things that you have access to that your trajectories are just like S T S T plus one S T plus two.

> 所以你能拿到的,你的轨迹只是 sₜ、sₜ₊₁、sₜ₊₂ 这样的状态序列。

`[41:34]` **SPEAKER_01:** So there's a, you're saying there's a decent number of these. That's. Yeah. Some like dash cam footage on YouTube or something, but not really that many either.

> 所以你是说这类数据有相当一部分。对。YouTube 上有一些行车记录仪的片段之类的,但其实也没那么多。

`[41:41]` **SPEAKER_01:** Yeah.

> 是的。

`[41:41]` **SPEAKER_02:** Relative. And so if you wanted to do a self-driving car and you didn't want to go spend a million dollars, trillion dollars on going, collecting all this data, then you want to leverage this data somehow. And this is going to be really applicable for, uh, robotics because we have a lot of, uh, videos of people doing things, right. Especially with egocentric.

> 相对而言。所以如果你想做自动驾驶汽车,又不想花上百万、上万亿美元去收集所有这些数据,那你就想设法利用这类数据。而这对机器人非常适用,因为我们有大量人们在做各种事情的视频,对吧,尤其是第一人称(egocentric)视角的。

`[41:59]` **SPEAKER_02:** Like we, we have those videos, but we, what we don't have is the actions they take.

> 我们有那些视频,但我们没有的是他们所采取的动作。

`[42:06]` **SPEAKER_01:** Yeah. Yeah. So this is like. This is, this is a sequence of what you're showing here, right?

> 对。对。所以这就是——这是你这里展示的一个序列,对吧?

`[42:12]` **SPEAKER_01:** Unless you're Tesla, unless you're Tesla and Tesla has this.

> 除非你是特斯拉,除非你是特斯拉——特斯拉才有这个(动作数据)。

`[42:14]` **SPEAKER_02:** So this is a huge competitive mode of like, what do people do in that state? And then so you can behavior clone to go from here to here, from here to here, go here to here, et cetera. But even then it's still very, very difficult. You have to, it's, it's not sufficient.

> 所以这构成了一条巨大的竞争护城河:人们在那个状态下会做什么?于是你可以做行为克隆(behavior cloning),从这里到这里、从这里到这里,等等。但即便如此,它仍然非常非常难。你必须——这还不够。

`[42:27]` **SPEAKER_02:** People think that like, okay, I have this, we have a self-driving car, right? I mean, the amount of work that they're doing at FSD is like incredible and it's, it's not generally available. Like you can't, you know, it's not Waymo level, um, yet.

> 人们以为,好,我有了这个,我们有自动驾驶汽车了,对吧?我是说,FSD 团队所做的工作量简直令人难以置信,而且它还没有普遍可用。它还没到 Waymo 那个水平。

`[42:38]` **SPEAKER_01:** Would this be a good moment to briefly talk about model-free versus model-based RL? Yeah. I think that's an important distinction. That's going to be relevant when we talk about more world models.

> 现在是不是个好时机,简要谈谈无模型(model-free)与有模型(model-based)强化学习的区别?是的。我觉得这是个重要的区分,当我们更多地讨论世界模型时会用得上。

`[42:47]` **SPEAKER_01:** Yeah.

> 好。

`[42:47]` **SPEAKER_02:** So this is a perfect point. Um, so model-free just means that my, my policy pie, uh, of a T given ST, uh, I have no world model involved. It's literally, it's literally doing what I said. I grab a bunch of these and I train go from S to a, S to a, just predict the next day.

> 这是个绝佳的切入点。无模型的意思就是:我的策略 π(给定 sₜ 得到 aₜ)完全不涉及世界模型。它字面上就是我刚才说的:我抓一堆数据,训练从状态 s 到动作 a、s 到 a,只预测下一个动作。

`[43:06]` **SPEAKER_02:** That's it. Yeah. And that's, and this is logical VLA. Yeah.

> 就这样。是的。而这就是逻辑上的 VLA(视觉-语言-动作模型)。对。

`[43:08]` **SPEAKER_02:** Um, you know, this is like giving us pretty good results, it's behavior cloning, it's all the, the, the, the stuff that, uh, it's not getting us to Rosie the robot just yet, but, um,

> 这已经给了我们相当不错的结果,它就是行为克隆,就是所有那些东西。它还没能让我们造出"Rosie 机器人"(《杰森一家》里的家务机器人),但是……

`[43:18]` **SPEAKER_01:** in many ways, it's the closest thing that just looks like the next token prediction from LLMs that seems to scale pretty well with natural language. I mean, it's like, it's not exactly the same thing, cuz there's no action exactly, but picking a token is not exactly the same thing, but it's very analogous to that basic thing.

> 在很多方面,它是最接近大语言模型那种"预测下一个 token"的东西,而那种方式在自然语言上似乎能很好地规模化。我是说,它并不完全是同一回事,因为(语言里)并没有真正的动作,选一个 token 也不完全等同,但它与那个基本机制非常类似。

`[43:32]` **SPEAKER_02:** I basically take away the tokenizer head and I give it an action space and I collect a bunch of tele ops data. You know, like this as, as the self-driving car does in Tesla, and I just taken the, the state, which is some image and, or maybe sequence of images, and then I'll output some action and that's it. Cool. And this is, let's say model three, cuz I don't have a model for the environment.

> 我基本上是把分词器头(tokenizer head)去掉,给它一个动作空间,再收集一堆遥操作(teleop)数据——就像特斯拉的自动驾驶汽车那样。我只是取状态(某张图像,或者一系列图像),然后输出某个动作,就这样。很好。我们就把这叫作"无模型"吧,因为我没有对环境的模型。

`[43:58]` **SPEAKER_02:** And then now if I do model based RL, I have not just some PI, but I have also my, uh, size as well here. Right. Yeah. And so, uh, by, uh, by including this, I can have a much stronger policy, but it would take a lot more time to perform inference because I have to do this full test time planning.

> 而现在如果我做有模型强化学习,我不仅有一个策略 π,这里还同时有我的转移模型。对。是的。所以通过纳入这个,我能得到一个强大得多的策略,但推理会花费多得多的时间,因为我必须做这整套测试时规划。

`[44:22]` **SPEAKER_01:** Just to remind us that size referring to this specific transition function, right? It's referring to this. You're saying this is specifically referring to, um, a function of ST plus one given ST and action T yes. So it's like your ability to predict the next state you'll be in.

> 提醒一下,你说的这个模型指的就是这个具体的转移函数,对吧?指的就是这个。你说的具体是指:给定 sₜ 和动作 aₜ 得到 sₜ₊₁ 的那个函数。对。所以它就是你预测下一个状态的能力。

`[44:41]` **SPEAKER_01:** Yep. Is, is the crux of it. Yep. As opposed to just directly predicting the actions.

> 对。这是核心。对。而不是直接预测动作。

`[44:45]` **SPEAKER_02:** Yeah. And the main thing that I believe is that this is required for AGI. This is what the, the human brain is, is at least in the way the human brain does it. Yeah.

> 是的。而我坚信的核心一点是:这对 AGI 来说是必需的。这正是人类大脑的运作方式——至少人类大脑是这么做的。对。

`[44:55]` **SPEAKER_02:** And, and let me go further in saying that, like, if you look at the, um, billions of years of evolution, basically there's this thing called 10 million, 10 million years ago called the great cortical expansion, which you see the size of a brain just explode, get bigger, bigger, bigger, exponentially up until us. And it basically stops. And if the entire point of the neocortex is world modeling, what happened is we started from VLAs. This would be like ants or fish.

> 我再进一步说,如果你看数十亿年的进化,大约一千万年前有一件事叫"大脑皮层大扩张",你会看到大脑体积急剧膨胀,越来越大、越来越大,呈指数增长,一直到我们人类。然后它基本就停止了。如果新皮层的全部意义在于世界建模,那么实际情况是:我们从 VLA 起步——那就好比蚂蚁或鱼。

`[45:22]` **SPEAKER_02:** Yeah. Right. Just like very, like, you know, lizard brain, whatever you want to call it. And then we developed this neocortex to like, you know, go from our, our motor cortex to actually simulate what's going to happen.

> 对。就是那种非常原始的"蜥蜴脑",随你怎么叫。然后我们进化出了新皮层,以便从运动皮层出发,去真正模拟接下来会发生什么。

`[45:33]` **SPEAKER_02:** And that makes us just so much smarter. And then we, once we get those samples, we can compress it when we sleep or otherwise. With this hippocampal shortwave ripple, whatever you want to call it. And then that helps us, uh, develop a better policy.

> 这让我们聪明得多。然后,一旦我们获得那些样本,就可以在睡眠或其他时候把它压缩下来——通过海马体的"短波涟漪"(sharp-wave ripple),随你怎么称呼。这帮助我们发展出更好的策略。

`[45:47]` **SPEAKER_02:** And that marriage between the two is, is not only helps us, um, train on hallucinated, uh, examples, but it also allows us to test time plan.

> 而这两者的结合,不仅帮助我们在"幻想出来的"样本上进行训练,还让我们能够进行测试时规划。

`[45:57]` **SPEAKER_?:** Right.

> 对。

`[45:58]` **SPEAKER_01:** I guess the, the kind of extreme case then of self-driving car is kind of general robotics, right? So if you're, if you're like a humanoid company, like figure or pie or whatever, again, same S T A R. Yeah. I guess the gist of it is that a is now even bigger, right?

> 我想,自动驾驶汽车的那种极端情形,大概就是通用机器人,对吧?如果你是一家做人形机器人的公司,比如 Figure 或 Physical Intelligence 之类的,同样是 STAR 框架。对。其要旨大概是:现在动作空间 A 更大了,对吧?

`[46:15]` **SPEAKER_01:** It is like, I guess a very simple robot would be, yeah. How would you, how would you play action space? Like, let's like, let's take a very basic one.

> 我想一个非常简单的机器人会是——对,你会怎么设定它的动作空间?我们就拿一个非常基础的例子来说。

`[46:21]` **SPEAKER_02:** If I take like my six axis, uh, arm as your standard here that we're actually working on right now in Stanford robotics center, um, you have two degrees of freedom, two degrees of freedom, two degrees of freedom. Uh, and then you have another two for the end effector, right? And so that's a simple end effector, not even like a, not even like a one axis, like, yeah. You know, we, you can rotate, but you have the, the, the, the one axis Yumi style, uh, thing.

> 如果我拿一个六轴机械臂作为标准——就是我们现在在斯坦福机器人中心正在做的那种——你有两个自由度、两个自由度、两个自由度,然后末端执行器还有另外两个,对吧?那是个简单的末端执行器,甚至不是单轴的那种。你可以旋转,但你有那种单轴、Yumi 风格的东西。

`[46:46]` **SPEAKER_02:** So this is eight. So you have 16 degrees of freedom. And let's just say that you do the suit three 65, two by 10 or whatever, you know, kind of thing. I mean, it's like 10 to the 16th.

> 所以这就是八(自由度)。那么(两条臂)你就有 16 个自由度。假设你按 360 度、每个再分 10 档之类的来算,那大概就是 10 的 16 次方。

`[46:56]` **SPEAKER_02:** It's like insane. It's like, yeah, it's an insane number. Um, and so much bigger than self-driving car, um, and even worse, like getting tele ops data is extremely painful and expensive. It's not just like, oh, we'll just get some people.

> 简直疯狂。对,这是个疯狂的数字。比自动驾驶汽车大太多了。更糟的是,获取遥操作数据极其痛苦且昂贵。可不是"哦,我们随便找些人"就行的。

`[47:10]` **SPEAKER_02:** The Philippines will give them like some, you know, things or whatever is like totally, totally doesn't work.

> 找菲律宾的人给他们一些设备之类的——那完全、完全行不通。

`[47:15]` **SPEAKER_01:** And nor is there yet something like, uh, Tesla's fleet where there are cars deployed that people are just using. And they're not even necessarily realizing that every time they turn the steering wheel, they're providing this, this data set for Tesla.

> 而且也还没有像特斯拉车队那样的东西——那些部署在外、人们日常使用的汽车。人们甚至没意识到,他们每次转动方向盘,都在为特斯拉贡献这份数据集。

`[47:29]` **SPEAKER_02:** And then even worse, you have this like what's called cross embodiment gap. And so if I were to like train this policy on Tesla model X. And I were to like, put up. On a Tesla model three, it wouldn't work.

> 更糟糕的是,还有所谓的"跨具身差异"(cross-embodiment gap)。如果我在特斯拉 Model X 上训练这个策略,然后把它装到特斯拉 Model 3 上,它就不管用了。

`[47:43]` **SPEAKER_02:** No, like it totally wouldn't work. Like all the, so much, so much of this, uh, the, the way that if, if I were to break on a model three versus a model X, the model X weighs more, it has different dynamics, aerodynamics, and things like that. And so what's actually gonna happen is very different. Like the, the degradation you have across cross or across embodiments is very, very, very strong.

> 是的,它完全不管用。这里面很多东西——如果我在 Model 3 上刹车和在 Model X 上刹车,Model X 更重,有不同的动力学、空气动力学之类的。所以实际发生的情况非常不同。跨具身之间的性能退化非常非常非常严重。

`[48:04]` **SPEAKER_01:** And clearly Tesla's figured various ways to get around that. I mean, they, they have these that roll up, but actually even with Tesla's new FSD today. They don't roll out in all the cars at the same time, probably for more or less that reason. And in this case, it's even harder now.

> 显然特斯拉已经想出了各种办法来绕过这个问题。他们有各种手段。但其实即便是今天特斯拉最新的 FSD,他们也不会同时向所有车型推送,多半就是出于这个原因。而在(机器人)这种情况下,现在就更难了。

`[48:15]` **SPEAKER_01:** I mean, you have bigger differences between embodiments than a model three versus Y and you have way bigger action spaces. You have to sum up model. Yeah.

> 我是说,机器人各具身之间的差异比 Model 3 和 Model Y 之间要大得多,而且你的动作空间也大得多。你不得不……(把这些都综合建模)。对。

`[48:23]` **SPEAKER_02:** Uh, Lane McIntosh, I played hockey with at, at Stanford, uh, who now runs Tesla FSD. Um, I can ask him, but I would bet money that they shard the data per model per, uh, car type. Yeah. Wouldn't be surprised.

> Lane McIntosh,我在斯坦福和他一起打过曲棍球,他现在负责特斯拉 FSD。我可以问问他,但我敢打赌,他们是按车型、按每一种车对数据进行分片(sharding)的。对。我一点也不会意外。

`[48:36]` **SPEAKER_02:** I, I just, cause that's what I would do. There's no way that like, you know, I, I would try. Trust, you know, data that was collected on a model X on a model three, I just wouldn't, no way I would trust it.

> 我这么说是因为我自己就会这么做。我绝不会——我绝不会去信任那些在 Model X 上采集、却用于 Model 3 的数据,绝不可能,我根本不会信任它。

`[48:46]` **SPEAKER_01:** Okay. So now that we understand the basic setup here and why the action space problem is so big, why don't we talk a little bit about how world models actually fit into this? You know, maybe first, you know, I guess what didn't work about the naive world models and how do we fix those? And then let's kind of talk about some of the newest world modeling techniques.

> 好。既然我们已经理解了这里的基本设定,以及为什么动作空间问题如此之大,我们不如聊聊世界模型究竟如何嵌入其中?或许先说说朴素的世界模型有哪些行不通之处,我们又是如何修正它们的?然后再谈谈一些最新的世界建模技术。

`[49:01]` **SPEAKER_01:** Cool.

> 好。

`[49:02]` **SPEAKER_02:** So like in robotics in particular, it's very hard to get these, this kind of trajectories that you want, that you kind of need to train for your VLA is, and people. Spend up, you know, uh, with a whole bunch of tele ops data. It's very expensive, very expensive. Ideally, what we would do is take like data like this from someone who is just like puts a camera on them and just like making sushi.

> 尤其在机器人领域,你很难获取想要的那类轨迹——那是训练 VLA 所需要的。人们要花很多钱去搞一大堆遥操作数据,非常昂贵、非常昂贵。理想情况下,我们想做的是:利用这样一类数据,比如某人身上戴一个摄像头,就那样在做寿司。

`[49:22]` **SPEAKER_02:** Okay. Like I want to make a sushi robot. Um, how do I do it? Give it to all the sushi chefs.

> 好比说我想造一个做寿司的机器人。我该怎么做?把摄像头给所有的寿司厨师戴上。

`[49:27]` **SPEAKER_01:** Don't put anything in their hands and just have them start cutting up sushi and making sushi. And ideally we would train it in that way. You were describing of like, somehow we would train a model just on these two and then later add this afterwards.

> 别在他们手里放任何设备,就让他们开始切鱼、做寿司。理想情况下我们会用那种方式来训练——就是你之前描述的:设法只用状态和转移这两者来训练一个模型,之后再把动作加进去。

`[49:38]` **SPEAKER_02:** And so the first real person. That, um, you know, went after this was Juergen Smidhuber, uh, please, uh, so, so he doesn't yell at us. We have to, we have to make sure we cite him. Uh, but he has this really cool paper called world models, uh, very aptly named.

> 而第一个真正去做这件事的人是 Jürgen Schmidhuber。拜托,为了不让他冲我们发火,我们一定得把他引用上。他有一篇非常酷的论文,就叫《World Models(世界模型)》,名字起得恰如其分。

`[49:53]` **SPEAKER_02:** And it's basically, he took these like, um, open AI gym, classic, uh, games, car racing, and I think doom as well. And then just like trained a model at that time was like an RNN. Um, he had some funky, uh, uh, zero order stuff in there. Um, he had some funky, uh, zero order stuff in there.

> 基本上,他拿来了 OpenAI Gym 里那些经典游戏,赛车游戏,我记得还有《毁灭战士(Doom)》。然后训练了一个模型,当时那还是个 RNN。他里面用了一些古怪的零阶(zero-order)方法。

`[50:10]` **SPEAKER_02:** But basically the key premise was I can take an environment. I can extract a whole bunch of this type of data off of it. I think he actually does actually this data, but we'll get into dreamer where he does it in this paper in this way. And then, uh, trains a policy on only the, uh, the, the synthetic data, the imaginative, uh, rollouts, and it actually performs well in the environment.

> 但核心前提是:我可以拿一个环境,从中提取一大堆这类数据。我想他实际上用的是真实数据,不过我们讲 Dreamer 时会看到他在那篇论文里就是以这种方式来做的。然后,只用合成数据、即"想象出来的"推演,来训练一个策略,而它在真实环境中的表现居然很好。

`[50:36]` **SPEAKER_02:** This is the first time in my understanding that that actually happened. And it actually works really well.

> 据我理解,这是第一次真正实现这一点,而且效果确实非常好。

`[50:41]` **SPEAKER_01:** And then, so the key thing there, you can basically use this. If you have some predictive model of this, in that case, and eventually of this, you can use that as basically a synthetic training set to train your policy model and then basically fine tune it on real data later. Exactly.

> 那么这里的关键在于:你基本上可以利用它。如果你有一个对状态转移的预测模型,以及最终对动作的模型,你就可以把它当作一个合成训练集来训练你的策略模型,之后再在真实数据上做微调。没错。

`[50:55]` **SPEAKER_02:** And which is just like a really powerful idea, especially since in robotics, the limiting step is access to large amounts of state action data. And so now the dreamer series. So basically this published publishes in. May of 2018.

> 这真是个非常强大的想法,尤其在机器人领域,瓶颈就在于能否获得大量的状态-动作数据。那么现在来说 Dreamer 系列。这篇(世界模型论文)大约发表于 2018 年 5 月。

`[51:10]` **SPEAKER_02:** Yeah. Uh, Dan is jar, uh, Hafner publishes dreamer one, I think in November of 2018, and then now he's been on this rampage for the last seven years, publishing these papers and dreamer V4, I think is the capstone of it, um, where he basically does the same thing and he focuses on Minecraft, um, and he trains these, a world, a world model on this type of data and then injects action conditioning on a very small amount of data. Yeah. Yeah.

> 对。Danijar Hafner 大约在 2018 年 11 月发表了 Dreamer V1,此后七年他就一路高歌猛进,不断发表这些论文,而 Dreamer V4 我认为是集大成之作。他基本上做的是同样的事,专注于《我的世界(Minecraft)》。他在这类数据上训练一个世界模型,然后只用很少量的数据注入动作条件化。对,对。

`[51:40]` **SPEAKER_02:** To get to this type of world model that can, that has the action conditioning as well, and then samples a lot from it. And then trains a policy on those synthetic, uh, imaginative rollouts. And it's the policy is so good that it's the first paper to mine diamonds in Minecraft. I'm not a big Minecraft player, but apparently that's extremely difficult.

> 从而得到这样一种同样具备动作条件化的世界模型,然后从中大量采样,再在那些合成的、想象出来的推演上训练一个策略。这个策略好到——它是第一篇能在《我的世界》里挖到钻石的论文。我不太玩《我的世界》,但据说那极其困难。

`[52:01]` **SPEAKER_02:** That's like next level difficulty. And it did it all on synthetic data, which is kind of crazy.

> 那是更高一个级别的难度。而它完全是在合成数据上做到的,这挺疯狂的。

`[52:05]` **SPEAKER_01:** And the key unlock there. Yeah. Use synthetic data specifically on a model trained. On just this sort of state transition type of thing.

> 而那里的关键突破在于:使用合成数据,而且这个模型专门是在这种状态转移类的数据上训练的。

`[52:13]` **SPEAKER_01:** Yes. And this ends up being very convenient because it turns out we, as a society have a lot of this. Exactly. Yeah.

> 对。而这最终非常方便,因为事实证明,我们整个社会拥有大量这类数据。没错。对。

`[52:19]` **SPEAKER_01:** All of YouTube, right.

> 整个 YouTube,对吧。

`[52:20]` **SPEAKER_02:** He does do a very small amount of data from app for, to enable the action conditioning and that get, that allows you to do this full, uh, simulated rollout. But yeah, it's true. So we have, we have YouTube, we have like Flickr, we have all these data sets online of like, you know, people doing things we'd like to use it. And no one has really.

> 他确实用了极少量的数据来实现动作条件化,而那让你能够做这整套模拟推演。但没错,确实如此。我们有 YouTube,有 Flickr,有网上所有这些数据集,都是人们在做各种事情的,我们很想利用它们。可是还没有人真正……

`[52:39]` **SPEAKER_02:** Really gotten that to work. And then now that with this, um, these like video generated generation models, we can take that data, create a world model out of it, add action conditioning, post-train it with action conditioning for some new task. That is we want it to do chopping down wood or, uh, you know, um, making sushi or folding my bed or whatever it is only a few amount of examples. And then we can train a policy on this, in this neural, uh, simulation.

> ……真正让它奏效。而现在,有了这些视频生成模型,我们可以拿那些数据,从中构建一个世界模型,加上动作条件化,针对某个新任务用动作条件化对它做后训练——比如我们想让它砍柴、做寿司、叠被子或别的什么,只需要很少量的样本。然后我们就可以在这个神经模拟里训练一个策略。

`[53:08]` **SPEAKER_01:** Yeah. And you know, we put. And you know, we put out a video, um, about diffusion models very recently in flow matching. I imagine that now ties very closely to this, right?

> 对。我们最近发布了一个关于扩散模型和流匹配(flow matching)的视频。我想那现在和这个联系得非常紧密,对吧?

`[53:17]` **SPEAKER_01:** Ultimately the, the kind of current state of the art best way to do this on basically infinity data that we have available and can keep generating is using state of the art video diffusion slash flow matching.

> 归根结底,在我们拥有的、并且可以持续生成的近乎无限的数据上,做这件事当前最先进、最好的方式,就是使用最先进的视频扩散 / 流匹配。

`[53:26]` **SPEAKER_02:** Exactly. Yeah. So like if you have your, your C dance or your Sora or whatever, exactly all those models. Like basically the idea is now we have them and they're already trained and they're great.

> 没错。所以如果你有 Seedance、Sora 之类的,就是所有那些模型。基本思路是:现在我们有了它们,它们已经训练好了,而且非常出色。

`[53:38]` **SPEAKER_02:** Let's. small amount of action conditioning on them to get to this, uh, this world model. And then we can sample from it a bunch and then train. And this is exactly what wave, uh, did with Gaia and Gaia.

> 那我们就在它们之上加一点点动作条件化,得到这个世界模型。然后我们可以从中大量采样,再进行训练。这正是 Wayve 用 GAIA(以及 GAIA)所做的事。

`[53:51]` **SPEAKER_02:** I think they raised $1.5 billion to, to basically run with this idea for self-driving car. Um, I think a bunch of companies, um, Nvidia, uh, uh, this, this paper here, uh, is basically talking about doing exactly the same, this dream zero for robotics.

> 我记得他们融资了 15 亿美元,基本上就是拿这个想法去做自动驾驶汽车。我想有一批公司,比如英伟达——这里这篇论文——基本上讲的就是做完全一样的事:面向机器人的 Dreamer Zero。

`[54:06]` **SPEAKER_01:** Um, and what I thought was really cool about this paper is that the, yeah, they do exactly this process where they have this, um, joint model of, um, state transitions and actions. They train it by first instantiating it with the open source one video diffusion model. And then it only takes them about 500 hours of teleop data, which is basically exactly this right to get it to be pretty good. And they have a lot of clever tricks that allowed it to be cross embodiment and working on scene tasks with relatively small amounts of data.

> 我觉得这篇论文很酷的地方在于:他们正是做了这套流程——他们有一个对状态转移和动作的联合模型。他们先用开源的 Wan 视频扩散模型来初始化它,然后只需大约 500 小时的遥操作数据(基本上就是这个)就能把它训得相当好。而且他们有很多巧妙的技巧,使它能够跨具身,并且用相对少量的数据就能完成场景任务。

`[54:34]` **SPEAKER_01:** Right. So they're taking basically the exact concept, I believe from the dreamer paper and applying it specifically to these robot embodiments. Exactly. Um, and it, and it turns out it actually works, uh, actually better than I would've anticipated it to work.

> 对。所以他们基本上是把 Dreamer 论文的那套完全相同的概念,专门应用到这些机器人具身上。没错。而事实证明,它确实奏效,而且比我预想的效果还要好。

`[54:46]` **SPEAKER_02:** Right. Yeah. So I think that this is basically the, the, the path to, it was the path, I believe the path to get humans, uh, to be as good as we are genetically over the last 10, 20 million years of evolution, a bigger world model helps, uh, for training and for, uh, test time planning.

> 对。是的。所以我认为这基本上就是通往目标的路径——我相信,让人类在过去一两千万年进化中变得像今天这样出色的那条路径,就是:一个更大的世界模型,既有助于训练,也有助于测试时规划。

`[55:05]` **SPEAKER_01:** Um, and I think it'll be the same thing as true as for, for robotics. What's also cool is there's a bunch of applications of this, the things outside of robotics too. I mean, there was a weather planning paper, for example, we were reading this gen cast paper, which I think applies a relatively similar concept, um, in terms of how they model, you know, literally the world, the world's weather, um, with something like this.

> 而且我认为这对机器人同样成立。同样很酷的是,这在机器人之外也有一堆应用。比如有一篇天气预测的论文,我们读过的 GenCast 论文,我觉得它运用了相对类似的概念——用这样的方式去建模,字面意义上的世界、全球的天气。

`[55:27]` **SPEAKER_02:** Yeah. We have to talk about the world model for the world. Um, yeah. So basically they do this exact same thing where, you know, the key unlocks.

> 是的。我们必须聊聊"针对整个世界的世界模型"。基本上他们做的是完全相同的事,而关键突破在于……

`[55:32]` **SPEAKER_02:** Yeah. Yeah. Yeah. The key unlocks for this whole thing was getting diffusion to work in very high dimensional state spaces.

> 对对对。这整件事的关键突破,就是让扩散模型能在极高维的状态空间中奏效。

`[55:41]` **SPEAKER_02:** Like we talked about in the last, uh, lecture and then learning to, to use that to con action condition in the way that he's done. But they did this for the entire world with this exact same diffusion steps, which go from some, and they go back to, uh, two time steps lag of, of order to AR two for the set of sessions there. And then basically predict the next, uh, state of the world based on the, those things with this Lingam and diffusion rollouts. Yeah.

> 就像我们上一讲谈到的,然后学会用它、以他所做的方式来做动作条件化。但他们是对整个地球做这件事,用的是完全相同的扩散步骤——回溯两个时间步的滞后(相当于 AR(2)自回归),然后基本上就是基于这些东西、通过扩散推演来预测世界的下一个状态。对。

`[56:08]` **SPEAKER_02:** My, my big assertion is that, um, it was necessary for the human brain to develop world modeling. I actually just saw this paper that I wanted to make sure to call out that that was so great, uh, out of, uh, university of Washington, where they say explicitly in the, in the abstract, each cortical area estimates both latent sensory states and actions, and the cortex as a whole predicts the consequences of those actions. Yeah. That sounds like a world model to me.

> 我的重大论断是:人类大脑发展出世界建模是必然的。我刚看到一篇论文,想一定要点名提一下,它太棒了,来自华盛顿大学。他们在摘要里明确写道:每个皮层区域都同时估计潜在的感觉状态和动作,而整个皮层作为一个整体预测这些动作的后果。对。在我看来,这听起来就是一个世界模型。

`[56:37]` **SPEAKER_01:** Yeah. Right. Um, it's actually describing exactly these two equations here where we're estimating both the sensory latent states and actions. I mean, I guess it's really the joint model that we showed earlier is what he's describing here.

> 对。它其实描述的正是这里的这两个方程,我们同时估计感觉潜在状态和动作。我想他这里描述的,其实就是我们前面展示的那个联合模型。

`[56:49]` **SPEAKER_01:** It's exactly this, this equation is showing.

> 就是这个方程所展示的。

`[56:52]` **SPEAKER_02:** Yeah, exactly. Right. And so, uh, if it works in us, it should work in robotics. Um, and I think that that takes us the rest of the distance.

> 对,没错。所以如果它在我们身上奏效,那它在机器人上也应该奏效。我认为那会带我们走完剩下的路程。

`[56:59]` **SPEAKER_01:** Why don't we talk briefly about latent world models, especially the con the JEPA concept? Cause I think there's been a number of papers that use JEPA as an element of their, I guess, architecture. Why don't we just briefly introduce JEPA and how it fits into the current landscape of world modeling?

> 我们不如简要谈谈潜在世界模型,尤其是 JEPA 这个概念?因为我觉得有不少论文把 JEPA 作为其架构的一个组成部分。我们何不简单介绍一下 JEPA,以及它如何嵌入当前世界建模的格局?

`[57:15]` **SPEAKER_02:** Yeah. In classic RL, you'll have like, you know, if you do study Q learning, for example, you basically keep this matrix called the Q matrix and it's going to be, uh, S by a. And so I have this, um, S by a states and actions and each one I need, you know, some, you know, a set of values. And I'm going to do a little bit of math.

> 好。在经典强化学习里,比如你学 Q 学习,你基本上会维护一个叫 Q 矩阵的东西,它是 S×A 的。所以我有一个 S×A 的状态-动作表,每个格子里我需要一组数值。我来做点小小的数学。

`[57:35]` **SPEAKER_02:** So let's just say I take the amount of counts of being in this state action. Uh, and I take the average value of being, of taking that action in this state. Yes. And that's my Q value there.

> 比如说,我统计处于这个状态-动作对的次数,再取在这个状态下采取那个动作的平均价值。对。那就是我这里的 Q 值。

`[57:46]` **SPEAKER_02:** And it's a little bit more complicated than that. There's Bellman equation, all this backup, all this stuff like that. But so this scales horribly because as the cardinality of my space space gets bigger and my kind of action space gets bigger stuff, I don't have enough time. I become less and less sample efficient.

> 实际上比这要复杂一点,还有贝尔曼方程、各种回溯(backup)之类的东西。但这东西的扩展性糟糕透顶,因为随着我的状态空间基数变大、动作空间变大,我没有足够的时间,我变得越来越样本低效。

`[58:00]` **SPEAKER_02:** Correct.

> 没错。

`[58:01]` **SPEAKER_01:** Right. Yeah. And so it's like, yeah, it's this whole thing we described earlier, right? It's absolutely massive because it has all of these elements in it couldn't really enumerate a huge grid.

> 对。是的。这就是我们前面描述的那整件事,对吧?它绝对是庞大无比的,因为它包含了所有这些元素,你根本没法枚举这么大的一个表格。

`[58:10]` **SPEAKER_02:** And so the classic trick, I mean, since I took, you know, uh, C it's two 29 with Andrew wrong in 2012 is you do this, take a neural network on it. Exactly. And you basically are just going to compress that state into some lower dimensional state space. This is actually predates deep learning.

> 所以经典的技巧——自我 2012 年跟吴恩达上 CS229 以来——就是对它套一个神经网络。没错。你基本上就是把那个状态压缩到某个更低维的状态空间里。这其实比深度学习还要早。

`[58:25]` **SPEAKER_02:** Uh, we were doing stuff like this. Um, I think my first paper was basically doing something like this, uh, basically turning like a grid. Uh, into like a bunch of like pyramids and like, and, and the state was how much I'm in pyramid one or pyramid two or whatever, but anyway, the neural network can just do this. And so basically what, uh, the, the key idea in JPA, if I have, um, an image one and I have image two and I have image three, I can do my, my world modeling, uh, my, my world modeling of ST plus one, uh, given ST and 80.

> 我们那时就在做类似的事。我的第一篇论文基本上就是干这个的——大致是把一个网格转化成一堆金字塔,状态就是我处在金字塔一、金字塔二里的程度之类的。总之,神经网络就能做到这一点。所以 JEPA 的核心思想基本上是:如果我有图像一、图像二、图像三,我可以做世界建模,即给定 sₜ 和 aₜ 来建模 sₜ₊₁。

`[59:03]` **SPEAKER_02:** So what I'm going to do is I'm going to, like, I'm gonna get an image from the C plus one and I'm going to place it in pixel space and have, this is, uh, let's say at time t t plus one t plus two, et cetera, et cetera. And I have to actually predict now the full, uh, image that's extremely expensive from a computation standpoint. And also from like a sample efficiency, standpoint. Yeah.

> 我要做的是:我拿到 t+1 时刻的一张图像,把它放在像素空间里——比如说在时刻 t、t+1、t+2 等等。而现在我必须真正预测出完整的图像,这从计算的角度看极其昂贵,从样本效率的角度看也是如此。对。

`[59:31]` **SPEAKER_02:** What I can do instead is put this through some. ComNet encoder, encoder. have a latent for t plus one of a latent for z t plus two and then i'll have from this from zt i want to predict z t plus one hat and my goal is to make this and this uh make my loss function will be something very simple like i want to minimize this that's it now this doesn't work this collapses hard and so what happens like is basically just if you if you just predict zero just output zeros which the model will learn to do and i'm actually incorporating this into my current research right now um and so what you need to do is something called sig reg or uh this is one technique vic reg is another where basically i add this another term that basically says uh i want the um over a large enough batch size i want the the the distribution of z t plus one to follow a gaussian you know it's kind of like a normalized it like a like a batch norm type of yeah of track i mean not in the same and and if if it's zero it can't be this yeah right because then this is non-zero and so maybe i think that there's probably this or something like that but basically this prevents it from modal collapse and it makes it do something good and this is the most recent paper for the audience is le wm le world model which is super super great um however to be completely frank the this this is self-supervised learning super great it doesn't work that well if you were to not do uh these techniques and there's there's a bunch of other techniques that you can do uh it will actually outperform much better and that are let's say for example um if i'm going to do an llm and you have like you know francois uh likes sushi which is definitely true um and i tokenize this into a bunch of different different tokens here and this is token id 6 19 28 whatever and i look up the encoding into this and that's going to be uh e1 yes e2 e3 etc um what you can actually do is have the llm output uh what the lm will take in taking these things and will output um the the next token and so it would be like let's call it h uh this would be the low jets coming out of it t plus one and what you can do is actually have this be close to e t plus one and a lot of people are playing with this idea and getting rid of the cross entropy loss entirely and so if you were to do this it actually is a proxy for the cross entropy loss and there is no cross entropy loss and the cross entropy head is actually very expensive yeah and so this is very cheap and like this lady just so people are playing around with this idea um and as a basically as a cheaper proxy for the cross-country loss so there's lots of different ideas on basically uh taking this jpa idea to not just pixels but to lns as well yeah interesting yeah so just to define what jp is it's joint

> 我可以改为把它送进一个卷积网络编码器,得到 t+1 的一个潜在表示 z_{t+1}、t+2 的潜在表示 z_{t+2},然后从 z_t 出发,我想预测 ẑ_{t+1},我的目标是让这个和这个接近——损失函数会非常简单:我想最小化这个差,就这样。可是这行不通,它会严重坍缩(collapse)。原因是:如果你只预测零、只输出零,模型就会学会这么做(我现在的研究其实正在处理这个问题)。所以你需要做一种叫 SigReg 的东西——这是一种技术,VICReg 是另一种——基本上我再加一项,大意是:在足够大的批量上,我希望 z_{t+1} 的分布服从高斯分布,有点像归一化、像批归一化(batch norm)那样的处理。如果它是零,就不可能满足这个,对吧,因为那样这一项就非零了。总之这能防止模态坍缩,让它学到有用的东西。对听众来说,最新的论文是 LeWM(LeJEPA World Model),超级超级棒。不过老实说,这是自监督学习,虽然很棒,但如果你不做这些技术,它效果就没那么好;而还有一堆别的技术你可以做,能让它表现好得多。举个例子,如果我要做一个大语言模型,你有"François likes sushi(François 喜欢寿司)"——这肯定是真的——我把它分词成一堆不同的 token,token id 是 6、19、28 之类的,我查表得到它们的编码 e₁、e₂、e₃ 等等。你实际上可以让大语言模型接收这些、输出下一个 token——我们把输出的 logits 记为 h_{t+1}——你可以让它接近 e_{t+1}。很多人在玩这个想法,彻底去掉交叉熵损失。如果你这么做,它实际上就成了交叉熵损失的一个代理,而且没有交叉熵损失了——交叉熵头(head)其实非常昂贵,对,而这种方式非常便宜。所以人们在摆弄这个想法,把它作为交叉熵损失的一个更廉价的代理。所以有很多不同的想法,基本上就是把 JEPA 这个思路不仅用到像素上,也用到大语言模型上。对,很有意思。对,顺便定义一下 JEPA 是什么,它是"联合

`[62:56]` **SPEAKER_01:** embedding predictive architecture i think one of the things i find uh cool about this jp idea is it feels like an idea we see over and over in deep learning but there's a version of this idea that's basically the staple diffuse layer of this idea that's basically the staple diffuse layer of the fusion idea. There's a version of this idea that in my company training graph convolutional neural networks to design drugs we use to do latent variable generation, for example. And it's an idea that comes back over and over and then has this various tricks that it actually takes to get it to work in practice. Okay, now we have a pretty good sense for how world models work. We have a pretty good sense for what the state of the art looks

> 嵌入预测架构(Joint Embedding Predictive Architecture)"。我觉得关于 JEPA 这个想法很酷的一点是,它感觉像是我们在深度学习中反复见到的一个想法。这个想法有一个版本基本上就是 Stable Diffusion 里的那一层。这个想法还有一个版本,在我公司里我们训练图卷积神经网络来设计药物时,曾用它来做潜变量生成。这个想法一次又一次地回归,而每次都需要各种技巧才能让它在实践中真正奏效。好,现在我们对世界模型如何运作有了相当好的理解,对当前最先进技术是什么样子

`[63:29]` **SPEAKER_01:** like. If we trust this paper, and it seems like these kind of work on robots too. This paper is only from the end of last year, this year, and it seems like they have various methods that allow you to train on relatively small amounts of data that's tractable and pre-trained on data diffusion models. So are we good? Or does it all work?

> 也有了相当好的理解。如果我们相信这篇论文,它们似乎在机器人上也能奏效。这篇论文才是去年底、今年发的,他们似乎有各种方法,让你能在相对少量、可处理的数据上训练,并在数据扩散模型上做预训练。那么我们搞定了吗?这一切都行得通吗?

`[63:48]` **SPEAKER_02:** We're done. Yeah, this is 2016. And 2016 will be the year of the robot. We're going to have the robot in your house. Yeah, no, I don't think so.

> 我们搞定了。对,现在是 2016 年,2016 年将是机器人元年,我们要让机器人进你家了。哈,不,我可不这么认为。

`[63:58]` **SPEAKER_01:** What are one or two, because there's lots of open problems remaining, what are a few open problems maybe we can...

> 有哪一两个——因为还剩下很多未解难题——我们不妨谈谈其中几个未解难题……

`[64:03]` **SPEAKER_02:** Yeah, so I think the first one is that pins doesn't really work. What is pins? Physics informed neural networks. So pins doesn't really work. This is physics informed neural networks.

> 好,我认为第一个是 PINN 其实并不太管用。PINN 是什么?物理信息神经网络(Physics-Informed Neural Networks)。所以 PINN 其实不太管用。这就是物理信息神经网络。

`[64:21]` **SPEAKER_02:** And so basically, if like almost all of the self-driving car data looks like this, the car is driving down the road. And let's just say, for example, I have, you know, a house here, and I want to train the model on, you know, not driving into the house. And so let's say I put, I put it into a state right here to drive into the house. What's going to happen is because almost all the data is like, looks like this, driving down the road, this will just turn magically into like a highway. And I'm just like, boo, just don't worry. It basically needs like a ton of data not

> 基本上,如果几乎所有自动驾驶数据看起来都是这样的——车在路上正常行驶。假设这里有一栋房子,我想训练模型别撞进房子里。那么假设我把车置于这样一个正对着房子要撞进去的状态。会发生什么呢?因为几乎所有数据都长这样(在路上正常行驶),这栋房子就会神奇地变成一条高速公路。而我就傻眼了。它基本上需要海量的数据才能

`[64:59]` **SPEAKER_01:** to do that either from simulation for that to not happen. In fact, I actually don't even know if

> 避免这种情况,要么从仿真里获取数据。事实上,我甚至不确定

`[65:04]` **SPEAKER_02:** because of the data, I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work.

> 因为数据的问题,我不知道它能不能行得通。我不知道它能不能行。

`[65:05]` **SPEAKER_02:** So there's no data distribution. There's no data here. There's almost all the data here. And like when you're training a neural network, it has a tendency to collapse if you don't keep the mini, mini batch composition, like very even over the, you know, over the class space or whatever you want to want to call it. But like, you'd have to train on, you have to be very careful about

> 因为那里没有数据分布,那里没有数据(撞房子的情形),而几乎所有数据都集中在这里(正常行驶)。当你训练神经网络时,如果你不让小批量(mini-batch)的组成在类别空间(或你想怎么称呼它)上非常均衡,它就有坍缩的倾向。所以你必须非常小心地控制

`[65:27]` **SPEAKER_02:** your data mixing to make sure you get this right to solve this problem that no one really has. But even then, the if you take just a simple thing like this, this is like the conic example. And I have some sine wave. And I want and I have these as my x and I have these as my y. So this is complete interpolation. No, that's maybe messes up. But

> 你的数据混合,以确保把这一点做对,来解决这个几乎没人真正拥有(数据)的问题。但即便如此,如果你只取一个像这样简单的东西——这是个经典例子:我有一条正弦波,我把这些作为 x、这些作为 y。这纯粹是插值。不,这也许会出岔子。但

`[65:55]` **SPEAKER_02:** why like this? No, we can't get to like, machine precision. They can't what is what is it one a minus 16 or whatever it is. We can't we, the SGD will not get to zero, effectively zero.

> 为什么会这样?我们无法达到机器精度。达不到——是 1e−16 之类的吧,随便多少。我们做不到,SGD 不会收敛到零、实际意义上的零。

`[66:07]` **SPEAKER_02:** So we'll always get zero. So we'll always get zero. So we'll always get zero. So we'll always get zero. So we'll always get

> 所以我们总会有(残差)。所以我们总会

`[66:08]` **SPEAKER_02:** have some residual and for us to be like a really good world model to simulate body interactions like to simulate this what's going to happen when i do this and like let's say that i'm trying to be lebron james like there's like i saw this one video of um steph curry dribbling about a basketball on a court and he just felt that there was a dead spot in the court and he because he's so good and he knows exactly the physics of what's going to happen if i hit this you know the ball with this force like the ball is going to come back exactly this spot and it just didn't and he knew it wasn't him it was the the court and he found a dead spot in the court like that's how good the the human brain is at world modeling in my opinion i think it's an sgd issue i think it's probably an architecture issue i think sam altman just kind of came and just said that he thinks that there's definitely an architecture that's going to be more performant than the transformer i think he's right um i think the the transformer doesn't do compression uh uh in the time domain at all it just keeps running everything um so anyway so i think that the getting higher fidelity in the world model is extremely important one i think two seems like test time probably is going to be a big thing like adaptation exactly test time planning we how quickly the human brain can you know in times of in sports and things like that when you're playing tennis i think you're a tennis player like how quickly we can adapt to what a player is doing and things like that we're not going to sleep and like retraining we're very quick to adapt to a new new environment it's like the out of distribution prediction exactly really challenging and like one little data point we can like quickly adapt to that new thing and change um i think there's been a lot of papers uh uh on like basically estimating the friction coefficients and so like those can change over time if you go to a human environment or not for example like this this friction might change and that's important in control um and so you need to estimate that very quickly and adapt and that these models

> 总会有一些残差。而要让我们成为一个非常好的、能模拟物体相互作用的世界模型——比如模拟"我这么做会发生什么"——假设我想成为勒布朗·詹姆斯:我看过一个视频,斯蒂芬·库里在球场上运球,他就是感觉到球场上有一个"死点",因为他太厉害了,他精确地知道物理规律——如果我用这个力量拍球,球应该正好弹回到这个位置,可它偏偏没有。他知道不是自己的问题,而是球场的问题,他在球场上找到了一个死点。在我看来,人类大脑的世界建模就是这么厉害。我认为这是个 SGD 的问题,也可能是架构的问题。我想 Sam Altman 前不久就说,他认为一定存在一种比 Transformer 性能更好的架构,我觉得他说得对。我认为 Transformer 在时间维度上根本不做压缩,它只是一直把所有东西都跑一遍。总之,我认为提高世界模型的保真度极其重要,这是第一点。第二点,测试时(适应)似乎会是件大事——没错,测试时规划。人类大脑能有多快——在运动之类的场合,比如你打网球(我想你是网球选手),我们能多快地适应对手在做的事。我们不会去睡觉、重新训练,我们能非常快地适应一个新环境,这就像分布外(out-of-distribution)预测——没错,非常有挑战性——只需一个小小的数据点,我们就能迅速适应那个新情况并做出改变。我记得有很多论文基本上是在估计摩擦系数,而这些系数会随时间变化,比如你进入某个人类环境,这个摩擦可能会变,而这在控制中很重要。所以你需要非常快地估计它并适应,而这些模型

`[68:04]` **SPEAKER_01:** don't have a mechanism to do it yeah and then i guess there's like those practical speed elements of these right a lot of these are doing some sort of expensive planning step and we're doing some sort of like uh we're kind of hacking around it with this retraining process and synthetic data but even so like to really get maximum performance right now you'd want to do something that's closer to like the alpha go style

> 并没有做到这一点的机制。对。然后我想还有这些实际的速度问题,对吧——很多方法都要做某种昂贵的规划步骤,而我们是用这种重新训练的过程和合成数据来变相绕过它。但即便如此,要想现在真正获得最高性能,你还是会想做更接近 AlphaGo 那种风格的

`[68:29]` **SPEAKER_02:** rollout and that's extremely slow right the mcts process which can't happen um the other thing i'm gonna say is that like the the thing that that is pretty crazy about the way that the brain works is that like everything is kind of running autonomously and so like you'll you might be like in the middle of saying sentence one and be like oh actually no something else and so like what does happen there it's like type one and type two thinking are happening at the same time in some way and so like there's definitely uh you know some um really cool mix of these like heterogeneous models and like some are overriding others and like taking control of the motor cortex and like commanding the body to do a thing you know okay but on the flip side now we um talked

> 推演,而那极其慢,对吧——那种 MCTS 过程,根本没法实时。我还想说,大脑运作方式中相当疯狂的一点是:一切都在自主地并行运行。所以你可能说着第一句话说到一半,突然"哦不对,是别的事"。那里发生了什么?某种意义上,类型一思维和类型二思维在同时进行。所以肯定存在某种非常酷的异质模型混合,其中一些会覆盖(override)另一些,接管运动皮层,指挥身体去做某件事。好,那么另一方面,现在我们谈到

`[69:10]` **SPEAKER_01:** in the past video about the squint test and how we felt that autoregressive llms maybe don't pass the squint test why don't we reintroduce what the squint test was for a second and then maybe let's think about whether this passes the squint test despite all those limitations yeah and this one

> ——我们在之前的视频里谈过"眯眼测试"(squint test),以及我们为什么觉得自回归大语言模型也许通不过眯眼测试。我们不如再简单介绍一下眯眼测试是什么,然后想想:尽管有这一切局限,这个(世界模型)能否通过眯眼测试。对,而这个

`[69:24]` **SPEAKER_02:** test for me i think is like um this comes from the yan lakoon uh we didn't need uh flapping wings to achieve flight um and to that i say well we did need two wings and like if i squint and i look at a bird and i squint and i look at a plane i'm like yeah it's kind of similar it looks right um similarly if i squint i look at the human brain and i squint and i look at all these these world models we have like this vla this action policy and that they're doing test time planning together and things like that it's getting really close

> 测试,在我看来——这来自 Yann LeCun 的说法:我们实现飞行并不需要扑动的翅膀。对此我要说:可我们确实需要两只翅膀啊,如果我眯着眼看一只鸟,再眯着眼看一架飞机,我会觉得,嗯,它们还挺像的,看起来对。同样,如果我眯着眼看人类大脑,再眯着眼看我们拥有的所有这些世界模型——比如这个 VLA、这个动作策略,以及它们一起做测试时规划之类的——它已经变得非常接近了。

`[69:53]` **SPEAKER_01:** it's much much closer it seems closer than an autoregressive llm and that's like this concept of a world model of you know implicitly predicting future states and actions feels and we're thinking about things like that because we're thinking about like what we're

> 它接近多了,似乎比自回归大语言模型更接近。而世界模型这个概念——隐式地预测未来的状态和动作——感觉上……而我们之所以思考这类事情,是因为我们在思考我们正在

`[70:09]` **SPEAKER_02:** doing and it seems like there's some you know neuroscience evidence yeah i mean i'm i'm getting to the conclusion that i think that the brain is the optimizer not the model and that the brain emits like has models that it invokes but the brain is somehow also the optimizer itself and so in that way it doesn't pass the squint um because like you know something magical is happening when you're sleeping there's no intelligent species that we're aware of that have dolphins all those stuff elephants they all sleep there's some reason for that and that seems like a really thing about like the evolutionary re like recourse of sleeping like you get eaten when you sleep so like for the benefit of sleeping should be so so much better to outperform that so i think we don't have this idea of awake sleep uh in our current um architecture but i can imagine i'm like simulating you know you know compressed from the hippocampus some like experience in the day i'm like training on more of those examples right you're like collecting a whole bunch of

> 做的事,而且似乎有一些神经科学证据。对。我逐渐得出一个结论:我认为大脑是优化器,而不是模型;大脑会发出、会调用它拥有的各种模型,但大脑本身某种程度上也是优化器本身。从这个角度说,它通不过眯眼测试。因为你睡觉时,某种神奇的事情正在发生。我们所知的所有智能物种——海豚、大象——它们都睡觉,这是有原因的。这真的很值得深思:从进化的角度看,睡觉是有代价的,你睡觉时会被吃掉,所以睡觉带来的好处必定好到足以压倒这个风险。所以我认为我们当前的架构里没有"清醒-睡眠"这个概念。但我可以想象:我在模拟——从海马体压缩出来的、白天的某些经历,我在用更多这样的样本进行训练,对吧,你在收集一大堆

`[71:05]` **SPEAKER_01:** these experience rollouts and then you're updating your your policy function there's got to be something

> 这些经历的推演,然后更新你的策略函数。那里一定有某种东西

`[71:11]` **SPEAKER_02:** like like there's this thing called shortwave ripple where like the hippocampus when you're sleeping like emits these uh spike trains that are actually reversed from when they actually happen back in through the both both the hemispheres and for like seven times and then it like stops so like there's something happening there that's very uh uh training something yeah and if you don't sleep then you don't up you don't have long-term memory right right and so like there's definitely a reason why we're training uh things that happened uh into our brain so where does that put us now we have all this

> ——有一种叫"短波涟漪"(sharp-wave ripple)的现象:睡觉时海马体会发出这些脉冲序列,而且相对于它们实际发生时的顺序是倒放的,穿过两个半球来回传递,大约重复七次然后就停止。所以那里发生的事情非常像在"训练"某个东西。对。而如果你不睡觉,你就不会——你就没有长期记忆,对吧。所以我们把发生过的事情"训练"进大脑,肯定是有原因的。那么这把我们带到了什么处境?现在我们有了所有这些

`[71:42]` **SPEAKER_01:** work happening with world models how should we think about what's coming ahead in these next

> 围绕世界模型展开的工作,我们该如何看待接下来这几年

`[71:45]` **SPEAKER_02:** few years in the research community yeah i think that like we're going to see a lot more uh of these world models in robotic policies i think that's going to unlock probably full self-driving would be like a one of those examples that they can get the real-timeness of it it seems like that's coming probably solve it with more compute to like have parallel things and you probably don't need it for like most standard things maybe like you know getting out of weird parking jams and like things like that would take us some time similar to the rose of the robot which we've always wanted to have a rose of the robot to like you know clean up my room for me um i think that like this feels like we're getting to good enough that we can pay up for data and compute to get to rose of the robot it does feel like that it'll be expensive to collect the data and do the dreamer sequence of going from state to state and then getting the action conditioning to work but like

> 研究界会发生什么?好,我认为我们会在机器人策略中看到多得多的这类世界模型。我觉得这大概会带来完全自动驾驶——那会是其中一个例子,只要他们能解决它的实时性问题,而这似乎快来了,可能靠更多算力来并行处理来解决;对大多数标准场景你可能都不需要它,也许像脱离奇怪的停车僵局之类的还得花些时间。类似地,还有"Rosie 机器人"——我们一直想要一个 Rosie 机器人帮我打扫房间。我觉得现在感觉我们已经做到足够好,好到值得为数据和算力砸钱来实现 Rosie 机器人了。确实感觉是这样。收集数据、做 Dreamer 那套从状态到状态、再让动作条件化奏效的流程会很昂贵,但

`[72:37]` **SPEAKER_01:** i feel like it should work yeah i mean what's pretty cool is we see a lot of companies at yc working at every step of this from the collecting egocentric data collecting uh the teleop data training their own world models and action models um building new embodiments and then making ways of adapting those embodiments and feels like this is the first year where you see demos where you're like okay this actually like kind of is starting to look like it's going

> 我觉得它应该能行。是的。很酷的一点是,我们看到 YC 里有很多公司在这条链路的每一个环节上发力:从采集第一人称数据、采集遥操作数据,到训练自己的世界模型和动作模型,再到构建新的具身,以及想办法让这些具身相互适配。感觉今年是第一年,你看到那些演示会觉得:好吧,这确实开始看起来像是要

`[73:01]` **SPEAKER_02:** somewhere yeah and it seems like a very exciting year yeah so anyway i think that there are real ai problems to solve still we talked about pins we talked about the real time issues and then on the robotic side there's real issue like it's amazing how effective our epidermis is in terms of we we can detect tactile oh epidermis yeah epidermis are tactile we can detect shear force we can detect temperature and it's everywhere yeah and so like versus you know like the we get like one little sensor that only does tactile we don't have the the friction component we don't have temperature we don't have all these the feeling we can't estimate coefficient of friction very quickly i can touch something and say oh this is smooth this is rough it doesn't we don't have any of that and if i numb your hands i actually had this experience um just recently if i numb your hands like you actually can't tie your shoes yeah so you can't perform control and so like yeah if you like you know uh uh if you train enough um on enough human data tying your laces you can do it with no feedback maybe maybe but like how much would you need if you did actually have the human like touch like i think it'd be so much easier yeah well there's a lot of more

> 走向某个方向了。对,而且这看起来是非常激动人心的一年。对。总之,我认为仍有真正的 AI 问题有待解决:我们谈了 PINN,谈了实时性问题;而在机器人这一侧,也有实实在在的问题。我们的表皮有多么高效简直令人惊叹——我们能感知触觉。哦,表皮,对,表皮能感知触觉,我们能感知剪切力,能感知温度,而且它遍布全身。对。相比之下,我们(机器人)只有一个只能做触觉的小传感器,没有摩擦这一项,没有温度,没有所有这些感觉,我们没法很快估计摩擦系数。我可以摸一样东西说"哦,这个光滑、这个粗糙",而它——我们完全没有这些。如果我把你的手麻掉——我最近其实亲身经历过——如果把你的手麻掉,你实际上连鞋带都系不了。对,所以你没法执行控制。所以,如果你在足够多的人类系鞋带数据上训练得足够充分,也许能在没有反馈的情况下做到,也许吧;但如果你真的拥有人类那样的触觉,你需要的数据量会少多少?我觉得会容易太多了。对。嗯,还有很多更多的

`[74:12]` **SPEAKER_01:** research to do then yeah yeah Francois thanks so much for joining us thanks so much for watching everyone we'll be back for the next episode of Decoded

> 研究要做。对,对。François,非常感谢你来参加。也非常感谢大家的收看,我们下一期《Decoded》再见。
