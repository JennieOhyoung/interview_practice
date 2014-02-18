""" 
write an algorithm that will read a string of symbols from left to right and decide whether the symbols are balanced.
e.g 
    { { ( [ ] [ ] ) } ( ) }
    [ [ { { ( ( ) ) } } ] ]
    ( [ ) ]
    ( ( ( ) ] ) )
"""

class Stack(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def match(opens, closes):
    openers = "({["
    closers = ")}]"
    return openers.index(opens) == closers.index(closes)


def balanced_symb(symb_str):
    s = Stack()
    balanced = True
    for val in symb_str:
        if val in "({[":
            s.push(val)
        else:
            if s.isEmpty():
                balanced = False
            else:
                opens = s.pop()
                if not match(opens, val):
                    balanced = False
    if balanced and s.isEmpty():
        return True
    else:
        return False

print balanced_symb("(){")
print balanced_symb("(){}[]")
print balanced_symb("[{()]}[)")
















