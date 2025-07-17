import sys

input = lambda: sys.stdin.readline().rstrip()

while 1:
  a,b = map(int,input().split())
  result = a + b
  if result == 0:
    break
  else:
    print(result)