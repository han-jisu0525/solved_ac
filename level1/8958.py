n = int(input())

for i in range(n):
    ox = input()
    score = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1

            score += cnt
        else:
            cnt = 0
    print(score)


