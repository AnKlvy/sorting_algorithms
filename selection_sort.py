from common_decorator import print_sorting_result


@print_sorting_result
def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i]>arr[j]:
                min_i=j

        arr[i], arr[min_i] = arr[min_i], arr[i]

selection_sort()
