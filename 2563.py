
import sys

N = int(sys.stdin.readline().rstrip())

paper = [[0] * 100 for _ in range(100)]
# print(paper)
for _ in range(N):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  for i in range(10):
    xChange = x + i
    for j in range(10):
      yChange = y + j
      paper[xChange][yChange] = 1
count = sum(row.count(1) for row in paper)
print(count)