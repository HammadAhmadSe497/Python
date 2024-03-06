#                       Q11
# (Body Mass Index Calculator): bmi= weightInKilograms/ (heightInMeters2). User will enter his weight in
# Kilograms and height in meters (1 M=3.23 Feet) and the bmi of the user and display following:
# • Display “You are Underweight” if bmi is less than 18.5
# • Display “You are Normal” if bmi is between 8.5 and 24.9
# • Display “You are Overweight” if bmi is between 25 and 29.9
# • Display “You are Obese” if bmi is greater than 30
# Use And (&&) operator for writing multiple conditions in the if statement


weight = eval(input("Enter you weight in kg: "))
height = eval(input("Enter you height in meters: "))

bmi=weight / (height**2)

if bmi < 18.5:
    print("You are underweight!")

elif bmi >= 18.5 and bmi <= 24.9:
    print("You're normal => ", bmi)

elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight! => ", bmi)

elif bmi > 30:
    print("You are obese. Get some help! => ",bmi)

else:
    print("Invalid input")

