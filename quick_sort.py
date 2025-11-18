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

l = [3,2,1,4,2,9,7,4,3,5,6,21,7]

print(quick_sort(l))