#!/bin/env python3


def selection_sort(a):

    for i in range(0, len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        if (min_index != i):
            a[i], a[min_index] = a[min_index], a[i]


if __name__ == "__main__":
    a = [2, -1, 3, -22]
    print(a)
    selection_sort(a)
    print(a)
