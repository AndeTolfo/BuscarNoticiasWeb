import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#trazendo a noticia inteira
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#trazendo somente o Titulo
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

#trazendo resumo notifica
resumo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})

#trazendo o tempo que foi publicado
data = noticia.find('span', attrs={'class': 'feed-post-datetime'})


#Para Trazer a Estrutura HTML
#print(noticia.prettify()) 

print(titulo.text)
print(resumo.text)
print(data.text)


