# Given a class Linked_list(), inserting node at position after i
# 6b. delete a node
# 6c. print as list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(data, i):
        new_node = Node(data)
        counter = 0
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                counter += 1
                if counter == i:
                    new_node.next = current.next
                    current.next = new_node

    def delete(self, i):
        counter = 0
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                counter += 1
                if counter == i-1:
                    current.next = current.next.next

    def prnt(self):
        l = []
        if self.head != None:
            current = self.head
            while current.next != None:
                l.append(current.data)
        print l



