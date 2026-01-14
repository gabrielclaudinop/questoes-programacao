qntd_casos = int(input())

poderes = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
    'y': 100
}

for i in range(qntd_casos):
    nome1, nome2 = input().split()

    qntd_poder_nome1 = 0
    for caracter in nome1:
        qntd_poder_nome1 += poderes.get(caracter, 0)
    
    qntd_poder_nome2 = 0
    for caracter in nome2:
        qntd_poder_nome2 += poderes.get(caracter, 0)
    
    if qntd_poder_nome1 > qntd_poder_nome2:
        print(nome1)
    elif qntd_poder_nome2 > qntd_poder_nome1:
        print(nome2)
    else:
        print('naruto')