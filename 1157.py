from collections import Counter

word = input().lower()

print(word)
res = Counter(word).most_common(2)
print(res)
print(res[0][1])
print(res[1][1])
if res[0][1] == res[1][1]:
  print("?")
else:
  print(res[0][0])



