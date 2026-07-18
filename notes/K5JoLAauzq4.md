# 我们如何重做官网:用"讲故事"代替"卖产品",用 AI 直接做交互原型 / How We Redesigned Our Website

> **来源**: [How We Redesigned Our Website](https://www.youtube.com/watch?v=K5JoLAauzq4) · Y Combinator · 2026-01-30 · 时长 18:40
> **讲者**: Aaron Epstein(YC General Partner,主持,SPEAKER_01)与 Eve Bouffard(YC 产品设计师,SPEAKER_02);另有一段官方申请广告口播(SPEAKER_00)
> **一句话定位**: 一期"设计复盘"节目,拆解 YC 官网从"B2B SaaS 模板式推销页"改成"以创始人故事激发梦想"的落地页的全过程——对要给 AI Agent 产品做官网/落地页、并想用 Opus 4.5 + Cursor 把设计当协作者来做交互原型的创始人极其对症。

## 🎯 TL;DR(中文核心要点)
- **激发梦想,而不是推销产品(inspire, don't sell)**:旧站是"利落但无灵魂"的 B2B SaaS 模板(hero 图 + 一堆 CTA + logo 墙);新站的目标改成"让访客看到后觉得'这也可能是我'",这是整次改版的北极星。
- **把主角从品牌换成用户**:旧站只堆公司 logo,新站放创始人本人的脸和"当年 vs 现在"的对比,弱化"YC 有多牛",强化"这些人当年和你在同一起点"。
- **别自夸,让用户替你说话**:关于"YC 体验有多好"的描述,全部改用真实创始人访谈的原声拼接,而不是自己写文案——来自用户的话可信度远高于自我表扬。
- **文案能留就留、别为改而改**:官网核心介绍段直接沿用 PG 15 年前写的原文,只更新"一年四批""在旧金山"等事实细节——好文案有长期价值。
- **极简是为叙事服务**:去掉边框、硬分割线、多余动效和"到处塞 apply 按钮"的冲动;这不是要把转化率提 0.1% 的 SaaS,加按钮反而稀释故事。
- **动效不为炫技,只为传达**:每个 section 都问"最能表达这段信息的交互版本是什么",用动画呈现"during YC → now"的转变,而非为动而动。
- **用 AI 当设计协作者,别在 Figma 里死磕**:画了几帧就觉得受限,于是直接开新 repo,用 Opus 4.5 + Cursor 在真实页面上做原型;prompt 常常就是"这些信息,创意地展示出来",再从产出里挑"有价值的种子"迭代。
- **在活页面上迭代交互,是最终效果的关键**:很多最终方案(如轮播、对比动画)在 Figma 等静态工具里根本想不出来,是"边做边看 before/after"才逼出来的。

## 🧭 适合谁 / 什么时候看
- 要给 AI Agent / SaaS 产品做**官网首页或落地页**、纠结"该讲功能还是讲故事"的创始人。
- 想把 **AI 编码工具(Opus 4.5 + Cursor)当设计协作者**、跳过大量 Figma 静态稿、直接做可交互原型的独立开发者/小团队。
- 正在写**首页文案与信任背书**、想知道如何用真实用户原声替代自夸的营销/增长负责人。
- 时长仅 18 分钟,适合动手改版前当"设计哲学 + 工作流"速览。

## 📝 分段精读

### 1. 背景与旧版诊断:一个"利落但无灵魂"的 SaaS 模板 / Setup & Diagnosing the Old Homepage `[00:00–02:30]`
**要点(中文)**: 这是一期特别版 Design Review,两人先对旧 YC 首页做"设计复盘"。旧站约在 COVID 时期(4–5 年前)做成,是典型的 B2B SaaS 模板:hero 配图、一堆 CTA、左文右图、几组数据、一排 logo。Eve 的核心批评是:YC 是极特别的品牌,本可以做到"鼓舞人心、讲故事",但旧站完全没做到。
> 🗣️ "it is a very utilitarian website. It feels a little bit like a B2B SaaS template with some call to actions, some picture in the hero section, and then some text on the left and then some stats, and then some logos." —— Eve Bouffard
> 译:它是个非常"实用主义"的网站,感觉有点像带一堆行动号召按钮的 B2B SaaS 模板——hero 区一张图、左边一段文字、几个数据、再来一排 logo。
> 🗣️ "YC is such a truly special brand where we can do so much more in being inspiring and telling a story, and this was not really doing it." —— Eve Bouffard
> 译:YC 是个如此特别的品牌,我们本可以在"鼓舞人、讲故事"上做得多得多,而旧站根本没做到这点。

### 2. 把叙事重心放到创始人身上 / Centering the Story on Founders `[02:30–04:00]`
**要点(中文)**: Aaron 逐条批旧站的空洞文案:标题"top YC companies"什么信息都没传达,该直接说"有几十家十亿美金公司诞生于 YC";"我们帮创始人做人们想要的东西,结果不言自明"——那结果到底是什么?没量化。还有"我们把创始人利益放第一",底下却全是"我们不做什么"(不占董事席、不拖几个月、不要 deck),而不是正面表达。核心问题:该说清楚的都没说清楚,该量化的都没量化。
> 🗣️ "We help founders make something people want and the results speak for themselves. And it's like, well, what are the results?" —— Aaron Epstein
> 译:(旧站写)"我们帮创始人做出人们想要的东西,结果不言自明"——可问题是,结果到底是什么?
> 🗣️ "We put founders interests first, which I think is actually a really important message. But everything underneath it is all these things that we don't do." —— Aaron Epstein
> 译:"把创始人利益放第一"其实是个很重要的信息,但它底下写的全是"我们不做哪些事",而不是正面把价值讲出来。

### 3. 新愿景:激发梦想,而不是推销 / The New Vision: Inspire, Don't Sell `[04:00–05:30]`
**要点(中文)**: 改版的核心定位——不"卖项目、卖产品",而是"让你做梦(make you dream)"。团队回到 YC 根源,精读 PG 的 essay,提炼出反复出现的关键词 **formidable**(令人生畏/强悍),并用页脚做 PG 式的脚注解释这个词。hero 之下用"before / after"呈现成功创始人的转变,刻意突出他们卑微的起点,让访客(builder)看到后产生"这可能就是我"的代入感。
> 🗣️ "we really wanted to not sell you a program or sell you a product, but instead make you dream." —— Eve Bouffard
> 译:我们真正想要的,不是向你推销一个项目或产品,而是让你敢做梦。
> 🗣️ "So that as a builder, you see that and you think, oh, this could be me. I could do this." —— Eve Bouffard
> 译:这样一来,作为一个 builder,你看到之后会想:哦,这也可能是我,我也能做到。

### 4. 可视化创始人的"蜕变" / Visualizing Founder Transformation `[05:30–07:00]`
**要点(中文)**: 左边是现在正在跑 batch、看起来平平无奇的人,右边是 10 年后建成世代级公司的同一批人——让访客"容易看见自己"。同时,介绍 YC 的核心段落**直接沿用 PG 十几年前写的原始文案**,借 Wayback Machine 对照,只把过时事实(一年四批、地点在旧金山而非山景城)更新掉。启示:真正好的核心文案有长期价值,不必为改版而重写。
> 🗣️ "these founders that are really incredible have built generational companies actually started in the same place that I'm at right now." —— Aaron Epstein
> 译:这些无比出色、建成了世代级公司的创始人,当初其实和我现在处在完全相同的起点。

### 5. 让创始人替自己说话 / Letting Founders Speak for Themselves `[07:00–08:45]`
**要点(中文)**: 描述"经历 YC 是什么感受",团队不用自己的话,而是访谈了近一两年走过 batch 的创始人,采集原声金句、并排拼成可连续阅读的文本(悬停可看头像与公司)。理由很直接:自己夸自己"会改变你的一生"没人信;同样的话从真实用户口中说出来,可信度和说服力都高得多——这也贴合"把创始人而非 YC 品牌放到台前"的整体主题。
> 🗣️ "We didn't want to say a bunch of things about how great YC is and it'll change your life and stuff like that. Instead, we wanted to just have the founders' stories communicate that." —— Aaron Epstein
> 译:我们不想自己讲一堆"YC 多棒、会改变你一生"之类的话,而是让创始人的故事来传达这一切。
> 🗣️ "it makes it a lot more credible and believable when it comes from them rather than us saying it about ourselves." —— Aaron Epstein
> 译:同样的话由他们说出来,而不是我们自夸,会可信、可靠得多。

### 6. 用 AI 让 YC 的人脉"活"起来 & 降低申请门槛 / Bringing YC's Network to Life `[08:45–12:00]`
**要点(中文)**: 两处落地。其一,把 events 上拍的合影**用 AI 轻度动画化**让画面"活起来";踩过很多工具的坑(人脸逐帧漂移、主创始人变得认不出),最后靠一家秋季 batch 的 YC 创业公司推荐的工具(名为 One)才做成——启示:选生成式工具要盯住"一致性/可识别性"这类硬指标。partner section 悬停能看到每位合伙人当年 batch 时的照片,强化"YC 的人也曾和你一样"。其二,收尾 CTA 是"永远不嫌太早,别想太多":很多人误以为要有收入/产品/成熟想法才配申请,而"给你机会的最好办法,就是去点申请按钮"。
> 🗣️ "one thing to make them feel even more alive could be to use a little bit of AI to animate them." —— Eve Bouffard
> 译:让这些照片更有生气的一个办法,就是用一点点 AI 把它们动画化。
> 🗣️ "very often the faces would change frame by frame and the founders, the main founders in the frame would become unrecognizable." —— Eve Bouffard
> 译:很多工具下,人脸会逐帧变化,画面里的主创始人会变得认不出来。
> 🗣️ "the best thing that gives you a shot is just hitting the apply button." —— Aaron Epstein
> 译:能给你机会的最好办法,就是去点那个申请按钮。

### 7. 极简设计 & 用 AI 当协作者的工作流 / Minimal Design & the AI-Assisted Process `[12:00–17:00]`
**要点(中文)**: 设计上聚焦叙事、砍掉一切干扰——hero 最终选了极简方案,整体"通透、呼吸感、内容像漂浮在页面上",刻意避免边框和硬分割线;甚至克制住"到处放 apply 按钮"的本能,因为这不是要抠 0.1% 转化率的 SaaS,加按钮只会稀释故事。工作流是最大亮点:先在 Figma 做 mood board 和方向,但画了几帧就觉得受限,于是**直接开新 repo,用 Opus 4.5 + Cursor 在真实页面上做原型**。他们把 Opus 4.5 当成设计团队的"同事",prompt 常常就是"这段要展示这些信息,创意地呈现出来",产出有时很烂、有时藏着"一颗好种子"值得留下来迭代(最终的轮播就是这么长出来的)。Aaron 强调:正因为能在活页面上看 before/after,才把这些交互逼了出来——在静态工具里根本到不了这个结果。AI 省下的基础编码时间,全部让给了最重要的叙事。
> 🗣️ "we'd rather go for something that is extremely minimal and simple. And that really gets the message across." —— Eve Bouffard
> 译:我们宁愿选一个极致极简、极其简单的方案,它才真正把信息传达出去。
> 🗣️ "this is not some B2B SaaS where we're, you know, trying to increase the conversion rate 0.1% or something. We want people to be inspired" —— Aaron Epstein
> 译:这又不是那种想把转化率提高 0.1% 的 B2B SaaS;我们要的是让人被激励、被鼓舞。
> 🗣️ "it would be probably more efficient to create a brand new repo, brand new project, and then just chat with Opus 4.5 and Cursor and see what it can cook up for us." —— Eve Bouffard
> 译:更高效的做法,大概是直接建一个全新 repo、全新项目,然后就和 Opus 4.5 加 Cursor 对话,看它能给我们"炒"出什么来。
> 🗣️ "we used Opus 4.5 as like a coworker as part of our little design team... some of our prompts were, this is the information we want to show in this section, display it creatively... And sometimes it's really bad. Sometimes it has a kernel of something good that we wanted to keep." —— Eve Bouffard
> 译:我们把 Opus 4.5 当成小设计团队里的一名同事……有些 prompt 就是"这一段我们想展示这些信息,请创意地呈现出来";它的产出有时很糟,有时藏着一颗我们想保留、值得继续打磨的好种子。
> 🗣️ "for all of these sections, we would not have ended up where we ended up had we not been actually doing it live, basically." —— Aaron Epstein
> 译:所有这些板块,如果不是真的在活页面上边做边看,我们根本到不了最终这个结果。

### 8. 交互式网页设计的未来 / The Future of Interactive Web Design `[17:00–18:40]`
**要点(中文)**: Aaron 对未来 1–5 年的判断:网页与产品设计会更多地从"静态图 + 静态文字"转向用交互和动画来传达想法——但永远不是为动效而动效,而是因为它更好地传达了你想表达的信息;而如今做到这点比以往任何时候都容易。收尾是两人互相致谢与对成果的自豪。
> 🗣️ "how can you use interactivity and animation and things like that? Not for that sake, but because it does a better job of communicating the message that you want." —— Aaron Epstein
> 译:如何运用交互、动画这类手段?不是为了用而用,而是因为它能更好地传达你想传达的信息。
> 🗣️ "It gave us a lot of bandwidth to focus on the storytelling, which was probably the most important part of this whole project." —— Eve Bouffard
> 译:(AI)给了我们大量余力去聚焦叙事,而叙事大概是整个项目里最重要的部分。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把落地页目标从"卖功能"改成"让用户看见自己"**:首屏别堆 feature/CTA,先用一个"before → after"式的转变故事,让目标用户产生"这就是我要的结果/我也能做到"的代入感。
- [ ] **用真实用户原声替代自夸**:找 5–10 个已用过你 Agent 的真实用户做短访谈,采集原声金句拼成信任背书区,悬停显示头像/公司;可信度远高于你自己写的"效果很好"。
- [ ] **审一遍首页每句文案**:凡是"结果不言自明""效果显著"这类空话,要么量化(提升多少 %、省多少小时),要么删掉;凡是"我们不做 X"的负面表达,改成正面价值主张。
- [ ] **把 Opus 4.5 + Cursor 当设计协作者做原型**:别在 Figma 里死磕静态稿,开一个新 repo,用"这段要展示这些信息,请创意地呈现出来"这类 prompt 让它出交互版本,在活页面上迭代——最好的方案往往是"边做边看"逼出来的。
- [ ] **动效/交互只为传达服务**:给每个 section 先问"最能表达这段信息的交互是什么",而不是"这里加个动画好不好看";砍掉边框、硬分割线和多余装饰,给内容留白。
- [ ] **选生成式 AI 工具盯"一致性"硬指标**:做 AI 图像/视频/动画时,把"跨帧是否漂移、主体是否可识别"当作选型的第一标准,而不是单看单帧惊艳度;多找同行推荐踩过坑的工具。

## 🔑 关键术语 / 概念
- **Inspire, don't sell(激发而非推销)** — 落地页的核心定位:不去推销项目/产品,而是让访客"敢做梦"、看见自己能成为的样子。
- **Formidable(强悍/令人生畏)** — PG 与 Jessica 早年用来形容他们所投的非凡创始人的词;新站把它作为核心气质,并用 PG 式脚注在页脚解释。
- **Before / After transformation(转变叙事)** — 用"当下的普通起点 vs 未来的世代级成就"并置,制造用户代入感的叙事结构。
- **Storytelling over utility(叙事优先于实用堆料)** — 与"B2B SaaS 模板式"页面相对:优先讲清一个能打动人的故事,而非罗列功能与数据。
- **AI as a coworker(把 AI 当同事)** — 用 Opus 4.5 + Cursor 在真实代码/页面上协作出创意与交互原型的工作方式,而非仅当补全工具。
- **Minimal design(极简/呼吸感设计)** — 去边框、去硬分割线、去多余动效,让内容"漂浮"、留白通透,把注意力集中到人脸与故事上。

## 🔖 高价值金句时间戳
- `[04:04]` "we really wanted to not sell you a program or sell you a product, but instead make you dream." — 一句话定死改版北极星:激发梦想,而非推销。
- `[07:43]` "it makes it a lot more credible and believable when it comes from them rather than us saying it about ourselves." — 信任背书法则:让用户替你说,别自夸。
- `[14:15]` "it would be probably more efficient to create a brand new repo... and then just chat with Opus 4.5 and Cursor and see what it can cook up for us." — 用 AI 编码工具跳过静态稿、直接做原型的工作流转向。
- `[16:07]` "we used Opus 4.5 as like a coworker as part of our little design team." — 把 AI 当协作者而非补全器的心态标签。
- `[15:00]` "we would not have ended up where we ended up had we not been actually doing it live." — 好交互是"在活页面上边做边看"逼出来的,不是静态工具里想出来的。
- `[13:19]` "this is not some B2B SaaS where we're... trying to increase the conversion rate 0.1%... We want people to be inspired" — 提醒别把每个页面都做成抠转化率的 SaaS,克制加 CTA 的冲动。
