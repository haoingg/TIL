evenNum,oddNum = 0,0

for x in range(0,101,2):
    if x%2==0:
        evenNum += x
    else:
        oddNum += x

print("1부터 100까지의 숫자들 중에서")
print("짝수의 합은", evenNum, "이고")
print("홀수의 합은", oddNum, "이다.")