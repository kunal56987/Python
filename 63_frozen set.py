# 1.creation of frozen set 

# a.creating empty frozenset:

fz=frozenset()
print(fz) #frozenset()


# b.creating frozenset with set:
s={12,22,22,25}
fz=frozenset(s)
print(fz) #frozenset({25, 12, 22})

# c.Creating frozenset from list
l=[10,20,30,40,50]
fz=frozenset(l)
print(fz) #frozenset({40, 10, 50, 20, 30})


# d. creating frozenset with range
fz=frozenset(range(10))
print(fz) #frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# we can not use modifiation operation in frozenset bcz frozenset is immutable
# if we use add() or update() method thn it gives error

fz=frozenset(range(10))
# fz.add(99)
# print(fz) #AttributeError: 'frozenset' object has no attribute 'add'

# fz.update([10,20]) AttributeError: 'frozenset' object has no attribute 'update


# we can apply other opertation except modification opertations

fz1=frozenset([23,33,43,53,63])
fz2=frozenset([11,12,13,23,63])
fz3=frozenset([23,43])

# copy()
fz4=fz1.copy()
print(fz4)#frozenset({33, 43, 53, 23, 63}) 

# union()
print(fz1.union(fz2))#frozenset({33, 43, 11, 12, 13, 53, 23, 63})

#intersection()
print(fz1.intersection(fz2)) #frozenset({63, 23})

#difference()
print(fz2.difference(fz1)) #frozenset({11, 12, 13})

#symmetric_difference()
print(fz1.symmetric_difference(fz2)) #({33, 53, 43, 11, 12, 13})


# issubset()

print(fz3.issubset(fz1)) #True

#issuperset()

print(fz1.issuperset(fz3)) #True

# isdisjint()
fz5=frozenset([11,13])
print(fz1.isdisjoint(fz5)) #True