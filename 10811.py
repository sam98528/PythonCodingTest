import sys

read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())

result = list((i+1 for i in range(N)))

for _ in range(M):
  start, end = map(int,read().split())
  tempList = list(reversed(result[start-1:end]))
  temp = 0
  for i in range(start-1, end):
    result[i] = tempList[temp]
    temp+=1

print(" ".join(map(str, result)))