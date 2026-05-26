rice_price=float(input("please enter the price of the rice : "))
rice_quantity=int(input("please enter the quantity you have taken : "))

milk_price=float(input("please entern the price of the milk : "))
milk_quantity=int(input("please enter the quantity you have taken : "))

chocolate_price=float(input("please entern the price of the chocolate : "))
chocolate_quantity=int(input("please enter the quantity you have taken : "))

rice_total=rice_price*rice_quantity
milk_total=milk_price*milk_quantity
chocolate_total=chocolate_price*chocolate_quantity

total_bill=rice_total+milk_total+chocolate_total

if total_bill > 1000 :
   discount = total_bill * 0.10
   final_bill = total_bill - discount
 
   print("Total Bill:", total_bill)
   print("Discount Applied:", discount)
   print("Final Bill:", final_bill)

else:
   print("Total Bill:", total_bill)
   print("No Discount Applied")


