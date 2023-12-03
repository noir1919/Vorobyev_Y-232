
# Вариант 6

MATRIX = [
        [1,2,3,],
        [4,5,6,],
        [7,8,9],
        ]

def diags(matrix):
    result = {}
    maindiag = {}
    seconddiag = {}
    center = 0
    x = 0
    for i in range(len(matrix)):
        maindiag[i,x] = matrix[i][x]
        x += 1
    result.update(maindiag)
    x = 0
    for i in reversed(range(len(matrix))):
        seconddiag[i,x] = matrix[i][x]
        x += 1
    result.update(seconddiag)
    max_value_index = max(result, key=lambda maxindex: result[maxindex])
    for a in maindiag.keys():
        for b in seconddiag.keys():
            if a == b:
                center = a
    return max_value_index,center

def swap(lst,matrix):
    max,cent = lst
    x1,y1 = max
    x2,y2 = cent
    matrix[x1][y1],matrix[x2][y2] = matrix[x2][y2],matrix[x1][y1]
    return matrix

def disp(matrix):
    for i in matrix:
        result = ' '.join(map(str,i))
        print(result)

def main(matrix):
    print(f'Матрица до перестановки:\n')
    disp(matrix)
    print(f'\nМатрица после перестановки:\n')
    disp(swap(diags(matrix),matrix))

main(MATRIX)
