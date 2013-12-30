# Given 2 lists of values of any kind, return list that contains all common values

l1 = list("abcd1234")
l2 = list("7654eald")

# O[n^2]
def common_val(l1,l2):
    l = []
    for i in l1:
        for j in l2:
            if i == j:
                l.append(i)
    return l

# O[2n]
def common_val(l1,l2):
    d = {}
    l = []
    for i in l1:
        d[i] = 1
    for j in l2:
        if d.get(j):
            l.append(j)
    return l

print common_val(l1,l2)