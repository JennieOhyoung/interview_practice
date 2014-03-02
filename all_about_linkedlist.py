"""
Implement a linked list that can perform the following:
    - print (constructor and method)
    - add 
    - insert (by index)
    - delete (by index and value)
    - search
    - find size
    - is empty
    - check for circular linked list

Write functions to:
    - delete duplicate nodes in linked list
    - make random linked list
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.visited = False

    def __str__(self):
        printed = []
        i = 0
        current = self.head
        while i < self.size():
            printed.append(str(current.data))
            current = current.next
            i += 1
        return " -> ".join(printed)

    def prnt(self):
        printed = []
        current = self.head
        while current != None:
            printed.append(current.data)
            current = current.next
        return printed

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node

    def insert(self, data, index):
        new_node = Node(data)
        count = 0 
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                count += 1
                if count == index:
                    new_node.next = current.next
                    current.next = new_node

    def delete_val(self, data):
        if self.head != None:
            current = self.head
            while current.next != None:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next       

    def delete_index(self, index):
        count = 0
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                count += 1
                if count == index-1:
                    current.next = current.next.next

    def search(self, value):
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                if current.data == value:
                    return True
            return False

    def size(self):
        size = 0
        if self.head != None:
            current = self.head
            size += 1
            while current.next != None:
                current = current.next
                size += 1
        return size

    def is_empty(self):
        return self.head == None

    def circular_flat(self):
        if self.head:
            current = self.head
            while current:
                if current.visited == True:
                    return True
                current.visited = True
                current = current.next
        return False

    def circular_slow_fast(self):
        slow = self.head
        flast = self.head

        while fast != None:
            slow = slow.next
            if slow == fast:
                return True
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            return False

def delete_duplicates(linkedlist):
    if linkedlist.head != None:
        current = linkedlist.head
        d = {current.data: 0}
        while current.next != None:
            if current.next.data in d:
                current.next = current.next.next
            else:
                d[current.next.data] = 0
                current = current.next

from random import randint
def make_random_ll(length, min_val, max_val):
    linkedlist = Linked_List()
    for i in range(length):
        random = randint(min_val, max_val)
        linkedlist.add(random)
    return linkedlist




l = Linked_List()
for x in range(1, 21):
    l.add(x)

l.add(3)
l.add(10)
# l.insert("a", 2)
# l.delete_val(5)
# print l.search(25)
# print l.size()
# print l.is_empty()
delete_duplicates(l)
print l.prnt()
print make_random_ll(10,1,35)


























