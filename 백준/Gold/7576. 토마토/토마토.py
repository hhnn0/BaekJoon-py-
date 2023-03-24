from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    global m, n, graph, queue

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(queue):
        now = queue.popleft()
        cnt = graph[now[0]][now[1]] + 1

        for i in range(4):
            nextY = now[0] + dy[i]
            nextX = now[1] + dx[i]

            if nextY < 0 or nextX < 0 or nextY >= n or nextX >= m:
                continue
            if graph[nextY][nextX] == -1:
                continue
            if graph[nextY][nextX] == 0 or graph[nextY][nextX] > cnt:
                graph[nextY][nextX] = cnt
                queue.append([nextY, nextX])


bfs()
ans = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)

        ans = max(ans, graph[i][j])

print(ans-1)
