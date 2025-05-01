# unordered collection(koi v cllection) of unique element 
# used to freeze(no changein structure) any collection this exception case in immutalble(giv e difer memory address fir v immutable) due to freez
# in immutable we cn not change structure
s = 'python'
fs = frozenset(s)
print(fs)
print(type(fs))
print(id(fs))


# FUNCTION for min and max - it should be collection of string or number ,for sum only integer

s = 'python'
fs = frozenset(s)
print(min(fs))

s=[1,2,3,4]
fs = frozenset(s)
print(max(fs))


# METHODS 

# 1)union
s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.union(fs2))

# 2)intersection

s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.intersection(fs2))


# 3)difference
s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.difference(fs2))


# 4)symmetric-differnce


s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.symmetric_difference(fs2))


# 5)isdisjoint

s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.isdisjoint(fs2))


# 6) issubset

s1=[1,2,3,4]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.issubset(fs2))

# 7) issuperset
s1=[1,2,3,4 ,34]
s2=(1,2,34,)
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print(fs1.issuperset(fs2))
