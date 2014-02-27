
"""
write functions to convert Infix expressions to Postfix, another to evaluate.
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


################################################################################


def order_operation(operator):
    if operator in "^":
        return 3
    elif operator in "*/":
        return 2
    elif operator in "+-":
        return 1
    else:
        return 0

def postfix_conversion(infix):
    s = Stack()
    output = []
    infix_list = infix.split()

    for i in infix_list:
        if i in "0123456789" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            output.append(i)
        elif i == "(":
            s.push(i)
        elif i == ")":
            top = s.pop()
            while top != "(":
                output.append(top)
                top = s.pop()
        else:
            while (not s.isEmpty()) and (order_operation(s.peek()) >= order_operation(i)):
                output.append(s.pop())
            s.push(i)

    while not s.isEmpty():
        output.append(s.pop())

    return "".join(output)

# print postfix_conversion("A * B + C * D")
# print postfix_conversion("A + B * C + D")
# print postfix_conversion("( A + B ) * C + D")
# print postfix_conversion("A + B + C + D")
# print postfix_conversion("( A + B ) * C - ( D - E ) * ( F + G )")
# print postfix_conversion("5 * 3 ^ ( 4 - 2 )")



################################################################################

def math(op, op1, op2):
    if op =="*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2

def postfix_eval(infix):
    s = Stack()
    infix_list = infix.split()
    print type(infix_list)

    for i in infix_list:
        print type(i)
        if i in "0123456789":
            s.push(int(i))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = math(i, op1, op2)
            s.push(result)
    return s.pop()


print postfix_eval(" 3 5 + ")
print postfix_eval("7 8 + 3 2 + /")
print postfix_eval("4 8 / 3 6 * ")
print postfix_eval("17 10 + 3 * 9 / ==")
print postfix_eval("5 * 3 ^ (4 - 2)")






