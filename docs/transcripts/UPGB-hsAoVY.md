# 全文转录 · 微调的强力替代方案:给 LLM 装上"高跷"的递归自我改进

> ▶ [YouTube](https://www.youtube.com/watch?v=UPGB-hsAoVY) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/UPGB-hsAoVY.md) &nbsp;·&nbsp; The Powerful Alternative To Fine-Tuning
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_04:** The world is changing so quickly. This is probably a little bit obvious, but you should just try things. And like every day, do something with AI. Last summer, I took a weekend and used GPT-5 to help me build an iPhone app. I hadn't done that in a decade. So fast. Yeah, it's so fast and so easy. And that was, you know, an age ago. That was like eight months ago. Now it's even faster and easier. Don't limit yourself. Like anything that you imagine, you should just try to use AI and see how far you can get with it.

`[00:30]` **SPEAKER_04:** And you'll be making the world better.

`[00:40]` **SPEAKER_02:** Welcome to another episode of The Light Cone. Ian Fisher is the co-founder and co-CEO of Poetic, which is building recursively self-improving AI reasoning harnesses for LLMs. Previously, he spent a decade as a researcher at Google DeepMind and founded a mobile dev tools company through YC years ago. Welcome, Ian. Thank you. I'm so happy to be here. What is Poetic? How's it different than RL? You know, how's it different than context engineering?

`[01:06]` **SPEAKER_04:** At Poetic, what we're building is a recursively self-improving system. And so recursive self-improvement is this, you know, kind of the holy grail of AI where the AI is making itself smarter. The core insight that we had is that we could do recursive self-improvement far faster and cheaper than all of the other ways that people had been proposing to do this. And so obviously, I can't go into details about what that is, what our particular approach is. But most of the approaches out there involve, you know,

`[01:38]` **SPEAKER_04:** they require you to train a new LLM from scratch. And training LLMs from scratch costs, you know, hundreds of millions of dollars and takes months of effort. And so the...

`[01:49]` **SPEAKER_02:** And then Anthropic or OpenAI will come along and just eat your lunch in the next model release.

`[01:53]` **SPEAKER_04:** Right, right. And, you know, of course, Anthropic and OpenAI and Google, they're exploring recursive self-improvement, but typically at that level of having the, you know, having to train a new model, they're looking for every step of self-improvement that they do.

`[02:07]` **SPEAKER_02:** I mean, that seems like actually the, like, defining thing that a startup really, really wants. Like, I know that I want to take advantage of whatever the next model is, but the second you're in fine-tuning land, I'm spending, you know, millions to hundreds of millions of dollars. And then guess what? Like, I just lit it on fire because, you know, the next version of the frontier model comes out, and I'll never catch up. Whereas, like, working with your systems means that I will always have the thing

`[02:34]` **SPEAKER_02:** that is best for me. Better than the thing that's out of box. And that's sort of like the Holy Grail.

`[02:39]` **SPEAKER_04:** Yeah, we think that this is incredibly valuable to anybody who's building on top of large language models. And we don't view the, you know, the frontier models as competitors. They're, you know, they're the ones that were using the stilts, you know, building stilts to stand on top of. But if we didn't have that foundational layer, then, you know, Poetic couldn't exist.

`[02:59]` **SPEAKER_02:** Yeah, I mean, being the smartest model, you know, it's a game of inches, actually. And, like, so those inches matter. They matter a lot. Right, right. How do we actually get started? I mean, you've built something that basically any startup could use that it's sort of like stilts, really.

`[03:15]` **SPEAKER_04:** We have built a system that can automatically generate systems for your particular problem that will always outperform the underlying language models. And without kind of the massive expense, as you're saying, about the bitter lesson, where, you know, what would you have done without Poetic? You probably would have said, OK. We're going to first collect a large data set, you know, like tens of thousands of examples for our particular problem that we're working on. And we're going to fine-tune, you know, the best model we can get our hands on.

`[03:45]` **SPEAKER_04:** Maybe that's, you know, one of the frontier models, or maybe it's an open weights model. It doesn't particularly matter. You're going to spend a lot of money on that fine-tuning. The compute is so expensive. And then at the end of it, you have something that, you know, works better than the thing that you fine-tuned on top of. But by then, a new model has come out. And it's better than the thing that you fine-tuned on top of. It's better than the thing that you fine-tuned. You know, you fine-tuned, you know, like three years ago on top of GPT-3.5 or whatever.

`[04:10]` **SPEAKER_04:** And then GPT-4 comes out, and it just blows you out of the water. And so are you going to do that again? Or are you going to go out of business? And like, in some cases, the latter. With Poetic, what we end up giving you is a, you know, people are calling these things harnesses now. But, you know, or an agentic system, or whatever you want to call it, that sits on top of one or more language models. And it performs better than them. And when the new model comes out, that same harness is perfectly compatible with it.

`[04:41]` **SPEAKER_04:** And you don't need to change anything to get the, you know, an even bigger performance bump. Additionally, we can, you know, continue to optimize for this new model, whatever the new model is that you want to use, and, you know, make it even better. But you don't lose out on, you know, hundreds of millions of dollars. In fact, we do this so much more cheaply. Yeah.

`[05:03]` **SPEAKER_02:** Than fine-tuning would cost, as well. And you've done this actually a bunch of times, right? Like, I remember when you first came out with your paper in December of last year, you shot to the top of Arc AGI v2. And then you've done this a bunch of times for other benchmarks, too. What was that like?

`[05:19]` **SPEAKER_04:** Arc AGI v2 was a, this was kind of, you know, us coming out of stealth, letting people know that we could tackle these really hard problems. And in particular, you know, we wanted to show that our system could generate these, you know, these problems. And so, I mean, that was the first step. Yeah. Awesome. generate these, what we call, you know, we call our system like the poetic metasystem, can generate reasoning systems that are highly effective. Gemini 3, DeepThink had just come out

`[05:43]` **SPEAKER_04:** and they were, you know, really quite dramatically at the top of the leaderboard at 45%. And two days later, we released our results where we were showing that we could get

`[05:57]` **SPEAKER_02:** a lot higher than that. So they come out with SOTA and then you come in right above them every single time. Yeah. Like wild to see, honestly. That's what it's like to have stilt, you know, like whatever model comes out, you can be taller than that one with poetic, which is like, that's

`[06:13]` **SPEAKER_04:** so awesome. Yeah. So the interesting thing is that we were half the cost of Gemini 3, DeepThink because we were building on top of Gemini 3 Pro, which is a much cheaper model. But we still got in the end, a nine percentage point improvement. On the official verification. So they were at 45% and we were and like 70 something dollars and we were at 54% and $32 per problem. So recently you guys just announced some incredible results

`[06:40]` **SPEAKER_01:** for Humanity's last exam. Can you tell us more about those? Humanity's last exam is a set of

`[06:47]` **SPEAKER_04:** 2,500 really, really hard questions written by experts in many different domains. They're meant to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for the people who don't know how to do it. And so we're going to be challenging even for PhDs in those fields. AI hasn't passed it yet, but we got to 55%, which is almost two percentage points higher than the

`[07:06]` **SPEAKER_04:** the previous state-of-the-art. Which came out just last week from Anthropic with Claude Opus 4.6. They got 53.1% and we got 55% on it. And one thing that Humanity's last

`[07:21]` **SPEAKER_01:** exam doesn't publish is the cost of getting those results. In your case, this run, run was done with less than around six figure. How much was it?

`[07:31]` **SPEAKER_04:** MARK MANDELBACHER- We didn't publish any cost for this, but I can say that the optimization costs us less than $100,000, yeah.

`[07:38]` **SPEAKER_01:** MELANIE WARRICK- Which is impressive, because each of these big foundation modeled train runs are in the hundreds of millions of dollars. And you guys, as a company, you're only seven people?

`[07:49]` **SPEAKER_04:** MARK MANDELBACHER- That's right, yeah. Seven research scientists and research engineers, yeah.

`[07:53]` **SPEAKER_01:** MELANIE WARRICK- That's impressive. And I think the thing that's very interesting about your approach is sort of taking a very scientific approach to the emergent behaviors that a lot of the best founders are doing with models. I think a lot of founders that get very good results for agents, they treat the underlying model as a common layer that you can switch in between. And there's a certain task, for example, for GPT 5.2, like very hard to verify bugs get sent to that, versus architecture that gets sent to clot

`[08:25]` **SPEAKER_01:** 4.2. Or 4.6. But you're kind of doing this automatically, instead of having a human conducting, is very impressive. I think there's something more special going on underneath. Can you tell us a bit about how it works?

`[08:37]` **SPEAKER_02:** MARK MANDELBACHER- Yeah, it sounds magical. So what can you tell us?

`[08:40]` **SPEAKER_04:** MARK MANDELBACHER- Right, so you're getting at a core, a really core thing. These harnesses, they are code, prompts, data, built on top of one or more language models. And so this is something that, in principle, you can build by hand. Or with like cloud code, or whatever. But in practice, it takes a lot of work to do these, to have all the insights to make these work well. And so the core technology that we've developed at Poetic is recursive self-improvement. So we have a recursively self-improving system,

`[09:16]` **SPEAKER_04:** which we call the Poetic Metasystem. The output of that system is systems that solve hard problems, where a hard problem is something that, if you can solve it, you can solve it. If you gave it to GPT-5-2, it would struggle to give you a reliable, robust result, just to use an example. So this is a very big advantage for us. We can generate these systems in a much more automated manner, which means that we can do it much more quickly and much more cheaply than if you hired a team yourself

`[09:44]` **SPEAKER_04:** to try to make your own agent to solve your particular task. But not only that, since this is really an automated optimization process. If you already have done that work, you're a startup that's going after a particular vertical, and you think you understand your problem pretty well, you've put together your agent, and maybe it's working pretty well, but you know you can get something better or you really need something better, then you can bring that to us. And we can optimize that entire agent or pieces of that agent.

`[10:19]` **SPEAKER_04:** We could optimize just the prompts, just the reasoning strategies. There's a lot of different things that we can do, depending on your particular needs.

`[10:26]` **SPEAKER_01:** MELANIE WARRICK- It sounds like this is a complete different paradigm than RL, because we went through the S-curve of regular pre-training, RL with when OpenAI released 01, and now this feels like a new one. It sounds special. It rhymes a lot with RNNs, which is a whole different paradigm than RL, right?

`[10:46]` **SPEAKER_04:** JOSE QUINONEZ- It's going to depend on the particular task, the particular type of problem that we're going after, that we're trying to solve, and the underlying models that we're working with. But effectively, you could say like each model or each set of models that we're working with will have their own S-curve. The poetic system, the poetic metasystem itself, is also going to have its own S-curve. And so as a poetic metasystem gets better and as the underlying models get better, you'll find that the S-curve that you're dealing with

`[11:15]` **SPEAKER_04:** keeps shifting higher and higher until ultimately either you saturate or like- MELANIE WARRICK- Reach AGI? JOSE QUINONEZ- Yeah, reach AGI, reach super intelligences, yeah.

`[11:24]` **SPEAKER_02:** MELANIE WARRICK- Given that it's stilts, you might like hit the ceiling first then.

`[11:27]` **SPEAKER_04:** JOSE QUINONEZ- That's the goal, right? JOSE QUINONEZ- Yeah. MELANIE WARRICK- You want to hit the ceiling first with poetic.

`[11:30]` **SPEAKER_02:** JOSE QUINONEZ- I think a lot of startups that we work with, and then in my spare time, I do a bunch of context engineering. And then the thing is we're sort of like tuning it, tuning evals, tuning like we're context stuffing ourselves. What does that even feel like to have a recursively self-improving version of prompt engineering and context engineering?

`[11:52]` **SPEAKER_04:** JOSE QUINONEZ- We don't spend a lot of time looking at the particular data that we're working with. Instead, we're letting the poetic meta system look at that data. And so the meta system, if it thinks that it needs to put more things into context, do more context stuffing or whatever, it'll do that. If it needs to generate a bunch of examples to get better performance, it'll do that for you, right? It was pretty interesting to look at the prompt outputs, and particularly I'd say for ArcAGI,

`[12:26]` **SPEAKER_04:** in that I think you can read those and say, well, that's not what a human would have written pretty clearly. And there's some unexpected stuff. And it made some really simple examples. And one of the examples is actually wrong. But we didn't change it. We're like, this is the thing that output. We'll just leave it be. We don't want to go in and monkey around with things. And so historically in machine learning, you do this. You don't want to go in and monkey around with things. And so historically in machine learning,

`[12:53]` **SPEAKER_04:** And so historically in machine learning, And so historically in machine learning, And so historically in machine learning, learning you always you know it's like the the rule was you have to know your data set really well um but now we're kind of outsourcing that to the ai itself where the ai is the it's the ai's job to understand the data set and figure out where are the failure modes um and where are the kind of robust reasoning strategies that uh the model that that the agent could uh use um to get

`[13:18]` **SPEAKER_02:** better performance how much of it is like much the output is much better prompts and then how much of it is like the harness itself uh context stuffing or summarizing in the right way or re-ranking in the right way so that like you have some number of like mega llm calls and then how do you get

`[13:34]` **SPEAKER_04:** the most out of um each of those calls yeah and so that definitely varies per problem but uh what we've seen uh in fact uh our our last paper at deepmind was not doing this recursive self-improving stuff but we were um we were showing that you could build these harnesses um maybe you could build these harnesses um maybe you could build these harnesses um maybe you could manually to solve really hard problems and what we saw is there is that uh you know we manually optimized the prompts really hard for these very hard problems and that got us a little bit of the

`[14:03]` **SPEAKER_04:** way uh in this particular case you know the hardest the hardest task we were working on we got like to five percent performance with gemini 1.5 flash this was a while ago and then when we added on the the reasoning strategies we went from five percent to ninety five percent uh and so uh this is typically what we see you know like everybody's out there kind of doing some amount i wouldn't say everybody but many people are out there kind of doing some amount of automated prop prompt optimization every you know jepa is this very popular paper everybody's kind of

`[14:35]` **SPEAKER_04:** re-implementing that that will get you some performance improvements but it's very far from everything that you can get if you actually think about these reasoning strategies that are really going to be written in code rather than in just better prompts so if

`[14:51]` **SPEAKER_00:** startups want to use poetic to put their agent on stilts what should they do yeah so right now

`[14:58]` **SPEAKER_04:** uh we haven't released anything yet but uh if you go to poetic.ai there is a button you can click to get uh sign up for early access and if you're a startup or a company who has a really hard problem and you've tried everything that you can to make it reliable and robust and you just can't get all the way there you you need something more then uh let us know we're looking for problems like that uh so just tell us tell us what it is that you're working on and uh we'll reach out you'll be the first to know when we're when we're ready to work with you

`[15:30]` **SPEAKER_02:** i mean if you're at the top of um humanity's last exam then i mean that's that's pretty big so it's you're all you're already all the way out there at soda and then i guess the stilts basically let any agentic company become soda that's the idea yeah yeah

`[15:45]` **SPEAKER_04:** and you know we view the rkgi results and the humanities last exam results as showing kind of two different uh capabilities that we have we can really improve your reasoning and we can really improve uh deep knowledge extraction uh from these models and then you're just totally vaccinated

`[16:01]` **SPEAKER_02:** against the bitter lesson exactly yc's next batch is now taking applications got a startup in you apply at ycombinator.com apply it's never too early and filling out the app will level up your

`[16:15]` **SPEAKER_03:** idea okay back to the video a slight sort of change change a topic but something i was curious about you arrived at google over a decade ago when they acquired your first yc startup a portable a portable was it's importing mobile apps cross-platform right like android or whatever it's quite different to um recursive self-improving agi um how did you make that leap what happened once you got to google um what made you think that you maybe wanted to shift down do something

`[16:44]` **SPEAKER_04:** different and just would love to hear that story the acquisition was this amazing opportunity to reflect on what i really wanted to be doing next right like google was in the you know itself is a place where you can do so many different things uh so i spent some time thinking about um where uh where i wanted to go next in in uh in my journey i realized that the problems that i was most excited about were really actually ai and uh and robotics and the best people in the world many of them in those fields were at google at the time

`[17:27]` **SPEAKER_04:** and so i went and talked to them they let me come join you know a new ai robotics team in google research which was this amazing opportunity for me since that wasn't my background my background was like computer security and then this cross-platform mobile you know it's systems building uh stuff i was able to join this team and i didn't really want to be doing robotics it was more aspirational at that moment uh but i was really um passionate about machine learning so i just i made a very hard switch into just doing

`[18:04]` **SPEAKER_04:** machine learning research uh and did that for you know about a decade at google and then google and then deepmind what's maybe some advice that you have today for engineers who want to get

`[18:16]` **SPEAKER_03:** Maybe some advice that you have today for engineers who want to get into sort of more of the AI side, probably the applied AI and build startups around AI, like how should they think about that?

`[18:28]` **SPEAKER_04:** You know, the world is changing so quickly. This is probably a little bit obvious, but you should just try things and like every day do something, do something with AI, always try to push yourself to find the boundaries of what they're capable of and build the things that you want to build, right? Even for me, you know, last summer, I took a weekend and used GPT-5 to help me build an iPhone app. I hadn't done that in a decade. So fast. Yeah, it's so fast and so easy. And that was, you know, that was an age ago.

`[19:07]` **SPEAKER_04:** That was like eight months ago. Now it's even faster and easier. Don't limit yourself. Like anything that you imagine, you should just try to use AI and see how far you can get with it and you'll be, you know, making the world better.

`[19:19]` **SPEAKER_02:** That's all we have time for today. But Ian, thank you so much for giving us all stilts. We can't wait to use it at YC. I can't wait to use it for Gary's list. I mean, there's just so much to do.

`[19:30]` **SPEAKER_04:** So yeah, thank you for having me. This was a lot of fun.
