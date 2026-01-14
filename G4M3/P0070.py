qntd_colunas = int(input())
linha1 = list(map(int, input().split()))
linha2 = list(map(int, input().split()))

maiores_valores = [str(max(linha1[col], linha2[col])) for col in range(qntd_colunas)]

print(" ".join(maiores_valores))