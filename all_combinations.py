""" 
Write function to print all combinations of a string
"""

import itertools
l = "abc"

# if 1 char may appear multiple times
def all_combinations(l):
    count = 0  
    for p in itertools.product(l, repeat=len(l)):
        print p
        count +=1
    return "There are %d combinations " %count
print all_combinations(l)

# without duplicates
def all_combinations1(l):
    result = []
    for i in range(len(l)):
        result.append(l[i])
        for j in all_combinations1(l[:i]+ l[i+1:]):
            result.append(l[i]+j)
    return result
print all_combinations1(l)