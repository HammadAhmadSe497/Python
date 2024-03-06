#                       Q15
# Write a function which take the radius of circle as first argument and a choice (a or c) as second argument. If second argument is a then return the area of circle. If the second argument is c then return the circumference of circle

def circle(radius, choice):
  
  if choice == 'a':
    return 3.14159 * radius * radius
  
  elif choice == 'c':
    return 2 * 3.14159 * radius
  
  else:
    return "Invalid argument. Type 'a' for area or 'c' for circumference."

#main
radius=eval(input("Enter radius of circle: "))
choice=input("Type 'a' for area or 'c' for circumference: ")

print("Result for given parameters is: ", circle(radius, choice))
