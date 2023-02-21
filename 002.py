import requests
from bs4 import BeautifulSoup

req = requests.get('https://medium.com/horadecodar/como-fazer-webscraping-com-python-e-beautiful-soup-28a65eee2efd')

site = BeautifulSoup(req.content, 'html.parser')

titulo = site.find('h1', attrs={'class': 'pw-post-title hf hg hh bd hi hj hk hl hm hn ho hp hq hr hs ht hu hv hw hx hy hz ia ib ic id bi'})

print(titulo.text)