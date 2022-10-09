# 1.append() method:

l=[10,20,30,50,55,40]
print(l)
l.append(999)
print(l)
# append() is used to add element in the last position.

# wap to add 20 0's in a list
l=[]
for i in range(20):
    l.append(0)
print(l)

# wap to add numbes from 1-10 in a list
l=[]
for i in range(11):
    l.append(i)
print(l)



# 2.insert() method:
# insert() is used for adding element at the specific position
l=[55,85,96,85,78]
print(l)
l.insert(3,999) # it will insert 999 at the index no 3 but not update the value of index 3=85
print(l)
l.insert(90,33) # If the positive index crossed the maximum index,then it will inserted at the end of the list .
print(l)
l.insert(-99,10)# if the negative index crossed the minimum index,then it will inserted at first of the list.
print(l)
l.insert(-3,0000)
print(l)



# # 3.count() method:
# l=[10,20,33,50,10,33,50,65]
# print(l.count(10)) # it will count how many times the element repeted
# print(l.count(20))




# # 4.remove() method:
# l=[10,20,33,50,10,33,50,65]
# print(l)
# l.remove(33) # if the element  occures many times then occure first i.e. at the index[2] 33 comes first so it will romoved
# print(l)
# #l.remove(999) # it gives value Error bcz 999 is not present inside the list




# # 5.pop() method:
# #pop() is revome element on the basis of indix value
# l=[10,20,30,40,50,60,]
# print(l)
# l.pop(2)
# print(l)
# # l.pop(99) it gives index error bcz 99 index is not present insid the list





# # 6.index() method:
# # index() is used for knowing the index value of the element
# l=[33,53,63,43,23]
# print(l.index(43))
# # print(l.index(99)) # it will give value error




# # 7.extend() method:
# # extend() is used to merge two list
# l=[10,20,30,40,50,60]
# s=[100,200,300,'kunal']
# l.extend(s)
# print(l)




# # 8.reverse() method:
# # reverse() is used to revrese an list:
# l=[10,20,30,40,50]
# print(l)
# l.reverse()
# print(l)


# # 9.sort() method:
# # sort() is used to sort a list in ascending or descending order
# l=[6,8,9,2,3,1,5,4,7,10]
# l.sort()# it will sort in ascending order
# print(l)

# l.sort(reverse=True) # it will sort in descending order
# print(l)

# # if l contain strings then it will sort according to Alphabet order like English dictionary
# # Ex-1
# l=['kunal','srivastava','maatey','laxmi','priya','ankita']
# l.sort()
# print(l)

# #Ex-2
# l=['d','c','b','a','D','B','C','A']
# l.sort()
# print(l) #['A','B','C','D','a','b','c','d']
# l.sort(reverse=True)
# print(l)

# #EX-3
# l=['a','b','c','d']
# l.sort(reverse=True)
# print(l)

# # if list contain hetrogenous elements

# # l=['kuanl','srivastava',10,30,20]
# # l.sort()
# # print(l)# it gives type error bt we sort in python 2 but in python 3 it is not possible




# # 10.clear() method:

# #it is used to delete all the elements from the list

# l=[10,90,45,67,56]
# print(l)
# l.clear()
# print(l)



# # 11.copy() Method:

# l=[10,20,30,40,50]
# s=l.copy()
# print(l) #1864463949632
# print(s) #1864463949376
# # it will print the same list but it points to different memory location

# print(id(l))
# print(id(s))

# # if we modify the elements of list 's' then it will not reflected to the list 'l'

# s[1]=999
# print(l) #[10, 20, 30, 40, 50]
# print(s) #[10, 999, 30, 40, 50]


# # if we use = insted of copy() methon then it will posint to the same memory location

# l=[10, 20, 30, 40, 50]
# s=l
# print(l)
# print(s)

# print(id(l))
# print(id(s))
# # both list 'l' and 's' pointing to the same memory location

# # if we modify any list then it refelect to the another list also bcz both are pointing to the same memory location

# s[2]=999
# print(l)
# print(s)