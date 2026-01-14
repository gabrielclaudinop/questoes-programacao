qntd_kits = int(input())
qntd_times = int(input())

qntd_pessoas = qntd_times*3

if qntd_kits > qntd_pessoas:
    print('MANTER ABERTAS')
else:
    print('FECHAR IMEDIATAMENTE')