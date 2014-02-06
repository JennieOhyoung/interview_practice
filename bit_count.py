"""
Given a number (decimal base 10), write function to count the number of bits set to '1' in its binary (base 2) value.

    - translate number from base 10 to base 2
    - count 1s in binary value
"""

# first thought: base case is 1 and 2, base of "1" + the "0"s grows by power of 2. eg 1 = 1, 2 = 1+0, 2^2 = 10+0, 2^2^2 = 100+0 etc. Therefore, for the base in num is 2^i < num, and the # of 0 trailing 1 in base is i

import math


def binary(num):
    if num < 1:
        return 0

    if num == 1:
        return 1

    else:
        # establish how many digits(of 0) after 1
        base = 2
        count = 0
        while base < num:
            base *= 2
            count += 1

        # add trailing 0s
        basis = 1
        i = 0
        while i < count:
            basis *= 10
            i += 1

        rest = num - base/2
        return basis + binary(rest)

def count_1s(binary):
    if binary < 1:
        return "sorry no negatives"

    count = 0
    string = str(binary)

    for i in string:
        if i == "1":
            count += 1
    return count



print count_1s(binary(337))
print count_1s(binary(-6))