
# 1) append() - add single element in last position
l = [ 1 ,3 ,4,'hii','python']
l.append("hii")
print(l)

l = [ 1 ,3 ,4,'hii','python']
t = ['python' , 'java']
l.append(t)
print(l)


# 2) extend()- add multiple element in last position - give error if two argument/value

# l = [ 1 ,3 ,4,'hii','python']
# l.extend("class" ,"there")
# print(l)


# it seperate class
l = [ 1 ,3 ,4,'hii','python']
l.extend("class")
print(l)


l = [ 1 ,3 ,4,'hii','python']
t = (20,10)
l.extend(t)
print(l)



# 3) insert()- add single element in target position

l = [ 1 ,3 ,4,'hii','python']
l.insert(0,"hii")
print(l)

l = [ 1 ,3 ,4,'hii','python']
l.insert(1,['python','hii'])
print(l)



# 4) pop() - remove last element permanent  ,  by default -1 pass as an argument  ,only one argument we cn give


l = [ 1 ,3 ,4,'hii','python']
l.pop(2)
print(l)

l = [ 1 ,3 ,4,'hii','python']
print(l.pop(4 ))
print(l)


# 5) remove() - remove target element


l = [ 1 ,3 ,4,'hii','python']
l.remove(3)
print(l)


# 6) copy( ) - create new object with same element , give different memory address

l = [ 1 ,3 ,4,'hii','python']
l1 = l.copy()

print(id(l),id(l1))



# 7) clear()- remove all element , if list empty  it also hold memory address

l = [ 1 ,3 ,4,'hii','python']
l1 = l.clear()
print(l)
print(id(l),id(l1))

# it is used to free memory address of list

# del l
# print(l)

# 8) reverse() - 

# it give none result
l = [ 1 ,3 ,4,'hii','python']
print(l.reverse())

l = [ 1 ,3 ,4,'hii','python']
l.reverse()
print(l)


# 9) sort() - arrange ascending order  / give error in hetrogenous(linter ,string)

# 
# l= [ 1 ,3 ,4,'hii','python']
# l.sort()
# print(l)

# arrange accoding to ascii value
l= [ 'hello','Python']
l.sort()
print(l)

# in desending order
l= [ 1 ,6 ,4,]
l.sort()
l.reverse()
print(l)





# 10) count() - repeation , if not give 0

l = [ 1 ,3 ,4,'hii','python']
print(l.count(1))



# 11) index9() -