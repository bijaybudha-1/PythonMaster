# Pet Food Recommendation
# Problem: Recommendation a type of pet food based on the pet's species and age (e.g., Dog: < 2 years - Puppy Food, Cat: >5 years - Senior cat food).

species = input("Enter the species name [Dog, Cat]: ").lower()
years = int(input("Enter the number of years: "))
if species == "dog" and years < 2:
    food_type = "Puppy Food"
elif species == "cat" and years > 5:
    food_type = "Senior Cat Food"
else:
    print("Something went wrong")

print(food_type)