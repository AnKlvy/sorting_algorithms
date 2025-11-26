# O(n^2), 1954, Гарольд Х. Сьюард

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num + min_val] * freq)

    return arr


arr = [4, 2, 2, -6, -3, 3, -1, 6, 5, -2, 3]
counting_sort(arr)
print("Sorted array:", arr)
