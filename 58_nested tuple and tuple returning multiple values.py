# 1.Nested Tuple:

t=((23,'kunal',79.8),(23,'maatey',79.8))
print(t[0]) #(23, 'kunal', 79.8)
print(t[1]) #(23, 'maatey', 79.8)

# we also acces nested tuple using loop
t=((23,'kunal',79.8),(23,'maatey',79.8))
for i in t:
    print(i)

# we can not modify the tuple but we modify nested tuple if it contain list

t=((23,'kunal',79.8),[23,'maatey',79.8])
print(t) #((23, 'kunal', 79.8), [23, 'maatey', 79.8])

t[1][1]='kutti' #t[1] is list thats why we can do modification

print(t) #((23, 'kunal', 79.8), [23, 'kutti', 79.8])



# 2.Tuple returning multiple values:

def fun():
    l=[23,33,43,53,63]
    return (l[0],l[3],l[-1])


t=fun() #it returns (23, 53, 63)
print(t) #(23, 53, 63)
print(type(t)) #<class 'tuple'>


# 3.tuple comprehension:

t=(i for i in range(10))
print(t) #<generator object <genexpr> at 0x000001C951D407B0>

#here we will not get tuple object, indted of tuple object we get generating object.

# we can do comprehension of tupe bt we have to write the comprehension code inside tuple() function

t=tuple(i for i in range(10)) #Here we will convert generator to tuple
print(t) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)