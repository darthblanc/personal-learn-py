def dfs(arr, acc):
    if len(acc) == num:
        acc.sort()
        return [acc]

    p = []

    for x in in_:
        if x not in acc:
            p += [[x]] + dfs(arr, acc + [x])

    return p


def clean(arr):
    arr = map(tuple, dfs(arr, []))
    return set(filter(lambda k: len(k) == num, tuple(arr)))


in_ = [1, 2, 3, 4]
num = 1

# use a dfs
print(clean(in_))
