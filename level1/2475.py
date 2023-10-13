a, b, c, d, e = map(int, input().split())

arr = [a, b, c, d, e]
sum = 0

for i in range(len(arr)):
    sum += arr[i]*arr[i]

print(sum % 10)