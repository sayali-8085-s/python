while True:
    print("1.Add(+) \n 2.Subst(-) \n 3.Div (/)\n 4.Off")

    n = int(input("enter any option:"))
    x=(1,2,3,4)
    if n in x:
        if n==1:
            p=int(input("enter 1st value"))
            q=int(input("enter 2nd value"))
            print(p+q)
        elif n==2:
                 p=int(input("enter 1st value"))
                 q=int(input("enter 2nd value"))
                 print(p-q)
        elif n==3:
                 p=int(input("enter 1st value"))
                 q=int(input("enter 2nd value"))
                 print(p/q)
        elif n==4:
            break
    else:
          print("plavalue")