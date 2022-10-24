import math

cars = 3;
people = 8;
people_per_car = people/cars 
print(f"There are {people_per_car:.2f} people in each car")
print(f"There are {people_per_car:.1f} people in each car")
print(f"There are {people_per_car:.3f} people in each car")

first = int (input("number of my ice-cream: "))
second = int (input("how many? "))
result = first/second
print(f"how_many_for_instance {result:0f} in my hand")
print("###############################################")



big_number = 13346817564269542565
print(f"The number is: {big_number:,} hereeeee")
print("###############################################")

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area:3f}")
print("###############################################")



weight = 1.62
lower = math.floor(weight)
print(lower)

lower = math.ceil(weight)
print(lower)
