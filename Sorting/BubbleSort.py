from random import randint
from verification import verify_sort


# Complexity: O(N^2) 
def bubble_sort(data):
    for _ in range(len(data)):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


N = 10

data = [randint(1, N*2) for _ in range(N)]

print(data)
# verify_sort(bubble_sort, 10000)

print(bubble_sort(data))
