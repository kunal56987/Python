s=input('Enter a string:')
d={}
for i in s:
    d[i]=d.get(i,0)+1

print(d)#{'m': 2, 'a': 2}

for i,j in d.items():
    print(f'{i} is present {j} times')
# m is present 2 times
# a is present 2 times