import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.divan.ru/category/svet'

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

for light in lights:
    try:
        name = light.find_element(By.CLASS_NAME, 'lsooF').text
        price = light.find_element(By.CLASS_NAME, 'pY3d2').text
        link = light.find_element(By.CSS_SELECTOR, 'a') .get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open('Svet.csv','w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название источника света', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)