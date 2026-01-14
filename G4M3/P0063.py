qntd_antenas = int(input())
frequencias = list(map(int, input().split()))

frequencias.sort()

forma_progressao = True
diferenca_inicial = frequencias[1] - frequencias[0]
for i in range(1, qntd_antenas):
    if frequencias[i] - frequencias[i-1] != diferenca_inicial:
        forma_progressao = False
        break

print(str(forma_progressao).upper())