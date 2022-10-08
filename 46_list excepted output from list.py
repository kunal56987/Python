#l=['Hi','Hello']
#s=['Kunal','laxmi','priya','Harsh']

# output
# new_list=['Hi kunal','Hi laxmi','Hi priya','Hi Hrash','Hello Kunal",'Hello laxmi','Hello priya','Hello Harsh']
l=['Hi','Hello']
s=['Kunal','laxmi','priya','Harsh']
new_list=[]

for i in l:
    for j in s:
        new_list.append(i+' '+j)
print(new_list)
