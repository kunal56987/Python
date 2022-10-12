# craetion of set in different ways:

# 1.Creation of empty set:
s={} # we can't create empty set like this it will treated as dist
print(type(s)) #<class 'dict'>

# we can create empty set by using set()
s=set()
print(type(s)) #<class 'set'>


# 2.Creartion of set with heterognous elements:

s={10,20,30,40,50,60,'kunal',True}
print(s) #{True, 40, 'kunal', 10, 50, 20, 60, 30}

# that means set does not mantain order


# 3.Creation of set using set()

# creation of set from list:
l=[10,20,30,40,50]
s=set(l)
print(s) #{40, 10, 50, 20, 30}

# creation of set from tuble
t=(10,20,30,40,50)
s=set(t) #{40, 10, 50, 20, 30}
print(s)

#creation of set from range()
s=set(range(10))
print(s) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# creation of set from string:
name='kunal srivastava'
s=set(name)
print(s) #{'i', 'n', 'a', 't', 'u', 'r', 'v', 'l', 's', ' ', 'k'}
print(type(s)) #<class 'set'>
# using split()
s=set(name.split())
print(s) #{'kunal', 'srivastava'}


# We cant preform indixing and slicing operator:
# l={10,20,55,44,65}
# print(l[2]) #TypeError: 'set' object is not subscriptable
# print(l[1:2:]) #TypeError: 'set' object is not subscriptable


# membership operator in or not in

s={23,33,'kunal','srivastava',43,56}
print('kunal' in s) #True
print('maatey' in s) #False
print('kunal' not in s) #False
print('maatey' not in s) #True