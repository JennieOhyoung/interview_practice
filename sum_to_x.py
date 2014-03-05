"""
Function to check if any 3 numbers sum to x.
"""

l1 = [7,3,1,4,5]
# l2 = [4,5,6,7]

def sum_to_x(l, x):
    l.sort()
    # print l
    for i, val in enumerate(l):
        lower = 0
        upper = len(l)-1
        while lower < i < upper:
            temp = val + l[lower] + l[upper]
            if temp > x:
                upper -= 1
            elif temp < x:
                lower += 1
            else:
                yield l[lower], val, l[upper]
                lower += 1
                upper -= 1


print list(sum_to_x(l1, 8))