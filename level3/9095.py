import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    ans = [0] * (N+1)

    for i in range(1, N+1):
        if i == 1:
            ans[i] = 1
        elif i == 2:
            ans[i] = 2
        elif i == 3:
            ans[i] = 4
        else:
            ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
    
    print(ans[N])
