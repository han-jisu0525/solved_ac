def my_round(val):
    return int(val) + 1 if val-int(val) >= 0.5 else int(val)

import sys
 
input = sys.stdin.readline
n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    n2 = my_round(n * 0.15)
    print(my_round(sum(arr[n2:-n2] if n2 else arr) / (n - 2*n2)))
else:
    print(0)