import sys
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = sys.stdin.readline().rstrip()

for i in croatia:
  input = input.replace(i, '*')

print(len(input))