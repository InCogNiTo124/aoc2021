with open('02.in') as file:
    x = list((t[0], int(t[1])) for t in map(str.split, file.readlines()))

h, d, aim = 0, 0, 0
for t in x:
    if t[0] == 'forward':
        h += t[1]
        d += aim*t[1]
    elif t[0] == 'down':
        aim += t[1]
    elif t[0] == 'up':
        aim -= t[1]

print(h*d)
