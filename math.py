from ctypes.wintypes import FLOAT


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


#print (int(firts_num) + int(second_num))


