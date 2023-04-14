from collections import deque

while True:
    flag = True
    s = input()
    if s == '.':
        exit(0)
    stack = deque([])
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                flag = False
            elif stack[-1] == "(":
                stack.pop()
            else:
                flag = False
        elif i == "]":
            if len(stack) == 0:
                flag = False
            elif stack[-1] == "[":
                stack.pop()
            else:
                flag = False
    if len(stack) == 0 and flag == True:
        print("yes")
    else:
        print("no")
