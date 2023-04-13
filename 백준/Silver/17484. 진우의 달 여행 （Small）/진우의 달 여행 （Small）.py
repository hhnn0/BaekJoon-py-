n, m = map(int, input().split())
board = []
dp = []
max = 100*6*6
for _ in range(n):
    board.append(list(map(int, input().split())))

for _ in range(n):
    dp.append([[0]*3 for _ in range(m)])

for j in range(m):
    for k in range(3):
        dp[0][j][k] = board[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (k == 0 and j == m-1) or (k == 2 and j == 0):
                dp[i][j][k] = max
                continue

            if k == 0:
                dp[i][j][k] = board[i][j] + \
                    min(dp[i-1][j+1][1], dp[i-1][j+1][2])

            elif k == 1:
                dp[i][j][k] = board[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
            else:
                dp[i][j][k] = board[i][j] + \
                    min(dp[i-1][j-1][0], dp[i-1][j-1][1])


ans = max
for j in range(m):
    ans = min(ans, min(dp[n-1][j]))


print(ans)
