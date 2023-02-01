for i in range(5):
    print(i)
else:
    print('i am else block')
# it is same as the while with else block i.e when the for loop is executed fully successfully than the else block
# will be executed

for i in range(5):
    if i==4:
        break
    print(i)
else:
    print('i am else block')
# here else block can not be executed bcz for loop is not executed fully it will break at i=4