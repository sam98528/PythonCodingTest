import sys
n = int(sys.stdin.readline().rstrip())

ls = list(map(int, sys.stdin.readline().rstrip().split()))

print(f'{min(ls)} {max(ls)}')