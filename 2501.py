
import sys

a , b = map(int, sys.stdin.readline().split())

currentIndex = 0
currentVal = 0
for i in range(1,a+1):
  if a % i == 0:
    currentIndex += 1
    currentVal = i
  if currentIndex == b :
    print(i)
    break

if currentIndex < b:
  print("0")

