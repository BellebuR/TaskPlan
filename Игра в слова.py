from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return {
            'english_words': english_words,
            'word_definition': word_definition
        }
    except:
        print('Произошла ошибка')

def translate_to_russian(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ru')
    return translation.text

def word_game():
    print('Добро пожаловать в игру!')
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        translated_definition = translate_to_russian(word_definition)

        print(f'Значение слова - {translated_definition}')
        user = input('Что это за слово? ')
        if user.lower() == word.lower():
            print('Всё верно!')
        else:
            translated_word = translate_to_russian(word)
            print(f'Ответ неверен, было загадано это слово - {translated_word} ({word})')

        play_again = input('Хотите сыграть ещё раз? y/n ')
        if play_again.lower() != 'y':
            print('Спасибо за игру!')
            break

word_game()