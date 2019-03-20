#!/bin/env python3


def sum(a, b):
    c = [0] * (len(a) + 1)
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1 and b[i] == 1:
            c[i + 1] = carry
            carry = 1
        elif carry == 1 and (a[i] == 1 or b[i] == 1):
            c[i + 1] = 0
            carry = 1
        elif a[i] == 0 and b[i] == 0:
            c[i + 1] = carry
            carry = 0
        else:
            c[i + 1] = 1
    c[0] = carry
    return c


if __name__ == "__main__":
    a = [1, 1, 1]
    b = [0, 0, 1]

    print(sum(a, b))
