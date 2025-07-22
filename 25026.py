import sys 

grade = {}
scores = {'A+': 4.5,'A0': 4.0,"B+": 3.5,"B0": 3.0,"C+": 2.5,"C0": 2.0,"D+": 1.5,"D0": 1.0,"F": 0.0}
sum = 0
scoreTotal = 0
for _ in range(20):
  _ , num, score = map(str, sys.stdin.readline().rstrip().split())
  if score != 'P':
    sum += float(num) * scores[score]
    scoreTotal += float(num)
  

if sum == 0:
  print(0.0)
else:
  print(sum / scoreTotal)