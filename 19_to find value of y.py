# wap to input the value of n and find tha value of y(n)
#         1+x ,when n=1
#         1+x/n ,when n=2
# y(x,n)= 1+x**n ,when n=3
#         1+xn ,when n>3 or n<1
import math
x=int(input('Enter the value of x:'))
n=int(input('Enter the value of n:'))
if n==1:
    y=1+x
elif n==2:
    y=1+x/n
elif n==3:
    y=math.pow(x,n)
else:
    y=1+(x*n)
print('Output:',y)