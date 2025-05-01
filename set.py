# unorderd collection of unique element ( homogenious and hetro)
# it remove duplicate value
s ={ 1,2,3,4,5,5,6,'hii','python','class'}
print(s)
print(type(s))
print(id(s))

# FUNCTION

# for sum homo but integer and for min max homo string or num

s ={ 1,2,3,4,5,5,6,'hii','python','class'}
print(len(s))

# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# print(max(s))

# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# print(min(s))

# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# print(sum(s))


s ={'hii','python','class'}
print(min(s))

# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# print(sum(s))

s ={ 1,2,3,4,5,5,6}
print(sum(s))

s ={ 1,2,3,4,5,5,6}
print(max(s))


# METHOD

# 1)add - to add new element in random position
s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.add(8)
print(s)


# 2) update(collection) - multiple element add in random in collection form

# if there is modify in collection (s)then we hv to print collcetion (s) after updation

# it give error
# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# s.update(6)
# print(s)


s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.update('php','da')
print(s)


s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.update([8,9])
print(s)


# 3) pop () - remove random  one element
s ={ 1,2,3,4,5,6,'hii','python','class'}
s.pop()
print(s)

s ={ 1,2,3,4,5,6,'hii','python','class'}

print(s.pop())



# 4) remove() - remove one target element , it give error when element is not in set

s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.remove('hii')
print(s)


# s ={ 1,2,3,4,5,5,6,'hii','python','class'}
# s.remove('say')
# print(s)


# 5) discard() - to overcom error of remove


s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.discard('say')
print(s)


# 6) copy() - creat new object of different address
s ={ 1,2,3,4,5,5,6,'hii','python','class'}
a =s.copy()
print(id(s) , id(a))


# 7) clear - give empty set()

s ={ 1,2,3,4,5,5,6,'hii','python','class'}
s.clear()
print(s)

#8) union -
s1 ={1,2,3,4 ,'hii'}
s2 ={ 5,6,7,8}
print(s1.union(s2))


# 9) intersecton
s1 ={1,2,3,4}
s2 ={ 4,5,6,7,8}
s3 = s1.intersection(s2)
print(s3)

# 10) difference 
s1 ={1,2,3,4}
s2 ={ 4,5,6,7,8}
print(s1.difference(s2))


# 11)  symmetric diffence - opposite of intersection
s1 ={1,2,3,4}
s2 ={4, 5,6,7,8}
print(s1.symmetric_difference(s2))

# 12)intersection-update - change exixting 
s1 ={1,2,3,4,8}
s2 ={4, 5,6,7,8}
s1.intersection_update(s2)
print(s1)


s1 ={1,2,3,4,8}
s2 ={ 5,6,7,8}
s1.symmetric_difference_update(s2)
print(s1)


s1 ={1,2,3,4}
s2 ={4, 5,6,7,8}
s1.difference_update(s2)
print(s1)

# is disjoint - no common element give true
s1 ={1,2,3,4}
s2 ={4, 5,6,7,8}
print(s1.isdisjoint(s2))


# issubset
s1 ={1,2,3,4}
s2 ={ 5,6,7,8}
print(s1.issubset(s2))

# is superset
# imp
s1 ={1,2,3,4}
s2 ={1,2,3,4}
print(s1.issuperset(s2))
print(s1.issubset(s2))
