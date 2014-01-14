
import random
# import pdb
# pdb.set_trace()

# mat = []
# coordinates = []
# h = 4
# w = 4
# b = None
# matrix = [list("....."), list("....."), list("....."), list("....."), list(".....")]
# matrix = [list("abcd"), list("efgh"), list("ihkl"),  list("mnop")]



# allow user to define size of game board and generate matrix of board
def generate_matrix():
    global h 
    h = int(raw_input("what is the height? "))
    global w 
    w= int(raw_input("what is the width? "))
    global mat
    mat = []
    row = []
    for i in range(w):
        row.append(" . ")
        mat.append(row)
    # print mat
    return h, w, mat

# allow user to set number of bombs in game and generate that number of bombs randomly, returns a set of non-repeating tuples.
def random_bombs(h, w):
    b = int(raw_input("how many bombs? "))
    star_row=[]
    star_col=[]

    for count in range(b):
        star_row.append(random.randint(0, h-1))
        star_col.append(random.randint(0, w-1))
        # star_row = random.randint(0, h-1)
        # star_col = random.randint(0, w-1)
        # mat[star_row][star_col] = '*'

    coordinates =  zip(star_row, star_col)
    global unique_coord
    unique_coord = set(coordinates)
    while len(unique_coord) < len(coordinates):
        x = random.randint(0, h-1)
        y = random.randint(0, w-1)
        unique_coord.add((x,y))
    print unique_coord
    return unique_coord

# replaces item on matrix list with * according to coordinates
def modify_matrix(unique_coord, mat):
    for pair in unique_coord:
        # print "x is " + str(pair[0]) + " y is " + str(pair[1])
        mat[pair[0]][pair[1]] = " * "
    # return mat


# draw mat visually to represent board
def draw_board(mat):
    for i in mat:
        for j in i:
            print j,
        print


# draw_board(generate_matrix(h,w,b))
generate_matrix()
random_bombs(h,w)
modify_matrix(unique_coord, mat)
draw_board(mat)


# format of mat is wrong. modify matrix is modifying every coloumn instead of individual cell. 
# I am appending the same row over and over again to mat til len(mat) is met.

    