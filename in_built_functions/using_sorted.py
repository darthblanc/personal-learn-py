# sorted takes three parameters -> the list, the key to sort by, reverse
# the last two are optional

# sort a regular array
arr = [1, 4, 3, 2]
print(sorted(arr, reverse=True))

# sort a 2d array by its second value
arr = [[1, 2], [3, 4], [7, 1], [5, 5]]
print(sorted(arr, key=(lambda item: item[1])))

# sort a dictionary by value in descending order
d = {1: 2, 3: 4, 7: 1, 5: 5}
print(sorted(d, key=(lambda k: d[k]), reverse=True))

