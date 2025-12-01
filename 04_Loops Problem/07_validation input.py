# Validation  Input

while True:
    number = int(input('Enter a number 1 to 10: '))
    if 1 <= number <= 10:
        print('You entered a number:', number)
        break
    else:
        print('Invalid number, please try again.')