from string import ascii_lowercase

#arr = [-1 for i in range(26)]
alphabet = list(ascii_lowercase)
S = list(input())

for i in alphabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')

