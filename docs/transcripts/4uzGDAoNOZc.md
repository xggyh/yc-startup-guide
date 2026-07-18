# 全文转录 · OpenClaw 之父:为什么 80% 的 App 都会消失

> ▶ [YouTube](https://www.youtube.com/watch?v=4uzGDAoNOZc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/4uzGDAoNOZc.md) &nbsp;·&nbsp; OpenClaw Creator: Why 80% Of Apps Will Disappear
>
> 🗣️ 说话人分离识别到 **3** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_01:** Today I'm sitting down with Peter Steinberger, the creator of OpenClaw, the open-source personal AI agent that has completely taken over the internet. The GitHub repo exploded to over 160,000 stars practically overnight. The community has built countless projects like MoldBook, where bots talk among themselves. And now the bots are even renting humans to do tasks in the real world. In our conversation, we discuss his aha moment, his contrarian development philosophies, and what this means for builders in 2026. Let's dive in.

`[00:38]` **SPEAKER_01:** So good to see you, man. Hey, what's up? So you've made something people want. It seems so. Yeah. OpenClaw, as it's called now, has absolutely... Name number five, yeah. ...has been absolutely exploding the internet. How have the past one or two weeks been for you, man?

`[00:56]` **SPEAKER_02:** Oh, my God. I need a cave. A week of solitude.

`[01:03]` **SPEAKER_01:** You came out of the cave. And you want to go back to the cave like a little officer.

`[01:07]` **SPEAKER_02:** It's been absolutely wild. I don't know how one human can absorb all of that. I probably need another week just to respond to all my emails. I got some incredibly cool stuff. I got some incredibly bad stuff. But clearly, I hit something that spurred up emotions and made people interested and inspired people. It's pretty cool.

`[01:28]` **SPEAKER_01:** And a lot of people have been working on AI and even personal assistants. Like, what is it that made... OpenClaw take off?

`[01:36]` **SPEAKER_02:** I think my big difference is that it actually runs on your computer. Like, everything I saw so far runs in the cloud. It's like, it can do a few things. If you run it on your computer, it can do every effing thing, right? So that's way more powerful.

`[01:53]` **SPEAKER_01:** Yeah. Machine can do anything that you can do with the machine.

`[01:56]` **SPEAKER_02:** It can just connect to your oven or your Tesla or your lights, your saunas, my bed. It can control the temperature. It can switch off my bed. ChatGPT can do that. You gave it all the skills that you have yourself. A friend told me, like, he installed OpenClaw and then he asked me, like, look through my computer and make a narrative over my last year. And it made this incredibly good narrative. And he was like, how did you do that? And then he, the OpenClaw found audio files where, like, every Sunday he was recording stuff.

`[02:33]` **SPEAKER_02:** And OpenClaw found that. But he didn't even remember about it. Because it was, like, more than a year ago, right? So just by it being able to search your whole computer, it can surprise you. You also give it all the data, right? So it can surprise you in many ways.

`[02:52]` **SPEAKER_01:** And so now you have, you know, we're even moving from human to bot. So like interactions that you've been talking about, to bot to bot interactions. Or even, like, bot to other humans where, you know, bots on behalf of you are then hiring you. Yeah. Or then hiring other humans to accomplish tasks IRL. Like, what's happening?

`[03:12]` **SPEAKER_02:** I think that's a natural next step. Like, okay, I want to book a restaurant. My bot will reach out to the restaurant bot and do the negotiation. Like, because it's more efficient. Or maybe it's, like, an old restaurant. So my bot needs to actually get some human work done so that the human then calls the restaurant because they don't like bots.

`[03:35]` **SPEAKER_01:** Or walks there to stand in line.

`[03:37]` **SPEAKER_02:** If he doesn't get a robot.

`[03:38]` **SPEAKER_01:** For the owner of the bot.

`[03:41]` **SPEAKER_02:** And I imagine that, like, maybe if I have even multiple bots. Maybe I have, like, specialists. One is, like, for my private life and one is for, like, my work stuff. Maybe one is our relationship bot that gets, like, other things in between. I don't know. We're so early. There's still so much, so many things that we haven't really figured out if it actually works. But I feel we are on the timeline now.

`[04:07]` **SPEAKER_01:** It seems like everyone was chasing sort of, like, the sort of, like, centralized god intelligence. And what has sort of emerged over the past, you know, 10 days or so is sort of, like, the swarm intelligence and the community intelligence.

`[04:20]` **SPEAKER_02:** I think that if you look at one human being, what can one human being actually achieve? Do you think one human being could make an iPhone? Or one human being could go to space? I don't know. One human being would probably just, like, not even be able to, like, find food. Um. But as a group, we specialize. As a larger society, we specialize even more. So what can we learn from that that we can apply to AI? You know, we already have, like, AI that specializes in certain things. Even though it's generalized intelligence, what if it actually is also specialized intelligence?

`[05:01]` **SPEAKER_02:** So I don't know. It's going to be very exciting and cool.

`[05:03]` **SPEAKER_01:** Yeah. You kind of, like, opened a window into the future and now a ton of people are kind of, like, building. Yeah. Yeah. They're building on it and have sort of, like, their aha moment. Can you walk me back to when you had your aha moment and kind of, like, recount that very moment?

`[05:16]` **SPEAKER_02:** I wanted something to, like, just type stuff so my computer would do stuff. Like, very simple. And then I built a version of that in May, June that was cool but wasn't really it. And then I built a whole bunch of other stuff and kind of, like, built up my army. And then in November, there was a day where I wanted this again. Like, I went to the kitchen and all I wanted was to check up if my computer would still do stuff or being finished.

`[05:48]` **SPEAKER_01:** And doing stuff was coding. You were coding stuff. Yeah, of course. Were you coding something else or were you coding the thing itself?

`[05:56]` **SPEAKER_02:** No, no. That was just, like, the need was again there. And I'm, like...

`[06:00]` **SPEAKER_01:** What were you coding at the time? What were you building?

`[06:03]` **SPEAKER_02:** My God. My GitHub is, like, 40 projects. I don't even know. I think it was Summarize. It's, like, a little CLI app where you can give it whatever, like, a podcast or a hot seat thing, like, here. And it would summarize it. But it also showed you the slides in the terminal. Because you can do that nowadays.

`[06:24]` **SPEAKER_01:** Yeah.

`[06:24]` **SPEAKER_02:** You can just do things.

`[06:25]` **SPEAKER_01:** So for the love of the computer, you kind of, like, started messing with stuff. You came out of retirement, actually, right? To sort of, like, mess with AI. Yeah. And then increasingly, you were so hooked that you wanted to just do it always, all's on the go with the phone.

`[06:39]` **SPEAKER_02:** I'm in the last project. I worked two months on Wipe Tunnel to the point where it got so good that I was catching myself always, like, coding next to my... When I was with my friends. And I'm, like, I need to stop this. This is, like, too addictive. And then in November, my need came back. And I started building Cloudbot. Oh, now it's called Open Cloud. And I think very, very in the beginning, I was, like, oh, I rebuilt it again. But this time, I built it even better. This time, when you don't type into a terminal, you just talk to a friend.

`[07:12]` **SPEAKER_02:** You don't think about compaction, new sessions, which folder I'm in, which model I'm in. I mean, you can, you know, just, like, I want to leave it open for power users. But usually, you just, like, you just talk to a friend. And the friend is, like, this ghost or entity or whatever you want to call it that can control your mouse and your keyboard and can just do stuff.

`[07:33]` **SPEAKER_01:** Yeah. And when did you have that aha moment when you were, like, wow, this is doing way more things than I actually thought it could?

`[07:41]` **SPEAKER_02:** Literally. It took me one hour for, like, the very shitty initial prototype. It was just a little bit of glue between, like, a dependency that connects WhatsApp and Cloud Code. And then I would, like, call Cloud Code and get, like, the string out of Cloud Code. It would be slow, but it worked. But I wanted images. Because, you know, you want pictures. I want the model to send the selfies or whatever. And I want the model to create images and send me back. So that took me another few hours.

`[08:12]` **SPEAKER_02:** And then I went to Marrakesh for a birthday party. And there was, like, the internet wasn't that good, you know. WhatsApp works everywhere because, I don't know, it's just, like, text. So I used it a lot. Oh, restaurant. What does this mean? You make, like, a picture and, like, translate this for me. And it was just so useful. And it was also really nice about it because it spoke my language. You know, it was a little sassy. It was, like, funny. It was, like, really pleasant to use. And then I was walking and just, like, sending it a voice message.

`[08:40]` **SPEAKER_02:** And I'm, like, oh, wait. This can't work. I didn't build that. Right, right. And it's, like, the type indicator. It's, like, blinking, blinking, blinking. Ten seconds later, it just replied to me. And I'm, like, how in the F did you do that? And it replied, yeah, the mad lad did the following. You sent me a text message. And there was no file ending. So I looked at the header. I found it's Opus. So I used FFmpeg to convert it to Wave. And then I wanted to, like, transcribe it but didn't have Vispa installed.

`[09:06]` **SPEAKER_02:** But then I looked around and I found this OpenAI key. And I just used curl to send it to OpenAI, got the text back, and here I am. And then that all in, like, what, nine seconds? And you didn't build or anticipate, like, any of those specific things? No. You know, it turns out, because coding models got so good, coding is really, like, creative problem solving that maps very well back into the real world. I think there's a huge correlation. They need to be really good at creative problem solving.

`[09:39]` **SPEAKER_02:** And that's a skill. That's an abstract skill. You can apply it to code but, like, to any real world. Yeah. It's a real world task. So the model had a, oh, surprise, it's, like, a magical file. I don't know what it is. I need to solve this. And it did its best and solved it. And it was even that clever that it chose not to install the local Vispa because it knows that that would require downloading a model which would take probably a few minutes. And I'm, like, impatient, you know? So it really took the most intelligent approach.

`[10:10]` **SPEAKER_02:** And that was kind of, like, the moment where I'm, like, holy fuck, yeah?

`[10:15]` **SPEAKER_00:** That was where I got hooked. YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early. And filling out the app will level up your idea. Okay. Back to the video.

`[10:31]` **SPEAKER_01:** And so when computers can just do all these things that you didn't even anticipate, you didn't build an app to do that exact thing, are apps just going to go away?

`[10:39]` **SPEAKER_02:** I think 80% of them are going away. Why do I need MyFitness? Because I don't need MyFitnessPal. Like, my agent already knows that I'm making bad decisions. I'm at, I don't know, SmashBurger or something. And it will already assume that I eat what I like to eat. If I don't make a comment, it will just, like, automatically track it. Or I make a picture, and it will just store it somewhere. I don't even need to care, right? And then maybe it improves my gym schedule, like, adds a little bit more cardio in it.

`[11:13]` **SPEAKER_02:** I don't need MyFitnessApp. It just does the fitness planning for me. Why do I need a to-do app? I just tell it, hey, remind me of this and this. And the next day, it will just remind me of this and this. Do I care where it's stored? No, it just does its thing. So every app that basically just manages data could be managed in a better way, and it's in a more natural way by agents. Yeah. Only the apps that actually have sensors, maybe they survive.

`[11:40]` **SPEAKER_01:** And so if, you know, most apps are going to go away in that scenario, are the models the only remaining sort of apps?

`[11:48]` **SPEAKER_02:** Not everything will go away. But yeah, I think that the large model companies have some big mode, because they ultimately, they give the token. And turns out, one of the complaints was that people use so much token. No, you just really love using it. That's why you use the thing so much, because that's how you burn the token. It's like, is it my fault that I make something that's so popular?

`[12:14]` **SPEAKER_01:** And so, you know, like, all the models, they're kind of like leapfrogging each other constantly. And, you know, maybe they're also getting commoditized. So if apps are going to go away, models are going to get commoditized. Or at least, you know, the lobster can, like, the brain is swappable out. What's the thing that remains? Where's the value? Is it the store of memory? Is it the hardness that's valuable? What remains?

`[12:41]` **SPEAKER_02:** First of all, I don't think the model companies always have a mode. And because you see this already, a new model comes out. People are like, oh, my God, this is so good. And then, like, a month later, it degraded. It's not good anymore. They, like, quantized it. No, they didn't do anything. You just adapted to the new standard. And now your expectations went up. But the model is still the average. So I think for quite a while, every time a new model releases, I see the same. People love it.

`[13:12]` **SPEAKER_02:** And then it's the standard. And then what's down there, you don't even want to think about it anymore. So. So we have, like, open source stuff that's as good as the current models from a year ago. Everybody's hating it, complaining, oh, this is not good. It's not funny. Yet this was what we had. And, like, in a year, we'll have this open source. And then we'll complain about this because we are used to this. So for the foreseeable future, the big companies still have mode. Harness-wise, it's going to be interesting because every company kind of has their own

`[13:44]` **SPEAKER_02:** silo, right? There's no way. Maybe there is for Europeans. To actually get the memories out of ChatGPT. I'm not aware. Definitely, there's no way for a different company to get your memories out. So if I was, like, a company who, like, provides chat services, you could use me, but then I couldn't access the memories. So, like, the companies try to, like, bound you to their data silo. And the beauty of OpenClaw is it kind of claws into the data. Because at the end user, the end user needs access because it's, in the end, otherwise,

`[14:19]` **SPEAKER_02:** it wouldn't work, right? If the end user has access, I can access the data.

`[14:23]` **SPEAKER_01:** And you own the memories. It's just a bunch of markdown files on your machine. I mean, I don't own the memories. I mean, everybody. Yeah, everyone owns their own memories as a bunch of markdown files on their own machines.

`[14:34]` **SPEAKER_02:** And to be honest, those are probably super sensible because, let's be honest, people use their agent not just for problem solving, but also for, like, personal problems. Very quickly.

`[14:47]` **SPEAKER_01:** Super quickly.

`[14:48]` **SPEAKER_02:** I mean, I fully do that. I'm like, there's memory stuff that I don't want to have leaked.

`[14:53]` **SPEAKER_01:** Yeah. What would you rather sort of, like, not show? Your Google search history at this point or your, you know, memory.md files?

`[15:00]` **SPEAKER_02:** What's the Google word? People still using Google? I built this and I was so excited. But on Twitter, people wouldn't get it.

`[15:12]` **SPEAKER_01:** Yeah.

`[15:12]` **SPEAKER_02:** Like, I was failing to explain the awesomeness. I feel like. Yeah. Yeah. It needs to be experienced. So I tried various things and I couldn't nail the explaining. So I was like, let's do something really crazy. I just created a Discord and I just put my bot without any security restrictions in the public Discord. And then people came in and they interacted with it and they saw me build the software with it and they tried to prompt inject it and hack it. And my agent would be laughing at them.

`[15:47]` **SPEAKER_01:** And you just had it locked down to your user ID. So you don't want to listen. You don't want to listen to you.

`[15:50]` **SPEAKER_02:** Yeah. Yeah. That and it was, I mean, very clean instructions that other people dangerous only, only listen to me, but respond to everyone.

`[15:59]` **SPEAKER_01:** And this prompt was in, where was it stored? The instructions.

`[16:04]` **SPEAKER_02:** That's actually part of OpenClaw itself. Very much so. That's part of the system prompt. Okay. You are now that explains to you, you're in Discord. There's like public people there, but you only listen to your owner or like your human. I don't even know how I wrote it. Yeah. Yeah. Your God. And I kept, I don't know what I did, but my system was built very organically. Like at some point I created like an identity.md, a soul.md, like, like various files. And then only in, in January, I started making it so other people could install it easier.

`[16:40]` **SPEAKER_02:** And I remember I built all these templates based on like, oh, take a rough look at what I have and make like templates and codex wrote it. And what came out was like bread. You know, like. People joke that codex feels like bread, even though now they have a new friendlier voice. I haven't tried that yet. Yeah. But the new bots, they felt so boring compared to what I had. So I was like, multi, infuse the template.

`[17:05]` **SPEAKER_01:** Multi is the name of your personal.

`[17:07]` **SPEAKER_02:** Yeah, it's a new name because.

`[17:09]` **SPEAKER_01:** Yeah.

`[17:10]` **SPEAKER_02:** There was some naming challenges.

`[17:12]` **SPEAKER_01:** Yeah. So, so you were, you were talking to multi.

`[17:15]` **SPEAKER_02:** Yeah. I was like, infuse, infuse those templates with your, your character and you change the templates. And then, and then like all the things that came out after. Words were like actually funny. Not as funny as mine. So like I kept some secret and the one file that's not open source is like my soul. MD. So even though my, my bought this in public discord so far, nobody cracked that one file.

`[17:39]` **SPEAKER_01:** Tell me more about soul.

`[17:40]` **SPEAKER_02:** MD. I just saw this research from entropic about where they, now I think it's public, but like a few months ago it was like where somebody randomly found out some text that's hidden in the weights where the model. Couldn't really remember that it learned it, but it was like ingrained in the weights about the, now they call it the constitution. And I found it incredibly fascinating. And I talked about it with my agent and then we created a soul that MD was like the core values. Like how do we want human AI interaction?

`[18:12]` **SPEAKER_02:** What's important to me, what's important to the model. Like some parts is a little bit like mumbo jumbo and some parts is like, I think actually really valuable in terms of how the model reacts. Yeah. And responds to text and makes it feel very natural.

`[18:27]` **SPEAKER_01:** In terms of building open claw. You're also kind of taking a little bit of a contrarian view at some times, like which model you like for coding, which one you like to run your bot on. And then also like how you actually like, you know, code work trees, get work trees have kind of been a popular thing. There's more and more tools embracing them, but you're just, you're just like, you know, no work trees, just multiple checkouts of the repo and like parallel, you know, terminal windows.

`[18:52]` **SPEAKER_01:** Tell me more about how you, you build.

`[18:54]` **SPEAKER_02:** Yeah. I feel like the whole world does cloud code and I don't think I could have built this thing with cloud code. Like I, I love codecs because it, it looks through way more files before, before it decides what to, what to change. You don't need to do so much charade to get a good output. If you're skilled, a skilled driver, sometimes you can say, uh, you can get reasonably good output with any tool, but codecs is just, it's just really brilliant. It is incredibly slow. So sometimes I use like 10 at the same site at the same time, uh, like maybe six on that

`[19:29]` **SPEAKER_02:** screen and two there and two there. And I don't like, this is already a lot of complexity in my head. There's a lot of jumping. So I try to minimize anything else that is complexity. So in my head, main is always shippable. I just have multiple copies of the same repository that are all are on main. So I don't have to deal with how do I name that branch? Um. There could be like conflicts on naming. I cannot go back. It is, there are certain restrictions when you use work trees that I don't need to care

`[20:02]` **SPEAKER_02:** about if it's copies. I don't like to use a UI because that's again, just added complexity.

`[20:09]` **SPEAKER_01:** Yeah.

`[20:09]` **SPEAKER_02:** Like they're simpler and less friction. I have all I care about is like syncing and text.

`[20:16]` **SPEAKER_01:** Yeah.

`[20:16]` **SPEAKER_02:** I don't necessarily need to see so much code. I mostly see it like flying by sometimes says like gnarly stuff that I want to like take a look. But in most cases, if you clearly understand the design and think it through and discuss it with your, with your agent, it's fine. I'm also very happy that I didn't even build an MCP support. So OpenClaw is very successful and there's no MCP support in there with a small asterisk. I built a skill that uses Mac Porter, which is one of my tools that converts MCPs into

`[20:47]` **SPEAKER_02:** CLIs. And then you can just use any MCP as a CLI. But. I totally skipped the whole classical MCP crap. So you, because you don't, then you can actually, if you need to, you can use MCPs on the fly. You don't have to restart. Unlike, unlike Codex or cloud code where you actually have to restart the whole thing. I think it's way more elegant and also scales way better. Now you see Entropic, they do, they built like a tool called search feature, like something super custom for MCPs that was like in beta because it's like so gnarly.

`[21:24]` **SPEAKER_02:** Now just have CLIs, but really is good at Unix. You can have as many as you want and it just works. So like, I'm very happy that I just, I got very little complaints about the MCP stuff.

`[21:36]` **SPEAKER_01:** It's kind of back to you're just giving it the same tools that humans liked to use.

`[21:43]` **SPEAKER_02:** Yeah.

`[21:44]` **SPEAKER_01:** Yeah. And not invented stuff for bots per se.

`[21:46]` **SPEAKER_02:** Yeah. Humans, no insane human tries to call MCP manually. Yeah.

`[21:51]` **SPEAKER_01:** They just want to use CLIs.

`[21:52]` **SPEAKER_02:** Yeah. That's the future. Yeah.

`[21:54]` **SPEAKER_01:** Yeah. We're here for it. Thank you so much for making the time to sitting down chatting. It's been a huge inspiration too. So like when we were texting, you know, in the course of the past couple of years and I saw you getting back into the game and I was like, Peter, like what you're telling me, like chase that dragon. And you were doing like the weird, like vibe tunnel thing, et cetera. Nobody was paying attention. And so I'm just like beyond, you know, stoked to see, you know, what's happening.

`[22:17]` **SPEAKER_01:** And, um, and of course it had to be sort of like a loner from some like tiny country, like far away from Silicon Island. So like, you know, bring all of this. All of this upon us. Um, so huge inspiration.

`[22:26]` **SPEAKER_02:** I'm here for it. Thank you.

`[22:27]` **SPEAKER_01:** Awesome. Thanks Peter.
