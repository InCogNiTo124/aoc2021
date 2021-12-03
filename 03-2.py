with open('03.in') as file:
    x = file.readlines()

def get_1_counts_on_i(x, i):
    count = 0
    for t in x:
        b = t[i]
        if b == '1':
            count += 1
    return count

def get_oxy(x):
    for i in range(len(x[0])):
        count_1 = get_1_counts_on_i(x, i)
        if count_1 >= len(x) / 2:
            x = list(filter(lambda t: t[i] == '1', x))
        else:
            x = list(filter(lambda t: t[i] == '0', x))
        if len(x) == 1:
            break
    return int(x[0], 2)


def get_c02(x):
    for i in range(len(x[0])):
        count_0 = len(x) - get_1_counts_on_i(x, i)
        if count_0 <= len(x) / 2:
            x = list(filter(lambda t: t[i] == '0', x))
        else:
            x = list(filter(lambda t: t[i] == '1', x))
        if len(x) == 1:
            break
    return int(x[0], 2)

oxy = get_oxy(x.copy())
co2 = get_c02(x.copy())
print(oxy)
print(co2)
print(oxy*co2)
