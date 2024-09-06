from flask import Flask, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # Запрашиваем случайную цитату из API
    response = requests.get('https://api.quotable.io/random')

    if response.status_code == 200:
        data = response.json()
        quote = data.get('content', 'No quote found')
        author = data.get('author', 'Unknown')
    else:
        quote = 'Could not retrieve a quote at this time'
        author = ''

    # HTML-шаблон для отображения цитаты
    template = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Random Quote</title>
      </head>
      <body>
        <h1>Random Quote</h1>
        <blockquote>
          <p>"{{ quote }}"</p>
          <footer>— {{ author }}</footer>
        </blockquote>
        <button onclick="window.location.reload();">Get Another Quote</button>
      </body>
    </html>
    '''

    return render_template_string(template, quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)