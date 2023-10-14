arr = []

for i in range(10):
    a = int(input())
    a %= 42
    arr.append(a)

ans = set(arr)
print(len(ans))