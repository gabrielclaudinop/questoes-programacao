qntd_retalhos = int(input())
cores = input()

cor1 = cores[0]
cor2 = cores[0]
pos_cor1 = 0
pos_cor2 = 0

maior_tam = 0
tam_atual = 0
for i in range(qntd_retalhos):
    if cores[i] != cor1 and cores[i] != cor2:
        cor1, cor2 = cores[i-1], cores[i]
        pos_cor1, pos_cor2 = pos_cor2, i
        tam_atual = pos_cor2 - pos_cor1 + 1
    elif cores[i] != cores[i-1]:
        if cores[i] == cor1:
            pos_cor1 = i
        elif cores[i] == cor2:
            pos_cor2 = i
        tam_atual += 1
    else:
        tam_atual += 1
    maior_tam = max(maior_tam, tam_atual)

print(maior_tam)