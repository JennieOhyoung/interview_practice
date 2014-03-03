# Check to see if item is in list using binary search.

l = [1,2,4,5,7,9,11,16,20,36,68]

def in_list(item, l):
    found = False
    bottom = 0
    top = len(l)-1

    while bottom <= top and not found:
        middle = (bottom+top)/2
        if l[middle] == item:
            found = True
        elif l[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


# print in_list(20,l)
# print in_list(11,l)

def in_list2(item, l):
    first = 0
    last = len(l)-1
    while first <= last:
        mid = (first+last)//2
        if l[mid] == item:
            return True
        elif l[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


# print in_list2(37,l)
# print in_list2(11,l)

# RECURSIVELY
def in_list3(item, l):
    if len(l) == 0:
        return False
    else:
        mid = len(l)//2
        if l[mid] == item:
            return True
        elif l[mid] > item:
            return in_list3(item, l[:mid])
        else:
            return in_list3(item, l[mid+1:])
# :mid doesnt have +1 because in list slicing, the last number is already excluded! [3:9]

print in_list3(36,l)
print in_list3(6,l)
print in_list3(9,l)

