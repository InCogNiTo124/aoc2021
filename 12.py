from collections import defaultdict
NEIGHBOURS = defaultdict(list)

with open('12.in') as file:
    for line in file:
        first, second = line.strip().split('-')
        NEIGHBOURS[first].append(second)
        NEIGHBOURS[second].append(first)

def paths(path):
    node = path[-1]
    if node == 'end':
        yield path
        return
    for n in NEIGHBOURS[node]:
        if n != 'start' and (n.isupper() or n.islower() and n not in path):
            yield from paths(path+[n])

print(sum(1 for _ in paths(['start'])))
