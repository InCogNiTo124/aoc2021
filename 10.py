with open('10.in') as file:
    inputs = list(map(str.strip, file))

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
closes = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_score = 0
for x in inputs:
    stack = []
    for c in x:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            value = stack.pop(-1)
            if c != closes[value]:
                error_score += points[c]

print(error_score)
