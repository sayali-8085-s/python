from abc import ABC,abstractmethod
class senior(ABC):
    def add(self,x,y):
        print(x+y)
    def sub(self,x,y):
        print(x-y)    
    def mul(self,x,y) :
        print(x*y)  
    @abstractmethod
    def div(self)    :
        pass 
class junior(senior) :
    def div(self,x,y) : #same method name as in senior class
        print(x/y)  

obj = junior()   
obj.mul(2,4)    