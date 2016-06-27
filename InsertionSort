'''
    Insertion Sort Analysis

    O(n^2)

    Because this is a shifting operation it requires a 1/3 of the processing work of an exchange.
    This has very good performance over a sort that exchanges.

'''


def insertionSort(alist):

    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)

print alist
