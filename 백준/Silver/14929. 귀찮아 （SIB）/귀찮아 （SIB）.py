import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prefix_sum = 0
res = 0
for i in range(len(arr)-1, 0, -1):
    prefix_sum += arr[i]
    res += prefix_sum * arr[i-1]

print(res)
