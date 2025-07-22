
import sys

large = -1
x1 = 0 
y1 = 0

for i in range(9):
  line = sys.stdin.readline().strip().split()
  for j, x in enumerate(line):
    num = int(x)
    if num > large:
      large = num
      x1 = i+1
      y1 = j+1
print(large)
print(f'{x1} {y1}')