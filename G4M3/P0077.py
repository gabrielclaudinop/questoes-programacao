numeros = list(map(int, input().split()))

menor, meio, maior = sorted(numeros)

if numeros[0] == menor and numeros[1] == meio and numeros[2] == maior:
    print(0)
elif numeros[0] == menor and numeros[1] == maior and numeros[2] == meio:
    print(1)
elif numeros[0] == meio and numeros[1] == menor and numeros[2] == maior:
    print(1)
elif numeros[0] == meio and numeros[1] == maior and numeros[2] == menor:
    print(2)
elif numeros[0] == maior and numeros[1] == menor and numeros[2] == meio:
    print(2)
else:
    print(3)

"""
Resultados para as permutações possíveis dos números 1 (menor), 2 (meio) e 3 (maior):
'1 2 3': 0
'1 3 2': 1
'2 1 3': 1
'2 3 1': 2
'3 1 2': 2
'3 2 1': 3
"""