def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inversions_left = merge_sort(arr[:mid])
    right, inversions_right = merge_sort(arr[mid:])
    merged, inversions = merge(left, right)

    return merged, inversions + inversions_left + inversions_right

def merge(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

# Example usage
arr = [1, 3, 2, 5, 4]
inversions = count_inversions(arr)
print("Number of inversions:", inversions)
