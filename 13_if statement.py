#take two input and find which number is gratter among two.
a=int(input('enter the first no:'))
b=int(input('enter the secound no:'))
if(a>b):
    print(a,"is gratter then",b)
if(b>a):
    print(b,"is gratter then",a)

#input a student marks and check the result wither the student is pass or fail if the passing marks is equals to 33

mark=int(input('Enter the marsk:'))
if(mark>=33):
    print('congratulations you are pass')
if(mark<33):
    print('sorry you are fail') 