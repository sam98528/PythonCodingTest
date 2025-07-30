
while True:
  tempList = list(map(int, input().split()))
  if sum(tempList) == 0:
    break
  tempList.sort()
  tempList.reverse()

  if tempList[0] >= tempList[1] + tempList[2]:
    print("Invalid")
  elif len(set(tempList)) == 1:
    print("Equilateral")
  elif len(set(tempList)) == 2:
    print("Isosceles")
  else:
    print("Scalene")