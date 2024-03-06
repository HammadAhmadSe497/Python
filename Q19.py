#19. Write a function with the name of fact, which calculate fact of a value that is sent as an argument

def fact(n):

  if n < 0:
    return "factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
    return fact

n = int(input("Enter a non-negative integer: "))  # User input
result = fact(n)
print(result)
