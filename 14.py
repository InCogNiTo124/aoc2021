from collections import deque, Counter
rules = dict()
with open('14.in', 'r') as file:
    poly = deque(file.readline().strip())
    file.readline()
    for line in file:
        start, end = line.strip().split(' -> ')
        rules[start] = end

#print(poly)
for _ in range(10):
    substitutions = dict()
    for i in range(len(poly)-1):
        subs = poly[i]+poly[i+1]
        if subs in rules:
            substitutions[i+1] = rules[subs]
    for i in reversed(sorted(substitutions.keys())):
        poly.insert(i, substitutions[i])

    #print(poly)
most_common = Counter(poly).most_common()
print(most_common[0][1] - most_common[-1][1])
