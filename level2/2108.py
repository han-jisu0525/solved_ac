import math
import sys
from collections import Counter

N = int(sys.stdin.readline())
ans = []

for i in range(N):
    num = int(sys.stdin.readline())
    ans.append(num)

length = len(ans)

result = sum(ans) / length
print(round(result))  # 산술평균

ans.sort()
print(ans[length//2])  # 중앙값

cnt_ans = Counter(ans).most_common()  # 최빈값
if len(cnt_ans) > 1 and cnt_ans[0][1] == cnt_ans[1][1]: #최빈값 2개 이상
    print(cnt_ans[1][0])
else:
    print(cnt_ans[0][0])

print(ans[length-1] - ans[0])  # 범위


