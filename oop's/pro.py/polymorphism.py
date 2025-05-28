#more then one form of any function is polymorphism examle-len max of string,tuple,list
# dir,super key,method overloading -not support by python we can getit my argument */**

class student:
     def __init__(self):
          
        print('from first')
     def __init__(self):
        print('from second')


obj = student()        #from second we can access bt not frist access never


# in ascending order in conven
l=[10,2,4,6,8,20]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i] ,l[j] = l[j] ,l[i]

print(l)            


# in descending order
l=[10,2,4,6,8,20]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            l[i] ,l[j] = l[j] ,l[i]

print(l) 




l=[10,2,4,6,8,20]


for i in range(len(l)):
    if l[i]