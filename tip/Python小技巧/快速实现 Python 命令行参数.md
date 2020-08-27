# 快速实现 Python 命令行参数

## 背景

有时候需要在使用 Python 开发一些命令行工具，并在运行命令的时候指定一些参数，例如：

```bash
python serve.py --host localhost --port 8888
```

对于简单的，只有几个参数的工具，我们可以使用 `sys.argv` 来获取。

`sys.argv` 列表第一个值是文件名，后面是命令行传入的参数。

例如：

```bash
python arg.py a b c 2 3

# ['arg.py', 'a', 'b', 'c', '2', '3']
```

如果还需要在参数里面输出帮助信息，并且同时兼顾两种格式：

```bash
python serve.py --name=ph --age=24

python serve.py --name ph --age 24
```

## 实践

使用 `fire` 这个库。

`arg.py`:

```Python
import fire

def intro(name, age):
    print(f'我的名字是：{name}, 我的年龄是：{age}')

if __name__ == '__main__':
    fire.Fire(intro)
```

这段代码支持三种调用方法：

```bash
$ python arg.py ph 24
# 我的名字是：ph, 我的年龄是：24

$ python arg.py --name ph --age 24
# 我的名字是：ph, 我的年龄是：24

$ python arg.py --name=ph --age=24
# 我的名字是：ph, 我的年龄是：24
```

如果某些参数可要可不要，在函数传参时使用默认参数即可。

```Python
def intro(name='ph', age=24):
    print(f'我的名字是：{name}, 我的年龄是：{age}')
```

