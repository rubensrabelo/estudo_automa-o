import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

req = requests.get('https://g1.globo.com/')

cont = req.content

site = BeautifulSoup(cont, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in  noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    titulo2 = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    linkTitulo = titulo['href']
    
    #print(titulo.text)
    #print(linkTitulo)

    if (titulo2):    
        #print(titulo2.text)
        #print(linkTitulo2 = titulo2['href'])
        lista_noticias.append([titulo.text, linkTitulo, titulo2.text])
    else:
        lista_noticias.append([titulo.text, linkTitulo, ''])

    #print()

#print(lista_noticias)

df = pd.DataFrame(lista_noticias, columns=['Título', 'Link', 'Titulo2'])

df.to_excel('noticias.xlsx', index=False)