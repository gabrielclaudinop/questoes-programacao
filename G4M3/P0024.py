pilhas = [0, 0, 0, 0, 0]

pilhas[0] = int(input())
pilhas[1] = int(input())
pilhas[2] = int(input())
pilhas[3] = int(input())
pilhas[4] = int(input())

menor_pilha = min(pilhas)

qntd_blocos_destruidos = 0
for pilha in pilhas:
    qntd_blocos_destruidos += pilha - menor_pilha

print(qntd_blocos_destruidos)