M, N = map(int, input().split())

for i in range(M, N+1):
    ans = []
    for j in range(1, i+1):
        if i%j == 0:
            ans.append(j)
    
    if len(ans) == 2:
        print(i)