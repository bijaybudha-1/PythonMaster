# Prime Number Checker
# Problem: Chech if number is prime or not

number = int(input("Check a prime number or not: "))
is_prime = True

if number > 1:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
print(f'is prime: {is_prime}')