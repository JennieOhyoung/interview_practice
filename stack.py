"""Implement a stack using list that includes the following operations
    - Stack(): creates stack
    - push(item): adds new item
    - pop(): remoes top item
    - peek(): returns top item w/out removing it
    - isEmpty(): tests to see if stack is empty
    - size(): returns number of items on stack
    - print
    Be able to reverse a string using stack
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def reverse(my_str):
    for ch in my_str:
        s.push(ch)
    rev_str = ""
    while not s.isEmpty():
        rev_str = rev_str + s.pop()
        # print rev_str
    return rev_str


s = Stack()
print reverse("hello world")
print s


