from random import randint  # генератор случайного числа

width = input('Введите ширину матрицы: ')  # спрашиваем ширину
width = int(width)  # получаем ширину
height = input('Введите высоту матрицы: ')  # спрашиваем высоту
height = int(height)  # получаем высоту

matrix = []  # объявляем матрицу

# инициализация матрицы (двумерный массив)
for i in range(height):
    matrix.append([])
    for j in range(width):
        matrix[i].append(0)

column_sums = [0] * width  # список сумм столбцов
row_sums = [0] * height  # список сумм строк

# перебираем элементы матрицы
for i in range(height):
    for j in range(width):
        matrix[i][j] = randint(10, 99)  # заполняем матрицу случайными числами
        row_sums[i] += matrix[i][j]  # считаем сумму строк (i - номер строки)
        # считаем сумму столбцов (i - номер столбца)
        column_sums[j] += matrix[i][j]

# перебираем элементы матрицы
for i in range(height):
    for j in range(width):
        print(matrix[i][j], end=('   '))  # выводим каждый элемент матрицы
    print(str(row_sums[i]))  # выводим сумму по строке
    print()  # добавим пустую строку

# перебираем суммы столбцов
for j in range(len(column_sums)):
    print(str(column_sums[j]), end='  ')  # выводим сумму столбца
