#EX-1
a=10
b=4
print(a>b)
print(a<b)

#EX-2
a=20
b=20
print(a>=b)

#EX-3
a=15
b=15
print(a<=b)

#EX-4
#we can also apply relational operator for string datatype
a='aaa'
b='bbb'
print(a>b) #aaa>bbb
print(a<b) #aaa<bbb

#EX-5
name='kunal'
name1='kunal'
print(name>name1) #both are equal so we get false as result
print(name<name1) #again we get false ,both are equal
print(name<=name1) #true
print(name>=name1) #true

#EX-6
print(10<20<30<40) #true
print(10<20<50<40) #false
#print(100<'kunal') #error
print(True>True) #false (1>1)
print(False>True) #false (0>1)
print(True>False) #true(1>0)
print(False>False) #false(0>0)

#Ex-7
#Equality operator (== ,!=)
print(10==10) #true
print(100==10) #false 
print(100!=10) #true
print(10==10==10==10==10) #true
print(10==10==10==11==10) #false

#we can also apply  equality operator with string datatype
print('kunal'=='kunal') #true
print(20=='kunal') #false
print('Apple'=='apple')#false