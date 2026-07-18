# 脑机接口的未来 / The Future Of Brain-Computer Interfaces

> **来源**: [The Future Of Brain-Computer Interfaces](https://www.youtube.com/watch?v=5gspRJVp9dI) · Y Combinator · 2026-03-09 · 时长 53:20
> **讲者**: Max Hodak(Neuralink 联合创始人、Science 创始人,受访嘉宾) × Garry Tan(YC CEO,《How to Build the Future》主持人)
> **一句话定位**: 一位从纯软件工程师转型硬科技、做出"让盲人重见"视网膜芯片的连续创始人,讲他如何用第一性原理选赛道、把"大脑当计算机"来做 API,以及创业最该学会的元技能——这些"选楔子、找缺口、抄别人的红利、拜师而非单打"的方法论,对 AI Agent 创始人几乎条条可迁移;同时点破 AI 与神经科学正在大统一(潜空间、表征),对做 Agent 的技术人是极强的世界观校准。

## 🎯 TL;DR(中文核心要点)
- **BCI 不是一个产品,而是一个像"制药"的品类**:不会有"那款大家都装的脑机接口",而是一堆公司针对不同应用、用不同探针去做。对 Agent 创始人的映射:别做"通用 Agent 平台",按具体应用切,不同场景配不同"探针"。
- **永远从风险-收益最不对称的地方切入**:Max 从最重度失能的盲人患者做起——哪怕只恢复很基础的功能,收益/风险比也极高。健康人不会为 10 bit/s 的运动解码去做开颅手术(键盘鼠标快得多)。找那些"现状烂到用户愿意忍受你早期粗糙方案"的人群。
- **"技术早就可行、却没人经济地部署"的缺口,就是创业本身**:Vessel 项目源于他读到一个靠 ECMO 续命、却因每月 50 万美元被踢出移植名单的少年——技术能救、系统不做。发现这种缺口并把它工程化(比如"让一颗肾脏能当行李托运上飞机"),正是创始人该干的事。
- **用第一性原理,但在复杂系统里"第一性原理不够"**:生物里还必须搞清"进化到底做了什么"。Science 没有像多数生物医疗公司那样围绕一个专利/资产成立,而是把"该刺激哪层细胞 × 用电还是光遗传"四个象限全跑一遍,靠实证找到答案。
- **大脑就是一台计算机,它有明确的 API**:所有进出信息只走 12 对脑神经 + 31 对脊神经,"现实不过是这些神经上的脉冲"。做 BCI 的本质是拿到这个 API 并翻译潜空间——这和你训练/接入模型时思考输入-信号-表征的方式高度同构。
- **AI 与神经科学正在大统一,而且是 AI 在教神经科学**:图像/语言模型内部的表征"看起来很像大脑里的表征";大脑深处就是一个个"潜空间"(物体图谱、人脸图谱)。别信"随机鹦鹉/高级自动补全"那套贬低。
- **会抄别人的红利("智能手机红利")**:Neuralink 能把电子器件做到可全植入、封住皮肤,靠的是苹果三星砸巨资把低功耗小型电子做出来——"BCI 自己做不到"。做 Agent 同理:白嫖基础模型、推理硬件、工具生态的行业红利。
- **创业是"口口相传的手艺",要拜师而非单打**:Max 最大的教训是没早点去给 Elon 这样的人打工——"这会极大提升你的能力、让你懂游戏怎么玩"。20 岁进对文化,和 26/28 岁才进,轨迹天差地别。先想清"你到底想要什么",再高能动性地扑上去。

## 🧭 适合谁 / 什么时候看
- 你是软件/AI 背景,想切入更"硬"、更有护城河的方向,纠结"我是不是只能做 B2B SaaS"。
- 你在给 Agent 选赛道/选第一个产品,需要一套"如何用风险-收益和第一性原理选楔子"的思考框架。
- 你想校准 AI 世界观:想搞清"表征/潜空间"这些概念在生物大脑里的对应,以及为什么 Max 认为 AI"还没被 price in"。
- 你在纠结要不要先给牛人打工、还是直接自己干——这集有一段非常直接的过来人建议。

## 📝 分段精读

### 1. 视网膜芯片、BCI 到底是什么、以及"BCI 是一个品类不是产品" / What BCIs really are & why it's a category, not a product `[00:26–05:44]`
**要点(中文)**: Science 的 Prima 是一枚 2mm×2mm 硅片,植入视网膜下方,像一小片"太阳能板";患者戴的眼镜用摄像头看世界、激光把图像投进眼底,芯片吸光后直接激发上方细胞,绕过坏死的视杆视锥。40+ 患者已在欧洲 17 个中心的临床试验中受益,正在申请上市。Max 强调 BCI 的本质:大脑是台强大计算机但"被封在颅骨里、并非神奇地连着外界",只有少数几条通道(感官/运动)。因此 BCI 会像制药一样是**一个品类**,不同模态服务不同应用。选人群要看**风险-收益**:从最重度失能者做起,因为哪怕基础功能对他们收益也极高;而健康人不会为 10 bit/s 的运动解码去挨开颅刀。
> 🗣️ "the brain is this powerful computer, but it's encased in the skull. Like, it is not magically connected to things." —— Max Hodak
> 译:大脑是这么一台强大的计算机,但它被封在颅骨里。它并不是神奇地就连着外界万物。
> 🗣️ "it really is going to be a category like pharma." —— Max Hodak
> 译:它真的会成为一个像制药那样的品类(而不是单一产品)。
> 🗣️ "You always look at risk reward. You start at the most disabled patients who get the most benefit for even relatively basic functionality." —— Max Hodak
> 译:你永远要看风险-收益。你从最重度失能的患者做起,他们哪怕只拿到相对基础的功能,收益也最大。

### 2. 大脑的可塑性:两个能互相学习的系统 & 植入后"看见"是什么感受 / Plasticity, two learning systems, and what sight feels like `[05:44–13:01]`
**要点(中文)**: 早期发育有真正的"关键期"(先天性白内障拖到成年再修,很多人无法处理涌入的信息,甚至有人自杀);但成年后大脑"比普遍认为的可塑得多"。惊人的实验:在皮层几乎任意位置放电极、给患者一个"随该神经元放电强度闪烁"的反馈灯,几分钟内他就能学会控制那个神经元。最早的运动解码甚至不拟合任何东西——**固定权重,让大脑自己去学**。于是形成"两个能互相学习的系统"(而非一个固定、一个可塑)。你体验到的世界其实是大脑"编造"的世界模型;失明期大脑因缺输入而"调高增益",刚开机时患者会分不清真实光点和幻觉,需要康复训练去区分。
> 🗣️ "the brain stays way more plastic throughout life and adulthood than I think is widely appreciated." —— Max Hodak
> 译:大脑在人的一生和成年期都比人们普遍认为的要可塑得多。
> 🗣️ "They fixed the weights and let the brain figure it out, let the brain learn." —— Max Hodak
> 译:他们固定住权重,让大脑自己去搞明白、让大脑去学。
> 🗣️ "you're not experiencing directly, you're experiencing a world model like fabricated by your brain." —— Max Hodak
> 译:你并不是在直接体验世界,你体验的是一个由你大脑编造出来的世界模型。

### 3. 药物发现 vs 神经工程:重构医学、选对第一个产品 / Drug discovery vs neural engineering: reframing medicine & picking the wedge `[13:01–17:55]`
**要点(中文)**: Max 的核心世界观:医学有两条路——"药物发现"和"神经工程"。人类其实很不擅长药物发现(偶尔撞上 GLP-1 就惊艳,但更常见的是花十年走进死胡同);已投入巨资找药去阻止/逆转失明,基本无效;有百万美元/患者的基因疗法收效甚微。而 Science 的视网膜假体能让"十年看不见人脸"的患者读出视力表上每个字母。结论:大脑不仅是最要紧的器官,人类还**在工程改造它上更擅长**——这是对医学的根本重构。选第一个产品的逻辑:视网膜假体是巨大未满足需求、且当时技术已就绪、又离他过往工作足够远值得探索。
> 🗣️ "not only is the brain the only organ that really in some deep sense matters, we are also just empirically much better at engineering it." —— Max Hodak
> 译:大脑不仅是那个在某种深层意义上唯一真正要紧的器官,而且从经验上看,我们对它做工程改造还要在行得多。
> 🗣️ "we can take a patient who's been unable to see faces for a decade and allow them to read every letter on an eye chart." —— Max Hodak
> 译:我们能让一个十年都看不清人脸的患者,读出视力表上的每一个字母。

### 4. 大脑就是一台计算机:API、湿件、逆向工程 / The brain is a computer: its API, wetware & reverse engineering `[17:55–24:59]`
**要点(中文)**: 一句会"被业内某个角落骂"但可以"几乎照字面理解"的话:大脑是台计算机,只是架构不同于冯诺依曼。所有进出信息只通过 12 对脑神经 + 31 对脊神经——"这就是大脑的 API";"现实不过是脑/脊神经上的那些脉冲"。BCI 研发的瓶颈不是神经科学(一旦能记录信号,表征很快就搞明白),而是**记录与刺激信号的能力**。Second Sight 的教训:他们刺激已被 100 倍压缩的神经节细胞,只能得到杂乱闪光;Science 刺激压缩前的双极细胞,才拿到成像。方法论上,他们不像多数生物医疗公司围绕单一资产成立,而是用第一性原理把"双极/神经节 × 电/光遗传"四象限全跑一遍——但要记住"生物里第一性原理不够,还得懂进化做了什么"。
> 🗣️ "you can think of that as like the API of the brain... reality is whatever spikes are on the cranial and spinal nerves." —— Max Hodak
> 译:你可以把它看成大脑的 API……现实不过就是脑神经和脊神经上那些脉冲罢了。
> 🗣️ "you have to be careful with first principles in biology, because first principles are not enough." —— Max Hodak
> 译:在生物学里用第一性原理要小心,因为光靠第一性原理是不够的。
> 🗣️ "we just went and explored all four quadrants of that." —— Max Hodak
> 译:我们就直接把那(四个象限)全都探索了一遍。

### 5. 从软件到硬科技的创始人之路 & Neuralink 如何启动 / From software to hard tech & how Neuralink actually started `[24:59–33:10]`
**要点(中文)**: Max 最深的硬技能是软件(从小编程),但一直痴迷大脑,被《黑客帝国》深刻影响——"如果能造出以假乱真的模拟世界,那真正要紧的就是大脑"。Neuralink 的起点:2016 年初 Sam(Altman)一封主题为"疯狂问题"的邮件——Elon 要开脑机接口公司,谁来管?他先推荐了 MIT 的朋友,一小时后回过神来毛遂自荐。2016 下半年一群人每周聚一次,滚成 Neuralink,最终共识落在薄膜聚合物电极丝上。Elon 的真实动机不是产品,而是"AI 来了,人类不能被甩下、必须以某种方式融合"——他比多数人更早更清楚地看到这点。方法:"聚起你能找到的最聪明的一群人 + 足够资源,去做任何合理的事"。
> 🗣️ "if you could simulate a world... the thing that matters is the brain. And if you can engineer the brain and support the brain, then kind of all the rest of it is replaceable." —— Max Hodak
> 译:如果你能模拟出一个(以假乱真的)世界……那真正要紧的东西就是大脑。而只要你能对大脑做工程、能支撑住大脑,其余的一切都是可替换的。
> 🗣️ "we keep our closest living relatives in glass boxes so they don't go extinct." —— Max Hodak
> 译:我们把与我们血缘最近的物种关进玻璃箱里、免得它们灭绝。(Max 借此说明:更高的智能在历史上一向危险,人类不能被 AI 甩下。)

### 6. 大脑如何表征信息:潜空间、AI↔神经科学的大统一、智能手机红利 / How the brain represents info: latent spaces & the smartphone dividend `[33:10–39:47]`
**要点(中文)**: 理解大脑的关键词是"表征(representation)"。靠近输入/输出处(初级运动皮层离肌肉常只隔两个突触)的表征很"具体",直接对应关节力矩等我们易懂的量;越往深处越抽象——下颞叶皮层里有一整张"物体图谱""人脸图谱",在这个流形上移动就得到任意物体的知觉,**这就是一个潜空间**。而重磅事实:训练图像/语言模型时,模型内部的表征"看起来很像大脑里的表征"——十年前大家以为是 AI 向神经科学学,结果反过来了。Max 直言"随机鹦鹉/高级自动补全"那套是"不懂装懂"。他甚至常拿 LLM"沿突触在大脑里走一步步问下一层连到哪些细胞"。工程侧的关键杠杆是"智能手机红利":苹果三星砸钱造出的低功耗小电子,让 Neuralink 能全植入、封住皮肤——"BCI 自己做不到"。
> 🗣️ "the representations that you get inside them look a lot like the representations you see in the brain." —— Max Hodak
> 译:你在这些(AI)模型内部得到的表征,看起来非常像你在大脑里看到的那些表征。
> 🗣️ "there's like stochastic parrots or glorified autocompletes... these people just don't know what they're talking about." —— Max Hodak
> 译:什么"随机鹦鹉""高级自动补全"……这些人根本不知道自己在说什么。
> 🗣️ "what we call the smartphone dividend... BCI couldn't have done this on its own, but Apple and Samsung and others have poured epic amounts of money onto making these types of electronics exist." —— Max Hodak
> 译:我们管它叫"智能手机红利"。BCI 靠自己是做不到的,但苹果、三星等公司砸了天量的钱,才让这类电子器件存在于世。

### 7. Bio-hybrid 与 Vessel:发现"技术可行却没人做"的市场缺口 / Bio-hybrid & Vessel: the gap between possible and deployed `[39:47–44:32]`
**要点(中文)**: Science 有三条线:视网膜(Prima)、神经接口、灌注(Vessel)。Bio-hybrid 的思路是"向进化学习":大脑两半球靠 2 亿纤维的胼胝体连成"一个整合的当下";若要造超高带宽的脑对脑连接,自然会长出"一根带 USB 口的新神经"。于是他们用被"隐身"于免疫系统的低免疫原性干细胞衍生神经元,种在器件上、贴到脑表面自行长出生物连接——不插线、不改造你自己的大脑(避免基因疗法那种"单向门"的风险)。Vessel 的由来更是创业范本:他读到一个靠 ECMO 续命、却因每月 50 万美元 ICU 成本和"通往无处的桥"伦理争议被踢出移植名单的少年,发现**"技术上明明可行、却因某种原因无法经济地部署"之间存在巨大鸿沟**——而弥合这道鸿沟正是创始人该做的事(比如把 50 万美元、只能私人飞机运的灌注系统,做到"一颗肾脏能当行李托运上联航班机")。
> 🗣️ "there seemed to be this big gap between what was technically possible. And what was, was economic to deploy for some reason." —— Max Hodak
> 译:在"技术上可行"和"出于某种原因能经济地部署"之间,似乎横着一道巨大的鸿沟。
> 🗣️ "what if you could refine this to the point where you could check a kidney as luggage on a United flight to the East coast?" —— Max Hodak
> 译:如果你能把这套技术打磨到——一颗肾脏可以当行李托运、坐联航的航班飞到东海岸——那会怎样?

### 8. 组建 Science、"创业是口口相传的手艺" & 未来展望 / Building Science, the oral tradition & the future `[44:32–53:20]`
**要点(中文)**: 给 2016 年的自己两条建议——一条是他做对了的、一条是他没做的。做对的:**先想清楚你到底想要什么,然后高能动性地扑上去**(大学时为进杜克那个不收本科生的灵长类神经实验室,靠在化学系选独立研究"走后门"混进去)。没做的:**该更早去给 Elon 这样的人打工**。因为"创业是一门口口相传的手艺"——除了 PayPal 那种极少数从零悟出来的,绝大多数是从少数硅谷文化里一代代传下来的;拜对师能极大改变你的职业轨迹。他 2012–2016 做 Transcriptic(机器人云实验室)那段,"强烈认同 Ben Horowitz 那篇《The Struggle》",是纯粹的 hard mode。展望:他有个"2035 事件视界",五年后看不清;认为"活到一千岁的第一批人可能现在就活着";AI"是真的、却还没被 price in、人们仍然低估它";智能将对"有能动性去部署它的人"广泛可得;BCI 与 AI 是两条平行但截然不同的故事线,而"脑机接口在很多情况下等价于脑对脑接口"。
> 🗣️ "running a startup is an oral tradition... the thing that I should have done earlier is go work for somebody like Elon, because that's just like so dramatically leveled up like my ability to do this and know how the game is played." —— Max Hodak
> 译:创业是一门口口相传的手艺……我本该更早去做的一件事,就是去给 Elon 那样的人打工,因为那会极大地提升我做这件事的能力、让我懂得这个游戏是怎么玩的。
> 🗣️ "the first is like figure out what you want." —— Max Hodak
> 译:第一件事,是搞清楚你到底想要什么。
> 🗣️ "artificial intelligence is real, it is still not priced in, people still don't appreciate it... intelligence is going to become widely available for those that have the agency to deploy it." —— Max Hodak
> 译:人工智能是真实的,它仍然没有被(市场)定价进去,人们依然低估它……智能将会对那些有能动性去部署它的人变得广泛可得。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把"BCI 是品类不是产品"套到你身上**:别做"通用 Agent 平台",挑一个具体应用切入;不同场景配不同"探针"(工具/模型/上下文),别指望一个万能形态。
- [ ] **用风险-收益选第一批用户**:找"现状烂到愿意忍受你早期粗糙方案"的人群——他们对基础功能的收益/风险比最高;别一上来就想服务"键盘鼠标已经够用"的高性能用户。
- [ ] **主动去找"技术已可行、却没人经济地部署"的缺口**:像 Max 读 PubMed / Lancet 那样,系统性地翻行业里"明明能做却没人做"的痛点,那就是你的机会。
- [ ] **第一性原理 + 领域实证并用**:在 AI 里"第一性原理不够",还要搞清楚"这个行业/这套数据实际长什么样";必要时把关键设计的几个象限全跑一遍(A/B/评测),用实证而非直觉定方案。
- [ ] **主动薅"智能手机红利"式的行业红利**:白嫖基础模型、推理硬件、开源工具与 Agent 生态的巨额投入——你自己造不出来的能力,让别人的巨资替你造。
- [ ] **拜师而非单打**:如果你还年轻,认真考虑先去一家"会打仗"的团队/牛人手下待一两年,把创业这门"口传手艺"学到手,再自己干——先想清"你到底想要什么"。

## 🔑 关键术语 / 概念
- **BCI(Brain-Computer Interface,脑机接口)** — 在大脑与外部设备间建立信息通道的技术;Max 认为它会像制药一样是一个"品类",而非单一产品。
- **Prima(视网膜假体)** — Science 的 2mm×2mm 视网膜下芯片,像太阳能板,靠眼镜投射的激光供能并刺激双极细胞,绕过坏死的视杆视锥恢复"形觉视觉"。
- **Representation / Latent space(表征 / 潜空间)** — 大脑用神经元活动"编码"世界的方式;越深处越抽象(如下颞叶的"物体图谱/人脸图谱")。Max 指出 AI 模型内部表征与大脑表征高度相似。
- **神经工程 vs 药物发现(Neural engineering vs drug discovery)** — 两条医学路线;Max 主张前者更可控:与其搞清分子层面哪里坏了,不如直接把信号工程性地送回系统。
- **Bio-hybrid neural interface(生物混合神经接口)** — 用低免疫原性干细胞衍生神经元种在器件上、贴脑自行长出生物连接,像"长出一根带 USB 口的新脑神经"(他用《阿凡达》的辫子接口打比方)。
- **Neuroplasticity(神经可塑性)** — 大脑在反馈下重连的能力;成年后仍远比普遍认为的强,是"两个学习系统互学"的基础;但早期发育存在不可逆的"关键期"。
- **Smartphone dividend(智能手机红利)** — 手机产业砸巨资造出的低功耗小型电子,被 BCI"白嫖"用于全植入器件;泛指借用其他行业巨额投入的红利。
- **The API of the brain(大脑的 API)** — 12 对脑神经 + 31 对脊神经构成大脑与外界的全部信息接口;"现实不过是这些神经上的脉冲"。
- **ECMO / 灌注(Perfusion)** — 体外膜肺氧合等"心肺机";Vessel 项目要把昂贵笨重的灌注系统工程化到可普及。
- **The Struggle(《挣扎》)** — Ben Horowitz 的著名文章,描述创业至暗时刻;Max 说 2012–2016 那段强烈认同它。

## 🔖 高价值金句时间戳
- `[03:51]` "it really is going to be a category like pharma." — 别做"那一款通用 Agent",按应用切品类。
- `[04:35]` "You always look at risk reward. You start at the most disabled patients." — 选第一批用户的黄金法则:从风险-收益最不对称处切入。
- `[18:43]` "reality is whatever spikes are on the cranial and spinal nerves." — 把大脑当有明确 API 的计算机,是整套方法论的地基。
- `[22:24]` "you have to be careful with first principles in biology, because first principles are not enough." — 第一性原理要配领域实证,AI 里同理。
- `[36:32]` "the representations that you get inside them look a lot like the representations you see in the brain." — AI 与神经科学正在潜空间层面大统一。
- `[38:22]` "what we call the smartphone dividend... Apple and Samsung and others have poured epic amounts of money." — 学会薅别的行业砸出来的红利。
- `[41:09]` "there seemed to be this big gap between what was technically possible. And what was, was economic to deploy for some reason." — "技术可行却没人做"的缺口就是创业本身。
- `[49:59]` "running a startup is an oral tradition." — 创业是口传手艺,拜师胜过单打。
- `[52:09]` "artificial intelligence is real, it is still not priced in, people still don't appreciate it." — 对 Agent 创始人最提气的一句世界观校准。
