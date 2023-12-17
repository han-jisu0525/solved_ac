from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and arr[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visit[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visit:
    print(*i)