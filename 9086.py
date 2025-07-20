import sys

read = lambda: sys.stdin.readline().rstrip()
N = int(read())

for _ in range(N):
  word = read()
  print(word[0]+word[len(word)-1])