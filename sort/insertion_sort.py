import sys


# array -> sorted array
def sort(arr):
    # if the length of the array is < 2 no sorting is required
    if len(arr) < 2:
        return arr

    sorted_array = []

    while len(arr) > 0:
        minimum = sys.maxsize
        for item in arr:  # find the smallest item in unsorted array
            if item < minimum:
                minimum = item
        arr.remove(minimum)  # remove the item from the unsorted array
        sorted_array.append(minimum)  # add the item to the sorted array

    return sorted_array


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 4, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# insertion sort:
# create an empty array [the sorted array]
# pick the smallest item in the unsorted array and append to the empty array
