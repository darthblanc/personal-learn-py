# array, Any: val -> String
def find_status(arr, val):
    if search(arr, val):
        return f"found {val} in array"
    return f"{val} NOT found in array"


# array, Any: val -> boolean
def search(arr, val):
    if len(arr) == 0:
        return False

    elif len(arr) == 1:
        if arr[0] == val:  # check if item in the array is val
            return True
        return False

    mid = len(arr) // 2

    if arr[mid] == val:  # check if item in the middle of array is val
        return True

    return search(arr[:mid], val) or search(arr[mid:], val)


print(find_status([1, 2, 3, 4, 5, 6, 7], 3))
print(find_status([6, 2, 3, 1, 7, 5, 10, 4, 8, 9], 2))
print(find_status([7, 6, 5, 4, 3, 2, 1], 11))
print(find_status([3, 2, 5, 4], 0))
print(find_status([1, 1, 1, 1, 1, 1], 5))
print(find_status([1], 0))
print(find_status([2, 2, 3, 4, 5, 5, 1, 8], 8))

# binary search:
# divide array in half each time until you get to one item
# if item is found return True
# else return False
