import sys

read = lambda: sys.stdin.readline().rstrip()

resultMap = {}

for _ in range(10):
  num = int(read()) % 42
  if num in resultMap:
    resultMap[num] += 1
  else:
    resultMap[num] = 0

result = 0

for _ in resultMap:
  result += 1

print(result)