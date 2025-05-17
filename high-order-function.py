# MAP() - syntax map(function name,collection(list tuple string))

l =[1,23,4]

def add5(n):
    return n+5
x=map(add5,l)
print(x)
print(tuple(x))




l =[1,23,4]
l2 =[3,4,5]

def add5(n ,m):
    return n+m
x=map(add5,l,l2)
print(x)
print(tuple(x))





l =[1,23,4]
l2 =[3,4,5]

def add5(n ,m):
    return n**m
x=map(add5,l,l2)
print(x)
print(list(x))





#filter

l =[1,23,4]

def add5(n):
    return n%2==0
x=filter(add5,l)
print(x)
print(list(x))



