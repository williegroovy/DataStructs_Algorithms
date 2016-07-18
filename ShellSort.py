'''
    Linked List Analysis

    O(n) ~ O(n^2)

    Since the list is pre-sorted, the final pass doesn't require many comparisons (or shifts).

    Marginally better than the Insertion Sort.
'''


def shellSort(alist):
    sublistcount = len(alist)//2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount //= 2


def gapInsertionSort(alist, start, gap):

    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
