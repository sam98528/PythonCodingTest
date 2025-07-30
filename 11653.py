
a = int(input())
i = 2

if a != 1:
  while a != 1:
    if a % i == 0:
      print(i)
      a = a / i 
    else:
      i+=1


