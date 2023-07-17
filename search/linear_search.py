# array, Any: val -> String
def find_status(arr, val):
    if search(arr, val):
        return f"found {val} in {arr}"
    return f"{val} NOT found in {arr}"


# array, Any: val -> boolean
def search(arr, val):
    for item in arr:
        if item == val:
            return True

    return False


print(find_status([1, 2, 3, 4, 5, 6, 7], 3))
print(find_status([6, 2, 3, 1, 7, 5, 10, 4, 8, 9], 2))
print(find_status([7, 6, 5, 4, 3, 2, 1], 11))
print(find_status([3, 2, 5, 4], 0))
print(find_status([1, 1, 1, 1, 1, 1], 5))
print(find_status([1], 0))
print(find_status([2, 2, 3, 4, 5, 5, 1, 8], 8))

# linear search:
# go through array linearly [eg: using loop]
