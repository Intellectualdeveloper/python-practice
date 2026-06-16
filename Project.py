# #Project
# #to make a budget calculater

# Simple Calculator

#this is a simple calculator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b

choice = input("Enter choice ('1' for adding  / '2' for Subtracting  / '3' for  multiplying  / '4' for dividing  ): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", (num1+num2))
elif choice == '2':
    print("Result:", (num1-num2))
elif choice == '3':
    print("Result:", (num1*num2))
elif choice == '4':
    try:
        (num2==0)    
        print("error")
    except:
        (num2!=0)
        print("Result:",num1/num2)
    
else:

    print("Invalid input!")





