import sys

N, M = map(int, sys.stdin.readline().split())
dict = {}

for i in range(N):
    link, password = sys.stdin.readline().split()
    dict[link] = password

for i in range(M):
    cmd = sys.stdin.readline().strip()
    print(dict[cmd])