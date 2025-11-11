import random


def print_sorting_result(func):
    def wrapper():
        arr = [random.randrange(0, 22) for _ in range(10)]
        print("Array before sorting:\n", arr)
        func(arr)
        print("Array after sorting:\n", arr)
    return wrapper