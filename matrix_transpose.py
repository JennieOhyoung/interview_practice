# matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
matrix = [list("abcd"), list("efgh"), list("ijkl")]

# , list("mnop")

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print j,
        print


def transpose(matrix):
    transposed = []
    for i in range(len(matrix)):
        transposed.append([row[i] for row in matrix])
    return transposed

def transpose2(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed

def transpose3(matrix):
    return zip(*matrix)


# print_matrix(matrix)
# print 
print_matrix(transpose2(matrix))
