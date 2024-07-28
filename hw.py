import requests

# Задаем URL API
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода и содержимого ответа
print(f"Статус-код: {response.status_code}")
print("Содержимое ответа:")
print(response.json())