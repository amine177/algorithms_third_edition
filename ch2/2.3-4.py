def insertion_sort(a):
    if len(a) <= 1:
        return a
    else:
        a = insertion_sort(a[0:len(a) - 1]) + [a[len(a) - 1]]
        temp = a[len(a) - 1]
        i = len(a) - 2
        print(i)
        while i >= 0 and a[i] > temp:
            a[i + 1] = a[i]
            i -= 1
        a[i+1] = temp
        return a


if __name__ == "__main__":
    print(insertion_sort([1, 3, 2]))

