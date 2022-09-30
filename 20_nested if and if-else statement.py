#Nested if
num=int(input('Enter the no:'))
if num!=0:
    if num>0:
        print(num,'is positive')
    if num<0:
        print(num,'is negative')
else:
    print(num,'is zero')

#Nested if-else statement
num=int(input('Enter a number:'))
if num!=0:
    if num>0:
        print('number is positive')
    else:
        print('number is negative')
else:
    print('number is zero')