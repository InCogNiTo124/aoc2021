import statistics

with open('07.in') as file:
    x = list(map(float, file.read().strip().split(',')))

m = statistics.median(x)
print(sum(abs(t - m) for t in x))
