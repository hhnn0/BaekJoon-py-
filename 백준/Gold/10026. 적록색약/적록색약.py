import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    board.append(list(input().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

rgb = 0
gb = 0


def dfs(x, y):
    visited[x][y] = 1
    now = board[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0 and board[nx][ny] == now:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            rgb += 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            gb += 1

print(rgb, gb)
