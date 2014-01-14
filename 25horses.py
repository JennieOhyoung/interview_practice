# Given 25 horses, find the fastest 3 with the least # of races. you can only race 5 at a time and you have no timer. 

import random
# import itertools
# import pdb

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def randomize_horses(x):
    random.shuffle(x)
    
# seperate horses into 5 groups/races
def first_five_rounds(x):
    # race = []
    global matrix
    matrix = []
    while x != []:
        matrix.append(x[:5])
        x = x[5:]
    for races in matrix:
        races.sort()
    return matrix

# program only has 30% accuracy of getting the fastest 3 (aka 1,2,3), so another round of race to make sure the fastest horses grouped in the same race during first_five_rounds are taken into consideration.
def sixth_round(matrix):
    global sixth
    sixth = []
    for races in matrix:
        sixth.append(races[0])
    sixth.sort()
    return sixth

# take the fastest 3 from sixth_round and compare with the fastest 2 from second places in first_five_rounds. 
def seventh_round(sixth, matrix):
    second_fastest = []
    for races in matrix:
        second_fastest.append(races[1])
    second_fastest.sort()

    seventh = []
    seventh.append(sixth[:3])
    # pdb.set_trace()
    seventh.append(second_fastest[:2])
    final = sum(seventh, []) # list(itertools.chain(*seventh))
    final.sort()
    return final[:3]


randomize_horses(x)
first_five_rounds(x)
sixth_round(matrix)
print seventh_round(sixth, matrix)

