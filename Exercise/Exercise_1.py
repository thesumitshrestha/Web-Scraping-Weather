# You can choose the one you like to extract the info, in this exercise, try to extract this product detail such as title, desc and price.

from bs4 import BeautifulSoup
import requests

page = requests.get('https://scrapingclub.com/exercise/detail_basic/')
soup = BeautifulSoup(page.content, 'html.parser')
card_detail = soup.find(class_='card').get_text()
print(card_detail)
