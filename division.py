# Implement division without using the / division operator.
"""
dividend/divisor = quotient (+ remainder)

scenarios:
- dividend > divisor
- divisor > dividend
- 0 as divisor -> return division by 0 is undefined
- infinite quotient -> return remainder 
- negative numbers

"""

def custom_division(dividend, divisor):
    track = 0
    if dividend == 0:
        return track
    if divisor == 0:
        return "Division by 0 is undefined!"
    else:
        if dividend >= divisor:
            current = dividend
            while current >= divisor:
                current = current - divisor
                track += 1
            if current != 0:
                return str(track) + " with a remainder of " + str(current)
            else:
                return track
        else:
            current = dividend * 10
            while current >= divisor:
                current = current - divisor
                track += 1
            if current != 0:
                return str(track*.1) + str(current)
            if current == 0:
                return track*.1



print custom_division(3,10)






