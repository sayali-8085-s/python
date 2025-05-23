# 1.instance variable - it depend upon object ,when object change it change its value , it is given or written along with self



class student:
    def __init__(self ,name,city):
        self.n =name
        self.m=city    # inside constuctor decleration
        print(self.n,self.m) #access inside constructor
        # print(self.n,self.m,self.p,self.school) #error

    def add(self,phone):
        self.p=phone  # inside instance method declration
        print(self.n,self.m,self.p,self.school) #access inside instance


obj = student("say","rewa")
# print(obj.n,obj.m,obj.p,obj.school) # access outside of class - error

obj.school = "vindhya"    # outside of class decleration
obj.add(222)


print(obj.n,obj.m,obj.p,obj.school) # access outside of class





# 2.class/static - independent to object

class Sudent:
    school = "shhss"  # declaration inside class body

    def __init__(self, name):  # constructor needs a 'name' argument
        self.n = name
        Sudent.school_code = 101  # inside constructor
        print(Sudent.school)

    def addNew(self):
        Sudent.school_city = 'BHopal'  # inside instance method
        print(Sudent.school_city, Sudent.school_code)

    def Display(self):
        print(Sudent.gread)

Sudent.gread = "10th"  # outside of class

obj = Sudent("Unnamed")  # name argument required
obj.addNew()
obj.Display()

obj1 = Sudent('Ayush')
# obj2 = Sudent('Rahul')

print(Sudent.school)
# print(obj1.school)
# print(obj2.school)











# 3.local variable- scope or block dependent



class student:
    def __init__(self,name):
        self.n= name
        grade ='10th'
        print(grade)

    def new(self)  :
        print(grade)  

obj = student("say")   