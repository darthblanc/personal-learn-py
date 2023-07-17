import sys


def sort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    sorted_array = []

    while len(arr) > 0:
        minimum = sys.maxsize
        for item in arr:
            if item < minimum:
                minimum = item
        arr.remove(minimum)
        sorted_array.append(minimum)

    return sorted_array


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 4, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# insertion sort:
# create an empty array [the sorted array]
# pick the smallest item in the unsorted array and append to the empty array
