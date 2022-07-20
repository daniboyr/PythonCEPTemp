# 3) Salva um arquivo Excel (XLS) com a lista de links presentes em uma URL

import requests
from bs4 import BeautifulSoup
import re
import validators

def main():
    print('')
    url = input ('Informe uma URL: \n')
    valid=validators.url(f'{url}')
    if valid==True:
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

    result = []
    for i in links:
        if i not in result:
            result.append(i)

    for link in result:
        print(link)

if __name__ == '__main__':
    main()