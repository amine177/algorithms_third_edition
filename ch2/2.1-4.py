#!/bin/env python3 


def sum(a, b):
    c = [0] * (len(a) + 1)
    carry = 0
    for i in range(0, len(a), -1):
        if a[i] == 1 and b[i] == 1:
            c[i] = carry
            carry = 1
        elif carry == 1 and (a[i] == 1 or b[i] == 1):
            c[i] = 0
            carry = 1
        elif a[i] == 0 and b[i] == 0:
            c[i] = carry
            carry = 0
        else:
            c[i] = 1
        c[0] = carry
        return c
