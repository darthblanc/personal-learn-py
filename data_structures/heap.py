class MyHeap:
    def __init__(self, manager):
        self.manager = manager

    def heapify(self):
        for j in range(len(self.manager)):
            for i in range(len(self.manager) - 1, -1, -1):
                if self.manager[i] > self.manager[i // 2]:
                    self.manager[i], self.manager[i // 2] = self.manager[i // 2], self.manager[i]

        return arr

    def add(self, item):
        pass

    def heappop(self):
        rv = self.manager[0]
        self.manager = self.manager[1:]
        self.heapify()
        return rv

    def __len__(self):
        return len(self.manager)

    def __str__(self):
        rv = ""

        for item in self.manager:
            rv += f"{item}, "

        rv = rv[:-2]

        return "[" + rv + "]"


def heapsort(manager):
    rv = []

    while manager:
        rv += [manager.heappop()]

    return rv

arr = []
# arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
arr = MyHeap(arr)
print(arr.heapify())
print(heapsort(arr))
print()
