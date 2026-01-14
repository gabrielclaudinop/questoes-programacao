a, b = map(int, input().split())

for i in range(2, a+b):
    if (a+b)%i == 0:
        print('Xi')
        break
else:
    print('Xau')