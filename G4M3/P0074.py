qntd_max_caracteres = int(input())
palavra = input()

possui_numero = False
for caracter in palavra:
    if ord(caracter) >= ord('0') and ord(caracter) <= ord('9'):
        possui_numero = True
        break

if possui_numero:
    print(palavra, 'YES')
else:
    print(palavra, 'NO')