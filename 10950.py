import sys

func = lambda: sys.stdin.readline().rstrip()
n  = int(func())

for i in range(n):
  a,b =  map(int, func().split())
  print(a+b)