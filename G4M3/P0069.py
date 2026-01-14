n = int(input())

eh_tia = True
for i in range(2, n+2):
    if (n-1 != i and (n-1) % i == 0) or (n+1 != i and (n+1) % i == 0):
        eh_tia = False
        break

if eh_tia:
    print(n, 'TIA')
else:
    print(n, 'NAH')