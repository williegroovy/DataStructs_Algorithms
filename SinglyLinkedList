'''
    Linked List Analysis

    -isEmpty:   O(1)
    -length:    O(n)
    -UOsearch:  0(1)
    -Osearch:   0(n)
    -add:       O(n)
    -remove:    O(n)

    Linked List are typically better than arrays when the use case is quickly inserting data.
'''


class Node:

    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() is item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

print("---------")
print(" Ordered ")
print("---------")

myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)

print(myList.size())
print(myList.search(93))
print(myList.search(100))

myList.add(100)
print(myList.search(100))
print(myList.size())

myList.remove(54)
print(myList.size())
myList.remove(93)
print(myList.size())
myList.remove(31)
print(myList.size())
print(myList.search(93))

print("---------")
print(" Ordered ")
print("---------")

print("---------")
print("Unordered")
print("---------")

myList = OrderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)

print(myList.size())
print(myList.search(93))
print(myList.search(100))

myList.add(100)
print(myList.search(100))
print(myList.size())

myList.remove(54)
print(myList.size())
myList.remove(93)
print(myList.size())
myList.remove(31)
print(myList.size())
print(myList.search(93))

print("---------")
print("Unordered")
print("---------")

# No support for catching edge cases if item is being deleted does not exist.
