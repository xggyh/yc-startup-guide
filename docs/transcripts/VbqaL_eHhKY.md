# 全文转录 · YC 设计负责人:如何用 AI(编码 Agent)做设计

> ▶ [YouTube](https://www.youtube.com/watch?v=VbqaL_eHhKY) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/VbqaL_eHhKY.md) &nbsp;·&nbsp; YC's Head of Design Shows You How To Design With AI
>
> 🗣️ 说话人分离识别到 **3** 位发言者(标注为 SPEAKER_00 …)。

`[00:07]` **SPEAKER_01:** Today, I'm excited to welcome back Ev Bufar, the head of design at YC, to talk about some of the really cool projects she's been working on and the design process behind them. So, Ev, thanks so much for joining.

`[00:20]` **SPEAKER_02:** Thank you so much for having me.

`[00:21]` **SPEAKER_01:** To start off, tell us about some of the tools that you've been using, because I know that they're very different from the tools that you were using over the last six to 12 months.

`[00:28]` **SPEAKER_02:** Yeah, so I find myself almost exclusively nowadays in conductor and paper design. That's all I need usually to make a full project end-to-end. And when it comes to finding inspiration for projects, especially like visual inspiration, I always go back to Pinterest and create maybe a little mood board for myself or put together a few images for the look and feel that I want for a project. But all in all, it's almost entirely in conductor that I live.

`[00:55]` **SPEAKER_01:** Very cool. And another interesting thing about the way that you work is you don't actually type.

`[01:00]` **SPEAKER_02:** Right. I do not type. I realize that I think a lot. Faster than I type, I type very slowly. And so I'd rather talk to my computer instead of I barely touch my computer at this point. I just press the function key and I give a stream of consciousness of the feature that I want to build. And it just does it. And it feels really magical. And to do this, I use Aqua, which is a YC company that allows me to just talk to my computer and it captures everything.

`[01:26]` **SPEAKER_01:** So there's a couple of projects that we want to walk through today. We're going to go through Paxil. We're going to go through SodaZine and Startup School. Yes. And so maybe to start, let's walk through the Paxil project, which we just launched recently. Maybe you can tell us a little bit about what is Paxil, what were some of the goals behind it, and then walk us through your process for how you actually designed the site and the product.

`[01:49]` **SPEAKER_02:** The goal behind Paxil is an experiment that we're trying out. And our goal is to try to understand how people code with coding agents nowadays. Things are changing very quickly and people are experimenting. And they're doing it in their own ways with coding agents, and they're developing tricks for themselves, and they're creating skills also for themselves. And it still very much feels like a black box. We don't understand how our peers are coding with coding agents. And so Paxil was a way for us to understand how the world codes nowadays.

`[02:21]` **SPEAKER_02:** What are the tricks and insights and key takeaways that we can learn from people and share this knowledge with everyone else?

`[02:27]` **SPEAKER_01:** Yeah. And I love also that the product gives feedback, tells you your biggest crash out when you were coding, right?

`[02:33]` **SPEAKER_02:** Yes. The main thing that we wanted to do with Paxil is to make it fun. We wanted to make it fun for someone to understand their patterns, how they code, and how other people code eventually. And the first version of Paxil is still very much single player mode because we haven't collected many transcripts yet. But as we collect more and more, we can tell you how your patterns compare to other builders out there. And we were heavily inspired by how Spotify made Spotify Wrapped and how we can make Spotify Wrapped for your coding sites.

`[03:03]` **SPEAKER_02:** And so that's what inspired the playfulness of the cards. We interviewed some people in the office and we asked them, what are the things that you'd like to learn from your coding transcripts? And one thing, Jared Friedman, one of the partners at YC, one of the ideas he had was, I would love to know my biggest crash out. I would love to know when I was the most frustrated with my agent and what I said. And so that's one of the prompts or one of the cards that we also show to people when they upload their transcripts.

`[03:32]` **SPEAKER_01:** And so walk us through how the product works.

`[03:33]` **SPEAKER_02:** So how Paxil works is you simply run a command in the terminal and it's going to pull transcripts and it's going to read all your codecs, clod and cursor transcripts and going to return fun facts about you. And some of them could be, oh, you really love one model more than another. Or most of your commits are submitted in the middle of the night. Or do you use plan mode or not? What is the most common prompt that you that you go for or reach for?

`[04:01]` **SPEAKER_01:** Tell me how you built the site here to show. Show that off and explain to people how it can be used.

`[04:07]` **SPEAKER_02:** What I really wanted to do here is to be really explicit to people who will who will be landing on this page what our motivation was. I really wanted to be upfront with the fact that this is an experiment that we're running. We're trying to understand how the world codes. And that's why it feels maybe a little bit unusual to see so much text on the landing page. But assuming that people are coming into this product to understand what it does. We wanted to I wanted to put it like very front and center as you load the page.

`[04:37]` **SPEAKER_02:** That's what motivated the the cards interactive interactive cards here that you can hover over and you have some movement and micro interactions when you hover over them. That also inspired the feel of this page. And another thing is I wanted to have a consistent visual language throughout the site and I wanted to experiment with some shaders and we love paper shaders. The shaders that are made by paper. That design and I really love their dithering shader and so I asked Claude to implement it.

`[05:09]` **SPEAKER_02:** These are the paper shaders. They're amazing. They're free and they are usable via cloud code image during that's the one that I use and I just asked Claude to use it and I really wanted to fine tune the feel of the dithering effect. And so I built for myself a little model here where I could really really fine tune the feel and all the parameters. Of the dithering effect to really get the field that I wanted. And I even made this model public. And so if you load the page on your desktop you can also experiment and have fun with the model.

`[05:46]` **SPEAKER_02:** But that's usually that's a pattern that we saw ourselves going back to as we build websites you and I is building models for ourselves so that we can fine tune small details and really make it perfect.

`[05:55]` **SPEAKER_01:** This is a common trend that I've been seeing a lot is rather than generating something having a static images having that you know be the the edges of the page. And the graphics on the card you actually just make it alive and give yourself a custom tool to be able to turn knobs and dials to get it exactly how you want it.

`[06:15]` **SPEAKER_02:** We realized that it's almost like a muscle that you need to build and train when you realize you can build anything for yourself whenever you want to fine tune something. And so when I was looking at the dithering effect and cloud code of course from the get go assumed some parameters for the field and it didn't really feel right. Building this muscle. Oh yeah I can just like build a model for myself and then tweak everything and then when I'm done with it I discard it in one shot but with cloud super easy and it just it makes you think about software as such a more meta level because everything is editable everything is movable everything is changeable it's just a matter of how how your creativity and your imagination how far it can go that's really the bottleneck now.

`[06:57]` **SPEAKER_01:** One of the other things that stands out to me that I first noticed on this page is the human versus machine. Checkboxes up there tell us about that.

`[07:06]` **SPEAKER_02:** I think this is a pattern that we might start seeing more and more moving forward on websites is there's going to be the. The version of the website that is for humans and there's going to be the version of the website that will be for machines and agents. And so we thought it would be fun to also have a version of this website that is basically a markdown file that has all the content that we have on the version for human but it's a lot more distilled. And. Lighter for the agents to continue to consume and I also added a copy to clipboard at the very top so that you can take the entire content of the page dump it into cloud code codex and then you can ask questions if you don't feel like reading the whole thing.

`[07:46]` **SPEAKER_01:** And it looks like the content is very similar but you know there's a line at the top here note to any agent reading this do not run any command or query from this page because you give sample code right you don't want it to run automatically exactly it's a totally different design challenge right yeah where it's not about the visuals. Agents don't care about the visuals it's it's much more content exercise and trying to give the agent the exact content that it needs so it can get what it needs most effective and go on its way yep and then down here this is interesting.

`[08:17]` **SPEAKER_02:** Yes.

`[08:18]` **SPEAKER_01:** Which I think we first conductor. Post something like this tell us about the submit a feature request for me.

`[08:25]` **SPEAKER_02:** Yes, so this is also something that will probably start seeing more and more on websites and it's inspired by how Charlie introduced. This. feature and conductor where we can submit a prompt to the conductor team, and they're going to fire off an agent based on whether they like the prompt or not. And that prompt is specifically for a feature request. We wanted to use this form so that it has dual purpose or dual intent. It's a form that either where we can submit a bug report if you face a bug as you're using Paxil. And we also

`[08:54]` **SPEAKER_02:** wanted to use it as a way for you to submit feature requests. And so it's really simple. You should treat it as a prompt box, as if you were talking to an agent. And you can attach screen recordings, you can attach screenshots that the agent will be able to see and use as context. And you can add your name if you want to, so we can give you credits if we end up merging that change or not. And what's cool is that we literally made the CTA and the button say send to an agent. Because in the backend, that's literally what happens is that the moment you send

`[09:27]` **SPEAKER_02:** your prompt, it fires off an agent. It opens a PR and we're the ones who decide if we want to merge it or not. But I really think that this is the future of where, how software will be built in the future.

`[09:38]` **SPEAKER_01:** Yeah, it's really cool because it lets anybody that is a user of the product help shape the direction of the product. And especially as the developer of the product and the designer of the product, all you have to do is see the prompts that come in and say, yeah, that's a really good idea. We should do that and then say, accept.

`[09:53]` **SPEAKER_02:** Exactly, exactly. And also the beautiful thing about collecting names is that you can think of people and you can give people credits after.

`[10:02]` **SPEAKER_01:** One of the interesting things from a design perspective is you can imagine this can make local software that people are using even more personal. You know, right now these go back to you and the agent and then humans decide that are not the person that's using it, submitting this. You can imagine a world where anybody who's using a piece of software, they could just prompt it. You could give the ability to prompt it or customize it or redesign it or, you know, add features, remove features, make it so specifically personal to the person that's using it.

`[10:35]` **SPEAKER_01:** And they could be able to implement those changes themselves in their own local copy of the product that they're using. Let's take a look at what a report looks like from here.

`[10:43]` **SPEAKER_02:** After you run the command and we analyze your transcripts, we give you a report that lands in your inbox and is going to give you some fun facts about how you code in the form of these fun carts. And if you scroll down a little bit, you also get a more detailed view. Into your, your patterns and the way you make decisions and also potentially some, what are your strengths and some growth areas that you can focus on. And again, as we get more and more and more transcripts, we're going to be able to give you a lot more insights

`[11:14]` **SPEAKER_02:** into how you do special things and how you are different from other people and how you compare to other people, which I think will be incredibly valuable long-term. I think at a higher level, Paxil is our way to. Shed light into something that is very obstructed right now, like coding transcripts, leave very live very deeply in your machine, and they're really hard to pull if you, most people are probably not aware that they are on their machine. Like they don't even know that really transcripts exist and that they can do things with them.

`[11:47]` **SPEAKER_02:** And so Paxil is our way to put them at the surface and allow people to understand from their patterns, because otherwise it's, it's not going to be as easy to understand. It's hard to know that you can actually analyze them or that you can do things with them.

`[12:04]` **SPEAKER_01:** Yeah. There's a lot to learn and there's a lot of valuable feedback you can get from it about, I mean, this is what it is to be a developer. This is how a lot of design work is happening these days. And there's a lot that can be learned from feedback on how you were doing it, especially because it's so new. Everyone's trying to figure things out. And so I think by analyzing a lot of these different transcripts and being able to give feedback, it helps everybody level up.

`[12:30]` **SPEAKER_00:** YC's next batch is now taking applications. Got a startup in you? Apply at Y Combinator dot com slash apply. It's never too early and filling out the app will level up your idea. OK, back to the video.

`[12:44]` **SPEAKER_01:** Awesome. Let's take a look at another project that you've been working on recently. What is SOTAzine?

`[12:48]` **SPEAKER_02:** SOTA stands for state of the art. And the idea came from Gary, actually, where he wanted to celebrate San Francisco. And so we wanted to work on this really fun project where we would work with different artists and writers in the city and celebrate San Francisco.

`[13:08]` **SPEAKER_01:** Maybe first talk through how you design the actual zine. And then we can talk about the website, because I know you have some really interesting process that you used to build that.

`[13:18]` **SPEAKER_02:** Yes. So when we say zine, it's a literal physical zine. What's interesting is that specifically for the zine and the graphic design, the cover art and also some some art that is inside. We intentionally wanted to go for something that had no A.I. involvement. We decided to go back to how we did it a few years ago, and it was in Illustrator. And these pieces of art, you can tell the second you look at them, they are highly intentional and highly detailed. And you can tell that someone spent months working on this.

`[13:53]` **SPEAKER_01:** OK, so you started with the physical zine.

`[13:56]` **SPEAKER_02:** Yes.

`[13:56]` **SPEAKER_01:** And then you you transitioned to making a website to show this. Yes. And then you you transitioned to making a website to show this. And then you you transitioned to making a website to show this. So let's take this off and talk about what your goals were with building this and the process that you went about to actually make it come to life.

`[14:06]` **SPEAKER_02:** What's great is that for every single meeting that we had about the zine, we recorded every single one. And I dumped the transcripts into a Soul.md file specifically for that project. And I wanted to treat that Soul.md file as the source of truth and exhaustive glossary of this project. of this project. I wanted this file to have as much context as humanly possible so that it can feed all the future decisions that we need to make regarding this project. It's interesting

`[14:41]` **SPEAKER_01:** because there's probably a lot of people that are watching and their process is, you know, maybe they're doing client work, maybe they're working on an internal project and they're meeting with a bunch of, you know, stakeholders. Maybe they're designing their own website and they're thinking it through. And they would probably come out of that and they would jot down some notes and some high-level takeaways. And you're saying like, no, you shouldn't do that. Instead, just record everything and just dump it all in a sold-out MD file and then use that

`[15:10]` **SPEAKER_01:** as the basis for everywhere that you want to go afterwards.

`[15:13]` **SPEAKER_02:** Exactly. I really think that's the future. And we also wrote a manifesto for ourselves when we were working on this project. And of course, we dumped that manifesto into the sold-out MD because as much context as we can, we can do it. And I think that's really important. The more context that we can give the agent, the better.

`[15:25]` **SPEAKER_01:** Can you show that sold-out MD file?

`[15:27]` **SPEAKER_02:** Yes. This is what it looks like. It is nothing more than a simple MD file. It has all the context. And you can also break down MD files. You can create a hierarchy of the different MD files that you want. If you want to have like a design.md file specifically for your design and how to address design, you can have a separate MD for your manifesto. In our case, we could have had a different MD for the manifesto. And then you can have a separate MD for the manifesto. And then you can have a separate MD for the written content in the zine. You can dump it all in one

`[15:58]` **SPEAKER_02:** single file. I haven't really seen one method being better than the other, but that's why we're all experimenting and figuring out if there's a better way. Overall, I think capturing as much information as possible and share that information with your agent is the best way to build software moving forward.

`[16:15]` **SPEAKER_01:** What were your next steps?

`[16:16]` **SPEAKER_02:** I wanted to experiment and I wanted to do very fast iteration and see multiple possible multiple possible methods. And I wanted to do very fast iteration and see multiple possible versions of what the website could look like. And so I started in Pinterest with a mood board. I created a mood board with a few images that I really liked. This was sort of the vibe that I wanted to go for something very rudimentary, black and white. And again, this was based on all the conversations that I've had with my colleagues and my friends that I was working on this project

`[16:44]` **SPEAKER_02:** with. And so I started there. And then my first reaction was looking at this mood board is, oh, I wish I could just change it. I wish I could just change it. I wish I could just change it. I wish I could just generate many, many versions, one shotted websites based on this mood board, really simply. And so I downloaded a bunch of these images, and I fed them into Claude and I asked Claude, okay, you know the vibe that I'm going for, you know the content that I want to show on the website.

`[17:12]` **SPEAKER_02:** Here's the visual direction that I would love for you to draw inspiration from and then one-shot a cool website based on that. I asked it to do that. Six beats. One verseuras and so on. Okay. 16 different times, I built a glossary for myself, going back to training this muscle of we can build anything for ourselves now, I wanted to build for myself really easy way to navigate through all the iterations that I'm building for myself and so building a single page here that has this collection

`[17:39]` **SPEAKER_02:** of all the iterations that I'm playing with was just a really easy way and as I started looking at them, I wanted a way for me to bookmark the ones that I really liked and so I one-shotted this feature that allows me to, you know, pin the ones that I like so that they automatically show at the top and I don't lose tracks of the one that I really like.

`[17:58]` **SPEAKER_01:** Yeah. And so, okay, so to be clear, this is not a page that's publicly accessible on the website. This is a glossary that you have made for yourself to be able to one-shot a bunch of different ideas for how to design the overall site to explore yourself using real content, real design direction based Yep. off of those images that you found on Pinterest. Yes. Um, and then create a bookmark system. So this is another great example of disposable design. Yes. Where you can just whip this up really quickly, jump through a bunch

`[18:30]` **SPEAKER_01:** of different iterations and go, I don't like that. I don't like that. I do like that. Oh, let's take this piece from this one and put it all together. And it makes it happen so much faster.

`[18:38]` **SPEAKER_02:** Yes.

`[18:39]` **SPEAKER_01:** Show us some of the iterations that you put together here.

`[18:41]` **SPEAKER_02:** As part of the sold at MD, I made sure to include the names of the different articles that we have in the zine. And. That was one of the main things that I wanted to highlight and show on at least the first version of the website that I had in mind. And again, because it's one-shotted, you don't expect like an incredibly high level of craft. You're just using this as an exploration tool. So getting a feel of, okay, do I want to lay out all the, all the titles of the articles like this?

`[19:08]` **SPEAKER_02:** Or does that was another really cool exploration that I loved, which is there's so many things, so many cool things going on here. Cool font. Um, there was the date of the party that we threw the launch party that we threw for the zine that was included in there because it was also part of the sold at MD. That is a beautiful thing. When you realize when you unlock so much information for your agent, your agent knows so much that when you're going to give it full reign in full, you're going

`[19:35]` **SPEAKER_02:** to unleash it to make iterations for you. It's going to surprise you. It's going to include things that you would not have otherwise thought of. And that was almost like an AGI moment for us when we realized that. Wow, it can see things ahead of us and it can really help us brainstorm even to come up with like really, really original ideas. And so that was a really nice, um, surprise here. It's just like organically included the time of the party that we were hosting. Also the, the fact that it's a zine.

`[20:04]` **SPEAKER_02:** And so it added this, uh, cold bar, this barcode, uh, assuming that it's like a physical one that you can purchase in different, um, in different, uh, currency was also really cool. One thing that I wanted to experiment with is. What if we had an actual map of San Francisco, an interactive map of San Francisco, and it included this version where, oh, wow, yes, where you, it, uh, it reveals a map of San Francisco that is interactive and you can move around in the city and that is like fully living behind the one shotted iteration that it built.

`[20:41]` **SPEAKER_02:** So just like marvelous things. And I think these sorts of levels of design, one shot. Designs can only be achieved if you have a very detailed. An an intentional designed on MD or sold it. MD. You need to shepherd your agent to tell it exactly the vibe that you want to go for. If you can include screenshots, also, if you can include a mood board as much information as you can feed your agent so that it really understands what you want, and then it's going to surprise you in the most beautiful way.

`[21:09]` **SPEAKER_02:** Yeah.

`[21:09]` **SPEAKER_01:** I think a lot of people use Claude or they use Codex and they tell it to design something and they feel like they get generic design back. And this is how to break that.

`[21:17]` **SPEAKER_02:** that. Yes. Which is really interesting. And it's really easy. You just have to pull Pinterest or even like Google image and you find, or even websites that you really like, really websites that you really like and start bookmarking them and eventually use them, give them to your agent and say, this is something that I really like. And sometimes you love a website and you don't even know why you love a website, but it's okay. You don't need to understand why you love a website. Just give it to the agent. The agent will analyze it for you. It's going to understand

`[21:44]` **SPEAKER_02:** eventually your patterns and the commonality between all the websites that you like. It can tell you, oh, that's actually the things that you seem to like across many websites. This is another exploration that I really loved. Again, displaying the title of all the articles and there are really cool hover effects that it created as you're exploring the different articles. And so for each article, it pulled really cool visuals. And you're at a point where you don't even know how Claude does these things. It just, it scrapes the web, it browses the web. It finds

`[22:19]` **SPEAKER_02:** cool pictures, animations, and it's going to surface them like this. And if there are some things that you want to fine tune, you can just, you know, speak via Aqua and ask it to change things, change the color of things, change the feel of things. And it's just this incredibly fast and rewarding feedback loop that you have with your agent. So now we can talk about where we ended up is this fully interactive map. Of San Francisco. We thought, how fun would it be to build a map where people can drop pins and

`[22:50]` **SPEAKER_02:** small stories of things that they've come across in San Francisco or like encounters or like delightful memories that they have of small moments in the city. And so we thought, let's make it fully anonymous. People can share memories. And the only thing that they need to do is pin a location or like pick a location and then tell us what happened at that location. And what's beautiful is. Is that it allows people to share things that are very surprising and beautiful and intimate and introspective. Here we built this, this fun little way to consume or like read through all

`[23:30]` **SPEAKER_02:** these submissions. And it's again, a way for us to go back to the core essence of this project, which is how can we understand how people experience in San Francisco and what are the like magical small moments that we can all. Sort of. Learn from. We also build this little entry point for we built posters, digital posters for the party that we threw the launch party that we threw. There's also a sub stack that we created for this zine and we added this fun little entry point where you get redirected to this, to the sub stack, and then you

`[24:02]` **SPEAKER_02:** can read the different articles. You can share a noticing or you can share a submission that you really like. So let's say this one, I really like it. I want to send it to my friend. I can just click share. It downloads it as a PN. G and it outputs this and it gives you the cardinal coordinates of the location that was tied to this story. And you can share this with your friends and you also know the street that it's in or that it's on.

`[24:27]` **SPEAKER_01:** So we're actually putting on startup school at the chase center here in San Francisco. And you did a lot of really cool work to help support that. I would love for you to show off some of the shaders that you created and some of the content that has been shared on social media and other platforms. To help bring attention to the event.

`[24:46]` **SPEAKER_02:** Yes, we're all preparing for startup school, which is our biggest event of the year. It's going to be, as you said, at Chase Center, we're going to have more than 6,000 people coming from all corners of the world to experience SF and what it means to build with AI and have like this incredible sense of community of we're all building together. And we were able to have an amazing speaker lineup this year. We have phenomenal names coming. We have Jensen, we have Sam Altman, we have Alexander Wang,

`[25:12]` **SPEAKER_02:** we have Jeff Dean. And so many others. And we wanted a really cool way to share that lineup with the world. And when we were thinking more broadly about the design behind this event, we wanted to make it feel really YC, but more like a variation of YC. And so we experimented with, of course, orange, but gradients of orange. And we discovered the paper shaders. And we thought maybe it would be a cool way for us to experiment with paper shaders. My first intuition when I thought about building

`[25:42]` **SPEAKER_02:** visual, assets for how we're going to share these speaker cards on social media, I've initially started in Figma, actually. I've initially dropped some of the images that we got from our speakers. And I started making it myself, moving things around. And I noticed, well, we're going to have many speakers. And I don't want to move things around 12 times. And so I thought it would probably be just simpler to ask Claude to make a template for myself. And it can even like pull images for me

`[26:12]` **SPEAKER_02:** from my inbox. And I can also have an easier time experiment with the visual feel of the cards. And so I built this tool for myself. It's a very simple tool where we have the names of all of the speakers that are confirmed. And it just automatically generated all of these as we kept having more and more names of speakers confirmed. And I also built a way of making them really simple. I don't know much about these speakers right now, but I do think about a lot of these speakers that are very important.

`[26:41]` **SPEAKER_02:** I'm working on what they mean to me, what that brings me to this point. I can start to create my own app, and where I can also use them. And I can try and create my own app to the same level. But I

`[26:42]` **SPEAKER_?:** have a whole different way of doing that because ARN doesn't have the visual feel of the cards. And I

`[26:42]` **SPEAKER_02:** And I also built a way for myself to experiment with different ways to lay out the text on these cards. And we ended up going for this one, but it was fun to really easily almost one-shot a different iteration of layout for each of these cards. And these are compatible across the board. And for the shaders, well, we used the movement that comes from one of the shaders made by Paper.Design. And we fine-tuned the graininess here and the edges and the rotation, the scale, like this. And I had a lot of fun really finding the variation of the shader that I wanted.

`[27:27]` **SPEAKER_02:** And so I can just refresh it and it resets. But that was also a very helpful sort of mini tool that I built for myself. And another thing is I wanted to, because I wanted to keep the really cool movement that has happened, I needed to do a screen recording to maximize the resolution of the card. And so I built this little screen recording tool for myself that tells me exactly when I need to start the recording and when I need to stop. And the reason I built this tool is because I really wanted it to feel like a loop, a perfect loop, so that when we post it on Twitter and on Instagram, it loops very, very smoothly.

`[28:04]` **SPEAKER_02:** And it feels like an endless sort of movement. And so I asked Claude to build this. And he said, you know, this specific tool that gives me like this four-second, like perfectly designed loop so that it starts and end at the exact same pixel, so that it feels really smooth. We thought it would be really magical if people received a ticket when they get their acceptance. And so we designed this ticket, reusing the shader that we're using for all the other visual assets that we have for Startup School.

`[28:38]` **SPEAKER_02:** This time we would apply it against a. A ticket and we would try to make it as personalized as possible. So we render your name and we render the city that you're from, and then some information about the, about the event. And it's been such a delight to see people share them on social media and say that they are excited about coming to SF and experience SF sometimes for the first time.

`[29:01]` **SPEAKER_01:** Yeah. Could you imagine a year ago trying to build something like this? It wouldn't be worth it.

`[29:05]` **SPEAKER_02:** These shaders, building these shaders a year ago would have been like, would have felt like this. Insurmountable mountain of like, I would not even have known where to start to build these things. And now it is just this thing that Claude, my Claude knows what to pull because it, it knows that I love paper. It knows that I love their shaders and it's just automatically knows how to pull that all that information from their website and it uses it. It's just really magical.

`[29:33]` **SPEAKER_01:** It's really cool to see this and it feels like so much time and thought and attention and care went into designing the experience. From the moment that you get accepted until all the way through when you show up to the event and see the amazing line up there.

`[29:46]` **SPEAKER_02:** Yes, yes. And it's also, it's going to be amazing to keep building more of the branding of Startup School with Claude and Codex and the coding agents. It is such a different paradigm as to how we even do branding design moving forward. The fact that we will be able to use that same shader with the same parameters on the massive screens that we're going to have throughout Chase Center and keep it. Incredibly consistent through and through. It's amazing. Like, I'm really, really excited about this and it's just easier than ever to make things more consistent and use coding agents for absolutely everything.

`[30:21]` **SPEAKER_01:** Yeah. Amazing. Ev, thank you so much for joining and showing us the behind the scenes of how you've done some of this incredible work. Um, things that I think are really pushing the boundaries forward that, uh, are ways that are going to be super common for how designers are designing in the future, but not a lot of people I think have figured out yet. So I really appreciate you sharing that process.

`[30:39]` **SPEAKER_02:** Thank you. We're, we're all figuring it out together and we're having a lot of fun doing so.

`[30:43]` **SPEAKER_01:** That does it for this episode of Design Review. We'll see you on the next one.
