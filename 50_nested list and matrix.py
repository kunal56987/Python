#Represent a nested list
#Ex-1

l=[10,20,30,[40,41,41],50,60,70]
print(l) 
print(l[2])  #30
print(l[3]) #[40,41,42]
print(l[3][1])  #41
print(l[3][0]) #40
print(l[3][-1]) #41
print(l[-4][-1]) #41


#Ex-2
l=[10,20,30,[40,41,41],50,[11,22,33],60,70]
print(l[5]) #[11, 22, 33]
print(l[2:6]) #[30, [40, 41, 41], 50, [11, 22, 33]]


#EX-3
l=[10,20,30,[40,41,[1,2,3],41],50,60,70]
print(l[4]) #50
print(l[3]) #[40, 41, [1, 2, 3], 41]
print(l[3][2]) #[1, 2, 3]
print(l[3][2][0]) #1
print(l[-4][-2][-1]) #3
print(l[-4][-2][-2]) #2 
print(l[-4][-2][-3]) #1


#Nested  list as a matrix


l=[
    [10,20,30],
    [21,32,43],
    [43,54,65]
]

print(l) # [[10, 20, 30], [21, 32, 43], [43, 54, 65]]

# print in row wise
print(l[0])# [10, 20, 30]
print(l[1])# [21, 32, 43]
print(l[2])# [43, 54, 65]

# print row wise by using loop:

l=[
    [10,20,30],
    [21,32,43],
    [43,54,65]
]

for i in l:
    print(i)
    # [10,20,30]
    # [21,32,43]
    # [43,54,65]

# if we want matrix without [] and ,
l=[
    [10,20,30],
    [21,32,43],
    [43,54,65]
]

for i in l:
    for j in i:
        print(j,end=' ')
    print(' ')
# Output
# 10 20 30
# 21 32 43
# 43 54 65



# To reverse the list using function


l=[10,20,30,[40,41,41],50,60,70]
l.reverse() # It will not reverse the nested list
print(l) # [70, 60, 50, [40, 41, 41], 30, 20, 10]
