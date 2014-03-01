"""
Implement a function that checks whether a string is a palindrome using a deque.
"""

class Deque(object):
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def is_empty(self):
        return self.items == []
    def add_back(self,item):
        self.items.insert(0,item)
    def add_front(self, item):
        self.items.append(item)
    def remove_back(self):
        return self.items.pop(0)
    def remove_front(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def palindrome(string):
    deque = Deque()
    for char in string:
        deque.add_front(char)

    still_equal = True

    while deque.size() > 1 and still_equal:
        front = deque.remove_front()
        back = deque.remove_back()
        if front != back:
            still_equal = False
    return still_equal



s1 = "radar"
s2 = "kayak"
s3 = "false"
print palindrome(s1)
print palindrome(s2)
print palindrome(s3)








