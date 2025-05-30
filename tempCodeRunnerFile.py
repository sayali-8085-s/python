
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


# 4)decorator -spcl function whicch change internal behviour of function without change code
# it take function as parameter and return function

# python tutor -imp for debugging


def outer_fun(f):