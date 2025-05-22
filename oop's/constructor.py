# magic variable

class First:
    "hello"
    pass
print(dir(First))
print(First.__doc__)

# consturctor - it is special method in which object called automatically (__init__) and used to intialize object value
#  self - it is refrence variable which hold address of current object ,,object and self are same
class First:
    def __init__(self):
        print("constuctor called")
        print(id(self))
    

obj=First()
print(id(obj))




class student:
    def __init__(self,name,age):
        self.n=name
        self.m=age
# obj = student
# print(obj.n)        
obj = student("say",21)
obj1= student("hii",22)
print(obj.n ,obj.m)        
print(obj1.n ,obj1.m)        