# React Native 在 Airbnb 的使用（2018-06-20）

## 原文链接

[React Native at Airbnb](https://medium.com/airbnb-engineering/react-native-at-airbnb-f95aa460be1c)

## 文章内容大意

### 引入 React Native 的背景

选择 React Native 的原因：有限的开发团队满足不了日益增长的也无需求。

Airbnb 引入 React Native 的目标有：

1. 大团队快速迭代（Allow us to move faster as an organization.）
2. 原生应用质量（Maintain the quality bar set by native.）
3. 代码跨双平台（Write product code once for mobile instead of twice.）
4. 提升开发体验（Improve upon the developer experience.）

### React Native 的好处

- 跨平台 （只有 0.2% 的平台特定代码）
- 统一的设计语言，同时还能为不同平台提供不同设计
- React 的 scale 很好，生命周期比原生简单，声明式很好
- 迭代速度快（主要是 hot reloading 很快）
- 大量基础设施的投入值得（网络、国际化、复杂动画、设备信息、用户信息等等都是通过一个桥把原生 api 暴露给 RN 的。）
- 同时他们在这里也指出：他们并不相信在一个已有 app 上集成 RN 是一件简单事儿，必须要大量且持续地投入基础设施才行（说好的「满意的地方」呢）
- 性能 （尽管大家都担心但是其实基本没有问题）
- 不过首次渲染比较慢，导致不适合用作启动屏、deeplink，也增加了可交互时间（TTI），另外掉帧不好 debug（说好的「满意的地方」呢）
- Redux（好用，虽然废话太多）
- 背后是原生，一些曾经不确定能不能做的功能（Shared element transitions、动画库 Lottie、网络层、核心基础设施）发现都能做
- 静态分析（eslint，prettier，一些性能检测）
- 动画
- JS/React 的开源生态
- Flexbox （via Yoga）
- 有时候可以加上 Web 跨三端

### React Native 的问题

- RN 太不成熟
- 需要 fork RN
- JS 不行 （JS 没有类型不 scale，flow 不好用，TS 不好集成到 babel 和 metro）
- 不好重构（JS 没有类型无法静态分析，重构引起的错误不能在编译时被捕捉到）
- JSCore 在 iOS / Android 上不一致 （Android 上是 RN 自己 bundle 的），很难 debug 这种坑
- RN 的开源库质量不行（因为太少人能精通所有平台了）
- 做功能时要回去搞基础设施（因为有的基础设施可能还没暴露给 RN）
- 崩溃监控（业内没方案，只能自己搞）
- 原生桥太难写，另外 JS 的类型太难预料（和强类型语言 interop 时）
- RN 运行时的初始化太慢
- 首次渲染时间慢（需要从 主线程 -> JS -> Yoga -> 主线程）
- 应用体积
- 64 位 （因为 RN 不兼容的 issue 导致他们至今没法在 android 发布 64 位应用）
- 手势（iOS 和 Android 的手势不好统一，虽然他们搞了 react-native-gesture-handler）
- 长列表，虽然 RN 团队很努力了，但是由于 RN 的异步通信机制，长列表的流畅渲染，目前依然无解。
- 升级 RN 有的时候非常麻烦
- Accessibility （RN 的有 bug，又要 fork）
- 稀奇古怪的崩溃
- 安卓上的应用实例序列化问题

### 不是技术问题的问题

1. 要用好 RN 你必须同时熟悉 iOS 和 Android ，当然还有 RN 本身，这就对我们工程师提出了更多挑战。
2. 团队的管理，责任的划分。
3. 生态，RN 文档及相关资源不如 iOS 和 Android 的丰富。

面对技术与管理的双重挑战，他们认为 RN 并没有达到他们最初列出的四个目标，所以决定 sunset RN 了。

### Airbnb 在移动端的未来方向

一个新方向：

**Server-Driven Rendering （服务端驱动渲染）**

服务端发送某种 View 的抽象描述，然后移动端解析这种描述并渲染。

## 个人感想

事情的复杂性就在那里，一种技术解决了一些问题必然会带来其它的问题。对于移动端跨端，使用某种框架就会受限于该框架的局限，因此简单的小项目可以尝试跨端写一套代码，复杂的应用还是应该用原生开发。
