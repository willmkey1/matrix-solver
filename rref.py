import re
import sys

def get_matrix():
    matrix = []
    rowf = []

    inp = input("Enter First Row or Type 'q' to Quit\n")

    if inp == 'q':
        sys.exit()

    row = re.findall(r'-\d+|\d+', inp)
    length = len(row)

    if length == 0:
        print("Invalid Length")
        get_matrix()

    for i in row:
        rowf.append(float(i))

    matrix.append(rowf)

    while inp != "f":
        rowf = []

        inp = input("Enter Next Row or Type 'f' to Finish\n")
        if inp == "f":
            break
        row = re.findall(r'-\d+|\d+', inp)
        if len(row) != length:
            print("Invalid Length")
            continue

        for i in row:
            rowf.append(float(i))

        matrix.append(rowf)

    return matrix

def row_op(row1, row2, index):
    factor = row2[index] / row1[index]
    
    for i in range(len(row1)):
        row2[i] = row2[i] - (row1[i] * factor)

    return row2

def calc_ref(matrix):
    for row_ind_1 in range(len(matrix)):
        for col_index in range(len(matrix[row_ind_1])):
            if matrix[row_ind_1][col_index] == 0 or col_index == len(matrix[row_ind_1]) - 1:
                continue
            for row_ind_2 in range(len(matrix)):
                if row_ind_2 == row_ind_1:
                    continue
                row_op(matrix[row_ind_1], matrix[row_ind_2], col_index)
            break
    return matrix

def calc_rref(matrix):
    for row_ind_1 in range(len(matrix) - 1, -1, -1):
        for col_index in range(len(matrix[row_ind_1])):
            if matrix[row_ind_1][col_index] == 0 or col_index == len(matrix[row_ind_1]) - 1:
                continue
            pivot = matrix[row_ind_1][col_index]
            for i in range(len(matrix[row_ind_1])):
                matrix[row_ind_1][i] = matrix[row_ind_1][i] / pivot
            for row_ind_2 in range(len(matrix) -1, -1, -1):
                if row_ind_2 == row_ind_1:
                    continue
                row_op(matrix[row_ind_1], matrix[row_ind_2], col_index)
            break

    for i in range(len(matrix)):
        final_count = 999
        for row_index in range(i, len(matrix)):
            count = 0
            for col_index in range(len(matrix[row_index])):
                if matrix[row_index][col_index] == 0:
                    count += 1
                    continue
                else:
                    break
            if count < final_count:
                final_count = count
                highest_row_ind = row_index
        buffer_row = matrix[i]
        matrix[i] = matrix[highest_row_ind]
        matrix[highest_row_ind] = buffer_row

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row, sep='\n')

while True:
    print_matrix(calc_rref(calc_ref(get_matrix())))
