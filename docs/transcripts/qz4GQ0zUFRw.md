# 全文转录 · 人脑真正独有、AI 正拼命追赶的那个东西:世界模型

> ▶ [YouTube](https://www.youtube.com/watch?v=qz4GQ0zUFRw) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/qz4GQ0zUFRw.md) &nbsp;·&nbsp; The Key Thing Human Brains Have That AI Is Trying To Learn
>
> 🗣️ 说话人分离识别到 **3** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_01:** One of the biggest open problems in AI right now is how to solve sample efficiency. That is, how do you get models to quickly learn new tasks or skills from relatively small amounts of training data?

`[00:08]` **SPEAKER_02:** Humans do this incredibly well. We can learn new games, concepts, and skills, often after just a handful of tries. Our best models, on the other hand, often need tens of thousands of data points just

`[00:18]` **SPEAKER_01:** to learn. So today we're going to discuss what many top researchers believe is the most promising path to closing that gap, world models.

`[00:24]` **SPEAKER_02:** We're going to discuss the motivation and math behind world models, current applications, and why this approach might be the key to unlocking AGI.

`[00:39]` **SPEAKER_01:** You and I have talked a lot about the various ways people are training models and the sample efficiency of them. Why don't we start by just defining sample efficiency and how we intuitively think about it as humans?

`[00:49]` **SPEAKER_02:** Yeah. So I think from my perspective, the two major problems that we have left to solve is intelligence per watt and intelligence per sample. Intelligence per watt is like how many valve perplexity points we get per watt of spend. And then intelligence per sample is basically... If I have one addition... If I have one additional sample in my data set, how much more intelligent am I getting? And so if I imagine I have a new task, like RKGI, for example, I think really, François Chollet has been on the forefront of this thinking and talking about intelligence as

`[01:17]` **SPEAKER_02:** a rate of skill acquisition versus skill acquisition. And that's very different. And so how fast do we get smarter with more and more samples? And these things are incredibly poor at getting smarter with fewer and fewer samples.

`[01:33]` **SPEAKER_01:** And for context, the RKGI test... Yeah. The RKGI test sets are a really good example of cases where humans are intuitively very good at them. Most humans can intuitively solve those puzzles with some amount of thinking and effort. But our current state-of-the-art AI systems, what people consider frontier intelligence, basically can't do them. Right.

`[01:52]` **SPEAKER_02:** I mean, we come into new problems with such inductive bias from K through 12, like all these math in school that we've had, that these models are kind of getting from the entire... Yeah. The entire internet. And so when we come in, we're not coming in tabula rasa, just bare bones, but even so that they have... I don't know what percent of the internet you've read. I've read very little percent of the internet. But despite that, and having read the entire internet, it still can't really do well in

`[02:20]` **SPEAKER_02:** generalizing to these new tasks.

`[02:22]` **SPEAKER_01:** So now let's think about this in the extreme cases. In the extreme case where let's say we were perfectly sample efficient, we were as sample efficient as possible. What would that mean in terms of a... A model that is taking a set of actions in the world?

`[02:37]` **SPEAKER_02:** Well, I guess the perfect sample efficiency would be zero samples. And there are examples of this, and that sounds absurd to say, and the hypothetical I'll give on this is imagine I had a perfect world model, then I should never go to the environment to go and collect samples to train on. And well, that can't possibly happen. No, it actually can happen. We do it all the time. It's called Newton's second law of motion. It's like Newton mechanics. We basically know how to get an object from point A to point B with a rocket quite easily

`[03:12]` **SPEAKER_01:** just by following Newton's laws of motion. Yeah. When NASA plans to intercept an asteroid and is planning it years in advance and can set it off in a trajectory where it just glides to the right thing and intersects to the right point, that is an example of a perfect world model we've built where we're then just letting that world model act. And that system does not need to intelligently... Yeah. It can intelligently collect new samples from the environment to decide which direction to go next.

`[03:37]` **SPEAKER_01:** It's already been pre-programmed and it can perfectly do it.

`[03:39]` **SPEAKER_02:** Yeah. Can you imagine if we needed to collect 1 million training examples of us shooting spaceships to the moon to know how to do it? Right. We definitely wouldn't have the Apollo missions, right? But we do have that ability because the real world is differentiable and we can do something called model predictive control that we're going to talk about in a little bit. But even in our own brain... I was just thinking about this on the drive up, but there's so many ways that I can basically

`[04:07]` **SPEAKER_02:** think about the things that you are going to say or what a VC is going to say when I was pitching them or what a customer might say, and even product, having taste. What is taste? It's like predicting that other people are going to like this thing. And so we've built this world model over years of entrepreneurship, 10 years of like getting it wrong, right? That maybe Bill Gates, Steve Jobs, and Jensen... Yeah. Yeah. ...couldn't have 50 years of world modeling experience to know what people want.

`[04:38]` **SPEAKER_02:** And basically, this is actually proven in the 1967 COGSI study by Richardson, that basically showed that if you take a cohort of three groups of people and you have one go practice layups in basketball, and they go and they shoot, they improve... For one hour, they've improved by... I think it was like 24% or something like that. And then if you take the other one... they just blindfold them and they imagine laying up a basketball they improve it 23 interesting against the control i mean that's insane it means that we have this

`[05:12]` **SPEAKER_02:** crazy good world model and there's this neuroscientist at stanford named shaw drachman who basically is of the view that the entire point of the growing neocortex for the during the great cortical expansion 10 million years ago was to get better and better and better and better world modeling and having just like my little vla which we'll define of doing the next predicting next action is not as good as having a world model to lean on either for training for training purposes or for test time adaptation yeah what it fundamentally comes down

`[05:41]` **SPEAKER_01:** to is you know we as humans we think about our intuitive ability to think as coming from some implicit world model we have in our heads encoded by genetics and our ability to learn and whatever else it seems like models can do surprisingly intelligent things despite not having an explicit world model when it comes to natural language when they're just talking it seems like you know maybe under the hood deep inside the weight somewhere there's some kind of implicit understanding of the world but there isn't an explicit representation of that

`[06:10]` **SPEAKER_01:** but it seems like in certain domains especially in robotics and self-driving as we'll talk about that sort of breaks down and um you know maybe it would be helpful now to just think a little bit about and sort of define some of the pieces of what makes it challenging in these different domains and then we can use that to kind of build up to why it's particularly hard in things like robotics to get these types of predictive models to work yeah let's do it so let's actually like

`[06:35]` **SPEAKER_02:** take a step back and just talk about like control reinforcement learning and define some define some common terms so typically in um we teach a course called decision making under uncertainty which is like the main reinforcement learning course at stanford i like to show a specific example of let's say i have some drone and this is my poor little drone here and it has some mass m and we have some uh some sort of uh like gravity g is pulling down on it and it's currently at position

`[07:07]` **SPEAKER_02:** uh t with velocity t which we will collectively call the state and to be really clear this is going to be p x p y p z t t t and v x v y z v z it's like the six-dimensional state vector yep and we have uh some thrust vector u and we're trying to get to some point p star and v star which is v star is typically zero and so you have some platform that i want this thing that's drawn to land on this is this control problem right and so uh let's say this is like and we'll go through optical or optimal optimal

`[07:52]` **SPEAKER_02:** optimal control so how would i actually solve this so the first thing i need to know is my transition function and so this is my state transition function which is st plus one given the previous given st and my action which which i control is ut and so this is my state transition or dynamics function or a world model this is a world model this is like a very fundamental for

`[08:17]` **SPEAKER_01:** for context you know this this equivalent to the transition function you would think about in rl in

`[08:21]` **SPEAKER_02:** general exactly and so uh and then what i'm trying to learn is something called a policy which is like what ut should i uh uh emit given some st yep and so this is the ultimate question what should i do what action should i take given some state st and so uh the way that we'll solve this and luckily we have a world model that is perfect it's called newtonian physics newtonian physics this is like newton's second law of motion which is f equals ma and so we know that the position p t plus one is going to equal p

`[08:59]` **SPEAKER_02:** t plus uh delta t vt plus one half delta t squared so everyone's taking high school high school physics and the same thing for the velocity and then my acceleration is the sum of some of the for some of the forces uh which is going to be my uh ut i think i divide by the mass and g and so that's it and now i have my transition function now how do i get to a policy and i'm going to apply something called model predictive control or real-time model predictive control which is like the way that

`[09:37]` **SPEAKER_02:** spacex lands the rocket on uh on some platform in the ocean and what you're going to do is you're going to set up your loss function you're going to minimize sum over all t you have ut to infinity and i'm going to minimize my p star minus pt plus v star minus vt and usually you add this little lambda ut which is like how much energy you're exerting and you can't have infinite thrust so you typically will have to say ut u max thrust yeah that can be achieved and so this is easily solvable with comics optimization

`[10:26]` **SPEAKER_02:** and so this is convex this is convex this is convex the sum of convex functions is convex this constraint and so i dcp discipline convex programming means that i can put this into cvx pi and it will just give me out my policy which will be the solution will be the optimal

`[10:47]` **SPEAKER_01:** ut plus one all the way to infinity so we can solve this in closed form basically we can because we have this world model of newtonian physics we can say at every step exactly how this drone should fly so that it lands on the appropriate thing exactly under a set of constraints

`[11:03]` **SPEAKER_02:** Exactly. You'll run your log barrier, interior point, whatever, to some solver on this, and it will give me my optimal, and this would be literally the optimal path that this thing can take to get to this state. And that will minimize, and I can increase this if I want it to do the least energy path, and I make that zero if I want it to be the fastest. And so that's typically the way that you would do what I would call deterministic differentiable control. And why differentiable?

`[11:40]` **SPEAKER_02:** Because I can form the Lagrangian by taking this minus this constraint and take the gradient of it, and I can do monorobins.

`[11:50]` **SPEAKER_01:** You use the fact that it's differentiable to do the optimization. Exactly.

`[11:54]` **SPEAKER_02:** If this is non-differentiable, you cannot do convex optimization, and you cannot do SGD. Even if it's non-convex, you could still solve and get a pretty good solution, as we do in deep learning, but if it's non-differentiable, you kind of can't. There's nothing you can do.

`[12:08]` **SPEAKER_01:** So, yeah, let's have an example then of how you could make this non-differentiable. Like, well, what's a scenario, I guess, even in like this drone scenario where it now becomes non-differentiable.

`[12:16]` **SPEAKER_02:** Yeah. So I'll put this adversary named Ankit. Okay. And your job is to, you have another drone, let's say, Ankit's drone is to try to hit me and stop me from getting there.

`[12:28]` **SPEAKER_01:** Now, from the position of your drone, you don't know what actions I'm going to take. Right.

`[12:32]` **SPEAKER_02:** And so now, let's just call this the, this would be now, we're definitely not deterministic, we're stochastic, and stochastic and non-differentiable. And in this case, my state transition, what is ST plus one? It's going to be my, say, I'm in now, my thrust, and what Ankit's going to do. Right. And these, it was all differentiable until this new variable. Yeah. And I can't like back prop through your brain to say what you're going to do with your little drone controller. Right. It's completely non-differentiable now.

`[13:12]` **SPEAKER_02:** And I'm resorting and I have to resort to this awful area called reinforcement learning, which is just super brutal and it's sprawling and there's so many different things. And you'll hear things like when you study initial reinforcement learning called value iteration or policy iteration. And there's DQN or deep Q-learning or just Q-learning, there's actor-critic, there's all this bag of stuff.

`[13:40]` **SPEAKER_01:** And all of this stuff ultimately comes down to ways to estimate, to model this non-differentiable stochastic process. Exactly.

`[13:50]` **SPEAKER_02:** Yeah. And so that's basically the main thing is you're going to start talking about this as a model where I'm going to introduce this psi to say that this is going to be stochastic. This is going to be some model that's going to take in these things and then output this and that we're going to train it over many, many instantiations of this. And that's to get a better and better world model. And then I need to train some policy, A-T-S-T. And then typically you also need a value function.

`[14:18]` **SPEAKER_02:** Yeah. And that is the value of some state. And to discern between the value of different states. And in this case, I don't know what a valid state is. But let's just say I was doing... SpaceX with launching rockets and landing rockets in Florida. Let's just say that there's different... If I have my launch pad here and I have a whole bunch of houses here, let's just say the path going from here to here, I may think that doing this and then coming across here and burning all these houses alive may be not highly valued.

`[14:56]` **SPEAKER_02:** So I might say, as an example, they typically call this some kind of a cone. And I might say it's low value to be here and it's very high value to be in this cone or something.

`[15:07]` **SPEAKER_01:** In a sense, the value gives you some expectation of future rewards, like the sum of future rewards you're getting. And so if you're in a bad space, you would set the value to zero or negative infinity or something like that.

`[15:18]` **SPEAKER_02:** Yeah, so we should introduce R-T as well. And so typically, if you're playing Go or chess, winning the game, you can say winning the game is plus one, minus one for losing, draw zero. That's what's done in AlphaGo. In chess, we have these heuristics, like a pawn is worth one point, a rook is worth five, et cetera, et cetera. So you can already have reward is the difference in board state. And then this, yes, will be the sum of my discount. I should just do T of R-T. Yeah. And it's important also to use this nomenclature.

`[16:00]` **SPEAKER_02:** The pie. And the reason why that's important is because what's actually happening here is this is the discounted reward following policy pie. And that means that when I'm in this state, I will take this action, and then I'll end up in this to SC plus one, and then I'll take this action, and it's taking it greedy. And so that's the value with respect to pie.

`[16:20]` **SPEAKER_01:** And so ultimately, what it comes down to is we are trying to still find a new policy pie. And along the way, we will use the learning models in various capacities. This is standard RL to estimate the value function given the rewards we're receiving. And then where world models come in is a way of incorporating all of those into some sort of joint modeling of the state and action distribution so that we can make more intelligent policies off of it.

`[16:48]` **SPEAKER_02:** And so your standard kind of setup for this is what I'm always trying to get to at the end of the day is some joint distribution, which would be SC plus one, given where I'm at now. And then this factorizes with chain rule, simply to my pie, my policy, AT given ST, and my world model. This is usually represented with theta. And this is my world model, which would be ST plus one, given ST and AT. And these are typically learned separately. And you can imagine, in fact, actually, you can actually learn this.

`[17:35]` **SPEAKER_02:** This is a video generation model. And I have the frame ST, and I predict the next frame ST plus one.

`[17:39]` **SPEAKER_01:** And we'll get into this. For those of us who kind of saw our diffusion model series, often people these days use video diffusion for exactly this.

`[17:47]` **SPEAKER_02:** And then what you can do, and this is like the in vogue thing to do since Danijar and the Dreamer paper series from V1 to V4 is do action conditioning later, like similar to clip. Where we will inject this like input head, input tail to come into the model to influence and enable the world model to have embodiment. What does that mean? It means that not only can I predict like as a plant or tree growing on the side of the building, I can like see the world passing by, but I can actually influence it.

`[18:21]` **SPEAKER_02:** And I can change the world, and I can learn that with AT. And that's far fewer samples to do this post action conditioning. Right. I already have a really good ST to ST plus one world model.

`[18:35]` **SPEAKER_01:** And so here you're saying, you know, what's also in vogue now is jointly training these versus separately training them. Exactly.

`[18:42]` **SPEAKER_02:** And so this is called, that is called a world action model where some of the issues here is one, there's all these training dynamics. If these things are just disparate training on different sets and things like that. The other issue is plainly obvious. What I have to do to actually do test time planning is I'll have to sample my. With model one, invoke theta and then pass that sampled action into here and then roll it out to ST plus one and it's very expensive and it's a very not real time to major issues and why, like, why can't we just scale up alpha go to like solve all the problems is because it's because of this property.

`[19:20]` **SPEAKER_02:** If I have one invocation to the model and it gives me both, here's the action I should take. And here's the ST plus one that'll end up much, much cheaper and much, much faster.

`[19:29]` **SPEAKER_01:** Okay. So I think that's. Really good segue. I think, why don't we now motivate everything we just described through a series of increasingly complex environments. So I'll contend that I think the right set of environments for us to consider is chess followed by go, followed by self-driving followed by robotics.

`[19:48]` **SPEAKER_02:** Um, all right. So let's go through a couple examples of problems that we want to apply, uh, reinforcement learning to. So chess is, is a pretty easy one. There's an eight by eight grid. Um, and so typically when you, when you, uh. Approach any, uh, RL problem, you're going to look at, uh, star. And so this, this, the size of the state, uh, the number of states I can be in. So if I have these eight here and these eight, so this would be eight, 1632. So it'd be 32 to the 64. Yes. Quite large, quite large.

`[20:23]` **SPEAKER_02:** Then, uh, my transition function is. Stochastic and non-differentiable. Cause you can, you don't know what the other player is going to do. Yeah. So if I'm like. In, uh, playing chess.com at my house, I move and then something happens and it comes back and, and then now you moved and the board has changed. So I can't really differentiate through what the other player, uh, is doing. The car line, my action space is actually quite small. Um, even though there's 32, uh, uh, pieces and all that stuff that there's only eight possible moves in expectation that you can actually, that are legit moves.

`[20:55]` **SPEAKER_01:** So like in any, in any given state, there's only eight ish moves you could do.

`[20:59]` **SPEAKER_02:** Let's just say in the beginning I can move all my pawns. I can move my horses. So that's tent. Yeah. That's like not that much. So this is extremely small. And then my reward, we can use the heuristic based approach, or we can just say, you know, plus one, zero or minus one. If I lose plus one, if I win.

`[21:14]` **SPEAKER_01:** And, uh, so this is very tractable. You say it's tractable, even though there's a really big state space here. Yeah. But why don't we talk about that for just a second? I think this is a really important point. When you say it's tractable, you're specifically referring to the action space being small because it affects the kind of like color. This is the combinatorial expansion here. Should we talk about that for just a second? Yeah. Or maybe we can add go and then kind of contrast the two.

`[21:37]` **SPEAKER_02:** Yeah. So why don't we do that? Because, um, it's because I want to get to the alpha go, uh, uh, the way that they solve this and you're right. So if I were to do this naively and I just took, um, and my ST plus one and I want to do look aheads. Uh, what I would do is I would take all of the actions I can take. So there's eight. So I would do action one, action, two action, eight. Bop. Bop. Bop. Bop. these i need to expand it for all possible states and so now i need to do cardinality s which we

`[22:07]` **SPEAKER_02:** just said is this huge freaking number and so i have to do that eight times and i have to do it again i have to do it again so just doing looking forward one move is like quite intractable although

`[22:19]` **SPEAKER_01:** at the same time you know the you everyone starts at the same starting position and while it is a really large space you know it there isn't an infinity number of potential there's actually a really really small number of game boards even four moves into the game right as opposed to a game where you could start in any permutation for example of initial game state and right what

`[22:41]` **SPEAKER_02:** a few states down yeah so this is like definitely over uh um done because there's there's it's it's much much less than this in practice yes but just naively like looking at you know uh what possible game states could be in a game where you could start in any permutation you could start in any could be uh as a rough math here but this is roughly the idea and then each one of these leaves i need to invoke my value function right uh which is the value of that state t plus one and so i have to do that all many times and we'll get this off a go but like

`[23:10]` **SPEAKER_02:** this ends up being estimating the leaf node uh because at the end of the day my policy atst i want to pick on the arg max of like the value of the the following action i guess it would be yeah a exactly yeah the arg max over a of the value of the state of the of the end state st plus n let's say it's like that's the the main goal here um and so for me to do that i need to roll all this out estimate the value and then pick the best one and so this this quickly grows um however and we'll see this about how we go

`[23:50]` **SPEAKER_02:** which is actually actually has an even bigger state space um so i'm going to do that and then i'm going to do that so i think it's 19 by 19. um apparently i think it's spot right now so you have this 19 by 19 grid you can in each one it can be black white or or nothing there so i have three uh so let's do our star again so the cardinality of the state i think is going to be s uh two or three my ternary thing here to the 19th squared i think it's 361. yeah something like that 361. um

`[24:23]` **SPEAKER_02:** my transition same issue i don't know if it's going to be the same issue i don't know if it's going to be the same issue i don't know uh my action space is going to be 361 let's say so it's a good amount

`[24:31]` **SPEAKER_01:** bigger than chess much bigger but it's still not uh enormous yeah as we'll see in a second yeah

`[24:38]` **SPEAKER_02:** and so basically what they do they call this z which is kind of annoying but let's call it r and it's the terminal it's the terminal when they won the game and they basically you know you have your trajectory which is um s zero a zero r zero um then all the way to the end of the game yep s n a n r n and if you won then all of these uh all the moves that black if black won all the moves that black did get plus all the moves that white did were minus one and they just that's how they create their um their rollouts rollout refers

`[25:20]` **SPEAKER_01:** to a taking n steps of play of all players one after another yeah of moves under a specific policy at the at the particular instantiation of it

`[25:32]` **SPEAKER_02:** right so let's just let's probably under this policy p theta t and we're gonna overload t but like this is that instantiation we froze that model we froze that model and we play i think it's like 70 games and we like treat all of those and we're going to sub sample a bunch of um of these uh state action results state action results to train our to update our policy in our um in our world model our transition model and what it's actually doing is we we take in an st we give it to some theta and it wants to output um the probability of st plus one being played

`[26:12]` **SPEAKER_02:** which is our transition function and uh the uh value of the current state and how do we get the velocity and so the value of the current state uh well both of them are coming out of the model but basically the loss function l theta is going to equal and it's going to be really close to this control problem one is we have some v theta minus this z which we'll just call it r here um squared and then plus uh actually so it's minus this pi which i'll explain in a second log p theta and i think they everyone includes this but

`[26:59]` **SPEAKER_02:** they include it in the paper so i'll include it there as well which is the um weight decay yep and so um so this is basically what uh our loss function is then we'll play a bunch of these games and let's try to be a little bit organized here and uh and so this is our setup this architecture and now the most once we train this thing we do an insane insanely expensive task of uh of test time planning and so this trend in rl is just called test time planning and the specific algorithm they use here for this is

`[27:35]` **SPEAKER_02:** monte carlo research mcts and so this is one of the possible things that you could do uh it ends up working extremely well if you have small action spaces yeah so let's let's like very intuitively

`[27:47]` **SPEAKER_01:** talk about what mcts does a lot of people have heard about monte carlo research because alpha goal was such a you know big moment yeah how exactly does that map into our star and value

`[27:57]` **SPEAKER_02:** function and policy yep so i'll take this as t this will give me uh 361 uh uh numbers that sum to one and so i'll have some probability of uh of where these things are gonna go for the of where my my opponent will play um here so these are like the sets of actions yeah so i'm here so that i have all my st plus ones i'll have 361 of

`[28:23]` **SPEAKER_01:** these things um and then to be clear this is like action one action two all the way to action yeah

`[28:30]` **SPEAKER_02:** exactly yeah and the um we have to estimate the value of each one of these and so then we have to invoke the model all 361 times to give me values for each one of these things and then i will select i'll select it based on the the ucb the upper confidence bound which is this equation that is roughly something like um balancing uh my value function of st plus one which they're gonna in the literature would be called the q value because it's actually the difference between a value function and q value is just that i have the action as well yep so it'd

`[29:12]` **SPEAKER_02:** be st then at um so we'll just call that q value which is my um exploitation term and then my exploration term will be something like uh it's this funky square root of n uh so it's the arg max of a of my q and then i have this which is the probability of this this move being played which we have from here of of s let's just call it st plus one and then i have this term which is this sum over uh n s b divided by n sa and yeah what's what what's the intuition yeah this term so these ends is is the the v

`[30:03]` **SPEAKER_02:** So this whole tree, I'm going to, so this tree could get really big, right?

`[30:08]` **SPEAKER_01:** It's three 61 per thing, depth of 30. So you can't visit every single week though.

`[30:14]` **SPEAKER_02:** Exactly. And so you want to keep track of which, uh, which state did you end up in? And what action did you take when you were in that state? And you want to make sure that you, you have good exploration, right? And so the way you keep track of the way you ensure that you have good exploration is you want to not just be greedy and always pick the highest value one, because that could be local, very myopic. And so what you'll do is during this MCT process, you'll start this dictionary,

`[30:44]` **SPEAKER_02:** which will be all zeros of the visit count of being in this state and taking this action, and then once you go through your first rollout, you'll do, you'll go here. You'll all these things will be an edit to zero. You'll have some probability. What we're going to do is we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to do a, we're going to bias it towards the

`[31:02]` **SPEAKER_02:** higher probability of places to go. And then we'll go, we'll expand those trees. And then we will, um, update the counts that we visited this and that will basically reduce the amount of, uh, uh, probably that we're going to select it again, because this, this will reduce my, my exploration term. And if it's highly valued, then we're going to increase the Q on this. Cause this is the expected value of going down this, this, this path.

`[31:29]` **SPEAKER_01:** So the gist of it is fundamentally. You want to take the optimal ish path, but have enough exploration in this really expensive, uh, step you're doing here so that you are making sure you're getting a decent chunk of the other potential leaf nodes you could traverse to right in these 30 step rollouts.

`[31:51]` **SPEAKER_02:** And so I'm going to do this, this MCTS simulation 800 times here. And then for all 800, I have to go through this whole process and I have to invoke them. The model, like at least 30 times to get through all of here. And so that's, you know, 27,800 times 30.

`[32:09]` **SPEAKER_01:** Yeah.

`[32:09]` **SPEAKER_02:** And so, uh, 24,000, uh, invocations of the model to, to develop this tree. And then once I have it per step, per step, just to do one action into the game. A lot of people don't understand that this is like, you don't like store this MCTS tree, you like you throw it away after, uh, you, you make the move. Um, but once it's very expensive to develop this MCTS tree. And once you have it, the probabilities of traversal are actually extremely useful for training. And then you end up biasing it and you train it with the MCTS tree, which is like a little

`[32:43]` **SPEAKER_02:** bit, seems like circular motion or something like that. Like, uh, but you end up treating that as, as the pie that you'll train in your loss function. Um, so you, we have the R of, did we win or lose? We have the pie of, of what was the end result of this whole expensive process. Um, and then at test time, we are going to do these 24,000 steps, every single, um, uh, every single move to pick the arg max, uh, that gives that, that satisfies both exploration and exploration and exploitation.

`[33:18]` **SPEAKER_01:** In this case, you know, this still feels somewhat tractable though, because the action space is small enough where this like kind of works. Exactly. But now like, let's say hypothetically, maybe we can draw like an imaginary go, a game, a game of go where it's like, you know, let's, let's, let's say this game of go was like a thousand by a thousand. And so now you have a equals, uh, you know, more or less, uh, a million. And now this, this tree, uh, we're drawing here that has to take here.

`[33:52]` **SPEAKER_01:** This has cardinal or like, you know, with, I guess 1 million. Right. And there's like S zero through S 1 million. And the number of, uh, you know, steps you would have to take here, presumably will have to be way more than 800 in order to get any reasonable, uh, kind of sampling of this. And so you're probably multiplying the test time cost of doing a rollout or of doing a next step prediction astronomically. If the game was even, let's say, you know, this is only a hundred X bigger than the current

`[34:25]` **SPEAKER_01:** game, not even 50 X bigger than the current game. Everyone was very excited about alpha go.

`[34:29]` **SPEAKER_02:** And at the time in what was this? 2017, uh, 2016. Uh, everyone's very excited about this. And the important thing to pick up is that we did 800, uh, MCTS simulations and to cover 361 possible actions on average. So that gives us about two samples, roughly on an expectation for every single action. So here you need like 2 million of them for a similar depth for, for a similar depth. And then that's still to do a depth of 30. I would still have to do this times 30. This would be 60 million, uh, invocations of the model.

`[35:02]` **SPEAKER_02:** So that better be a small amount. Right. That's a lot. Um, so yeah, so that's to do a single action to be clear. Yeah, so exactly to do one action. So just imagine, uh, so why alpha go, uh, doesn't scale.

`[35:15]` **SPEAKER_?:** Yeah.

`[35:16]` **SPEAKER_02:** To me, there's one, uh, the carnality of the action space must be extremely small. If it's big, sad, uh, to the, um, I need a perfect, uh, deterministic environment, right? Like this, this, this. This doesn't change. The rules of this game don't change, but like the rules of the stock market change all the time. The rules to like venture change all the time. Like the real world changes quite often. So, uh, like, uh, homeless could ask this stick, uh, and real time. If you saw the movie, the documentary is such an amazing documentary.

`[35:59]` **SPEAKER_02:** I'd highly recommend it to anyone that watches it. Um, the guy is sitting there for like 60 seconds, maybe five minutes waiting for the computer to like decide. And, and it's kind of like. Imagine that we were driving a car and like, you took like 60 seconds to like turn the steering wheel. Everyone's dead. Like the whole car is dead. And so like, you know, uh, now let's talk about, uh, robotics and self-driving car. Um, and why this, why that approach kind of can't scale.

`[36:26]` **SPEAKER_01:** Yeah. I think the really good contrast here, because intuitively, uh, I think in thinking through this exact star layout, it actually really changed how I think about the kind of problem space of both of these two. So like. And let's take self-driving car as an example. This is one, you know, many people have started to experience for the first time, because we have some self-driving cars that actually work. You have Waymo and Tesla, FSD and whatnot that seem like they kind of work.

`[36:49]` **SPEAKER_01:** So like, let's maybe apply your same star framing here. Um, I would contend that the state space of self-driving car is enormous and it's actually not intuitive to me whether it's more or less large than this one. Right. I mean, in a sense, the chess and AlphaGo state space is already like more than a number of atoms. In the universe or something to that effect. Right. But like, just to emphasize that here, you know, you are considering, you know, surroundings, the vehicle state. Yep.

`[37:20]` **SPEAKER_01:** Uh, like, you know, camera, like weather, weather. I guess the point is like road conditions. It's like massive. This is massive. It is infinite. It's like, yeah. For all intents and purposes, it is infinite. Correct. Yeah.

`[37:34]` **SPEAKER_02:** Um, and, and so is the, uh, space of pixels. Like. Yeah. You know, like what can I put in an image? I can take a picture, an image of anything. Yes, true. Um, and so we're able to handle it and the same thing here where we compress from the board state, we don't represent the board state. We compress it with a calm net. So they have some deep, some, some, some deep calm net that actually takes this state and converts it into a latent. Right. And that latent compression is sufficient to kind of like do pattern matching, do, do some type of like symmetric, symmetric, uh, uh, equal variance kind of things.

`[38:09]` **SPEAKER_02:** And same thing with this and even better with JPA, which we can talk about at the end there, which is like basically taking some type of state space and doing all of our optimization in the latent space, which stable diffusion did, uh, that worked extremely well, which reduces our state space dramatically because I'm in some latent high dimensional space.

`[38:27]` **SPEAKER_01:** So like the, the, the key thing there is that, yeah, despite this state space being effectively infinite, we've actually gotten really good at compressing this. Yeah. And we'll, we'll talk more about some of the tricks for how we actually do this in practice here. But the TLDR is, you know, where there's like 10 years of deep learning work that basically makes us extremely good at compressing that very fast. Exactly. Right. Exactly. T seems to have a similar problem as before. Right. In fact, maybe even more extreme.

`[38:53]` **SPEAKER_01:** There's like infinity other variables around you. Right.

`[38:55]` **SPEAKER_02:** In some ways you'd think that it's, this is physics. Newton's laws, laws of motion should apply. If I turn the steering wheel like this and I hit the gas, I should be able to really easily model this. But what is non differentiable is that I have. If I'm going into a, a circle, right. It's like the most, the biggest issue that, that we, we faced in, when I was doing self-driving car is like, you were imposing your will onto maybe driving in India. I think you're imposing your will onto the environment and like people just kind of adapt naturally.

`[39:26]` **SPEAKER_02:** Like if you were doing Newton's law of motion, you were gonna, gonna collide. And so that the optimal policy, if you were doing strict Newtonians here would be like, don't move because anything you do, you're gonna crash, but it's not true like that. Then we wouldn't function. Like cars wouldn't go down the road. Um, and so you have to model the, the environment, you have to include other people in the environment and, uh, understand the embodiment of like how your action will change other people's actions.

`[39:51]` **SPEAKER_00:** YC's next batch is now taking applications, got a startup in you apply at ycombinator.com slash apply. It's never too early and filling out the app will level up your idea. Okay. Back to the video.

`[40:05]` **SPEAKER_01:** Now let's talk about the action space. You know, like one way to look at the. Action space is that it seems relatively small. It seems like, well, you know, you turn the steering wheel left to right. You hit the break, you hit the, you hit the gas. Doesn't seem that big, but like how big is it actually? Like, how do we actually represent these action spaces when it comes to a realistic self-driving car scenario?

`[40:23]` **SPEAKER_02:** Yeah, I, I don't know how they, how they do this nowadays. Um, they, they're doing a whole bunch of like bird's eye view, different things like that.

`[40:30]` **SPEAKER_01:** That's considered even just like a very simplified case.

`[40:32]` **SPEAKER_02:** But what, what do you have? You have a steering wheel that you can turn left, right. You have, uh, a brake pad. Yeah. And you have the gas. Yeah.

`[40:40]` **SPEAKER_01:** And so this thing is like 365 degrees. Yeah. So it's like a one to three 65, let's say zero to three 65. Yep. And you, let's just say you break this up into 10 different, uh, uh, severities. You're already, uh, even with just this oversimplified model, your action space cardinality is 365,000. So that's like a hundred X bigger than alpha. It's in fact, it's about the size of the example. It's in fact a decent amount smaller than the size we said, which is brake and CTS.

`[41:11]` **SPEAKER_02:** And so, yeah, so 36,000 action space is very large. And then even worse, unless you're Tesla, we have a bunch of video of people driving cars. We don't have video of like dash cams and like that. Like you actually don't have, again, only Tesla has this of the action as well. And so the things that you have access to that your trajectories are just like S T S T plus one S T plus two.

`[41:34]` **SPEAKER_01:** So there's a, you're saying there's a decent number of these. That's. Yeah. Some like dash cam footage on YouTube or something, but not really that many either. Yeah.

`[41:41]` **SPEAKER_02:** Relative. And so if you wanted to do a self-driving car and you didn't want to go spend a million dollars, trillion dollars on going, collecting all this data, then you want to leverage this data somehow. And this is going to be really applicable for, uh, robotics because we have a lot of, uh, videos of people doing things, right. Especially with egocentric. Like we, we have those videos, but we, what we don't have is the actions they take.

`[42:06]` **SPEAKER_01:** Yeah. Yeah. So this is like. This is, this is a sequence of what you're showing here, right? Unless you're Tesla, unless you're Tesla and Tesla has this.

`[42:14]` **SPEAKER_02:** So this is a huge competitive mode of like, what do people do in that state? And then so you can behavior clone to go from here to here, from here to here, go here to here, et cetera. But even then it's still very, very difficult. You have to, it's, it's not sufficient. People think that like, okay, I have this, we have a self-driving car, right? I mean, the amount of work that they're doing at FSD is like incredible and it's, it's not generally available. Like you can't, you know, it's not Waymo level, um, yet.

`[42:38]` **SPEAKER_01:** Would this be a good moment to briefly talk about model-free versus model-based RL? Yeah. I think that's an important distinction. That's going to be relevant when we talk about more world models. Yeah.

`[42:47]` **SPEAKER_02:** So this is a perfect point. Um, so model-free just means that my, my policy pie, uh, of a T given ST, uh, I have no world model involved. It's literally, it's literally doing what I said. I grab a bunch of these and I train go from S to a, S to a, just predict the next day. That's it. Yeah. And that's, and this is logical VLA. Yeah. Um, you know, this is like giving us pretty good results, it's behavior cloning, it's all the, the, the, the stuff that, uh, it's not getting us to Rosie the robot just yet, but, um,

`[43:18]` **SPEAKER_01:** in many ways, it's the closest thing that just looks like the next token prediction from LLMs that seems to scale pretty well with natural language. I mean, it's like, it's not exactly the same thing, cuz there's no action exactly, but picking a token is not exactly the same thing, but it's very analogous to that basic thing.

`[43:32]` **SPEAKER_02:** I basically take away the tokenizer head and I give it an action space and I collect a bunch of tele ops data. You know, like this as, as the self-driving car does in Tesla, and I just taken the, the state, which is some image and, or maybe sequence of images, and then I'll output some action and that's it. Cool. And this is, let's say model three, cuz I don't have a model for the environment. And then now if I do model based RL, I have not just some PI, but I have also my, uh, size as well here.

`[44:10]` **SPEAKER_02:** Right. Yeah. And so, uh, by, uh, by including this, I can have a much stronger policy, but it would take a lot more time to perform inference because I have to do this full test time planning.

`[44:22]` **SPEAKER_01:** Just to remind us that size referring to this specific transition function, right? It's referring to this. You're saying this is specifically referring to, um, a function of ST plus one given ST and action T yes. So it's like your ability to predict the next state you'll be in. Yep. Is, is the crux of it. Yep. As opposed to just directly predicting the actions.

`[44:45]` **SPEAKER_02:** Yeah. And the main thing that I believe is that this is required for AGI. This is what the, the human brain is, is at least in the way the human brain does it. Yeah. And, and let me go further in saying that, like, if you look at the, um, billions of years of evolution, basically there's this thing called 10 million, 10 million years ago called the great cortical expansion, which you see the size of a brain just explode, get bigger, bigger, bigger, exponentially up until us. And it basically stops.

`[45:14]` **SPEAKER_02:** And if the entire point of the neocortex is world modeling, what happened is we started from VLAs. This would be like ants or fish. Yeah. Right. Just like very, like, you know, lizard brain, whatever you want to call it. And then we developed this neocortex to like, you know, go from our, our motor cortex to actually simulate what's going to happen. And that makes us just so much smarter. And then we, once we get those samples, we can compress it when we sleep or otherwise. With this hippocampal shortwave ripple, whatever you want to call it.

`[45:44]` **SPEAKER_02:** And then that helps us, uh, develop a better policy. And that marriage between the two is, is not only helps us, um, train on hallucinated, uh, examples, but it also allows us to test time plan.

`[45:57]` **SPEAKER_?:** Right.

`[45:58]` **SPEAKER_01:** I guess the, the kind of extreme case then of self-driving car is kind of general robotics, right? So if you're, if you're like a humanoid company, like figure or pie or whatever, again, same S T A R. Yeah. I guess the gist of it is that a is now even bigger, right? It is like, I guess a very simple robot would be, yeah. How would you, how would you play action space? Like, let's like, let's take a very basic one.

`[46:21]` **SPEAKER_02:** If I take like my six axis, uh, arm as your standard here that we're actually working on right now in Stanford robotics center, um, you have two degrees of freedom, two degrees of freedom, two degrees of freedom. Uh, and then you have another two for the end effector, right? And so that's a simple end effector, not even like a, not even like a one axis, like, yeah. You know, we, you can rotate, but you have the, the, the, the one axis Yumi style, uh, thing. So this is eight. So you have 16 degrees of freedom.

`[46:49]` **SPEAKER_02:** And let's just say that you do the suit three 65, two by 10 or whatever, you know, kind of thing. I mean, it's like 10 to the 16th. It's like insane. It's like, yeah, it's an insane number. Um, and so much bigger than self-driving car, um, and even worse, like getting tele ops data is extremely painful and expensive. It's not just like, oh, we'll just get some people. The Philippines will give them like some, you know, things or whatever is like totally, totally doesn't work.

`[47:15]` **SPEAKER_01:** And nor is there yet something like, uh, Tesla's fleet where there are cars deployed that people are just using. And they're not even necessarily realizing that every time they turn the steering wheel, they're providing this, this data set for Tesla.

`[47:29]` **SPEAKER_02:** And then even worse, you have this like what's called cross embodiment gap. And so if I were to like train this policy on Tesla model X. And I were to like, put up. On a Tesla model three, it wouldn't work. No, like it totally wouldn't work. Like all the, so much, so much of this, uh, the, the way that if, if I were to break on a model three versus a model X, the model X weighs more, it has different dynamics, aerodynamics, and things like that. And so what's actually gonna happen is very different.

`[47:59]` **SPEAKER_02:** Like the, the degradation you have across cross or across embodiments is very, very, very strong.

`[48:04]` **SPEAKER_01:** And clearly Tesla's figured various ways to get around that. I mean, they, they have these that roll up, but actually even with Tesla's new FSD today. They don't roll out in all the cars at the same time, probably for more or less that reason. And in this case, it's even harder now. I mean, you have bigger differences between embodiments than a model three versus Y and you have way bigger action spaces. You have to sum up model. Yeah.

`[48:23]` **SPEAKER_02:** Uh, Lane McIntosh, I played hockey with at, at Stanford, uh, who now runs Tesla FSD. Um, I can ask him, but I would bet money that they shard the data per model per, uh, car type. Yeah. Wouldn't be surprised. I, I just, cause that's what I would do. There's no way that like, you know, I, I would try. Trust, you know, data that was collected on a model X on a model three, I just wouldn't, no way I would trust it.

`[48:46]` **SPEAKER_01:** Okay. So now that we understand the basic setup here and why the action space problem is so big, why don't we talk a little bit about how world models actually fit into this? You know, maybe first, you know, I guess what didn't work about the naive world models and how do we fix those? And then let's kind of talk about some of the newest world modeling techniques. Cool.

`[49:02]` **SPEAKER_02:** So like in robotics in particular, it's very hard to get these, this kind of trajectories that you want, that you kind of need to train for your VLA is, and people. Spend up, you know, uh, with a whole bunch of tele ops data. It's very expensive, very expensive. Ideally, what we would do is take like data like this from someone who is just like puts a camera on them and just like making sushi. Okay. Like I want to make a sushi robot. Um, how do I do it? Give it to all the sushi chefs.

`[49:27]` **SPEAKER_01:** Don't put anything in their hands and just have them start cutting up sushi and making sushi. And ideally we would train it in that way. You were describing of like, somehow we would train a model just on these two and then later add this afterwards.

`[49:38]` **SPEAKER_02:** And so the first real person. That, um, you know, went after this was Juergen Smidhuber, uh, please, uh, so, so he doesn't yell at us. We have to, we have to make sure we cite him. Uh, but he has this really cool paper called world models, uh, very aptly named. And it's basically, he took these like, um, open AI gym, classic, uh, games, car racing, and I think doom as well. And then just like trained a model at that time was like an RNN. Um, he had some funky, uh, uh, zero order stuff in there.

`[50:10]` **SPEAKER_02:** Um, he had some funky, uh, zero order stuff in there. But basically the key premise was I can take an environment. I can extract a whole bunch of this type of data off of it. I think he actually does actually this data, but we'll get into dreamer where he does it in this paper in this way. And then, uh, trains a policy on only the, uh, the, the synthetic data, the imaginative, uh, rollouts, and it actually performs well in the environment. This is the first time in my understanding that that actually happened.

`[50:40]` **SPEAKER_02:** And it actually works really well.

`[50:41]` **SPEAKER_01:** And then, so the key thing there, you can basically use this. If you have some predictive model of this, in that case, and eventually of this, you can use that as basically a synthetic training set to train your policy model and then basically fine tune it on real data later. Exactly.

`[50:55]` **SPEAKER_02:** And which is just like a really powerful idea, especially since in robotics, the limiting step is access to large amounts of state action data. And so now the dreamer series. So basically this published publishes in. May of 2018. Yeah. Uh, Dan is jar, uh, Hafner publishes dreamer one, I think in November of 2018, and then now he's been on this rampage for the last seven years, publishing these papers and dreamer V4, I think is the capstone of it, um, where he basically does the same thing and he focuses on Minecraft, um, and he trains these, a world, a world model on this type of data and then injects action conditioning on a very small amount of data.

`[51:39]` **SPEAKER_02:** Yeah. Yeah. To get to this type of world model that can, that has the action conditioning as well, and then samples a lot from it. And then trains a policy on those synthetic, uh, imaginative rollouts. And it's the policy is so good that it's the first paper to mine diamonds in Minecraft. I'm not a big Minecraft player, but apparently that's extremely difficult. That's like next level difficulty. And it did it all on synthetic data, which is kind of crazy.

`[52:05]` **SPEAKER_01:** And the key unlock there. Yeah. Use synthetic data specifically on a model trained. On just this sort of state transition type of thing. Yes. And this ends up being very convenient because it turns out we, as a society have a lot of this. Exactly. Yeah. All of YouTube, right.

`[52:20]` **SPEAKER_02:** He does do a very small amount of data from app for, to enable the action conditioning and that get, that allows you to do this full, uh, simulated rollout. But yeah, it's true. So we have, we have YouTube, we have like Flickr, we have all these data sets online of like, you know, people doing things we'd like to use it. And no one has really. Really gotten that to work. And then now that with this, um, these like video generated generation models, we can take that data, create a world model out of it, add action conditioning, post-train it with action conditioning for some new task.

`[52:53]` **SPEAKER_02:** That is we want it to do chopping down wood or, uh, you know, um, making sushi or folding my bed or whatever it is only a few amount of examples. And then we can train a policy on this, in this neural, uh, simulation.

`[53:08]` **SPEAKER_01:** Yeah. And you know, we put. And you know, we put out a video, um, about diffusion models very recently in flow matching. I imagine that now ties very closely to this, right? Ultimately the, the kind of current state of the art best way to do this on basically infinity data that we have available and can keep generating is using state of the art video diffusion slash flow matching.

`[53:26]` **SPEAKER_02:** Exactly. Yeah. So like if you have your, your C dance or your Sora or whatever, exactly all those models. Like basically the idea is now we have them and they're already trained and they're great. Let's. small amount of action conditioning on them to get to this, uh, this world model. And then we can sample from it a bunch and then train. And this is exactly what wave, uh, did with Gaia and Gaia. I think they raised $1.5 billion to, to basically run with this idea for self-driving car.

`[53:55]` **SPEAKER_02:** Um, I think a bunch of companies, um, Nvidia, uh, uh, this, this paper here, uh, is basically talking about doing exactly the same, this dream zero for robotics.

`[54:06]` **SPEAKER_01:** Um, and what I thought was really cool about this paper is that the, yeah, they do exactly this process where they have this, um, joint model of, um, state transitions and actions. They train it by first instantiating it with the open source one video diffusion model. And then it only takes them about 500 hours of teleop data, which is basically exactly this right to get it to be pretty good. And they have a lot of clever tricks that allowed it to be cross embodiment and working on scene tasks with relatively small amounts of data.

`[54:34]` **SPEAKER_01:** Right. So they're taking basically the exact concept, I believe from the dreamer paper and applying it specifically to these robot embodiments. Exactly. Um, and it, and it turns out it actually works, uh, actually better than I would've anticipated it to work.

`[54:46]` **SPEAKER_02:** Right. Yeah. So I think that this is basically the, the, the path to, it was the path, I believe the path to get humans, uh, to be as good as we are genetically over the last 10, 20 million years of evolution, a bigger world model helps, uh, for training and for, uh, test time planning.

`[55:05]` **SPEAKER_01:** Um, and I think it'll be the same thing as true as for, for robotics. What's also cool is there's a bunch of applications of this, the things outside of robotics too. I mean, there was a weather planning paper, for example, we were reading this gen cast paper, which I think applies a relatively similar concept, um, in terms of how they model, you know, literally the world, the world's weather, um, with something like this.

`[55:27]` **SPEAKER_02:** Yeah. We have to talk about the world model for the world. Um, yeah. So basically they do this exact same thing where, you know, the key unlocks. Yeah. Yeah. Yeah. The key unlocks for this whole thing was getting diffusion to work in very high dimensional state spaces. Like we talked about in the last, uh, lecture and then learning to, to use that to con action condition in the way that he's done. But they did this for the entire world with this exact same diffusion steps, which go from some, and they go back to, uh, two time steps lag of, of order to AR two for the set

`[55:59]` **SPEAKER_02:** of sessions there. And then basically predict the next, uh, state of the world based on the, those things with this Lingam and diffusion rollouts. Yeah. My, my big assertion is that, um, it was necessary for the human brain to develop world modeling. I actually just saw this paper that I wanted to make sure to call out that that was so great, uh, out of, uh, university of Washington, where they say explicitly in the, in the abstract, each cortical area estimates both latent sensory states and actions, and the cortex as a whole

`[56:32]` **SPEAKER_02:** predicts the consequences of those actions. Yeah. That sounds like a world model to me.

`[56:37]` **SPEAKER_01:** Yeah. Right. Um, it's actually describing exactly these two equations here where we're estimating both the sensory latent states and actions. I mean, I guess it's really the joint model that we showed earlier is what he's describing here. It's exactly this, this equation is showing.

`[56:52]` **SPEAKER_02:** Yeah, exactly. Right. And so, uh, if it works in us, it should work in robotics. Um, and I think that that takes us the rest of the distance.

`[56:59]` **SPEAKER_01:** Why don't we talk briefly about latent world models, especially the con the JEPA concept? Cause I think there's been a number of papers that use JEPA as an element of their, I guess, architecture. Why don't we just briefly introduce JEPA and how it fits into the current landscape of world modeling?

`[57:15]` **SPEAKER_02:** Yeah. In classic RL, you'll have like, you know, if you do study Q learning, for example, you basically keep this matrix called the Q matrix and it's going to be, uh, S by a. And so I have this, um, S by a states and actions and each one I need, you know, some, you know, a set of values. And I'm going to do a little bit of math. So let's just say I take the amount of counts of being in this state action. Uh, and I take the average value of being, of taking that action in this state. Yes.

`[57:45]` **SPEAKER_02:** And that's my Q value there. And it's a little bit more complicated than that. There's Bellman equation, all this backup, all this stuff like that. But so this scales horribly because as the cardinality of my space space gets bigger and my kind of action space gets bigger stuff, I don't have enough time. I become less and less sample efficient. Correct.

`[58:01]` **SPEAKER_01:** Right. Yeah. And so it's like, yeah, it's this whole thing we described earlier, right? It's absolutely massive because it has all of these elements in it couldn't really enumerate a huge grid.

`[58:10]` **SPEAKER_02:** And so the classic trick, I mean, since I took, you know, uh, C it's two 29 with Andrew wrong in 2012 is you do this, take a neural network on it. Exactly. And you basically are just going to compress that state into some lower dimensional state space. This is actually predates deep learning. Uh, we were doing stuff like this. Um, I think my first paper was basically doing something like this, uh, basically turning like a grid. Uh, into like a bunch of like pyramids and like, and, and the state was how much I'm

`[58:38]` **SPEAKER_02:** in pyramid one or pyramid two or whatever, but anyway, the neural network can just do this. And so basically what, uh, the, the key idea in JPA, if I have, um, an image one and I have image two and I have image three, I can do my, my world modeling, uh, my, my world modeling of ST plus one, uh, given ST and 80. So what I'm going to do is I'm going to, like, I'm gonna get an image from the C plus one and I'm going to place it in pixel space and have, this is, uh, let's say at time t t plus

`[59:19]` **SPEAKER_02:** one t plus two, et cetera, et cetera. And I have to actually predict now the full, uh, image that's extremely expensive from a computation standpoint. And also from like a sample efficiency, standpoint. Yeah. What I can do instead is put this through some. ComNet encoder, encoder. have a latent for t plus one of a latent for z t plus two and then i'll have from this from zt i want to predict z t plus one hat and my goal is to make this and this uh make my loss function will be something very simple like i want to minimize this that's it now this doesn't work

`[60:03]` **SPEAKER_02:** this collapses hard and so what happens like is basically just if you if you just predict zero just output zeros which the model will learn to do and i'm actually incorporating this into my current research right now um and so what you need to do is something called sig reg or uh this is one technique vic reg is another where basically i add this another term that basically says uh i want the um over a large enough batch size i want the the the distribution of z t plus one to follow a gaussian you know it's kind of like a normalized it like

`[60:40]` **SPEAKER_02:** a like a batch norm type of yeah of track i mean not in the same and and if if it's zero it can't be this yeah right because then this is non-zero and so maybe i think that there's probably this or something like that but basically this prevents it from modal collapse and it makes it do something good and this is the most recent paper for the audience is le wm le world model which is super super great um however to be completely frank the this this is self-supervised learning super great it doesn't work that well

`[61:10]` **SPEAKER_02:** if you were to not do uh these techniques and there's there's a bunch of other techniques that you can do uh it will actually outperform much better and that are let's say for example um if i'm going to do an llm and you have like you know francois uh likes sushi which is definitely true um and i tokenize this into a bunch of different different tokens here and this is token id 6 19 28 whatever and i look up the encoding into this and that's going to be uh e1 yes e2 e3 etc um what you can actually do is have the llm output

`[61:56]` **SPEAKER_02:** uh what the lm will take in taking these things and will output um the the next token and so it would be like let's call it h uh this would be the low jets coming out of it t plus one and what you can do is actually have this be close to e t plus one and a lot of people are playing with this idea and getting rid of the cross entropy loss entirely and so if you were to do this it actually is a proxy for the cross entropy loss and there is no cross entropy loss and the cross entropy head is actually very expensive yeah and so this is very cheap and like this lady just

`[62:37]` **SPEAKER_02:** so people are playing around with this idea um and as a basically as a cheaper proxy for the cross-country loss so there's lots of different ideas on basically uh taking this jpa idea to not just pixels but to lns as well yeah interesting yeah so just to define what jp is it's joint

`[62:56]` **SPEAKER_01:** embedding predictive architecture i think one of the things i find uh cool about this jp idea is it feels like an idea we see over and over in deep learning but there's a version of this idea that's basically the staple diffuse layer of this idea that's basically the staple diffuse layer of the fusion idea. There's a version of this idea that in my company training graph convolutional neural networks to design drugs we use to do latent variable generation, for example. And it's an idea that comes back over and over and then has this various tricks that

`[63:22]` **SPEAKER_01:** it actually takes to get it to work in practice. Okay, now we have a pretty good sense for how world models work. We have a pretty good sense for what the state of the art looks like. If we trust this paper, and it seems like these kind of work on robots too. This paper is only from the end of last year, this year, and it seems like they have various methods that allow you to train on relatively small amounts of data that's tractable and pre-trained on data diffusion models. So are we good? Or does it all work?

`[63:48]` **SPEAKER_02:** We're done. Yeah, this is 2016. And 2016 will be the year of the robot. We're going to have the robot in your house. Yeah, no, I don't think so.

`[63:58]` **SPEAKER_01:** What are one or two, because there's lots of open problems remaining, what are a few open problems maybe we can...

`[64:03]` **SPEAKER_02:** Yeah, so I think the first one is that pins doesn't really work. What is pins? Physics informed neural networks. So pins doesn't really work. This is physics informed neural networks. And so basically, if like almost all of the self-driving car data looks like this, the car is driving down the road. And let's just say, for example, I have, you know, a house here, and I want to train the model on, you know, not driving into the house. And so let's say I put, I put it into a state right here to drive into the house. What's going to happen is because almost

`[64:49]` **SPEAKER_02:** all the data is like, looks like this, driving down the road, this will just turn magically into like a highway. And I'm just like, boo, just don't worry. It basically needs like a ton of data not

`[64:59]` **SPEAKER_01:** to do that either from simulation for that to not happen. In fact, I actually don't even know if

`[65:04]` **SPEAKER_02:** because of the data, I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work. I don't know if it's going to work. So there's no data distribution. There's no data here. There's almost all the data here. And like when you're training a neural network, it has a tendency to collapse if you don't keep the mini, mini batch composition, like very even over the, you know, over the class space or whatever you

`[65:22]` **SPEAKER_02:** want to want to call it. But like, you'd have to train on, you have to be very careful about your data mixing to make sure you get this right to solve this problem that no one really has. But even then, the if you take just a simple thing like this, this is like the conic example. And I have some sine wave. And I want and I have these as my x and I have these as my y. So this is complete interpolation. No, that's maybe messes up. But why like this? No, we can't get to like, machine precision. They can't what is what is it one a

`[66:02]` **SPEAKER_02:** minus 16 or whatever it is. We can't we, the SGD will not get to zero, effectively zero. So we'll always get zero. So we'll always get zero. So we'll always get zero. So we'll always get zero. So we'll always get have some residual and for us to be like a really good world model to simulate body interactions like to simulate this what's going to happen when i do this and like let's say that i'm trying to be lebron james like there's like i saw this one video of um steph curry dribbling about a basketball on

`[66:25]` **SPEAKER_02:** a court and he just felt that there was a dead spot in the court and he because he's so good and he knows exactly the physics of what's going to happen if i hit this you know the ball with this force like the ball is going to come back exactly this spot and it just didn't and he knew it wasn't him it was the the court and he found a dead spot in the court like that's how good the the human brain is at world modeling in my opinion i think it's an sgd issue i think it's probably an architecture issue i think sam altman just kind of came and just said that he thinks that there's

`[66:54]` **SPEAKER_02:** definitely an architecture that's going to be more performant than the transformer i think he's right um i think the the transformer doesn't do compression uh uh in the time domain at all it just keeps running everything um so anyway so i think that the getting higher fidelity in the world model is extremely important one i think two seems like test time probably is going to be a big thing like adaptation exactly test time planning we how quickly the human brain can you know in times of

`[67:25]` **SPEAKER_02:** in sports and things like that when you're playing tennis i think you're a tennis player like how quickly we can adapt to what a player is doing and things like that we're not going to sleep and like retraining we're very quick to adapt to a new new environment it's like the out of distribution prediction exactly really challenging and like one little data point we can like quickly adapt to that new thing and change um i think there's been a lot of papers uh uh on like basically estimating the friction coefficients and so like those can change over time if you go

`[67:54]` **SPEAKER_02:** to a human environment or not for example like this this friction might change and that's important in control um and so you need to estimate that very quickly and adapt and that these models

`[68:04]` **SPEAKER_01:** don't have a mechanism to do it yeah and then i guess there's like those practical speed elements of these right a lot of these are doing some sort of expensive planning step and we're doing some sort of like uh we're kind of hacking around it with this retraining process and synthetic data but even so like to really get maximum performance right now you'd want to do something that's closer to like the alpha go style

`[68:29]` **SPEAKER_02:** rollout and that's extremely slow right the mcts process which can't happen um the other thing i'm gonna say is that like the the thing that that is pretty crazy about the way that the brain works is that like everything is kind of running autonomously and so like you'll you might be like in the middle of saying sentence one and be like oh actually no something else and so like what does happen there it's like type one and type two thinking are happening at the same time in some way and so like there's definitely uh you know some um really cool mix of these like

`[68:58]` **SPEAKER_02:** heterogeneous models and like some are overriding others and like taking control of the motor cortex and like commanding the body to do a thing you know okay but on the flip side now we um talked

`[69:10]` **SPEAKER_01:** in the past video about the squint test and how we felt that autoregressive llms maybe don't pass the squint test why don't we reintroduce what the squint test was for a second and then maybe let's think about whether this passes the squint test despite all those limitations yeah and this one

`[69:24]` **SPEAKER_02:** test for me i think is like um this comes from the yan lakoon uh we didn't need uh flapping wings to achieve flight um and to that i say well we did need two wings and like if i squint and i look at a bird and i squint and i look at a plane i'm like yeah it's kind of similar it looks right um similarly if i squint i look at the human brain and i squint and i look at all these these world models we have like this vla this action policy and that they're doing test time planning together and things like that it's getting really close

`[69:53]` **SPEAKER_01:** it's much much closer it seems closer than an autoregressive llm and that's like this concept of a world model of you know implicitly predicting future states and actions feels and we're thinking about things like that because we're thinking about like what we're

`[70:09]` **SPEAKER_02:** doing and it seems like there's some you know neuroscience evidence yeah i mean i'm i'm getting to the conclusion that i think that the brain is the optimizer not the model and that the brain emits like has models that it invokes but the brain is somehow also the optimizer itself and so in that way it doesn't pass the squint um because like you know something magical is happening when you're sleeping there's no intelligent species that we're aware of that have dolphins all those stuff elephants they all sleep there's some reason for that and that seems like a

`[70:39]` **SPEAKER_02:** really thing about like the evolutionary re like recourse of sleeping like you get eaten when you sleep so like for the benefit of sleeping should be so so much better to outperform that so i think we don't have this idea of awake sleep uh in our current um architecture but i can imagine i'm like simulating you know you know compressed from the hippocampus some like experience in the day i'm like training on more of those examples right you're like collecting a whole bunch of

`[71:05]` **SPEAKER_01:** these experience rollouts and then you're updating your your policy function there's got to be something

`[71:11]` **SPEAKER_02:** like like there's this thing called shortwave ripple where like the hippocampus when you're sleeping like emits these uh spike trains that are actually reversed from when they actually happen back in through the both both the hemispheres and for like seven times and then it like stops so like there's something happening there that's very uh uh training something yeah and if you don't sleep then you don't up you don't have long-term memory right right and so like there's definitely a reason why we're

`[71:36]` **SPEAKER_02:** training uh things that happened uh into our brain so where does that put us now we have all this

`[71:42]` **SPEAKER_01:** work happening with world models how should we think about what's coming ahead in these next

`[71:45]` **SPEAKER_02:** few years in the research community yeah i think that like we're going to see a lot more uh of these world models in robotic policies i think that's going to unlock probably full self-driving would be like a one of those examples that they can get the real-timeness of it it seems like that's coming probably solve it with more compute to like have parallel things and you probably don't need it for like most standard things maybe like you know getting out of weird parking jams and like

`[72:10]` **SPEAKER_02:** things like that would take us some time similar to the rose of the robot which we've always wanted to have a rose of the robot to like you know clean up my room for me um i think that like this feels like we're getting to good enough that we can pay up for data and compute to get to rose of the robot it does feel like that it'll be expensive to collect the data and do the dreamer sequence of going from state to state and then getting the action conditioning to work but like

`[72:37]` **SPEAKER_01:** i feel like it should work yeah i mean what's pretty cool is we see a lot of companies at yc working at every step of this from the collecting egocentric data collecting uh the teleop data training their own world models and action models um building new embodiments and then making ways of adapting those embodiments and feels like this is the first year where you see demos where you're like okay this actually like kind of is starting to look like it's going

`[73:01]` **SPEAKER_02:** somewhere yeah and it seems like a very exciting year yeah so anyway i think that there are real ai problems to solve still we talked about pins we talked about the real time issues and then on the robotic side there's real issue like it's amazing how effective our epidermis is in terms of we we can detect tactile oh epidermis yeah epidermis are tactile we can detect shear force we can detect temperature and it's everywhere yeah and so like versus you know like the we get like one little sensor that only does tactile we don't have the the friction component we don't have

`[73:36]` **SPEAKER_02:** temperature we don't have all these the feeling we can't estimate coefficient of friction very quickly i can touch something and say oh this is smooth this is rough it doesn't we don't have any of that and if i numb your hands i actually had this experience um just recently if i numb your hands like you actually can't tie your shoes yeah so you can't perform control and so like yeah if you like you know uh uh if you train enough um on enough human data tying your laces you can do it with no feedback maybe maybe but like how much would you need if you did actually

`[74:07]` **SPEAKER_02:** have the human like touch like i think it'd be so much easier yeah well there's a lot of more

`[74:12]` **SPEAKER_01:** research to do then yeah yeah Francois thanks so much for joining us thanks so much for watching everyone we'll be back for the next episode of Decoded
