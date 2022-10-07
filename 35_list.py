# creation of list
# 1. creation of empty list
l=[]
print(l)

# 2. creation of list dynamically using eval()
l=eval(input('enter a list:'))
print(l)

#3. creation of list using list() function
#Ex-1
l=list((23,33,43,53))
print(l)

#Ex-2 creation of list using range()
l=list(range(10,21))
print(l)

# 4.creation of list directly
l=[23,33,'kunal',True,6.5]
print(l)

#list can also hold dist,tuple etc.
l=[23,{'name':'kunal'},list((10,20,30))]
print(l)

# 5.creation of list using split() function
#Ex-1
msg='wlcome to the world of python'
l=msg.split()# it will split on the basis of space( )
print(l)

#Ex-2
msg='Wlcome-to-the-world-of-python'
l=msg.split("-")#it will split according to (-)
print(l)
