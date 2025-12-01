user_string = input("Enter a any words: ")
reversed_string = ''

for letter in user_string:
    reversed_string = letter + reversed_string

print(f"This '{user_string}' word reversed word is: {reversed_string}")