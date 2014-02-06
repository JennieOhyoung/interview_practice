# Write a function to find the square root of a number given epsilon (acceptable margin of error)

def sqrt(n, epsilon):
    upper_x = float(n)
    lower_x = 0

    if n < 0 or epsilon < 0:
        return "Both n and epsilon have be greater than 0"

    while True:
        mid_pt = (upper_x + lower_x)/2
        test = mid_pt*mid_pt

        if test > n:
            upper_x = mid_pt

        if test < n:
            lower_x = mid_pt

        if n-epsilon < mid_pt*mid_pt< n+epsilon:
            return mid_pt

print sqrt(100, 15)

