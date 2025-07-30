
def findPrimeList(M,N):
  primeList = []
  for i in range(M, N+1):
    if isPrime(i):
       primeList.append(i)

  if len(primeList) == 0:
    print(-1)
  else:
    print(sum(primeList))
    print(primeList[0])


def isPrime(N):
  if N == 1:
    return False
  primeList = []
  for i in range(2, int(N**(1/2)+1)):
    if N % i == 0:
      primeList.append(i)
      if i**2 != N :
        primeList.append(N // i)
  
  if len(primeList) == 0:
    return True
  else: 
    return False


M = int(input())
N = int(input())

findPrimeList(M,N)

