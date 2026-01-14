angulo = float(input())

horas = int(angulo//30)
minutos = int((angulo%30)*2)

print(f'{horas}h{minutos}m')