# Take a number n, return a list of fibbonacci numbers up to n. (value -> index, index -> value)

# O(2^n) recursively
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

def fib_list(n):
    l = []
    for i in range(n+1):
        if fib(n):
            l.append(fib(i))
    return l

# O(n) dynamically (w/ datastructure)
def fib2(n):
   fibValues = [0,1]
   for i in range(2,n+1):
      fibValues.append(fibValues[i-1] + fibValues[i-2])
   return fibValues[n]

# O(n) dynamically (w/out datastructure)
def fib(n):
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return a

print fib_list(8)