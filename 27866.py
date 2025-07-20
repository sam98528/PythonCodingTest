import sys

read = lambda: sys.stdin.readline().rstrip()

word = read()
N = int(read())
print(word[N-1])