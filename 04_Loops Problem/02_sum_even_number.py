# Sum of Even Number
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("Enter a number: "))
sum_even_number = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_even_number += num

print(f"The sum of Even Number: {sum_even_number}")