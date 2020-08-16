import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://www.bbc.com/weather/2643743")
soup = BeautifulSoup(page.content, 'html.parser')
main_div = soup.find('div', class_='wr-day-carousel')
items = main_div.find_all(class_='wr-day')

weather_descriptions = [item.find(class_='wr-day__weather-type-description').get_text() for item in items]
high_temperature = [item.find(class_='wr-day-temperature__high-value').get_text() for item in items]
low_temperature = [item.find(class_='wr-day-temperature__low-value').get_text() for item in items]
period_time = [item.find(class_='wr-day__title').get_text() for item in items]
weather = pd.DataFrame(
    {
        'date': period_time,
        'high': high_temperature,
        'temperature': low_temperature,
        'description': weather_descriptions
    }
)

print(weather)

weather.to_csv('weather.csv')
