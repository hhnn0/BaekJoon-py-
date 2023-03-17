from collections import deque
import sys
input = sys.stdin.readline

c = int(input())
l = int(input())
graph = [[] for _ in range(c+1)]
visited = [0] * (c+1)

for _ in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
queue = deque([1])

while (len(queue)):
    tmp = queue.popleft()
    if (visited[tmp] == 1):
        continue
    visited[tmp] = 1
    cnt += 1
    for g in graph[tmp]:
        queue.append(g)
print(cnt-1)
