from ctypes.wintypes import FLOAT
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
print("###############################################")





childs_meal = input ("What is the price of a child's meal?  ");
adults_meal = input ("What is the price of an adult's meal?  ");

many_children = input ("How many children are there?  ");
many_adults = input ("How many adults are there?  ");

tax_rate = input ("What is the sales tax rate?")
childs = (float(childs_meal)) * (float(many_children))
adults = (float(adults_meal)) * (float(many_adults))
subtotal = (float(childs)) + (float(adults));
sales_tax = ((float(subtotal)) * (int(tax_rate)) / 100)
total = sales_tax + subtotal


print ("Subtotal: ", subtotal)
print ("Sales Tax: ", sales_tax)
print ("Total: ", total)

payment  = input ("What is the payment amount?  ");
change = ((int(payment)) - total)
change_2 = round(change, 2)
print("Change: " ,change_2)
print("###############################################")


amount = (int(input ("What is your favorite number? ")))

if amount == "123":
    print("I like you!");
else:
    print ("Get out of here")
print("###############################################")

