# Write a function that helps cashier to give change back in as little coins as possible. Input is change need to be given back, output is minimum # of coins needed.


def change(amount):
    quarter = 0.25
    q_count = 0
    dime = 0.1
    d_count = 0
    nickel = 0.05
    n_count = 0
    penny = 0.01
    p_count = 0
    left = amount
    while left > 0:
        if left >= quarter:
            left -= quarter
            q_count += 1
            print left
        if left >= dime:
            left -= dime
            d_count += 1
            print left
        if left >= nickel:
            left -= nickel
            n_count += 1
            print left
        if left >= 0:
            left -= penny
            p_count += 1
            print left

    total = q_count + d_count + n_count + p_count
    # print left
    # print q_count
    # print d_count
    # print n_count
    # print p_count

    return "you need a minimum of " + str(total) + " coins."


# print change(.35)


def coinChange(centsNeeded, coinValues):
    minCoins = [[0 for j in range(centsNeeded + 1)]
               for i in range(len(coinValues))]
    minCoins[0] = range(centsNeeded + 1)

    for i in range(1,len(coinValues)):
      for j in range(0, centsNeeded + 1):
         if j < coinValues[i]:
            minCoins[i][j] = minCoins[i-1][j]
         else:
            minCoins[i][j] = min(minCoins[i-1][j],
             1 + minCoins[i][j-coinValues[i]])

    print minCoins
    return minCoins[-1][-1]


coinValues = [1, 5, 10, 25]
print coinChange(15,coinValues)


