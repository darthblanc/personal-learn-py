import heapq

# initialize an array
arr = [1, 10, 3, 4, 6, 7]
# heapify the array, note this returns nothing
heapq.heapify(arr)

# add an item to arr, but preserving the heap properties
heapq.heappush(arr, 0)

# remove the smallest item in the list whilst maintaining the heap properties
heapq.heappop(arr)

# find the n largest numbers in a dataset, opposite of nsmallest
print(heapq.nlargest(4, arr))

# pop the smallest element and replace it with another value whilst maintaining heap properties
heapq.heapreplace(arr, -1)
print(arr)
