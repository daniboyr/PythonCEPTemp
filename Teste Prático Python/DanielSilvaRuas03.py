"""
3) Salva um arquivo Excel (XLS) com a lista de links presentes em uma URL
getLinks(URL, depth, fileName)

Ex: getLinks(“https://enttry.com.br/contato”, 2, “linksEnttry.xls”)
Descobre todos os links/urls contidos na página apontada por URL.

Salva um arquivo Excel (XLS) com o nome passado em fileName

Colunas do Excel a ser retornado: “link” (url absoluta do link),
”atualTime”(hora que o link foi encontrado).

Um link não deve ser inserido mais de uma vez na listagem.

O parâmetro depth indica quantos níveis devemos descer na procura

Ex: (0) Somente os links contidos na página URL, (1) Todos de URL e os que estão nas páginas que estão na lista de links de URL (2) Todos os anteriores e mais os que estão nas páginas abertas dos links anteriores....
E assim continua descendo a profundidade de acordo com o número informa
"""

import requests
from bs4 import BeautifulSoup
import re
import validators
import pandas as pd
from datetime import datetime


def main():
    print('')
    url = input('Informe uma URL: \n')
    valid = validators.url(f'{url}')

    if valid == True:
        print('Parabéns! A sua URL é válida!')

    else:
        print('Oops. Você não informou uma URL válida.')
        print('#######################################')

        main()

    links = []
    website = requests.get(url)
    website_texto = website.text
    soup = BeautifulSoup(website_texto)

    for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
        links.append(link.get('href'))

    # Filtro para não duplicar os resultados de links encontrados
    result = []
    for i in links:
        if i not in result:
            result.append(i)
    for link in result:
        print(link)

    planilha = {
        "URL": [],
        "Horario": [],
    }

    for meta in links:
        horario = datetime.today().strftime('%H:%M:%S')
        planilha['URL'].append(meta)
        planilha['Horario'].append(horario)

    planilha = pd.DataFrame(data=planilha)
    planilha.to_excel('DanielSilvaRuas03.xls', index=False)
    print(planilha)

if __name__ == '__main__':
    main()

