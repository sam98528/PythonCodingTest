import sys

result = [i+1 for i in range(30)]

read = lambda: sys.stdin.readline().rstrip()
tempList = list()
for i in range(28):
  result.remove(int(read()))

for ans in result:
  print(ans)


