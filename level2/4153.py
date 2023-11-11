while True:
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    else:
        sum = arr[0]**2 + arr[1]**2
    
    if sum == arr[2]**2:
        print("right")
    else:
        print("wrong")