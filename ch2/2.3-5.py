def search(a, e, begin, end):
    if begin == end:
        if a[end] != e:
            return False
        else:
            return True
    middle = (begin + end) // 2
    if a[middle] > e:
        return search(a, e, begin, middle)
    elif a[middle] < e:
        return search(a, e, middle, end)

if __name__ == "__main__":
    print(search([1, 2, 3], -1, 0, 2))
