# 全文转录 · 每个创始人都该懂的机器学习技术:扩散模型

> ▶ [YouTube](https://www.youtube.com/watch?v=dC_3ys349bU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/dC_3ys349bU.md) &nbsp;·&nbsp; The ML Technique Every Founder Should Know
>
> 🗣️ 说话人分离识别到 **2** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_00:** Welcome back to another episode of Decoded. Today, I'm sitting down with YC visiting partner Francois Chaubard to talk about one of the most important topics in AI today, diffusion. Francois has been doing computer vision since 2012 when he started in Fei-Fei Li's lab. And after a decade running focal systems, he's currently back at Stanford finishing his PhD, working on diffusion-based world models for AGI. We're going to break down what diffusion is, how it's evolved over the past decade, and how it's used today.

`[00:31]` **SPEAKER_00:** Francois, thanks for being here.

`[00:32]` **SPEAKER_01:** Thank you for having me.

`[00:33]` **SPEAKER_00:** Well, we just got back from NeurIPS. We just spent a lot of time talking to researchers and thinking about all the newest models out there. I think we saw diffusion pop up over and over and newer versions of this type of approaches that are not autoregressive LLMs. And so I wanted to talk to you about those today. So first, why don't we start by defining what is diffusion?

`[00:53]` **SPEAKER_01:** Diffusion is a very fundamental machine learning framework that allows you to learn any p-data, any probability of data for any domain as long as you have the data.

`[01:03]` **SPEAKER_00:** So you're trying to learn some data distribution. That's right. Now, in a sense, all LLMs or all machine learning models are about learning data distributions. That's true. How does diffusion in particular, what stance does it take or what approach does it take to being able to learn distribution?

`[01:16]` **SPEAKER_01:** Yeah, I mean, I think you can use diffusion to always do that. The thing where it stands out in particular is mapping from high dimensions to high dimensions, especially in low data regimes. So say I only have 30 images of Gary, which I actually have some code that we're going to walk through. Cool. I only have 30 images of Gary. And again, we're in this thousand by one, thousand by three dimensional space, and I want to map to another three million dimensional space with only 30 training samples and I can still do it.

`[01:46]` **SPEAKER_01:** And it's pretty powerful in that way.

`[01:48]` **SPEAKER_00:** Okay, cool. So you have this ability to use relatively small amounts of data compared to the dimensionality to learn a p-data. That's right. What's the basic process by which diffusion works? Like just walk through, like at a very high level, and we'll walk through the math a little bit later, but at a very high level, how does this process actually work?

`[02:04]` **SPEAKER_01:** We take some sample of the data, an image of Ankit, an image of Gary, and we just hit it with noise, and then we just keep hitting it with noise, and we create this train of noised up images. It's very easy to create noisy images, right? It's hard to walk backwards and create from noise images of you or Gary. And so then we flip it, and then we try to teach the model to reverse that process. And that's basically it.

`[02:32]` **SPEAKER_00:** Okay, cool. So it's basically a noise-reversal process. A de-noiser and a de-noiser, and the de-noiser is the model that you end up training. Exactly, yeah. You will basically teach your force

`[02:40]` **SPEAKER_01:** and give it noised up images, and then have it learn intermediate representations to get back to p-data.

`[02:48]` **SPEAKER_00:** Cool, nice. And what kinds of stuff is diffusion used for today? What are some applications that it's widely deployed in?

`[02:53]` **SPEAKER_01:** It's honestly surprising how applicable this process is. I think the original 2015 Joshua-Sold-Dixie paper was on CIFAR-10, which is just images. And I think it has its roots in images, but it is far more sprawling than just images. As you've seen, DeepMind just won the Nobel Prize for doing this exact procedure on protein folding. You can drive cars with this, with the diffusion policy paper, which is like an insane result. You can predict the weather. There's really no limit to the things that this can do.

`[03:32]` **SPEAKER_00:** Yeah, it's pretty incredible to see. I mean, you have these image and video generation models that seem to be really advancing over the last few years. Stable diffusion is the one that I think many people have heard of, and then newer versions of it seem to be using this as well. And then, yeah, in the world of life sciences that my company was in too, I think we see this newest generation of life sciences, AI companies are heavily investing in this set of technologies. There's a model called DiffDoc that works really well

`[03:54]` **SPEAKER_00:** for predicting small molecule binding to proteins. And then, yeah, AlphaFold, especially the newest AlphaFold versions use diffusion pretty heavily. It's really cool to see the same core, piece of technology applied to so many different domains. Yeah, yeah. This class of models has evolved over the years, and there's a whole slew of papers someone could read. So you should probably go read the papers to learn all the details. But maybe at a high level, we can try to trace out a few of the key innovations that happened,

`[04:19]` **SPEAKER_00:** starting with the paper you already mentioned that now led to the newest versions of these models. So how would you map those out? Like, what was the first kind of turn of the crank from this very high level diffusion process you outlined? What was the first version of that that started to work?

`[04:33]` **SPEAKER_01:** Yeah. So I think the 2015 original Joshua paper is it put up all the key pieces, all key components of modern diffusion. And so like now we're just playing with different things. So the scheduler, how do we add noise? At what weight? Like that's a whole part that we can discuss. What's the loss function? Should I predict, should the deep learning model condition upon X of T predict the actual data, X of T minus one? Or should it predict the error that was just added to it? Or should it predict the velocity?

`[05:03]` **SPEAKER_01:** Which is the error divided by the time. Should it predict the velocity of the start and the end? That's called flow matching. There's all these different plays on what the loss function is.

`[05:14]` **SPEAKER_00:** So in all of those, the idea is still to do denoising. Yes. But the objective for each of them is somewhat different from each other. And they're all pretty closely related, whether it's basically a delta between two things, or the previous step, or the first step. How do these all actually come together? But these are series of papers that happened one after another?

`[05:32]` **SPEAKER_01:** Yeah. Okay. Yeah. I think. We just kind of hill climbed on this Farashay inception distance metric. That's kind of a kooky, weird measure to see how good an image is. But we just kept getting better and better and better on it, by doing these little tricks. And so it turns out that predicting the actual data itself is actually quite hard. And maybe predicting the error is actually easier. And then predicting the velocity was even easier than that. And then predicting the global error across the entire diffusion schedule

`[06:01]` **SPEAKER_01:** is even easier than that. And just kept. Finding easier and easier ways to basically sample from noise to data.

`[06:09]` **SPEAKER_00:** And here when you say easier, was the ease largely driven by it was mathematically simpler? Or it was easier to implement an engineer? Or simpler to reason about? Or what got easier really?

`[06:22]` **SPEAKER_01:** It actually is that too, but I didn't mean it that way. What I actually meant was it's easier for the model to learn. But it is also, and we'll go through some coding examples, the math actually got easier. And the code got smaller, which is actually oppositely true in most of the case in most machine learning. Actually, things get more complicated. I think we started with UNETs, and that was the predominant architecture. We didn't really talk about architectures that much, but then we got into these diffusion transformers,

`[06:51]` **SPEAKER_01:** and this cross-attention mechanism, and things like that. And so, yeah, we just kept getting better and better at reducing FID. Hmm, interesting. Dive into some code examples? Let's do it. Let's do it. I'll walk you through, I made about one, two, three, four, five, six, seven of these that I implemented with varying levels of success. But all the structures are going to be the same. So the Joshua paper, the non-equilibrium thermodynamics paper, you can see here are some nice images of Gary, you can see here.

`[07:24]` **SPEAKER_01:** Very nice. This is what I could find online. Nice. And then-

`[07:27]` **SPEAKER_00:** So those are images of Gary that you've down sampled so that they're 1,000 by 1,000, or they're smaller, I think. Yeah, I think these are 64 by 64. 64 by 64. Yeah, they're really small.

`[07:36]` **SPEAKER_01:** This is just a very small example. Yeah. 64, and then I randomly augmented to create more data. Great. Because I was lazy, and that was easier than downloading more images of Gary. Okay, cool. Didn't want to get a security call on you. Exactly. So, and then I implemented this diffusion schedule, and this is probably one of the most important, like of all the parts of diffusion that's difficult to comprehend, I would say that the noise schedule is actually the hardest part, to understand, that I really, like, I struggled with myself.

`[08:03]` **SPEAKER_01:** And so, if you can see here, the noise that's added from time step 0 to 10 to 25, all the way to 100, it's clearly destroying the structure. Yes. And then we want to train the model.

`[08:16]` **SPEAKER_00:** Where you end is basically random static.

`[08:18]` **SPEAKER_01:** Exactly. And we want to basically reverse this, and from here, get to here, and have the model get to that point, get to this point, get to that point, et cetera, et cetera. And so, the interesting part, and this is Joshua really, you know, implemented almost everything that we needed for diffusion. And there was just a few little tweaks that were missing, and he didn't scale it up. That's, to me, the parts that we're missing. And if you see here, the noise schedule. So, it would make sense to me that I would have

`[08:52]` **SPEAKER_01:** linear interpolation between the image and the noise. And I would start with like one and zero. Sure. One being the image, and zero being the noise. And you gradually add it. And I linearly add it. But if you do that, it actually is massively unstable. Because the instantaneous amount of error that you're adding is very small in the beginning. Right. If you think about like an image. Like on a relative basis. On a relative basis. And then at the end, you have to destroy all the, to get to a complete noise, you need to add a lot of error.

`[09:23]` **SPEAKER_01:** Yeah. And so like, if you're a model, and you're just looking at this little chunk of the noise schedule, then you have to handle a lot of error, in one step. And on this side of the schedule, you need to handle such small amounts of error. And what you actually want is constant, like relatively constant amount of error being introduced every single time step. Right. And that, the cumulative sum of all that error actually ends up looking like this, like this curve here.

`[09:50]` **SPEAKER_00:** That's the pink curve. Yeah.

`[09:52]` **SPEAKER_01:** And so, they call this a beta schedule. Beta is the diffusion rate. The rate of diffusion that I'm doing while I'm rolling this. This thing out from time zero to time T, capital T, and so you can see here, the beta schedule. So, we usually have some beta min to beta max. And then, one minus that is the alpha. And you can think about the beta as like, how much noise I'm adding at every time step. Yup. And you think about the alpha as how much. How much data is lost, basically? Yeah. Being retained.

`[10:23]` **SPEAKER_01:** And then, the term that really matters is the alpha bar, and these are the weights that are used and it has this kind of, like, one minus sigmoid looking thing. But that's basically the noise schedule. And once you get that right, really this part here, then everything else just works. And then I train some model and then we can actually.

`[10:45]` **SPEAKER_00:** So there, what was the training objective again? So you're adding this noise and the training objective was to do what exactly?

`[10:51]` **SPEAKER_01:** In this case, it's to minimize the KL divergence between the real distribution and the distribution that I'm learning. And so, I won't go through the code for this one, because it's a little bit hairier, but you can kind of see the result on these generated images after 100 diffusion steps at inference time. And you can see that that Farashay inception distance is 222, which is like extremely high today. Like modern day would be like maybe like eight or 10 or something.

`[11:19]` **SPEAKER_00:** And what's interesting here, I mean, you kind of scroll through it there, but it's, you mentioned it, there's quite a lot of code that it actually takes to do that KL divergence base loss. I suspect that in these later models, you're going to show, it gets significantly simpler. So, I'm just mentally noting that because I suspect there's going to be an interesting contrast to draw between these two.

`[11:37]` **SPEAKER_01:** Yeah. So, the next one I would like to show is flow matching, which is just so beautiful and simple. And this was out of Meta, Yaron Lipman, where he basically said, we don't need a lot of this stuff. What we need to do, forget the, if you think about the noising process as being this, like I start from data, I randomly sample a vector of noise, and I just go in this direction, and then I do it again. I go in this direction, and I do it again, I go in that direction, I go in this direction,

`[12:08]` **SPEAKER_01:** that direction, and then I'm here at noise. And then you have to teach the thing to go in the exact opposite path and you have to do this very circuitous path. And so, at test time, it's actually quite expensive. You have to do, we've all waited for ChatGPT or Midjourney to like make an image, and it takes a while. Right. What it's doing is like a thousand calls to the model, again and again, iterating through to get to that point of pData. Right. Instead.

`[12:32]` **SPEAKER_00:** And like intuitively, it's like, okay, we're doing the circuitous path, but surely there's a shorter path between those two.

`[12:38]` **SPEAKER_01:** Yes. And so, that's what makes flow matching so cool, to me at least, is that they said, forget all of that intermediary results. There is a velocity, a global velocity between the noise and the data, and it's just this direction, and it's just this straight line. And I don't care where you are, go in that line, wherever you are, you're over here, go in that line and teach it to go in that line. And that's what flow matching does. And so, I'll show you the code. Yeah, let's see that in the code.

`[13:04]` **SPEAKER_01:** Yeah, but it's like five lines of code. It really is quite simple. And so, this is pretty cool. So, here you go. You basically have like 10, 15 lines of code that is the most powerful machine learning procedure ever. So, I have some data, an image of Gary. Yeah. I have some noise, some isotropic Gaussian noise that I sample from. Yeah. There's some time that I'm trying to index into in the diffusion schedule, and I create xt, which is the image at the noised up image that's somewhere between extremely noisy and not noisy at all.

`[13:41]` **SPEAKER_00:** And that's basically just the sampling procedure. It's t times data plus one minus that times noise.

`[13:47]` **SPEAKER_01:** That's right. And then I compute the velocity which is independent of the time. I don't care where you are, it's just this global velocity, which is just the noise minus the data, and then it, I return that back to my training loop, which is the shortest amount of code training loop I've ever written, which is five lines of code. I have my batch, I have some time, I sample from that function I just explained before, and then I have my prediction from the model. I feed it in this some noise up image,

`[14:23]` **SPEAKER_01:** somewhere between lots of noise and little noise, x of t, let's call it. And I just want it to predict the velocity that I want to go.

`[14:29]` **SPEAKER_00:** And this is also really powerful because here, you know, you have model abstracted, but that model can be any model. That's right. So, you can put in whatever the relevant model is for your distribution, whether that's a protein model for proteins, or if it's an LLM for text, or an image-based model for images, that is a very clean abstraction, as long as you can then predict this velocity and then move in that direction.

`[14:51]` **SPEAKER_01:** That's right. This code here has nothing to do with images. It could be weather data, it could be, you know, a stock market data, it could be trajectories from a robotics and a tele-ops setup, it could be proteins, it could be DNA, it doesn't really matter. It's all the exact same code. And so, and then also we haven't talked about the architecture. So, like this model here could be anything you want it to be. Like it could be a RNN, it could be a UNET, which is typically, you know, traditionally is, and modernly,

`[15:23]` **SPEAKER_01:** they use these diffusion transformers doing this cross attention mechanism. And so, it can be whatever you want. But all that is independent from whether or not you're doing flow matching or not.

`[15:34]` **SPEAKER_00:** I think this is like a really profoundly interesting result in that, especially this thing we often assume as models have gotten more sophisticated, that they become less accessible for people to understand. But this is quite literally 10 lines of code. Right. That explains essentially all of the most important kind of mathematical and fundamental foundations of the models that we all see, as generating basically like magical AI results on our phones. Of course, there's lots of engineering how you scale them up.

`[16:02]` **SPEAKER_00:** Right. That model could be a 100 billion parameter. Across a thousand data centers.

`[16:07]` **SPEAKER_01:** Totally.

`[16:08]` **SPEAKER_00:** You know, GPUs. Totally.

`[16:09]` **SPEAKER_01:** Yeah, 100 percent.

`[16:09]` **SPEAKER_00:** So, it's the engineering that's the really hard part there, but a lot of the basic machine learning math is actually quite straightforward.

`[16:15]` **SPEAKER_01:** That's right. Yeah. And so, there's a bunch of these like tangent fields to diffusion that all have some different interpretation on what's actually happening, but it's all the same exact math. And most people learning diffusion actually get quite confused, because if you talk to some probabilistic graphical model people, they're saying, oh, this is a probabilistic graphical model, and what's actually, this is a hidden Markov model, and what we're doing is we're learning this like Markovian thing or whatever.

`[16:43]` **SPEAKER_01:** It's like, okay, fine. But like, it's just noise minus data. And like, you should just show that first. And then like, if you think about it from like a physics perspective, and there's all this stat mech people that have that interpretation there's a whole bunch of different interpretations. I think it gets a little bit confusing. And the whole stochastic differential equation people like thinking about this as an SDE, and I think that's all fine. It probably is helpful to think about,

`[17:11]` **SPEAKER_01:** but in terms of teaching it, it's actually quite, quite simple, which is powerful. Cool. So, if we go back to here, you can see that this is literally predicting the velocity. Your goal is to have the model predict.

`[17:22]` **SPEAKER_00:** You're minimizing the loss between predictive velocity and velocity.

`[17:24]` **SPEAKER_01:** And the actual velocity. That's it. And that's super stable. And it's, it's really clean. And then at test time for the physics people, this is like a Euler step kind of thing that you're doing where you call the model a bunch of times. And you iteratively refine. So, back to the hill climb that we were talking about. I'll grab some random noise here, x. And I just do, and I call basically reverse that, that noising process. To de-noise, de-noise, de-noise, and.

`[17:58]` **SPEAKER_00:** It's literally Euler's method. Like you're using the velocity to point in the direction you want to go.

`[18:02]` **SPEAKER_01:** Point in the direction and just keep going, keep going, keep going until you've done the number of steps. The one thing that I really don't like about diffusion as it's done today, is that I can't keep calling it beyond, if I only trained on 100 diffusion steps in my diffusion schedule, if I change that at test time, it doesn't work. And so, you can't like, oh, I want it even better. So, I'll call it even more. That doesn't, you can't. I've tried it, it doesn't work.

`[18:27]` **SPEAKER_00:** Yeah, there's various tricks people try there, but yeah.

`[18:29]` **SPEAKER_01:** Yeah, and so like, there's games played that is actually quite exciting. All the expense.

`[18:35]` **SPEAKER_00:** But sorry, to be clear, here you're saying that's not relevant, right? It's not relevant. Because in this type of model, you don't have this time dependency.

`[18:41]` **SPEAKER_01:** Well, so you do. So, at this time, if you change, for example, the number of steps, if you double it, let's say that, and you expect to get even higher resolution images, it actually will just turn into like white. Like it actually just like doesn't work at all. So, you can't step beyond that. You can't step beyond number of steps that was trained. That's an important detail. There are tricks that people are doing to try to compress that representation. So, like if at train time, I train for 100 steps,

`[19:08]` **SPEAKER_01:** and at test time, I want to do 10 steps. Then what you can do is you can do distillation into the model to try to have the 10-step model learn the 100-step models thing. But then you still got to train with 10 steps. And so, like if you're training with X steps, you have to be using X steps at test time. I see. Interesting.

`[19:25]` **SPEAKER_00:** Yeah. So, you talked about this concept of a squint test. Why don't you define the squint test for a second? Tell me a little about where this comes from. And then I'd be curious to hear how you think about diffusion models in the context of general intelligence broadly.

`[19:36]` **SPEAKER_01:** Yann LeCun has this like interesting lecture where he talks about our discovery of flight and that we didn't need flapping wings. We kept trying to mimic a bat and how that was a waste of time. And to that, I say you're 100% right. However, we did need two wings. And you look at the Wright Brothers original plane and you squint and you look at a bird. You're just like, hmm, while we have helicopters and we have jets and things like that and rockets, like we got there eventually. And so, there's many elements in the set of things

`[20:08]` **SPEAKER_01:** that can achieve flight and they have different pros and cons. And there are many elements in the set of things that can achieve intelligence. We are the only existence proof of it at all. And like I'm sure there will be more elements in the set. And maybe LLMs, broadly speaking, can get there. But if I squint and I look at LLM setup, which I see this monolithic stack transformers, the same thing, stack, stack, stack. And there's three stages of training. We do this pre-train, SFT, post-train,

`[20:38]` **SPEAKER_01:** and then no learning at all beyond that. And it produces exactly one token at a time. Right, so an iterative token. Iterative token at a time. And it never goes backwards. And then you look at a brain, massive amounts of recursion. You have one learning procedure the whole time. You have these two lobes with a corpus callosum between them that's going back and forth like this. And we think. And then I definitely don't think in one token at a time. When I write code, I don't write one little character at a time.

`[21:05]` **SPEAKER_01:** I never go backwards. And I'm going backwards. I'm recursively improving. I'm going backwards again and again. I'm thinking in concepts.

`[21:13]` **SPEAKER_00:** There's this dynamic process that's emitting concepts and then higher level concepts and then lower level manifestations of them.

`[21:19]` **SPEAKER_01:** And I'm sure that may be happening inside the LLM, but it's almost like, it's almost like stuck. It can't do more than in one step, even though it might want to. Right. Because it has to. That's the way that we trained it.

`[21:31]` **SPEAKER_00:** Right, like it might have all that in the LLM, but then it's sort of bottlenecked ultimately. It's action space. It's action space is one.

`[21:37]` **SPEAKER_01:** Is one token at a time. And so I think that that's where I think about diffusion. There's like two main things that diffusion gives me. It doesn't get me all the way to pass my squint test, but it gives me two things that for sure the brain is doing. Number one, all of biology and nature is randomness. Randomness is good. And what is diffusion doing? It's leveraging randomness. If you give me data, I noise it up, and from that I can learn about the data. And like, can the brain add noise to input data?

`[22:06]` **SPEAKER_01:** Absolutely. Like absolutely. Like neurons are massively random. There's log normal distributions, spike patterns, and things like that. And the other one is this emission of one thing at a time versus thinking in concepts and then decoding into a big chunk of text and thought and visioning of the previous thoughts and things like that. And so I think diffusion gives me both of those things for sure.

`[22:27]` **SPEAKER_00:** People have probably heard of stable diffusion as a very common application of this. It's an image generation model that was pretty widely available for the last few years. What people may not be so aware of is all the other ways that diffusion is used in the last few years in products that people are widely using. So what are some of the areas in which diffusion is most widely accessible?

`[22:47]` **SPEAKER_01:** Yeah, it's really any mapping from very high dimensional P data to very high dimensional action spaces or P data that you may want to map to. And so I mean, yeah, of course everyone knows generating images because we've done mid-journey and things like that and even more modern versions of that with Sora and VO and Flux and SD3 now and things like that. And we've generating videos which is just images stapled together and video gen and image gen and things like that. However, there's so many more applications that now we're seeing.

`[23:19]` **SPEAKER_01:** That's the most exciting part in my view of all the new applications. And so whether or not you're now creating sentences, I mean, diffusion LLMs was one of the biggest topics that we saw in EurIPS, whether it's continuous diffusion LLMs or discrete diffusion LLMs. It's writing code now. It's creating proteins. I mean, DeepMind has won the Nobel Prize for that. There is robotic policies, this diffusion policy thing, which I think might actually be one of the biggest uses of it and will result in like robotics.

`[23:51]` **SPEAKER_01:** It's actually working. It was the robot actually working. There's weather forecasting for the GenCast. It's the most accurate weather forecasting system in the world. It's really anything. And even like I mentioned, Harrison working on the diffs diffusion for failure sampling, just like sampling for failures and like bad things that could happen. We can do that as well.

`[24:11]` **SPEAKER_00:** So a lot of the products where we see people actually using AI, especially for things other than just text-based chat, a lot of them are using diffusion, especially our images, videos, increasingly now things like code and the life sciences. So yeah, pretty wide berth of things. Yeah.

`[24:26]` **SPEAKER_01:** In fact, I would say the only two holdouts right now where state-of-the-art is not diffusion, diffusion has eaten all of AI except two. AR LLMs still are outperforming and gameplay and things like AlphaGo. And so MCTS is still state-of-the-art for those types of things. And so we haven't seen diffusion really take a step in those two areas, but more research is needed.

`[24:48]` **SPEAKER_00:** So to bring the conversation to a head now, how should people think about this research area, either as researchers contributing to the field or as founders looking to build a new product?

`[24:58]` **SPEAKER_01:** Yeah. I mean, I would think about maybe this falls in two camps. If you're training models yourself or if you're using models and not in the business of training models. If you're in the business of training models, I would seriously look at diffusion. I don't care what your application is. You should be looking at this procedure, even if it's just to get a latent space that you can then train off of. And so there's no application in machine learning that I don't think you should be heavily looking at diffusion procedures

`[25:28]` **SPEAKER_01:** as a fundamental piece of your training loop. In the case of people who are not training models, I would just update your prior on how good these things are getting. And if you just look at in the last five years on how good image generation got from mid-journey when we first came out to VO and Sora and Flux and SD3 now, it's like a thousand times better, right? The answer was just scale it up. And that takes time and that takes money and all those things and data. And now you apply that to proteins.

`[26:00]` **SPEAKER_01:** You apply that to DNA. You apply that to robotics policies, self-driving car. I mean, skate to where the puck's going to go. All these things are going to work. And we're watching it happen. It may cost money and time and those kinds of things. But those are solvable things. Those are tractable problems that we can go solve. And also the core procedure of diffusion is getting better. That's another major factor. A lot simpler. A lot simpler. And it's getting like it's just working better.

`[26:27]` **SPEAKER_01:** And so skate to where the puck's going to go. Bet that rows of the robot will work in people's homes. Bet that the protein folding is only going to get better and now we're going to apply that to DNA and all these other metabolomics and things like that.

`[26:39]` **SPEAKER_00:** We see founders develop new models for robotics or for text generation or for video using diffusion. And we see founders who are using all of these methods coming from other places build companies on top of them. And it seems like there's this whole new wave of companies that can be built on either end of this now. Right. I think it's going to redefine the entire economy. Thanks so much for joining us. We're going to keep digging in on topics related to machine learning research like diffusion.

`[27:01]` **SPEAKER_00:** Can't wait to see you at the next one.
