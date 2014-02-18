"""
write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced.
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


#buggy 
def balanced_par(symb_str):
    s= Stack()
    symb_list = list(symb_str)

    if len(symb_str)%2 != 0:
        return False
    for ch in symb_list:
        if ch == "(":
            s.push(ch)
        else:
            if s.isEmpty():
                return False
            else:            
                s.pop()
                symb_list.remove(ch)
    return True



def balanced_par2(symb_str):
    s = Stack()
    balanced = True

    for val in symb_str:
        if val == "(":
            s.push(val)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

    if balanced and s.isEmpty():
        return True
    else:
        return False


print balanced_par2("()())(")
print balanced_par2('((()))')
print balanced_par2('(()')
print balanced_par2('()()((()))((')




