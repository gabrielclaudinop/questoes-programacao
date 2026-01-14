x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xj = []
yj = []

for x in (x1, x2, x3):
    xj.append(x) if x not in xj else xj.remove(x)

for y in (y1, y2, y3):
    yj.append(y) if y not in yj else yj.remove(y)

print(xj[0], yj[0])