from common_decorator import print_sorting_result
@print_sorting_result
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = []
    right = []
    equals= []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equals.append(x)

    return [*quick_sort(left), *equals, *quick_sort(right)]

quick_sort()