import requests
from bs4 import BeautifulSoup

req = requests.get('https://g1.globo.com/')

cont = req.content

site = BeautifulSoup(cont, 'html.parser')