 #generate collection but in controlled way
def natural(n):
    i =1
    while i<n:
        yield i # hols value and its position , not terminate
        i=i+1
x =  natural(10)  
# for i in x :
#     print(i)      
print(next(x))
print('hello')
print(next(x))
# module packge file -