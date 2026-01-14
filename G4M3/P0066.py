tamanho = int(input())

matriz = []
for i in range(tamanho):
    linha = input().split()
    matriz.append(linha)

i = j = tamanho//2
qntd_voltas = tamanho//2

sequencia = [matriz[i][j]]
for volta in range(qntd_voltas):
    i, j = i, j+1
    sequencia.append(matriz[i][j])

    for l in range(1+volta*2):
        i, j = i-1, j
        sequencia.append(matriz[i][j])
    
    for l in range((volta+1)*2):
        i, j = i, j-1
        sequencia.append(matriz[i][j])

    for l in range((volta+1)*2):
        i, j = i+1, j
        sequencia.append(matriz[i][j])

    for l in range((volta+1)*2):
        i, j = i, j+1
        sequencia.append(matriz[i][j])

print(" ".join(sequencia))