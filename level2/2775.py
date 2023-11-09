T = int(input())

for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호수
    k0 = [x for x in range(1, n+1)]  # 0층

    for i in range(k):  # 층 수 만큼 반복
        for j in range(1, n):
            k0[j] += k0[j-1]

    print(k0[-1])