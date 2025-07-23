import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

print(ls.count(int(sys.stdin.readline())))