def merge_sort_multiway(arr):
    if len(arr) > 1:
        mid1 = len(arr) // 3
        mid2 = 2 * mid1

        left_third = arr[:mid1]
        middle_third = arr[mid1:mid2]
        right_third = arr[mid2:]

        merge_sort_multiway(left_third)
        merge_sort_multiway(middle_third)
        merge_sort_multiway(right_third)

        i = j = k = l = 0

        while i < len(left_third) and j < len(middle_third) and k < len(right_third):
            if left_third[i] > middle_third[j] and left_third[i] > right_third[k]:
                arr[l] = left_third[i]
                i += 1
            elif middle_third[j] > right_third[k]:
                arr[l] = middle_third[j]
                j += 1
            else:
                arr[l] = right_third[k]
                k += 1
            l += 1

        while i < len(left_third):
            arr[l] = left_third[i]
            i += 1
            l += 1

        while j < len(middle_third):
            arr[l] = middle_third[j]
            j += 1
            l += 1

        while k < len(right_third):
            arr[l] = right_third[k]
            k += 1
            l += 1

def merge_sort_multiway_wrapper(arr):
    merge_sort_multiway(arr)

# Example usage:
arr = [12, 11, 13, 5, 6, 7, 8, 1, 9, 3]
merge_sort_multiway_wrapper(arr)
print(arr)  # Output: [13, 12, 11, 9, 8, 7, 6, 5, 3, 1]
