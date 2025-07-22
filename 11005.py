N, B = map(int, input().split())

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while N != 0:
  ans += number[N%B]
  N = N // B

print(ans[::-1])
