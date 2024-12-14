# python -m venv venv
# venv\Scripts\activate
# pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup

url = 'https://vk.com'

response = requests.get(url)
text = response.text

print(text, end='\n\n') # или response.json

soup = BeautifulSoup(text, 'html.parser')
links = soup.find_all('div')
for link in links:
    print(link)