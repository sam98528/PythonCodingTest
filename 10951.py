import sys

func = lambda: sys.stdin.readline().rstrip()

while 1:
  try:
    a,b =  map(int, func().split())
    print(f"{a+b}")
  except:
    break