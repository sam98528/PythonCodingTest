# import sys
# getInput = lambda: int(sys.stdin.readline().rstrip())

# max = 0
# index = 0

# for i in range(9):

#   num = getInput()
#   if i == 0:
#     max = num
#   if max < num:
#     max = num
#     index = i

# print(max)
# print(i)

numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)