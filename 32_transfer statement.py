# In python their are three types of transfer statement
#1. break  2. continue  3.pass

# break--- it is used to break or cut the flow of execution
for i in range(10):
    if i==7:
        break# when i=7 then it breaks the loop and come out from the loop
    print(i)

#continue---- skip
for i in range(10):
    if i==4 or i==8:
        continue # when i=4 or i=8 it gose to the loop it does not read the code after continue
    print(i)

#pass --- pass means empty block or statement

for i in range(10):
    if i%2==0:
        pass #if i%2=0 then it do nothing and pass to the next line or the loop
    else:
        print(i)