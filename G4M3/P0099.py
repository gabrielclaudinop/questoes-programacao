qntd_linhas = int(input())

caracteres_usados = set()
for i in range(qntd_linhas):
    linha = input().lower()
    caracteres_usados |= set(linha)

letras_nao_usadas = set('abcdefghijklmnopqrstuvwxyz') - caracteres_usados

print("".join(sorted(letras_nao_usadas)))