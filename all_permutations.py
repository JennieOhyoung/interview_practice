""" 
Write function to print all permutation of a string/list
"""
import itertools
s = "abc"
l = list("abc")


def all_permutations(l):
    if not l:
        return [[]]
    result = []
    for i in l:
        temp = l[:]
        # print temp
        temp.remove(i)
        result.extend([[i]]+r for r in all_permutations(temp))
    return result
print all_permutations(l)


def all_permutations1(s):
    combo = list(itertools.permutations(l))
    return combo
# print all_permutations1(s)


def all_permutations2(a):
    if len(a) <= 1:
        return

    first = 0
    last = len(a)

    while True:
        i = last - 1

        while True:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i] # swap the values
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == first:
                a.reverse()
                return
# print list(all_permutations2(l))











