list_menu = []

print("Welcome to your List \n")

print("1. View Menu \n2. Add Item to Menu \n3. Remove an Item \n4. Sort the List \n5. Reverse the List \n6. Show your Top Three \n")
user_input = input("Enter the appropriate number from the list above: ")
stored_input = int(user_input)


if stored_input == 1:
    print(list_menu)
elif stored_input == 2:
    print("Add a new item to the list")
    user_input_add = input()
    list_menu.append(user_input_add)
    print("item added")
elif stored_input == 3:
    print("Remove an item from the list below")
    print(list_menu)
    user_input_remove = input()
    list_menu.pop()
    print("item removed successfully")


else:
    print("Please enter a valid response")

