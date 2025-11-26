# O(n log(n)), 1945, Джон Фон Нейман

def merge_sort(arr):
    if len(arr) == 1:
        print(arr)
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    print(left, right)
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    li = 0
    ri = 0
    sorted_arr = []
    print("merge", left, right)
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            sorted_arr.append(left[li])
            li += 1
        else:
            sorted_arr.append(right[ri])
            ri += 1
        print(li, ri, sorted_arr)


    sorted_arr.extend(left[li:])
    sorted_arr.extend(right[ri:])
    print("sorted", li, ri, sorted_arr)

    return sorted_arr

l = [7, 56, 56, 3, 1, 1, 56, 2, 3, 4, 1]

print("\nEnd of merge sort", merge_sort(l))
