with open('02.in') as file:
    x = list((t[0], int(t[1])) for t in map(str.split, file.readlines()))

h, d = 0, 0
for t in x:
    if t[0] == 'forward':
        h += t[1]
    elif t[0] == 'down':
        d += t[1]
    elif t[0] == 'up':
        d -= t[1]

print(h*d)
