# Password Strength Checker
# Problem: Check if a password is "Week", "Medium", or "Strong". Criteria: < 6 chars (Week), 6-10 chars (Medium), > 10 chars (strong)

password = input("Enter your password: ")
password_length = len(password)

if password_length < 6:
    print("Your password is week")
# elif 6 <= password_length < 10:
elif password_length >= 6 and password_length < 10:
    print("Your password is medium")
else:
    print("Your password is Strong")