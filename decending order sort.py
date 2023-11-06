def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_descending(left_half)
    right_half = merge_sort_descending(right_half)

    return merge_descending(left_half, right_half)

def merge_descending(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_descending = merge_sort_descending(arr)
print(sorted_descending)
