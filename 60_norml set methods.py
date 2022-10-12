# set method:

# 1.add() method:

# it is used to add single element to the set at one's

s={10,20,30,40}
s.add('kunal')
print(s) #{40, 10, 20, 'kunal', 30}

# if we add same element to the set then their is no effect no error occer

s.add('kunal')
print(s) #{40, 10, 20, 'kunal', 30}

# if we pass more than one argument then it gives type error bcz add() is only to add single element to the list

# s.add(999,56) #TypeError: set.add() takes exactly one argument (2 given)
# print(s)


# 2.update method:

# it is used to add muliple iterable element

s={10,20,30,40}
l=[1,2,3,4]
t=('kunal','maatey')
s.update(l,t)
print(s) #{1, 2, 3, 4, 'kunal', 40, 10, 'maatey', 20, 30}

# we can also pass range

s={10,20,30,40}
l=[1,2,3,4]
t=('kunal','maatey')
s.update(l,t,range(10,21))
print(s) #{1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 'kunal', 16, 17, 18, 20, 19, 30, 40, 'maatey'}

# If we pass two int element then it gives Error bcz int is not a iterable

# s.update(999,56) # TypeError: 'int' object is not iterable
# print(s)


# 3.remove() method

# it is used to delete a perticular element fron the set

s={24,52,65,75,84,36}
s.remove(52)
print(s) #{65, 36, 84, 24, 75}

# if pass that argument which is not avalable in the set then it gives key error:

# s={12,56,84,75,26}
# s.remove(99) #KeyError: 99
# print(s)


# 4.discard() method:

# it is used to delete an element from the set
s={12,56,84,75,26}
s.discard(12)
print(s) #{84, 56, 26, 75}

# if we pass that aurgaument which is not avalable in the set then it doesn't give any type of erroe:

s={35,56,78,94,45}
s.discard('kunal') # No Error
print(s) #{35, 56, 94, 45, 78}


# 5.pop() method:

# it is return and  delete rendom element from the set 

s={12,53,61,45,85}
s.pop()
print(s) #{85, 53, 12, 45}
print(s.pop()) #85
print(s) #{53, 12, 45}



#  6.copy() method

# it is used to create a sallow copy of a set

s1={20,51,63,42,61}
s2=s1.copy()
print(s1)
print(s2) 

# it will pointing to different memory location and if we change some contant of any set then it doesn't reflect to
# another

print(id(s1)) #2143946977152
print(id(s2)) #2143946977376

s1.add(999)
print(s1) #{51, 20, 999, 42, 61, 63}
print(s2) #{51, 20, 42, 61, 63}


# 7.clear() method:

# it is used to remove or delete all the content of a set and it returns empty set

s={51, 20, 42, 61, 63}
s.clear()
print(s) #set()


# 8.ennamorate() method

# it returns element as well as index value

s={12,13,14,15,16}
for i in enumerate(s):
    print(i)



# 9. min() and max() method:

# it return the min and max element of a set

s={42,54,95,41,1,32,46,75}
print(max(s)) #95
print(min(s)) #1


# 10. sum() method:

# it returns the sum of all the elements inside a set

s={42,54,95,41,1,32,46,75}
print(sum(s)) #386


#11. sorted() method:

# it returns the sorted value in ascending and in descending order but in a form of list.

s={12,51,43,61,75,92}
print(sorted(s)) #[12, 43, 51, 61, 75, 92]

# if we want to print in a revrse order:

print(sorted(s,reverse=True)) #[92, 75, 61, 51, 43, 12]