"""
Given an array of integers, find the sub array with the largest sum. (must be done in linear time)
"""


l = [-1,2,-5,2,1,7,-9]

def mssl(l):
    best = 0
    cur = 0

    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)

    return best

print mssl(l)