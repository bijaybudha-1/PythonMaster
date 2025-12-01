age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a Child")
# elif age > 13 and age <= 19:
#     print("You are a Teenager")
# elif age >= 20 and age < 59:
#     print("You are a Adult")
# elif age >= 60:
#     print("You are a Senior")

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 60:
    print("You're a Adult")
else:
    print("You're a Senior")