import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

# Faz a requisição para o site
response = requests.get('https://g1.globo.com/')
content = response.content

# Parseia o conteúdo HTML da página
site = BeautifulSoup(content, 'html.parser')

# Encontra todas as notícias na página
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

# Percorre todas as notícias encontradas
for noticia in noticias:
    # Extrai o título da notícia
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    if titulo and titulo.get('href'):
        print('Título:', titulo.text.strip())
        print('Link:', titulo['href'])

        # Extrai o tempo de publicação
        data = noticia.find('span', attrs={'class': 'feed-post-datetime'})
        print('Publicada:', data.text.strip())
        
        # Extrai todos os resumos da notícia, se houver
        resumos = noticia.findAll('div', attrs={'class': 'bstn-fd-relatedtext'})
        qtdResumos = 1
        if resumos:
            for resumo in resumos:
                # Remove o tempo de publicação do resumo, se presente
                data_resumo = resumo.find('span', attrs={'class': 'feed-post-datetime'})
                if data_resumo:
                    data_resumo.extract()  # Remove o span do tempo de publicação

                print(f'Resumo{qtdResumos}:', resumo.text.strip())
                qtdResumos += qtdResumos
            lista_noticias.append([titulo.text.strip(), resumo.text.strip(), data.text.strip(), titulo['href']])
        else: lista_noticias.append([titulo.text.strip(), '', data.text.strip(), titulo['href']])
        print()  # Adiciona uma linha em branco entre as notícias


print()

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Publicada', 'Link'])
news.to_excel('News.xlsx', index=False)
print(news)
