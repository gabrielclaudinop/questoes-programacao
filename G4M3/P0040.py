while True:
    try:
        texto = input()
        posicao = texto.find('How')
        if posicao == -1:
            print(-1)
        else:
            print(posicao + 1)
    except:
        break