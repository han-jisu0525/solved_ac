a = int(input())
b = int(input())
c = int(input())
mul = a * b * c

arr = [0 for i in range(10)]

while mul > 0:
    ans = 0
    ans = mul % 10
    arr[ans] += 1
    mul //= 10

for i in range(10):
    print(arr[i])
