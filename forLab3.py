import random
y=random.randint(0,10)
x=random.randint(30,40)

sum=0
for i in range(y,x+1):
    if i%2==0:
        sum+=i

print("%d부터 %d까지의 짝수의 합 : %d" %(y,x,sum))