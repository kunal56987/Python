# 1.index() method:
#it will return the index of first occurence of the given element


t=(23,33,43,53,63,23,43,33)
print(t.index(43)) #2


# 2.count() method:
# it will return the specified element present hoe many times.
t=(23,33,43,53,63,23,43,33)
print(t.count(23)) #2
print(t.count(53)) #1
print(t.count(99)) #0


# 3.len() method:
# it is used to calculate the length of tuple
t=(23,33,43,53,63,23,43,33)
print(len(t)) #8


# 4.min() and max() method:
# it is used to find min and max element in tuple

t=(33,54,75,12,0,36,88,52,99)
print(min(t)) #0
print(max(t)) #99


# 5.sorted() method:

#it will sort the tuple but after sorting it will convert into list
t=(2,5,8,3,1,6,4,9)
s=sorted(t)
print(s) #[1, 2, 3, 4, 5, 6, 8, 9]
print(type(s)) #<class 'list'>

# we can also sort in descending order by passing reverse=True
t=(2,5,8,3,1,6,4,9)
s=sorted(t,reverse=True)
print(s) #[9, 8, 6, 5, 4, 3, 2, 1]


# 6.cmp() method:

# cmp() is used to compare tuple but in python 3 onwards it is outdated.
# but it will work in python 2 

# t1=(10,11)
# t2=(10,1)
# t3=(10,1)
# print(cmp(t1,t2)) #1
# print(cmp(t2,t1)) #-1
# print(cmp(t2,t3)) #0

# output of the above code when we run in python 2 version