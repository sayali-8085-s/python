# 1) INHERITANCE - parent child relation - code reusebility


# i) single level

class Parent:
    x=10
    def __init__(self,name):
        self.name=name

    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from parent class")  

class child(Parent):
    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from child class") 
        super().home() # take from parent home


obj = child("saty")
print(obj.x)
print(obj.name)
obj.home()


# ii)multilevel

class gdparent:
    def car(self):
     print("car frm gdparent")
    

class Parent(gdparent):
    x=10
    def __init__(self,name):
        self.name=name

    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from parent class")  

class child(Parent):
    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from child class") 
        super().home() # take from parent home


obj = child("saty")
print(obj.x)

print(obj.name)
obj.home()
obj.car()




# iii)mutiple


class parent1:
    def car(self):
     print("car frm gdparent")
    
    
class Parent2:
    x=10
    def __init__(self,name):
        self.name=name

    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from parent class")  

class child(parent1,Parent2):
    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from child class") 
        super().home() # take from parent home


obj = child("saty")
print(obj.x)
print(obj.name)
obj.home()
obj.car()



# iv)herarichal
   
class parent:
    x=10
    def __init__(self,name):
        self.name=name

    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from parent class")  

class child1(parent):
    def home(self):  #method overiding -two same method in diffent class and betwen them inhertance exixt
        print("home from child class") 
        super().home() # take from parent home

class child2(parent):
    pass
obj = child1("saty")
obj2 = child2('rahul')
print(obj.x)
print(obj2.name)
obj.home()
obj2.home()



# v)  hybrid


class a:
    def first(self):
        print('from a class')

class b:
    
    def first(self):
        print('from b class')

class c(a):
    pass        
class d(b):
    pass

class e(d,c):
    pass
    
obj = e()
obj.first()



# mro -method resolution order to check postion example like e class check d,c