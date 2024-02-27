import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', {'id': 'example2'}).find('tbody').find_all('tr')

countries_list = []

for row in rows:
    countries = {}

    countries['Country'] = row.find_all('td')[1].text
    countries['Population in 2024'] = row.find_all('td')[2].text

    countries_list.append(countries)


df = pd.DataFrame(countries_list)
df.to_csv('countries_data.csv', index=False)