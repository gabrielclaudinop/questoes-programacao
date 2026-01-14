qntd_paginas, qntd_palavras = map(int, input().split())

dicionario = {}
for i in range(1, qntd_paginas+1):
    pagina = input().split()
    for palavra in pagina:
        dicionario[palavra] = i

qntd_perguntas = int(input())
for i in range(qntd_perguntas):
    pergunta = input()
    print(pergunta, dicionario[pergunta])