#more then one form of any function is polymorphism examle-len max of string,tuple,list
# dir,super key,method overloading -not support by python we can getit my argument */**

class student:
     def __init__(self):
          
        print('from first')
     def __init__(self):
        print('from second')


obj = student()        #from second we can access bt not frist access never


# in ascending order in convent method
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

# firstt even print then odd print number

l = [1,34,5,67,8]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)   



# farcotr or perfet number