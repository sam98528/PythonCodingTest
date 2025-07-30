tempList = []

for _ in range(3):
  a = int(input())
  tempList.append(a)

if sum(tempList) != 180:
  print("Error")
elif len(set(tempList)) == 1:
  print("Equilateral")
elif len(set(tempList)) == 2:
  print("Isosceles")
else:
  print("Scalene")
