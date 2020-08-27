# TypeScript, why is so important?（2020-08-16）

## 原文链接

[TypeScript, why is so important?](https://www.warambil.com/typescript-why-is-so-important)

## 文章内容

文章先介绍编程语言强类型的好处，然后对 TypeScript 做了一个简明介绍。

### 安装

```bash
# npm
$ npm install typescript

# yarn
$ yarn add typescript
```

### 使用

```bash
tsc demo.ts

npx tsc demo.ts
```

### demo

```typescript
/**
 * demo
 */

function add(num1: number, num2: number): number {
    return num1 + num2
}
```

### 基本类型和特殊类型

```typescript
/**
 * Types
 */

// Boolean, Number and String
let isDone: boolean = false
let decimal: number = 6
let hex: number = 0xf00d
let binary: number = 0b1010
let octal: number = 0o744
let colour: string = 'blue'

// Arrays
let list_n: number[] = [1, 2, 3]
let list_A: Array<number> = [1, 2, 3]

// Tuples
let x: [string, number]
x = ["Hello", 10]

// Enums
enum Color {
    Red,
    Green,
    Blue,
}

let c: Color = Color.Green
// 枚举从 0 开始, Red = 0, Green = 1, Blue = 2, 当然也可以自定义
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT",
}


// 特殊类型
const elem = document.getElementById('elementId')! as HTMLInputElement


// 多种类型
function combine(a: number | string, b: number | string): void {
    // logic to validate types and perorm operations
}


// 特定的字符串
function foo(color: 'yellow' | 'brown') {}


// 一个抛出异常的函数返回类型应该是什么？never
function error(msg: string): never {
    throw new Error("msg")
}

// 另外，如果函数不返回任何值应该声明为 void
function message(msg: string): void {
    console.log(msg)
}


// 如果不知道会返回什么类型的数据, 可以用 unknown 关键字
let input: unknown

// before assigning it we should check its type
if (typeof input === "string") {
    let name: string = input
}

// 除了在分配值之前检查类型外，我们甚至可以将类型转换为我们已知的类型
let myinput_0: unknown
let mylength_0: number = (<string>input).length
// or
let myinput_1: unknown
let mylength_1: number = (input as string).length


// 如果不希望 TypeScript 检查其类型，可以用 any
declare function getValue(key: string): any
const str: string = getValue("test")
```

### 接口

```typescript
/**
 * Interfaces
 */

// 接口定义对象
interface User {
    name: string
    age: number
}

function displayPersonalInfo(user: User) {
    console.log(`Name: ${user.name} - Age: ${user.age}`)
}


// 用修饰符，例如 ? 表示可以为 null，用 readonly 关键字设置属性不可变
interface Square {
    color?: string
    width?: number
}

interface Point {
    readonly x: number
    readonly y: number
}

let square: Square = {
    width: 14,
}

// readonly 关键字也可以用在其它类型上，例如 ReadonlyArray
let a: number[] = [1, 2, 3, 4]
let ronumbers: ReadonlyArray<number> = a

ronumbers[0] = 4 // WRONG! It cannot be assigned

// But it could be used for iterating over its values for reading purposes
for (const num of ronumbers) {
    console.log(num)
}
```

### 类

```typescript
/**
 * Classes
 */

class Rectangle {
    height: number
    width: number

    constructor(h: number, w: number) {
        this.height = h
        this.width = w
    }
}

const rectangle = new Rectangle(200, 10)

/** 
 * 在TypeScript中，还可以将 private，public，protected 和 static 用作类属性，虽然这些在 JavaScript 还没被支持，但是可以完美转译过去
 * 而且，TypeScript 也支持继承和抽象类
 */
```

### 泛型

```typescript
/**
 * Generics
 */

/**
 * Last but not least: 最后但同样重要的是，TypeScript 也支持泛型
 * 
 * 可重用组件是每种现代强类型编程语言的基础，一旦将强类型控制引入JavaScript，我们还必须为程序员提供一种方法，以定义将相同逻辑应用于不同类型数据的函数。
 * 
 * 对于那些来自诸如C ++，C＃，Kotlin，Java甚至Rust的语言的人，他们必须完全熟悉这个概念。
 * 
 * 对于其他开发人员，我们应该说泛型是一种声明数组，类或函数的方法，该数组，类或函数使用在声明过程中对它们未知的类型。 此通用类型由字母（通常为T）表示，并用大于和小于符号括起来
 * 
 * 可以使用任何字母，只要它们包含在<>中即可。 这些字母稍后在实现逻辑中用作标记，并在定义发生时由实际类型替换。
 */

function myMax<T>(x: T, y: T): T {
    return x > y ? x : y
}

let intMax = myMax<number>(12, 50)

console.log(intMax)
```
