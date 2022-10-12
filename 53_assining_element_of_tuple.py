# Assining by index

t=(10,20,30,40,50)
print(t[0]) #10
print(t[-1]) #50
# print(t[99]) #IndexError: tuple index out of range

# Assining by slice operator:

t=(10,20,30,40,50)
print(t[::]) #(10, 20, 30, 40, 50)
print(t[::2]) #(10, 30, 50)
print(t[:3:]) #(10, 20, 30)

# tuple is immutable in nature:
t=(10,20,30,40,50,44)
# t[2]=99 #TypeError: 'tuple' object does not support item assignment