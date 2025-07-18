import sys

input = sys.stdin.readline().rstrip().split()

answerList = [1,1,2,2,2,8]
inputList = list(map(int, input))

for i in range(6):
  inputList[i] = answerList[i] - inputList[i]

print(" ".join(map(str, inputList)))