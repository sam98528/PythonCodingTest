import sys

temp = [['']] * 5
check = [False] * 5
for i in range(5):
  temp[i] = list(map(str,sys.stdin.readline().rstrip())) 

result = ""
index = 0

while (False in check):
  for i in range(5):
    if len(temp[i]) <= index:
      check[i] = True
    elif check[i] == True:
      continue
    else:
      result += temp[i][index]
  index +=1

print(result)