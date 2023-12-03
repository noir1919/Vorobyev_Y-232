
# Вариант 6

MATRIX = [
        [1,6,3],
        [4,8,2],
        [7,9,4]
        ]

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

print(f'Максимальные значения в строках: {max_in_stroke(MATRIX)}\nМинимальные значения в столбцах: {min_in_column(MATRIX)}')
