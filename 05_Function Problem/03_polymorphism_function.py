# Polymorphism in Function
# Problem: Write a function multiply that multiples two numbers, but can also accept and multipy strings.

def multiply(item1, item2):
    return item1 * item2

result1 = multiply(5, 4)
result2 = multiply("Apple", 4)
result3 = multiply(2, "Today")
print(f"The multiplication of two numbers is: {result1}")
print(f"The multiplication of two numbers is: {result2}")
print(f"The multiplication of two numbers is: {result3}")