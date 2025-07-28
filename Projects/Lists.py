list_menu = ["pizza", "movies", "coding", "music", "football"]

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
    print("item added successfully")
elif stored_input == 3:
    print("Remove an item from the list below")
    print(list_menu)
    user_input_remove = input()
    stored_user_input_remove = int(user_input_remove)
    list_menu.pop(stored_user_input_remove)
    print("item removed successfully")
elif stored_input == 4:
    list_menu.sort()
    print(f"List sorted alphabetically\n{list_menu}")
elif stored_input == 5:
    list_menu.reverse()
    print(f"List shown in descending order\n{list_menu}")
elif stored_input == 6:
    print(list_menu[:3])
else:
    print("Please enter a valid response")

