'''
1) Транспонирование
2) Повышение дискретизации методами:
a) Среднего значения
б) Ближайшего соседа
в) Билинейной интерполяцией
3) Повышение/понижение яркости на заданное значение
4) Операцию свертки
'''
import math

def Neighbor(matrix, width, height):
    newMatrix = []
    kHeight = len(matrix)/height
    kWidth = len(matrix)/width
    for i in range(1024):
        buffer = []
        for j in range(1024):
            buffer.append(matrix[math.trunc(kWidth * i)][math.trunc(kHeight * j)])
        newMatrix.append(buffer)
    return newMatrix

