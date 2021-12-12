import itertools as it
from collections import deque

GRID = dict()

def neighbour8(i, j, limits=None):
    if limits is None:
        min_i, min_j, max_i, max_j = -float('inf'), -float('inf'), float('inf'), float('inf')
    else:
        min_i, min_j, max_i, max_j = limits

    for y, x in it.product(range(-1, 2), range(-1, 2)):
        if min_i <= i+y < max_i and min_j <= j+x < max_j and (y, x) != (0, 0):
            yield (i+y, j+x)

with open('11.in') as file:
    for i, row in enumerate(file):
        for j, c in enumerate(row.strip()):
            GRID[i, j] = int(c)

grid_size = (i+1, j+1)
flash_count = 0
N = 100
total_flash = 0
for step in range(N):
    for key in GRID:
        GRID[key] += 1

    to_flash = deque(key for key, value in GRID.items() if value > 9)
    visited = set()
    while len(to_flash) > 0:
        key = to_flash.popleft()
        if key not in visited:
            visited.add(key)
            for n in neighbour8(*key, (0, 0, *grid_size)):
                GRID[n] += 1
                if GRID[n] > 9:
                    to_flash.append(n)
    total_flash += len(visited)
    for key in visited:
        GRID[key] = 0

print(total_flash)
