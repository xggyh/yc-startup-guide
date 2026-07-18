# 点阵图:真正看清用户在做什么 / Dot Plots: How to Actually See What Your Users Are Doing

> **来源**: [Dot Plots: How to Actually See What Your Users Are Doing](https://www.youtube.com/watch?v=e5-6rEwzxLs) · Y Combinator · 2026-07-09 · 时长 13:50
> **讲者**: David Lieb(YC General Partner,Bump 创始人,前 Google Photos 负责人;视频中自称 "Dave")
> **一句话定位**: 手把手教你用"点阵图"这一张纸/一块屏,看清每个用户逐日的真实使用行为,替代会骗人的 DAU/MAU 聚合曲线——对判断 AI Agent 产品是否真的被需要至关重要。

## 🎯 TL;DR(中文核心要点)
- **聚合指标会骗你**:DAU/MAU 只要有增长就"向右上",哪怕用户根本不喜欢产品;它无法告诉你任何一个具体用户在怎么用。
- **点阵图 = 一张二维网格**:每一行是一个用户,每一列是一个时间段(默认用"天"),用户当天做了"价值动作"就画一个点,首次使用日再套一个圈。
- **点要选"价值事件",不是"打开 App"**:听一首歌、分享一张照片、处理一张发票才算数;选 "open the app / signed in" 只是为了让图好看,毫无信号。
- **人脑擅长在网格里找模式**:工作日用户 vs 周末用户、一次性流失、某功能带来长连续使用——这些聚合曲线永远看不到。
- **可加"状态维度"**:用不同符号/底色标记 iOS/Android、国家、收入等属性,再按属性排序,让模式浮现(源自 PayPal 反欺诈"人肉盯图"的思路)。
- **B2B 同样适用**:一个 $80K/年合同买了 10 个座位却只激活 3 个、每周用不到两天——点阵图能提前预警续约危机。
- **时间粒度别太宽**:用"天"甚至"子天",别用"周",否则看不出真实节奏。
- **实现极简**:本质是日志可视化,没有复杂计算,"现代 AI 编码工具 10 分钟就能搭出来";与 cohort 留存曲线配合使用效果最佳。

## 🧭 适合谁 / 什么时候看
- 刚有 10 – 几百个用户、想判断"是否 build 了 people want"的早期创始人。
- AI Agent 方向的创始人:需要定义"Agent 到底何时为用户创造了价值",而不是盯着调用量/登录数自欺。
- 卖席位(seats)的 B2B/SaaS 团队:想提前发现座位未激活、champion 流失、续约风险。
- 任何被 DAU/留存曲线"感觉还行"迷惑、却说不清用户具体行为的团队。

## 📝 分段精读

### 1. 别再盯着聚合指标 / Stop Looking at Aggregate Metrics · Why DAUs Lie `[00:08–01:39]`
**要点(中文)**: 创始人最大的错误之一,是用聚合指标代替对"任何一个具体用户如何使用产品"的理解。上一集讲的 cohort 留存曲线能告诉你用户是否留存,但答不出他们"怎么用、用什么功能、多频繁"。DAU/MAU 这类聚合图只要有增长就"向右上",哪怕用户其实不享受产品——这是最危险的假信号。
> 🗣️ "One of the biggest mistakes I see founders make is relying on aggregate user metrics instead of understanding how any individual users use their product." —— David Lieb
> 译:我看到创始人犯的最大错误之一,就是依赖聚合用户指标,而不去理解任何一个具体用户是怎么使用产品的。
> 🗣️ "And if you have any amount of growth, those graphs tend to be going up and to the right, even if users aren't actually enjoying using your product." —— David Lieb
> 译:只要你有一点点增长,那些曲线就会一路向右上方,哪怕用户其实根本不喜欢用你的产品。

### 2. 什么是点阵图 & 怎么选事件 / What is a Dot Plot · Picking the Right Event `[01:39–03:34]`
**要点(中文)**: 点阵图就是一张二维网格(像电子表格):每行一个用户,每列一个时间段(建议用"天")。关键在于选一个代表"产品价值"的事件——分享照片、听一首歌、处理一张发票——用户当天做了就画一个点;首次使用那天再套个圈,多给一点信号。日积月累就得到一张高密度的"个体使用行为"可视化。
> 🗣️ "You want to pick an event that your user does in the process of using your product that you think represents value in the product." —— David Lieb
> 译:你要挑一个用户在使用产品过程中会做、且你认为代表了产品价值的事件(作为要画点的动作)。

### 3. 在点里读出模式 / Reading Patterns in the Dots `[03:34–05:17]`
**要点(中文)**: 一旦能看到个体行为,人脑会自动发现聚合图里绝对看不到的模式:有的用户只在工作日用(可能在办公室听),有的只在周末用——这决定了你该服务哪类用户、怎么改产品。还能一眼看出留存问题,比如"试了一天就再没回来"的用户(user four)。Bump 当年用不同符号区分"交换名片"还是"分享照片",可以做到任意精细。
> 🗣️ "What's really cool about this is it lets you figure out patterns that you probably would not have seen with your human brain, just looking at aggregate charts or looking at individual user logs." —— David Lieb
> 译:它真正厉害的地方在于:能让你发现一些你光看聚合图表、或光翻单个用户日志时,人脑根本发现不了的模式。

### 4. 追踪用户状态与属性 / Tracking User State & Attributes `[05:17–06:41]`
**要点(中文)**: 除了追踪"动作",还能追踪"状态":iPhone/Android、Web、国家、收入水平、来源(比如从 Reddit 拉来的大学生),用不同符号或底色编码。然后按任意属性排序,只看某一类用户(如只看 iOS、或只看某周一首次使用的人)。这样一屏看下来,大脑会自发注意到那些你事先(a priori)绝不会预设的规律。GitHub 首页的贡献热力图就是把"天"按周折行的点阵图。
> 🗣️ "Your brain will start to notice these patterns in a way that you would never have figured out on your own a priori." —— David Lieb
> 译:你的大脑会开始注意到那些模式——而这些是你靠先验推理、自己怎么想都想不出来的。

### 5. PayPal 反欺诈的启发 / The PayPal Fraud Insight `[06:41–07:29]`
**要点(中文)**: 这个方法的思想源自 PayPal 联创 Max Levchin。早期 PayPal 深受欺诈困扰却不知该找什么模式,于是他们把所有交易画成可视化图,让人肉盯屏——即便说不清具体逻辑,人也能一眼指出"那里不太对,八成是欺诈",再去深挖。点阵图同理:先用眼睛发现异常模式,再去下钻调查。
> 🗣️ "They were able to look at the screen and say, that thing happening there, that's different and probably fraud." —— David Lieb
> 译:他们能盯着屏幕说:那边正在发生的那个东西不太一样,很可能是欺诈。

### 6. 点阵图 vs DAU 图 & 找出驱动留存的功能 / Dot Plot vs. DAU · Features That Drive Retention `[07:29–09:36]`
**要点(中文)**: 把同一批用户画成 DAU 曲线,只会看到 2-3-2-2-2-1-0 这种"没啥增长"的干瘪结论;点阵图却给出对用户行为乃至生活方式的丰富理解。更进一步:用不同符号标记不同功能(用了搜索标 S、加入公开歌单标 P),就能看到"加入公开歌单"后紧跟一长串连续使用日——从而推断某功能可能是驱动活跃的因果因素,再去验证。
> 🗣️ "We could then infer like, oh, maybe the playlist feature is really causal to having people be really active in our product." —— David Lieb
> 译:于是我们可以推断:哦,也许"歌单"这个功能,才是真正让用户在产品里高度活跃的因果原因。

### 7. 规模化 & $80K 合同流失案例 / Scaling to Billions · The $80K Contract That Churned `[09:36–11:53]`
**要点(中文)**: 早期你能把每个用户每一天都放进一屏看完;规模大了(Google Photos 十亿+ 用户)则改为抽样——打印几十张点阵图,把"法国的 iOS 用户""美国 Web 上年收入 8 万美元以上的用户"分给团队各自研读。B2B 也一样:一个 $80K/年、买了 10 座位的名牌客户,实际只激活 3 座、每周用不到两天;后来推动购买的 champion 离职,新来的人一句"我们为什么要用这软件"就退订了。点阵图本可提前暴露这份合同岌岌可危。
> 🗣️ "The company bought 10 seats, but only three seats ever activated. Only three of those people ever tried the product." —— David Lieb
> 译:那家公司买了 10 个座位,但只有 3 个座位真正被激活——只有 3 个人试用过产品。
> 🗣️ "The company could have known that this contract was in jeopardy by looking at the dot plot." —— David Lieb
> 译:只要看一眼点阵图,这家公司本可以知道这份合同已经岌岌可危。

### 8. 常见误用 & 与 cohort 曲线配合 / Common Mistakes · Dot Plots + Cohort Curves `[11:53–13:50]`
**要点(中文)**: 两个头号误用:(1) 画错事件——为了图好看去选"打开 App/登录",这类事件不代表用户获得真实价值;要选"听歌/分享照片"这种真价值事件。(2) 时间粒度太宽——用"周"会掩盖真实节奏,应该用"天"甚至"子天"。在拥有几百个用户之前,点阵图可以是你唯一的仪表盘;它本质只是日志可视化,没有复杂计算,现代 AI 编码工具 10 分钟就能搭好。最后与 cohort 留存曲线搭配:曲线告诉你"整体是否留存",点阵图告诉你"他们具体怎么用",两者结合最强。
> 🗣️ "Maybe you'll pick like open the app or signed into the product. Those are pretty bad events to choose because they don't really measure whether the user is getting real value." —— David Lieb
> 译:你可能会选"打开 App"或"登录产品"这类事件——但它们是很糟糕的选择,因为它们根本衡量不了用户是否真的获得了价值。
> 🗣️ "Until you have hundreds of users, the dot plot could be your only dashboard." —— David Lieb
> 译:在你拥有几百个用户之前,点阵图完全可以是你唯一的仪表盘。
> 🗣️ "This is a thing that modern AI coding tools can whip up in 10 minutes." —— David Lieb
> 译:这种东西,现代 AI 编码工具 10 分钟就能给你搭出来。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **为你的 Agent 定义一个真正的"价值事件"**:不是"发起会话/调用一次",而是"任务被成功完成""Agent 产出被用户采纳/合并""跑通一次真实工作流"——用它作为点阵图的点。
- [ ] **本周用 AI 编码工具搭一版点阵图**:解析日志 → 二维网格(行=用户,列=天),首用日套圈;讲者说这类工具 10 分钟就能搭出来,别拖。
- [ ] **用"天"级粒度**,拒绝用"周"掩盖节奏;必要时下探到子天,看清 Agent 的使用是持续还是零星。
- [ ] **叠加状态维度**:标记模型/套餐、平台、来源、企业客户 vs 个人,按属性排序,找出"哪类用户离不开 Agent"。
- [ ] **给 Agent 每个功能编码符号**(如工具调用、记忆、自动化触发),观察哪个功能后面跟着"一长串连续使用日",定位驱动留存的功能再重点投入。
- [ ] **若卖席位(seats)**:为每个企业客户画点阵图,监控"买了 N 座实际激活几座、每周用几天、champion 是否还活跃",提前预警续约风险。
- [ ] **点阵图 + cohort 留存曲线一起看**:曲线判断整体留存,点阵图解释行为原因,两者结合去问对问题、改对功能。

## 🔑 关键术语 / 概念
- **Dot Plot(点阵图)** — 二维网格:每行一个用户,每列一个时间段,用户当天做了"价值动作"就画点,首用日套圈;一屏内看清个体逐日行为。
- **价值事件(value event)** — 代表用户真正获得价值的动作(听歌/分享照片/处理发票),而非"打开 App""登录"这类无信号动作。
- **DAU / MAU** — 日活/月活等聚合指标;有增长就"向右上",无法反映个体行为,易造成"产品健康"的错觉。
- **Cohort 留存曲线(cohort retention curve)** — 按获取批次追踪用户是否随时间留存的聚合工具;与点阵图互补:一个看"是否留存",一个看"如何使用"。
- **首用日套圈(ring on first day)** — 在用户首次使用当天的点上加圈,便于识别 onboarding 与一次性流失模式。
- **状态编码(user state)** — 用符号/底色标记用户属性(平台、国家、收入、来源等),再排序以让模式浮现。
- **Champion(内部推动者)** — B2B 中促成采购的关键人;其离职常是合同流失的前兆,点阵图可提前发现座位未激活的迹象。

## 🔖 高价值金句时间戳
- `[00:08]` "One of the biggest mistakes I see founders make is relying on aggregate user metrics instead of understanding how any individual users use their product." — 全片核心:别用聚合指标代替对个体用户的理解。
- `[01:16]` "those graphs tend to be going up and to the right, even if users aren't actually enjoying using your product." — DAU 向右上是假信号,可能掩盖用户其实不爱用。
- `[02:32]` "You want to pick an event that your user does ... that you think represents value in the product." — 选点=选"真价值事件",这是点阵图成败关键。
- `[03:47]` "it lets you figure out patterns that you probably would not have seen with your human brain, just looking at aggregate charts or looking at individual user logs." — 点阵图的价值在于让人脑发现聚合图看不到的模式。
- `[11:15]` "The company bought 10 seats, but only three seats ever activated." — B2B 席位买了却不激活,是续约流失的早期铁证。
- `[12:46]` "Until you have hundreds of users, the dot plot could be your only dashboard." — 早期阶段,点阵图足以当唯一仪表盘。
- `[13:02]` "This is a thing that modern AI coding tools can whip up in 10 minutes." — 实现零门槛,用 AI 工具即刻上手,没有借口不做。
