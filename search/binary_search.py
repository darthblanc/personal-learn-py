def binary_search(arr, target, start, end):
    if start > end:
        return False

    if start == end:
        if arr[start] == target:
            return True
        return False

    if arr[start] == target:
        return True

    if arr[end] == target:
        return True

    mid = (start + end) // 2

    if target > arr[mid]:
        return binary_search(arr, target, mid + 1, end)

    elif target == arr[mid]:
        return True

    else:
        return binary_search(arr, target, start, mid - 1)


#

if __name__ == '__main__':
    print(binary_search([1], 1, 0, len([1]) - 1))
    print(binary_search([1, 2], 1, 0, len([1, 2]) - 1))
    print(binary_search([1, 2, 3, 4, 5], 1, 0, len([1, 2, 3, 4, 5]) - 1))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) - 1))
