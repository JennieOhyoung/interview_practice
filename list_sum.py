# write function to sum up numbers in a list

l = [1,2,3,4,5]
l2 = [1,3,5,7,9]

def iterative(l):
    total = 0
    for i in l:
        total += i
    return total

def recursive(l):
    if len(l) == 1:
        return l[0]
    return l[0]+recursive(l[1:])


print iterative(l),
print iterative(l2)
print recursive(l),
print recursive(l2)

