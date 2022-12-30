import wave  # для работы с wave файлами
import struct  # для распаковки амплитуды
import math  # для математических операций

# pip install matplotlib
import matplotlib.pyplot as plt  # для построения графиков
# pip install numpy
import numpy as np  # для манипуляции с большими массивами и матрицами
# pip install scipy
from scipy.fft import fft, fftfreq

audio = wave.open('signal_24.wav', 'r')  # на чтение открываем аудио-файл

waves = []  # для хранения точек графика
nframes = audio.getnframes()  # количество фреймов в файле
framerate = audio.getframerate()  # количество фреймов в секунду
sampwidth = audio.getsampwidth()  # количество байт, требуемое на один фрейм
# считаем длину аудиофайла в миллисекундах
time = np.arange(0, nframes) * (1 / framerate) * 1000

for i in range(nframes):  # перебираем фреймы
    wave_data = audio.readframes(1)  # берем данные из одного фрейма
    # получаем амплитуду. "<h", где < - порядок байтов: little-endian; h - integer -32768 и 32767
    data = struct.unpack('<h', wave_data[:sampwidth])
    waves.append(data[0])  # сохраняем в массив

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)  # настройка окна графика
ax1.grid()  # добавляем сетку
ax1.set_title('Гистограмма')  # название графика
ax1.set_ylabel('Сигнал')  # название оси Y
ax1.set_xlabel('Время, мс')  # название оси X
# создаем гистограмму (time[1] - 1 можно увеличить, чтобы столбики были шире)
ax1.bar(time, waves, width=(time[1] - time[0]))
# спектральный анализ
fft_waves = fft(waves)  # Вычисление прямого ДПФ с помощью алгоритма БПФ
y_fft = []
for fft_wave in fft_waves:  # перебираем сэмплы
    real_part = np.real(fft_wave)  # берем действительную часть числа
    imag_part = np.imag(fft_wave)  # берем мнимую часть числа
    phase = math.atan(imag_part / real_part)  # считаем (формула дана в задании)
    y_fft.append(phase)  # сохраняем в массив
# (1.0 / framerate т.к. framerate это частота, а нам нужен период)
# оператор // - деление без остатка
x_fft = fftfreq(nframes, 1.0 / framerate)[0:nframes // 2]  # дискретные частоты в Герцах
y_fft = y_fft[0:nframes // 2]  # если этого не сделать, по получится галиматья
ax2.plot(x_fft, y_fft)  # задаем значения графика
ax2.set_title('Фаза ДПФ')  # название графика
ax2.set_ylabel('arct(Im/Re)')  # название оси Y
ax2.set_xlabel('Частота')  # название оси X
ax2.grid()  # добавляем сетку
abs_y = []
for fft_wave in fft_waves:  # перебираем сэмплы
    real_part = np.real(fft_wave)  # берем действительную часть числа
    imag_part = np.imag(fft_wave)  # берем мнимую часть числа
    abs_part = math.sqrt(real_part ** 2 + imag_part ** 2) # берем корень из суммы степеней действ. и мнимой части
    abs_y.append(abs_part)  # сохраняем в массив
abs_y = abs_y[:len(abs_y) // 2]  # если этого не сделать, по получится галиматья
ax3.plot(x_fft, abs_y)  # задаем значения графика
ax3.set_title('Модуль ДПФ')  # задаем значения графика
ax3.set_ylabel('arct(Re)')  # название оси Y
ax3.set_xlabel('Частота')  # название оси X
ax3.grid()  # добавляем сетку
plt.show()  # отобразить окно