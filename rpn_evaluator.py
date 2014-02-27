
""" 
Implement a RPN evaluator. It should be able to evaluate the following strings and answer with the corresponding numbers: 

"1 2 +" = 3 

"4 2 /" = 2 

"2 3 4 + *" = 14 

"3 4 + 5 6 + *" = 77 

"13 4 -" = 9

And should provide an error message for the following types of errors

"1 +" (not enough arguments)
"a b +" (invalid number)

We should be able to evaluate a string from the command line in the following way:

$ ruby rpn.rb "1 2 +"
"""

import sys

# implement stack
class Stack(object):
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []

# helper function to perform operations
def math(operator, first_num, second_num):
    if operator =="*":
        return first_num*second_num
    elif operator == "/":
        return first_num/second_num
    elif operator == "+":
        return first_num+second_num
    else:
        return first_num-second_num

# separate operants from operators, call helper function on last two items on stack. 
def postfix_evaluator(equation):
    s = Stack()

    for i in equation:
        if str(i).isdigit():
            s.push(int(i))
        elif str(i) in "+-*/":
            second_num = s.pop()
            if not s.isEmpty():
                first_num = s.pop()
                result = math(i, first_num, second_num)
                s.push(result)
            else:
                return "Not enough arguments"
        else:
            return "Invalid number"
    return s.pop()


if __name__ == "__main__":
    # type(argv) = list
    raw = sys.argv
    # take out argv[0], tokenize
    equation = ''.join(raw[1:]).split()
    # call function to evaluate input equation
    print postfix_evaluator(equation)
    sys.exit(0)



