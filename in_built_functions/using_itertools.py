from itertools import combinations, permutations, product, chain

arr = ["1", "2", "3"]

# combinations gives the combinations of elements in a given array
# its second argument specifies the length of the combinations
print(list(combinations(arr, len(arr))))

# permutations gives the permutations of elements in a given array
# its second argument specifies the length of the permutations
print(list(permutations(arr, len(arr) - 1)))

# product may be used to find the cartesian product of two sets
# the cartesian product of (x , y) is all the combinations of points x and y
# from two separate sets of points X and Y
arr2 = ["4", "5", "6"]
arr3 = [""]
arr4 = [""]
print(list(product(arr, arr2, arr3, arr4)))

# if you want to use a set several times on itself use the repeat argument
print(list(product(arr, repeat=3)))

# if you need to combine more than one series of iterables together use chain
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6, 7]
print(list(chain(list1, list2)))

d1 = {1: 2, 3: 4}
d2 = {5: 6, 7: 8}
print(list(chain(d1, d2)))
# for dictionaries, it returns the keys
