# Вариант 14

stroke = str(input('Введите строку: '))

def count(s):
    split = s.split()
    result = []
    for i in split:
        if i[0].lower() == 'а' and i[-1].lower() == 'я':
            result.append(i)
    return result

def result(list):
    message = "\nСписок слов начинающихся на 'а' и заканчивающихся на 'я':\n"
    for i in list:
        message += f'{i}\n'
    return message

print(result(count(stroke)))
