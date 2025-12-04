# Function with **kwargs
# Problem: Create a function that accepts any number of keyword argument and prints them in the format key: value.

def print_Kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_Kwargs(name = "Bijay", age = 19, address = "Narephat, Jadibutti")