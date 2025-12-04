# Function with *args
# Problem: Write a function that takes variable number of arguments and return their sum.

def variable_number (*args):
    # return sum(args)
    add = 0
    for arg in args:
        add += arg
    return add

result1 = variable_number(5, 10)
result2 = variable_number(5, 10, 4, 23, 4, 22, 9)
print(f"The sum number: {result1}")
print(f"The sum number: {result2}")