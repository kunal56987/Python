# 1.union() method:

A={13,43,612,42}
B={40,51,13,26,42}
print(A.union(B)) #{612, 40, 42, 43, 13, 51, 26}
# Here we get all the elements of set A and B And common elements at one's

# we can also write as 
 
print(A|B) #{612, 40, 42, 43, 13, 51, 26}


# 2.intersection() method:

# Here we get common elements of two sets

A={42,52,62,72,82}
B={12,34,51,42,82}
print(A.intersection(B)) #{82, 42}

# we can also write as

print(A & B) #{82, 42}


# 3.difference() method:

A={12,54,62,35,84}
B={31,51,12,36,85,62}
print(B.difference(A)) #B-A {51, 36, 85, 31}

print(A.difference(B)) #{35, 84, 54}  A-B


# 4.symmetric_difference() method:

# it mean all the elements of the two set except common element:

A={12,54,62,35,84}
B={31,51,12,36,85,62}
print(A.symmetric_difference(B)) #{84, 85, 31, 35, 36, 51, 54}

# we can also write as:
print(A^B) #{84, 85, 31, 35, 36, 51, 54}


# 5.issubset() method:

# if we have two sets suppose A and B and if B contens all the elements of A then we call B is a subset of A.

A={24,52,62,32,42,51}
B={62,32,42}
print(B.issubset(A)) #True

print(A.issubset(B)) #False



# 6.issuperset() method:

 # if we have two sets suppose A and B and if B contens all the elements of A then  we call A is a superset of B.

A={24,52,62,32,42,51}
B={62,32,42}
print(A.issuperset(B)) #True

print(B.issuperset(A)) #False


# 7.isdisjoint() method:

# if have two set and both sets have different elements then it is called distjoint set

A={23,51,62,42,31}
B={20,10,61,43,17}
print(A.isdisjoint(B)) #True

A={23,51,62,42,31}
B={20,10,61,43,17,23}
print(A.isdisjoint(B)) #False