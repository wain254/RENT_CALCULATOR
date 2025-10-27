#TOTAL RENT
#TOTAL FOOD ORDER AMOUNT
#ELECTRICITY UNITS SPENT
#NUMBER OF PERSONS SHARING THE ROOM

rent_charges = float(input("Enter the total rent amount: ")) #float used to include decimal values
food_charges = float(input("Enter the total food order amount: "))     
electricity_units = float(input("Enter the total electricity units spent: "))
unit_per_charge = float(input("Enter the rate per unit of electricity: "))
num_persons = int(input("Enter the number of persons sharing the room: ")) #int used as number of persons cannot be in decimal
# electricity_rate_per_unit = 7.5 #fixed rate per unit of electricity

#calculate electericity charges
# electricity_charges = electricity_units * electricity_rate_per_unit
total_bill = electricity_units *unit_per_charge 

#calculate total full bill and individual share
total_full_bill = rent_charges + food_charges + total_bill

#INDIVIDUAL SHARE CALCULATION
individual_share = total_full_bill / num_persons

print(f"\n total electricity charges: ${total_bill:.2f}")    # prints total electricity charges with 2 decimal places


print(f"\n Total full bill amount: ${total_full_bill:.2f}")  # prints total full bill amount with 2 decimal places


print(f"\n Each person has to pay: ${individual_share:.2f}")  # prints individual share with 2 decimal places