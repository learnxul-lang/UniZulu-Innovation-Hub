import random                             # At some point i will use the random shuffling function to randomly arrange elements of a collection (list)

print("""                                    
""")                                                     #Well we needed space before the headline and hence we created the space

welcome_string = " Welcome to Shoppy-Shoppy "               #This variable's value will serve as a title head for the program
select_option = "Select our lovely products below"
spaces = " " * 12                                           # I coded 12 "empty" spaces that i will need dont worry you will see their purpose
item = "Item              "                                 
prices = "Prices"                                            
coloumn_table = "|"

set_up = f"{item}{spaces}{prices}"

print(welcome_string.center(34, "*") )
print("-"* 34)
print(select_option.ljust(42, " "))
print("." * len(select_option))
print("")

print(set_up)
print("-" * 37)
print(f"""Premio 3XD HeadSet {spaces}{coloumn_table}R289
Samsung EarPods 2s{spaces} {coloumn_table}R345
Samsung Galaxy A05{spaces} {coloumn_table}R2300
Samsung Galaxy A16s{spaces}{coloumn_table}R3200
Hauwei Y16{spaces}         {coloumn_table}R4300
Hisense M19{spaces}        {coloumn_table}R3900
Mobicel EGO{spaces}        {coloumn_table}R1300
""")

my_cart = []
products = ['Premio 3XD HeadSet', 'Samsung EarPods 2s', 
            'Samsung Galaxy A05', 'Samsung Galaxy A16s', 'Hauwei Y16', 'Hisense M19','Mobicel EGO' ]

random.shuffle(products)


for product in products:
   
   print(f"\nProduct available: {product}")

   prompt = input("Do you want this product: ")

   if prompt.lower() == "Yes".lower():
      my_cart.append(product)
      
   elif prompt.lower() == "skip".lower():
      continue
   
   elif prompt.lower() == "No".lower():
      continue
   else:
      print("INVALID CHOICE")

    
    

if my_cart != []:
    print("-" * 42)
    print("Your Cart has the following items")
    print("." * 42)

for j in my_cart:
   
    print(j)


price = 0
for product in my_cart:
   if product == "Premio 3XD HeadSet":
      price = price + 289
   if product == "Samsung EarPods 2s":
      price = price + 345
   if product == "Samsung Galaxy A05":
      price = price + 2300
   if product == 'Samsung Galaxy A16s':
      price = price + 3200
   if product == 'Hauwei Y16':
      price = price + 4300
   if product == 'Hisense M19':
      price = price + 3900
   if product == 'Mobicel EGO':
      price = price + 1300

print("-"*42)

print(f"The cost of your items is R {price}")
print(" ")

number_of_items = len(my_cart)

if number_of_items < 3:
   delivery_fee = 150
elif number_of_items >= 3:
   delivery_fee = 200

totalCost = delivery_fee + price

print(f"The delivery fees are: {delivery_fee}")
print("")
print(f"The total cost to be paid is: R {totalCost}")


