import sys

price = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total = 0

for _ in range(n):
  itemPrice, itemCount = map(int, sys.stdin.readline().split())
  total = total + itemPrice * itemCount

print("Yes" if total == price else "No")