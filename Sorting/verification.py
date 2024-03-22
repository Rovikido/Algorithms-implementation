from random import randint


def verify_sort(func, itterations, N=10):
    for _ in range(itterations):
        data = [randint(1, N*2) for _ in range(N)]
        sorted_data = func(data)
        if sorted_data != sorted(data):
            raise ValueError(f"Found error in array {data}\nResult: {sorted_data}")