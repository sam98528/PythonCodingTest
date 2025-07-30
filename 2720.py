N = int(input())
cash = [25, 10, 5, 1 ]
for _ in range(N):
  result = list(0 for _ in range(4))
  money = int(input())
  for i in range(4):
    result[i] = money // cash[i]
    money = money % cash[i]
  print(" ".join(map(str,result))) 

