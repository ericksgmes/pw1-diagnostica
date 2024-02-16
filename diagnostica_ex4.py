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
    matrix = []
    for i in range(3):
        m = []
        for j in range(3):
            m.append(int(input(f"Insira o número da matriz na posição {i};{j}: ")))
        print()
        matrix.append(m)
    return matrix



matrix = input_matrix()

print_matrix_with_indices(matrix)

