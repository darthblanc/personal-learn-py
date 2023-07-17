import sys


# array -> sorted array
def sort(arr):
    # if the length of the array is < 2 no sorting is required
    if len(arr) < 2:
        return arr

    i = 0

    while len(arr[i:]) != 0:  # continue until size of unsorted partition is 0
        minimum = sys.maxsize  # biggest int in python
        min_index = len(arr)
        for j in range(i, len(arr)):
            if arr[j] < minimum:  # find the smallest number in unsorted partition
                minimum = arr[j]
                min_index = j
        # switch first element in unsorted partition with the smallest number in the partition
        temp = arr[i]
        arr[i] = minimum
        arr[min_index] = temp
        # reduce the size of the sorted partition
        i += 1

    return arr


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 4, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# selection sort:
# switch the first item in an array partition with the smallest item in the array partition
# when this is done reduce the partition to the unsorted partition
# continue until all items are sorted
