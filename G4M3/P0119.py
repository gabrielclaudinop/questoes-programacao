mem_fat = {}
def fat(x):
    if x == 1:
        return 1
    
    if x in mem_fat:
        return mem_fat[x]
    
    mem_fat[x] = x * fat(x-1)
    return mem_fat[x]

def log_2(x):
    for potencia in range(0, 15):
        if 2**potencia == x:
            return potencia

    potencia_min = 0
    potencia_max = 14

    while True:
        potencia = (potencia_max+potencia_min)/2.0
        valor_atual = 2**potencia

        if x == valor_atual:
            return potencia
        
        if abs(x-valor_atual) < 0.00001:
            return potencia
        
        if x > valor_atual:
            potencia_min = potencia
        else:
            potencia_max = potencia

funcoes = {
    1: lambda x: x,
    2: lambda x: log_2(x),
    3: lambda x: x**0.5,
    4: lambda x: x*log_2(x),
    5: lambda x: x**2,
    6: lambda x: x**3,
    7: lambda x: 2**x,
    8: lambda x: fat(x),
}

l, r = map(int, input().split())
comandos = list(map(int, input().split()))

funcoes_usadas = []
for i in range(len(comandos)):
    if comandos[i]:
        funcoes_usadas.append(funcoes[i+1])
print()
for n in range(l, r+1):
    resultados = []
    for funcao in funcoes_usadas:
        resultado = int(funcao(n))
        if resultado > 9999999:
            resultados.append('9999999')
        else:
            resultados.append(str(resultado))
    print(" ".join(resultados))

"""
1 12
1 0 1 0 1 1 1 1

1 1 1 1 2 1
2 1 4 8 4 2
3 1 9 27 8 6
4 2 16 64 16 24
5 2 25 125 32 120
6 2 36 216 64 720
7 2 49 343 128 5040
8 2 64 512 256 40320
9 3 81 729 512 362880
10 3 100 1000 1024 3628800
11 3 121 1331 2048 9999999
12 3 144 1728 4096 9999999

x * log_2(x)
real: 10000 * 8.00002 = 80000.2
calc: 10000 * 8.00001 = 80000.1



Precisão 0.00001 3.1
"""