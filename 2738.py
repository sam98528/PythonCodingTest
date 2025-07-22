
import sys

N,M = map(int, sys.stdin.readline().rstrip().split())

first = [[0] * M] * N
second = [[0] * M] * N

for i in range(N):
    first[i] = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(N):
    second[i] = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(N):
  for j in range(M):
    print(first[i][j] + second[i][j], end=" ")
  print()