from heapq import heapify, heappop

if __name__ == '__main__':
    in_ = [20, 5, 7, 9, 2, 1, 23, 1000, -1, -2, 11, 32, 2]

    # to sort in ascending order
    heapify(in_)

    rv = []

    while in_:
        rv += [heappop(in_)]

    print(rv)

    # to sort in descending order
    in_ = [20, 5, 7, 9, 2, 1, 23, 1000, -1, -2, 11, 32, 2]
    in_ = [-1 * num for num in in_]
    heapify(in_)

    rv = []

    while in_:
        rv += [-heappop(in_)]

    print(rv)
