from collections import defaultdict, Counter

NEIGHBOURS = defaultdict(list)

with open('12.in') as file:
    for line in file:
        first, second = line.strip().split('-')
        NEIGHBOURS[first].append(second)
        NEIGHBOURS[second].append(first)

def allowed(path):
    c = Counter(t for t in path if t.islower())
    if max(c.values()) > 2:
        return False
    return list(c.values()).count(2) <= 1

def paths(path):
    node = path[-1]
    if node == 'end':
        yield path
        return
    for n in NEIGHBOURS[node]:
        if n != 'start' and (n.isupper() or allowed(path+[n])):
            yield from paths(path+[n])

print(sum(1 for _ in paths(['start'])))
