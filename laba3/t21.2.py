def transpose(matrix):
    result = []
    global num_col
    global num_str
    for j_ in range(num_str):
        tmp = []
        for i_ in range(num_col):
            tmp += [matrix[i_][j_]]
        result += [tmp]
    return result


print('Заполните исходную матрицу:')
original_matrix = [[int(input()), int(input())], [int(input()), int(input())]]
num_col = len(original_matrix)
num_str = len(original_matrix[0])
tr_matrix = transpose(original_matrix)
for i in range(num_str):
    for j in range(num_col):
        print(tr_matrix[i][j], end=' ')
    print()
