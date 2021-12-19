from collections import deque, Counter
rules = dict()
with open('14.in', 'r') as file:
    poly = file.readline().strip()
    file.readline()
    for line in file:
        start, end = line.strip().split(' -> ')
        rules[start] = end

chars = Counter(poly)
pairs = Counter(list(a+b for a, b in zip(poly, poly[1:])))
for _ in range(40):
    for (left, right), count in pairs.copy().items():
        sub = rules[left+right]
        pairs[left+right] -= count
        pairs[left+sub] += count
        pairs[sub+right] += count
        chars[sub] += count


print(max(chars.values()) - min(chars.values()))
