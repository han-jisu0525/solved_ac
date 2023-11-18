while True:
    cmd = input()  # sys쓰면 출력 초과..
    stack = []

    if cmd == ".":
        break
    
    for i in cmd:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[': 
                stack.pop()
            else:
                stack.append(i)
                break  # 짝 안맞음
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break # 짝 안맞음
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
                