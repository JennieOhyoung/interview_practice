"""
Implement power (x,n) using recursion in log n time.
"""


def pow(x, n):
    temp = 1
    if n == 0:
        return 1
    temp = pow(x, n/2)
    if n%2 == 0:
        return temp*temp
    return x*temp*temp

print pow(2, 3)