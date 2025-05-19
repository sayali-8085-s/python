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





#filter - filter(fun-name ,collection)

l =[1,23,4]

def even(n):
    if n%2==0:

       return n
x=filter(even,l)
print(x)
print(list(x))



l =[1,23,4]

def grtr(n):
    if n>5:

       return n
x=filter(grtr,l)
print(list(x))


# another way or conventional method
l =[2,4,5,6]
l1=[]
for i in l:
    if i>=5:
        l1.append(i)
print(l1)        



# reduce() - 

from functools import reduce
l =[1,8,5,6,7]

def maxv(x,y):
    if x>y:
       return x
    else:
       return y

       
x=reduce(maxv,l)
print(x)



from functools import reduce
l =[1,8,5,6,7]

def minv(x,y):
    if x<y:
       return x
    else:
       return y

       
x=reduce(minv,l)
print(x)


from functools import reduce
l =[1,8,5,6,7]

def sum(x,y):
       return x+y
    
       
       
x=reduce(sum,l)
print(x)


# quet


from functools import reduce
l =[1,23,4]

def add5(n):
    return n+1
x=map(add5,l)

p=tuple(x)
  
def add(p,m):
    return p+m

y =reduce(add,p)
print(y)


# or 

x = reduce()


