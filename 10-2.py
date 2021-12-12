with open('10.in') as file:
    inputs = list(map(str.strip, file))

points = {'(': 1, '[': 2, '{': 3, '<': 4}
closes = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = []
for x in inputs:
    incomplete = True
    stack = []
    for c in x:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            value = stack.pop(-1)
            if c != closes[value]:
                # discard corrupted
                incomplete = False
                break
    if incomplete:
        score = 0
        for c in reversed(stack):
            score = 5*score + points[c]
        scores.append(score)
print(sorted(scores)[len(scores)//2])
