"""
Teste Prático Python Maio de 2022

2) Retornar a temperatura atual de um CEP específico
getTemperature (CEP)
Ex: getTemperature (“95020-360”)
Retorna a temperatura atual no local do CEP especificado
Você pode utilizar mais de uma API ou webservice de CEP e previsão do tempo.
Fique à vontade para escolher.
"""
import requests

def main():
    print('#######################################')
    print('                                       ')
    print('    Consulta de temperatura por CEP    ')
    print('                                       ')

    CEP = input('Digite o CEP para a consulta, somente números: \n')

    if len(CEP) != 8:
        print('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(CEP))
    #   Consultando o endereço de um CEP em uma api específica
    address_data = request.json()

    if 'erro' not in address_data:
        print()
        print('==> CEP ENCONTRADO <==')
        API_KEY = "214be6e403df9108e60a54ee8a7db500"
        requisicao2 = requests.get('https://viacep.com.br/ws/{}/json/'.format(CEP))
        requisicao_dic = requisicao2.json()
        #   A variavel requisicao_dic serve para armazenar as informações contidas no json, serve como dicionário
        localidade = requisicao_dic['localidade']
        bairro = requisicao_dic['bairro']
        uf = requisicao_dic['uf']
    #   Extraindo os parâmetros localidade, bairro e uf, da primeira API que utilizamos para buscar o endereço por CEP

        link = f"https://api.openweathermap.org/data/2.5/weather?q={localidade}&appid={API_KEY}&lang=pt_br"
    #   Utilizando a localidade encontrada na primeira API, para buscar a temperatura em uma segunda API
    #   Quem não tem cão, caça com gato

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        #   Reuisição para pegar as informações do clima na localidade dentro da segunda API
        temperatura = int(requisicao_dic['main']['temp'] - 273.15)  #  -273.15 = Conversão de Kelvin para Celsius
        #   Requisição para pegar as informações de temperatura e descrição do clima dentro da segunda API
        print()
        print(f"Atualmente em {bairro}-{uf}, o clima está com {descricao}", f"e a temperatura é de {temperatura}ºC.")


    else:
        print('{}: CEP inválido.'.format(CEP))

    print('')
    option = int(input('Deseja realizar uma nova consulta?\n1 = Sim;\n2 = Sair.\n'))

    if option == 1:
        main()
    else:
        print('O estagiário agradece a sua consulta e aguarda seu retorno!')
    #   Se option = 1, libera uma nova consulta. Se = 2, finaliza o script.
if __name__ == '__main__':
    main()