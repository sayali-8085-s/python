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

# x = reduce()




# 4)decorator -spcl function whicch change internal behviour of function without changing the code
# it take function as parameter and return  another function
# it is represented by @

# python tutor -imp for debugging


#internal working
# def outer_fun(f):
#     def inner_fun(p,q):
#         p=p+5
#         q =q+5
#         d =f(p,q)
#         return d
#     return inner_fun

# def add(a,b):
#     return a+b

# x = outer_fun(add)
# print(x)
# z=x(10,20)
# print(z)


#main to do
def outer_fun(f):
    def inner_fun(p,q):
        p=p+5  #modification
        q =q+5
        d =f(p,q)
        return d
    return inner_fun
@outer_fun    #decorator
def add(a,b):
    return a+b

x = add(10,30)
print(x)