# import sys
# N, B = map(str,sys.stdin.readline().rstrip().split())

# notation = int(B)
# result = 0

# for i, x in enumerate(N):
#   if x.isdigit():
#     result += int(x) * pow(notation, (len(N)-1)-i)
#   elif x.isalpha():
#     converted = ord(x) - 55
#     result += int(converted) * pow(notation, (len(N)-1)-i)

# print(result)

n, b = input().split()
print(int(n, int(b)))