import time

products = ["Apples", "Bananas"]
cart = []
Places_1 = ["Salvador", "Khandisa", "KwaDlangezwa"]
Places_2 = ["Empangeni"]
current_time = time.localtime().tm_hour
day = ""
item = ""
days = 0
number = 0
no_of_apples = 0
no_of_bananas = 0
price_apple = 3
price_banana = 2
tot_amount_apples = 0
tot_amount_bananas = 0
address = 0
universal_tariff = 1.1
username_lyst = []
password_lyst = []
Alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Beta = list("abcdefghijklmnopqrstuvwxys")
special_char = list("!@#$%^&*")
digits = list("123456789")

username = "Johnson"
password = "John@011"
defined_username = []
defined_password = []

#############################        CREATE USER ACCOUNT       ##################################################
"""
User Account:
1. Username:
    1.1 must begin with capital letters
2. Password:
    2.1 Minimum length must be 6 characters 
    2.2 Maximum length must be 16 characters
    2.3 Must have at least one special characters(!@#$%^&*())
    2.4 Must have at least one digit(1234567890)
    2.5 Must have at least one upper case and one lower case characters
"""

print(" "*57, "PICKALOT")
print(" "*40,"Welcome to Pickalot, where you find and pick all you need!")

def check_account_exist():
    global day

    account_check = input(f" {" "*20}Do you have an existing Account?\n Either enter 'Yes or No':")
    if account_check.upper() == "YES":
            open_account()
    elif account_check.upper() == "NO":
            create_account()
    while account_check.upper() != "YES" or account_check.upper() != "NO":
        print(f" {" "*20}Invalid characters. Please try again!")
        print(check_account_exist())
        break

def create_account():
    global day
    consent_check = input(f"Do you wish to open one?\n Either enter 'Yes or No':")

    if consent_check.upper() == "YES":
        create_username()
    elif consent_check.upper() == "NO":
        time_of_day()
        print(f" {" " * 40}Thank you and gave a good {day}")
        exit()
    while consent_check.upper() != "YES" or consent_check.upper() != "NO":
        print(f" {" "*20}Invalid characters. Please try again!")
        print(create_account())
        break

def create_username():
    global username_lyst, username
    print(f" {1}. Username must begin with Capital letter! \n {2}. Must have minimum 6 characters")
    username = input("Create username: ")

    username_lyst.append(username)
    username_lyst = list(username)

    if any(x in username_lyst for x in Alpha) and username_lyst == list(username) and len(username_lyst) >= 6:
        print(f"Hi {username.upper()}, lets create password ")
        create_password()
    elif any(x  not in username_lyst for x in Alpha) and len(username) >= 6 and username_lyst == list(username):
        print(f"Username does not have a capital letter!\nTry again.")
        create_username()
    elif any(x in username_lyst for x in Alpha) and len(username) < 6 and username_lyst == list(username):
        print(f"Username has {len(username)} chacacters and must have a minimum of 6 characters\nTry again.")
        create_username()
    elif any(x not in username_lyst for x in Alpha) and len(username) < 6 and username_lyst == list(username):
        print(f"Username has no Capital letter!\nUsername has {len(username)} chacacters and must have minimum 6 characters\nTry again.")
        create_username()
    else:
        print("Error input")
        create_username()

