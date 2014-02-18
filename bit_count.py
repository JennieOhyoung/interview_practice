"""
Given a number (decimal base 10), write function to count the number of bits set to '1' in its binary (base 2) value.

    - translate number from base 10 to base 2
    - count 1s in binary value
"""

# first thought: base case is 1 and 2, base of "1" + the "0"s grows by power of 2. eg 1 = 1, 2 = 1+0, 2^2 = 10+0, 2^2^2 = 100+0 etc. Therefore, for the base in num is 2^i < num, and the # of 0 trailing 1 in base is i

# import math

# translate number into binary value
def binary(num):
    # establish base cases
    if num < 1:
        return 0

    if num == 1:
        return 1

    if num == 4:
        return 100

    else:
        # establish how many digits(of 0) after 1
        base = 2
        count = 0
        while base < num:
            base *= 2
            count += 1

        # populate established base with 0s
        basis = 1
        i = 0
        while i < count:
            basis *= 10
            i += 1

        # figure out subset and its return recursively
        rest = num - base/2
        return basis + binary(rest)

# iterate through binary number and find 1s
def count_1s(number):
    # find binary value of number
    binary_rep = binary(number)

    # 
    if binary_rep <= 0:
        return "sorry no negatives or 0s"

    # set number of 1s at 0, and turn number into string to iterate through
    count = 0
    string = str(binary_rep)

    # iterate through string and count 1s
    for i in string:
        if i == "1":
            count += 1
    return count

# print count_1s(337)
# print count_1s(-6)
# print count_1s(12.6)

def find_binary(num):
    if num < 1:
        return 0

    if num == 1:
        return 1

    if num == 4:
        return 100

    else:
        base = 2
        count = 0
        while base < num:
            base = base << 1
            count += 1

        # populate established base with 0s
        basis = 1
        i = 0
        while i < count:
            basis *= 10
            i += 1

        # figure out subset and its return recursively
        rest = num - base/2
        return basis + find_binary(rest)

# iterate through binary number and find 1s

print find_binary(8)




























