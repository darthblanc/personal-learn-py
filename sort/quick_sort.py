def sort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    greater = []
    equal = []
    lesser = []
    pivot = arr[0]

    for item in arr:
        if item > pivot:
            greater.append(item)
        elif item < pivot:
            lesser.append(item)
        else:
            equal.append(item)

    return sort(lesser) + equal + sort(greater)


print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([4, 2, 3, 1, 5, 6, 7]))
print(sort([7, 6, 5, 4, 3, 2, 1]))

# quick sort:
# divide array into 3 sections > pivot | == pivot | < pivot [divide]
# recursively divide for each section [no need to do so for == section]
# then combine all the sections [conquer]
