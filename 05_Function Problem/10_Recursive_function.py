# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def recursive_factorial(number):
    if number == 0:
        return 1
    else:
        return number * recursive_factorial(number - 1)

    # factorial = 1
    # while number > 0:
    #     factorial *= number
    #     number -= 1
    #     return factorial
print(recursive_factorial(5))