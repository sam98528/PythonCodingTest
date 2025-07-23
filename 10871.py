import sys

temp = lambda: sys.stdin.readline().rstrip().split()
n , a = map(int, temp())

tempList = list(map(int, temp()))
result = list()
for i in tempList:
  if i < a:
    result.append(str(i))

print(" ".join(result))