point_cloud = set()
instructions = []

with open('13.in', 'r') as file:
    for line in file:
        if ',' in line:
            x, y = line.strip().split(',')
            point_cloud.add((int(x), int(y)))
        elif 'x' in line:
            n = int(line.strip().split('=')[1])
            instructions.append(('x', n))
        elif 'y' in line:
            n = int(line.strip().split('=')[1])
            instructions.append(('y', n))

for fold in instructions:
    line = fold[1]
    if fold[0] == 'y':
        points_below = set(filter(lambda t: t[1] > line, point_cloud))
        for px, py in points_below:
            point_cloud.remove((px, py))
            point_cloud.add((px, 2*line-py))

    elif fold[0] == 'x':
        points_below = set(filter(lambda t: t[0] > line, point_cloud))
        for px, py in points_below:
            point_cloud.remove((px, py))
            point_cloud.add((2*line - px, py))

lines = []
for row in range(max(t[1] for t in point_cloud)+1):
    columns = set(t[0] for t in point_cloud if t[1] == row)
    lines.append(''.join("#" if x in columns else '.' for x in range(max(t[0] for t in point_cloud)+1)))

print('\n'.join(lines))
    

