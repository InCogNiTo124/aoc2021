from collections import defaultdict
import itertools as it

CAVE = defaultdict(lambda: float('inf'))
with open('09.in') as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            CAVE[complex(j, i)] = int(char)
risk_sum = 0
for y, x in it.product(range(i+1), range(j+1)):
    index = complex(x, y)
    value = CAVE[index]
    if all((value < CAVE[index+d]) for d in [1, 1j, -1, -1j]):
        risk_sum += value + 1

print(risk_sum)
