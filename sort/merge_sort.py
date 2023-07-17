def merge(left, right):
    for i in range(len(right)):
        for j in range(len(left)):
            if right[i] <= left[j]:
                left.insert(j, right[i])
                break
            elif j == len(left) - 1:
                left.append(right[i])
                break
            else:
                continue

    return left


def sort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr

    mid = len(arr) // 2

    return merge(sort(arr[:mid]), sort(arr[mid:]))


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# merge sort:
# divide array into 0, 1, 2 or item arrays [divide]
# if the length of the array is two -> do a mini sort if necessary
# use a merge [insertion sort] step to create sorted array [conquer]
