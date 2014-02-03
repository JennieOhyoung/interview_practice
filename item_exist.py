# given a list, determine whether element k is in the list

l = [1,7,3,8,2,4,9]
sorted_l = [1,2,3,4,7,8,9]

def exist(k):
    for i in l:
        if i == k:
            return True
    return False

print "random list: \n"
print exist(0)
print exist(2)
print exist(5)
print exist(10)
print "\n"



# how does it change if list is sorted?

def sorted_exist(k):
    if k >= sorted_l[0] and k <= sorted_l[-1]:
        for i in range(len(sorted_l)):
            if sorted_l[i] == k:
                return True
        return False
    return False
        

print "sorted list: \n"
print sorted_exist(0)
print sorted_exist(2)
print sorted_exist(5)
print sorted_exist(9)
print sorted_exist(-1)




















