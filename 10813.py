import sys

read = lambda: sys.stdin.readline().rstrip()

N,M = map(int,read().split())

resultList = [str(i+1) for i in range(N)]

for _ in range(M):
  i,j = map(int,read().split())
  temp = resultList[i-1]
  resultList[i-1] = resultList[j-1]
  resultList[j-1] = temp

print(" ".join(resultList))