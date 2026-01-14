qntd_linhas = int(input())

qntd_caracteres_imprimidos = 0
for i in range(qntd_linhas):
    linha = input()
    if qntd_caracteres_imprimidos + len(linha) > 144:
        break
    else:
        print(linha)
        qntd_caracteres_imprimidos += len(linha)