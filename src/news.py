import requests
from bs4 import BeautifulSoup

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
        #print('Link:', titulo['href'])
        
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

        # Extrai o tempo de publicação
        data = noticia.find('span', attrs={'class': 'feed-post-datetime'})
        print('Publicada:', data.text.strip())
        
        print()  # Adiciona uma linha em branco entre as notícias
