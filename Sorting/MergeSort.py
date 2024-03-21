from random import randint
from math import floor


N = 10


def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_sort(data):
    if len(data) < 2:
        return data
    if len(data) > 2:
        divide_point = floor(len(data)/2)
        a = merge_sort(data[0:divide_point])
        b = merge_sort(data[divide_point:len(data)])
        return merge(a, b)
    return data if data[0] < data[1] else data[::-1]


data = [randint(1, N*2) for _ in range(N)]

print(data)

print(merge_sort(data))
