count=int(input("ok nice for addition enter 1,for subtraction enter 2, for multiplication enter 3 , for division enter 4:"))

if count == 1:
    print("now u  can perform addition:",count)
    num1=int(input("enter ur first number:"))
    num2=int(input("enter ur second number:"))
    a= num1 + num2
    print("your addition of two number is :",a)
elif count==2:
    print("u can perform subtraction:",count)
    num1=int(input("enter ur first number:"))
    num2=int(input("enter ur second number:"))
    b= num1 - num2
    print("your subtraction of two number is :",b)
    
elif count==3:
    print("u can perform multiplication:",count)
    num1=int(input("enter ur first number:"))
    num2=int(input("enter ur second number:"))
    b= num1 * num2
    print("your multiplication of two number is :",b)
    
else :
    count==4
    print("u can perform division:",count)
    num1=int(input("enter ur first number:"))
    num2=int(input("enter ur second number:"))
    b= num1 / num2
    print("your division of two number is :",b)
