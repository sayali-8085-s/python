
# when key is same it take latest value of key
# when value is same it give smae result
# index not supprot in dictionary we acn get dta by uing key
d = {'name':21,'age':21}
print(d)
print(type(d))
print(id(d))


# FUNCTION
# on the basis key ascii value calculate max min not sum  , for sum interger reqired ,key value sholud be integer or number then we can find sum
# and if key value is number or string then error in sum and min ,max
d = {'name':21,'age':21}
print (max(d))

d = {'name':21,'age':21}
print (min(d))

# d = {'name':21,'age':21}
# print (sum(d))



d = {1:21,2:'hii'}

print (max(d))

d = {1:21,2:'hii'}

print (min(d))


d = {1:21,2:21}

print (sum(d))


# d = {1:21,'name':21}

# print (min(d))


# d = {1:21,'name':21}

# print (sum(d))


# we can not found length on integer

x = 10 
y = str(x)
print(type(y))
print(len(y))


# METHOD

# 1)copy - it is used to create new object


d = {'name':21,'age':21}
l1 = d.copy()

print(id(d),id(l1))



# 2) clear() - remove all pair from dict

d = {'name':21,'age':21}

print(d.clear())
 
print(id(d))

# it is uesd to claer the hold memory
# del d
# print(d)



# 3) pop() - remove target key from dict

d = {'name':21,'age':21}
d.pop('age')
print(d)


# 4) popitems() - to remove last pair\item

d = {'name':21,'age':21}
d.popitem()
print(d)


# 5)get('key) - get value of target key


d = {'name':21,'age':21}

print(d.get("name"))


# 6) keys() - get all keys from dict in form of list

d = {'name':21,'age':21}

print(d.keys())





# 7)values() -  get all keys from dict in form of list

d = {'name':21,'age':21}

print(d.values())


# 8) items -  get all pairs\items from dict in form of list


d= {'name':21,'age':21}

print(d.items())



# 9)fromkeys(collection) - create new dict on the basis of given collection element

s ='python'
dic = {}
d= dic.fromkeys(s)

print(d)

# when we give value exa(10)  it give  same value to all keys
s = [1 ,2 ,3,'hii']
dic = {}
d= dic.fromkeys(s ,10)

print(d)



# 10) setdefault() - if key exist there is no change if not exsit add another pair - it also chec whether key exist or not

d= {'name':21,'age':21}

d.setdefault('name' ,200)
print(d)

d= {'name':21,'age':21}

d.setdefault('p' ,200)
print(d)


# 11) upadte
d= {'name':21,'age':21}
d1= {2 : 1 , 6:1}

d.update(d1)
print(d)
print(d1)



# CRUD OPERATION


# creat
d ={}
print(type(d))

d['key'] = 'value'
d['hii'] = 'value'
print(d)


# update/edit
d['key'] = 'say'
print(d)   


# get/read value
x=d['key']
print(x)


# delete

d.pop('key')
print(d)
