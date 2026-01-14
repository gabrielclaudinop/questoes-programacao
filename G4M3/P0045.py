dimensao, qntd_bombas = map(int, input().split())

tabuleiro = []
for i in range(dimensao+2):
    linha = [0]*(dimensao+2)
    tabuleiro.append(linha)

bombas_podem_ser_inseridas = True
for i in range(qntd_bombas):
    x_bomba, y_bomba = map(lambda cord: int(cord)+1, input().split())
    for x_adj in range(x_bomba-1, x_bomba+2):
        for y_adj in range(y_bomba-1, y_bomba+2):
            if x_adj == x_bomba and y_adj == y_bomba:
                continue
            elif tabuleiro[x_adj][y_adj] == 4:
                bombas_podem_ser_inseridas = False
                break
            else:
                tabuleiro[x_adj][y_adj] += 1

print(bombas_podem_ser_inseridas)