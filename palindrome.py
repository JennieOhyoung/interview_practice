

# Given a string, determine if it's a palindrome or not. 
# 2 other solutions, give pros and cons.

string = "racecar"
string2 = "racexcar"


'''
divid string in half
     check to see if first and last are the same
     if same, move on. at end of iteration return True
     if not same, return false
'''

# For loop
def palindrome(string):
    for i in range(len(string)/2):
        if string[i] != string [-1-i]:
            return False
    return True

print palindrome(string)
print palindrome(string2)

# Recursively
def palindrome_rec(string):
    if len(string) <= 1:
        return True
        #both of these statements have to be true in order to return true at the end
    return string[0] == string[-1] and palindrome_rec(string[1:-1])

print palindrome_rec(string)
print palindrome_rec(string2)

# Built in reverse function
def palindrome_py(string):
    if string == ''.join(reversed(string)):
        return True
    return False

print palindrome_py(string)
print palindrome_py(string2)



##################################################################################

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


















