# collecting info from a user

 fist_name = input("What is you name? ").title()
 country = input("WHat is your Country? ").title()
 city = input("WHat city do you live in? ").title()

 print(f"{fist_name} lives in {city}, {country}.")

#create 2 variable to gather user info

 rent_price = int(input("Rental car price per day: ")) 
 rent_days = int(input("How long do you intent to hire it? ")) 
 total_cost = ( rent_days * rent_price)

 print(f"Total car price is : {total_cost}")

# 3 variable for shopping packages

 bag1 = int(input("Package weight 1? =  "))
 bag2 = int(input("Package weight 2? =  "))
 bag3 = int(input("Package weight 3? =  "))

 total_weight = (bag1+bag2+bag3) * 0.8

 print(f"Shipment total: {total_weight}")

# create user Id
name = input("What is you name? ").title()
age = input("How old are you? ")
id_no = str(786147)

print(f"Welcome {name}. You are {age} years old and your id number is: {id_no}")



