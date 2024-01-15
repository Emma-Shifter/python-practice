from collections.abc import Iterable

def invert(sequence: Iterable) -> list:
    res = []
    for i in sequence:
        if (isinstance(i, Iterable)): res += invert(i)
        else: res.append(i)
    return res

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(invert(nice_list))