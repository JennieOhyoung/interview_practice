# Given a list of consecutive numbers [1...n] where n is unknown, you only know whether a number is in list. Find length of list without using built in function len() or slicing. Do this in O(log n)

import random

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def list_gen():
    rand_len = int(random.uniform(1,100))
    rand_list = []
    for num in range(rand_len):
        rand_list.append(num)
    print rand_list[-1]
    return rand_list



# 1. Cheat ==========================================================

def slicing():
    lst = list_gen()
    return lst[-1]-lst[0]

print "The length is " + str(slicing())



# 2. Iterative ===================================================

def upper_bound(l):
    current = 1
    while current in l:
        current *= 2
        if current not in l and current/2 in l:
            upper = current
            lower = current/2
            return lower, upper

def binary_search(l):
    lower = (upper_bound(l))[0]
    upper = (upper_bound(l))[1]
    middle = (lower+upper)/2
    while True:
        if middle in l:
            lower = middle
            middle = (lower+upper)/2
            if middle in l and middle+1 not in l:
                return middle

        elif middle not in l:
            upper = middle
            middle = (lower+upper)/2
            if middle not in l and middle-1 in l:
                return middle -1


print "Iteratively: " + str(binary_search(list_gen()))




# 3. Recursive ======================================================

def probe(lst, n):
    if n <= len(lst):
        return True
    return False

def binary_search(low, high):
    if high - low == 1:
        return high
    mid = (high + low) / 2
    if probe(lst, mid) == False:
        return binary_search(low, mid)
    else:
        return binary_search(mid, high)

def find_len(lst):
    i = 0
    while True:
        if probe(lst, 2**i) == False:
            break
        else:
            i += 1
    return "Recursively: " + str(binary_search(2**(i-1), 2**i))


print find_len(list_gen())







