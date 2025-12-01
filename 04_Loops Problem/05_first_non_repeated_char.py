# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character

user_input = input("Enter a word: ")

for char in user_input:
    if user_input.count(char) == 1:
        print('First non-repeated character is:', char)
        break