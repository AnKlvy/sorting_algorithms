from common_decorator import print_sorting_result


@print_sorting_result
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp_v = arr[i]
        print('---------------------\n',i, ' iteration')
        for j in range(i-1, -1, -1):
            print('compare ', j,':',arr[j], ' and ', i,':',arr[i])
            if arr[j] < temp_v or arr[j]==temp_v:
                arr[j+1]=temp_v
                print('Array if  j < temp:\n', arr)
                break

            if arr[j] > temp_v:
                arr[j+1]=arr[j]
                if j==0:
                    arr[j]=temp_v
                print('Array if  j > temp:\n', arr)



insertion_sort([7,56,3,1,1,2,3,4,1])
