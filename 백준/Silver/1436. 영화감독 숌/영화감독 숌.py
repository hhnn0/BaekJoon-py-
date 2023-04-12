n = int(input())

cnt = 0
i = 665
while i < 10000000:
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        exit(0)
    i += 1
