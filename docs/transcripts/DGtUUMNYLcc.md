# 全文转录 · 递归:AI 的下一条 Scaling Law

> ▶ [YouTube](https://www.youtube.com/watch?v=DGtUUMNYLcc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/DGtUUMNYLcc.md) &nbsp;·&nbsp; Recursion Is The Next Scaling Law In AI
>
> 🗣️ 说话人分离识别到 **2** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_00:** Welcome back to another episode of Decoded. Today, I'm back with YC visiting partner, Francois Chaubard, to talk about one of the most interesting recent trends in AI research, recursion. Specifically, we're going to talk about how we can improve a model's reasoning performance by using recursion at inference time, rather than by just making the model bigger and bigger. There were two papers that made the power of this approach really clear in 2025. One on hierarchical reasoning models, or HRM, and another on tiny recursive models, TRM.

`[00:28]` **SPEAKER_00:** Francois, thanks for joining us. Can you tell us a little bit about these two models, and what was so interesting about them?

`[00:42]` **SPEAKER_01:** Sure. I guess to set up a little bit of a foundation, you already did an amazing lecture on RNNs and LLMs in one of the previous videos, so I won't overdo it, but just to give the cliff notes, an RNN is just a model that you recursively call again and again and again on itself, and we were very much in the belief that this was required to get to the point where we could do this. So we went to AGI peak RNN use, which was probably until 2016, with Alex Graves' keynote, which is just fantastic, and all his adaptive compute time work.

`[01:15]` **SPEAKER_00:** So this is about 10 years ago, people were working on these models. This was in the era of LSTMs and LSTMs with attention.

`[01:21]` **SPEAKER_01:** Yeah, and depending which professors you talk to, before attention was invented.

`[01:25]` **SPEAKER_00:** Yes, yes, totally.

`[01:28]` **SPEAKER_01:** And I think what really was the limiting step on RNNs in general was this thing called backprop. Backprop is where you have to, you roll out the model, and then to update the weights, you need to approximate the gradient, and you step back, back, back, and you keep rolling out. And as the model gets bigger and bigger, and as you roll out for more and more steps, then you have all these accumulation of errors, and the gradient gets noisier and noisier, and then it just kind of stops to work.

`[01:54]` **SPEAKER_00:** Yeah, so you have these vanishing or exploding gradient problems, and it's because if you have an input with 20 steps, you're multiplying these matrices 20 times, and that causes training.

`[02:01]` **SPEAKER_01:** And we're talking about doing context length of a million or a billion, and so it's not even just 20, it's like a billion. And even worse, you have to retain the activations at every single step. And so if this were happening in your brain, you would need a million copies of your brain at every single activation so that I can backprop through it. There's tricks around this that you can do, and you can do a gradient checkpointing and things like that to reduce that issue, but then you're just trading off memory for wall clock time and compute.

`[02:29]` **SPEAKER_00:** Right, so now if you contrast that with LLMs, the ones that people are widely using, these, while at face value they appear to be similar, at training time, they're doing basically this one-shot feedforward process for every input, right? The LLM, the transformer block, can take all of the inputs in parallel. It's not actually iteratively going over them one at a time at train time, so you don't have this needing to store tons of activations problem or this giant vanishing gradients problem with them.

`[02:55]` **SPEAKER_01:** Yeah, exactly. Like, it's actually all happening in time in one shot, magically. And that was like the trill or lower triangle trick, that kind of thing. Yeah. And that's what happens, this causal mask that occurs. And so you actually do all time steps in one shot, and you forward pass a feedforward model on all time steps in one shot, and you backwards in one shot, and it's amazing for train time in terms of like wall clock. It requires a lot of flops, and it still requires a lot of the memory.

`[03:23]` **SPEAKER_01:** You still need it there, but you don't have the vanishing gradient issue. And what you actually paid for that you have to give up is this latent reasoning thing and this compression in the time direction. There is no compression in LLMs. Every single decode that I do, I still have to retain the entire, you know, Shakespeare novel just to like decode a little bit, and in RNNs, you don't have to do that. It's all compressed in this hidden state that you kind of roll out.

`[03:46]` **SPEAKER_00:** Okay, so let's talk about that in a little bit more detail. Like, you refer to this inherent reasoning ability. You know, many people think about LLMs as doing reasoning, and we're going to talk about that a little bit later, but help me understand where you see the biggest limitations in LLMs reasoning ability. Or is in terms of what the model does in an actual forward pass.

`[04:08]` **SPEAKER_01:** Yeah, and so I guess we go back to chat GPT-2. GPT-2 was this landmark architecture and paper that basically was just get next token, next token, next token, and it kind of worked. And like we just watched val loss go down, perplexity goes down, like the model just is more performant, looks better, starts to make some Shakespeare that actually sounds somewhat plausible. Right. And then we have to get these things to reason. And to actually solve some really hard problems. And I've done extensive experiments on this, but like if you take, for example, sort.

`[04:42]` **SPEAKER_01:** You have infinite amounts of unsorted lists and you give it sorted lists. You keep feeding it to the model, it should work, right? It's actually impossible for the model to map from unsorted list to sorted list. If I have a- In a one-shot basically. In a one-shot basis. It's like literally that we know a theoretical lower bound that for comparison sort, you can't do better than n log n. Steps. And if I have a list that's 31 characters or elements long, and my transformer is 30, I run out of steps to do comparisons.

`[05:16]` **SPEAKER_01:** It's not possible for me to do all the steps that is needed to be done. In HRM and TRM, they use Sudoku as an incompressible problem. Similarly, and so are mazes, those are incompressible problems. Rolling sum, incompressible problem.

`[05:29]` **SPEAKER_00:** So when you mentioned the sorting algorithm, when I think back to my algorithms class from college, the one way you could get faster than n log n in a sorting algorithm is if you had some access to an external memory cache. If you had some tape you could write to, then you can actually do faster than n log n by basically selectively putting things onto this memory. And I suspect that's a key limitation of these LLMs in that because there's no external memory tape in-built into the model, you lose certain performance possibilities in terms of how

`[05:56]` **SPEAKER_00:** fast you can go.

`[05:57]` **SPEAKER_01:** That's right. And so I guess rate of sort would be the most common one, depending on the number of buckets that you have. You can kind of get from n log n to order n. You can't get less than n. You have to touch all the elements. Sorry, you have to do that. And if you run out of layers and transformer layers in your neural network, then you ran out of chances to do that.

`[06:20]` **SPEAKER_00:** So this is just like going back to like Alan Turing now and like a Turing machine, right? So what's the analogy there exactly that we should think about in terms of LLMs, I guess, not quite satisfying how you think about a Turing machine?

`[06:30]` **SPEAKER_01:** Yeah. So let's just talk about like chat-GBT2. GBT2. GBT2, the original, like no bells and whistles, it's just a feed-forward model. And so it's just forward passing one step and taking an input, creating a bunch of outputs. In the Sudoku case, if I have 50 different squares, and it's provable that I can only do one given this information, and I have this many layers, then that's all I can do. And the cheat is the chain of thought. And so it's completely true that at test time. They are Turing complete, and you can simulate all Turing computable functions at test time.

`[07:09]` **SPEAKER_01:** But how do you get it to learn it? You need to train it. And that's where, unless you're training it on human-labeled traces, for which there's a lot of problems like the millennial prize problem, we don't have the trace for it. Right.

`[07:21]` **SPEAKER_00:** So we'd love to have the trace for it, just doesn't exist. Totally. Makes sense. Okay. So with that context in mind now, let's talk about these two papers, because I think that sets up a lot of the contrast we're going to draw between these papers. Yeah. Yeah. And the models that people are maybe more used to. So let's talk about HRMs first. Walk me through a little bit about how this model works and some of the intuition behind

`[07:42]` **SPEAKER_01:** it. Sure. So this is directly in the lineage of RNNs. There's not that much novel from the RNN standpoint, at least in my opinion. They do have this idea of, inspired by the brain, where I have, there's different parts of the brain that operate at different frequencies. So some that operate at a really high frequency, which is then the low level of the hierarchy. Some that operate in a really low frequency, which is the higher level of the hierarchy. And the interplay between those things is really interesting.

`[08:13]` **SPEAKER_00:** So this is like literally in the human brain, there's some bio-inspiration here, which is that you have different waves running at different frequencies at different parts of the brain or something like that.

`[08:22]` **SPEAKER_01:** Yeah. And I guess that's one interpretation of it, of the way that they're talking about classifying these hierarchies of frequencies. Yeah. But the most interesting part, at least for me, is the way that they train the neural network. You take in some X, some input, whether it's a incomplete Sudoku puzzle, a maze, or an art prize challenge, you do TL steps with the lower level module, then you do, to go to H, you do that TH times. And then you have N sup outer refinement. Yeah.

`[09:02]` **SPEAKER_00:** So you basically are like running through the input with a given matrix, with a given transformation repeatedly on it. And you're doing that through two levels of refinement, and then basically running that process several times.

`[09:15]` **SPEAKER_01:** Yes. So there's exactly three levels of recursion occurring here. There's the low level, there's the high level, and then there's the outer refinement steps.

`[09:22]` **SPEAKER_00:** And we're calling it recursion because it's the same weights that are being applied repeatedly. We're not changing the weights in between these steps.

`[09:28]` **SPEAKER_01:** Exactly right. You get to recurse on the L net. TL times. You've recursed on the TH and the TL, this looped recursion, TH times, and then you do N sup, you do this whole outer refinement step, N sup times.

`[09:41]` **SPEAKER_00:** Cool. And so what's the basic intuition for why that works? Like why does that produce an effective paper result, and what even were the results that this paper showed?

`[09:50]` **SPEAKER_01:** Yeah. And so, I mean, this got state of the art on ArtPrize 1 and 2, this was only a 27 million parameter model. Okay. Yeah.

`[10:02]` **SPEAKER_00:** And so it's like a thousand inputs or something like that, like puzzles, basically.

`[10:06]` **SPEAKER_01:** Yeah. There's literally a thousand tasks, which is extremely small. There is no pre-training at all. This starts from like literally tabula rasa weights, and it can outperform at that time if we go back. You know, we had O3, if you remember back, way back when, and O3 gets zero, literally zero. And this got like something like 70% on ArtPrize 1 at least at the time, which was just a huge breakthrough. And so kind of the way you can kind of think this is like variable scoping. And so like if I have like, you know, three nested functions, I guess the first, the lowest

`[10:42]` **SPEAKER_01:** level function has like scoped variables, which they'll call ZL, which is the carry that and it's the zero.

`[10:48]` **SPEAKER_00:** A latent variable. Latent variable.

`[10:50]` **SPEAKER_01:** And like traditional RNN literature, they would call this the hidden state, the low level hidden state. Yeah. And I get to recurse, recurse, recurse. And then I pass back that ZL back to the outer scoped function, the higher level one. I let that one do one iter. It goes back and calls the lower level again. It does this whole thing in a third outer loop, which is called the outer refinement

`[11:11]` **SPEAKER_00:** step. But when you describe it like that, it seems like it would have the same back prop through time problem that you would have at RNNs, and I think they came up with a clever trick to basically get around that. So like what was that trick that they figured out?

`[11:22]` **SPEAKER_01:** And this is really the crux of the paper that like differentiates it, in my opinion, in the literature, is they, instead of doing what Alex Graves did in all of his papers from neural turing machines to adaptive compute time to differential neural computers, is he always back propped through all of the recursion steps. And he was limited by back prop through time, so you could only make the model so big, you have all these issues, vanishing gradients, et cetera, et cetera. And what they do is they kind of have this DEQ method of doing fixes.

`[11:56]` **SPEAKER_01:** So it's like deep equilibrium models. Yeah, deep equilibrium learning, where if I take a batch, and this is completely counterintuitive as a computer vision person, because you'd never do this, but it actually does make sense. And I'll explain why. If I take a batch of like ImageNet or CIFAR10, and I forward pass through the model, and I get some loss, and I back prop, and I update the weights, I would go get a different batch for the next one. But what they do instead is they actually do that 16 times.

`[12:25]` **SPEAKER_01:** Yeah. And so, and as you do that, you actually can see the change in your residuals get less and less and less. And why it actually makes sense is because when, in the RNN case, the ZL and the ZH, which are the carry, the task carry, start out as- Or the hidden states. The hidden states. Start out at zeros. Those are zeros. Then we go through this whole loopy recursion, at least the two loops, the two lower loops, the TL and TH steps. And then I back prop just through the two models. Just once.

`[12:58]` **SPEAKER_01:** And I don't recurse all the way back. I do a stop grad, and I stop right there. And then there's a huge residual, and then I don't reset ZL and ZH. I do it again at a different point in the carry or hidden variable space. And so one can actually look at it as a different batch every time, even though it's the same exact axis.

`[13:19]` **SPEAKER_00:** Yeah. Like the way I kind of think about it is like the 16 or whatever that you're recursing over, it's like constructing a mini batch, not from different inputs, but from different memory states basically. It's like across this hidden or carry memory access basically.

`[13:38]` **SPEAKER_01:** And that math holds, and it works. It follows DEQ directly in the event that the delta in ZL and the delta in ZH go to zero, which it actually doesn't do. And so we'll get to TRM. But Alexia- Yeah. It basically shows that it's just not the case, and you can't actually apply this math. And that's why it's working. That's not sufficient support for why it's working. We actually don't know why it's really working. And she figures out that you actually can back prop through all the way to the deep

`[14:12]` **SPEAKER_01:** recursion, which we're going to get into TRM in a second. And that actually improves performance much, much more.

`[14:17]` **SPEAKER_00:** Interesting. OK. So before we get into TRM, yeah, on this paper, I think there's a bunch of different ways people have looked at this, right? In terms of... How they came up with it, and then why this may or may not be working. One, it's a sort of bio-plausibility argument. As you know, I'm usually not super keen on these. I think machine learning tends to have a long history of people starting with bio-plausible arguments and then realizing that there's some variant of them that seems highly bio-implausible

`[14:42]` **SPEAKER_00:** that actually works better. I think you have example along those lines right there.

`[14:45]` **SPEAKER_01:** Yeah. The classic, the first deep learning paper that started this whole craziness is AlexNet. And in AlexNet, there's actually this funny little thing called Local Receptive... Activation, or Depression, or something like that, where once this activation fires, then I have this refractory region or something like that, it actually doesn't work at all. And it didn't work, and you didn't need that, and then VGG came out and said, get rid of all that, just go deeper. It's like three by three.

`[15:11]` **SPEAKER_01:** And three by three conv. And it actually just outperforms dramatically. And so this is always the case. Maybe you need to do it to get accepted into NeurIPS. Yeah, sure. Totally. Totally, yeah. You're definitely the expert here, but what do you consider to be bio-plausible and what's

`[15:24]` **SPEAKER_00:** not? I think a lot of machine learning literature has overlapped a lot with people working in neuroscience. I think it is very natural for us to ask questions about how does our brain work, because our brain is like an incredible instrument that does a ton of computing, obviously, and does it in a very shockingly efficient manner, it seems like. And so a lot of machine learning research has, for a long time, sought analog from how we think to understand our brain to work and try to encode that in various machine learning

`[15:50]` **SPEAKER_00:** systems. So from the very basic concept of what a neural network is, it's called a neural network because we think it's some basic model for what a neuron is, how certain activation functions work are meant to be inspired by certain biological premises.

`[16:03]` **SPEAKER_01:** Do you think that's a misnomer?

`[16:04]` **SPEAKER_00:** The thing about them is that often we use bio-plausibility to inspire us to come up with ideas, but we end up veering away from the bio-plausible to something adjacent to them that is likely bio-implausible, but that seems to work better.

`[16:18]` **SPEAKER_01:** Something that runs better on a GPU. Exactly.

`[16:20]` **SPEAKER_00:** It runs better on a GPU, it's more efficient in some capacity that is relevant to how we actually encode it in a computational system. So I find thinking about bio-plausibility fun and interesting, and it's definitely a great way to inspire us to think about new things. But I tend to not be bounded by bio-plausibility when I think about what machine learning systems we should prioritize working on or think are particularly exciting, other than as an interesting scientific launching point for a deeper exploration.

`[16:45]` **SPEAKER_00:** I think the version of this that I find more compelling is actually that original discussion we were having. It was around automata theory, basically, and honestly, just actually like fundamental data structures and algorithms theory, which is that if you're running a complex algorithm, having access to sort of a memory cache is actually very useful for being able to run that algorithm efficiently. And I kind of think of this set of hidden states or carry as akin to a Turing machine

`[17:11]` **SPEAKER_00:** tape or akin to the radix sort memory bank, where you can basically train a model to use this memory cache. And then you can do this in a more intelligent way in a single forward pass, so that you can get a more efficient time operation that would otherwise require some sort of more complicated reasoning. Yeah.

`[17:27]` **SPEAKER_01:** I think that a point I wanted to make earlier is that we did this COT stuff and this tool use thing as ways to get beyond the limitations of GPT-2. And so the way that we get... You can actually... I've done this experiment, you can actually, if you give me infinite amounts of unsorted list and sorted lists... If I can do chain of thought and I can do every single step and teach it to do every single step, then I can actually get it to do sort and become a Turing machine at test time.

`[18:02]` **SPEAKER_01:** And similarly, an even cheaper one that is much easier to do is you teach it and you say, hey, there's this Python function called sort. Just call the function. Just call the function. And I'm like, that's the easiest thing to do and you don't need back prop at all. And so those are the two hacks. Now, well, Francois, this is solved. Like, we're done. Right? No. Because I needed to know what sort was. What happens if we didn't know what merge sort is?

`[18:25]` **SPEAKER_00:** The chain of thought is not going to inherently discover sorting from first principles. It's finding it from our historical knowledge of everything it's trained on.

`[18:32]` **SPEAKER_01:** Yeah. I mean, this is like the... The demos had this whole thing about like the ultimate test is the Einstein test. Like go back to 1911 and then like have it rebuild all the physics up until now. Similarly, let's just pretend that we only had bubble sort. We knew other... No other sort system. If you chain of thought it on all the bubble sort input and output. It will only do bubble sort. In fact, it won't even do bubble sort that well. So this is the best situation. And then the tool use, of course, it can only know bubble sort.

`[18:57]` **SPEAKER_01:** I want to get to merge sort. How do I discover merge sort?

`[19:01]` **SPEAKER_00:** And I think the interesting thing just to emphasize here, because it may not have been extremely clear is there already exists some type of recursion that people are used to in LLMs, which is chain of thought we mentioned earlier. But that is a recursion that's happening in the token space of the model's outputs. Yeah. And that's inherent to the model itself. And that's sort of the fundamental limitation is that the model can only do a feed forward one shot output. And then we basically just have this hack that if you keep letting it output things,

`[19:32]` **SPEAKER_00:** then it can read its outputs and do somewhat intelligent seeming things with it. But it seems to sort of be upper bounded by the data that we feed it that the labs are very hungrily buying right now and not this sort of like inherent underlying recursive reasoning.

`[19:47]` **SPEAKER_01:** Yeah. So in both cases. In both cases. If you're using hacks to solve this in COT and tool use, you're bounded by the bounds of human knowledge. In the event it's outside the set of human knowledge, then like you're kind of SOL. And so that's one. The other, you make a great point about discrete versus latent space. Reasoning in a discrete, it can only output the carry in the case of LLMs has to be snapped back to some discrete token space. And in the case of RNNs. Yeah. RNNs in general, they remain in this continuous latent space, which is much higher dimensional.

`[20:24]` **SPEAKER_01:** If you give me like a tape that's this long and you cut it up into 10 buckets, like versus all the possible values. Right. Exactly. Yeah. It's much more expressive to being continuous space. But we can't train it that way because we actually, you know, because you're inhibited by back drop through time largely. And this is why this paper is so exciting.

`[20:40]` **SPEAKER_00:** Okay. So before we then go over to the TRM paper, let's just summarize here. What matters most from the HRM paper that we should take away? Before we transition and contrast it with the TRM paper?

`[20:51]` **SPEAKER_01:** Yeah. I think that the number one piece to take away is this outer refinement loop. The outer refinement loop scales. And there's a great breakdown. Basically the Sapien authors, which huge kudos for this paper because there's so many innovations in this paper, didn't really do like a scaling ablations on every single one of the inputs. But this guy, Constantine. Constantine at François Chalet's company, India, actually did. And it's this amazing breakdown that he posted on YouTube that you can go check out.

`[21:27]` **SPEAKER_01:** But basically the main takeaway is that the outer refinement loops is the main beneficiary, is the main reason why these things work so well, which Alexia basically takes the, she found I think in parallel and scales up and shows that you can get rid of a lot of all

`[21:46]` **SPEAKER_00:** this other stuff. It's a lot of machine learning. The follow on paper is basically delete 75% of the first paper, as we've often done in videos here, and keep the magic basically. So what's the magic then? What's the part that actually matters in terms of what stays in the TRM paper? And let's now contrast the core architectural differences between these two papers.

`[22:05]` **SPEAKER_01:** Yeah. So I think that, I guess if I break it down into two major things, is this outer refinement loop thing is really great and works really well, and that this truncated back prop through time. Yeah. So truncated back prop through time, except I truncate at some time. Some earlier point. Earlier point. Yeah. Called T, T back. T equals one is actually completely sufficient. And so truncated back prop through time, T equals one, completely sufficient. And that's very counterintuitive.

`[22:33]` **SPEAKER_00:** Which is what HRM found.

`[22:34]` **SPEAKER_01:** Which is what HRM found. And TRM does a little bit further, rather than going through just one call to the H net and the L net, it actually goes through one full recursion loop. So if I do it 16 times, I just go back. I go back through one time. And that is kind of sufficient. And if you do it with this fixed point iteration thing, pseudo fixed point iteration thing, where you keep hitting it with gradient at every single step, it weirdly works. And this batch size across the carry space actually works.

`[23:08]` **SPEAKER_00:** So that part is also kept between these two models. It seemed like another thing that changed was having this sort of double layer of higher order thinking. And lower order thinking. It seems like it collapsed it down into just a single one. What's the intuition there? And how does that actually work in the TRM paper?

`[23:25]` **SPEAKER_01:** Yeah, so it's interesting. She actually ablates having two separate networks versus just having one. I guess the more important space is the variable scope. Is that you should have low level features and high level features. But the same network. And so the best performance model.

`[23:37]` **SPEAKER_00:** The same network can extract both, basically.

`[23:39]` **SPEAKER_01:** Yeah. You weight share between the L net and the H net, and it's just called net. And you do just one transformer layer versus the four like they do in C. Yeah. And then you do one transapient and just whittle it down to one and do more recursion. But you keep ZL and ZH to be distinct and separate. And she calls it X and Y, which I found very confusing. X, Y, Z. It was just very confusing. And it's just like ZH and ZL is just cleaner.

`[24:04]` **SPEAKER_00:** So if you read the paper, Y is actually like latent space. It's like Z, basically.

`[24:08]` **SPEAKER_01:** And it is not a label. Yeah. Okay. Which really threw me through a loop. Whatever, yeah. But anyway, we'll go through some code here and I'll walk you through it. So I've replaced all of her nodes. Yeah. Yeah. I've used the old term and use the sapient notation, which is much cleaner and more straightforward to me at least.

`[24:23]` **SPEAKER_00:** Okay, cool. And now before we dive into the code for a sec, like in terms of how these TRMs actually work, it's pretty interesting. Because this recursion advantage now gives you a bunch of advantages over transformers. Rather than having, you know, 500 or a thousand or a million or whatever transformer layers and having tons and tons of parameters, you get compute depth basically without this parameter depth. Right. And the optimization process looks like more of like an iterative kind of like expectation

`[24:52]` **SPEAKER_00:** maximization algorithm. Do you want to talk about how that worked in the TRM paper? Because I thought that was also pretty interesting.

`[24:57]` **SPEAKER_01:** So both of them kind of have the same kind of EME feeling thing, where like we update ZL, condition upon the input X and ZH, the last ZH, ZH t minus one, let's say. And then we keep updating ZL, ZL, ZL, ZL, ZL, and we keep updating it. And then we go holding, we update ZH, condition upon ZL, and actually it's just ZL, it's not even X. And then we just update ZH. And the way to think about ZL and ZH is ZL is like your local scoped variables that are just being overwritten and updating, updating, updating.

`[25:37]` **SPEAKER_01:** And then ZH, and Azalea makes this point, sorry, Azalea, Alexia makes this point, that is, that is a candidate answer, a proposed answer. A proposed latent answer that is just an embedding space away, one MLP lookup away from the true answer.

`[25:54]` **SPEAKER_00:** So you're kind of like EMing, just to like zoom out a little bit. You're kind of maximizing the probability of the correct, you know, information stored in your memory, conditioned on a given output, and maximizing the right output conditioned on the information stored in your memory, quote unquote, in parallel. And like that optimization algorithm leads to... you ultimately learning a recursive method that stores the right information to this local memory, basically. Yeah. And then outputs the right thing.

`[26:26]` **SPEAKER_01:** It really, like, if we actually think of Sudoku, it's actually a really natural way to think about what's actually happening under the hood. Where Sudoku is an incomplete puzzle. You can't guess every cell at any one time. You can, actually it's designed where you can only guess one or two cells based on the available information. So it's not, it's an incompressible problem. You actually can't do it unless you're just randomly guessing and guessing and guessing, which is... it's a very high combinatorial space.

`[26:50]` **SPEAKER_01:** And so what the ZL is doing is some type of, let me try this, try that, do some computation, think about little things, and then it proposes, and then we go to condition upon, like, something that it may have found, it sends it to ZH, ZH fills it in, and now we have a little bit more of a filled in Sudoku puzzle.

`[27:07]` **SPEAKER_00:** And the training process is training the algorithm to know to do that, right? It's like, it's maximizing that, it's like, oh, this strategy for what you save tends to lead to correctness. Correct outputs.

`[27:18]` **SPEAKER_01:** Without chain of thought.

`[27:19]` **SPEAKER_00:** Without chain of thought, exactly.

`[27:20]` **SPEAKER_01:** That's the most important part. It's like, if we had Sudoku and we knew how to solve Sudoku, because, like, we were just, you know, dumb homo sapiens that didn't know how to solve Sudoku, like, it would just have solved it. And that's why it's cool, because it actually is able to discover things without being teacher forced via chain of thought. Right.

`[27:37]` **SPEAKER_00:** Interesting, yeah. Should we look at some code? Let's do it. Okay, let's dive in. And I would love to see what these papers or bottles look like just distilled down to their core essence. I know there's lots of details on how you train them, but kind of the core training algorithm. And it'd be great to contrast the two methods. Yeah.

`[27:53]` **SPEAKER_01:** So, I mean, they're remarkably similar. And so, largely one, and learning one is learning the other. But basically, you start out with some ZH and ZL that are just zeros. You have some input embedding space to go from X raw to X, which is the maze state or whatever it is, initial maze state. And then with no grad, you don't pass any gradients back through this. You...

`[28:17]` **SPEAKER_00:** This is the trick, basically. This is the trick. To not back prop through time.

`[28:20]` **SPEAKER_01:** Yeah. Here are two of the three recursion levels. So, yeah, this is like the... They do this just for simplicity, but I hit ZL, T low times. And then once for modulo, T low, then I hit the ZH and I do it again and again. And like you said, I'm updating ZL condition upon ZH and X. Right. And then I update ZH condition upon ZL.

`[28:45]` **SPEAKER_00:** Right. So, this is like the expectation maximization style approach. Exactly.

`[28:49]` **SPEAKER_01:** Yeah. And then you don't really need this. This is like just for cleanliness to show clearly that there's no gradients occurring above this line.

`[28:57]` **SPEAKER_00:** Basically freezing the weights past that.

`[28:58]` **SPEAKER_01:** Exactly. And then I hit L net and H net one more time.

`[29:01]` **SPEAKER_00:** And then... Which is the same thing as up above. So, this is just... Okay. It's literally just the no grad thing running one more time.

`[29:06]` **SPEAKER_01:** Exactly. Cool. Yeah. And just make it really clear. And then there you go. And that's your HRM model. Cool. And they use... That's quite simple. Yeah. It's actually sufficient. If you actually go much higher, Konstantin showed very clearly that it doesn't actually help.

`[29:22]` **SPEAKER_00:** So, that's two of the three recursions you said. The third happens in the actual train loop.

`[29:26]` **SPEAKER_01:** The third is in the train loop and at the test loop. They both have this M test or N supervision, which Alexia calls deep supervision. They call it adder refinement steps. It's just whatever you want to call it, call it NSUP.

`[29:40]` **SPEAKER_00:** And so, you do this NSUP times during training and then during test time, there's a different hyperparameter. So, for how many times it recurses over each model, which is M test, basically. They're actually the same.

`[29:50]` **SPEAKER_01:** Okay. And so, this and this, we can probably just call this the same. Yeah. But it's the same. And if you actually... Konstantin does a good job of this. If you actually train on 16 and you test on only one, you get like seven eighths of the performance or almost all the performance. So, it's actually quite interesting. This is just redundant, too much compute, and it doesn't actually help you all that much. So, setting this to one is actually like...

`[30:21]` **SPEAKER_00:** But presumably for like more complicated problems, having more test time compute is still useful is like the reason you would set it up this way.

`[30:28]` **SPEAKER_01:** Yeah, for sure. And so, we call our HRM, we get some loss, we back prop through just those two little parts here, and then we step, we zero out the gradient, but we do not update ZH and ZL. These are still the same in it, so that's the really important detail there. Right. And then so we go back, we pass in the ZH and the ZL from the previous one, so now this is actually not the same batch. Right. Because we have updated ZH and ZL, so it's in a different part of the latent space.

`[30:59]` **SPEAKER_00:** Cool. Yeah. And that's the key like mini batch construction through memory space concept. Yeah.

`[31:05]` **SPEAKER_01:** Exactly. Yeah, cool. Exactly. And then at test time, it's simply the three loops. So, there's your outer refinement loop, which turns out like just at train time... Doesn't matter. Train time recursion was important, but test time recursion was actually not that important, which is kind of counterintuitive. And then the HRM inside that has your two other loops. Makes sense. And that's it. So, pretty simple. Okay. Now the TRM. And now for the only two changes, the main two changes here is that they collapse, LNet

`[31:32]` **SPEAKER_01:** and HNet into just net. Great. And it's important detail. These are four transformer layers, this is four transformer layers, and this is just one transformer layer. Yeah. Yeah. So, this actually shows that going deeper actually didn't help.

`[31:44]` **SPEAKER_00:** Yeah. And actually on some tasks, it was just the feed forward net actually worked just as well as the transformer there, right? Yeah.

`[31:49]` **SPEAKER_01:** And the MLP. It was like on Sudoku, I think. Yeah. On Sudoku, MLP actually outperformed the attention. It scored zero on the maze, the MLP scored zero on the maze. And so, it's not clear, it's not obvious that the transformer is always better. So, there's the weight sharing. And then instead of going back just the one, two, the H, this back propping through just these two, you actually back prop through one latent recursion step, all the way through one latent recursion step. So, let me just walk through this a little bit.

`[32:20]` **SPEAKER_01:** So, we have the same thing here. Same starting point, yeah. It's mainly the same thing here. We're doing this six times. And then we go one more time here. And then we do our deep recursion. This is the outer loop, N sub times. And so, again, we have the no grad, we have the detach. And then this is where it's different. So, I am calling this latent recursion after the detach.

`[32:45]` **SPEAKER_00:** Yeah. So, it's one full recursive loop is happening versus here.

`[32:49]` **SPEAKER_01:** And so, that's the main difference in the optimization, otherwise it's effectively the same. And then it outputs, and then you're good to go. And you train it exactly as the same way before. And then at test time, it's the same thing again. And so, largely the same.

`[33:05]` **SPEAKER_00:** Cool. And so, in many ways, it's sort of a simplification, right? You're collapsing certain parts of it. You're simplifying this net arc. You're simplifying the architecture. It's slightly more complicated along this back prop through time part because you're actually back propping through more than you did before. But it's like taking a bunch of lessons from the first one and basically simplifying most

`[33:24]` **SPEAKER_01:** of it. Right. Which is actually why she needs, I think, is why she needs to make the model smaller. And so, it's a 28 million parameter model for HRM. Now she brings it down to a 7 million parameter model and it actually gets from 70% to 87% on ArcPrize 1. And it's actually quite well on ArcPrize 2 as well. And so, yeah. So, she makes the model three, four times smaller. But because it has that recursion, it actually outperforms. And there's this researcher named Melanie Mitchell that writes this book talking about

`[34:01]` **SPEAKER_01:** this very phenomenon, which is like it is sufficient, not necessary, to go bigger and get better performance. And it is sufficient and not necessary to add more. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. And so, you can get a lot more recursion. And so, where I'm really excited is what happens if you do both. Right. And you're still limited by back prop through time. Even Alexia is limited by that last step from a memory perspective for sure. And so, if you can make the model really big and you have lots of recursion and we do something

`[34:31]` **SPEAKER_01:** else other than back prop through time, then we can get exact all the benefits of this and all the benefits of the giant LLMs. And then you can get some crazy stuff.

`[34:39]` **SPEAKER_00:** So, now to wrap up. Why don't we talk a little bit about the bigger picture? What does this mean for the field of AI research? How should people think about where these models fit into the current span of research happening, especially given that it seems like a bit of a departure from a lot of the methods that people are used to hearing about and increasingly seeing products that people use?

`[34:57]` **SPEAKER_01:** Well, I think for one, from the arguments that Schmidhuber makes and that we've talked about today, recursion is important and it's not going away. And clearly the benefit is here of adding recursion into models and you've seen things like the recursion language models out of Google that are pretty powerful and cool. And so that's definitely one piece that's, I don't think, going away anytime soon. The next one is this add a refinement loop, like back t, tb, tt, like t equals one, truncated

`[35:25]` **SPEAKER_01:** back wrap through time t equals one. I think that that is a really powerful idea and the fact that that works so well, we have yet to really explore that extremely, really understand what's happening there. And then the third is that idea of like, okay. Okay. We know that recursion works. We have these tiny recursive models that are seven million parameters that can solve what a hundred million, a hundred billion, a trillion parameter model can't solve trained on the entire internet and a seven million parameter wins.

`[35:58]` **SPEAKER_01:** Like the right answer is to like take the amazingness here and take the amazingness here, which probably is already in Gemini already or some of these, it might be at least in some part. But when you, when you take. The benefit of both these TRMs and these giant models and you actually slam them together, I think that it's just going to take off and it's going to be really huge.

`[36:18]` **SPEAKER_00:** Yeah. One of the things that's really interesting about these TRMs and HRMs is they're not general purpose models, right? These were task specific models, right? The model trained to do Sudoku cannot do ArcPrize inherently, it has to be trained on the ArcPrize set to do so versus the LLMs that are used on these tasks are general purpose models that maybe get some additional fine tuning data or in context learning data on those tasks. And so I think that's where the interesting overlap might come is if you can make these

`[36:43]` **SPEAKER_00:** more general purpose agents that can somehow be general purpose in the way that the sort of next token prediction algorithm has given us and do more complex reasoning to achieve that. It seems like you can have really efficient architectures to do scale up reasoning.

`[36:57]` **SPEAKER_01:** Right. And like a lot of the view of what these LLMs are doing is finding really amazing embedding representation spaces, but reasoning inside that, that space is actually not done all

`[37:08]` **SPEAKER_00:** that much. It's always through the token space.

`[37:10]` **SPEAKER_01:** It's always through the token space. And so like what you can imagine is we found mapping from token space or from vision, from pixels, some really cool latent space where like things are just nicely semantically separated and we can, you know, makes it really easy for downstream tasks to do. But now in that space, use this like tiny reasoning models, use some type of recursion inside that and train those, those, those, that model on that, a little small model on that reasoning space.

`[37:39]` **SPEAKER_01:** That's really going to work.

`[37:40]` **SPEAKER_00:** Francois, thanks so much for breaking it all down for us. See you all in the next episode of Decoded. Thank you.
