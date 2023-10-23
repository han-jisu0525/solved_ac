import sys

k, n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)  # 이분 탐색

while start <= end:
    mid = (start+end) // 2
    lines = 0  # 새로운 랜선 수

    for i in lan:
        lines += i//mid  # 분할 된 랜선 수
    
    if lines >= n:  # 랜선 개수가 분기점
        start = mid + 1 
    else:
        end = mid - 1

print(end)