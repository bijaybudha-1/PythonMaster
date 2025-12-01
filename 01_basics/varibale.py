# Variable Question
# Qn.1: Declare a variable name and assign it your name as a string.

name = "Bijay"
print(name)

# Qn.2: Create two variables num1 and num2, assign them any numbers, and print their sum.
num1 = 5
num2 = 8
sum = 5 + 8
print(sum)

# Qn.3: Swap the values of two variables x and y without using a third variable.

x = 2
y = 4

x, y, = y, x
print(x, y)

# Qn.4: Assign a value to a variable, then reassign it with a different data type. Print its type before and after.

num_type_1 = 4
print(type(num_type_1))
num_type_1 = "4"
print(type(num_type_1))


# Casting

# Qn.1: Convert the string "100" to an integer and print its type.

casting_number = "100"
print(type(int(casting_number)))

# Qn.2: Convert 25.5 to an integer and a string, then print both values.
casting_number1 = 25.5
print(type(str(casting_number1)))
print(type(int(casting_number1)))

# Qn.3: Convert True to an integer and a string. What do you get?

boolen_value = True
print(int(boolen_value))
print(str(boolen_value))

# Qn.4: Try casting "Hello" to an integer. What happens?

greeting = "Hello"
# print(int(greeting))


# Type Checking
# Qn.1: Use the type() function to check the type of 42, 3.14, and "Python".
print("42", type(42))
print("3.14", type(3.14))
print("Python", type("Python"))

# Qn.2: Assign a boolean value to a variable and check its type.

is_student = True
is_teacher = False
print(type(is_student))
print(is_teacherls)
