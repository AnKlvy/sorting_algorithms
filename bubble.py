from common_decorator import print_sorting_result

# O(n^2), 1838, Чарльз Бэббидж

@print_sorting_result
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort()