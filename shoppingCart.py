
names  = ["Nike", "Puma", "Vans", "Adidas", "Mike"]
prices = [999.99, 799.99, 899.99, 1289.99, 299.99]

# The user's cart starts empty
cart_items     = []
cart_quantities = []

while True:
    for i in range(len(names)):
        print(str(i + 1) + ". " + names[i] + " - R" + str(prices[i]))

    print("")
    print("A - Add item")
    print("R - Remove item")
    print("D - Chechout")

    choice = input("Enter choice: ")

    if choice == "A":
        item_choice = int(input("Enter item number to add: "))
        qty = int(input("How many do you want?: "))
        cart_items.append(names[item_choice - 1])
        cart_quantities.append(qty)
        print(names[item_choice - 1] + " x" + str(qty) + " added to cart!")

    elif choice == "R":
        print("Your cart: " + str(cart_items))
        remove_item = input("Enter item name to remove: ")
        if remove_item in cart_items:
            index = cart_items.index(remove_item)
            cart_items.remove(remove_item)
            cart_quantities.pop(index)
            print(remove_item + " removed")
        else:
            print("That item is not in your cart.")

    elif choice == "D":
        total = 0
        print("")
        

        for i in range(len(cart_items)):
            for j in range(len(names)):
                if cart_items[i] == names[j]:
                    item_total = prices[j] * cart_quantities[i]
                    total = total + item_total
                    print(cart_items[i] + " x" + str(cart_quantities[i]) + " = R" + str(item_total))
        print("")
        print("Total: R" + str(total))
        running = False
 
