#!/bin/env python3


def find(l, e):
    for i in l:
        if i == e:
            return True
    return False


if __name__ == "__main__":

    ls = [1, 2, 3, -1]
    print(find(ls, -1))
    print(find(ls, -2))
