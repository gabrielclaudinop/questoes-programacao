qntd_linhas = int(input())

grafo = {}
for linha in range(1, qntd_linhas+1):
    grafo[str(linha)] = []

for i in range(qntd_linhas):
    x, ys = input().split(':')
    ys = set(ys.split())
    
    for y in ys:
        grafo[y].append(x)

pilha = ['1']
visitados = set()
alvo = str(qntd_linhas)
programa_termina = False

while pilha:
    no = pilha.pop()
    visitados.add(no)

    if no == alvo:
        programa_termina = True
    
    for adj in grafo[no]:
        if adj not in visitados:
            pilha.append(adj)

if programa_termina:
    print('VERY GOOD PROGRAM!')
else:
    print('TOO BAD...')