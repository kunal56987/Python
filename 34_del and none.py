#del-- it delete the memory
#Ex-1
a=100
print(a)
# del a
# print(a) #delete a so we will get name error bcz it deletes the value of a

#Ex-2
x='kunal'
print(x)
# del x
# print(x)

#Ex-3
x='kunal'
print(x)
# del x[0]
# print(x) #can't delete

#Ex-4
l=[10,20,30,40,50]
print(l)
del l[2]
print(l) #we can delete from list

#none
#Ex-5
a="Kutti"
print(a)
a=None
print(a)
a="cat"
print(a)