qntd_aprovados = 0
for i in range(100):
  n1, n2, n3, n4, n5 = map(int, input().split())
  media = (n1+n2+n3+n4+n5)/5
  if media >= 700:
    qntd_aprovados += 1
print(qntd_aprovados)