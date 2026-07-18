# Vibe Coding 落地页的常见翻车点 / Common Mistakes With Vibe Coded Websites

> **来源**: [Common Mistakes With Vibe Coded Websites](https://www.youtube.com/watch?v=DNSXlBmukck) · Y Combinator · 2026-03-06 · 时长 37:26
> **讲者**: Aaron Epstein(YC 合伙人,主持,SPEAKER_00)· Raphael Schaad(YC Visiting Partner、Cron / Notion Calendar 创始人兼设计师,SPEAKER_01)
> **一句话定位**: 一期 Design Review,现场拆解 6 个 YC 公司用 AI 一把梭出来的落地页,总结 vibe coding 最常见的设计翻车点——教 AI Agent 创始人把 AI 设计工具的"超能力"用在获客转化上,而不是把它变成一眼可辨的 "AI slop"。

## 🎯 TL;DR(中文核心要点)
- **落地页是获客渠道,不是产品,更不是"炫技作品"**。评价每个动效只问一个问题:它有没有帮我把访客转化成客户?没有就砍掉。
- **紫色渐变、fade-in、追光标的按钮、滚动劫持、鼠标跟随线——这些是 LLM 训练数据里的"高频套路"**,一个好网站火了,下周所有创业公司网站就都长一样,原创性和品牌感被稀释。
- **"能做"不等于"该做"**:很多动效(SVG 线条、meteor、卡片乱飞)人类从头写根本不划算,只是因为 AI 免费给你,你就顺手 accept 了——这恰恰是要警惕的。
- **人必须当"有主见的编辑",而不是无脑 accept all changes**。把 AI 省下来的时间投到 messaging、原创视觉和产品打磨上。
- **一把梭出来的东西你要真去用一遍(QA)**:hover 消失、假点击热区、选中态 bug、fade-in 把内容藏起来——这些小 bug 你不注意就直接上线了,客户会觉得"产品是不是也是 vibe 出来的"。
- **H1 三件事 + CTA**:是什么、给谁用、对他有什么价值,以及一个明确行动号召——首屏没讲清这几点,转化就难。
- **hover 只用来"让界面活起来 / 提示可点击",不要用它藏关键信息或功能**(手机根本没有 hover;long-press 从没在移动端普及)。
- **系统 emoji / 通用图标 / 假 dashboard(bento box + 图标+小标题)是明显的 "AI 味" tell**,一看就知道没花心思。

## 🧭 适合谁 / 什么时候看
- 正在用 Lovable / v0 / Cursor 等 AI 工具"一把梭"落地页、准备申请 YC 或上线首页的创始人。
- AI Agent 方向的技术创始人:你能写代码,但视觉品味和转化设计是短板,想知道审美红线在哪。
- 任何觉得"AI 能生成完整网站了,设计不用管"的人——这期专治这种错觉。

## 📝 分段精读

### 1. AI 设计趋势与 "AI slop" / AI design trends & the slop era `[00:00–02:58]`
**要点(中文)**: 开场点题:AI 让人人都能做出"看起来很专业"的网站,但也带来了千篇一律的 slop。核心机制是——过去一个好设计要很久才被抄袭,现在只要它够好、被大量链接,就会进入 LLM 训练数据,下周所有创业公司网站就都长成同一个样。紫色渐变、滚动 fade-in 本身不坏,坏在"太普遍以至于失去了特别感和原创性"。
> 🗣️ "if there's a good website with a purple gradient, it makes it into the LLM because the LLM gets trained on like the good examples that get linked to a lot. And then all of a sudden, like the next week, all the startup websites look the same." —— Raphael Schaad
> 译:如果有个好网站用了紫色渐变,它就会进到 LLM 里——因为 LLM 训练时吃的就是那些被大量链接的好案例。然后突然之间,下周所有创业公司的网站就都长一个样了。

### 2. Nunu.ai:好动效 vs 多余动效 / Nunu.ai `[02:58–09:25]`
**要点(中文)**: 第一个案例。紫色渐变一眼"AI 味"。跟随滚动的竖线纯属分散注意力——"人类根本不会想从头写这种线,只因为 AI 做起来太容易"。但卡片的 hover 动画是**好例子**:强化了品牌、有创意、过去只有顶级设计师才做得起。反例是导航 hover:鼠标移上去菜单反而**淡出/消失**,而浏览器本来就免费给你一个"手型光标"提示可点击,LLM 却发明了"越点越看不见"的反直觉效果。结论:AI 时代做不出基础水准的设计,等于"没努力"。
> 🗣️ "just because we now can, just because LMS are kind of like good at these type of like SVG... transforms doesn't mean that it's actually a good design and helps you convert potential... visitors into... customers" —— Raphael Schaad
> 译:并不是因为我们现在能做、因为 LLM 擅长这类 SVG 变换,它就真的是好设计、就真能帮你把潜在访客转化成客户。
> 🗣️ "it seems like the person just didn't even try because it's so easy to do it now." —— Aaron Epstein(评审 YC 申请时,若 demo 连基础设计水准都没有)
> 译:(现在做设计这么容易)看起来就是这人压根没努力。

### 3. Rosebud AI:非标准导航与品牌一致性 / Rosebud AI `[09:25–13:30]`
**要点(中文)**: 又是紫色渐变。首屏能直接玩一个浏览器 3D 游戏很吸引人,但页面没说清"这是用我们产品做的",错失了最强的证明点。非标准的锚点导航(点击垂直跳转)让人摸不着头脑。红色 logo 配紫色强调色并不协调;用系统 emoji 当图标显得"偷懒"——因为 LLM 没有自己的 IP,只会东拼西凑通用素材,一眼就露馅。首屏要讲清 H1 三件事 + CTA。
> 🗣️ "what's important for the H1 is typically kind of, you know, what is it, who is it for and to what end, why should that person that it's for care" —— Raphael Schaad
> 译:H1 真正重要的通常是:这是什么、给谁用、为了达成什么目的、这个目标用户为什么要在乎。
> 🗣️ "whenever I see the use of emojis, even though they're not the system emojis, I feel like it's a little lazy. And so I, I feel like LLMs kind of take the easy path because they don't have any IP really themselves." —— Raphael Schaad
> 译:每次看到用 emoji(哪怕不是系统 emoji)我都觉得有点偷懒。我感觉 LLM 走的是捷径,因为它们自己根本没有 IP。

### 4. Getcrux:滚动劫持与追着光标跑的按钮 / Getcrux `[13:30–19:12]`
**要点(中文)**: 自动 fade-in + 滚动被劫持(scroll jacking),体验"像在糖浆里游泳"。CTA 按钮一直追着鼠标跑,反而难点、且喧宾夺主——"它确实吸引了我的注意,但我根本没注意他们是干什么的"。角上还有 meteor 划过、hero 用了模糊的视频封面图。视觉语言前后不统一(疑似不同区块由 AI 分别生成)。启示:所有素材都该高清;fade-in/滚动劫持会让访客不知道"读到书的哪一页了",scroll indicator 是重要工具。
> 🗣️ "just because something is possible. Doesn't mean you should say yes to it." —— Aaron Epstein
> 译:一件事"能做到",不代表你就该对它说"是"。

### 5. Sphinx:层级混乱与"LLM 幻觉的视觉化" / Sphinx `[19:12–25:43]`
**要点(中文)**: 信息层级被 LLM 搞乱:logo、H1、副文本之外,又平白多出第四、第五种字体样式("meets Sphinx"),既占垂直空间又不加信息。右侧一堆按钮不停变形、换样式、自动轮播,还是"假点击热区"(显示手型却不是真按钮,点哪都能触发)——Raphael 称之为"LLM 幻觉的视觉化"。核心是:人必须当**有主见的编辑**,而不是把 AI 的每个建议都 accept。同时又肯定 Sphinx 把"是什么、给谁"讲得很清楚。
> 🗣️ "it feels like the visual manifestation of lm hallucinations" —— Raphael Schaad
> 译:这感觉就像是 LLM 幻觉的视觉化呈现。
> 🗣️ "You really have to be opinionated as the human that's in the loop and designing these around what you think is the right thing. Not just kind of saying yes, except all changes." —— Aaron Epstein
> 译:作为回路里的那个人,你必须真的有自己的主见,按你认为对的方式去设计,而不是一味说"好、接受所有改动"。

### 6. Build0:一次成型 ≠ 真能用 / Build0 `[25:43–30:30]`
**要点(中文)**: 又见紫色渐变、"dumb hover effect"(菜单竖向抖动、箭头往反方向移、整条菜单水平错位像 bug)。也有好 hover(黑白按钮变主品牌色)。交互组件里有明显选中态 bug——"如果是手写的,没人会注意不到"。由此引出关键提问:如果你只是 one-shot 生成落地页,你到底有没有真的去用一遍?你不会发现 LLM 埋下的小 bug,就直接把它们上线了。假 dashboard、bento box(图标+小标题的 3×2 网格)是最常见、也最没原创性的 AI 套路。AI 应把你从技术细节里解放出来,让你去想"做什么、给谁、为什么有价值"这些真正难的问题——而不是拿这份算力去批量生产 slop。
> 🗣️ "I almost wonder like if you're just one shot landing pages, do you actually go and really like use it?" —— Raphael Schaad
> 译:我甚至怀疑,如果你就是 one-shot 生成落地页,你到底有没有真的去用它一遍?
> 🗣️ "the really cool thing about ai tools is that it kind of frees you from having to kind of like you know fiddle with like the technical details so it can really work on the hard hard kind of questions of your offering of your product of your company such as like what are we making for whom why is this valuable to them" —— Raphael Schaad
> 译:AI 工具真正酷的地方,是把你从鼓捣技术细节里解放出来,让你能去攻克产品/公司里真正难的问题——比如我们在为谁做什么、这对他们为什么有价值。

### 7. Zarna:信息稀薄与 "molasses" 体验 / Zarna `[30:30–34:33]`
**要点(中文)**: 又被滚动劫持,"10x everything / everything unlocked" 这类词堆砌,信息量极低、留白过多,"像在糖浆里滚动老半天才看到有用的东西"。首屏占满 100% 视口高度、还配"scroll down to see more"——"当然知道要往下滚,这是网页"。更好的做法:让首屏稍微被打断,露出一点点下方的精彩内容,自然引导下滚。透明导航栏遇到动态视频背景会读不清(智能反色遇视频失效)。可点/不可点混乱、chevron 时有时无,整体"有点糙"。唯一亮点:至少没用紫色,视觉风格(颗粒感、放大背景图)其实挺清新。
> 🗣️ "it feels like i'm in molasses it just feels so clunky to use" —— Aaron Epstein
> 译:感觉像陷在糖浆里,用起来特别卡顿笨重。

### 8. 总结:落地页是"获客渠道",别把思考外包给 LLM / Takeaways `[34:33–37:26]`
**要点(中文)**: 两位收束观点。Raphael:大量紫色渐变、为动效而动效的雷同套路;有 AI 超能力是幸运,但你仍有责任**不把思考外包给 LLM**,只把它当工具帮你把好点子做出来。落地页本质是"定制化的获客渠道",不是产品、不是网络艺术品。Aaron 补两点:(1) **QA everything**——人必须逐一检查交互和 bug;(2) 品牌与原创性要真正代表你的公司,用和别人一样的工具很容易落到和别人一样的地方,你得**刻意**去到不一样的地方。把一把梭省下的时间,投到 messaging 和产品打磨上。
> 🗣️ "you are still kind of like responsible to not outsource your thinking to llms" —— Raphael Schaad
> 译:你仍然有责任——不要把你的思考外包给 LLM。
> 🗣️ "these are like startup landing pages and they're basically custom acquisition channels" —— Raphael Schaad
> 译:这些是创业公司的落地页,本质上就是定制化的获客渠道。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **给每个动效/效果做"转化审计"**:逐个问"它帮我转化了吗",答不上来就删(紫渐变、追光标按钮、meteor、鼠标跟随线、滚动 fade-in 优先审查)。
- [ ] **首屏按 H1 公式重写**:一句话讲清"是什么 / 给谁 / 对他什么价值" + 一个明确 CTA;确保透明导航栏在你的背景/视频上仍清晰可读。
- [ ] **落地页生成后当真实用户走一遍并 QA**:点每个按钮、测每个 hover、快速滚一遍看 fade-in 会不会漏内容、检查选中态和"假点击热区" bug 后再上线。
- [ ] **主动去"AI 味"**:换掉系统 emoji / 通用图标 / 假 dashboard bento box,做一处真正原创、on-brand 的视觉(哪怕只有一个元素),避免"和其它 AI Agent 产品撞脸"损失可信度。
- [ ] **hover 只用于提示可点击或让界面"活起来",绝不藏关键信息/功能**;移动端没有 hover,重要功能必须默认可见。
- [ ] **别用滚动劫持**:保留原生滚动,加一个清晰的 scroll indicator,让访客随时知道"读到哪了"。
- [ ] **把一把梭省下的时间再投入**:打磨 messaging、做一处别人没有的原创设计,把落地页当"获客渠道"而非"作品"来优化转化。

## 🔑 关键术语 / 概念
- **Vibe coding / one-shotting** — 用 AI 工具"一把梭"生成整站/整个落地页,通常不逐行检查、直接上线。
- **AI slop** — AI 批量产出的、雷同且缺乏原创性的内容/设计(此处指网站视觉)。
- **Scroll jacking(滚动劫持)** — 用 JS 接管浏览器原生滚动做花哨过渡,导致"像在糖浆里"、无法判断阅读进度。
- **Dumb hover effect** — 无意义的悬停动效(菜单抖动/淡出、箭头乱移),分散注意力甚至误导可点击性。
- **H1 三要素 + CTA** — 首屏标题需回答:是什么 / 给谁 / 有什么价值,并给出明确行动号召。
- **Bento box / 假 dashboard** — LLM 高频套路:图标+小标题的网格块、或深色图标配浅色背景的仿真仪表盘,非原创的明显 tell。
- **Custom acquisition channel(定制化获客渠道)** — 对落地页的正确定位:目标是转化,不是当"网络艺术品"或产品本身。

## 🔖 高价值金句时间戳
- `[02:11]` "if there's a good website with a purple gradient, it makes it into the LLM... And then all of a sudden, like the next week, all the startup websites look the same." — 解释了为何创业网站集体撞脸:好设计经 LLM 训练被瞬间复制,原创性被稀释。
- `[08:46]` "it seems like the person just didn't even try because it's so easy to do it now." — 设计门槛已降到最低,做不出基础水准 = 直接暴露"没努力",尤其在被评审时。
- `[15:08]` "just because something is possible. Doesn't mean you should say yes to it." — AI 时代的核心自律:能做的太多,克制说"不"才是竞争力。
- `[20:41]` "You really have to be opinionated as the human that's in the loop... Not just kind of saying yes, except all changes." — 人要当有主见的编辑,而不是无脑 accept all。
- `[22:13]` "it feels like the visual manifestation of lm hallucinations" — 一句精准命名:界面上乱变形的组件,就是模型幻觉的视觉版。
- `[26:23]` "I almost wonder like if you're just one shot landing pages, do you actually go and really like use it?" — 一把梭最大的隐患:你根本没真用过,小 bug 就随页面上线了。
- `[34:42]` "these are like startup landing pages and they're basically custom acquisition channels" — 给落地页正确定位:优化目标是获客转化,不是炫技或艺术。
