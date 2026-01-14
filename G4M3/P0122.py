qntd_times, qntd_problemas = map(int, input().split())
baloes_times = list(map(int, input().split()))

total_baloes_existentes = qntd_times * qntd_problemas
total_baloes_usados = sum(baloes_times)

print(total_baloes_existentes - total_baloes_usados)