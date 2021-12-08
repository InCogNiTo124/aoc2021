import itertools as it

with open('08.in') as file:
    print(sum(1 for t in it.chain.from_iterable(line.strip().split(' | ')[1].split(' ') for line in file) if len(t) in [2, 3, 4, 7]))
