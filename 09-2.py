from collections import defaultdict, deque
import itertools as it
import math

def flood_fill(index):
    visited = set()
    queue = deque([index])
    while len(queue) > 0:
        element = queue.popleft()
        visited |= {element}
        queue.extend([element+d for d in [1, 1j, -1, -1j] if CAVE[element+d] < 9 and (element + d not in visited)])
    return len(visited)


CAVE = defaultdict(lambda: float('inf'))
with open('09.in') as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            CAVE[complex(j, i)] = int(char)

basin_sizes = []
for y, x in it.product(range(i+1), range(j+1)):
    index = complex(x, y)
    value = CAVE[index]
    if all((value < CAVE[index+d]) for d in [1, 1j, -1, -1j]):
        # it's a bottom of a basin
        # flood fill algorithm go brr
        basin_sizes.append(flood_fill(index))


print(math.prod(sorted(basin_sizes)[-3:]))
