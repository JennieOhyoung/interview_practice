 # Take a number n, return a list of fibbonacci numbers up to n. (value -> index, index -> value)

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

def fib_list(n):
    l = []
    for i in range(n+1):
        if fib(n):
            l.append(fib(i))
    return l


# fib_list(17)
print fib_list(8)