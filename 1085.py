x,y,w,h = map(int, input().split())

ans = x

if y < x:
  ans = y
if w - x < ans:
  ans = w -x 
if h - y < ans:
  ans  = h - y

print(ans)