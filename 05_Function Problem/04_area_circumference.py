# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

def area_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return  round(area, 2), round(circumference, 2)

result1, result2 = area_circle(3)
print("The area of circle is", result1, "\nThe circumference of circle is", result2)