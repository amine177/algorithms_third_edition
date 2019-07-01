def merge(a, p, q, r):
    i = p
    j = q + p - i + 1
    ret = [None] * (r - p + 1)
    k = 0
    while i <= q and j <= r:
        if a[i] > a[j]:
            ret[k] = a[j]
            j += 1
        else:
            ret[k] = a[i]
            i += 1
        k += 1

    while i <= q:
        ret[k] = a[i]
        i += 1
        k += 1
        
    while j <= r:
        ret[k] = a[j]
        j += 1
        k += 1

    return ret


def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        left = merge_sort(a[0 : len(a)//2])
        right = merge_sort(a[len(a)//2 : len(a)])
        return merge(left + right, 0, len(left) - 1, len(a) - 1)


if __name__ == "__main__":
    print(merge_sort([1, 4, 2]))




