#                       Q16
# Modify the two-n calculator problem and solve it using functions for add, sub etc. Return the results from these functions and display them in main.

def add(a,b):
    print("Adition is: ",a+b)

def sub(a,b):
    print("Subtraction is: ",a-b)

def mul(a,b):
    print("Multiplication is: ",a*b)

def div(a,b):
    if b!=0:
        print("Division is: ",a/b)
    else:
        print("Can't divide by 0!")


#main
a=eval(input("Enter num1: "))
b=eval(input("Enter num2: "))

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
