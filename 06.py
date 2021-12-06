fishes = [0 for _ in range(9)]
with open('06.in') as file:
    for seed in map(int, file.read().strip().split(',')):
        fishes[seed] += 1


DAYS = 80
for i in range(1, DAYS+1):
    zero = fishes.pop(0)
    fishes.append(zero)
    fishes[6] += zero

print(sum(fishes))
