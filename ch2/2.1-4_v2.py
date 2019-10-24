#!/bin/env python3


def sum(a, b):
    n = len(a) + 1 if len(a) > len(b) else len(b) + 1
    c = [0] * n
    carry = 0
    i = len(c) - 1
    j = len(a) - 1
    k = len(b) - 1
    while i > -1:
        if j > -1 and k >  -1:
            c[i] = (a[j] + b[k] + carry) % 2
            carry = (a[j] + b[k] + carry) // 2
        elif j == -1 and k == -1:
            c[i] = carry
        elif j == -1:
            c[i] = (b[k] + carry) % 2
            carry = (b[k] + carry) // 2
        else:
            c[i] = (a[j] + carry) % 2
            carry = (a[j] + carry) // 2
        if j > -1:
            j -= 1
        if k > -1:
            k -= 1

        i -= 1
    return c


if __name__ == "__main__":
    a = [1, 0]
    b = [1, 0, 1]

    print(sum(a, b))
