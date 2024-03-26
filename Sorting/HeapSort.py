from random import randint
from verification import verify_sort


# Complexity is O(N*logN)


def heapify(array, N, i):
    largest = i 
    left_node = 2 * i + 1 
    right_node = 2 * i + 2 

    if left_node < N and array[left_node] > array[largest]:
        largest = left_node

    if right_node < N and array[right_node] > array[largest]:
        largest = right_node

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        array = heapify(array, N, largest)
    return array
    

def heap_sort(array):
    for i in range(len(array)//2 - 1, -1, -1):
        array = heapify(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        array = heapify(array, i, 0)
    return array


N = 6

data = [randint(1, N*2) for _ in range(N)]

print(data)
# verify_sort(heap_sort, 5000)
print(heap_sort(data))
