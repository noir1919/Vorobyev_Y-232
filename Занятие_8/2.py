
# Вариант 14

def set(point):
    x = int(input(f'Введите первую координату точку {point}: '))
    y = int(input(f'Введите вторую координату точку {point}: '))
    result = {'x': x,'y': y}
    return result

def cords():
    lst = ['X','Y','Z','P']
    points = {} 
    for i in lst:
        points[i] = (set(i))
    return points

def calculate(x1,x2,y1,y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

def dist():
    result = {}
    points = cords()
    keys = list(points.keys())
    for a in range(len(keys)):
        for b in range(a+1,len(keys)):
            key1,key2 = keys[a],keys[b]
            point1,point2 = points[key1],points[key2]
            x1,y1 = point1['x'],point1['y']
            x2,y2 = point2['x'],point2['y']
            calc = calculate(x1,x2,y1,y2)
            result[key1,key2] = calc
    return result

def main():
    distances = dist()
    max_value = max(distances.values())
    max_key = max(distances, key=lambda maxkey: distances[maxkey])
    points = ' и '.join(map(str, max_key))
    print(f'Наибольшее расстояние между точками {points}: {max_value}')

main()
