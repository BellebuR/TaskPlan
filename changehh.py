import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = 'https://saratov.hh.ru/vacancies/programmist'

driver.get(url)

time.sleep(3)

# Убедитесь, что классы верны и актуальны
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

parsed_data = []

# Ожидание до 10 секунд или до появления элемента
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span.vacancy-name--c1Lay3KouCl7XasYakLk"))
)

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')

        # Добавляем данные в список
        parsed_data.append([title, company, salary, link])
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

driver.quit()

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Оплата труда', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)