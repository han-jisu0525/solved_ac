N = int(input())
arr = list(map(int, input().split()))

M = int(input())
ans = list(map(int, input().split()))  

for i in ans:
    if i in arr:
        print(1)  
    else:
        print(0)