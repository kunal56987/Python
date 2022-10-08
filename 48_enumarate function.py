# enumarate()is used to genrate list into tupel format with (index,value)
l=[10,20,30,40,50]
for i in enumerate(l):
    print(i)
#output
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)
# (4, 50)

l=[10,20,30,40,50]
for i,j in enumerate(l):
    print(i,' ',j)
