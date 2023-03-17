from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
ans = []


def dfs(now, graph):
    global visited
    global ans
    ans.append(now)

    visited[now] = 1

    graph[now].sort()
    for g in graph[now]:
        if (visited[g] == 0):
            dfs(g, graph)


def bfs(start, graph):
    queue = deque([start])
    visited = [0] * (n+1)
    ans = []

    while (len(queue)):
        tmp = queue.popleft()
        if visited[tmp] == 1:
            continue
        visited[tmp] = 1
        ans.append(tmp)
        graph[tmp].sort()
        for g in graph[tmp]:
            queue.append(g)

    return ans


dfs(v, graph)
print(*ans)
print(*bfs(v, graph))
