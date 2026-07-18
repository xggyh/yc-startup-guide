# 全文转录 · 对话 Claude Code 之父 Boris Cherny:如何为「六个月后的模型」而造

> ▶ [YouTube](https://www.youtube.com/watch?v=PQU9o_5rHC4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/PQU9o_5rHC4.md) &nbsp;·&nbsp; Inside Claude Code With Its Creator Boris Cherny
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_02:** At Anthropic, the way that we thought about it is we don't build for the model of today. We build for the model six months from now. That's actually like still my advice to founders that are building on LLMs. Just try to think about like, what is that frontier where the model is not very good at today? Because it's going to get good at it. All of quad code has just been written and rewritten and rewritten and rewritten over and over and over. There is no part of quad code that was around six months ago.

`[00:21]` **SPEAKER_02:** You try a thing, you give it to users, you talk to users, you learn. And then eventually you might end up at a good idea. Sometimes you don't.

`[00:26]` **SPEAKER_04:** Are you also in the back of your mind thinking that maybe like in six months, you won't need to prompt that explicitly, but the model will just be good enough to figure out on its own?

`[00:34]` **SPEAKER_02:** Maybe in a month.

`[00:36]` **SPEAKER_00:** No more need for a plan mode in a month?

`[00:38]` **SPEAKER_04:** Oh my God.

`[00:46]` **SPEAKER_01:** Welcome to another episode of The Light Cone. And today we have an extremely special guest, Boris Cherny, the creator, engineer of quad code. Boris, thanks for joining us. Thanks for having me. Thanks for creating a thing that has taken away my sleep for about three weeks straight. I am very addicted to quad code and it feels like rocket boosters. Has it felt like this for people like for, you know, months at this point? I think it was like end of November is where a lot of my friends said like something changed.

`[01:19]` **SPEAKER_02:** I remember for me, I felt this way when I first created quad code and I didn't yet know if I was onto something. I kind of felt like I was onto something. And then that's when I wasn't sleeping. And that was just like three straight months. This was September 2024. Yeah, it was like three straight. I didn't take a single day vacation, worked through the weekends, worked every single night. I was just like, oh my God, this is, I think this is going to be a thing. I don't know if it's useful yet because it couldn't actually code yet.

`[01:45]` **SPEAKER_01:** If you look back on those moments to now, like what would be like the most surprising thing about this moment right now?

`[01:52]` **SPEAKER_02:** It's unbelievable that we're still using a terminal. That was supposed to be the starting point. I didn't think that would be the ending point. And then the second one is that it's even useful because, you know, at the beginning it didn't really write code. It didn't write code. It didn't write code. It didn't write code. It didn't write code. Even in February when we GA'd it, it wrote maybe like 10% of my code or something like that. I didn't really use it to write code. It wasn't very good at it.

`[02:09]` **SPEAKER_02:** I still wrote most of my code by hand. So the fact that it actually like our bets paid off and it got good at the thing that we thought it was going to get good at because it wasn't obvious. At Anthropic, the way that we thought about it is we don't build for the model of today. We build for the model six months from now. And that's actually like still my advice to founders that are building on LLMs is, you know, just try to think about like, what is that frontier? Where the model is not very good at today because it's going to get good at it and you

`[02:37]` **SPEAKER_02:** just have to wait.

`[02:38]` **SPEAKER_04:** Going back, do you remember when you first got the idea? Can you just talk us through that? Like, was there something like a spark or what was even the first version of it in your mind?

`[02:46]` **SPEAKER_02:** You know, it's funny. It was like, it was so accidental that it just kind of evolved into this. You know, as Anthropic, I think for Ant, the bet has been coding for a long time and the bet has been the path to safe AGI is through coding. And this is, this is. It's kind of always been the idea and the way you get there is you teach the model how to code, then you teach it how to use tools, then you teach it how to use computers. And you can kind of see that because the first team that I joined at Anthropic, this was the

`[03:14]` **SPEAKER_02:** Anthropic Labs team, and it produced three products. It was quad code, MCP and the desktop app. So you can kind of see how these like weave together. The particular product that we built, you know, like no one, no one asked me to build a CLI. We kind of knew maybe it was time to build some kind of coding product. Because it seemed like the model was ready, but no one had yet really built a product that harnessed this capability. So like still there's this insane feeling of product overhang.

`[03:41]` **SPEAKER_02:** But at the time it was just like even crazier because like no one had built this yet. And so I sort of like hacking around and I was like, OK, we build a coding product. What do I have to do first? I have to understand how to use the API because I hadn't used the Anthropic API at that point. And so I just built like a little terminal app to use the API. That's all that it did. And it was a little chat app because. Think about the, you know, AI applications at the time. And, you know, for non coders today, most what are most people using is just a chat app.

`[04:09]` **SPEAKER_02:** So that's what I built. And, you know, it was in a terminal. I can ask questions. I give answers. Then I think tool use came out. I just want to try out tool use because I don't really understand what this is. I was like, tool use, this is cool. Is this actually useful? Probably not. Let me just try it.

`[04:23]` **SPEAKER_04:** You built it in a terminal just because it was the easiest way to get something up and running. Yes, because I didn't have to build a UI.

`[04:29]` **SPEAKER_02:** OK. It was just me.

`[04:30]` **SPEAKER_04:** At that point, it was like the IDEs cursor. Windsurf were the things that were really taking off. Were you sort of under any pressure or getting lots of suggestions of, hey, like, we should build this out as a plugin or as a as a fully featured ID itself?

`[04:43]` **SPEAKER_02:** There was no pressure because we didn't even know what we wanted to build. Like the team was just in explore mode. You know, like we didn't we know vaguely we wanted to do something in coding, but it wasn't obvious what no one was high confidence enough. That was like my job to figure out. And so I gave the model the bash tool. That was the first tool that I gave it just because I think that was literally the example in our docs. I just like took the examples in Python. I just ported it to TypeScript because that's how I wrote it.

`[05:07]` **SPEAKER_02:** You know, I didn't know like what the model could do with bash. So I asked it to like read a file. It could like cat the files like that was cool. And then I was like, OK, like, what can you actually do? And I asked it, what music am I listening to? You wrote some like Apple script to script my my Mac and look up the music in my music player. Oh, my God. And this was sauna 3.5. And, you know, like, I didn't think the model could do that. And that was my first, I think, ever fueled the AGI moment.

`[05:33]` **SPEAKER_02:** Whereas it's like, oh, my God, the model, it just wants to use tools. That's all it wants.

`[05:38]` **SPEAKER_00:** That's kind of fascinating. I mean, it's very kind of contrarian that Clockwork works so well in such an elegant, simple form factor. I mean, terminals have been around for a really long time. And that seemed to be like a good design constraint that allowed a lot of interesting developer experiences. It doesn't feel like working. It just feels fun as a developer. I don't think about files. I don't know where everything is. And that came by accident almost.

`[06:07]` **SPEAKER_02:** Yeah, it was an accident. I remember. So after the terminal started to take off internally and honestly, like after building this thing, I think like two days after the first prototype, I started giving it to my team just for dogfooding. Because, you know, like, you know, if you come up with an idea and it seems useful, the first thing you want to do is you want to give it to people to see how they use it. And then I came in the next day. And then Robert, who sits across from me, he's another engineer, he just like had quad code on his computer.

`[06:32]` **SPEAKER_02:** And he was like using it to code. So I was like, what are you what are you doing? Like, this thing isn't ready. It's just a prototype. But yeah, it was already useful in that form factor. And I remember when we did our launch review to kind of launch quad code externally. This was in December, November or something like that. In 2024, Dario asked and he was like, the usage chart internally, like the DAO chart is like vertical. Are you like forcing engineers to use it? Like, why are you mandating them?

`[06:58]` **SPEAKER_02:** And I was just like, no, no, we didn't. We did. I just like posted about it. And they had just been like telling each other. About it, honestly, it was it was just accidental. We started with the CLI because it was the cheapest thing and it just kind of stayed there for a bit.

`[07:09]` **SPEAKER_04:** So in that 2024 period, what how are the engineers using it? Were they shipping code with it yet or were they using it in a different way?

`[07:18]` **SPEAKER_02:** The model is not very good at coding yet. I was using it personally for automating Git. I think at this point I've probably forgotten most of my Git because quad code has just been doing it for so long. But yeah, like automating bash commands, that was a very early use case. I think it was like operating like Kubernetes and kind of things like this. People were using it for coding, so there were some early signs of this. I think the first use case was actually writing unit tests because it's a little bit lower risk and the model is still pretty bad at it.

`[07:44]` **SPEAKER_02:** But people were kind of figuring it out and they were figuring out how to use this thing. And one thing that we saw is people started writing these markdown files for themselves and then having the model read that markdown file. And this is where QuadMD came from. Probably the single for me biggest principle and product is wait and demand. And. Just every bit of this product is built through wait and demand after their initial CLI. And so QuadMD is an example of that. There's this other general principle that I think is maybe interesting where you can build for the model and then you can build scaffolding around the model in order to improve performance a little bit.

`[08:19]` **SPEAKER_02:** And depending on the domain, you can improve performance maybe 10, 20%, something like that. And then essentially the gain is wiped out with the next model. So either you can build the scaffolding and then get some performance gain and then rebuild it again. Or you just wait for the next model and then you kind of get it for free. The QuadMD and kind of the scaffolding is an example of that. And really, I think that's why we stayed in the CLI is because we felt there is no UI we could build that would still be relevant in six months because the model was improving so quickly.

`[08:48]` **SPEAKER_01:** Earlier we were saying like we should compare CloudMDs, but you said something very profound, which is, you know, yours is actually very short, which is almost like the opposite of what, you know, people might expect. Why is that? What's in your CloudMD?

`[09:01]` **SPEAKER_02:** Okay. So I checked. I checked this before we came. So my, my QuadMD has two things. One is there, it's just two lines. So the first line is whenever you put up a PR, enable auto merge. So as soon as someone accepts it, it's merged. That's just so I can like code and I don't have to kind of go back and forth with CR or whatever. And then the second one is whenever I put up a PR, post it in our internal team stamps channel, just so someone can stamp it and I can get unblocked. And the idea is every other instruction is in our QuadMD.

`[09:32]` **SPEAKER_02:** That's checked. It's checked into the code base and it's something our entire team contributes to multiple times a week and very often I'll see someone's PR and they make some like mistake that's totally preventable and I'll just literally tag Claude on the PR. I'll just do like add Claude, you know, like add this to the QuadMD and I'll do this, you know, like many times a week.

`[09:51]` **SPEAKER_01:** Do you have to like compact the ClaudeMD? Like I've definitely reached a point where I got the message at the top saying your ClaudeMD is like thousands of tokens now. What do you do when you guys hit that?

`[10:01]` **SPEAKER_02:** So our ClaudeMD is actually pretty short. I think it's like a couple of thousand tokens, maybe something like that. If you hit this, my recommendation would be delete your QuadMD and just start fresh. Interesting. I think a lot of people like they try to overengineer this, right? And really like the capability changes with every model. And so the thing that you want is do the minimal possible thing in order to get the model on track. And so if you delete your QuadMD and then, you know, the model is getting off track, it does the wrong thing.

`[10:27]` **SPEAKER_02:** That's when you kind of add back a little bit at a time. And what you're probably going to find is with every model, you have to add less and less. For me, I consider myself a pretty average engineer, to be honest. Like I don't use a lot of fancy tools. Like I don't use like Vim. I use, you know, VS Code because it's simpler.

`[10:42]` **SPEAKER_03:** Wait, really? I would have assumed that because you built this in the terminal that you were sort of like a diehard terminal like Vim only person, you know, screw those VS Code people.

`[10:52]` **SPEAKER_02:** Well, we have people like that on the team. You know, like Adam Wolf, for example, he's on the team. He's like, you will never take Vim for my cold, dead hands. Yeah. So there's definitely a lot of people like that on the team. And this is one of the things that I learned. Early on is every engineer likes to hold their dev tools differently. They like to use different tools. There's just no one tool that works for everyone. But I think also this is one of the things that makes it possible for quad code to be so good because I kind of think about it as what is the product that I would use that makes sense to me.

`[11:18]` **SPEAKER_02:** And so to use quad code, you don't have to understand Vim. You don't have to understand Tmux. You don't have to know how to like SSH. You don't have to know all this stuff. You just have to open up the tool and it will guide you. It will do all this stuff.

`[11:28]` **SPEAKER_01:** How do you decide how verbose you want like sort of the terminal to be? Like sometimes. Sometimes you have to go, you know, control O and check it out. And is it like internal bike shed battles around like longer, shorter? I mean, every user probably has a different opinion. Like how do you make those sorts of decisions? What's your opinion? Is it too verbose right now? Oh, I love the verbosity because basically sometimes it just like goes off the deep end and I'm watching. And then I can just read very quickly and it's like, oh, no, no, it's not that.

`[11:57]` **SPEAKER_01:** And then I escape and then just stop it. And then it just like stops an entire bug farm like as it's happening. I mean, that's usually when I didn't do plan mode properly.

`[12:05]` **SPEAKER_02:** This is something that we probably change pretty often. I remember early on. This is maybe six months ago. I tried to get rid of bash output just internally just to like summarize it because I was like these giant long bash commands. I don't actually care. And then I gave it to anthropic employees for a day and everyone just revolted. I want to see my dash because it actually is quite useful for, you know, like for something like git output. Maybe it's not useful. But if you're running, you know, like Kubernetes jobs or something like this, you actually do want to see it.

`[12:32]` **SPEAKER_02:** We recently hit. The hid the file reads and file searches. So you'll notice instead of saying, you know, like read food, MD, it'll said, you know, like read one file search, search one pattern. And this is something I think we could not have shipped six months ago because the model just was not ready. You would, you know, it's still read the wrong thing pretty often. As a user, you still have to be there and kind of catch it and debug it. But nowadays, I just noticed it's on the right track almost every time.

`[12:55]` **SPEAKER_02:** And because it's using tools so much, it's actually a lot better just to summarize it. But then we shipped it. We dog fooded it for like a month. And then people on GitHub didn't like it. So there was a big issue where people like, no, like, I want to see the details. And that was a really great feedback. And so we added a new verbose mode. And so that's just like in slash config. You can enable verbose mode. And if you want to see all the file outputs, you can continue to do that. And then I put on the issue and people still still didn't like it, which is, again, awesome, because like my favorite thing in the world is just hearing people's feedback and hearing how they actually want to use it.

`[13:27]` **SPEAKER_02:** And so we just like iterated more and more and more to get that really good and to make it the thing that people want.

`[13:32]` **SPEAKER_01:** I'm amazed. Like how much. I enjoy fixing bugs now. And then all you have to do is have really good logging and then even just say, like, hey, check out that, you know, this particular object messed up in this way. And it like searches the log. It figures everything out. It can like go into your you can make a production tunnel and look at your production DB for you. It's like this is insane. But fixing is just going to century copy mark down, you know, pretty soon it's just going to be straight MCP.

`[13:59]` **SPEAKER_01:** It's like an auto bug fixing like and test making. Sort of what's the new term they call it, like making a startup factory.

`[14:08]` **SPEAKER_03:** Oh, yeah, right.

`[14:09]` **SPEAKER_01:** There's like all these concepts now of rather than having to review the code, you know, I'm I'm old school. So I like the verbosity. I like to say, oh, well, you're doing this, but I want you to do that. Right. But there's a totally different school of thought now that says, like, any time a real human being has to look at code, that's bad.

`[14:29]` **SPEAKER_02:** Yeah. Yeah.

`[14:30]` **SPEAKER_01:** Yeah. And it's fascinating.

`[14:31]` **SPEAKER_02:** I think like Dan Chipper talks about this. A lot as kind of whenever you see the model, make a mistake, try to put in the quad MD, try to put it in like skills or something like this. What's reasonable. But I think there's this meta point that I actually struggle with a lot. And people talk about like agents can do this, agents can do that. But actually what agents can do, it changes with every single model. And so sometimes there's a new person that joins the team and they actually use quad code more than I would have used it.

`[14:56]` **SPEAKER_02:** And I'm just constantly surprised by this. Like, for example, there was a we had like a memory leak and we were trying to debug it. And by the way, like Jared Sumner has just been on this crusade killing all the memory leaks. And it's just been amazing. But before Jared was on the team, I had to do this and there was this memory leak. I was trying to debug it. And so I took a heap dump. I opened it in DevTools. I was looking through the profile. Then I was looking through the code and I was just trying to figure this out.

`[15:20]` **SPEAKER_02:** And then another engineer on the team, Chris, he just like asked quad code. He was like, hey, I think there's a memory leak. Can you like this and then like try to figure it out? And quad code like took the heap dump. It wrote a little tool for itself to like analyze the heap dump. And then it found the leak faster than I did. And this is just something I have to constantly relearn because my brain is still stuck somewhere six months ago at times.

`[15:43]` **SPEAKER_00:** So what would be some advice for technical founders to really become maximalists at the latest model release? It sounds like people off of fresh off of school or that don't have any assumptions might be better suited than maybe sometimes engineers who have been working at it for a long time. And how do the. Experts get better.

`[16:05]` **SPEAKER_02:** I think for yourself, it's kind of beginner mindset and I don't know, maybe just like humility. Like, I feel like engineers as a discipline, we've learned to have very strong opinions and senior engineers are kind of rewarded for this. In my old job at a big company, when I hired like architects and this kind of a type of engineer, you look for people that have a lot of experience and really strong opinions. But it actually turns out a lot of this stuff just isn't relevant anymore.

`[16:28]` **SPEAKER_02:** And a lot of these opinions should change because the model is getting better. Um. So I think actually the biggest skill is people that can think scientifically and can just think from first principles.

`[16:38]` **SPEAKER_00:** How do you screen for that when you try to hire someone now for for your team?

`[16:42]` **SPEAKER_02:** I sometimes ask about what's an example of when you're wrong. It's really good on, you know, some of these like classic behavioral questions, like not even coding questions, I think are quite useful because you can see if people can recognize their mistake in hindsight, if they can claim credit for the mistake and if they learn something from it. And I think a lot of these like very senior people, especially there are some founder types like this. But I think founder. Is in particular actually quite good at it.

`[17:05]` **SPEAKER_02:** But other people sometimes will never really take they'll never take the blame for a mistake. But I don't know, like for me personally, I'm wrong probably half the time, like half my ideas are bad and you just have to try stuff and, you know, you try a thing, you give it to users, you talk to users, you learn, and then eventually you might end up at a good idea. Sometimes you don't. And this is the skill that I think in the past was very important for founders. But now I think it's very important for every engineer.

`[17:32]` **SPEAKER_01:** Do you think. You would ever hire someone based on the cloud code transcript of them working with the agent because we're actually doing that right now. We just added just as a test, like you can upload a transcript of you coding a feature with cloud code or codex or whatever it is. Personally, I think that like it's going to work. I mean, you can figure out how someone thinks, like whether they're looking at the logs or not, like can they correct the agent if it goes off off the rails?

`[18:02]` **SPEAKER_01:** Like. Do they use plan mode, you know, when they use plan mode, do they make sure that there are tests or, you know, all of these different things that, you know, do they think about systems? Do they even understand systems like there's just so much that's sort of embedded in that that I imagine I just want like a spider, a spider web graph, you know, like in those video games like NBA 2K and it's like, oh, this person is really good at shooting or defense. It's like you can imagine a spider web graph of like, you know, someone's cloud code skill level.

`[18:30]` **SPEAKER_01:** Yeah. What would it, what would the skills be? What would be those? I mean, I think it's like systems testing must be like user behavior. I mean, there's got to be a design part for sure. Like product sense, maybe also just like automating stuff. My favorite thing in CloudMD for me is I have a thing that says for every plan, decide whether it's overengineered, underengineered or perfectly engineered and why.

`[18:53]` **SPEAKER_02:** I think this is something that we're trying to figure out, too, because I think when I look at engineers on the team that I think are the most effective, there's essentially two. It's very bimodal. There's one side where it's extreme specialists and so like I named Jared before, like he's a really good example of this and kind of the bun team is a really good example, just hyper specialist. They understand DevTools better than anyone else. They understand JavaScript runtime systems better than anyone else.

`[19:16]` **SPEAKER_02:** And then there's the flip side of kind of hyper generalists and that's kind of the rest of the team. And a lot of people, they span like product and info or product and design or, you know, like product and user research, product and business. I really like to see people that just do weird stuff. I think that's one of these things that was kind of a warning sign in the past because it's like, can these people actually build something useful?

`[19:38]` **SPEAKER_01:** That's the litmus test.

`[19:39]` **SPEAKER_02:** Yeah, that's the litmus test. But nowadays, like, for example, an engineer on the team, Daisy, she was on a different team and then she transferred onto our team. And the reason that I wanted her to transfer is she put up a PR for Cloud Code like a couple of weeks after she joined or something, and the PR was to add a new feature to Cloud Code. And then instead of just adding the feature, what she did is first. She put up a PR to give Cloud Code a tool so that it can test an arbitrary tool and verify that that works.

`[20:07]` **SPEAKER_02:** And then she put up that PR and then she had Cloud write its own tool instead of herself implementing it. And I think it's this kind of out of the box thinking that is just so interesting because not a lot of people get it yet. You know, like we use the Cloud Agent SDK to automate pretty much every part of development. It automates code review, security review, it labels all of our issues, it shepherds things to production. It does pretty much everything for us. But I think extremely important.

`[20:31]` **SPEAKER_02:** I mean, internally, I'm seeing a lot of people start to figure this out, but it's actually taken a while to figure out how do you use LMS in this way? How do you use this new kind of automation?

`[20:39]` **SPEAKER_01:** So it's kind of a new skill. I guess one of the funnier things that I've been having office hours with various founders about is you have like sort of the visionary founder who has like the idea they've like built this like crystal palace of the product that they want to build. They've totally loaded in their brain, you know, who the user is and what they feel and what they're motivated by. And then. Yeah. They're sitting in cloud code and they can do like, you know, 50 X work and then, but they have engineers who work for them who like don't have the, you know, crystal memory palace of like the platonic ideal of the product that the founder has and they can only do like five X work.

`[21:16]` **SPEAKER_01:** Are you hearing stories like that? There's usually a person who's like the core like designer of a thing and they're just like, you know, trying to blast it out of their brain. What's the nature of like teams like that? You know, it seems. Like that's almost a stable configuration. Like you're going to have the visionary who like now is unleashed, but you know, maybe going back to the top of it, like I'm experiencing this right now. It's like, oh, well, I'm only a solo person and you know, I need to eat and sleep and I have, you know, a whole job and it's like, how am I going to do this?

`[21:50]` **SPEAKER_02:** You know, you know, like we just launched quad teams and you know, this is a way to do it, but you can also just build your own way to do it. It's pretty easy. What's the vision for cloud teams? Just cooperation. It's like. There's this whole new field of like agent topologies that people are exploring. Like what are the ways they can configure agents? There's this one sub idea, which is uncorrelated context windows. And the idea is just multiple agents. They have fresh context windows that aren't as actually polluted with each other's context or their own previous context.

`[22:16]` **SPEAKER_02:** And if you throw more context at a problem, that's like a form of test and compute. Um, and so you just get more capability that way. And then if you have the right topology on top of it, so the agents can communicate in the right way, they're laid out in the right way, then they can just build bigger stuff. And so. Teams is kind of like one idea. There's a few more that are coming pretty soon. Um, and the idea is just maybe it can build a little bit more. I think the first kind of big example where it worked is our plugins feature was entirely built by a swarm over, over a weekend.

`[22:45]` **SPEAKER_02:** It just ran for like a few days. There wasn't really human intervention and plugins is pretty much in the form that it was when, when it came out.

`[22:52]` **SPEAKER_01:** How did you set that up? Like, did you spec out sort of the outcome that you were hoping for and then let it sort of figure out the details? And then. Like, let it run.

`[23:02]` **SPEAKER_02:** Yeah. An engineer on the team just gave, uh, gave quad a spec and, um, told quad to use a Asana board and then quad just put up a bunch of tickets on Asana and then spawned a bunch of agents. And the agent started picking up tasks. The main quad just gave it instructions and they all just figured it out.

`[23:19]` **SPEAKER_00:** Like independent, um, agents that didn't have the context of the bigger spec. Right.

`[23:23]` **SPEAKER_02:** Right. If you, if you think about the way that, uh, you know, like how our agents actually started nowadays and, you know, I haven't pulled the data on this. But I would bet the majority of agents are actually prompted by quad today in the form of, uh, sub-agents because like a sub-agent is just like a recursive quad code. That's all it is in the code. And it's just prompted by, we call her mama quad and that's all it is. And I, I think probably if you look at most agents, they're launched in this way.

`[23:47]` **SPEAKER_04:** My cloud insights just told me to do this more for debugging so that I get like, I spent a lot of time on debugging and it would just be better to have like multiple sub-agents spin up and like debug something in parallel. And so then I just like added that. To my Claude MD to just be like, Hey, like next time you try and fix a bug, like have one agent that like looks in the log, like one that looks in the code path.

`[24:07]` **SPEAKER_01:** That just seems sort of inevitable for weird, scary bugs. I try to, uh, fix bugs in plan mode. And then it seems to use the agents to sort of search everything. Whereas like when you're just trying to do it in line, it's like, okay, I'm going to do like this one task instead of search wide. This is something I do all the time too.

`[24:24]` **SPEAKER_02:** I, I just say if the, if the task seems kind of hard, this kind of research task, I'll calibrate the number of sub-agents I ask it to use. Based on the difficulty of the task. So if it's like really hard, I'll say like use three or maybe five or even 10 sub-agents research in parallel and then see what they come up with. I'm curious. So then why don't you put that in your Claude MD file? It's kind of case by case, you know, like quite MD, like what is it? It's just a, it's a shortcut.

`[24:48]` **SPEAKER_02:** Like if you find yourself repeating the same thing over and over, you put in the quad MD, but otherwise you don't have to put everything there. You can just prompt quad.

`[24:54]` **SPEAKER_04:** Are you also in the back of your mind thinking that maybe like in six months, you won't need to prompt that explicitly like the more. Yeah. Yeah. It'll just be good enough to figure out on its own.

`[25:03]` **SPEAKER_02:** Maybe in a month.

`[25:05]` **SPEAKER_00:** No more need for a plan mode in a month.

`[25:07]` **SPEAKER_02:** Oh my God. I think plan mode probably has a limited lifespan. Interesting.

`[25:11]` **SPEAKER_00:** That's some alpha for everyone here. What would the world look like without plan mode? Do you just describe it at the prompt level and it would just do it one shot it?

`[25:19]` **SPEAKER_02:** Yeah, we've, uh, we've started experimenting with this cause Claude code can now enter plan mode by itself. I don't know if you've, you guys have seen that.

`[25:25]` **SPEAKER_00:** Yeah.

`[25:26]` **SPEAKER_02:** So we're, we're trying to kind of get this experience really good. So it would enter plan. Mode the same point where a human would have wanted to enter it. So I think it's like, I think it's something like this, but actually plan mode. There's no, there's no big secret to it. All it does is it adds one sentence to the prompt. That's like, please don't code. That's all it is. You can, you can actually just say that. Yeah.

`[25:45]` **SPEAKER_00:** So it sounds like a lot of the feature development for Claude code is very much, uh, when we talk about YC, talk to your users and then you come and implemented it. It wasn't the other way that you had this master plan and then implemented all the features.

`[25:58]` **SPEAKER_02:** Yeah. Yeah. I mean, that, that's all it was like plan mode was we saw. Users that, that were like, Hey, Claude, come up with an idea, plan this out, but don't write any code yet. And there was kind of various versions of this. Sometimes it was just talking through an idea. Sometimes it was these very sophisticated specs that, that they were asking Claude to write, but the common dimension was do a thing without coding yet. And so literally like this was like Sunday night at 10 PM. I was, I was just like looking at GitHub issues and kind of seeing what people were talking about and looking at our internal Slack feedback channel.

`[26:25]` **SPEAKER_02:** And I just wrote this thing in like 30 minutes and then, uh, shipped it that night. It went out Monday morning. That was plan mode.

`[26:31]` **SPEAKER_04:** So do you mean that there'll be no need for plan mode to, in the sense of I'm worried that the model is going to do, like, it's going to do like the wrong thing or head off in the wrong direction, but there will still be a need for that. You need to think through the idea and figure out exactly what it is that you want. And you have to do that somewhere.

`[26:47]` **SPEAKER_02:** I kind of think about it in terms of like kind of increasing model capabilities. So maybe six months ago, a plan was insufficient. So you get Claude to make a plan. Was he even with plan mode, you still have to kind of sit there and babysit because it can go off track nowadays. What I do is probably 80% of my sessions, I say, I say plan mode has a limited lifespan, but I'm a heavy plan mode user. Um, I probably 80% of my sessions, I start in plan mode and Claude will, you know, it'll start, it'll start making a plan.

`[27:13]` **SPEAKER_02:** I'll move on to my second terminal tab and then I'll have it make another plan. And then when I run out of tabs, I open the desktop app and then I go to the code tab and then I just start a bunch of tabs there. And they all start in plan mode, probably, you know, like 80% of the time. Once the plan is good. And sometimes it takes a little back and forth. They just get Claude to execute. And. Nowadays, what I find with Opus 4.5, I think it started with 4.6. It got really good. Once the plan is good, it just stays on track and it'll just do the thing exactly right.

`[27:40]` **SPEAKER_02:** Almost every time. And so, you know, before you had to babysit after the plan and before the plan, now it's just before the plan. So maybe the next thing is you just won't have to babysit. You can just kind of give a prompt and Claude will figure it out.

`[27:51]` **SPEAKER_01:** The next step is Claude just speaks to your users directly.

`[27:56]` **SPEAKER_04:** It just bypasses you entirely. It's funny.

`[27:58]` **SPEAKER_02:** This is actually the current stuff, bro. Our Claude's actually like, they talk to each other. They talk to our users on Slack, at least internally, pretty often. Um, my Claude will like tweet once in a while. No way. Um, but I actually like delete it. It's just like, it's a little like cheesy. Yeah. Like, I don't love the tone. What does it want to tweet about? Sometimes it'll just like respond to someone. Cause I always have like cowork running in the background and it's like, it's the cowork Claude that really loves to do that.

`[28:22]` **SPEAKER_02:** Cause it likes using a browser. That's funny. A really common pattern is I ask Claude to build something. It'll look in the code base. Uh, it'll see some engineer. It'll touch something in the Git flame and then it'll message that engineer on Slack. Um, just like asking a clarifying question. And then once it gets the answer back, it'll keep going.

`[28:37]` **SPEAKER_00:** What are some tips for founders now on how to build for the future? It sounds like everything is really changing. What are like some principles that will stay on and what will change?

`[28:47]` **SPEAKER_02:** So I think some of these are pretty, are pretty basic, but I think they're even more important now than they were before. Um, so one example is latent demand. Like I mentioned it a thousand times for me, it's just like the single biggest idea in product. It's a, it's a thing that no one understands. It's a thing. I certainly did not understand my first few startups and the idea is like people will only do a thing that they already do. You can't get people to do a new thing. If people are trying to do a thing and you make it easier, that's a good idea.

`[29:14]` **SPEAKER_02:** But if, if people are doing a thing and you try to make them do a different thing, they're not going to do that. And so you just have to make the thing that they're trying to do easier. And I think Claude is going to get increasingly good at kind of figuring out these kinds of product ideas for you. Just cause it can look at feedback. It can look at debug logs, like kind of figure this out.

`[29:28]` **SPEAKER_04:** That's what you mean by a plan mode. It was latent demand that people were already like, and it had their Claude chat window open in a browser and we're like talking to it to figure out like the spec and, and what it should do. And now it's the like plan mode just became that you just do it in Claude code.

`[29:44]` **SPEAKER_02:** Yeah. Yeah. That's it. Sometimes what I'll do is I'll just walk around the office on, on our floor and I'll just kind of stand behind people. I I'll say like, hi. So it's not great. And then, um, I'll, I'll just see kind of like how they're using quad code. Um, and this is also just something I saw a lot. Um, but it also came up in.

`[29:59]` **SPEAKER_04:** It seems like you're surprised how far the terminal has gone and how far it's been perished. Like how far do you think it has left to go just given with this world of swore multiple agents, like, do you think there's going to be a new, a need for a different UI on top of it?

`[30:17]` **SPEAKER_02:** It's funny. If you asked me this a year ago, I would have said the terminal has like a three month lifespan and then we're going to move on to the next thing. Um, and you can see us experimenting with this, right? Cause Claude code started in a terminal, but now it's in, you know, it's on web. You can like. It's in the desktop app. You know, we've had that for, you know, like three months or six months or something just in the code tab. Um, it's in the iOS and Android apps, just like in the code tab.

`[30:39]` **SPEAKER_02:** It's in Slack. It's in GitHub. There's VS code extensions. There's jet brains extensions. So we're just like, we're always experimenting with different form factors for this thing to figure out what's the next thing. I've been wrong so far about the lifespan of the CLI. So I'm probably not the person to forecast.

`[30:56]` **SPEAKER_04:** What about like your advice to dev tool founders? Like someone's. Building a dev tool company today. Should they just like be building for engineers and humans, or should they be thinking more about like what Claude is going to think and want and build for sort of like the agent?

`[31:11]` **SPEAKER_02:** The way I would frame it is think about the thing that the model wants to do and figure out how do you make that easier? And that's something that we saw, you know, like when I first started hacking on cloud code, I realized like this thing just wants to use tools. It just wants to interact with the world. And how, how do you, how do you enable that? Well, the way you don't do it is you put it in a box and you're like, here's the API. Here's how you interact with me. And here's how you interact with the world.

`[31:36]` **SPEAKER_02:** The way you do it is you see what tools it wants to use. You see what it's trying to do. And you enable that the same way that you do for your users. And so like for, if you're building a dev tool startup, I would think about like, what is the problem you want to solve for the user? And then when you use, when you apply the model to solving this problem, what is the thing the model wants to do? And then what is the technical and product solution that serves the weight and demand of both?

`[31:56]` **SPEAKER_01:** YC's next batch is now taking applications. It's got a startup in you, apply at YCombinator.com slash apply. It's never too early and filling out the app will level up your idea. Okay. Back to the video.

`[32:10]` **SPEAKER_00:** Back in the day, more than 10 years ago, you were a very heavy, heavy user and you wrote a book about TypeScript, right? Before TypeScript was cool. This is when everyone was a deep in JavaScript. This is back in early 2010s, right?

`[32:25]` **SPEAKER_02:** Yeah. Something like that.

`[32:27]` **SPEAKER_00:** Before TypeScript was a thing because back. Then it's a very weird language. It's not supposed to do a lot of things with being typed in JavaScript and now is the right thing. And it feels like cloud code in the terminal has a lot of parallels with TypeScript at the beginning.

`[32:44]` **SPEAKER_02:** TypeScript makes a lot of really weird language decisions. So if you look at the type system, pretty much anything can be a literal type, for example. And this is like, this is super weird because like, even though like Haskell doesn't even do this, it's just like, it's too extreme. Or it has like conditional types, which I don't think any language thought of at all.

`[33:05]` **SPEAKER_00:** It was like very strongly typed.

`[33:06]` **SPEAKER_02:** Yeah, it was very strongly typed. And the idea was like when, you know, like when Joe Pamer and Anders and the early team was like building this thing, the way they built it is that we OK, we have these teams with these big untyped JavaScript code bases. We have to get types in there, but we're not going to get engineers to change that the way that they code. You're not going to get JavaScript people to have like, you know, 15 layers of class inheritance like you would a Java programmer.

`[33:28]` **SPEAKER_02:** Right. They're going to write code. Right. The way they're going to write it, they're they're going to use a reflection and they're going to use mutation and they're going to use all these features that traditionally are very, very difficult to type.

`[33:36]` **SPEAKER_00:** They're a very unsafe type to any strong functional programmers, really.

`[33:40]` **SPEAKER_02:** That's right. That's right. That's right. And so the thing that they did instead of getting people to kind of change the way that they code, they built a type system around this. And it was just it's brilliant because there's all these ideas that no one was thinking about, even in academia, like no one thought of a bunch of these ideas. It purely came out of the practice of observing people and seeing how JavaScript programmers. Want to write code. And so, you know, for for cloud code, there are some ideas that are kind of similar in that, you know, like you can use it like a Unix utility.

`[34:07]` **SPEAKER_02:** You can pipe into it, you can type out of it in some ways. It is kind of rigorous in this way, but in in almost every other way, it's just the tool that we wanted. Like I build a tool for myself and then the team builds the tool for themselves and then for anthropic employees and then for users. And it just ends up being really useful. It's not it's not this like principled and academic thing.

`[34:27]` **SPEAKER_00:** Which I think the. The proof is actually in the results now, fast forward more than 15 years later, not many code bases are in Haskell, which is more academic, and there's tons of them now in TypeScript because it's way more practical.

`[34:41]` **SPEAKER_02:** Right.

`[34:42]` **SPEAKER_00:** Which is interesting.

`[34:43]` **SPEAKER_02:** Yeah, it is interesting, right? It's like TypeScript solves the problem.

`[34:45]` **SPEAKER_00:** I guess one thing that's cool, I don't know how many people know, but the terminal is actually one of the most beautiful terminal apps out there and is actually written with React terminal.

`[34:57]` **SPEAKER_02:** And when I first started building it, you know, like I did. I've been in front end engineering for for a while, so and I was also like, you know, I'm sort of like a hybrid, like I do like design and user research and, you know, write code and all the stuff. And we love hiring engineers that are like this, so we just we love generalists. So for me, it's like, OK, I'm building a thing for the terminal. I'm actually kind of a shitty Vim user. So like, how do I build a thing for people like me that, you know, are going to be working in a terminal?

`[35:22]` **SPEAKER_02:** And I think just the delight is so important. And I feel like at YC, this is something you talk about a lot, right? It's like build a thing that people love. The product is useful, but you don't fall in love with it. That's not great. So it kind of has to do both. Designing for the terminal, honestly, has been hard, right? It's like it's like 80 by 100 characters or whatever. You have like 256 covers. You have one font size. You don't have like mouse interactions. There's all the stuff you can't do.

`[35:45]` **SPEAKER_02:** And there's all these very hard tradeoffs. So like a little known thing, for example, is you can actually enable mouse interactions in a terminal so you can enable like clicking and stuff. Oh, how do you do that in cloud code? I've been trying to figure out how to do this. We don't we don't have it in cloud code because we actually prototyped it a few times. And it felt really bad because the tradeoff is you have to virtualize scrolling. And so there's all these weird tradeoffs because like the way terminals work is like there's no DOM, right?

`[36:07]` **SPEAKER_02:** It's like there's like anti-escape codes and these kind of weird organically evolved specs since like the 1960s or whatever.

`[36:14]` **SPEAKER_01:** Yeah, it feels like BBSs. It's like a BBS door game. Yeah, yeah, yeah. Oh, my gosh.

`[36:18]` **SPEAKER_02:** That's like that's like a great compliment. Yeah, yeah, yeah. It should feel like you're discovering.

`[36:22]` **SPEAKER_01:** Lord of the Red Dragons. Fantastic. Oh, my God.

`[36:24]` **SPEAKER_02:** Yeah, but we have we've had to just like discover all these kind of UX principles for building the terminal because no one really writes about this stuff. And if you look at the big terminal apps of, you know, like the 80s or 90s or 2000s or whatever, these like add curses and they have all these like windows and things like this. And it just looks kind of like janky by modern standards. It just looks too heavy and complicated. And so we had to like reinvent a lot. And, you know, for example, something like the terminal spinner, like just like the spinner words, it's gone through probably I want to say like 50, maybe 100 iterations at this point.

`[36:55]` **SPEAKER_02:** And probably 80% of those didn't ship. So we tried it. It didn't feel good. Move on to the next one. Try it. Didn't feel good. Move on to the next one. And this was like sort of one of the amazing things about Quad Code, right? Is like you can write these prototypes and you can just do like 20 prototypes back to back, see which one you like and then ship that. And the whole thing takes maybe a couple of hours. Whereas in the past, what you would have had to do is like weren't to use origami or framer or something like this.

`[37:17]` **SPEAKER_02:** You built like maybe three prototypes. It took like two weeks. It just took much, much longer. And so we have this luxury of we have to discover this new thing. We have to build the thing. We don't know what the right endpoint is. But we can. We can iterate there so quickly. And that's what makes it really easy. And that's what lets us build a product that's like joyous and that people like to use.

`[37:36]` **SPEAKER_03:** Boris, you had other advice for builders. And we kept interrupting you because we have so many questions.

`[37:43]` **SPEAKER_02:** I would say, so OK, so maybe two pieces of advice that are kind of weird because it's like about building for the model. So one is don't build for the model of today. Build for the model of six months from now. This is like sort of weird, right? Because like you can't find PMF if the product doesn't work. But actually, this is the thing. This is what you should do because otherwise what will happen is you spend a bunch of work, you find PMF for the product right now, and then you're just going to get leapfrogged by someone else because they're building for the next model and a new model comes out every few months.

`[38:10]` **SPEAKER_02:** Use the model, feel out the boundary of what it can do, and then build for the model that you think will be the model maybe six months from now. I think the second thing is, you know, actually in the quad code area where we sit, we have a framed copy of the Bitter Lesson on the wall. And this is this like Rich Sutton blog post. Everyone should read it if you haven't. And the idea is the more general model will always beat the more specific model. And there's a lot of corollaries to this, but essentially what it boils down to is never bet against the model.

`[38:40]` **SPEAKER_02:** And so this is just like a thing to that we always think about where we could build a feature into quad code, we could make it better as a product, and we call this scaffolding. That's all this code that's not the model itself. But we could also just wait like a couple months and the model can probably just do the thing instead. And there's always the straight off, right? It's like engineering work now. And you can kind of extend the capability a little bit, maybe 10, 20% or whatever in whatever domain on this, like, you know, like the spider chart of what you're trying to extend.

`[39:07]` **SPEAKER_02:** Or you can just wait and the next model will do it. So just always think in terms of this trade off. Where do you actually want to invest and assume that whatever the scaffolding is, it's just tech debt?

`[39:16]` **SPEAKER_00:** How often do you rewrite the code base of a clock code? Is this every six months with this first physical?

`[39:23]` **SPEAKER_03:** Is there scaffolding that you've deleted because you don't need it anymore because the model just improved?

`[39:26]` **SPEAKER_02:** Oh, so much. Yeah. Like all of quad code. Code has just been written and rewritten and rewritten and rewritten over and over and over. We unshipped tools every couple of weeks. We add new tools every couple of weeks. There is no product quad code that was around six months ago. It's just constantly rewritten.

`[39:41]` **SPEAKER_00:** Would you say that most of the code base for our current clock code is only, say, 80% of it is only less than a couple of months old?

`[39:48]` **SPEAKER_02:** Yeah, definitely. It might even be like less than, yeah, maybe like a couple of months. That feels about right.

`[39:53]` **SPEAKER_00:** So it's like the lifecycle of code now. That's another alpha is expecting it to be the shelf life to be just a couple of months.

`[39:58]` **SPEAKER_01:** Yeah.

`[39:59]` **SPEAKER_00:** For the best founders.

`[40:00]` **SPEAKER_01:** Do you see Steve Yegi's post about how awesome working at Anthropic is? And I think there's a line in there that says that an Anthropic engineer currently averages 1,000x more productivity than a Google engineer at Google's peak, which is really an insane number, honestly, like 1,000x. Three years ago, we were still talking about 10x engineers. Now we're talking about 1,000x on top of a Google engineer in the prime?

`[40:28]` **SPEAKER_02:** Like, this is unbelievable, honestly. Yeah, I mean, internally, if you look at like technical employees, they all use quad code every day. And even non-technical employees, I think like half the sales team uses quad code. They've started switching to co-work because it's a little easier to use. It has like a VM, so it's a little bit safer. But yeah, we actually we just pulled the stat and I think the team doubled in size last year, but productivity per engineer grew something like 70%.

`[40:53]` **SPEAKER_02:** As measured by? Just like the simplest, stupidest measure, pull requests. But we also kind of cross-checked that. I mean, we did a lot against like commits and like the lifetime of commits and things like this. And since quad code came out, productivity per engineer at Anthropic has grown 150%. Oh, my God. And this is crazy because in my old life, I was responsible for code quality at Meta, and I was responsible for the quality of all of our code bases across every product, across like, you know, Facebook, Instagram, WhatsApp, whatever.

`[41:20]` **SPEAKER_02:** And one of the things that the team worked on was improving productivity. And back then, seeing a gain of something like 2% in productivity. I mean, it was a year of work by hundreds of people. And so this like 100%, this is just like unheard of, just completely unheard of.

`[41:35]` **SPEAKER_01:** What drove you to come over to Anthropic? I mean, basically, as a builder, you could go anywhere. What was the moment that made you say, like, actually, this is the set of people or this is the approach?

`[41:45]` **SPEAKER_02:** I was living in rural Japan and I was opening up Hacker News every morning and I was reading the news and it was all it just started to be like AI stuff at some point. And I started to use some of these early products. And I remember like the first couple of times that I used it, I was just like, it just took my breath away. That was like very cheesy to say, but that was actually the feeling. Like, it was just like, it was amazing. Like, as a builder, I've just never kind of felt this feeling like using these very, very early products.

`[42:14]` **SPEAKER_02:** That was like in the quad two days or something like that. And so I just started talking to friends at Labs just to kind of see what was going on. And I met Ben Mann, who's one of the founders at Anthropic. And he just immediately won me over. And as soon as I met kind of the rest of the team at Anth, they just won me over. And I think probably in two ways. So one is it operates as a research lab. So the product was teeny, teeny, tiny. It's really all about building a safe model. That's all that matters.

`[42:44]` **SPEAKER_02:** And so this idea of just being very close to the model and being very close to development and being not the most important thing because the product isn't anymore. It's just the model is the thing that's the most important. That really resonated with me. And I've been building product for many years. And then the second thing was just how mission driven it is. Like I'm a huge sci-fi reader. My bookshelf is just like filled with sci-fi. And so like I just know how bad this can go. And when I kind of think about what's going to happen this year, you know, it's going to be totally insane.

`[43:15]` **SPEAKER_02:** And in the worst case, it can go very, very bad. And so I just wanted to be at a place that really understood that and kind of really internalized that. And at Anth, you know, like if you overhear conversations in the lunchroom or in the hallway, people are talking about AI safety. This is really the thing that everyone cares about more than anything. And so I just wanted to be in a place like that. I know for me personally, the mission is just so important. What is going to happen this year?

`[43:39]` **SPEAKER_02:** Okay. So if you think back like six months ago and kind of what are the predictions that people are making? So Dario predicted that 90% of the code at Anthropic would be written by Quad. This is true. For me personally, it's been 100% for like since Opus 4.5. I uninstalled it. Okay. I uninstalled my IDE. I don't edit a single line of code by hand. It's just 100% Quad code and Opus. And, you know, I land, you know, like 20 PRs a day every day. If you look at Anthropic overall, it ranges between like 70% to 90%, you know, depending on the team.

`[44:11]` **SPEAKER_02:** For a lot of teams, it's also like 100%. For a lot of people, it's 100%. And I remember making this prediction back in May when we GA'd Quad code that you wouldn't need an IDE to code anymore. And it was totally crazy to say. I feel like people in the audience gasped. Because it was such like a silly prediction at the time. But really all it is is like you just like trace the, you know, the exponential. And this is just like so deep in, you know, the DNA at Ant. Because like, you know, three of our founders were coauthors of the scaling laws paper.

`[44:39]` **SPEAKER_02:** They saw this very early. And so this is just like tracing the exponential. This is what's going to happen. And yes, that happened. So continuing to trace the exponential, I think what will happen is coding will be generally solved for everyone. And I think today coding is practically solved, you know, for me. And I think it'll be the case for everyone. You know, regardless of domain. I think we're going to start to see the title software engineer go away. And I think it's just going to be maybe builder, maybe product manager.

`[45:04]` **SPEAKER_02:** Maybe we'll keep the title as kind of a vestigial thing. But the work that people do, it's not just going to be coding. It's software engineers are also going to be writing specs. They're going to be talking to users. Like this thing that we're starting to see right now on our team where engineers are very much generalists. And every single function on our team codes, like our PM's code, our designer's code, our EM codes, our finance guy codes, like everyone on our team codes. We're going to start to see this everywhere.

`[45:31]` **SPEAKER_02:** So this is sort of this is kind of like the lower bound if we just continue the trend. The upper bound, I think, is a lot scarier. And this is something like, you know, we hit ASL 4. And, you know, at Anthropic, we talked about the safety levels. ASL 3 is where the models are right now. ASL 4 is the model is recursively self-improving. And so if this happens, essentially, we have to meet a bunch of criteria before we can release a model. And so the extreme is that, you know, this happens.

`[45:56]` **SPEAKER_02:** Or there's some kind of catastrophic misuse. Like people are using the model to design bioviruses, design zero days, stuff like this. And this is something that we're really, really actively working on. So that doesn't happen. I think it's just been, honestly, it's just been like so exciting and humbling. Like seeing how people are using quad code. Like, you know, I just wanted to build a cool thing. And it ended up being really useful. And that was so surprising and so exciting.

`[46:20]` **SPEAKER_04:** My impression from Twitter or just the outside is basically, everyone went away over the holidays and then like found out about quad code. And it's just been crazy ever since. But is that how it was for you at like internet? Did you, were you having like a nice Christmas break and then came back? You're like, what happened?

`[46:36]` **SPEAKER_02:** Well, actually, for all of December, I was traveling around. And I took a coding vacation. So we were kind of traveling around and I was just like coding every day. So that was really nice. And then I also started to use Twitter at the time. Because like I worked on threads back then, way back when. So I've been a threads user for a while. So I just like tried to see kind of like, oh. Other platforms where people are. Yeah, I think for a lot of people, they kind of discover, that was the moment where they discovered Opus 4.5.

`[46:59]` **SPEAKER_02:** I kind of already knew. And internally, quad code's just been on this like exponential tear for many, many months now. So that just like, it became even more steep. That's what we saw. And if you look at quad code now, you know, there was some stuff from Mercury that like 70% of startups are, you know, choosing quad as their model of choice. There were some other stuff from like semi-analysis that 4% of all public commits are made by quad code. From like of all code written everywhere.

`[47:25]` **SPEAKER_02:** I saw that. All the companies, you know, use quad code from like the biggest companies to kind of, you know, smallest startups. You know, like it wrote, it plotted the course for perseverance. Like for like the Mars Rover. This is just like, this is the coolest thing for me. And we like, we even printed posters. Because the team was like, wow, this is just like so cool. The NASA chooses to use this thing. So yeah, it's just like, it's humbling. But it also feels like the very beginning.

`[47:47]` **SPEAKER_01:** What's the sort of interaction between quad code and then co-work? Like, you know, was it a fork of? Was it like you had quad code look at the quad code code and say, let's make a new spec for non-technical people that, you know, keeps all the lessons. And then, you know, it sort of went off for a couple of days and did that. What's the genesis of that? And, you know, where do you think that goes?

`[48:10]` **SPEAKER_02:** This is going to be like my fifth time using the word weight and demand. Yeah. It was just that, I mean, like we were looking at Twitter and there was like that one guy that was using quad code to like monitor his tomato plants. There was like this other person that was using it to like recover wedding photos off of a corrupted hard drive. There were people that using it for like for finance. When we looked internally at Anthropic, every designer is using it. The entire finance team at this point is using it.

`[48:34]` **SPEAKER_02:** The entire data science team is using it not for coding. People are jumping over hoops to install a thing in the terminal so that they can use this. So we knew for a while that we wanted to build something. And so we're experimenting with a bunch of different ideas. And the thing that kind of took off was just, you know, a little quad code wrapper in a GUI in the desktop app. That's all it is. It's just quad code. There's no code under the hood. It's the same agent. Oh, wow. And Felix and the team,

`[48:57]` **SPEAKER_02:** and Felix was an early Electron contributor. He kind of knows that stack really well and he was hacking on various ideas. And they built it in I think something like 10 days. It was just like 100% written by quad code. And it just felt ready to release. There was a lot of stuff that we had to build for non-technical users. So it's a little bit different than a technical audience. It runs in a, all the code runs in a virtual machine. There's a lot of protections for deletion and things like this.

`[49:25]` **SPEAKER_02:** There's a lot of permission prompting and kind of other guardrails for users.

`[49:30]` **SPEAKER_01:** But yeah, it was honestly pretty obvious. Boris, thank you so much for making something that is taking away all my sleep. But in return, it's making me feel creator mode again, sort of founder mode again. It's been an exhilarating three weeks. I can't believe I waited that long since November to actually get into it. Thank you so much for being with us. And building what you're building.

`[49:52]` **SPEAKER_02:** Yeah. Thanks for having me. And send bugs.

`[49:55]` **SPEAKER_01:** Sounds good.
