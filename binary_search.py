# Check to see if item is in list using binary search.

l = [1,2,4,5,7,9,11,16,20,36,68]

def in_list(item, list):
    found = False
    bottom = 0
    top = len(l)-1

    while bottom <= top and not found:
        middle = (bottom+top)/2
        if list[middle] == item:
            found = True
        elif list[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


print in_list(12,l)
print in_list(11,l)