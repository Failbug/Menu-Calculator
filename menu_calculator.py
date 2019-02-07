''' Created by @Failbug '''

menu = [
    "1. Chicken Strips - $3.50",
    "2. French Fries - $2.50",
    "3. Hamburger - $4.00",
    "4. Hotdog - $3.50",
    "5. Large Drink - $1.75",
    "6. Medium Drink - $1.50",
    "7. Milk Shake - $2.25",
    "8. Salad - $3.75",
    "9. Small Drink - $1.25"
]

cost = [
    3.50,
    2.50,
    4.00,
    3.50,
    1.75,
    1.50,
    2.25,
    3.75,
    1.25
]

total = 0
finished_order = False

print("\nWelcome to my shop. Here is my menu:\n ")
for item in menu: # Prints the menu, one item at a time
    print(item)
print("\nTo select an item, enter a number, 1-9, of the items you want.")

while finished_order == False:

    # Asks user to input selection, quits if nothing is entered    
    selection = input("\nWhat do you want? ")
    if selection == "":
        print("\n\nYou didn't choose anything, please restart the program.\n")
        exit()
    
    # User input is converted from a string to an integer
    selection = [int(i) for i in str(selection)]
    
    # The value of the users selections are added together
    for val in selection:
        total = total + cost[val-1]
    print("\nYour total is now: " + str(total) + "$")
    finish = input("\nDo you want anything else? ")
    
    # If user say no to wanting more, the while loop is set to True
    if finish == "no" or finish == "No" or finish == "NO" or finish == "":
        finished_order = True
    elif finish == "yes" or finish == "Yes" or finish == "YES":
        finished_order = False


print("\nPlease proceed to checkout and pay the total of: " + str(total))
print("\nHave a nice day!")
