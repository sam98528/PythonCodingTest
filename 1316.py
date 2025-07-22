
n = int(input())
result = 0
for _ in range(n):
  word = input()
  temp = ""
  isRepeatWord = True
  occur = {}
  for i in word:
    if i in occur and temp == i:

      continue
    elif temp != i and not(i in occur):

      occur[i] = 1
      temp = i
    else:
      isRepeatWord = False

      break 
  if isRepeatWord:
    result+=1

print(result)