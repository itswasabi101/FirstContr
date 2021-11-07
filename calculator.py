print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for division")
print("Enter 4 for multiplication")
choice=int(input("Enter your choice :"))

if(choice==1):
    a=int(input("Enter the 1st value :"))
    b=int(input("Enter the second value :"))
    c=a+b
    print("The sum is :",c)
elif(choice==2):
    a=int(input("Enter the value for 1st variable :"))
    b=int(input("Enter the value for 2nd variable :"))
    c=b-a
    print("The difference of two numbers is :",c)
elif(choice==3):
    a = int(input("Enter the value for 1st variable :"))
    b = int(input("Enter the value for 2nd variable :"))
    c=b/a
    print("The quotient is :",c)
elif(choice==4):
    a = int(input("Enter the value for 1st variable :"))
    b = int(input("Enter the value for 2nd variable :"))
    c=a*b
    print("The product of two variables is :",c)
else:
    print("Invalid choice")