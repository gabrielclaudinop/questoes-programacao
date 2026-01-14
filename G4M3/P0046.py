qntd_const, max_estr_barriga = map(int, input().split())

d_nutricao = {}
for i in range(qntd_const):
    qntd_estr, valor_nutr = map(int, input().split())
    if valor_nutr in d_nutricao:
        d_nutricao[valor_nutr] += qntd_estr
    else:
        d_nutricao[valor_nutr] = qntd_estr

l_nutricao = [[valor_nutr, qntd_estr] for valor_nutr, qntd_estr in d_nutricao.items()]
l_nutricao_ordenada = sorted(l_nutricao, key=lambda lista: lista[0], reverse=True)

qntd_estr_barriga = 0
valor_nutr_barriga = 0
for valor_nutr, qntd_estr in l_nutricao_ordenada:
    if qntd_estr_barriga + qntd_estr > max_estr_barriga:
        valor_nutr_barriga += (max_estr_barriga - qntd_estr_barriga) * valor_nutr
        qntd_estr_barriga += max_estr_barriga - qntd_estr_barriga
    else:
        qntd_estr_barriga += qntd_estr
        valor_nutr_barriga += qntd_estr * valor_nutr
    
print(valor_nutr_barriga)