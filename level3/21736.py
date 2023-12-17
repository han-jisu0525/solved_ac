from collections import deque

N, M = map(int, input().split())
campus = []
start = ()

for i in range(N):
    row = list(input().rstrip())
    # 시작 위치
    for j in range(M):  
        if row[j] == 'I':
            start = (i, j)
    campus.append(row)
    
# BFS
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[False]*M for _ in range(N)]

res = 0 # 만날 수 있는 사람 수

queue = deque([start])
visit[start[0]][start[1]] = True
while(queue):
    x, y = queue.popleft()
    
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        
        # 캠퍼스를 벗어나지 않으면서
        if 0<= nx<N and 0<= ny<M:
            # 벽이 아니고 방문하지 않은 곳이면 방문
            if campus[nx][ny] != 'X' and not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
                
                # 사람이면 +1
                if campus[nx][ny] == 'P':
                    res += 1
                    
print(res if res > 0 else 'TT')