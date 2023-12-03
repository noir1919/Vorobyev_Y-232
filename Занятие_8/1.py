
# Вариант 14

def nums():
    b = int(input('Введите начальное число интервала: '))
    e = int(input('Введите конечное число интервала: '))
    if b > e:
        print('Неверный интервал')
        return nums()
    else:
        return b,e

def count(number):
    x = 0
    for i in range(1,number+1):
        if number % i == 0:
            x += 1
    return x

def divis(tuple):
    a,b = tuple
    max = 0
    numbers = []
    for i in range(a,b+1):
        divisors = count(i)
        if divisors > max:
            max = divisors
            numbers = [i]
        elif divisors == max:
            numbers.append(i)
    result = ', '.join(map(str, numbers))
    return result

print(f'Числа, имеющие наибольшее кол-во делителей: {divis(nums())}')
