import sys
import itertools as it


with open('04.in') as file:
    numbers = list(map(int, file.readline().strip().split(',')))
    file.readline()
    boards = []
    line = None
    while line != '':
        board = [list(map(lambda i: {'value': int(i), 'marked': False}, file.readline().strip().split())) for _ in range(5)]
        boards.append(board)
        line = file.readline()

print(numbers)
print(boards[0])

def is_winning(board):
    for i in range(len(board)):
        if all(t['marked'] for t in board[i]):
            return True
        if all(row[i]['marked'] for row in board):
            return True
    return False

for number in numbers:
    for board in boards:
        for i, j in it.product(range(5), range(5)):
            if board[i][j]['value'] == number:
                board[i][j]['marked'] = True
        if is_winning(board):
            s = sum(t['value'] for t in it.chain.from_iterable(board) if not t['marked'])
            print(s*number)
            sys.exit(0)
