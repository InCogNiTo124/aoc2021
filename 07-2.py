import statistics

with open('07.in') as file:
    x = list(map(int, file.read().strip().split(',')))

print(min(x), max(x))

E = lambda n: n*(n+1)//2

print(min(sum(E(abs(t-i)) for t in x) for i in range(min(x), max(x)+1)))
