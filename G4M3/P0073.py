def simbolo_ganhou(jogo):
    linha0 = [simbolo for simbolo in jogo[0]]
    linha1 = [simbolo for simbolo in jogo[1]]
    linha2 = [simbolo for simbolo in jogo[2]]

    coluna0 = [linha[0] for linha in jogo]
    coluna1 = [linha[1] for linha in jogo]
    coluna2 = [linha[2] for linha in jogo]

    diagonal_principal = [jogo[i][i] for i in range(len(jogo))]
    diagonal_secundaria = [jogo[i][len(jogo)-1-i] for i in range(len(jogo)-1, -1, -1)]
    
    fileiras_simbolos_unicos = list(map(lambda fileira: list(set(fileira)), 
                            [linha0, linha1, linha2,
                             coluna0, coluna1, coluna2,
                             diagonal_principal, diagonal_secundaria]
                            ))
    
    for fileira in fileiras_simbolos_unicos:
        if len(fileira) == 1 and fileira[0] != '.':
            return True
    
    return False

def computar_vitorias_jogo(jogo, celulas_vazias, jogador_atual):
    novas_celulas_vazias = celulas_vazias.copy()

    global qntd_vitorias_x
    global qntd_vitorias_o

    for i in range(len(celulas_vazias)):
        celula = celulas_vazias[i]
        novas_celulas_vazias = celulas_vazias[:i] + celulas_vazias[i+1:]
        novo_jogo = [linha.copy() for linha in jogo]
        linha = celula[0]
        coluna = celula[1]

        if jogador_atual == 'X':
            novo_jogo[linha][coluna] = 'X'
            if simbolo_ganhou(novo_jogo):
                qntd_vitorias_x += 1
            else:
                computar_vitorias_jogo(novo_jogo, novas_celulas_vazias, 'O')
        
        if jogador_atual == 'O':
            novo_jogo[linha][coluna] = 'O'
            if simbolo_ganhou(novo_jogo):
                qntd_vitorias_o += 1
            else:
                computar_vitorias_jogo(novo_jogo, novas_celulas_vazias, 'X')

jogo_inicial = [list(input()), list(input()), list(input())]

celulas_vazias = []
for i in range(0, 3):
    for j in range(0, 3):
        simbolo_celula = jogo_inicial[i][j]
        if simbolo_celula == '.':
            celulas_vazias.append([i, j])

if len(celulas_vazias) % 2 == 1:
    jogador_atual = 'X'
else:
    jogador_atual = 'O'

qntd_vitorias_x = 0
qntd_vitorias_o = 0

computar_vitorias_jogo(jogo_inicial, celulas_vazias, jogador_atual)

print(qntd_vitorias_x, qntd_vitorias_o)