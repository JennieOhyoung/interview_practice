# given a list of consecutive numbers [1...n] where n is unknown, you have a probe function that returns boolean if prob(num) is in list. Find length of list without using built in function len()

import random

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# where we don't know n = 14

def list_gen():
    rand_len = int(random.uniform(1,100))
    rand_list = []
    for num in range(rand_len):
        rand_list.append(num)
    print rand_list[-1]
    return rand_list

def len_search(l):
    current = 1

    while current in l:
        current *= 2
        if current not in l:
            upper = current
            lower = current/2
            middle = (lower+upper)/2
            if middle not in l:
                upper = middle
                middle = (lower+upper)/2
                if middle-1 in l:
                    return middle -1
            if middle in l:
                lower = middle
                middle = (lower+upper)/2
                if middle+1 not in l:
                    return middle
        if current in l and current+1 not in l:
            return current


print len_search(list_gen())
# print len_search(l)













