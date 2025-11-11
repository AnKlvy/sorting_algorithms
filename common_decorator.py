import random
from functools import wraps

def print_sorting_result(func):
    @wraps(func)
    def wrapper(arr=None, *args, **kwargs):
        if arr is None:
            arr = [random.randrange(0, 22) for _ in range(10)]
        print("Array before sorting:\n", arr)
        func(arr, *args, **kwargs)
        print("Array after sorting:\n", arr)
    return wrapper