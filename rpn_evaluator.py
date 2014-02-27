
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

$ python rpn.py "1 2 +"

In addition, implement your own string to number conversion function and use it in your RPN evaluator. Do not use any built-in method to convert your strings to numbers in your RPN evaluator.
"""

import sys

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

def str_to_num(string):
    int_list = []
    final_num = 0
    string_list = list(string)
    for char in string_list:
        if 48 <= ord(char) <= 57:
            int_list.append(ord(char)-48)
        else:
            return False
    for i in range(len(int_list)):
        value = int_list[-i-1]
        place = 10**i
        final_num += value*place
    return final_num

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
    # equation = (str(equation)).strip("[]'',")

    for i in equation:
        if i in "[]'',. ":
            continue
        elif i.isdigit():
            s.push(str_to_num(i))
        elif i in "+-*/":
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



