# Define a method on linked list return True if list is circular.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.visited = False
# solution #1, set flag
    def circular_flag():
        if self.head:
            current = self.head
            while current:
                if current.visited == True:
                    return True
                current.visited = True
                current = current.next
        retur False

    def circular_slow_fast():
        slow = self.head
        fast = self.head

        while fast != None:
            slow = slow.next
            if slow == fast:
                return True
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
        return False