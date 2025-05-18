# keyword argument - relation between argument and parameter
def fibp(x,y,z):
    print("value of x =",x)

p =10
q=20 
r= 30 
# fibp()   
# # fibp(p)
# fibp(p,q)
fibp(p,r,q)
# fibp(p,q,r,s)


# default argument
def fibp(x=0,y=0,z=0):
    print("value of x =",x)
    print("value of y =",y)

p =10
q=20 
r= 30 
fibp()   
fibp(p)
fibp(p,q)
# fibp(p,r,q,s)


# variable length positionl argument - it hold data in form of tuple (* args)
def fibp(* n):
    print(n)
    print(type(n))

# p =10
# q=20 
# r= 30 
# fibp()   
# fibp(p)
# fibp(p,q)
fibp(3,3,4,)


def fibo(* args):
    sum=0
    for i in args:
        sum=sum+i
    return sum    
x= fibo(2,4,6,8) 
print(x)   

def fibo(* args):
    sum=0
    for i in args:
        for j in i:
         sum=sum+j
    return sum    
p=(3,4,56,)
x= fibo(p) 
print(x)   

#keyword argument -  it hold data i dictionry form(** kwargs)
def new(**n):
    print(n)
    print(type(n))
new(name='neeraj',age=21)    
    



def  new(**n):
    for k,v in n.items():
        print(f'my key is {k} and value is {v}')
    
new(name='neeraj',age=21)    
    




def  new(**n):
    for k,v in n.values():
        print(f'my key is {k} and value is {v}')
    
new(name='neeraj',age=21)    
        


# 

