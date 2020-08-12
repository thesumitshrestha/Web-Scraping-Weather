import json

import requests
from bs4 import BeautifulSoup

page = requests.get('https://scrapingclub.com/exercise/detail_json/')
soup = BeautifulSoup(page.content, 'html.parser')

scripts = soup.find_all('script')
script = scripts[4]

print(str(json.loads(str(script))))
