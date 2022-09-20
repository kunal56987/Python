#bytes
a=[1,2,3,4,5]
b=bytes(a)
print(b[0])
print(b[-1])
# for print all the Element of bytes
for i in b:
    print(i)
# b[0]=10#'bytes' object does not support item assignment
# # we can't assing value or change value in bytes
# print(b[0])

#bytearray
c=[10,20,30,40,50]
d=bytearray(c)
print(d[1])
print(d[-1])
for i in d:
    print(i)
# In bytearray we can modify the values also
d[2]=200
for i in d:
    print(i)

