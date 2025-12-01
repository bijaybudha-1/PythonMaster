# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets $2 discount on Wednesday

user_Age = int(input("Enter your current age: "))
day = "Wednesday"
price = 12 if user_Age >= 18 else 8

if day == "Wednesday":
    price -= 2
print(f"Your Movie Ticket Price is ${price}")
