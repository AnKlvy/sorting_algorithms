def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

l = [2,3,4, 5, 1, 2,7,1]

print(bubble_sort(l))