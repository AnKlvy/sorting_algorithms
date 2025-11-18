from common_decorator import print_sorting_result

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
    print("merge", left, right)
    sorted = []
    while True:
        if left[li] > right[ri]:
            sorted.append(right[ri])
            ri += 1
            print(li, ri, sorted)
            if ri == len(right):
                sorted.extend(left[li:])
                print("sorted (left >)", li, ri, sorted)
                return sorted
        else:
            sorted.append(left[li])
            li += 1
            print(li, ri, sorted)
            if li == len(left):
                sorted.extend(right[ri:])
                print("sorted (right >=)", li, ri, sorted)
                return sorted


l = [4,2,3,1,1,1]

print("\nEnd of merge sort", merge_sort(l))
