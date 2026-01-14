qntd_linhas, qntd_colunas = map(int, input().split())

matriz_original = []
for l in range(qntd_linhas):
    linha = list(input())
    matriz_original.append(linha)

for c in range(qntd_colunas):
    linha_transposta = []
    for l in range(qntd_linhas):
        linha_transposta.append(matriz_original[l][c])
    print("".join(linha_transposta))