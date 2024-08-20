#Задача 1:

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

#Задача 2:

import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y, alpha=0.5, color='red')
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Задача 3:

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.divan.ru/category/divany-i-kresla'

driver.get(url)

time.sleep(3)

Divans = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

for divan in Divans:
    try:
        price = divan.find_element(By.CLASS_NAME, 'pY3d2').text
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([price])

driver.quit()

with open('Divans.csv','w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)

#Обработка:

import pandas as pd
import matplotlib.pyplot as plt
import re

# Чтение данных из CSV файла
df = pd.read_csv('Divans.csv')

# Функция для извлечения второй цены
def extract_second_price(raw_price):
    # Ищем все вхождения цен в формате числа с пробелами
    prices = re.findall(r'\d+\s\d+', raw_price)
    if len(prices) > 1:
        # Преобразуем вторую найденную цену в число
        return int(prices[1].replace(' ', ''))
    return None

# Применяем функцию к каждому элементу в колонке 'Цена'
df['Price'] = df['Цена'].apply(extract_second_price)

# Удаляем строки с невалидными данными
df = df.dropna(subset=['Price'])

# Нахождение средней цены
average_price = df['Price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} ₽")

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()