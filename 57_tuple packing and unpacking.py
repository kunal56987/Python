# tuple packing

a=23
b=33
c=43
d=53
e=63
t=a,b,c,d,e #packing
print(t) #(23, 33, 43, 53, 63)
print(type(t)) #<class 'tuple'>


# Tuple unpacking:
t=(23, 33, 43, 53, 63)
a,b,c,d,e=t
print(a,b,c,d,e)

# At the time of unpacking the numbers of variable and number of elements of tuple must be same otherwise it gives error

# t=(23, 33, 43, 53, 63)
# a,b,c=t #ValueError: too many values to unpack (expected 3)
# print(a,b,c)