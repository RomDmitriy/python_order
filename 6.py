# для перевода строки координат в tuple
from ast import literal_eval as make_tuple
# pip install pillow
from PIL import Image, ImageDraw  # для работы с изображениями

text = str('Hi')  # текст, который кодируем

# Пункт 1.1. Декодирование
img = Image.open('new24.png')  # открываем изображение
coordinates = open('keys24.txt')  # открываем координаты
values = []
for coordinate in coordinates:  # foreach для coordinates
    # make_tuple переводит str в tuple
    # добавляем значение синего (синий потому что так сказано в задании) в массив
    values.append(img.getpixel(make_tuple(coordinate))[2])

for i in range(len(values)):  # перебираем элементы массива values
    values[i] = chr(values[i])  # преобразовываем коды символов в символы
print(''.join(values))  # выводим (join объединяет элементы массива)


# Пункт 1.2. Кодирование и декодирование
bits = []  # массив для хранения битов исходного текста
# преобразовываем текст в двоичное представление
for char in text:  # перебираем символы исходного текста
    char_bits = ord(char)  # получаем UNICODE символа
    # переводим число в двоичную систему счисления
    char_bits = format(char_bits, 'b').zfill(8)
    for char in char_bits:  # перебираем символы
        bits.append(char)  # добавляем каждый бит в массив

# считаем сколько пикселей нам понадобится
# в один пиксель мы помещаем по 2 бита
amount = int(len(bits) / 2)

draw = ImageDraw.Draw(img)  # создаем эксемпляр картинки, чтобы на ней рисовать

# массивы для хранения исходных цветов
original_red = ''
original_green = ''
original_blue = ''
code_file = open('codes_crypted.txt', 'w')
# начинаем шифрование
i = 0
j = 0
for k in range(amount):
    code_file.write('(' + str(j) + ',' + str(i) + ')\n')
    # если нам все еще нужны пиксели
    pixel = img.getpixel((j, i))  # берем пиксель
    # zfill заполняет нулями слева до нужного количества
    # переводим исходный красный цвет в двоичный вид и сохраняем в массив
    original_red += format(pixel[0], 'b').zfill(8) + ' '
    # переводим исходный зеленый цвет в двоичный вид и сохраняем в массив
    original_green += format(pixel[1], 'b').zfill(8) + ' '
    # переводим исходный синий цвет в двоичный вид и сохраняем в массив
    original_blue += format(pixel[2], 'b').zfill(8) + ' '

    # вшиваем информацию
    coded_pixel = format(pixel[0], 'b').zfill(8)  # преобразуем в двоичный вид
    # получаем coded_pixel без двух последних символов
    coded_pixel = coded_pixel[:-2]
    # добавляем в конец два бита (* 2 потому что в один пиксель записываем два бита)
    coded_pixel += bits[k * 2] + bits[k * 2 + 1]
    # сохраняем в пиксель новую информацию, переведя в десятичное число
    new_pixel = int(coded_pixel, 2)
    # рисуем точку
    draw.point((j, i), (new_pixel, pixel[1], pixel[2], pixel[3]))
    j += 1  # переходим к следующему пикселю

    if j == img.width - 1:  # если это был последний пиксель в строке
        i += 1  # переходим на новую строку
        j = 0  # начинаем с первого пикселя по горизонтали

code_file.close()  # закрываем файл с координатами
img.save('img_crypted.png', 'PNG')  # сохраняем зашифрованную картинку
img.close()  # закрываем картинку

# начинаем дешифрование
coordinates = open('codes_crypted.txt')
img = Image.open('img_crypted.png')
crypted_red = ''
crypted_green = ''
crypted_blue = ''
interaction = 0
letter = ''
result = ''
for coordinate in coordinates:
    # из координаты берём значение цветов
    value = img.getpixel(make_tuple(coordinate))
    # берем битовое представление КРАСНЫЙ
    red = format(int(value[0]), 'b').zfill(8)
    # берем битовое представление ЗЕЛЁНЫЙ
    green = format(int(value[1]), 'b').zfill(8)
    # берем битовое представление СИНИЙ
    blue = format(int(value[2]), 'b').zfill(8)
    crypted_red += red + ' '  # запоминаем красный
    crypted_green += green + ' '  # запоминаем зелёный
    crypted_blue += blue + ' '  # запоминаем синий
    # берем два последних разряда значения КРАСНЫЙ
    # массив[<отступ>::<шаг>]
    letter += format(value[0], 'b')[-2::1]
    interaction += 2  # увеличиваем счетчик битов на 1
    if interaction == 8:  # если собрали достаточно бит для символа
        interaction = 0  # обнуляем таймер
        result += chr(int(letter, 2))  # сохраняем новую букву
        letter = ''  # очищаем биты записанной буквы


# вывод
print('Сообщение:', bits)
print('Изначальный красный: ', original_red)
print('Измененный красный:  ', crypted_red)
print('Изначальный зеленый: ', original_green)
print('Измененный зеленый:  ', crypted_green)
print('Изначальный голубой: ', original_blue)
print('Измененный голубой:  ', crypted_blue)
print('Расшифрованный текст:', result)