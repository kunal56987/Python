# list comparison using equality operator(==, !=)

# working procces
# 1.order of elements are  same
# 2.countent of list are same
# 3.number of element are same
# 4.case also same
l=['kunal','srivastava','harsh']
s=['Kunal','Srivastava','Harsh']
r=['kunal','srivastava','harsh']
# == operator
print(l==s) # here case is different so it retuens false
print(l==r)
print(r==s) 

# != operator
print(l!=s)
print(l!=r)

# list comaprison using relational operator

# working procces
# here only first element will campared

l=[10,20,30]
s=[11]
print(l>s) # 10>11 ----> False
print(l<s) # 11>10 ----> True

