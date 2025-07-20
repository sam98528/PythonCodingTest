N = int(input())

star = 1
space = N-1
for i in range(1, N+1):
  print(" "*space + (2*i-1)*"*")
  space-=1

space = 1
for i in range(N-1, 0, -1):
  print(" "*space + (2*i-1)*"*")
  space+=1
