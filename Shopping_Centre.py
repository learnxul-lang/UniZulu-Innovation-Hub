# Logging page

print("\n******************************************LOG-IN PAGE*************************************************************")
# name of shopping app
print("\n---INFINITE-SHOPPING STORE---")
#  Button
print("\n---CLICK HERE--- \n 1 = CREATE YOUR ACCOUNT")
# beginning of tries
Tries = 0
while True: # if the condition is still true, continue looping
    Tries += 1 # tries increases if logining details does not match, until everything match
    choice = int(input("Enter your choice : ")) # 1st choice
    while choice < 1 or choice > 1: # classify the truth set of choice, user must press 1 strictly
        choice = int(input("Invalid, Try again : "))
    if choice == 1:
        name_choice = 'CREATE YOUR ACCOUNT'
        # user creating account
        user_name = input("Set your username : ")
        user_password = input("Set your password : ")
        break

# account created the sign in
print("\n---SIGN-IN---\n ---PLEASE PUT IN YOUR CREDENTIALS---")

count = 0 # counting for user to put the credentials
while True:
    User_name = input("Username : ")
    User_password = input("password : ")
    count += 1 # user logging if not match it continue giving tries
    if user_password == User_password and user_name == User_name: # if they match
        print("---ACCESS GRANTED---")
        break
    else:
        print("INVALID, TRY AGAIN")
#Home page
print("\n**********************************HOME-PAGE****************************************************")
print("---We offer Men's clothes only, place your order now---")
print("\n 1 = Men suit (SET) \n 2 = Casual Clothes (SET) \n 3 = Gyming Cosume (SET)")

# choosing desired sets
Count = 0
while True:
    Count += 1
    option = int(input("what do you want to order : "))
    while option < 1 or option > 3:
        option = int(input("Invalid, try again : "))
        # 1st option
    if option == 1:
        option_name = 'Men suit'
        # list of clothes
        List_men_suit = [
            ['Black suit', 100.0, 10.0],
            ['Formal shoe', 50.0, 4.0],
            ['tie', 40.0, 5.0]
        ]
        # initial total cost
        total_cost = 0.0
        total_delivery_cost = 0.0

        print('---List_men_suit---')
        # executing the list each by each element
        for i, item in enumerate(List_men_suit, start = 1):
            print(f"{i} = {item}") # print the entire list
            print(f"---{i}.{item[0]}: R{item[1]:.2f} (Delivery: R{item[2]:.2f})---") # specifying the delivery and original price
            total_cost += item[1]
            total_delivery_cost += item[2]
        print(f"\n Total Cost: R{total_cost:.2f}") # the total cost in Rands
        print(f"Total Delivery Cost: R{total_delivery_cost:.2f}")
        print(f"Entire Total: R{(total_cost + total_delivery_cost):.2f}")
        break

        #2nd option
    elif option == 2:
        option_name = 'Casual Clothes'
        # list for clothes
        List_Casual_Clothes =[
            ['T-shirt', 70.0, 3.0],
            ['Jean', 500.0, 20.0],
            ['sneaker', 1500.0, 15.0]
        ]
        # initial total
        total_casual_clothes = 0.0
        total_delivery_clothes = 0.0

        print('\n---List for Casual Clothes---\n')
        for i, item in enumerate(List_Casual_Clothes, start = 1):
            #print(f"{i} = {item}")
            print(f"---{i}.{item[0]}: R{item[1]:.2f} (Delivery: R{item[2]:.2f}---")
            total_casual_clothes += item[1]
            total_delivery_clothes += item[2]
        print(f"\nTotal Casual Clothes : R{total_casual_clothes:.2f}")
        print(f"Total Delivery Clothes : R{total_delivery_clothes:.2f}")
        print(f"Entire Total Clothes : R{total_delivery_clothes + total_casual_clothes:.2f}")
        break

        # 3rd option
    elif option == 3:
        option_name = 'Gyming Cosume'

        List_Gyming_Cosume = [
            ["Trek pant", 200.0, 2.0],
            ["Gyming sneaker",300.0, 6.0]
        ]
        total_gyming_cosume = 0.0
        total_delivery_cosume = 0.0

        print("\n---List for available gyming cosumes---")
        for i, item in enumerate(List_Gyming_Cosume, start = 1):
            #print(f"{i} = {item}")
            print(f"---{i}.{item[0]}: R{item[1]:.2f} R{item[2]:.2f}---")
            total_gyming_cosume += item[1]
            total_delivery_cosume += item[2]
        print(f'\nTotal price : R{total_gyming_cosume:.2f}')
        print(f'Total price delivery : R{total_delivery_cosume:.2f}')
        print(f'Entire price : R{total_gyming_cosume + total_delivery_cosume:.2f}')
        break
    print('*************************************************GOOD-BYE******************************************************')














































