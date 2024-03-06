#                       Q10
# Input five integers from user and display minimum and maximum

num1=eval(input("Enter n 1: "))
num2=eval(input("Enter n 2: "))
num3=eval(input("Enter n 3: "))
num4=eval(input("Enter n 4: "))
num5=eval(input("Enter n 5: "))

#Check Max
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

#Check Min
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