# 全文转录 · 24 岁做出 Cursor:在 GitHub Copilot 阴影下,靠"信念一致性"押注编程的未来

> ▶ [YouTube](https://www.youtube.com/watch?v=TrXi3naD6Og) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/TrXi3naD6Og.md) &nbsp;·&nbsp; Michael Truell: Building Cursor At 23, Taking On GitHub Copilot & Advice To Engineering Students
>
> 🗣️ 说话人分离识别到 **3** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_02:** We realized we were really inherently excited about the future of coding and I think we took a step back and realized that if we were being really consistent with our beliefs there was going to be an opportunity for all of coding to change in the next five years and for all of software development to flow through models. It felt like no one working on the space at the time was really taking that seriously. It felt like they had great products and they were making them a bit better but they weren't really aiming for a world where you know all of coding as we

`[00:24]` **SPEAKER_02:** know it today gets automated and building software ends up looking very very different. Then with that in mind we set out to to work on that. Let's start this talk with sort of the

`[00:38]` **SPEAKER_00:** origin story of your journey as a founder. You kind of have to go way back to middle school when you were reading the essays from PJ right? So early on I think you know I had been interested

`[00:52]` **SPEAKER_02:** in starting a company for a long time. I'd been interested in a bunch of a bunch of other things too. I think actually I originally got into programming being interested in in starting something. It was kind of commercial where the first time that I ever saw code it was over some winter break and my brother and I we wanted to create a hit mobile game. We didn't really know how to do that. We looked on Google. How do you create a game? We heard that you need to download this application called Xcode. We did that and we were hit with these weird colorful esoteric symbols

`[01:23]` **SPEAKER_02:** which were Objective-C which you know is still around but maybe a little bit less popular than it was then for good reasons and stared at this kind of impenetrable wall of Objective-C and my brother promptly ejected. Didn't move on with programming. He now is on a very different career path. He's kind of trying to paint or something like that but I yeah kept going and bought a book on Objective-C and then eventually started working on on mobile games. That was the genesis of me getting into programming

`[01:54]` **SPEAKER_02:** and then along the way also yes was a big fan of PJ's essays and Sam's essays too also and a bunch of books and stuff. I was also inspired by his essay books. I was a huge fan of his essays and Sam's essays too also and a bunch of books. a bunch of the folks in YC, and that was definitely a big inspiration, even from the very early stages of high school.

`[02:09]` **SPEAKER_00:** I think the wildest thing about Cursor is that right now you're just 24 and build this monster of a company in a really short amount of time. To a lot of people it could seem that it's a bit of out of nowhere, but this was really in the making for more than a decade. You've been working and shipping a lot of different projects, right? And you were working in AI even when you were in high school, right? Tell us a bit about the projects and how you got started with that.

`[02:36]` **SPEAKER_02:** Was lucky enough to find programming early on. Was also lucky enough to be interested in AI early on and have some great collaborators to work on AI projects with. Soon after kind of the foray into mobile games, which also turned into, I wasn't very good at mobile games, so one of the things that I built, and actually one of the things that got most popular, which was kind of the technically easiest thing to build, which was maybe a lesson in startups of the code isn't everything, was this mobile game or this mobile app

`[03:03]` **SPEAKER_02:** where you could spoof high scores in things like piano tiles and Flappy Bird and then send them to your friends. And that was kind of the thing that went viral. It wasn't the painstakingly handcrafting the game engine yourself type thing. But yeah, no, soon after that, got interested with a friend in the idea of building a robotic dog, where we thought it would be really great to have a robot that you could teach to do things without programming it. Instead, you could give it positive and negative feedback,

`[03:29]` **SPEAKER_02:** like you give a dog, so you could give it a treat if it does some, quote, treat if it does something good. You could say bad if it does something bad. And then maybe you could teach it to play fashion, things like that. That idea really animated us. We had no idea how to build it. And so again, started the place where one would start, which is Google, and kind of went down a lot of rabbit holes and took us into a place of learning about genetic algorithms, and maybe that was gonna be helpful

`[03:53]` **SPEAKER_02:** for building this robot dog that we wanted to build. And then we eventually learned about this neural network stuff, because some people were playing with taking genetic algorithms and using them to evolve neural networks at the time with work like NEET. And then eventually it took us to RL, reinforcement learning, which was, even back in 2015, people had been working on it for a long time. In the end, my friend and I, we did eventually build a couple of robots. We didn't do any sort of substantial work

`[04:20]` **SPEAKER_02:** that really lasted, but we did work that was interesting at the time in taking reinforcement learning algorithms and making them more data efficient, making them better at learning from very, very few data points, order of tens of data points, and also from noisy data, data that a human's giving. It wasn't exactly a dog, but we built a couple of robots where one of them was this many-axis robot arm that could kind of swing a paddle and play ping pong, and if you put the right sensor on it and then you gave it the right

`[04:46]` **SPEAKER_02:** sort of positive and negative feedback, you could teach it to swing when it sees a ball. And then we had this KiwiDrive robot that we would teach to follow a line. To do that, it was actually kind of this great education in ML, partially because of our dumb naivete, where we didn't really know that there were things like Torch and TensorFlow and kind of other, you know, lots of building blocks we could use from. Maybe we weren't good enough at Googling.

`[05:09]` **SPEAKER_00:** So you implemented your own neural network from scratch?

`[05:12]` **SPEAKER_02:** Yeah, so-

`[05:13]` **SPEAKER_00:** When you were like, I don't know, 16, 17?

`[05:16]` **SPEAKER_02:** The constraints of the problem were we were dealing with robots, and so we were dealing with microcontrollers. And so microcontrollers have very little memory, and they couldn't really fit any of the normal standard ML libraries. So as part of our bike-shedding, trying to build a robot dog, we implemented our own tiny neural network library. And I have memories of us not really understanding any of the internals of how these things worked, or not really understanding calculus, but kind of fumbling our way through

`[05:44]` **SPEAKER_02:** reimplementing some important ideas from neural networks. You know, I think it taught us a lot. I think that there were a lot of gaps in the fundamentals that it took many years to fill in later.

`[05:53]` **SPEAKER_00:** Then fast forward to the founding of AnySphere. It's an interesting name. Because Cursor is not what it is. When you guys started, you had just graduated MIT, right? That was back in 2022. What were the first idea that all four of you started working on back in 2022?

`[06:14]` **SPEAKER_02:** Yeah, so the genesis of Cursor was in 2021. My co-founders and I, we had been interested in AI for a long time. Each of us kind of had our own little robot dog moment where one of my co-founders, he worked on trying to build a competitor to Google, actually, using LLMs in 2021 and training his own, and training his own contrastive models. One of my co-founders worked on computer vision in academia. And some of us also worked on recommendation systems at companies like Google. But we were really interested in AI.

`[06:46]` **SPEAKER_02:** In 2021, we were trying to figure out what we'd do with that interest. Do we go and work on AI in academia? Or do we go join a big existing AI effort? Or do we start our own thing? There were two moments that really got us excited. One was seeing the first AI product start to come out. GitHub Copilot was really the canonical example for us. The other was seeing work about how it looked like AI was going to predictably get better in the future as you scaled up these models. At the very beginning of 2022,

`[07:14]` **SPEAKER_02:** me and my co-founders, we went on like a month-long hackathon, basically. And we started hacking on ideas related to kind of picking an area of knowledge work and building what it looks like as AI gets more and more mature.

`[07:27]` **SPEAKER_00:** You guys have collected a lot of data for that. That's your first idea, right?

`[07:30]` **SPEAKER_02:** Yeah. So the first real idea that we worked on for a long time was in mechanical engineering. It was trying to build a copilot for mechanical engineers and trying to train models to kind of predict what you would do in a CAD system like SOLIDWORKS or Fusion 360, which is where mechies model out parts in 3D on a computer. We picked it because we thought it would be boring and sleepy and uncompetitive. And we were kind of doing an armchair MBA thing, even though it was a horrible choice from the get-go

`[07:56]` **SPEAKER_02:** because none of us were really mechanical engineers, so science wasn't really ready for that area.

`[08:00]` **SPEAKER_00:** But you guys kept working at it for a number of months, right? And you crawled and got all these CAD files and actually got something working with auto-completion, right? That was like the first version of it working?

`[08:12]` **SPEAKER_02:** Yes. A bunch of the work was in data scraping, honestly. It was trying to get all the CAD models on the internet. There are also all these different file formats and trying to convert them all into something that's canonical because CAD is this weird software market where there are all these different systems that are pretty popular and it's very fragmented. There are also Cloud CAD systems that don't have easily exportable files, and they don't want you to scrape their stuff. And so there was a bunch of work there.

`[08:36]` **SPEAKER_02:** Also, the training infrastructure for doing any kind of modeling work back then was pretty rudimentary. And so there was a lot of work on the infra side there and just a lot of experimenting with models and a lot of experimenting with how you even jerry-rig an extension into these CAD systems because we were building an extension. These applications aren't really extensible at all. There were actually also other projects that we were working on at the time. So two of my co-founders, they were

`[08:58]` **SPEAKER_02:** working on an extension. It was an end-to-end encrypted messaging system because one of them has a background in security research. And the idea there was apps like Signal and WhatsApp, they encrypt the body of the messages, but they don't hide who's talking to who at what time, which is actually really crucial information if you don't want to trust the messaging app provider. So if a journalist is talking to some informant in the government, just knowing that they're communicating at all is actually a really big piece of information.

`[09:27]` **SPEAKER_00:** So that was in the middle of 2022. So you guys were working for about a good six months on this idea?

`[09:34]` **SPEAKER_02:** Yes.

`[09:34]` **SPEAKER_00:** And how many users did you get at that point? So you shipped the product.

`[09:39]` **SPEAKER_02:** All of these projects were ill-fated, and it had basically no users.

`[09:43]` **SPEAKER_00:** At what point did you realize that the idea was not working? It's like, oh, no, we're all working on this. We're trying to do a startup. It's not working. And what was that moment like?

`[09:55]` **SPEAKER_02:** I think it was a bit different for each of the projects. I think for the messaging app, it was a bit different. Yeah. Yeah. The messaging system that two of my co-founders worked on, it was really technically impressive, but it had these bad trade-offs where it wasn't very scalable. And I think they tried to give it to people, and it didn't really work. And then they tried to sell it B2B, and then it didn't really work. And I think it was after a couple of months of trying to get traction.

`[10:14]` **SPEAKER_02:** For the CAD ideas, it was, yeah, many months of trying to get the models to really be useful for end users. And then also reckoning around, are we really interested in these areas, or is there something else that we're inherently much more excited about?

`[10:29]` **SPEAKER_00:** So there was a moment that you decided, OK, these ideas are not working. We have to pivot again.

`[10:33]` **SPEAKER_02:** Yes.

`[10:34]` **SPEAKER_00:** You churned through three ideas, three, four, five ideas before landing into code completion?

`[10:42]` **SPEAKER_02:** Yeah, I think that we had been inspired by tools like Copilot really, really on. And we had avoided working on AI and coding because we thought it was too competitive. Which is crazy. It was competitive then, still is competitive now.

`[10:57]` **SPEAKER_00:** Because back in 2022. GitHub Copilot was making already about $100 million in revenue?

`[11:02]` **SPEAKER_02:** I think potentially more, yeah.

`[11:04]` **SPEAKER_00:** And you guys were like, oh, we could still do a better job than GitHub Copilot? Because people thought the game was done.

`[11:08]` **SPEAKER_02:** It's like, hey, GitHub did it. Well, I mean, we didn't think we could at the start. And then I think it was the desperation of having worked on ideas for a while and not really being excited about them after a while and them not really working out. And that kind of shapes, I think, what you care about and what you're aiming for. And we realized we were really inherently excited about the future of coding. I think also. We got to see how some of the other people in the space were working on their products.

`[11:33]` **SPEAKER_02:** We got to see how the tech was developing. And I think we took a step back and realized that if we were being really consistent with our beliefs, there was going to be an opportunity for all of coding to change in the next five years and for all of software development to flow through models. And it felt like no one working on the space at the time was really taking that seriously. It felt like they had great products, and they were making them a bit better. But they weren't really aiming for a world

`[11:57]` **SPEAKER_02:** where all of coding as we know it today gets automated. And building software ends up looking very, very different. Then with that in mind, we set out to work on that.

`[12:06]` **SPEAKER_00:** That was a bold move, because you said, OK, we're going to stop working on all these other ideas that we didn't have as much of a background. And you were excited about programming, even though you had this big Goliath in the room with GitHub Copilot. You decided to go, and let's just solve this problem.

`[12:22]` **SPEAKER_02:** It didn't really feel bold or like a move at the time, because it's like a bunch of people sitting around in their living room on laptops. It's not like pivoting some giant company. But yeah, no, we did. And initially, we kind of waded into it where we were thinking, well, maybe we do this very niche tool for basically security reviews, trying to detect future CVEs in your code. Or maybe we build something that's just for this one niche area of software. We thought about building for quants

`[12:49]` **SPEAKER_02:** and actually prototypes and things just for quantitative researchers. But yeah, in doing that, we were just brimming with ideas for what Cursor could be if it were just about trying to be the best way to code with AI in general. And then I think that we had a ton of conviction about that, and we had a ton of excitement about that. And so at some point, we just decided to go for it.

`[13:09]` **SPEAKER_00:** And that was end of 2022, right, when you decided to make that move? And how quickly did you ship the first product? And what did the first product look like? And that was around, you shipped it a couple of weeks later. And what was that look like?

`[13:21]` **SPEAKER_02:** It did take us a little bit of time to ship something publicly. It took us roughly, I think, three months from first. It took us a little bit of time to ship the first line of code to open it up and GA it. Originally, what we did is we built our own editor, quote unquote, from scratch. Oh, my god. It was still using a bunch of open source building blocks. There are a lot of great primitives like CodeMirror and the language servers, and there's a lot of open source tech that can help you build an editor.

`[13:47]` **SPEAKER_02:** But yeah, no, it was cobbled together from scratch, and there was our own version of remote SSH, our own Copilot integration at the time, because we didn't have anything like autocomplete. You have to build your own PIN system. You have to build all your own language server integrations. It ends up going into something as developed as the code editor market, making something that can actually be competitive there and serve as someone's daily driver. But I think it was four weeks until we built something

`[14:10]` **SPEAKER_02:** that we could use as our daily driver. It was maybe four weeks later where we gave it to the first beta testers. And then there was another four weeks, and then we GA'd it. And it was still very, very crude at the time. It didn't feel like a big thing to just open it up to the public.

`[14:22]` **SPEAKER_00:** What did you learn in that first version? Because you built a code editor from scratch. You guys haven't done the whole forking yet.

`[14:29]` **SPEAKER_?:** Yeah.

`[14:29]` **SPEAKER_02:** Yeah. We had the fear of God in us. I mean, people hadn't really liked some of the things we had built for a while. So I think that we were kind of all in on it and very focused. But what did we learn from that? I think that we learned the first initial set of AI features, where when we started, I think that there was just one key command. And it pulled up this universal remote in the editor. And then you asked it to do something. And then entirely, the AI would just figure out, oh, what

`[14:56]` **SPEAKER_02:** exactly do you want it to do? Do you want something back? That's like a chat response? Or do you want a code suggestion that you can then take? Or do you want it to go search around your code base and answer a question? Or do you want it to go spin for a really long time or a short time? And there wasn't a lot of control. And I think that we learned, given the tech of the time at the end of 2022, that the form factor has to look a bit different. And so we learned the first early AI features that then

`[15:21]` **SPEAKER_02:** became part of the core of Cursor from iterating both for ourselves and also giving it to people. I think another thing we learned was we were very rapidly building a feature-complete version of what we want in a normal code editor, plus then some AI stuff that we thought was great. But then a feature-complete code editor for the world is going to be a way, way, way longer road. We thought that Fiescode had been developed over the course of 12 years, was one of the earliest TypeScript projects, had lots of people on it.

`[15:48]` **SPEAKER_02:** We thought, oh, yeah, of course, you can kind of spin something up that's just equivalent for the world in a few months. And I think that we learned very rapidly that that wasn't the reality, and our time was going to be best spent just focused on the AI stuff. And so similar to how browsers often base themselves off of Chromium's rendering engine, we then switched to being based off of VS Code.

`[16:06]` **SPEAKER_00:** The other thing is you guys had also implemented your own models too. Back then, you got a lot of inspiration from Codex, right?

`[16:15]` **SPEAKER_02:** Yes. So when we were setting out to work on our first idea that we really spent a bunch of time on, which was trying to help mechanical engineers be more productive using AI, one of the things when we raised our first round of funding, because we actually kind of needed money from the get-go to do a little bit of model training, because you couldn't bootstrap it with the models that existed off the shelf. They weren't good enough at that task. One of the papers that we would tout around is actually the original Codex paper,

`[16:39]` **SPEAKER_02:** because by our calculations, Codex, which was the first, this was the first autocomplete model behind GitHub Copilot, it didn't really cost that much money to train, even though even back then, at kind of the beginning and middle of 2022, people were talking about how expensive AI models were to train. I think it cost, my math might be wrong, but I think it was about $100K in training costs. And then, you know, during this foray into mechanical engineering, we had done our own training.

`[17:03]` **SPEAKER_02:** And then when we set off on Cursor, I think we were a little bit burned by that. And so we wanted to be as pragmatic as possible, not reinvent the wheel. And so we started by doing none of that. And then over the course of 2023, you know, in dialing in the product, that ended up being a really important product lever, especially as we got to scale and we got a bunch of people using the product. And then that also gives you the ability to use product data to make the product better. And so that actually has been a really important muscle

`[17:27]` **SPEAKER_02:** to build in the company.

`[17:28]` **SPEAKER_01:** YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early, and filling out the app will level up your idea. Okay, back to the video.

`[17:42]` **SPEAKER_00:** What happened then in 2023 was when you were still not sure about whether Cursor was going to be a thing, right? You were still debating with your co-founders whether you should still pivot. It's like, oh, is this idea still going to work? And you're still trying to grow it, right? Because it took a long time. It took a long time to get to revenue, right?

`[18:01]` **SPEAKER_02:** Yeah, I think that over 2023, it was growing. The numbers were kind of small. And I think that also we were working on something where there wasn't always a clear next step. I think that there are probably some markets where you're really well served by going and immediately talking to a bunch of people, listing down their problems really rigorously, or really kind of systematically and exhaustively thinking through each problem, what would kind of be the direct solution, and then prioritizing them and then going from there.

`[18:28]` **SPEAKER_02:** But I think that we were and are in a space that's a bit different than that. You know, we're this end user application that doesn't have much of a complexity budget. We are trying to build the best way to code with AI. And so a lot of that is figuring out, you know, given the tools that you have today, what can you actually do? There's a lot of things that you could write down that would be useful if you could build them, but then, you know, figuring out how to build them and all the details,

`[18:55]` **SPEAKER_02:** it's not entirely clear how to move forward on that. And so, yeah, there were a lot of times over the course of 2023. And then, you know, actually also to add to this, of our early user base, if you just kind of followed the gradient of exactly what they wanted, you would get pulled in slightly different directions than we ended up in. You know, we had a really loud segment of users that didn't know how to code at all. And we talked about, you know, should we focus on those folks? We had a really loud segment of users

`[19:19]` **SPEAKER_02:** that wanted us to do things that were very tech stack specific, you know, just building for one technology and making it much less of a horizontal tool. And we resisted doing that too. So there was a lot of early prototyping and kind of wandering the desert in 2023, and then, you know, figuring out things around, you know, where does it make sense to not just build the software, but also build our own models to improve the API models or to replace them in places, like, you know, for instance, with our tab,

`[19:46]` **SPEAKER_02:** you know, our next edit prediction, and then how exactly to do that.

`[19:49]` **SPEAKER_00:** You went from zero to 1 million around 2023, right? And it took a lot to get there, right?

`[19:56]` **SPEAKER_02:** Yeah, it was a bit more than that, but sort of roughly that.

`[19:59]` **SPEAKER_00:** Yeah. And then 2024 was a crazy year. You guys went from one to 100 million in one year. Tell us about this loss of compounding power, because you kept that growing 10% week over week. How did that happen?

`[20:14]` **SPEAKER_02:** So the numbers felt small early on, then the compounding kind of kept going. I think that there were a couple of things that really drove our growth. We're in this market where if you make the product better, you kind of see it in the numbers immediately, where, you know, things start to grow more, and so we felt it around, you know, when we first started to make Cursor Codebase aware, when we first started to, you know, be able to predict your next action, when we made that then more accurate,

`[20:39]` **SPEAKER_02:** then when we made that faster, then when we made that more ambitious, you know, it could predict sequences of changes, and then when we let the AI model start to take more action within your codebase, and then do that really fast, you know, speeding that up. And so all along the way, you know, we kind of just focused on making the product better. The compounding continued. And I don't think that this is true of all markets, but I think we're in a market where end user preferences matter a lot.

`[21:05]` **SPEAKER_02:** And if you make the best thing, people hear about it and talk about it. And that kept going for a long time.

`[21:11]` **SPEAKER_00:** I think one of the funny things that a lot of that's happened around that time, we did see a big shift in the YC companies as they were going through the batch. Because we would ask, what kind of tech stack do you use to build your applications? And it was night and day from one batch to the other. I remember in 2023, I think it was maybe single-digit percentage of the batch we used Cursor. Then 2024, it was like 80%. It's just like spread, like wildfires, like the best builders were using you.

`[21:40]` **SPEAKER_02:** CHRISTIAAN BRINKHOFF- We got onto their Twitter feed, yeah.

`[21:42]` **SPEAKER_00:** AMANDA SCHADE- It was a Twitter feed. Is that where a lot of adoption, how did all the growth came from?

`[21:48]` **SPEAKER_02:** CHRISTIAAN BRINKHOFF- So the very early stages, when we were first launching the editor, we tried to kind of evangelize it on social networks. And actually, one of my co-founders when kind of the dopamine hit keeping him going in 2022 when we were working on some of these ill-fated ideas, he started posting on the internet and kind of explicitly set out to gain a lot of followers, not by doing kind of normal social media things, but by talking about AI, actually. It was kind of surprising the degree to which someone could

`[22:21]` **SPEAKER_02:** actually just read kind of all the papers, think kind of deeply about what was going on at the time, talk about that publicly, and then get recognized by influential people in the space. And so there was like this particular open source model, Flan T5 at the time, that multiple AI efforts that ended up using that model, they found out about kind of the benefits of that model directly from my co-founder, just because he was posting on Twitter and doing that kind of consistently. But he became like sort of niche, very niche,

`[22:52]` **SPEAKER_02:** like sort of niche, niche, niche of SF, micro-celebrity. He would actually kind of evangelize the product early on. And so we had this kind of very movie magic, demo when we first launched and when we first did a wait list to just get our initial batch of users. I think that that was helpful, getting us kick-started. But then after that, we kind of stepped away from that. And we kind of lived like monks in 2023 and just focused on the product. And it really just spread from word of mouth.

`[23:17]` **SPEAKER_02:** I remember there were a couple of times during that year where there were members of the team that would say things like, guys, the product's already good enough. Like, let's put it aside. Let's just focus on growth engineering. And then the next day, we were like, oh, we're going to do this. We're going to do this. We're going to do this. We're going to do this. We're going to do this. And then there would be like a two-month sprint on doing some version of that. And it just never kind of washed away

`[23:36]` **SPEAKER_02:** compared to the other stuff that we worked on that year.

`[23:38]` **SPEAKER_00:** And by that time in 2024, how big was Kirchner? How big was the company at that point?

`[23:45]` **SPEAKER_02:** It was pretty small in 2023, where my co-founders are fantastic engineers, and there were four of us. And so we could go pretty far without hiring anyone. We also had our own set of missteps in figuring out, like, what are we going to do about the first set of people to hire and how exactly to do that? And so we were both very patient early on and also focused on hiring a lot less than we probably should have early on. I think we ended 2023 at only single digits, people. Like, we were less than 10 still.

`[24:20]` **SPEAKER_02:** Yeah.

`[24:21]` **SPEAKER_00:** Amazing. Now, I guess I'm curious, now shifting gears a little bit about what are your thoughts in terms of how the future is going to look with that?

`[24:29]` **SPEAKER_02:** What are your thoughts on coding? We were kind of this maybe middle road bet from the start, where when we set out to work on the company and we were hiring our first people, we would get these weird looks around, why are you? I mean, at the end of 2022, it wasn't really like this, right? Because kind of chat GPT happened, and then the whole world woke up to things in the beginning of 2023. But especially during 2022, when we were working on the CAD stuff and then the early code stuff, people thought working on AI, it was kind of weird to do.

`[24:58]` **SPEAKER_02:** I was not entirely convinced that it was a good use of time and that there were going to be lots of great applications to fall out of AI. And then even the people who are interested in AI, there was, in our space, a bunch of people that were just focused on optimizing kind of the form factor that exists already and just making those products a little bit better. And then at the same time, in our social circles and professional circles, there's a bunch of people that were thinking, oh, why would you work on anything other than AGI?

`[25:26]` **SPEAKER_02:** And all of the work that you're doing right now, in one or two years, circa 2022, is going to go away. And yeah, I think that we've always had this view that there's going to be lots and lots of incredibly valuable things to build over the next couple of decades. AI is going to be this transformative technology, maybe more so than any technological revolution in recent centuries. But it's going to take a couple of decades, and it's going to be this industry-wide effort where there are all of these independent capabilities that

`[25:57]` **SPEAKER_02:** each need to fall out to really get to a place where you can entirely get to the end state of transforming building software on computers or kind of the other areas of knowledge work that might be transformed by AI. And yeah, I think concretely kind of in the near term, we think that for professional engineers, which is the end user we serve, the market that we serve, code is still really important. And there will be this long, messy middle where you will be working with the AI. More and more, it will become like a colleague.

`[26:25]` **SPEAKER_02:** More and more, it may also become like a very advanced compiler. That can start to hide some of the code for you. You're going to have to read the logic and review it and edit it.

`[26:37]` **SPEAKER_00:** So what do you think are the skills that are still going to matter? What should everyone still be studying or stop studying?

`[26:42]` **SPEAKER_02:** I mean, I think that programming like math is kind of just a good general education. I don't think that that goes away. And I think that there's also lots of practical skills that comes from studying computer science right now. I mean, often when people are kind of entering dynamic industries, the specific stuff that they, Yeah. they study in school isn't super crucial. It's more the kind of learning that they get along the way. And I don't think that's changed with AI.

`[27:05]` **SPEAKER_00:** What advice do you have for the audience if you have like a young Michael Truel? Maybe not just three years ago. If they want to be like you three years ago before they start Cursor, what should they be doing right now?

`[27:19]` **SPEAKER_02:** I think just working on things that you're interested in and doing it with people both that you enjoy being around, but that you respect a ton, and taking that really seriously. Yeah, I think that for a lot of people that are in school, there's so many things that pulls you toward more checking boxes and less focusing on building something up over time and really focusing on something that you're interested in.

`[27:48]` **SPEAKER_00:** All right, let's give it a round of applause to Michael. Thank you so much. Yeah, of course.

`[27:54]` **SPEAKER_02:** Thank you for having me.

`[27:55]` **SPEAKER_?:** Yeah.
