DIGITS = [
    {'a','b', 'c', 'e', 'f', 'g'},
    {'c', 'f'},
    {'a', 'c', 'd', 'e', 'g'},
    {'a', 'c', 'd', 'f', 'g'},
    {'b', 'c', 'd', 'f'},
    {'a', 'b', 'd', 'f', 'g'},
    {'a', 'b', 'd', 'e', 'f', 'g'},
    {'a', 'c', 'f'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c', 'd', 'f', 'g'},
]

def n_intersect(n, word_list):
    assert len(word_list) == 10
    assert 2 <= n <= 7
    words = set.intersection(*[set(w) for w in word_list if len(w) == n])
    digits = set.intersection(*[s for s in DIGITS if len(s) == n])
    return words, digits


def get_mapping(signal):
    mapping = {
        'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    }
    for n in range(2, 7):
        word, possibilities = n_intersect(n, signal)
        for char in mapping:
            if char in word:
                mapping[char] &= possibilities
            else:
                mapping[char] -= possibilities
        if sum(map(len, mapping.values())) == 7:
            break
    return {k: v.pop() for k, v in mapping.items()}



with open('08.in') as file:
    lines = file.readlines()
    s = 0
    for line in lines:
        signal, output = line.strip().split(' | ')
        signal = signal.split(' ')
        output = output.split(' ')
        real_mapping = get_mapping(signal)
        s += int("".join(str(DIGITS.index(set(real_mapping[c] for c in word))) for word in output))
    print(s)

