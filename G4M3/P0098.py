n = input()

parte_grande1 = int(n[:len(n)-2])
parte_grande2 = int(n[1:len(n)-1])
parte_grande3 = int(n[2:])

maior_parte = max(parte_grande1, parte_grande2, parte_grande3)

if maior_parte == parte_grande1:
    parte1 = maior_parte
    parte2 = int(n[-2])
    parte3 = int(n[-1])
elif maior_parte == parte_grande2:
    parte1 = int(n[0])
    parte2 = maior_parte
    parte3 = int(n[-1])
else:
    parte1 = int(n[0])
    parte2 = int(n[1])
    parte3 = maior_parte

print(parte1+parte2+parte3)