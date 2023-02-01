# TraduPy.py

import requests

# lê o arquivo e conta a quantidade de caracteres
with open("generica.txt", "r") as file:
    text = file.read()
    char_count = len(text)
    file_size = file.tell()

# verifica se o arquivo possui menos de 500 bytes e 5000 caracteres
if file_size < 500 and char_count < 5000:
    continue_traducao = input("Arquivo possui menos de 500 bytes e 5000 caracteres. Deseja continuar? (s/n)")
    if continue_traducao == "n":
        exit()
else:
    print("Arquivo possui mais de 500 bytes ou 5000 caracteres. A tradução não será realizada.")
    exit()

# divide o texto em linhas
lines = text.splitlines()
translated_lines = []

# para cada linha, realiza a tradução para o português do Brasil
for line in lines:
    try:
        response = requests.get(f'http://api.mymemory.translated.net/get?q={line}&langpair=en|pt-br')
        response_json = response.json()
        translated_lines.append(response_json['responseData']['translatedText'])
    except KeyError as e:
        print(f"Erro na tradução da linha {lines.index(line) + 1}. Código de erro: {response_json['responseDetails']}")

# salva o resultado da tradução em um arquivo
with open("manual_traduzido.txt", "w") as file:
    file.write('\n'.join(translated_lines))
print("Texto traduzido com sucesso.")
