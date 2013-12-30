# chris/huy
# given a list of numbers from 1 to n randomly placed, there is one missing number. find the missing number without sort and with O(n)

l = [3,1,11,2,5,4,7,9,8,6,10,13]

def missing_num(l):
    acc_val = 0
    acc_i = 0
    for i, val in enumerate(l):
        acc_i += i+1
        acc_val += val
    return (acc_i + len(l)+1) - acc_val


print missing_num(l)