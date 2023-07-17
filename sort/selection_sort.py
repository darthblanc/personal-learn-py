import sys


def sort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    i = 0

    while len(arr[i:]) != 0:
        minimum = sys.maxsize
        min_index = len(arr)
        for j in range(i, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                min_index = j
        temp = arr[i]
        arr[i] = minimum
        arr[min_index] = temp
        i += 1

    return arr


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 4, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# selection sort:
# switch the first item in an array partition with the smallest item in the array partition
# when this is done reduce the partition to the unsorted partition
# continue until all items are sorted
