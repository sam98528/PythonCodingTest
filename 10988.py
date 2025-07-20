import math

word = input()

def result():
  for i in range(math.floor((len(word)/2))):
    if word[i] == word[len(word)-1-i]:
      continue
    else:
      print(0)
      return
  print(1)

result()