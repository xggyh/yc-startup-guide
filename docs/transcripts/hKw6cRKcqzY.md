# 全文转录 · 把数据中心送上太空:一家硬科技创业公司的诞生逻辑

> ▶ [YouTube](https://www.youtube.com/watch?v=hKw6cRKcqzY) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/hKw6cRKcqzY.md) &nbsp;·&nbsp; Inside The Startup Launching AI Data Centers Into Space

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_05:** This moment right here could represent the birth of an entirely new industry,

> 此时此刻,可能标志着一个全新行业的诞生,

[00:07] **SPEAKER_01:** data centers in space. The problem is that data centers take up a ton of space and they need a huge amount of energy. Enter StarCloud. This is the beginning of a future where most new data

> 那就是太空数据中心。问题在于,数据中心占用大量空间,而且需要极其庞大的能源。StarCloud 应运而生。这是一个未来的开端——在那个未来里,大多数新建的数据

[00:19] **SPEAKER_05:** centers are being built in space. They're starting small, but the goal is to build massive orbital data centers that will make computing more efficient and less of a burden on the limited

> 中心都将建在太空。他们从小规模起步,但目标是建造巨型轨道数据中心,让计算更高效,同时减轻对地球上有限

[00:29] **SPEAKER_06:** resources down here on Earth. I can see why it seems like a long shot to some people. To me, though, the reason for doing this is that the potential impact is absolutely massive. So even if you think there's a small percentage chance of it working, then it's worth taking this kind

> 资源的负担。我能理解为什么有些人觉得这是天方夜谭。但对我来说,做这件事的理由是,它的潜在影响极其巨大。所以哪怕你认为成功的概率只有很小一点,也值得去冒这样的

[00:42] **SPEAKER_05:** of risk. Philip Johnston and his team at StarCloud recently made aerospace history when they launched a satellite into orbit carrying an NVIDIA H100 GPU. This is the first time anybody's tried

> 险。Philip Johnston 和他在 StarCloud 的团队最近创造了航天史,他们把一颗搭载 NVIDIA H100 GPU 的卫星送入了轨道。这是有史以来第一次有人尝试

[01:03] **SPEAKER_06:** this. This is the first time anybody's tried to launch data center grade terrestrial Earth-based GPUs into space. It's going to be the first of many. While it's

> 这么做。这是第一次有人尝试把数据中心级别的、地面用的 GPU 发射到太空。这会是众多次尝试中的第一次。虽然它

[01:10] **SPEAKER_05:** essentially a prototype, it's still 100 times more powerful than any computer that's ever operated in the vacuum of space. To find out how they went from an idea to launching a demo satellite in less than two years, we visited StarCloud's HQ in Redmond, Washington. Tell us about what StarCloud

> 本质上只是个原型,但它仍比以往任何在太空真空中运行过的计算机强大 100 倍。为了了解他们如何在不到两年的时间里,从一个想法走到发射演示卫星,我们走访了 StarCloud 位于华盛顿州雷德蒙德的总部。请跟我们讲讲 StarCloud

[01:28] **SPEAKER_06:** is working on. We are building data centers in space initially to provide GPU compute to other satellites and then later to compete on energy costs even with terrestrial data centers.

> 在做什么。我们在太空建造数据中心,初期是为其他卫星提供 GPU 算力,之后则要在能源成本上,甚至与地面数据中心一较高下。

[01:38] **SPEAKER_05:** StarCloud's goal is to build the world's first orbital data centers, massive GPU clusters powered by constant solar energy to run AI compute at scale. Operating in a sun-synchronous orbit, they'll draw uninterrupted sunlight for energy, radiate heat into deep space, and run with zero fresh water and much lower carbon emissions than data centers down here on Earth. By taking the cloud off Earth, StarCloud can scale almost indefinitely, free from land, grid, and cooling limitations, and ultimately compete with the cost of the largest terrestrial data centers. Tell us more

> StarCloud 的目标是建造世界上第一批轨道数据中心——由持续不断的太阳能供电的大型 GPU 集群,用于大规模运行 AI 计算。它们运行在太阳同步轨道上,能不间断地获取阳光作为能源,把热量辐射到深空,运行时不消耗任何淡水,碳排放也远低于地球上的数据中心。通过把云从地球搬走,StarCloud 几乎可以无限扩展,摆脱土地、电网和冷却的限制,并最终在成本上与最大的地面数据中心竞争。再多讲讲

[02:15] **SPEAKER_06:** about how far along you are. We started about a year and a half ago. We've designed, built, and tested our first satellite and that will be the first satellite that will have an H100 from NVIDIA on board. The purpose of this is really to prove that our thermal management and radiation shielding techniques allow us to operate the state of the art in space. We're going to be running a whole bunch of data centers on that. We'll be the first to run Gemini from Google on there. We'll be the

> 你们目前的进展。我们大约一年半前起步。我们已经设计、制造并测试了第一颗卫星,它将是第一颗搭载 NVIDIA H100 的卫星。这么做的真正目的,是证明我们的热管理和辐射屏蔽技术,能让我们在太空中运行最先进的设备。我们会在上面运行一大堆数据中心业务。我们会成为第一个在上面运行谷歌 Gemini 的团队。我们也会是

[02:38] **SPEAKER_05:** first to do fine tuning of model and training a model in space. Why data centers in space? It seems like, you know, people are still struggling to get the compute that we need here, building them on Earth. Like, why is space going to be the next frontier for that? Yeah,

> 第一个在太空对模型进行微调、并训练模型的团队。为什么要在太空建数据中心?看起来,大家在地球上建数据中心、想获得所需算力,都还在苦苦挣扎。为什么太空会成为下一个前沿?是的,

[02:51] **SPEAKER_06:** so we see a world where almost all data centers, anything that doesn't require very low latency, is operating in space, surely because of the constraints we're facing on energy terrestrially. And so we're building with a vision to build extremely high-tech data centers, and we're building with a vision to build extremely large, full 40 megawatt data centers. It's about 100 tons. It's what you can fit in one full

> 我们预见的世界是,几乎所有数据中心——凡是不要求极低延迟的——都在太空运行,这必然是因为我们在地面上面临的能源限制。所以我们的愿景是建造极其高科技的数据中心,也要建造极其巨大的、满载 40 兆瓦的数据中心。它大约 100 吨重,正好是一整个

[03:08] **SPEAKER_05:** Starship Halo Bay. And if this works, what does the world look like?

> 星舰货舱能装下的量。如果这成功了,世界会是什么样子?

[03:12] **SPEAKER_06:** It takes a huge burden off the grid on Earth, both the grid and the water supply. The way that data centers on Earth keep cool is essentially they evaporate lots of fresh water. This is actually causing huge problems in certain parts of the U.S., where they're just sucking the rivers and the lakes dry in order to keep these data centers cool. Our data centers in space require zero fresh water. Instead of being this evaporation process, our heat sink is infrared radiation into deep space. And so we're building these very large radiators that we run a fluid through, but doesn't go anywhere. And then that dissipates heat out into the vacuum of space.

> 它会大大减轻地球电网的负担,既包括电网,也包括供水。地球上的数据中心散热,本质上就是蒸发大量淡水。这实际上在美国某些地区造成了巨大问题,那里为了给数据中心降温,几乎把河流和湖泊抽干了。而我们在太空的数据中心不需要任何淡水。我们的散热方式不是蒸发,而是向深空辐射红外线。所以我们在建造这些非常大的散热器,让一种流体在里面循环流动,但流体并不外排,然后热量就被散发到太空的真空中去了。

[03:47] **SPEAKER_05:** What led you to ultimately starting StarCloud and being co-founder here?

> 是什么最终让你创办 StarCloud、成为这里的联合创始人?

[03:51] **SPEAKER_04:** We're seeing an absolute tidal wave of demand for energy, primarily for data centers, but also broadly electrification within our society. And in the Western world, we're not that good at building large infrastructure projects quickly.

> 我们看到能源需求正掀起一股绝对的浪潮,主要来自数据中心,但也来自整个社会广泛的电气化。而在西方世界,我们并不擅长快速建成大型基础设施项目。

[04:04] **SPEAKER_03:** Our vision is to put larger and larger satellites in space and prove that this concept works. We can put essentially high-compute devices in space that are going to help our customers.

> 我们的愿景是把越来越大的卫星送入太空,证明这个概念行得通。我们本质上可以把高算力设备放到太空,去服务我们的客户。

[04:15] **SPEAKER_04:** If it works, when it works, it will have just such a huge impact on the world, on the development of AI, the way we train and use AI. So this is one of the most impactful things I think I could be spending my time on, and that's why we're dedicating so much to it.

> 如果它成功——当它成功时,它将对世界产生巨大的影响,影响 AI 的发展,影响我们训练和使用 AI 的方式。所以这是我认为自己能投入时间去做的、最有影响力的事情之一,这也是我们为它倾注如此之多的原因。

[04:32] **SPEAKER_05:** The vision hasn't convinced everyone. The concept of data centers in space has raised eyebrows and sparked plenty of heated debate online.

> 这个愿景并没有说服所有人。太空数据中心的概念引来了不少侧目,也在网上激起了大量激烈的争论。

[04:40] **SPEAKER_02:** I want you to react to Andrew McCallip's viral post. I was wondering if there were any key points in here that you think were easily debunked.

> 我想请你回应一下 Andrew McCallip 那条爆红的帖子。我想知道,里面有没有哪些关键论点是你认为很容易被驳倒的。

[04:49] **SPEAKER_06:** The criticism usually is, in order to dissipate that heat, you need a large surface area. And they think for some reason that that's super impractical. And my co-founder, Ezra, has a PhD in engineering, spent 10 years designing and building large deployable structures, solar panels. And he said, you know, if you want to build large deployable radiators, you just have to build a large surface area. And that's what we're doing. So half our engineering team is building a very large, low-cost and low-mass deployable radiator. So that is the core IP of our company.

> 这种批评通常是说,要散掉那么多热量,你需要很大的表面积。而他们不知为何认为这极其不切实际。我的联合创始人 Ezra 拥有工程学博士学位,花了 10 年设计和建造大型可展开结构、太阳能电池板。他说,如果你想造出大型可展开的散热器,你只需要造出大面积就行了。这正是我们在做的事。所以我们工程团队有一半人在建造一个非常大、低成本、低质量的可展开散热器。这就是我们公司的核心知识产权。

[05:12] **SPEAKER_05:** Is it fuel for motivation for you now? Oh, 100%. You guys are trying to pull off a very difficult business here, and a very difficult idea that hasn't been done before.

> 这现在成了激励你的动力吗?哦,百分之百。你们在尝试做成一门非常困难的生意,一个前所未有、非常难的想法。

[05:21] **SPEAKER_06:** Yeah, I mean, I have to say I was very inspired by a talk that Sam Altman gave about maybe eight or nine years ago. And he said something like, it's easier to build a hard company than it is to build an easy company. There's one hard thing, which is, can we operate data centers in space cheaply? If we can do that, everything else is easier. Hiring amazing people is easier. Getting people to write about us is easier. Even fundraising is easier. It's an unintuitive fact.

> 是的,我得说,大概八九年前 Sam Altman 的一次演讲给了我很大启发。他说了类似这样的话:创办一家难的公司,比创办一家容易的公司更容易。这里有一件难事,那就是:我们能不能低成本地在太空运营数据中心?如果我们能做到,其他一切都会变得更容易。招募优秀人才更容易,让人们报道我们更容易,甚至融资也更容易。这是一个反直觉的事实。

[05:43] **SPEAKER_05:** Yeah, it seems like you are opting for the path that has very high technical risk, that you can pull this off. But if you can pull it off, people will want it. It'll be incredibly valuable. There's very little market risk. All these other factors kind of go away. Tinian, step back. You have a pretty uncommon background to start a company like StarCloud.

> 是的,看起来你选择的是一条技术风险极高的路——就是你能否把它做成。但如果你能做成,人们就会想要它。它将极其有价值。市场风险很小,其他这些因素基本上都不成问题了。退一步说,Tinian,对于创办 StarCloud 这样一家公司,你的背景相当不寻常。

[06:03] **SPEAKER_06:** Yeah, that's true. So I don't come from a space engineering background. Actually, I started my career as an engineer for the first five years on the software side. And then before that, I studied applied math and theoretical physics, undergrad and master's. And what ignited your passion to start something in space? I've been passionate about space since I was a kid. But I think what made me realize that there is an opportunity here is seeing how quickly the launch cost is coming down.

> 是的,确实如此。我并非出身于航天工程背景。实际上,我职业生涯的头五年是做软件工程师起步的。在那之前,我本科和硕士学的是应用数学和理论物理。是什么点燃了你在太空领域创业的热情?我从小就对太空充满热情。但我认为,真正让我意识到这里存在机会的,是看到发射成本下降得如此之快。

[06:24] **SPEAKER_05:** That's in part thanks to companies like SpaceX and startups like Stokespace that are building reusable rockets.

> 这在一定程度上要归功于像 SpaceX 这样的公司,以及像 Stoke Space 这样正在研制可重复使用火箭的初创企业。

[06:30] **SPEAKER_06:** The launch capacity. The launch capacity might go up by 100 or 1,000x because you can refly these things every day and because they're producing so many of them. And that enables many different business use cases.

> 发射运力。发射运力可能会提升 100 倍甚至 1000 倍,因为你可以每天让这些火箭重复飞行,而且他们在大量生产这些火箭。这就催生出许多不同的商业应用场景。

[06:40] **SPEAKER_05:** And how did you come up with the idea for StarCloud?

> 那你们是怎么想出 StarCloud 这个点子的?

[06:43] **SPEAKER_06:** We were initially looking at space-based solar, which is this concept of very large solar panels in space and beaming the power down. We ran the numbers on that and we wanted to know what is the launch cost where that business model makes sense? The number we came to is around $50 a kilo where that would break even.

> 我们最初研究的是天基太阳能,也就是在太空部署非常大的太阳能电池板、把电能定向传回地面的概念。我们算了一笔账,想知道在什么样的发射成本下,这个商业模式才划得来?我们算出来的数字大约是每公斤 50 美元,在这个价位它才能盈亏平衡。

[06:56] **SPEAKER_05:** That's a long way from where launch costs are today. So they pivoted to a different idea.

> 这跟如今的发射成本还差得很远。于是他们转向了另一个想法。

[07:01] **SPEAKER_06:** The big problem with space-based solar is you lose 95% of the energy transmitting it from space to Earth.

> 天基太阳能的一大问题是,在把能量从太空传回地球的过程中,你会损失 95% 的能量。

[07:06] **SPEAKER_05:** So what if instead of sending the power down to Earth, you sent the data centers up?

> 那么,如果不是把电能送回地球,而是把数据中心送上去呢?

[07:11] **SPEAKER_06:** So after we reran those calculations, we came to a launch cost of $500 a kilo break even. We're much closer to that today than we are to $50 a kilo. So that was then the basis of a white paper.

> 于是我们重新算了一遍,得出的盈亏平衡发射成本是每公斤 500 美元。相比每公斤 50 美元,如今我们离这个数字要近得多。这就成了一份白皮书的基础。

[07:22] **SPEAKER_05:** In the summer of 2024, Philip and his co-founders pitched the idea to YC. They got in on what was their third attempt. Back then, they were called Lumen Orbit.

> 2024 年夏天,Philip 和他的联合创始人向 YC 推介了这个想法。他们是在第三次尝试时才被录取的。当时他们还叫 Lumen Orbit。

[07:31] **SPEAKER_06:** We're building a constellation of orbital data processing satellites to serve other satellites.

> 我们正在建造一个由轨道数据处理卫星组成的星座,用来服务其他卫星。

[07:36] **SPEAKER_05:** What were you focused on primarily during the batch and how did that kind of shape the company?

> 在那一期(YC 训练营)期间,你们主要专注于什么?那又是如何塑造了这家公司的?

[07:40] **SPEAKER_06:** We were applying only for the first part of the business, which is providing cloud services to other satellites. We knew, and actually we had mentioned it in the interview, that there was this much larger potential business model behind it, which is providing energy for almost all data centers. But we hadn't really been vocal about that. And we were kind of maybe even embarrassed to talk about such a grand vision. I think YC just really encouraged us to go for it.

> 我们申请时只提了业务的第一部分,也就是为其他卫星提供云服务。我们知道,而且其实在面试时也提到过,这背后有一个大得多的潜在商业模式,那就是为几乎所有数据中心提供能源。但我们当时并没有真正大声宣扬这一点。我们甚至有点不好意思去谈这么宏大的愿景。我觉得是 YC 真正鼓励我们去放手一搏。

[08:02] **SPEAKER_05:** Why was it embarrassing for you to talk about such a grand vision?

> 为什么谈论这么宏大的愿景会让你觉得不好意思?

[08:05] **SPEAKER_06:** I mean, when you tell people that within 10 years, it could be the case that most new data centers are being built in space, that sounds wacky to a lot of people, but not to YC.

> 我是说,当你告诉别人,10 年之内大多数新建数据中心有可能都建在太空,这在很多人听来很离谱,但对 YC 来说不会。

[08:15] **SPEAKER_05:** In just under two years, they were able to build the first demo satellite, the one that's currently in orbit over our heads right now. It seemed like you all have very complementary backgrounds that are perfect for this type of company.

> 在不到两年的时间里,他们就造出了第一颗演示卫星,也就是此刻正在我们头顶轨道上运行的那颗。看起来你们几位的背景非常互补,特别适合创办这类公司。

[08:28] **SPEAKER_06:** My co-founder, Addy, was 20 years on building data centers with Microsoft. And then he was with SpaceX as a principal software engineer. And so he's doing everything on the software side and with the compute module and making these chips work in a high radiation environment. And then my co-founder, Ezra, who's our CTO, spent a decade designing satellites. He worked on NASA's Lunar Pathfinder mission, did the deployable solar panels. He has a Ph.D. in engineering. And so he is doing all of the satellite structure. So between us, we've got commercial, compute payload, the bit we're doing, and satellite structure. So actually, yeah, the team is extremely well complemented.

> 我的联合创始人 Addy 在微软做了 20 年数据中心。之后他又在 SpaceX 担任首席软件工程师。所以他负责软件这一块的所有工作,包括计算模块,以及让这些芯片在高辐射环境下正常运行。还有我的联合创始人 Ezra,他是我们的 CTO,花了十年设计卫星。他参与过 NASA 的月球探路者(Lunar Pathfinder)任务,做的是可展开太阳能电池板。他拥有工程学博士学位,所以他负责整个卫星结构。所以在我们之间,商务、计算载荷(我负责的这块)和卫星结构都覆盖到了。所以实际上,是的,这个团队互补得极好。

[09:02] **SPEAKER_06:** We are headed into the main building. The main assembly facility that we have, this is where we're extending our deployables and iterating on different prototypes. This is where the engineering team sits. This is electrical and software and the mechanical engineers back here. This is the cleaner area of the two. If that was the clean side, then this is what you can think of as the dirty side, where we're fabricating all sorts of aluminum parts for the spacecraft. And so you're building a lot of the parts

> 我们正走进主楼。这是我们的主装配厂,我们在这里展开可展开结构,并对不同的原型进行迭代。这里是工程团队办公的地方。这边是电气和软件工程师,后面这里是机械工程师。这是两块区域中比较干净的一块。如果那边算是洁净区,那么这边你可以理解为"脏"区,我们在这里加工航天器用的各种铝制零件。所以你们很多零件

[09:28] **SPEAKER_05:** and assembling things right here in this facility.

> 都是在这个厂房里制造和组装的。

[09:30] **SPEAKER_06:** Exactly. So we're building all of the payload, all of the power, and then all of the thermal dissipation. Here we have the vibration table, which Ezra is setting up for a vibration test of some of the electrical hardware. So this is where we shake the satellite in all different directions, every axis and then into every different frequency, amplitude, et cetera.

> 没错。我们制造全部的载荷、全部的电源系统,以及全部的散热系统。这里是振动台,Ezra 正在为一些电气硬件的振动测试做准备。我们就是在这里从各个方向摇晃卫星,覆盖每一个轴向,以及各种不同的频率、振幅等等。

[09:46] **SPEAKER_06:** I think before us, it's been four years for any previous startup to go from day one founding to having something on orbit. 15 months, we went from founding to having the satellite design built, ready and tested. How are you able to do that so quickly? This is where I give credit to my co-founders. All of the compute module and antennas and everything, everything else they built in-house by hand. We were working through the night up until the day that we shipped down the payload.

> 我觉得在我们之前,任何一家初创公司从成立第一天到把东西送上轨道,都要花四年时间。而我们只用 15 个月,就从成立走到了卫星设计完成、造好、准备就绪并通过测试。你们怎么能做到这么快?这就要归功于我的联合创始人了。所有的计算模块、天线以及其他一切,他们都在公司内部亲手打造。我们一直通宵工作,直到把载荷交付发运的那一天。

[10:12] **SPEAKER_06:** So the first satellite is a small set. It's about 60 kilograms, the size of a small fridge. And on that, we have been responsible for the compute module and the antennas. We've contracted one of the bus manufacturers, a company called Astro Digital, to build the bus. And so, yeah, there's the high-powered GPUs. That's the H100 that we've got from NVIDIA on there. There's a bunch of different antennas that we're testing and using on that one.

> 第一颗卫星是个小家伙,大约 60 公斤,只有一台小冰箱那么大。在这颗卫星上,我们负责计算模块和天线。我们委托了一家卫星平台制造商——一家叫 Astro Digital 的公司来制造卫星平台。所以,是的,这上面有高性能 GPU,就是我们从 NVIDIA 拿到的那颗 H100。上面还有一堆不同的天线,我们在这颗卫星上测试并使用它们。

[10:34] **SPEAKER_05:** All of this led up to the historic launch on November 2nd.

> 这一切都指向了 11 月 2 日那次历史性的发射。

[10:38] **SPEAKER_00:** Good evening and welcome to SpaceX's live coverage of our fourth bandwagon rideshare mission. Onboard are StarCloud's StarCloud One, which is looking to prove that modern data center hardware can run in orbit, starting with the world's first NVIDIA H100 GPU deployed in space. All systems are go for an on-time liftoff.

> 晚上好,欢迎收看 SpaceX 对我们第四次 Bandwagon 拼车任务的现场直播。此次搭载的有 StarCloud 的 StarCloud One,它旨在证明现代数据中心硬件能够在轨道上运行,首先要实现的就是全球第一颗部署在太空的 NVIDIA H100 GPU。所有系统状态良好,准点升空。

[10:57] **SPEAKER_01:** Launch director, go for launch.

> 发射指挥,可以发射。

[11:00] **SPEAKER_02:** Three, two, one, engines for power. And liftoff. Go bandwagon. Go ADD 425.

> 三,二,一,发动机全功率。点火升空。Bandwagon 出发。ADD 425 出发。

[11:23] **SPEAKER_06:** Over the next few months, we'll be doing all this whole battery of tests we've got lined up. So training the first model in space, running high-powered inference in space, running a version of Gemini. We'll be doing a whole bunch of interesting firsts over the next few months.

> 在接下来的几个月里,我们将进行一整套已经排好的测试。比如在太空训练第一个模型、在太空运行高性能推理、运行一个版本的 Gemini。未来几个月,我们会创造一大堆有趣的"首次"。

[11:35] **SPEAKER_05:** Say more about your second launch, which you already have planned. What's going to go up there and how is that going to be different from the first one?

> 再多讲讲你们已经规划好的第二次发射吧。这次会送什么上去,又会和第一次有什么不同?

[11:41] **SPEAKER_06:** So the second one is launching in October next year. That's going to be at least 10 times more powerful than the first satellite and that will fly the Blackwell architecture from NVIDIA. It will have a whole bunch more GPUs. So that one will be much more capable. It will also have very high bandwidth connectivity through optical terminals. And so we'll have 24-7 high bandwidth connectivity with very low latency all the time. And then that's a huge differentiator.

> 第二颗将在明年 10 月发射。它的算力至少是第一颗卫星的 10 倍,并将搭载 NVIDIA 的 Blackwell 架构。它会有多得多的 GPU,所以能力会强得多。它还将通过光学终端实现极高带宽的连接。这样我们就能全天候拥有始终保持极低延迟的高带宽连接。这将是一个巨大的差异化优势。

[12:04] **SPEAKER_05:** While we may be a decade plus away from their grand vision of massive five gigawatt data centers in orbit, they've taken a critical first step. And they're not alone anymore.

> 尽管距离他们那个宏大愿景——在轨道上部署 5 吉瓦的巨型数据中心——可能还有十多年,但他们已经迈出了关键的第一步。而且他们不再是孤军奋战了。

[12:14] **SPEAKER_01:** A lot of the big tech giants are now starting to go into space. They're now starting to look up way above us. Google, SpaceX, Amazon, they are all exploring data centers in orbit, powered by the sun's rays and cooled by the vacuum of space.

> 许多科技巨头如今也开始进军太空。他们开始把目光投向我们头顶的高空。谷歌、SpaceX、亚马逊,都在探索轨道数据中心——由太阳光供电,靠太空的真空冷却。

[12:26] **SPEAKER_06:** Anything that's worth doing is going to be hard. And, you know, if something is too easy, it probably doesn't have the same potential outcome. And so we decided to do the biggest, most ambitious thing we could, and that's build almost all data centers in space.

> 任何值得做的事都会很难。你知道,如果一件事太容易,它大概就不会有同样量级的潜在回报。所以我们决定去做我们所能做到的最宏大、最有雄心的事,那就是把几乎所有的数据中心都建到太空去。
