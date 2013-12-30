# Write function that takes one number and two lists, find if two items from the lists can add up to that number. Three items? 


l1 = [1,2,3,4,5]
l2 = [8,7,6,5,4]


# nested loop (2 items sum)
def has_sum(num, l1, l2):
    for i in l1:
        for j in l2:
            if i + j == num:
                return True
    return False
# print has_sum(20, l1, l2)

def has_sum_modified(num, l1, l2):
    new_l = []
    for i in l1:
        new_l.append(num-i)
    for j in new_l:
        if j in l2:
            return True
    return False
# print has_sum_modified(81, l1, l2)

# 3 item sum (naive)
def three_item_sum(num, l1, l2):
    l3 = l1 + l2 # T_T'
    for i in l1:
        for j in l2:
            for k in l3:
                if i+j+k == num:
                    return True            
    return False

# print three_item_sum(800, l1, l2)

# 3 items sum (confusing attempt)
def corresponding_tuple(num, i):
    pairs_found = []
    for j in range(((num-i)/2)+1): #if num = 10, l1 = [5], range = (0,3)
        pairs_found.append((j,(num-i-j)))
    return pairs_found

# print corresponding_tuple(17, 2)
# print corresponding_tuple(16, 1)
# print corresponding_tuple(130, 5)

def three_item_sum(num, l1, l2):
    component_dict ={}
    for i in l1:
        component_dict[i] = corresponding_tuple(num, i)
        for j in l2:
            if j in dict[i] and i-j in (dict[i] and l2):
                return True
    for i in l2:
        component_dict[i] = corresponding_tuple(num, i)
        for j in l1:
            if j in dict[i] and i-j in (dict[i] and l1):
                return True
    return False

# print three_item_sum(15, l1, l2)




# dictionary (union, returns list of items in common)
def common_items(l1, l2):
    l = []
    d = {}
    for i in l1:
        d[i] = 1
    for j in l2:
        if d.get(j):
            l.append(j)
    return l

# print common_items(l1, l2)

