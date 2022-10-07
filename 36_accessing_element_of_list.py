# we can access list in two way 1.index 2.by using slice operator

# 1.By using index:
l=[10,20,40,65,74,89]
print(l[0])
print(l[5])
print(l[-1])
print(l[-4])
# print(l[22])# index error

# 2. By using slice operator:
l=[10,20,40,65,74,89]
print(l[::])
print(l[1:4:2])
print(l[2::2])
print(l[::3])