octetos = list(map(int, input().split('.')))

if sum(octetos) % 8 == 0:
    print('BLOCK')
else:
    print('PASS')