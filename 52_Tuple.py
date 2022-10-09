# creation of tuple in different ways:

# 1. creation of empty tuple:
t=()
print(t) #()
print(type(t)) #<class 'tuple'>

# 2.creation of tuple with single value

t=(17) #if we write like this then python trite this as int not as tuple
print(t) #17
print(type(t)) #<class 'int'>

# we can solve this problem by add (,) after the value

t=(17,)
print(t) #(17,)
print(type(t)) #<class 'tuple'>

# 3.creation of tuple with different data items

t=(17,'kunal',True,13.4)
print(t) #(17, 'kunal', True, 13.4)

# 4.creation of tuple without using ()
t=10,20,30,'kunal',True,19.4
print(t) #(10, 20, 30, 'kunal', True, 19.4)
print(type(t)) #<class 'tuple'>

# 5.creation of tuple using tuple() function:

l=[10,20,30,40]
t=tuple(l) # it convert list to tuple
print(t) #(10, 20, 30, 40)
print(l) #[10,20,30,40]

t=tuple(range(10)) #it will genrate tuple from 0-9
print(t) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

t=tuple('kunal')
print(t)
