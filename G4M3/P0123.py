qntd_rodadas = int(input())

pontos_andressa = 0
pontos_bianca = 0

jogadora_eh_andressa = True
for i in range(qntd_rodadas):
    carta = input()

    if jogadora_eh_andressa:
        if carta == 'A':
            pontos_andressa = 0
        elif carta == 'C':
            pontos_andressa = float('inf')
            break
        elif carta in set('XJQK'):
            pontos_andressa += 10
        else:
            pontos_andressa += int(carta)
        jogadora_eh_andressa = False

    else:
        if carta == 'A':
            pontos_bianca = 0
        elif carta == 'C':
            pontos_bianca = float('inf')
            break
        elif carta in set('XJQK'):
            pontos_bianca += 10
        else:
            pontos_bianca += int(carta)
        jogadora_eh_andressa = True

if pontos_andressa > pontos_bianca:
    print('ANDRESSA')
elif pontos_bianca > pontos_andressa:
    print('BIANCA')
else:
    print('EMPATE')