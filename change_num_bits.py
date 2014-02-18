
"""
write a function that returns the number of bits that would need to be changed to turn numberA into numberB. That is:
        int getNumberOfBitsToChange(int numberA, int numberB)
and if I passed it 12 and 16,
00001100
00010000

it is easy to see that 3 bits need to change to convert 12 to 16

"""


def bits_needs_changed(a,b):
    bin_a = bin(a)[2:].zfill(8)
    bin_b = '{0:08b}'.format(b) 
    count = 0
    for i in range(len(bin_a)):
        if bin_a[i] != bin_b[i]:
            count += 1
    return count

print bits_needs_changed(27,8)