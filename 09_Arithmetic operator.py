a=30
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b) #result is in float form
print(a%b)
print(a**b)
print(a//b) #in the form of int

#difference between division and floor division
a=40
b=3
print(a/b)# it gives float value i.e we divide 40 by 3 so our ans is 13.33
print(a//b)# but in floor division we get only 13 as a result besause it gives intiger part as a result

a=50.0
b=5
print(a/b)
print(a//b)

#we can't add string and int value
# name='kunal'
# print(name+24) #we will get type error

#add str and str
name='kunal'
print(name+'25')

# we can't divide any no by 0
# a=100
# b=0
# print(a/b) #zero division error

# multiplecatio of str and int
name='kunal'
print(name*5)

# we can't multipli str and float value together
# name='kunal'
# print(name*4.4) #Error 

# we also not divide float number by 0
# a=100.0
# b=0
# print(a/b) #zero division error

#result using BOADMAS rule
a,b,c,d,e,f,g,h=1,2,3,4,5,2,6,7
result=(a+b)*(c+d)*e**f//g+h
print(result)