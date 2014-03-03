
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