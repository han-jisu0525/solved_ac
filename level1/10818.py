N = int(input())
arr = list(map(int, input().split()))

arr.sort()

print(arr[0], end=' ')
print(arr[len(arr)-1])