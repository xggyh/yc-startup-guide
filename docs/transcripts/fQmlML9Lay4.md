# 全文转录 · 像指挥家一样管理一群编程 Agent:Conductor CEO 的 AI 编码工作流

> ▶ [YouTube](https://www.youtube.com/watch?v=fQmlML9Lay4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/fQmlML9Lay4.md) &nbsp;·&nbsp; Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup
>
> 🗣️ 说话人分离识别到 **2** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_01:** Hello, I am Charlie, the co-founder of Conductor, which is an app that lets you orchestrate a bunch of coding agents on your Mac. And we were YC summer 24, and I'd love to show you my setup. So a recent thing that I can't live without is this gooseneck microphone, $20 on Amazon. We are all trying to talk to our computers more. One issue with having like an open floor plan office is that can be pretty distracting. So one advantage of these is you can like lean over and whisper into cloud and be like,

`[00:41]` **SPEAKER_01:** please merge PR 3475. And it's a little bit less disruptive. We all got these in an attempt to encourage more talking to computers. I spend most of my day in Conductor. We're using Conductor to build Conductor. One thing that I do is I'm constantly kicking off new tasks. So I'm constantly going command N. That was actually a sneak peek of something we are working on, which is cloud workspaces. But I'll do command N and then I'll speak into my computer. So I'll do command N and then I'll speak into my computer.

`[01:08]` **SPEAKER_01:** And say, can you take a look at the latest linear issue and give me a rough pass at how you'd solve it? Stuff like that. And then press Enter. And then I can see that it's running in the sidebar. And while cloud is working, I'll go to another chat. I'm very into keyboard shortcuts. So I try to make everything have a keyboard shortcut. So in this case, I'll do command shift Y. I can see here that this workspace is ready to merge. So I'll take a look at it, give cloud a quick review. In this case, it's a pretty small PR.

`[01:38]` **SPEAKER_01:** So it looks good to me. But quite often, cloud won't get things exactly right. And I'll give things a comment, like a GitHub style comment. Say, this looks a little bit weird to me. Why do we need this? Press Enter, get cloud running, and then go back to a different workspace. A big part of how I use Conductor is experimentation. I'm always kicking off workspaces to try different ideas. Most of them don't make it in. So you can see we have four PRs here that are in review. But there's a bunch of random ideas that I've tried here

`[02:12]` **SPEAKER_01:** that are in progress that may never see the light of day. If I like it, then it might get promoted to an internal setting and then an experimental setting. OK, so something I'm very excited about is on the go. I'm going to just speak into my phone and say, let's add a new feature where I can change the theme to hacker mode. And then I'm going to click Conduct. And then my computer starts working on it. And I can conduct on the go.

`[02:39]` **SPEAKER_00:** Do you still write code today?

`[02:41]` **SPEAKER_01:** No. Yeah, no. Very occasionally, I will edit Tailwind classes or open up an IDE to change a .env file. We actually added a mode that we call Caveman mode, which is you click this, and you can actually type with your keyboard and make changes in a file. Once in a while, you do need to make a change to a file by hand, but it's called Caveman mode for a reason. Most of the time, if I want small edits, I'll highlight and then tell the AI about my comments. Or I'll just speak into my computer

`[03:17]` **SPEAKER_01:** and say, that button looks a little too wide. Can you make it smaller? By the way, this thing is now ready to merge. So I just wanted to show you, I can now click Archive. And it's gone from my side panel and merged into the code base. And this one, I can see that there are checks running. And once it's finished, I can just click Merge and get it in. We recently added this thing called, Status, in the left. So when something is kicked off, it's in progress. And then once there's a PR created, it's in review.

`[03:46]` **SPEAKER_01:** And then once it's merged, it goes into the Done folder. We have this new concept of a dashboard page, where from one place, you can see what all your agents are working on, and then take them to the next action. But we're still messing around with what the interface should look and feel like. But the ideal is you should feel like the CEO of a little company. And you can see all your agents working for you. And they'll bring you up digestible reports. And then you can point them in the right direction

`[04:13]` **SPEAKER_01:** if they need some correction, or just merge it in if it looks good.

`[04:17]` **SPEAKER_00:** What are your other main applications, main software that you use?

`[04:22]` **SPEAKER_01:** I use Telegram a decent amount to talk to my open claw. That's been a recent addition for me. I use Spokenly for text-to-speech. That's what comes up when I press Control-Space. It's actually running a local model. It's running Parakeet. I have a really beefed up computer. So it's like 128 gigabytes of RAM. Partly so I can run local models like Parakeet. But as a side note, I have just recently ordered the MacBook Neo, the bottom-of-the-line lowest RAM, lowest memory. I got it basically to force myself to use the lowest spec

`[04:53]` **SPEAKER_01:** option.

`[04:53]` **SPEAKER_00:** Are there any tweaks that you do still stand by that are the customizations that actually do matter?

`[04:58]` **SPEAKER_01:** A couple of things. We put a lot of time into our skills files and our Cloud MD. If I open it up, you can see this is probably a few hundred lines. There's some interesting things in here. We say engineering practices. We're a startup. You're probably used to writing enterprise code. But that's not how we do things around here. And we have a lot of things like that that we've put into our Cloud MD and our skills files over time. What else do I do? I always use Fast Mode. That's not a default.

`[05:27]` **SPEAKER_01:** If you're trying to token max, you have to be in Fast Mode. I do use a Context 7 MCP. I think that's pretty helpful to get documentation. But other than that, I use most of the things out of the box. One core thing is that we always run Cloud and dangerously accept all permissions. That is not the default. And that is the default way to run Cloud in Conductor. I think something that's really important to us is having clear boundaries between what we call them slot-free zones and having parts of the code base

`[05:57]` **SPEAKER_01:** or parts of the documentation that we know is written by a human. It's possible that the AI can contribute to the slot-free zones, but every line has to be read by a human. I think it's actually served us pretty well. Because if you're not careful, the AI can get in a vicious cycle where it sees bad code, and then it writes more bad code as a result. And the same thing can happen in the positive direction. We have some lines in our code base that are like, do not touch if you are an AI. This is for human eyes only.

`[06:32]` **SPEAKER_00:** What's the Conductor tech stack?

`[06:34]` **SPEAKER_01:** It's a Towery app. So it's using the native Safari web renderer. And the backend is technically Rust, but we write almost everything in TypeScript. So it's probably 90%, 95% TypeScript on the desktop app. The web app is Elixir. It's a Phoenix app. It's a very small app, because literally all you can do in it right now is just log in. But I'm a huge Elixir fan, and I am always pushing for more Elixir in our code base when we can. But most of what we're doing is in TypeScript. Another thing we talk about is don't let the AI be

`[07:08]` **SPEAKER_01:** your architect. Even the concept of a workspace here in the sidebar, which in some ways is just an abstraction around a work tree, at least for right now, that's actually going to change soon. But even that concept of a workspace, we as a human had to think that through. The other thing is design and interface decisions. This concept of having all your chats here on the left and then the chat in the middle and then the right sidebar where you can review code changes or run your app, we put a lot of thought into those decisions.

`[07:42]` **SPEAKER_01:** And I think if you let the AI make your UI choices for you, you can end up with something that just doesn't feel crafted. And it's really important to us that it feels crafted. Even this decision, we thought for a long time about how this Open In button should work, which is kind of funny, because now there's so many apps that have this same pattern. The thing that we were really thinking about is whether we should show the icons in the top. I was pretty against showing the icons. I was pretty against showing icons here at first,

`[08:10]` **SPEAKER_01:** because it just feels like, OK, in the top bar of our app, we're advertising a different app. But now I really like it, and it's like a clear visual of what's going to happen when you click it. I think something we would do a bit differently is building the core of the app around human-ridden APIs and contracts that the AI wouldn't contribute to as much. And then I think that it's important to have big chunks of your code base have free reign for the AI, where you can just throw a ton of

`[08:37]` **SPEAKER_01:** different ideas at it and know that it's not going to affect the core infrastructure. And I think right now, the boundaries are a little murky. And that's the thing we're working on improving. I think it's really important to us that we stay a little ahead of the frontier, push people's comfort zones a little bit more than they'd expect. When we first launched Conductor, most of the feedback we got was like, this is crazy. I barely can manage one cloud code or one codex. How am I going to manage three or even five?

`[09:11]` **SPEAKER_01:** We also purposely made it so you can't edit files directly. We made it so that any time a workspace has to be a work tree, and it has to then create a PR, and then you have to merge it. So we really enforced our workflow. I think what's exciting but also hard about where we're at is we have to constantly adapt to where the models are going. So that's one reason we are putting so much work into cloud right now is right now, you're going to shut your laptop, and the agents are going to stop running.

`[09:40]` **SPEAKER_01:** But it feels like we're very quickly moving to a world where the agents are going to run for 10 times longer, and they're going to be 10 times smarter, and they're going to need to run in an environment that isn't constrained by your Mac's CPU.

`[09:52]` **SPEAKER_00:** It seems like you're building Conductor in a very opinionated way. How do you build a conviction behind your decisions?

`[09:57]` **SPEAKER_01:** That's a great question, because especially for our audience, they want a lot of configuration. And I do think it is important for the tool to be flexible and to feel like yours. But the way we build conviction is we force ourselves to use it. Because actually, we don't even force it. Like, we just use it every day. And so if it doesn't feel right, we quickly can decide. But we're not big on analytics or looking at our A-B testing. It's very much a gut feel. This feels right. When I click this, it feels right

`[10:32]` **SPEAKER_01:** that it opens in the center. And that way, I don't need a separate composer. And I can type messages. I can type messages here.

`[10:39]` **SPEAKER_00:** And it all feels unified. You sound like you default to Cloud Code in a lot of places. But Conductor supports Codecs too.

`[10:45]` **SPEAKER_01:** When do you reach for Codecs? I've recently actually been using Codecs more. Codecs is like the workhorse. It will power through a specific problem. Or it's not afraid to do a ton of tool calls and debug something with me for a long time. Cloud, I'll reach for when I want a little more back and forth. I feel like Opus is just a little more creative, like a little more of a partner. I would say when I'm building out a new feature, I probably would instinctively reach for Opus. And then when I'm like, OK, now we just want to get stuff done,

`[11:16]` **SPEAKER_01:** I'll go to Codecs.

`[11:17]` **SPEAKER_00:** Why isn't just a terminal good enough?

`[11:20]` **SPEAKER_01:** There's a reason we moved from terminal interfaces to GUI interfaces in the 80s. I think humans are spatial visual creatures. And having a command line interface just feels very restrictive, and I think it maybe works for the AI brains better than the human brains. But I think just like, I want to know that, OK, my chats are over here, and my review panel is here. I can talk to the AI in the middle. I just think, yeah, bottom line, humans are visual, visual creatures. I also think, zooming in a little bit,

`[11:54]` **SPEAKER_01:** there's a lot that you can't do in a terminal that you can do with a user interface.

`[12:01]` **SPEAKER_00:** Let's talk about token maxing.

`[12:03]` **SPEAKER_01:** Yeah.

`[12:03]` **SPEAKER_00:** What's your high watermark on lines of code in a day or spend in a month?

`[12:07]` **SPEAKER_01:** I think the highest spend was when we were starting out Conductor, like in July 2025. I spent $22,000 on tokens that month. Granted, that was with a previous generation of models. And the lines of code must have been like tens of thousands that month. I'm very big on spending, like on token maxing, like using fast mode, like think extra hard, like high effort all the time. But we're not being on lines of code. We are. We try and keep the lines of code minimal, actually. There's a bunch of reasons for this,

`[12:40]` **SPEAKER_01:** but I think you can quickly spiral. Your code base can spiral out of control if you're not careful about the lines of code added. But I think about it very differently if I'm starting up an app versus working in an established code based like Conductor.

`[12:53]` **SPEAKER_00:** What's different about your workflows today from, say, six months ago?

`[12:57]` **SPEAKER_01:** On a lot of hard PRs, I would open an IDE and make changes by hand. And I also use GitHub, like the web app. It's a lot less now because I can just review the code changes here in Conductor and add comments here if I need to. We do have a lot of PR checks that run. And so that's why we recently added this Checks tab, which lets us just add comments from GitHub into Conductor.

`[13:24]` **SPEAKER_00:** What's the most surprising thing you've seen someone else do with Conductor?

`[13:28]` **SPEAKER_01:** One was someone built a mobile version of Conductor by hacking together a bunch of art. I don't actually even really know how it works, but I know it's spoofing IPC calls to our desktop app, which is pretty interesting. I think, honestly, Gary has shown us a lot of what you can do with Conductor. He is really putting it to the test. I think I've learned from him a bit about how hard you can go on skills. Skills are very much like a first class thing in GStack. And there's some interesting ideas there, I think,

`[14:00]` **SPEAKER_01:** especially around onboarding. And we've added, actually, a specific mode for him called Gary mode, which, by default, does not collapse any of the tool calls. So you can see all the tool calls are default on collapse. And you can even actually see Gary's face here if you're in Gary's mode.

`[14:17]` **SPEAKER_00:** What feels obvious to you and your team that the rest of the world doesn't fully understand yet?

`[14:22]` **SPEAKER_01:** I think there's a lot of cool stuff to explore with collaboration between humans and the AIs. Should you be able to communicate with subagents? Should you be able to have multiplayer chats where multiple people are working on the same thing with the AIs? And then, of course, a metaphor we'll often talk about is feeling like the conductor of an orchestra. You wave the baton, and the instruments are playing in unison. And then once in a while, you want to go to the trumpet player and be like, OK, you're out of tune.

`[14:50]` **SPEAKER_01:** And then you want to zoom out to the string section, and you should play a bit faster. But then most of the time, you're conducting at the orchestra level. Code is almost like sawdust now, in that it used to be that code was the thing you were building. It was the structure. You were putting time into crafting the code. And now, you're putting time into describing what you want and how you want it to be built. And the code is almost just like sawdust that comes out of that process. And that leads to a lot of interesting conclusions.

`[15:23]` **SPEAKER_01:** One of them is really what matters is your prompts. And when the next generation of models come out, you can just rerun your prompts again, and then you'll get new code, and the old code didn't really matter. I think that's one thing that like, the world is slowly waking up to. I think the submit a prompt, like the prompt request feature, is sort of like an early experiment with malleable software. The metaphor that I always think of when I think of malleable software is like video games,

`[15:49]` **SPEAKER_01:** and how when you play Call of Duty, the structure of the game is the same for everyone, and the skeleton is the same. But each person can, I don't know, use custom skins, or faster reload speeds, or whatever. And the same way you can mod a video game, I want you to be able to mod Conductor, and build in your own workflows a little bit. It's important that the structure feels the same, and people want software that's been crafted and been really thought through. But I also, video game mods make the game feel more

`[16:21]` **SPEAKER_01:** like your own. And I think that's going to happen with software as well.
