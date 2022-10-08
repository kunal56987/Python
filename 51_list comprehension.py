# list comprehension is used to write code in less no of line of codes

# wap to add no 1-10 in list using list comprehension
# Ex-1
l=[i for i in range(11)]
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ex-2
s=[i*i for i in range(11)]
print(s) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Ex-3
l=[i**i for i in range(11)]
print(l) # [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]

# Ex-4
l=[i+i for i in range(11)]
print(l) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# we can also add conditions

# Ex-5
# TO print list which contain only even no between 1-20

# Using list comprehension:
l=[i for i in range(1,21) if i%2==0]
print(l) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# without using list comprehension:
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#name=['kunal','priyanka','kutti','srivastav']
#expected output---> ['k','p','k','s']

names=['kunal','priyanka','kutti','srivastav']
new_list=[i[0] for i in names]
print(new_list)# ['k', 'p', 'k', 's']

# we can also appely slicing concept
names=['kunal','priyanka','kutti','srivastav']
new_list=[i[0:3] for i in names]
print(new_list) #['kun', 'pri', 'kut', 'sri']


#wap to create a new list by add the element which is contaning letter a

names=['kunal','priyanka','kutti','srivastav']
new_list=[i for i in names if 'a' in i]
print(new_list) # ['kunal', 'priyanka', 'srivastav']


# Wap to create a list in which if the element is priyanka than don't add it insted of that add Hello
names=['kunal','priyanka','kutti','srivastav']
new_list=[i if i!='priyanka' else 'Hello' for i in names]
print(new_list)


#creating list from tuple
# Ex-1
t=(10,20,30,40,50,60)
l=[i for i in t]
print(l) # [10, 20, 30, 40, 50, 60]

# Ex-2
# add elements  from tuple which is only divisible with 6 

t=(10,20,30,40,60,45,12,34)
l=[i for i in t if i%6==0]
print(l) # [30, 60, 12]


# Creating list from String
name='kunal'
l=[i for i in name]
print(l) # ['k', 'u', 'n', 'a', 'l']



# Creation of matrix using list comprehension

# Ex-1
l=[[j for j in range(3)] for i in range(3)]
print(l) # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Ex-2
l=[[i for j in range(3)] for i in  range(3)]
print(l) # [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

# Ex-3
l=[[i+j for j in range(5)] for i in range(3)]
print(l) # [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
