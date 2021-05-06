import requests
from bs4 import BeautifulSoup
n = 0
i = 0
op = ''

while op != 0:
    url = input('Digite um link: ')

    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    lista = []

    for link in soup.find_all('a'):
        n = n + 1
        lista.append(link.get('href'))
        if n >= 10:
            break
            
    for elemento in lista:
        i = i + 1
        print(elemento, i)

    num_link = int(input("Número do link que deseja acessar: "))

    novo_link = lista[num_link - 1]

    print(novo_link)

    novo_request = requests.get(novo_link)

    novo_soup = BeautifulSoup(novo_request.text, 'html.parser')

    palavra_chave = input("Digite uma palavra que deseja procurar: ")

    for palavra in novo_soup.find_all('p'):
        print(palavra_chave)

    op = int(input("Digite 0 se deseja encerrar o programa: "))
    
