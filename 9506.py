

def findDivisor(n):
  divisionList = []

  for i in range(1,int(n**(1/2)+1)):
    if n % i == 0 :
      divisionList.append(i)
      if(int(i**(2)) != n and n // i != n):
        divisionList.append(n // i)
  divisionList.sort()
  return divisionList

while True:
  a = int(input())
  if a == -1:
    break
  tempList = findDivisor(a)
  if sum(tempList) == a:
    ans = f'{a} = '
    ans += ' + '.join(str(item) for item in tempList)
    print(ans)
  else:
    print(f'{a} is NOT perfect.')
