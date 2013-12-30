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

    while left >= quarter:
        left -= quarter
        q_count += 1
    while left >= dime:
        left -= dime
        d_count += 1
    while left >= nickel:
        left -= nickel
        n_count += 1
    while left >= penny:
        left -= penny
        p_count += 1
    total = q_count + d_count + n_count + p_count

    return "you need a minimum of " + str(total) + " coins."



print change(.99)

