"""
1. convert base 10 number to binary using stack
2. convert base 10 number to any base using stack
hint: hex uses 0123456789ABCDEF

"""


class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()


####################################################################
# ITERATIVELY

def base2(num):
    s = Stack()
    binary = ''

    while num != 0:
        rem = num%2
        s.push(rem)
        num = num/2
    while not s.isEmpty():
        binary= binary + str(s.pop())
        # print type(str(s.pop()))
    return binary

# print base2(9)

def any_base(num, base):
    # for bases up to 36
    symb = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = Stack()

    while num >0:
        rem = num%base
        s.push(rem)
        num = num/base

    newval = ""
    while not s.isEmpty():
        newval = newval + symb[s.pop()]
    return newval

print any_base(40,30)

def any_base2(num, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    
    while num > 0:
        if num < base:
            s.push(digits[num])
        s.push(digits[num%base])
        n = n//base
        convert = ""
        while not s.isEmpty():
            convert += digits[s.pop()]
        return convert
    


####################################################################
# RECURSIVELY 

#NO STACK!!
def any_base3(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    return any_base2(num//base, base) + digits[num%base]
    
print any_base3 (700,16)

























