from collections import defaultdict
floor = defaultdict(int)

def get_direction(start, end):
    delta = end - start
    delta /= abs(delta)
    return complex(round(delta.real), round(delta.imag))

with open('05.in') as file:
    for line in file:
        start, end = line.strip().split(' -> ')
        start_x, start_y = tuple(map(int, start.split(',')))
        start = complex(start_x, start_y)
        end_x, end_y = tuple(map(int, end.split(',')))
        end = complex(end_x, end_y)
        direction = get_direction(start, end)
        p = start
        while p != end:
            floor[p] += 1
            p += direction
        floor[end] += 1

print(sum(1 for v in floor.values() if v >= 2))
