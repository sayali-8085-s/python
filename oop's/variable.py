# 1.instance variable - it depend upon object ,when object change it change its value , it is givenor written along with self



class student:
    def __init__(self ,name,city):
        self.n =name
        self.m=city    # inside constuctor decleration

    def add(self,phone):
        self.p=phone  # inside instance method declration


obj = student("say","rewa")
# print(obj.n,obj.m,obj.p,obj.school) # access outside of class - error

obj.school = "vindhya"    # outside of class decleration
obj.add(222)


print(obj.n,obj.m,obj.p,obj.school) # access outside of class


# 2.class/static - independent to object











# 3.local variable- scope or block dependent