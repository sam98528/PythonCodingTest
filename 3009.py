
xdict = {}
ydict = {}

for _ in range(3):
  x , y = map(int, input().split())
  if x not in xdict:
    xdict[x] = 0
  if y not in ydict:
    ydict[y] = 0
  xdict[x] += 1
  ydict[y] += 1

for k in xdict:
    if xdict[k] == 1:
        x = k
for k in ydict:
    if ydict[k] == 1:
        y = k
print(x, y)