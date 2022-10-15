# creation of dictionary:
d={
    'name':'kunal',
    'regno':2001297136,
    'Branch':'CSE',
    'clg name':'Nalanda institute of technalogy',
    'mob':7301216339
}

print(d['mob'])# 7301216339 
# here mob is my key and my number is my value

print(d) #{'name': 'kunal', 'regno': 2001297136, 'Branch': 'CSE', 'clg name': 'Nalanda institute of technalogy', 'mob': 7301216339}


# Different ways to creating dictionary:

# 1. Empty dictionary:

d={}
print(d) #{}
print(type(d)) #<class 'dict'>


# 2.creation of empty dictionary using dist():

d=dict()
print(d)# {}
print(type(d)) #<class 'dict'>


#3. create empty dictionary and add items on it:

d={}
print(d) #{}
d[17]='kunal'
d[27]='priya'
d[37]='Harsh'
print(d) #{17: 'kunal', 27: 'priya', 37: 'Harsh'}



# 4.creating dict directly:

d={17:'kunal',27:'priya',37:'Harsh'}
print(d) #{17: 'kunal', 27: 'priya', 37: 'Harsh'}



# 4.creating dictionary dynamically:

# d={}
# while True:
#     i=input('Enter the key:')
#     d[i]=input('Enter the {}:'.format(i))
#     choise=input('Do you want to add more [Y/N]:').upper()
#     if choise=='N':
#         break
# print(d)


# we can access the data elements by using key directly:

d={17: 'kunal', 27: 'priya', 37: 'Harsh',47:'sinu'}
print(d[27]) #priya
print(d[47]) #sinu
# print(d[5])  #KeyError



# We also check wether the key is exist or not

# 1. by unsing has_key() we can check wether the key is present or not but 
# this feature is not working in python 3 it is for python 2

# it can be check as

# d={17: 'kunal', 27: 'priya', 37: 'Harsh',47:'sinu'}
# print(d.has_key(27))#AttributeError: 'dict' object has no attribute 'has_key'


# we can solve this by using in operator:

d={17: 'kunal', 27: 'priya', 37: 'Harsh',47:'sinu'}
print(27 in d) #True



# Traversing a dict:

roll={1:'kunal',2:'Aditya',3:'priya',4:'sinu'}

# it will print only the key values i.e 1 2 3 4
for i in roll:
    print(i)

# To print key and value both 

for i in roll:
    print('{}:{}'.format(i,roll[i]))

# 1:kunal
# 2:Aditya
# 3:priya
# 4:sinu

# Addintion of items in a dict:

roll={1:'kunal',2:'Aditya',3:'priya',4:'sinu'}
print(roll) #{1:'kunal',2:'Aditya',3:'priya',4:'sinu'}
roll[5]='ishika'
print(roll) #{1:'kunal',2:'Aditya',3:'priya',4:'sinu',5: 'ishika'}


# modification in a dict:

roll={1:'kunal',2:'Aditya',3:'priya',4:'sinu'}
print(roll) #{1: 'kunal', 2: 'Aditya', 3: 'priya', 4: 'sinu'}

roll[3]='ishika'
print(roll) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}



# deletion of items in a dict

d={1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d)#{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

del d[4]
print(d) #{1: 'kunal', 2: 'Aditya', 3: 'ishika'}

# if we enter the key which is not avilable then it returns keyError

# del roll[24]
# print(d) #KeyError: 24



# To del all the items of the dict we use clear()

d={1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

d.clear()
print(d) #{}


# we can also delete the total dict 

d={1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d)

del d
# print(d)#NameError: name 'd' is not defined. Did you mean: 'id'?



# dict key are immutable in nature hence we can not use list,set,dict as a 
# dict key but we can use numbers,Tuple,frozenst as a dict key otherwise we
# will get TypeError

# 1.list as a key
# l=[10,20,30]
# d={l: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'} #TypeError: unhashable type: 'list'
# print(d)


#2.set as a key

# s={10,20,30}
# d={s: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'} #TypeError: unhashable type: 'set'
# print(d)


# 3. dict as a key:

# d={{1:'one'}: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'} #TypeError: unhashable type: 'dict'
# print(d)


# 4.Tuple as a key ---> we can use tuple as a key bcz tuple are immutable in nature

d={(10,20,30): 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d)#{(10, 20, 30): 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}


# 5.frozenset as a key:

s={10,20,30}
d={ frozenset(s): 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d)# {frozenset({10, 20, 30}): 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}


# can we use set as a value

s={10,20,30}

d={1:s, 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

print(d)#{1: {10, 20, 30}, 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
