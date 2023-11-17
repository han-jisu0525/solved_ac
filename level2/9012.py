import sys

N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline()
    stack = []
    for j in command:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")