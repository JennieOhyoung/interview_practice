# Cracking the Coding Interview Chapter 1

#1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

s_true = "abcdefghijklmnop"
s_false = "this is not a unique string"

# With list, O(n^2)
def with_ds(s):
    l = []
    for i in s:
        if i in l:
            return False
        else:
            l.append(i)
    return True


# With set, O(n)
def with_set(s):
    s_set =set(s)
    if len(s) != len(s_set):
            return False
    return True


# No additional data structure with O(n^2)
def no_ds(s):
    for i in s:
        repeat = 0
        for j in s:
            if i == j:
                repeat += 1
            if repeat > 1:
                return False

    return True

func_list = [with_ds, with_set, no_ds]
# for func in func_list:
#     print "Testing function " + str(func)

#     if func(s_true):
#         print "Test 1 passed"
#     else:
#         print "Test 1 failed"
    
#     if not func(s_false):
#         print "Test 2 passed"
#     else:
#         print "Test 2 failed"



#1.2 Implement a function that reverses a string

s = "hello world "

def reverse_slice(s):
    s_reversed = s[::-1]
    return s_reversed

def rev_with_list(s):
    s_list = []
    for i in range(len(s)-1,-1,-1):
        s_list.append(s[i])
    return s_list

def rev_with_list2(s):
    s_list = []
    for i in range(len(s)):
        s_list.append(s[-1-i])
    return s_list

def rev_manually(s):
    s_list = list(s)
    temp = 0
    for i in range(len(s_list)/2):
        temp = s_list[-1-i]
        s_list[-1-i] = s_list[i]
        s_list[i] = temp
    return s_list

def rev_recursively(s):
    if len(s) <= 1:
        return s
    return rev_recursively(s[1:]) + s[0]

# func_list2 = [reverse_slice, rev_with_list, rev_with_list2, rev_manually, rev_recursively]
# for func in func_list2:
#     print "testing function " + str(func)
#     print func(s)


#1.3 Given two strings, write a method to decide if one is a permutation of the other.

l1 = "racedcars"
l2 = "racecared"
l3 = "uvwxyz"
l4 = "zuyvxw"

def permutation(l1,l2):
    if len(l1) != len(l2):
        return False
    elif sorted(l1) == sorted(l2):
        return True

# print permutation(l1,l2)

def permutation2(l1,l2):
    if len(l1) != len(l2):
        return False
    else:
        for i in l1:
            if i not in l2:
                return False
        # for j in l2:
        #     if j not in l1:
        #         return False
    return True

# print permutation2(l1,l2)

#1.4 write a method to replace all space in a string with '%20'
def replace_space(s):
    s_list = []
    for i in s:
        if i == " ":
            s_list.append("%20")
        else:
            s_list.append(i)
    return "".join(s_list)

# print replace_space(s)


#1.5 Implement a method to perform basic string compression using counts of repeated characters. aabcccccaaa => a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string.
s1 = "aaabbcccaa"
s2 = "abcdefg"

def compression(s):
    last = ''
    count = 0
    l = []

    for i in s:
        if i == last:
            count += 1
        else:
            if last != '':
                l.append(last + str(count))
            count = 1
        last = i

    l.append(last + str(count))
    l = "".join(l)
    if len(l) < len(s):
        return l
    else:
        return s

# print compression(s1)
# print compression(s2)

# counts all repeats in string
def repeats(s):
    l = []
    for i in s:
        if i not in l:
            l.append(i)
            if s.count(i) != 1:
                l.append(str(s.count(i)))
    return ''.join(l)

# print repeats(s1)
# print repeats(s2)


#1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
class Matrix(object):

    def __init__(self,matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix

    def __str__(self):
        row = ""
        for i in self.matrix:
            row = row
            for j in i:
                row = row + " "+ str(j) +" "
            row = row + "\n"
        return row

    def rotate90CW(self):
        for row in self.matrix:
            columnlist.append([])        
        for row in self.matrix:
            columnindex=0
            for cell in row:
                columnlist[columnindex].append(cell)
                columnindex += 1
        newmatrix=[]
        for col in columnlist:
            newmatrix.append(reversed(col))
        self.matrix=newmatrix

matrix1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
# print str(matrix1)


#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


class Matrix(object):

    def __init__(self,matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix

    def __str__(self):
        row = ""
        for i in self.matrix:
            row = row + "["
            for j in i:
                row = row + " " + str(j) + " "
            row = row + "]\n"
        return row

    def zero_col_row(self):
        col_zero = []
        row_zero = []
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val == 0:
                    col_zero.append(j)
                    row_zero.append(i)
        for i in row_zero:
            self.row_turn(i)
        for j in col_zero:
            self.col_turn(j)

    def row_turn(self, i):
        new_row = []
        for x in range(0, self.m):
            new_row.append(0)
        self.matrix[i] = new_row

    def col_turn(self,j):
        for y in self.matrix:
            y[j] = 0

matrix2 = Matrix([[1,2,3], [4,0,6], [7,8,9]])
# print str(matrix2)
# matrix2.zero_col_row()
# print str(matrix2)


#1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings s1 s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring ( waterbottle is rotation of erbottlewat)

s1 = "waterbottle"
s2 = "bottlewater"

def is_substring(s1, s2):
    return s1.find(s2) > -1

def rotatedStringHasSubstring(s1,s2):
    #doubling the string ensures a complete substring regardless of rotation
    if len(s2)!=len(s1):
        return False
    doubles1 = 2*(s1)
    return is_substring(doubles1,s2)

print is_substring(s1,s2)
print rotatedStringHasSubstring(s1, s2)








