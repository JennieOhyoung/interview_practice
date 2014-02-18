"""
A pile of nuts is in an oasis, across a desert from a town.  The pile
contains 'N' kg of nuts, and the town is 'D' kilometers away from the
pile.

The goal of this problem is to write a program that will compute 'X',
the maximum amount of nuts that can be transported to the town.

The nuts are transported by a horse drawn cart that is initially next
to the pile of nuts. The cart can carry at most 'C' kilograms of nuts
at any one time. The horse uses the nuts that it is carrying as fuel.
It consumes 'F' kilograms of nuts per kilometer travelled regardless
of how much weight it is carrying in the cart. The horse can load and
unload the cart without using up any nuts.

Your program should have a function that takes as input 4 real numbers
D,N,F,C and returns one real number: 'X'

Your program should also have a function that reads an input text file
from the command line. This input file contains an arbitrary number of
lines. Each line is of the form:
D,N,F,C
where D,N,F, C are integers in decimal notation. This function should
write to standard output as many lines as the input file had. Each
line should contain a single real number X.

As part of your submission, please send the output of the latter
function when the input file is:

1000,3000,1,1000
1000,7000,1,1000
1000,100000,1,1000
1111,3000,1,1000
1000,3000,1,1111
1111,3334,3,4444
111,3333,3,2222
111,3333,3,1000
10000,1111111,3,1111
10000,1111111,5,1111
1000,1000000,2,1000
1111,22222222,5,3333
1000,12000,5,3000

The answer is greater than 0 even if C>D*F.

"""

# d = distance
# n = kg of nuts
# f = kg of nut consumed per km
# c = kg of nuts in carriage

# num of trips: consumption
# 1: 1(d*f)
# 2: 3(d*f)
# 3: 5(d*f)
# 4: 7(d*f)
# 5: 9(d*f)

import math

# text = raw_input("Which input file would you like to use? ")

# naive solution with single trips to and from oasis
def max_nuts(d,n,f,c):
    if n < c:
        x = n - d*f
        return x
    elif n == c:
        x = c - d*f
        return x
    else:
        least_trips = n/c
        if least_trips > 1:
            consumed = ((2*least_trips)-1)*(d*f)
        elif least_trips == 1:
            consumed = d*f
        x = least_trips*c - consumed
        oasis = n - least_trips*c

        # if horse is going to end up eating the entire stock of nuts, might as well not transport or have 0 kg transported
        if consumed >= n:
            return 0
        # if whats left at oasis is not enough to feed the horse for the last trip, then what we have at the village is what we will have as max.
        elif oasis < 2*(d*f):
            return x
        # otherwise, even if whats left at oasis is not enough for full capacity, we will transport the last bit to village less the horse feed.
        else:
            x += (oasis - 2*(d*f))
            return x

# print max_nuts(1000,3000,1,1000)




# d = distance
# n = kg of nuts
# f = kg of nut consumed per km
# c = kg of nuts in carriage

# recursive solution reducing last trip to max x
def max_nuts2(d,n,f,c):
    if n <= c:
        x = n - d*f
        return x

    trips = 2*(math.ceil(n/c)) - 1
    cost_km = trips*f
    check_point = c/trips
    remaining_distance = d - check_point
    consumed = check_point*cost_km
    remaining_nuts = n - consumed

    # if consumed >= n:
    #     total_consumption = trips*d*f
    #     x = 
    #     return 

    if check_point >= d:
        return n - d*cost_km
    print remaining_distance, remaining_nuts
    return max_nuts2(remaining_distance, remaining_nuts, f, c)

# print max_nuts2(1000,12000,5,3000)


def test(d,n,f,c):
    print str(max_nuts(d,n,f,c))+ " from fn1 and  " + str(max_nuts2(d,n,f,c)) + " from fn2 "

# test(1000,12000,5,3000)


def parser(text):
    f=open(text)
    dnfc = f.read()
    f.close()

    text = []
    for line in dnfc.splitlines():
        text.append(line.split(','))

    # solution = []
    for problem in text:
        d = float(problem[0])
        n = float(problem[1])
        f = float(problem[2])
        c = float(problem[3])
        # print max_nuts(d,n,f,c)
        print max_nuts2(d,n,f,c)

    return 



# parser(text)
print "naive solution yields: " +str(max_nuts(1000,3000,1,1000))
print max_nuts2(1000,3000,1,1000)


"""
karas
def max_nuts(d,n,f,c):
    max_trips = 2 * math.ceil(n / c) - 1
    min_trips = 2 * math.floor(n / c) - 1
    nuts_4_min_trips = min_trips * c
    max_trips_ans = n - (max_trips * d * f)
    min_trips_ans = nuts_4_min_trips - (min_trips * d * f)
    return max(max_trips_ans, min_trips_ans)
"""




