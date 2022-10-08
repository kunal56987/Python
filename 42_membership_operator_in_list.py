# in
l=[10, 20, 30, 40, 50]
print(20 in l)
print(999 in l)

# not in
l=[10, 20, 30, 40, 50]
print(20 not in l)
print(99 not in l)


#wap to check weather your lucky number is present inside list or not

a=int(input('Enter youe lucky no:'))
l=[13,17,36,23,27,14,98]
if a in l:
    print('Your lucky no is present')
else:
    print('Sorry your lucky is not present')


# wap to check your luck number until match your lucky number with list element

l=[13,17,36,23,27,14,98]
luckyno=int(input('Enter your lucky No:'))
while True:
    if luckyno in l:
        print('Your lucky no is present')
        break
    else:
        print('Sorry your lucky no is not present enter lucky number again')
        luckyno=int(input('Enter your lucky No:'))
