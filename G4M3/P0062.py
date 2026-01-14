qntd_linhas = int(input())

bug = False
for i in range(qntd_linhas):
    linha = input()
    if 'B' in linha:
        bug = True
        break

if bug:
    print('YES')
else:
    print('NO')