tamanho_mapa = int(input())

matriz = []
matriz.append(['X']*(tamanho_mapa+2))
for i in range(tamanho_mapa):
    linha = list(input())
    matriz.append(['X'] + linha + ['X'])
matriz.append(['X']*(tamanho_mapa+2))

def verificar_inimigos_estao_cercados():
    for i in range(tamanho_mapa+1):
        for j in range(tamanho_mapa+1):
            if matriz[i][j] == 'M':
                if matriz[i-1][j] == '-' or matriz[i][j-1] == '-' or matriz[i+1][j] == '-' or matriz[i][j+1] == '-':
                    return (inimigos_estao_cercados := False)
    return (inimigos_estao_cercados := True)

if resposta := verificar_inimigos_estao_cercados():
    print('SUCCESS')
else:
    print('FAIL')