#wap to input 3 number and check which one is greatest among 3 using if-elif-else statement
a=int(input('Enter the first number:'))

b=int(input('Enter the secound number:'))
c=int(input('Enter the third no:'))
if(a>b and a>c):
    print(a,'is greater')
elif(b>a and b>c):
    print(b,'is greater')
else:
    print(c,'is greater')

#wap to input 2 number and perform calculation based on user input like add sub mul div
a=int(input('Enter first number:'))
b=int(input('Enter the secound number:'))
choise=input('enter a choise you want to perform\naddition\nsubstraction\nmultiplication\ndivision:')
if choise=='addition':
    print(a,'+',b,'=',a+b)
elif choise=='substraction':
    print(a,'-',b,'=',a-b)
elif choise=='multiplication':
    print(a,'*',b,'=',a*b)
elif choise=='division':
    print(a,'/',b,'=',a/b)
else:
    print('invalid choise pls chose from the given operation')