def create_password():
    global password, password_lyst
    print(f"{1}. Must have minimum 8 characters\n{2}. Must have one special character(!@#$%^&*)\n{3}.Must have one digit(1234567890)\n{4}. Must have one upper case letter\n{5}. Must have one lower case letter.")
    password = input(f"Create password: ")

    password_lyst.append(password)
    password_lyst = list(password)
    while True:
            if any(n in password_lyst for n in Alpha) and any(a in password_lyst for a in special_char) and any(b in password_lyst for b in digits) and any(c in password_lyst for c in Beta ) and len(password) >= 8:
                print(f"{" "*20}Password created successfully!\n{" "*20}Sign in")
                open_account()
            elif any(a in password_lyst for a in special_char) and any(b in password_lyst for b in digits) and any(c in password_lyst for c in Beta) and any(n  not in password_lyst for n  in Alpha) and len(password) >= 8:
                print(f"{" "*20}Password has no Upper case character. Please try again!")
                print(" ")
                create_password()
            elif any(a not in password_lyst for a in special_char) and any(b in password_lyst for b in digits) and any(c in password_lyst for c in Beta) and any(n  in password_lyst for n  in Alpha) and len(password) >= 8:
                print(f"{" "*20}Password has no Special character. Please try again!")
                print(f" ")
                create_password()
            elif any(a in password_lyst for a in special_char) and any(b not in password_lyst for b in digits) and any(c in password_lyst for c in Beta) and any(n in password_lyst for n  in Alpha) and len(password) >= 8:
                print(f"{" "*20}Password has no digit character. Please try again!")
                print(f" ")
                create_password()
            elif any(a in password_lyst for a in special_char) and any(b in password_lyst for b in digits) and any(c not in password_lyst for c in Beta) and any(n in password_lyst for n  in Alpha) and len(password) >= 8:
                print(f"{" "*20}Password has no lower case character. Please try again!")
                print(f" ")
                create_password()
            elif any(a in password_lyst for a in special_char) and any(b in password_lyst for b in digits) and any(c not in password_lyst for c in Beta) and any(n in password_lyst for n  in Alpha) and len(password) < 8:
                print(f"Password lenghth is less tha 8. Please try again!")
                print(f" ")
                create_password()
            elif any(a not in password_lyst for a in special_char) or any(b not in password_lyst for b in digits) or any(c not in password_lyst for c in Beta) or any(n in password_lyst for n  in Alpha) or len(password) < 8:
                print("Password has missing characters or length of password below 8!")
                create_password()
            break
def open_account():
    global defined_username, defined_password, password_lyst, username_lyst, item , products, cart

    print(" " * 50, "PICKALOT PTY")

    open_username = input(f"Provide username: ")
    open_password = input(f"Enter Password: ")

    defined_username.append(open_username)
    defined_password.append(open_password)

    open_username_lyst = list(open_username)
    open_password_lyst = list(open_password)

    if ((open_username_lyst == username_lyst) and (open_password_lyst == password_lyst)) or ((open_username == username) and (open_password == password)):
        search_engine()
    elif ((open_username_lyst != username_lyst) and (open_password_lyst == password_lyst)) or ((open_username != username) and (open_password == password)):
        print("Incorrect Username!")
        open_account()
    elif ((open_username_lyst == username_lyst) and (open_password_lyst != password_lyst)) or ((open_username == username) and (open_password != password)):
        print("Incorrect Password:")
        open_account()
    while ((open_username_lyst != username_lyst) and (open_password_lyst != password_lyst)) or ((open_username != username) and (open_password != password)):
        print("Invalid input!")
        open_account()


##################################       END USER ACCOUNT FUNCTIONS  ###################################################

##################################   SEARCH ENGINE     #################################################################
def search_engine():
     global item, Alpha, Beta, products, number
     print(" " * 50, "PICKALOT PTY")
     item = input(f"Search any item: ")
     search_lyst = list(item)
     search_product1 = list(products[0])
     search_products2 = list(products[1])
     cart.append(item)
     print(cart)
     if any(i in search_lyst for i in search_product1 ):
         print(f"{" "*10}Search results:\n1. {products[0]}\n2. {products[1]}\nChoose one product")
         number = int(input("Enter choice:"))
         if any(i in cart for i in products):
            if number == 1:
                print(apples())
            elif number == 2:
                print(bananas())
         elif any(i not in cart for i in products):
            search_engine()
     elif any(i not in search_lyst for i in search_product1 ) and any(j not in search_lyst for j in search_products2) :
         print(f"{" "*10}Search results: No result")
         search_engine()


 ##################################   END OF SEARCH ENGINE    #########################################################


#########################################    ITERATION FUNCTIONS ####################################################

