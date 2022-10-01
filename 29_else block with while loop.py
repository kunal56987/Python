# else block is executed
i=1
while i<=10:
    print(i)
    i+=1
else:
    print('else block is executed sucessfully after sussfully completing the loop')
# else block is executed bcz loop if executed fully

#else block is not executed
i=1
while i<=10:
    if(i==7):
        break
    print(i)
    i+=1
else:
    print('else block is executed sussesfully')
#here the loop is not executed fully so else block is not executed