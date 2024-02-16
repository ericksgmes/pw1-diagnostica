def print_matrix_with_indices(matrix):
    # Loop over each row
    for i in range(len(matrix)):
        # Loop over each column in the current row
        for j in range(len(matrix[i])):
            # Print element at row i, column j
            print(matrix[i][j], end=' ')
        # Print a new line after each row
        print()

def input_matrix():
    param = [[8,3,4], [1,5,9], [6,7,2]]
    matrix = []
    for i in range(len(param)):
        m = []
        for j in range(len(param[i])):
            m.append(int(input(f"Insira o número da matriz na posição {i};{j}: ")))
        print()
        matrix.append(m)
    return matrix

matriz = [[8,3,4], [1,5,9], [6,7,2]]

#print_matrix_with_indices(matriz)

print(input_matrix())
