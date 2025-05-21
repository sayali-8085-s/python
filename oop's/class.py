# bule print or desgin of real world entity or object

class First:
    pass
print(id(First))
obj=First
print(id(obj)) 
obj1=First()   
print(id(obj1))   


# magic variable

class First:
    "hello"
    pass
print(dir(First))
print(First.__doc__)

# consturctor - it is special method in which object called automatically (__init__)
#  self - it is refrence variable which hold address of current object ,,oject and self are same
class First:
    def __init__(self):
        print("constuctor called")
        print(id(self))
    

obj=First()
print(id(obj))


