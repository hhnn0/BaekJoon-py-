n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

minNum = m*n


def checkBoard(startR, startC):
    startW = 0
    startB = 0
    for i in range(startR, startR+8):
        for j in range(startC, startC+8):
            if i % 2 != 0:
                if j % 2 != 0:
                    if board[i][j] != 'W':
                        startW += 1
                    if board[i][j] != 'B':
                        startB += 1
                else:
                    if board[i][j] != 'B':
                        startW += 1
                    if board[i][j] != 'W':
                        startB += 1
            else:
                if j % 2 != 0:
                    if board[i][j] != 'B':
                        startW += 1
                    if board[i][j] != 'W':
                        startB += 1
                else:
                    if board[i][j] != 'W':
                        startW += 1
                    if board[i][j] != 'B':
                        startB += 1
    return min(startW, startB)


for i in range(n-7):
    for j in range(m-7):
        minNum = min(minNum, checkBoard(i, j))

print(minNum)
