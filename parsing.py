from bs4 import BeautifulSoup
import requests

url = input('Введите URL на песню \n')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# заголовок
header = soup.find('h1').text
with open('Result.txt', 'a', encoding='utf-8') as file:
    print(header.upper(), file=file, end='\n \n')

# строчки
block = soup.find('div', class_='texts col')
rows = block.findAll('div', class_='string_container')

for row in rows:
    eng = row.find('div', class_='original').text
    rus = row.find('div', class_='translate').text
    with open('Result.txt', 'a', encoding='utf-8') as file:
        print(eng, ' --- ', rus, ' \n', file=file)
