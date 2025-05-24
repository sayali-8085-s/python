# 1) instance method - self used examp; used in variable





# 2) class method -it upadate the class variavble and add variable ,use cls
class student:
    school ='shs'
    gread ='11th'
    def __init__(self,name):
        self.n=name
    def show_details(self):
        print(self.n)
        print(student.school)
        print(student.gread)

    @classmethod
    def update_grade(cls,update):
        cls.gread=update


obj = student('say')
obj.show_details()

student.update_grade('12th')
obj2 = student('ram')
obj2.show_details()
    

# add new 
class student:
    school ='shs'
    gread ='11th'
    def __init__(self,name):
        self.n=name
    def show_details(self):
        print(self.n)
        print(student.school)
        print(student.city)

    @classmethod  # add new variable
    def add(cls,city):
        cls.city=city


obj = student('say')
# obj.show_details() #error

student.add('rewa')
obj2 = student('ram')
obj2.show_details()
    




 # 3) static mathod -it break the relation from class we have to give value of all variable during calling
 
class student:
    school ='shs'
    gread ='11th'
    def __init__(self,name):
        self.n=name
    def show_details(self):
        print(self.n)
        print(student.school)
        print(student.gread)

    @staticmethod
    def update_grade(cls,update):
        cls.gread=update


obj = student('say')
obj.show_details()

student.update_grade(student,'12th')
obj2 = student('ram')
obj2.show_details()
    



  
class student:
    school ='shs'
    gread ='11th'
    def __init__(self,name):
        self.n=name
    def show_details(self):
        print(self.n)
        print(student.school)

    @staticmethod
    def welcome():
        print('welcome')

    @staticmethod
    def tquhh():
        print('tquhh')
    

student.welcome()
obj = student('say')
obj.show_details()


obj2 = student('ram')
obj2.show_details()
student.tquhh()
       