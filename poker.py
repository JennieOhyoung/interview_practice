#Implement a Poker Hand solver for 1 deck. 2 cards in hand. 5 cards on table. find the best hand given the shown cards.

# total 52 cards
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
# heart, spade, diamond, club

from random import choice

def generate_game():
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list_b = ["heart", "spade", "diamond", "club"]

    a = []
    b = []
    global table
    table = []
    on_table = 5
    while len(table) < on_table:    
        a.append(choice(list_a))
        b.append(choice(list_b))
        table = zip(a,b)

    c = []
    d = []
    global hand
    hand = []
    in_hand = 2
    while len(hand) < in_hand:
        c.append(choice(list_a))
        d.append(choice(list_b))
        hand = zip(c,d)

    return table, hand
    # return "On table: " + str(table) + "\n" + "In hand: " + str(hand)



# Royal flush           values = A, K, Q, J, 10             suits = same
# straight flush        values = continuous                 suits = same
# four of a kind        values = 4 match                    suits = n/a
# full house            values = 3 match + 2 match          suits = n/a
# flush                 values = n/a                        suits = same
# straight              values = continuous                 suits = n/a
# three of a kind       value = 3 match                     suits = n/a
# two pair              value = 2 match  + 2 match          suits = n/a
# one pair              value = 2 match                     suits = n/a
# high card             value = max(value)                  suites = n/a

def best_hand(table, hand):
    values = []
    suits =[] 
    for card in table, hand:
        for properties in card:
            values.append(properties[0])
            suits.append(properties[1])
            

    # print values
    # print suits


    high_flush = [10, 11, 12, 13, 1]
    if high_flush in values and 



# def card_view():



def main():
    generate_game()
    best_hand(table, hand)



if __name__ == '__main__':
    main()












