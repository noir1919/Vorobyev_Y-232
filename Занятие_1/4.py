seconds = int(input('Введите число секунд: '))
days = seconds // 86400
minutes = (seconds // 60) % 60
hours = (seconds // 3600)
seconds = seconds % 60
print(f'Дни: {days}\nМинуты: {minutes}\nЧасы: {hours}\nСекунды: {seconds}')
