N = int(input())
ans = []  # push, pop 담을 배열
stack = []  # 숫자 담을 배열
count = 1
temp = True

for i in range(N):
    num = int(input())

    while count <= num:  # num 이하 숫자까지 스택에 넣기
        stack.append(count)
        ans.append('+')
        count += 1
    
    if stack[-1] == num:  # num이랑 스택 맨 위 숫자가 동일하다면 제거
        stack.pop()
        ans.append('-')
    
    else:  # 스택 수열을 만들 수 없으므로
        temp = False
        break

#  스택 수열을 만들 수 있는지 없는지
if temp == False:
    print('NO')
else:
    for i in ans:
        print(i)