with open('01.in') as file:
    x = list(map(int, file.readlines()))

print(sum(d>a for a, d in zip(x, x[3:])))
