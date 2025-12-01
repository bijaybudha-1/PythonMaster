# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., < 3km: Walk, 3-15km: Bike, > 15km: Car

distance = 3
if distance < 3:
    transport = "Walk"
elif 3 >= distance < 15:
    transport = "Bike"
else:
    transport = "Car"
print(transport)