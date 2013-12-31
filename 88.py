#88 The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

# Determine the prime numbers from 1 to number
# Find the largest item of a list
# observations about prime:
    # they're always odd
    # factors come in pairs (reduce runtime by shortening range?)

# def prime_list(num):
#     for i in range(num):


# plist = [2]

# def primes(min, max):
#     if 2 >= min: yield 2
#     for i in range(3, max, 2):
#         for p in plist:
#             if i%p == 0 or p*p > i: break
#         if i%p:
#             plist.append(i)
#             if i >= min: yield i
    
# def factors(number):
#     for prime in primes(2, number):
#         if number % prime == 0:
#             number /= prime
#             yield prime
#         if number == 1:
#             break

# print max(factors(318))

def highest_prime_factor(num):
        i = 2

        # only increment through numbers that are less than half of
        # the original number 
        while i*i < num:
                # print "i is: %d" % i

                # checks if the number incremented is divisible by number
                while num%i == 0:
                        num = num/i 
                i += 1

        return num


def main(): 
        solution = highest_prime_factor(195)
        print solution


main()

# import math
# def prime_factor(num):
#     for i in range(3, int(math.sqrt(num)), 2):
#         while num%i == 0:
#                 num = num/i 
#         i += 1
#     return num

# def main():
#     largest = prime_factor(600851475143)
#     print largest

# main()