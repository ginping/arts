# 使用 yield 压平多层嵌套字典列表混合数据

## 背景

有时候会遇到多层嵌套字典列表混合数据并需要将其压扁。

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
    'j': {'k': {'l': {'m': 8}}},
    'n': [1, {'o': 1, 'p': [1, 2, 3], 'q': {'r': {'s': 100}}}, 3, [1, 2, 3], 5]
}
```

需要将其压扁为：

```python
{
    'a': 1,
    'b_c': 2,
    'b_d': 3,
    'b_e_f': 4,
    'g_h': 5,
    'i': 6,
    'j_k_l_m': 8,
    'n_0': 1,
    'n_1_o': 1,
    'n_1_p_0': 1,
    'n_1_p_1': 2,
    'n_1_p_2': 3,
    'n_1_q_r_s': 100,
    'n_2': 3,
    'n_3_0': 1,
    'n_3_1': 2,
    'n_3_2': 3,
    'n_4': 5
 }
```

## 实践

只需要将列表的索引作为 key 遍历出来就可以和遍历字典一样处理了。因此编写遍历字典列表函数：

```python
def iter_x(x):
    if isinstance(x, dict):
        for key, value in x.items():
            yield (key, value)
    elif isinstance(x, list):
        for index, value in enumerate(x):
            yield (index, value)
```

改造 falt 函数遍历字典部分代码：

```python
def flat(x):
    for key, value in iter_x(x):
        if isinstance(value, (dict, list)):
            for k, v in flat(value):
                k = f'{key}_{k}'
                yield (k, v)
        else:
            yield (key, value)
```

