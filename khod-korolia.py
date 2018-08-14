x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 and y1 == y2:
    print('NO')
elif abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
    print('YES')
else:
    print('NO')

# dx = ((x2 - x1) ** 2) ** (1 / 2)
# dy = ((y2 - y1) ** 2) ** (1 / 2)
# print(dx, dy)
# mx = int((dx + 5) / (dx + 2))
# my = int((dy + 5) / (dy + 2))
# print(mx, my)
# ox = mx % 2
# oy = my % 2
# print(ox, oy)
# o = ox + oy
# print(o)
# print('YES' * (1 - o) + 'NO' * o)
