# # n natural even no.
# # n = int(input("Enter a number: "))
# for i in range(2, 2*n + 1,2):
#    if n%2 ==0:
#     if i<2*n:
#      print(i,end=',')
#     else:
#      print(i)
# else:
#   if i<2*n-1:
#    print(i,end=",")
#   else:
#    print(i)
# # n natural odd no.
# # 

# # even natural no.
# # n=int(input("enter a no"))
# for i in range(1,n+1):
#   if i<n:
#     print(2*i,end=',')
#   else:
#    print(2*i)






# for upto n odd natural no.
# n=int(input("enter a no"))
# for i in range(1,n+1,2):
#     if(n%2!=0):
#       if i<n:
#         print(i,end=',')
#       else:
#        print(i)
#     else:
#       if(i<n-1):
#        print(i,end=',')
#       else:
#        print(i)


n     =int(input("enter a no"))
for i in range(1,n+1,2):
    if(n%2!=0):
      if i<n:
        print(i,end=',')
      else:
       print(i)
    else:
      if(i<n-1):
       print(i,end=',')
      else:
       print(i)       