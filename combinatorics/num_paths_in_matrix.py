import math


# how do we find the number of paths from the top left to the bottom right position in a matrix/grid
# if we can only move down and right
# mathematically,
# we can think of the directions taken as a word
# the word changes throughout only in the arrangement of the directions taken
# thus, we can calculate the number of paths as the number of arrangements of the word

def mathematical(n, m):
    return math.factorial(n + m - 2) // (math.factorial(n - 1) * math.factorial(m - 1))


# def recursively(n, m):
#     ...

if __name__ == '__main__':
    print(mathematical(3, 2))
