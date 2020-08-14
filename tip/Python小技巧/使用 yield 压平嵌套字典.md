# 使用 yield 压平嵌套字典

## 背景

有时候会遇到字典嵌套字典的数据并需要将其压扁。

例如：

```python
nest_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': 3,
        'e': {'f': 4}
    },
    'g': {'h': 5},
    'i': 6,
    'j': {'k': {'l': {'m': 8}}}
}
```

需要将其压扁为：

```python
{
    'a': 1,
    'b_c'： 2，
    'b_d': 3,
    'b_e_f': 4,
    'g_h': 5,
    'i': 6,
    'j_k_l_m': 8
}
```

## 实践

要把这个嵌套字典压扁，可以从下向上来处理字段。例如对于 `b -> e -> f -> 4` 这条路径，可以把最里面的 `{'f': 4}` 转换为一个元组 `('f': 4)`。然后把这个元组向上抛，于是得到元组 `('e': ('f', 4))`。把 `e` 拼接到 `f` 的前面，变为：`('e_f', 4)`，继续往上抛出，得到 `('b', ('e_f', 4))`。再把 `b` 拼接到 `e_f` 上面，得到`('b_e_f', 4)`。完成一条线路的组装。

这个逻辑用 `yield` 关键字来实现：

```python
def flat(x):
    for key, value in x.items():
        if isinstance(value, dict):
            for k, v in flat(value):
                k = f'{key}_{k}'
                yield (k, v)
        else:
            yield (key, value)
```

```python
In [11]: {k: v for k, v in flat(nest_dict)}
Out[11]: {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'g_h': 5, 'i': 6, 'j_k_l_m': 8}
```

