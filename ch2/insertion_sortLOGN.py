#!/bin/env python3

import sys


def binary_search(a, e, low, high):
    if high <= low:
        return low + 1 if e > a[low] else low

    m = (high + low) // 2
    if a[m] > e:
        return binary_search(a, e, low, m - 1)
    if a[m] < e:
        return binary_search(a, e, m + 1, high)
    return m


def sort(a):

    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        loc = binary_search(a, key, 0, j)
        for t in range(i, loc, -1):
            a[t] = a[t - 1]
        a[loc] = key


if __name__ == "__main__":

    print(binary_search([1, 2, 3], 1, 0, 2))
    n = int(input("n = "))
    if (n < 0):
        sys.exit(1)

    a = []
    for i in range(n):
        a.append(int(input("a[{}] = ".format(i))))

    print("Before sorting:")
    print(a)
    sort(a)
    print("After sorting:")
    print(a)
