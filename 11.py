# chris/huy
# given a list of numbers from 1 to n randomly placed, there is one missing number. find the missing number without sort and with O(n)

l = [3,1,11,2,5,4,7,9,8,6,10,13] # missing 12, starts at 1, len = 12
l2 = [4,5,6,7,8,9,11,12,13]      # missing 10, starts at 4, len = 9
l3 = [3,4,5,6,7,8,9]

# iteratively
def missing_num(l):
    acc_val = 0
    acc_i = 0
    for i, val in enumerate(l):
        acc_i += i+1
        acc_val += val
    return (acc_i + len(l)+1) - acc_val
# print missing_num(l)


# with formula summation = (n(n+1))/2
def missin_num2(l):
    acc_i = 0
    acc_val = (max(l)*(max(l)+1))/2
    for i in l:
        acc_i += i
    return acc_val - acc_i
# print missin_num2(l)


# recursively - works on lists that doesn't start at 1 as well
def is_missing_num(l):
    expected_val = min(l) + len(l) -1
    if max(l) != expected_val:
        return False
    return True

def missing_num3(l):
    l.sort()
    


# print is_missing_num(l3)
missing_num3(l)


