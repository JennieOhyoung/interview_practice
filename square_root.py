# Write a function to find the square root of a number given epsilon (acceptable margin of error)

def sqrt(n, epsilon):
    upper_x = n
    lower_x = 0
    mid_pt = float(upper_x + lower_x)/2
    test = mid_pt*mid_pt

    if n < 0 or epsilon < 0:
        return "Both n and epsilon have be greater than 0"

    while True:
        mid_pt = float(upper_x + lower_x)/2
        test = mid_pt*mid_pt

        if test > n:
            upper_x = mid_pt
            mid_pt = float(upper_x + lower_x)/2

        if test < n:
            lower_x = mid_pt
            mid_pt = float(upper_x + lower_x)/2

        if n-epsilon < test < n+epsilon:
            return mid_pt
        


print sqrt(139, 0.1)
print sqrt(100.92, 0.000001)
print sqrt(1523, -0.01)



def sqrt_recursion(n, epsilon):
    

