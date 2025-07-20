import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())

tempList = list(map(int, read().split()))
maxVal = max(tempList)
total = 0
for i in range(len(tempList)):
  tempList[i] = tempList[i] / maxVal * 100
  total += tempList[i]

print(total/N)