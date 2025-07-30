
temp = list(map(int,input().split()))
temp.sort()
temp.reverse()

if temp[0] >= temp[1]+temp[2]:
  temp[0] = temp[1]+temp[2] -1 

print(sum(temp))