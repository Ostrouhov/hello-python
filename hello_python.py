print('--- Task 1 ---')
print(2+2, 37/10, 37//10, 37%10)

"""
1. Оператор добавления,
2. Оператор деления,
3. Оператор целочисленного деленяи,
4. Оператор взятия остатка от деления.
"""

#####

print('--- Task 2 ---')
print('Hello world')

#####

print('--- Task 3 ---')
a = 3
print(type(a)) # int
a = 3.5
print(type(a)) # float
a = 'qwerty'
print(type(a)) # string
a = True
print(type(a)) # bool
a = '123'
print(type(a)) # string

"""
Если в конце попытаться к "a" прибавить число,
то получим ошибку, т.к. с переменной типа "string" нельзя
проводить математические операции с типом "int".
"""

#####

print('--- Task 4 ---')
print(int(5.7), int(-5.7), 3**39 - int(float(3**39)))

#####

print('--- Task 5 ---')
name = input('Введите ваше имя: ')
print('Здравствуйте, ', name)

#####

print('--- Task 6 ---')
x, y = input('Введите X и Y (через запятую): ').split(',')
print(f'Доктор Иванов {int(x) * 60 + int(y)} минут находится в пути.')

#####

print('--- Task 6* ---')
print(sum([int(input("Введите X (часы до клиники): ")) * 60, int(input("Введите Y (минуты после обеда): "))]))

#####

print('--- Task 7 ---')
a, b, c = False, True, False
print(not (a or b) and c)

#####

print('--- Task 8 ---')
year = int(input('Введите год: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('С днём рождения!')
elif (year < 1900) or (year > 3000):
    print('Год не входит в выборку!')
else:
    print('Год обычный!')

#####

print('--- Task 9 ---')
a = 2
while a < 21:
    print(a, end=' ')
    a += 2
print('\n')

#####

print('--- Task 10 ---')
res = 0
while(True):
    num = int(input('Введите число: '))
    if (num == 0):
        print(res)
        break
    res += num

#####

print('--- Task 11 ---')
import math
x = int(input('Введите X: '))
y = int(input('Введите Y: '))
print('Нужно кусков: ', (x * y) // math.gcd(x, y))

#####

print('--- Task 12 ---')
for i in range(2, 21, 2): print(i, end=' ')
print('\n')

#####

print('--- Task 13 ---')

a, b, c, d = [int(input()) for i in range(4)]
print('', end='\t')
for j in range(c, d + 1):
    print(j, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()

#####

print('--- Task 14 ---')

n = int(input('Введите размер матрицы: '))
matrix = [[0] * n for _ in range(n)]
num = 1
left, right, top, bottom = 0, n - 1, 0, n - 1

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for row in matrix:
    for num in row:
        print(num, end='\t')
    print()

#####

print('--- Task 15 ---')

import time
from tkinter import messagebox

if __name__ == '__main__':
    while(True):
        time.sleep(5)
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')