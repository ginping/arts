def flat(deep_list, result=[]):
    for item in deep_list:
        if isinstance(item, list):
            flat(item, result)
        else:
            result.append(item)
    return result

deep_list = [1, 2, [3, 4, [5, 6, 7], 8], 9, [10, 11]]
print('deep_list: ', deep_list)
result = flat(deep_list)
print('flat result: ', result)


def flat_gen(deep_list):
    for item in deep_list:
        if isinstance(item, list):
            yield from flat_gen(item)
        else:
            yield item

result_gen = [x for x in flat_gen(deep_list)]
print('flat result gen: ', result_gen)

