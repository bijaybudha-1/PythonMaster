# Factorial Calculator
# Problem: Compute the factorial of number usign a while loop

number = int(input("Enter a factorial number: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial is:", factorial)