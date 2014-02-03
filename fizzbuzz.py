#85 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def main1():
    sum_multiples = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            sum_multiples += i
    print sum_multiples

# main1()

# Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz. For numbers which are multiples of both three and five print FizzBuzz

def fizzbuzz():
    for i in range(1,100):
        if i%3 == 0 and i%5 == 0:
            print str(i) + "FizzBuzz" 
        elif i%3 == 0:
            print str(i) + "Fizz"
        elif i%5 == 0:
            print str(i) + "Buzz"

# fizzbuzz()