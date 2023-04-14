import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = []
value = []
for _ in range(N):
    n, v = map(str, input().split())
    name.append(n)
    value.append(int(v))

for _ in range(M):
    num = int(input())
    start = 0
    res = 0
    end = len(value)-1
    while start <= end:
        mid = (start+end)//2
        if num <= value[mid]:
            end = mid-1
            res = mid
        else:
            start = mid + 1
    print(name[res])
