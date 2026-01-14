qntd_numeros = int(input())
numeros = list(map(int, input().split()))

sinal = 1
for i in range(qntd_numeros-1, -1, -1):
    if numeros[i] < 0:
        sinal *= -1
    numeros[i] = str(numeros[i] * sinal)

print(" ".join(numeros))