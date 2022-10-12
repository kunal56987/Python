# 1.creation of set with list

#Ex-1

l=[10,20,30,40,50]
s={i for i in l}
print(s)# {40, 10, 50, 20, 30}

#Ex-2
l=[10,20,30,40,50]
s={i*2 for i in l}
print(s) #{100, 40, 80, 20, 60}

# Ex-3
# creat a set from list called name by adding first char of each element

name=['kunal','ankita','sinu','prem']
s={i[0] for i in name}
print(s) #{'k', 'a', 's', 'p'}

#Ex-4
# create a set from a list (name) by adding the element but if the element starts with char a than change to laxmi

name=['kunal','ankita','sinu','prem']
s={i if i[0]!='a' else 'laxmi' for i in name}
print(s)#{'laxmi', 'kunal', 'prem', 'sinu'}


# 2.Work With range:

s={i for i in range(23,43)}
print(s)#{23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42}


# create a set by adding all the element from 20 to 40 which is
# divisible by 4

s={i for i in range(20,41) if i%4==0}
print(s) #{32, 36, 40, 20, 24, 28}


# 3.working with tuple

t=(10,21,42,51,31)
s={i for i in t}
print(s) #{10, 42, 51, 21, 31}