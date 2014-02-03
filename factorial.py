 # Given a number, return its factorial value.  Do it recursively and nonrecursively

# recursive
 def factorial_value(n):
    if n<=1:
        return 1
    return n*factorial_value(n-1)

# nonrecursively
def factorial_value(n):
    fac = 1
    if n<=1:
        return fac
    else:
        for i in range(1,n-1):
            fac = fac*i
    return fac

print factorial_value(6)