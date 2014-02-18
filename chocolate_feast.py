"""
Little Bob loves chocolates and goes to the store with a $N bill with $C being the price of each chocolate. In addition, the store offers a discount: for every M wrappers he gives the store, hell get one chocolate for free. How many chocolates does Bob get to eat?

Input Format:
The first line contains the number of test cases T (<=1000). 
Each of the next T lines contains three integers N, C and M

Output Format:
Print the total number of chocolates Bob eats.

Constraints:
2 <= N <= 100000
1 <= C <= N
2 <= M <= N


Sample input

3
10 2 5
12 4 4
6 2 2


Sample Output

6
3
5

"""


def chocolate_eaten(n,c,m):
#1st attempt
    # count = n/c
    # new_count = count/m
    # remaining = new_count%m
    # if remaining < new_count and remaining != 0:
    #     count += new_count+remaining
    # else:
    #     return count + new_count
    # return count

#2nd attempt
    # count = n/c
    # additional = count/m
    # wrapper = count - additional*m
    # total = count + additional
    # if total >= m:
    #     total += total/m
    # return total

#3rd attempt
    # count = n/c
    # wrapper = count
    # while wrapper >= m:
    #     count += wrapper-m
    #     wrapper -= m
    # return count

#4th attempt
    count = n/c
    wrapper = count
    while wrapper/m:
        additional = wrapper/m
        wrapper = wrapper%m + additional
        count += additional
    return count
    

print chocolate_eaten(10,2,5)
print chocolate_eaten(12,4,4)
print chocolate_eaten(27,3,2)


for i in (range(input()))[1:]:
    list_i = i.split()
    n = list_i[0]
    c = list_i[1]
    m = list_i[2]
count = n/c
wrapper = count
while wrapper/m:
    additional = wrapper/m
    wrapper = wrapper%m + additional
    count += additional
print count



