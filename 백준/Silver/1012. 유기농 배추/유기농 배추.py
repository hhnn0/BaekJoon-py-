from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
ans = []


def bfs(startRow, startCol, graph):
    global visited
    global n
    global m

    queue = deque([[startRow, startCol]])
    dc = [0, 0, 1, -1]
    dr = [1, -1, 0, 0]
    while (len(queue)):
        now = queue.popleft()
        if (visited[now[0]][now[1]] == 1):
            continue
        visited[now[0]][now[1]] = 1
        for i in range(4):
            nextCol = now[1] + dc[i]
            nextRow = now[0] + dr[i]
            if nextCol < 0 or nextRow < 0 or nextCol >= n or nextRow >= m:
                continue
            if visited[nextRow][nextCol] == 0 and graph[nextRow][nextCol] == 1:
                queue.append([nextRow, nextCol])


for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        col, row = map(int, input().split())
        graph[row][col] = 1
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == 1:
                bfs(i, j, graph)
                cnt += 1
    print(cnt)
