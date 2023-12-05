def create_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [0] * columns
        matrix += [row]
    return matrix


def update_matrix(matrix):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            matrix[c][r] = int(
                input(f'Insira um valor para o elemento {c, r} da matriz: '))
    return matrix


def sum_matrix(matrix1, matrix2):
    matrix_sum = create_matrix(len(matrix1), len(matrix1[0]))
    for c in range(len(matrix1)):
        for r in range(len(matrix1[0])):
            matrix_sum[c][r] = matrix1[c][r] + matrix2[c][r]
    return matrix_sum


# a function that creates a identity matrix

def identity_matrix(n):
    matrix = create_matrix(n, n)
    for c in range(n):
        for r in range(n):
            if c == r:
                matrix[c][r] = 1
    return matrix

# a function that create transpose matrix


def transpose_matrix(matrix):
    matrix_transpose = create_matrix(len(matrix[0]), len(matrix))
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            matrix_transpose[r][c] = matrix[c][r]
    return matrix_transpose


m1 = create_matrix(2, 2)
m2 = create_matrix(2, 2)

update_matrix(m1)
update_matrix(m2)

print(sum_matrix(m1, m2))


def print_matrix(matrix):
    for row in matrix:
        print(row)
