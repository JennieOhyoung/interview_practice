#1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

s_true = "abcdefghijklmnop"
s_false = "this is not a unique string"

# With list, O(n^2)
def with_ds(s):
    l = []
    for i in s:
        if i in l:
            return False
        else:
            l.append(i)
    return True


# With set, O(n)
def with_set(s):
    s_set =set(s)
    if len(s) != len(s_set):
            return False
    return True


# No additional data structure with O(n^2)
def no_ds(s):
    for i in s:
        repeat = 0
        for j in s:
            if i == j:
                repeat += 1
            if repeat > 1:
                return False

    return True

func_list = [with_ds, with_set, no_ds]
# for func in func_list:
#     print "Testing function " + str(func)

#     if func(s_true):
#         print "Test 1 passed"
#     else:
#         print "Test 1 failed"
    
#     if not func(s_false):
#         print "Test 2 passed"
#     else:
#         print "Test 2 failed"