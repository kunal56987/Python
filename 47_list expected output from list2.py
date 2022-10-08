# l=['kunal','srivastava','laxmi','priyanka']
#output
# ['kl', 'sa', 'li', 'pa']

l=['kunal','srivastava','laxmi','priyanka']
new_list=[]
for i in l:
    new_list.append(i[0]+i[len(i)-1])
print(new_list)