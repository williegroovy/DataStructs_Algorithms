def quick_sort(alist):

    qsh(alist, 0, len(alist)-1)


def qsh(alist, start, end):

    if start < end:

        split = part(alist, start, end)

        qsh(alist, start, split - 1)
        qsh(alist, split + 1, end)


def part(alist, start, end):

    pivot = alist[start]
    left = start + 1
    right = end

    done = False

    while not done:

        while left <= right and alist[left] < pivot:
            left += 1

        while alist[right] > pivot and left <= right:
            right -= 1

        if left > right:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]

    alist[start], alist[right] = alist[right], alist[start]

    return right


def bubble_sort(alist):

    swaps = True
    passnum = len(alist)-1

    while passnum > 0 and swaps:

        swaps = False

        for i in range(passnum):
            if alist[i] > alist[i+1]:
                swaps = True
                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum -= 1


def merge_sort(alist):

    if len(alist) > 1:

        mid = len(alist) // 2

        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while len(left_half) > i and len(right_half) > j:

            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1

            k += 1

        while len(left_half) > i:
            alist[k] = left_half[i]
            i += 1
            k += 1

        while len(right_half) > j:
            alist[k] = right_half[j]
            j += 1
            k += 1


def binary_search(alist, search):

    start = 0
    end = len(alist)

    found = False

    while start <= end and not found:

        mid = (start + end) // 2

        if alist[mid] is search:
            found = True
        else:
            if alist[mid] > search:
                end = mid - 1
            else:
                start = mid + 1

    return found


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

quick_sort(alist)
bubble_sort(alist2)
merge_sort(alist3)

print alist
print alist2
print alist3

print binary_search(alist2, 31)
print binary_search(alist2, 27)
print binary_search(alist2, 17)
print binary_search(alist2, 93)
print binary_search(alist2, 3)
