from random import randint
from verification import verify_sort


# Complexity is O(N^2), though better than classical 2 nested loops algorithms
# Actual complexity is (n(n+1))/2


def insertion_sort(array):
    for i in range(1, len(array)):
        # print(array)
        for j in range(len(array[:i])):
            if array[j] >= array[i]:
                val = array[i]
                del array[i]
                array.insert(j, val)
    return array


N = 10

data = [randint(1, N*2) for _ in range(N)]

print(data)
# verify_sort(insertion_sort, 50000)
print(insertion_sort(data))
