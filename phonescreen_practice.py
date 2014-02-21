# Write a function to reverse a string.
n = "hello world"
def reverse(n):
    # return n[::-1]
    n_list = []
    for i in range(len(n)):
        n_list.append(n[-1-i])
    return ''.join(n_list)
# print reverse(n)

l = [1,2,8,3,5,6]
def reverse2(l):
    temp = l[-1]
    for i in range(len(l)/2):
        temp = l[-1-i]
        l[-1-i] = l[i]
        l[i] = temp
    return l
# print reverse2(l)

# Write a function to check to see if string is a palindrome.
l1 = "kayak"
l2 = "Live not on evil"
l3 = "NoT a PalinDROME"
l4 = "Madam i'm Adam"

def reverse(l):
    normalized = l.replace(" ", "").replace("'", "").lower()
    if normalized == '':
        return normalized
    return reverse(normalized[1:]) + normalized[0]

def palindrome(l):
    if l.replace(" ", "").replace("'", "").lower().strip("'") == reverse(l):
        return True
    return False

# print reverse(l1)
# print reverse(l2)
print palindrome(l1)
print palindrome(l2)
print palindrome(l3)
print palindrome(l4)


# Write function to compute Nth fibonacci number
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

# print fib(6)
def fib2(n):
    fib = [0,1]
    for i in range(1,n):
        fib.append(fib[-1]+fib[-2])
    return fib[-1]

#Print out the grade-school multiplication table
def multiplication_table(w,h):
    for i in range(1,h+1):
        for j in range(1,w+1):
            print i*j, "\t",
        print


# Write function to print the odd numbers from 1 to 99.
def odd_num(num):
    for i in range(1,num+1):
        if i%2 != 0:
            print i


# Find the largest int value in an int array.
def largest_int(array):
    max = array[1]
    for i in array:
        if i>max:
            max = i
    return max


# Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.
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
        return self.items[-1]

    def size(self):
        return len(self.items)

def rbg_converter(rbg):
    hex_val = []
    hex_digits = "0123456789ABCDEF"
    s = Stack()

    for color in rbg:
        while color >0:
            rem = color%16
            s.push(rem)
            color = color//16

        hexstring = ''
        while not s.isEmpty():
            hexstring=hexstring+hex_digits[s.pop()]
        hex_val.append(hexstring)
    return ''.join(hex_val)


# rbg = [233,24, 255]
# print rbg_converter(rbg)






