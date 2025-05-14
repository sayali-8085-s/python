while True:
    print('1. Addition \n2. subtraction \n3. divide \n4. off')

    n = int(input("Enter any option: "))
    x = (1, 2, 3, 4)
    if n in x:
        if n == 1:
            p = int(input("Enter first number: "))
            q = int(input("Enter second number: "))
            print(f"addition of {p} + {q} =", p + q)
        elif n == 2:
            p = int(input("Enter first number: "))
            q = int(input("Enter second number: "))
            print(f"subtraction of {p} - {q} =", p - q)
        elif n == 3:
            p = int(input("Enter first number: "))
            q = int(input("Enter second number: "))
            print(f"divide of {p} / {q} =", p / q)
        elif n == 4:
            break
    else:
        print("enter valid option!")