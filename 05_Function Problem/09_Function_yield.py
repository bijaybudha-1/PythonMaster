# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(number):
    for num in range(2, number + 1, 2):
        yield num

for result in even_generator(20):
    print(result)