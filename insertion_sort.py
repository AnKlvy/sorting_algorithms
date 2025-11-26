from common_decorator import print_sorting_result

# O(n^2), 1945, Джон Фон Нейман
@print_sorting_result
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

insertion_sort([7, 56, 3, 1, 1, 2, 3, 4, 1])