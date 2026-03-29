import time

products = ["Apples", "Bananas", "0ranges"]
Places_1 = ["Salvador", "Khandisa", "KwaDlangezwa"]
Places_2 = ["Empangeni"]
item = input("Search :")
current_time = time.localtime().tm_hour
day = ""
days = 0

no_of_apples = 0
no_of_bananas = 0

price_apple = 3
price_banana = 2

tot_amount_apples = 0
tot_amount_bananas = 0

address = 0
universal_tariff = 1.1





##################### Iteration function #######################
def restart_error():
    global item
    again_item = input("Try again:")
    item = again_item
    if item == "Apples":
        print(apples())
    elif item == "Bananas":
        print(bananas())


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

    print("Current total is ZAR", tot_amount_apples + tot_amount_bananas)

    check_procedure = input("Do you still wish to add more products (Yes / No)?")

    if check_procedure == "Yes":
        return add_to_cart()

    if check_procedure == "No":
        address = input("Please write street name to address for delivery:")
        print(delivery_time())
        print(time_of_day())
        print("Great! Your checkout price is ZAR",
              tot_amount_apples + tot_amount_bananas,
              "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
              address, "in", days,"days\nThanks and have a good"+ day +"!")
    exit()


###################### END #####################################


############# FUNCTIONS FOR PRODUCTS ############################
def apples():
    global no_of_apples,\
        tot_amount_apples,\
        address, \
        days, \
        day,\
        current_time

    print("Price of 1 apple is R3")

    if item == products[0]:
        no_of_apples = int(input("How many apples?"))
        tot_amount_apples = int(no_of_apples * price_apple * universal_tariff)

        print("Price for", no_of_apples, "apples is ZAR", tot_amount_apples)

        check_procedure_apple = input("Do you wish to add more products (Yes / No)?")

        if check_procedure_apple == "Yes":
            return add_to_cart()

        if check_procedure_apple == "No":
            address = input("Please write street name to address for delivery:")
            print(delivery_time())
            print(time_of_day())
            print("Great! Your checkout price is ZAR",
                  tot_amount_apples + tot_amount_bananas,
                  "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
                  address, "in", days," days\nThanks and have a good"+ day +"!")
    exit()

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


    print("Price of 1 banana is R2")

    if item == products[1]:
        no_of_bananas = int(input("How many bananas?"))
        tot_amount_bananas = int(no_of_bananas * price_banana * universal_tariff)

        print("Price for", no_of_bananas, "bananas is ZAR", tot_amount_bananas)

        check_procedure_banana = input("Do you wish to add more products (Yes / No)?")

        if check_procedure_banana == "Yes":
            return add_to_cart()

        if check_procedure_banana == "No":
            address = input("Please write street name to address for delivery:")
            print(delivery_time())
            print(time_of_day())
            print("Great! Your checkout price is ZAR",
                  tot_amount_apples + tot_amount_bananas,
                  "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
                  address, "in", days ,"days\nThanks and have a good"+ day +"!")
    exit()






#################### MAIN LOOP ##################################
while item in products:
    if item == "Apples":
        print(apples())

    elif item == "Bananas":
        print(bananas())
    elif item not in products:
        print("Invalid Input")
        print(restart_error())

