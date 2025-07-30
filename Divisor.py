

# 전부 도는 방식
# 시간 복잡도 O(N)
def getMyDivisorSlow(n):
    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList



# N = A * B 를 이용한 방식 
# 약수를 구하면, 그 짝이 있다 (ex: 6 = 2 * 3) 
# 이제 중복값만 조심하면 된다 .
# 1 ~ N^(1/2) 까지만 검사
# 시간 복잡도 O(N^(1/2))
def getMyDivisorFast(n):
  divisorList = []
  for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
      divisorList.append(i)
      if ((i**2) != n)
        divisorList.append(n // i)
  divisorList.sort()
  return divisorList

