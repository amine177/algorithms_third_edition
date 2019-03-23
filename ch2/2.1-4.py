#!/bin/env python3


def sum(a, b):
    c = [0] * (len(a) + 1)
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        c[i + 1] = (a[i] + b[i] + carry) % 2
        if (a[i] + b[i] + carry) > 1:
            carry = 1
        else:
            carry = 0
    c[0] = carry
    return c


if __name__ == "__main__":
    a = [1, 0, 1]
    b = [0, 0, 1]

    print(sum(a, b))
