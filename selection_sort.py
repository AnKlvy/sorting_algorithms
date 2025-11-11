import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[min_i]>arr[j]:
                min_i=j

        arr[i], arr[min_i] = arr[min_i], arr[i]

arr = [random.randrange(0, 22) for i in range(10)]

print(arr)

selection_sort(arr)

print(arr)