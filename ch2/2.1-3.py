#!/bin/env python3


def find(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return i
    return None


if __name__ == "__main__":

    ls = [1, 2, 3, -1]
    print(find(ls, -1))
    print(find(ls, -2))
