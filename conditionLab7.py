import random

num=int(input("숫자 입력"))

if 1<=num<=10:
	if num%2==0:
	    print(str(num), ": 짝수")
	if num%2==1:
	    print(str(num), ": 홀수")
else:
    	print("1부터 10사이의 값이 아닙니다.")