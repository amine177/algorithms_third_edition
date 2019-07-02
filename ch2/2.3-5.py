def search(a, e):
    if len(a) == 1:
        if a[0] == e:
            return True
        if a[0] != e:
            return False
    if a[len(a)//2] > e:
        return search(a[0 : len(a) // 2 + 1], e)
    elif a[len(a)//2] < e:
        return search(a[len(a) // 2 : len(a)], e)
    else:
        return True

if __name__ == "__main__":
    print(search([1, 2, 3], 2))
