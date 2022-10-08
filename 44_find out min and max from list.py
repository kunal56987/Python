l=[22,45,67,1,89,423,90,999,0]
min=l[0]
max=l[0]
for i in l:
    if min>i:
        min=i
    if max<i:
        max=i
print('min={}'.format(min))
print('max={}'.format(max))