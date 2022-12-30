import wave  # для работы с wave файлами
import struct  # для распаковки амплитуды

# pip install matplotlib
import matplotlib.pyplot as plt  # для построения графиков
# pip install numpy
import numpy as np  # для манипуляции с большими массивами и матрицами

audio = wave.open('signal_24.wav', 'r')  # на чтение открываем аудио-файл

waves = []  # для хранения точек графика
nframes = audio.getnframes()  # количество фреймов в файле
framerate = audio.getframerate()  # количество фреймов в секунду
# считаем длину аудиофайла в миллисекундах
time = np.arange(0, nframes) * (1 / framerate) * 1000

for i in range(nframes):  # перебираем фреймы
    wave_data = audio.readframes(1)  # берем данные из одного фрейма
    # получаем амплитуду. "<h", где < - порядок байтов: little-endian; h - integer -32768 и 32767
    data = struct.unpack('<h', wave_data)
    waves.append(data[0])  # сохраняем в массив

# задаем границы гистограммы
# можно заменить границы, но важно, чтобы количество элементов совпадало
time = time[0:25]
waves = waves[0:25]

fig, ax = plt.subplots()  # настройка окна графика
ax.set_title('Гистограмма')  # название графика
ax.set_ylabel('Амплитуда сигнала')  # название оси Y
ax.set_xlabel('Время, мс')  # название оси X
# создаем гистограмму (time[1] - 1 можно увеличить, чтобы столбики были шире)
ax.bar(time, waves, width=(time[1] - time[0]))
# задаем границы графика (xmin, xmax, ymin, ymax)
plt.show()  # отобразить окно
