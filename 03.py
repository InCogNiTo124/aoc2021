with open('03.in') as file:
    x = file.readlines()

counts = [0]*12

for t in x:
    for i, b in enumerate(t):
        if b == '1':
            counts[i] += 1

gamma = int(''.join(str(int(t > len(x)//2)) for t in counts), 2)
epsilon = int(''.join(str(int(t < len(x)//2)) for t in counts), 2)
print(gamma)
print(epsilon)
print(gamma*epsilon)
