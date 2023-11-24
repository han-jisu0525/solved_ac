import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

sum_list = []

for i in range(len(arr)):
    cnt = 0
    for j in range(i+1):
        cnt += arr[j]
    sum_list.append(cnt)

print(sum(sum_list))