#2.1 Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?
class Nodes(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def linked_list(self):
        self.head = None
        self.tail = None
    def remove_dup(self):
        if self.head != None:
            current = self.head
            dic = {current.data: True}
            while current.next != None:
                if current.next.data in dic:
                    current.next = current.next.next
                else:
                    dic[current.next.data] = True
                    current = current.next
    def remove_dup2(self):
        if self.head != None:
            current = self.head




#2.2 Implement an algorithm to find the kth to last element of a singly linked list.


#2.3 Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.


#2.4 Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.


#2.5 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. WRite a function that adds the two numbrs and returns the sum as linked list


#2.6 Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.


#2.7 Implement a function to check if a linked list is a palindrome.