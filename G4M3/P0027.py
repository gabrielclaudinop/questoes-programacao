qntd_casos, tam_vetor = map(int, input().split())

for i in range(qntd_casos):
    vetor = list(map(int, input().split()))
    qntd_0 = 0
    qntd_pares = 0 #0s não serão contados aqui
    qntd_impares = 0

    for n in vetor:
        if n == 0:
            qntd_0 += 1
        elif n % 2 == 0:
            qntd_pares += 1
        else:
            qntd_impares += 1

    existe_permutacao = True
    if qntd_pares > 1:
        existe_permutacao = False
    elif qntd_0 and qntd_pares == 0 and qntd_impares != 0:
            existe_permutacao = False
    
    if existe_permutacao:
         print("=-)")
    else:
         print("=-(")

"""
Restrições para poder permutar:
- só pode haver no máximo um par diferente de 0
- se tiver algum 0:
    - 0s requerem ser os últimos números na permutação e deve ter um único par antes do primeiro 0
    - obs: 0 0 0 ... 0 0 0 funciona (ous seja, em vetor não há números pares nem ímpares)
- senão:
    - par requer ser o último número da permutação
"""








