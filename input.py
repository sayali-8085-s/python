x=input("enter a value = ")
print(type(x))
# by default input always give string datatype 
# if we give eval before input then it give true data type
# tuple can also be like (10,)
x=eval(input("enter a value = "))
print(x)
print(type(x))


# id - adderss
x="hii"
print(id(x))