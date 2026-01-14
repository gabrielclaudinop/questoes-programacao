qntd_num = int(input())
numeros = list(map(int, input().split()))

valor_compra = numeros[0]
valor_venda = numeros[0]
lucro = 0
for n in numeros:
    if n < valor_compra:
        valor_compra = n
        valor_venda = -1
    elif n > valor_venda:
        valor_venda = n
        lucro = max(lucro, valor_venda - valor_compra)

print(lucro)