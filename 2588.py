import sys

a,b = [(sys.stdin.readline()) for _ in range(2)]
b1,b2,b3 = int(b[2]),int(b[1]),int(b[0])
a = int(a)
b = int(b)
print(a * b1)
print(a * b2)
print(a * b3)
print(a*b)
