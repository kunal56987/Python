#wap to print the element of list which is divisible by 4 & 8.
l=[10,34,24,54,67,87,94,16,28]
for i in l:
    if i%4==0 and i%8==0:
        print(i)

#wap to display list element of a list along with positiv and negative index:
l=eval(input('Enter a list inside []:'))
n=len(l)
for i in range(n):
    print('{} is at index {}/{}'.format(l[i],i,i-n))
