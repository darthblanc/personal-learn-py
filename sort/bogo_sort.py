import random


def not_monotonic(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return True

    return False


def sort(arr):
    while not_monotonic(arr):
        random.shuffle(arr)

    return arr


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# shuffle array till it is sorted
