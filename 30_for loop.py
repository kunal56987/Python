
#Ex-1
for i in range(10):
    print('kunal')
    
#Ex-2
# 1 2 3 4 5 6 7 8 9 10
for i in range(1,11,1):
    print(i)    

#Ex-3
# 2 3 4 5 6 7 8
for i in range(2,9,1):
    print(i)    

#Ex-4
# 200 400 600  800 1000
for i in range(200,1001,200):
    print(i)    

#Ex-5
# 10 9 8  7 6 5 4 3 2 1
for i in range(10,0,-1):
    print(i)

#Ex-6
#999 777 555 333 111
for i in range(999,110,-222):#(start,stop,step)
    print(i)

#Ex-7
#Print all even number from 100 to 120
for i in range(100,121,1):
    if i%2==0:
        print(i)

#OR
for i in range(100,121,2):
    print(i)        

#Ex-8
name='kunal srivastava'
for i in name:
    print(i)

#Ex-9
name='888888'
for i in name:
    print(i)

#Ex-10
name='priyanka'
for i in name:
    print(i,end='_')