#                       Q14
# Write a function, which takes 5 arguments and print the largest and smallest

def max(num1=10,num2=20,num3=30,num4=40,num5=50):
    if num1>num2 and num1>num3 and num1>num4 and num1>num5:
        print("\nnum1 is max!")
    
    elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
        print("\nnum2 is max!")
    
    elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
        print("\nnum3 is max!")
    
    elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
        print("\nnum4 is max!")
    
    else:
        print("\nnum5 is max!")

def min(num1=10,num2=20,num3=30,num4=40,num5=50):
    if num1<num2 and num1<num3 and num1<num4 and num1<num5:
        print("\nnum1 is min!")
    
    elif num2<num1 and num2<num3 and num2<num4 and num2<num5:
        print("\nnum2 is min!")
    
    elif num3<num1 and num3<num2 and num3<num4 and num3<num5:
        print("\nnum3 is min!")
    
    elif num4<num1 and num4<num2 and num4<num3 and num4<num5:
        print("\nnum4 is min!")
    
    else:
        print("\nnum5 is min!")


#main
print("\n\nIf num1=10, num2=20, num3=30, num4=40, num5=50")
max()
min()
