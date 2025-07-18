import sys

read = lambda: sys.stdin.readline().rstrip()

N,M = map(int,read().split())

resultList = ["0" for _ in range(N)]

for _ in range(M):
  start,end,num = map(int,read().split())
  for i in range(start-1,end):
    resultList[i] = str(num)

print(" ".join(resultList))