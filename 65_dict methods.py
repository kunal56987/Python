# dict methods:

# 1. get() methods:

# it returns the value of that key that u entered

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d.get(2)) # Aditya

#if the key is not present then it ruterns default value i.e. None

print(d.get(5)) #None

# we can also change the default value if the key is not present

print(d.get(99,'not avilable')) #not avilable

# if the key is present and we provide the default value then it not be reflected

print(d.get(4,'Not Avilable'))# sinu


# 2.items()

# it returns the  list of a tuple that contain key and value of a dict

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

print(d.items()) #dict_items([(1, 'kunal'), (2, 'Aditya'), (3, 'ishika'), (4, 'sinu')])

# by using for loop we can print the tuples

for i,j in d.items():
    print(i,' ',j)

# 1   kunal
# 2   Aditya
# 3   ishika
# 4   sinu


# 3.pop() method:

# it will delete and return the vaule accosited by that key

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

print(d.pop(3)) #ishika
print(d) #{1: 'kunal', 2: 'Aditya', 4: 'sinu'}


# if the key is not present the it riase KeyError 

# print(d.pop(3)) #KeyError: 3 bcz 3 is already deleted

# pop() method wants at least one argument otherwise it gives TypeError

# print(d.pop()) #TypeError: pop expected at least 1 argument, got 0



# 4. popitem() method:

# it will remove the last one and return both key and value in the form of tuple

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

print(d.popitem()) #(4, 'sinu')
print(d)# {1: 'kunal', 2: 'Aditya', 3: 'ishika'}

# if the dict is empty then it will raise KeyError
# d={}
# print(d.popitem()) #KeyError: 'popitem(): dictionary is empty'


# 5.keys() method

# it will return the keys of a dict in a form of List

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d.keys()) #dict_keys([1, 2, 3, 4])


# 6.value() method:

# it will return the values of a dict in a form of List
d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d.values()) #dict_values(['kunal', 'Aditya', 'ishika', 'sinu'])


# 7.setdefault() method:

# it will add the key and value if the key is not present in the dict

d={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d.setdefault(23,'Babaji')) #Babaji
print(d)#{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 23: 'Babaji'}

# if we provide present key then it will return the actule key value not the provided value

print(d.setdefault(2,'sherma ji')) #Aditya

# if we provide only key then it will add the key and default value i.e none if key is not avalible

print(d.setdefault(99)) #None
print(d) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 23: 'Babaji', 99: None}


# 8.update() method:

#  it will add or update the two dict

name={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
clg_name={11:'NIT',22:'KIIT',33:'ITER'}

name.update(clg_name)
print(name) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 11: 'NIT', 22: 'KIIT', 33: 'ITER'}
print(clg_name)# {11: 'NIT', 22: 'KIIT', 33: 'ITER'} it will not update bcz we update name dict

# if in both dict the key are same than it will update the value of that dict to updated one

d1={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
d2={1:'babaji',22:'Sharma ji'}

d1.update(d2)
print(d1) #{1: 'babaji', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 22: 'Sharma ji'} here kunal is updated to babaji



# 9.copy() method:

d1={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

d2=d1.copy()
print(d2) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d1) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

# but it pointing to different memory location

print(id(d1))#2225303395776
print(id(d2))#2225303126336


# if we change any items in any dict it will not reflect to another

d1[23]='Pikul'
print(d1) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 23: 'Pikul'}
print(d2) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}


# if we use = insted of copy then it will point to same memory location 
# if we change any item of any dict then it will also reflect to another

d1={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

d2=d1
print(d2) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
print(d1) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}

print(id(d1))
print(id(d2))

d1[23]='pinkul'
print(d1) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 23: 'pinkul'}
print(d2) #{1: 'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu', 23: 'pinkul'}



# 10.clear() method:

d1={1:'kunal', 2: 'Aditya', 3: 'ishika', 4: 'sinu'}
d1.clear()
print(d1) #{}



# 11.fromkeys() method:

# it is used to create a new dict from iterable objects like list,Tuple,range,etc
# and value(optional)


# creation of dict from list:

l=[10,20,30,40,50]
d=dict.fromkeys(l)
print(d) #{10: None, 20: None, 30: None, 40: None, 50: None}

d=dict.fromkeys(l,'name')
print(d)#{10: 'name', 20: 'name', 30: 'name', 40: 'name', 50: 'name'}


# creation of dict from tuple:

t=(23,33,43,53)
d=dict.fromkeys(t)
print(d) #{23: None, 33: None, 43: None, 53: None}


# creation of dict from range:

d=dict.fromkeys(range(10))
print(d)#{0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}


# we can also provide value 

d=dict.fromkeys(range(10),'kunal')
print(d)#{0: 'kunal', 1: 'kunal', 2: 'kunal', 3: 'kunal', 4: 'kunal', 5: 'kunal', 6: 'kunal', 7: 'kunal', 8: 'kunal', 9: 'kunal'}

# if we will provide the iterable object then what will be the output

#Ex-1
r=range(5)
l=[1,2,3]
d=dict.fromkeys(r,l)
print(d) #{0: [1, 2, 3], 1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3], 4: [1, 2, 3]}

#Ex-2
r=range(5)
l=[]
d=dict.fromkeys(r,l)
print(d) #{0: [], 1: [], 2: [], 3: [], 4: []}

#EX-3
d=dict.fromkeys([],[1,2,3])
print(d)#{}

#Ex-4
l=[]
d=dict.fromkeys(l,l)
print(d) #{}