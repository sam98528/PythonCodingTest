import sys
x,y = [int((sys.stdin.readline())) for _ in range(2)]
result = 0

if x > 0:
  if y > 0:
    result = 1
  else:
    result = 4
else:
  if y > 0:
    result = 2
  else:
    result = 3

print(result)