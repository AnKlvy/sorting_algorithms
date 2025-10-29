def bubble_sort(arr):
    if len(arr)==1:
        return arr
    temp = arr[0]

    for i in range(1, len(arr)):
        if temp > arr[i]:
            arr[i-1]=arr[i]
            arr[i]=temp
        elif temp < arr[i]:
            temp = arr[i]
    return [*bubble_sort(arr[:-1]), arr[-1]]


l = [2,3,4, 5, 1, 2,7,1]

print(bubble_sort(l))