def add_to_cart():
    global no_of_apples, no_of_bananas
    global tot_amount_apples, tot_amount_bananas
    global address
    global days
    global current_time
    global day

    another_item = input("Search again:")

    if another_item == "Apples":
        print("Price of 1 apple is R3")
        add_no_of_apples = int(input("How many apples?"))
        no_of_apples += add_no_of_apples
        tot_amount_apples = int(no_of_apples * price_apple * universal_tariff)
    elif another_item == "Bananas":
        print("Price of 1 banana is R2")
        add_no_of_bananas = int(input("How many bananas?"))
        no_of_bananas += add_no_of_bananas
        tot_amount_bananas = int(no_of_bananas * price_banana * universal_tariff)
    elif another_item not in products:
        print("Product not found! Please re-enter item")
        add_to_cart()

    print("Current total is ZAR", tot_amount_apples + tot_amount_bananas)

    check_procedure = input("Do you still wish to add more products (Yes / No)?")

    if check_procedure == "Yes":
     add_to_cart()

    if check_procedure == "No":
        address = input("Please write street name to address for delivery:")
        print(delivery_time())
        print(time_of_day())
        print("Great! Your checkout price is ZAR",
              tot_amount_apples + tot_amount_bananas,
              "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
              address, "in", days,"days\nThanks and have a good"+ day +"!")
    exit()


#####################################      END  OF ITERATION FUNCTIONS   ###############################################

################################        FUNCTIONS FOR PRODUCTS       ###################################################
def apples():
    global no_of_apples,\
        tot_amount_apples,\
        address, \
        days, \
        day,\
        current_time, \
        item, cart
    print(" " * 57, "PICKALOT")
    print("Price of 1 apple is R3")
    if item == "Apples":
        no_of_apples = int(input("How many apples?"))
        tot_amount_apples = int(no_of_apples * price_apple * universal_tariff)

        print("Price for", no_of_apples, "apples is ZAR", tot_amount_apples)


        check_procedure_apple = input("Do you wish to add more products (Yes / No)?")
        if check_procedure_apple.upper() == "YES":
            print(add_to_cart())

        elif check_procedure_apple.upper() == "NO":
                    address = input("Please write street name to address for delivery:")
                    delivery_time()
                    time_of_day()
                    print("Great! Your checkout price is ZAR",
                    tot_amount_apples + tot_amount_bananas,
                    "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",address, "in", days," days\nThanks and have a good"+ day +"!")
                    exit()
        while check_procedure_apple.upper() != "YES" or check_procedure_apple.upper() != "NO":
            print(f" {" "*20}Invalid input. Please try again!")
            print(apples())
            break


def delivery_time():
    global days
    if address in Places_1:
        days = 1
    if address in Places_2:
        days = 2

def time_of_day():
    global day
    if 5 <= current_time < 12:
        day = "morning"
    elif 12 <= current_time < 18:
        day = "day"
    else:
        day = "night"

def bananas():
    global no_of_bananas
    global  tot_amount_bananas
    global address
    global days
    global current_time
    global day
    global item

    print(" " * 57, "PICKALOT")
    print("Price of 1 banana is R2")
    if item == products[1]:
        no_of_bananas = int(input("How many bananas?"))
        tot_amount_bananas = int(no_of_bananas * price_banana * universal_tariff)
        print("Price for", no_of_bananas, "bananas is ZAR", tot_amount_bananas)

        check_procedure_banana = input("Do you wish to add more products (Yes / No)?")
        if check_procedure_banana == "Yes":
         add_to_cart()
        elif check_procedure_banana == "No":
            address = input("Please write street name to address for delivery:")
            delivery_time()
            time_of_day()
            print("Great! Your checkout price is ZAR",
                  tot_amount_apples + tot_amount_bananas,
                  "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
                  address, "in", days ,"days\nThanks and have a good"+ day +"!")
        while check_procedure_banana.upper() != "YES" or check_procedure_banana.upper() != "NO":
            print(f" {" "*20}Invalid input. Please try again!")
            print(bananas())
            break

#############################    END OF PRODUCT DUNCTIONS  #############################################################


################################  LOOP FOR DETERMINING ACCESS TO PRODUCTS #############################################

while item in products:
    if item == "Apples":
        print(apples())
    elif item == "Bananas":
        print(bananas())
    elif any(a not in cart for a in products):
        print("Entered peoduct unavailable, Please try again")


##########################################     END OF LOOP            #################################################

check_account_exist() # To start program
