# N = int(input())
# arr = [i for i in range(1, N+1)]

# for i in range(N-1):
#     arr.pop(0)
#     tmp = arr[0]
#     print(tmp)
#     for j in range(1, N-i-1):
#         arr[j-1] = arr[j]
#     arr.append(tmp)

# print(arr[0])

from collections import deque

N = int(input())
arr = deque()
for i in range(1, N+1):
    arr.append(i)

while len(arr) > 1:
    del arr[0]
    x = arr.popleft()  # deque의 맨 앞의 값을 빼서 x로 지정.
    arr.append(x)

    if len(arr) == 1:
        break

print(arr[0])