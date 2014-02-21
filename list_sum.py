# write function to sum up numbers in a list

l = [1,2,3,4,5]
def iterative(l):
    total = 0
    for i in l:
        total += i
    return total
# print iterative(l)

l2 = [1,3,5,7,9]
def recursive(l2):
    if len(l2) == 1:
        return l2[0]
    return recursive(l2[0])+recursive(l2[1:])
print recursive(l2)