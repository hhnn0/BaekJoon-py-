from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, startY, startX):
    global visited
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([[startY, startX]])
    while (len(queue)):
        now = queue.popleft()
        if visited[now[0]][now[1]] == 1:
            continue
        visited[now[0]][now[1]] = 1
        cnt += 1
        for i in range(4):
            nextX = now[1] + dx[i]
            nextY = now[0] + dy[i]
            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= n:
                continue
            if graph[nextY][nextX] == 1:
                queue.append([nextY, nextX])
    return cnt


n = int(input())
ans = []
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            ans.append(bfs(graph, i, j))

print(len(ans))
ans.sort()
for a in ans:
    print(a)
