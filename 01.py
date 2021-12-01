with open('01.in') as file:
    x = list(map(int, file.readlines()))

print(sum(b>a for a, b in zip(x, x[1:])))

