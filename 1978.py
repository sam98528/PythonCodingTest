
def findDivisor(n):
  if n == 1:
    return True
  divisionList = []
  for i in range(2,int(n**(1/2)+1)):
    if n % i == 0 :
      divisionList.append(i)
      if(int(i**(2)) != n and n // i != n):
        divisionList.append(n // i)
  if len(divisionList) == 0:
    return False
  else:
    return True


N = int(input())

inputList = list(map(int, input().split()))
ans = 0

for i in inputList:
  ans += 1 if not(findDivisor(i)) else 0

print(ans)