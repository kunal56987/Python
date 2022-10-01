# wap to read tha number untill -1 is entered and calculate no of -ve,+ve and zeros entered
a=int(input('Enter a number:'))
negative=0
positive=0
zeros=0
while a!=-1:
    if a>0:
        positive+=1
    elif a<0:
        negative+=1
    else:
        zeros+=1
    a=int(input('Enter a number:'))
print('number of postive no. entered:',positive)
print('number of negative no. entered:',negative)
print('number of zeros entered:',zeros)