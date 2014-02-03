# Given a class Linked_list(), define a method that adds a new node to the end of a linked list. Assume there are no loops in the list

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def add(data):
        # add new node, if there is a head then start from head. while not at end of list, set current node to next node (traversal), then set the current.next to new node(add)
        new_node = Node(data)
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

