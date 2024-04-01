import unittest

def partition(arr, s, e):
    if e <= s:
        return
    pivot = arr[s]
    i = s + 1
    for j in range(i, e+1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    arr[i-1], arr[s] = arr[s], arr[i-1]
    partition(arr, s, i-1)
    partition(arr, i, e)
    
def sort(arr):
    partition(arr,0,len(arr)-1)


class TestClass(unittest.TestCase):
    def test_sorted_ascending(self):
          test_arr = [1, 2, 3, 4, 5, 6, 7]
          sort(test_arr)
          self.assertEqual(test_arr, [1, 2, 3, 4, 5, 6, 7])
    
    def test_sorted_descending(self):
        test_arr = [1, 2, 3, 4, 5, 6, 7][::-1]
        sort(test_arr)
        self.assertEqual(test_arr, [1, 2, 3, 4, 5, 6, 7])

    def test_random(self):
        test_arr = [4,7,1,3,6,8,5,2]
        sort(test_arr)
        self.assertEqual(test_arr, [1, 2, 3, 4, 5, 6, 7,8])

unittest.main()