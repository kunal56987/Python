#wap to surch an value from a list then display its index
#if the value is present multiple times then print its all indices and
#also count the number of time that value repeted in the list.

l=[10,65,75,84,95,64,75,84,95,62,64,10]
key=int(input('Enter the value you want to serach:'))
i=0
count=0
while i<len(l):
    if key == l[i]:
        print(f'{key} is present at {i} index')
        count+=1
    i+=1
print(f'{key} is present {count} times')