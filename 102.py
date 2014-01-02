
# O(2^n) recursively
def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib(i-1) + fib(i-2)

# print fib(50)


# O(n) dynamically (w/ datastructure)
def fib2(n):
   fibValues = [0,1]
   for i in range(2,n+1):
      fibValues.append(fibValues[i-1] + fibValues[i-2])
   return fibValues[n]

print fib2(50)

# O(n) dynamically (w/out datastructure)
def fib(n):
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return a
print fib(50)