from random import randint
from verification import verify_sort


# Complexity is  O(N^2), though technicaly better, since it skips some of the inner loops
# Actual complexity is (n(n+1))/2
def selection_sort(array):
    for i in range(len(array)):
        lowest_pos = 0
        lowest_val = array[i]
        for j in range(i, len(array)):
            if array[j] <= lowest_val:
                lowest_val = array[j]
                lowest_pos = j

        array[i], array[lowest_pos] = array[lowest_pos], array[i]
    return array


N = 10

data = [randint(1, N*2) for _ in range(N)]

print(data)
verify_sort(selection_sort, 50000)
print(selection_sort(data))


