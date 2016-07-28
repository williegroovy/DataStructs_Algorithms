def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] is item:
            found = True
        else:
            pos += 1

    return found


testList = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print sequentialSearch(testList, 3)
print sequentialSearch(testList, 13)