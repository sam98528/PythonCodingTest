input = int(input())

print("1" if input%4 == 0 and input%100 != 0 else "1" if input%400 == 0 else "0")