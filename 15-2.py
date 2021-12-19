from collections import defaultdict
import itertools as it
from heapq import heappush, heappop

def neighbour4(i, j, limits=None):
    if limits is None:
        min_i, min_j, max_i, max_j = -float('inf'), -float('inf'), float('inf'), float('inf')
    else:
        min_i, min_j, max_i, max_j = limits

    for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if min_i <= i+y < max_i and min_j <= j+x < max_j and (y, x) != (0, 0):
            yield (i+y, j+x)
    return


CAVERN = defaultdict(lambda: float('inf'))
with open('15.in') as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            for extra_i, extra_j in it.product(range(5), range(5)):
                CAVERN[j+100*extra_j, i+100*extra_i] = (extra_i + extra_j + int(char)-1)%9+1

grid_size = (5*(i+1), 5*(j+1))
#for i in range(grid_size[0]):
#    for j in range(grid_size[1]):
#        print(CAVERN[j, i], end='')
#    print()
#print(grid_size)

# A*    cost i  j before
queue = [(0, 0, 0, None)]
visited = set()
while len(queue) > 0:
    top_cost, top_i, top_j, _ = heappop(queue)
    if (top_i, top_j) == (grid_size[0]-1, grid_size[1]-1):
        print(top_cost)
        break
    elif (top_i, top_j) not in visited:
        visited.add((top_i, top_j))
        for n_i, n_j in neighbour4(top_i, top_j, (0, 0, *grid_size)):
            heappush(queue, (top_cost + CAVERN[n_i, n_j], n_i, n_j, (top_i, top_j)))
