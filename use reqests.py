import requests
import pprint

params = {
    'q' : 'python'
}

response = requests.get('https://api.github.com/search/repositories', params = params)

response_json = response.json()
pprint.pprint(response_json)

