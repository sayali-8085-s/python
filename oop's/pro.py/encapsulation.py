# public  - access every where
class p:
    x=10
    def show(self):
        print('from p class')

class c(p):
    pass
obj =c()
print(obj.x)
print(obj.show())


# protected variable/method - access it in parent class as well as child -python not supported
class p:
    _x=10
    def _show(self):
        print('from p class')

class c(p):
    pass
obj =c()
print(obj._x)
print(obj._show())


# private - it is only acceses in parent calss not child class

class p:
    __x=10
    def __show(self):
        print('from p class')

class c(p):
    print(p.__x)
obj =c()
# print(obj.__x)
# print(obj.__show())


class p:
    __x=10
    def __show(self):
        print('from p class')

class c(p):
    pass


# print(dir(c))

obj = c()
print(obj._p__show())