from random import randint
from math import floor


def process_pivot(array, pivot_pos):
    if len(array)<2:
        return array
    left_arr = []
    right_arr = []
    prev_pivot = array[pivot_pos]
    del array[pivot_pos]
    for val in array:
        if val < prev_pivot:
            left_arr.append(val)
        if val >= prev_pivot:
            right_arr.append(val)
    
    left_arr = process_pivot(left_arr, len(left_arr)-1)
    right_arr = process_pivot(right_arr, len(right_arr)-1)
    return left_arr + [prev_pivot] + right_arr
    


def quick_sort(array):
    return process_pivot(array, len(array)-1)



N = 10

data = [randint(1, N*2) for _ in range(N)]

print(data)

print(quick_sort(data))
