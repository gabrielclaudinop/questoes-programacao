x_ponto_inf_esq_1ret, y_ponto_inf_esq_1ret = map(int, input().split())
x_ponto_sup_dir_1ret, y_ponto_sup_dir_1ret = map(int, input().split())
x_ponto_inf_esq_2ret, y_ponto_inf_esq_2ret = map(int, input().split())
x_ponto_sup_dir_2ret, y_ponto_sup_dir_2ret = map(int, input().split())

pontos_1retangulo = [
    (x_ponto_inf_esq_1ret, y_ponto_inf_esq_1ret),
    (x_ponto_sup_dir_1ret, y_ponto_sup_dir_1ret),
    (x_ponto_inf_esq_1ret, y_ponto_inf_esq_1ret),
    (x_ponto_sup_dir_1ret, y_ponto_inf_esq_1ret)
]

pontos_2retangulo = [
    (x_ponto_inf_esq_2ret, y_ponto_inf_esq_2ret),
    (x_ponto_sup_dir_2ret, y_ponto_sup_dir_2ret),
    (x_ponto_inf_esq_2ret, y_ponto_inf_esq_2ret),
    (x_ponto_sup_dir_2ret, y_ponto_inf_esq_2ret)
]

retangulos_colidem = False
for x, y in pontos_1retangulo:
    if x_ponto_inf_esq_2ret <= x and x <= x_ponto_sup_dir_2ret and y_ponto_inf_esq_2ret <= y and y <= y_ponto_sup_dir_2ret:
        retangulos_colidem = True
        break

for x, y in pontos_2retangulo:
    if x_ponto_inf_esq_1ret <= x and x <= x_ponto_sup_dir_1ret and y_ponto_inf_esq_1ret <= y and y <= y_ponto_sup_dir_1ret:
        retangulos_colidem = True
        break

print(str(retangulos_colidem).upper())