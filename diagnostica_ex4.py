def print_matrix_with_indices(matrix):
    # Loop over each row
    for i in range(len(matrix)):
        # Loop over each column in the current row
        for j in range(len(matrix[i])):
            # Print element at row i, column j
            print(matrix[i][j], end=' ')
        # Print a new line after each row
        print()

def input_matrix(n):
    matrix = []
    for i in range(n):
        m = []
        for j in range(n):
            m.append(int(input(f"Insira o número da matriz na posição {i};{j}: ")))
        print()
        matrix.append(m)
    return matrix

def quadrado_perfeito(matrix):
    diagonal_principal = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                diagonal_principal += matrix[i][j]

    diagonal_secundaria = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                diagonal_secundaria += matrix[i][j - i - 1]

    linhas = []
    for i in range(len(matrix)):
        soma = 0
        for j in range(len(matrix)):
                soma += matrix[i][j]
        linhas.append(soma)

        colunas = []
    for j in range(len(matrix)):
        soma = 0
        for i in range(len(matrix)):
                soma += matrix[i][j]
        colunas.append(soma)

    resLinhas = 1
    resColunas = 1
    for i in range(len(linhas)):
        if(linhas[i] != linhas[i-1]):
            resLinhas = 0
            break
        elif(colunas[i] != colunas[i -1]):
            resColunas = 0
            break
    
    resDiag = 1
    if(diagonal_principal != diagonal_secundaria):
        resDiag = 0
    
    if (resLinhas == resColunas):
            if(resLinhas == resDiag):
                 print("\nQuadrado mágico!")
    else:
         print("\nQuadrado não mágico")              
    


matriz = [[8,3,4], [1,5,9], [6,7,2]]

matrix = input_matrix(4)

print_matrix_with_indices(matrix)
quadrado_perfeito(matrix)

