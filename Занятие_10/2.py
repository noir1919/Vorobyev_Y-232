
# Вариант 6

def import_matrix():
    with open('Воробьев_Андрей_У-232_vvod_t2.txt','r') as file:
        txt = file.readlines()
        matrix = []
        for a in txt:
            lst = []
            for b in a.split():
                lst.append(int(b))
            matrix.append(lst)
        file.close()
    return matrix

def export_matrix(matrix):
    with open('Воробьев_Андрей_У-232_vivod_t2.txt','w') as file:
        for i in matrix:
            data = ' '.join(map(str,i))
            file.write(f'{data}\n')
        file.close()

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

def main():
    matrix = import_matrix()
    print(f'Матрица до перестановки:\n')
    disp(matrix)
    print(f'\nМатрица после перестановки:\n')
    new_m = swap(diags(matrix),matrix)
    disp(new_m)
    export_matrix(new_m)

main()
