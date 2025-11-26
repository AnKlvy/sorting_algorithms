from collections import defaultdict


def counting_sort(arr):
    count_of_nums = defaultdict(int)
    min_num=arr[0]
    max_num=arr[0]
    for i in range(len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
        if max_num < arr[i]:
            max_num = arr[i]
        count_of_nums[arr[i]]+=1
    print(dict(sorted(count_of_nums.items())))

    for num in range(min_num, max_num):
        count_of_nums[num+1] = count_of_nums[num] + count_of_nums[num+1]
    print("after cumulative amount:")
    print(dict(sorted(count_of_nums.items())))

    print(arr)
    sorted_output = [0 for _ in range(len(arr))]
    print(sorted_output)
    for num in arr:
        print(num, ':', count_of_nums[num])
        sorted_output[count_of_nums[num]-1] = num
        count_of_nums[num] -= 1


    print("Finally:", sorted_output)
    arr[:] = sorted_output

arr = [3,4,-3,-8,5,6,-3,2,5]
counting_sort(arr)

print(arr)
