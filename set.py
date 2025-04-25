list=[1,1,1,1,2,2,2,3,3,3]
sample_set=set(list)
print(sample_set)

if 4 in sample_set:
    print("yes")
else:
    print("no")

myset=set([])
myset.add(2)
myset.add(4)
myset.add(5)
myset.add(2)
myset.add(1)

print(myset)

myset.remove(4)
print(myset)

myset.discard(1)
print(myset)

a={1,2,3,4,5,6}
b={4,5,6,7,8}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(b - a)

print(a.symmetric_difference(b))
print(a ^ b)