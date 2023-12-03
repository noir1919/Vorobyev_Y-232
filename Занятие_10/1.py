
# Вариант 6

def import_matrix():
    with open('Воробьев_Андрей_У-232_vvod_t1.txt','r') as file:
        txt = file.readlines()
        matrix = []
        for a in txt:
            lst = []
            for b in a.split():
                lst.append(int(b))
            matrix.append(lst)
        file.close()
    return matrix

def export_output(out):
    with open('Воробьев_Андрей_У-232_vivod_t1.txt','w') as file:
        file.write(out)
        file.close()

def max_in_stroke(matrix):
    result = []
    for i in matrix:
        result.append(max(i))
    return ', '.join(map(str,result))

def min_in_column(matrix):
    result = []
    for i in zip(*matrix):
        result.append(min(i))
    return ', '.join(map(str,result))

def main():
    matrix = import_matrix()
    maxval = max_in_stroke(matrix)
    minval = min_in_column(matrix)
    output = f'Максимальные значения в строках: {maxval}\nМинимальные значения в столбцах: {minval}'
    export_output(output)
    print(output)

main()
