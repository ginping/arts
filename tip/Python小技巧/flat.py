def iter_x(x):
    if isinstance(x, dict):
        for key, value in x.items():
            yield (key, value)
    elif isinstance(x, list):
        for index, value in enumerate(x):
            yield (index, value)

def flat(x):
    for key, value in iter_x(x):
        if isinstance(value, (dict, list)):
            for k, v in flat(value):
                k = f'{key}_{k}'
                yield (k, v)
        else:
            yield (key, value)

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

d = {k: v for k, v in flat(nest_dict)}

from pprint import pprint
pprint(d)
