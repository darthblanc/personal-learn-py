# array -> boolean
def not_monotonic(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return True

    return False


# array -> sorted array
def sort(arr):
    # if the length of the array is < 2 no sorting is required
    if len(arr) < 2:
        return arr

    while not_monotonic(arr):  # continue until array is monotonic increasing
        for i in range(1, len(arr)):
            # swap items in list
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp

    return arr


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# switch items in array
# keep doing this until function is sorted
