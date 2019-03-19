#!/bin/env python3


import sys


def revsort(a):

    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while (j >= 0 and a[j] < key):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


if __name__ == "__main__":

    n = int(input("n = "))

    if (n <= 0):
        sys.exit(1)

    a = []
    for i in range(n):
        a.append(int(input("a[{}] = ".format(i))))

    print("Before sorting:")
    print(a)
    revsort(a)
    print("After sorting:")
    print(a)
