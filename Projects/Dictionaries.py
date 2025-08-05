
looper = 0

while 

personal_info = {
    "Name": "Mel",
    "Age": "25",
    "Hobby":"Reading"
}

print("\nWelcome to your Personal Info Organizer!\n")
print("1. View Keys \n2. View Values \n3. View Items \n4. Add Info \n5. Remove Info")
print()
user_input = input("Choose an option (1-5): ")
stored_user_input = int(user_input)

if stored_user_input == 1:
    stored_keys = list(personal_info.keys())
    print(f"The current keys in the organizer are: {stored_keys}")
elif stored_user_input == 2:
    stored_values = list(personal_info.values())
    print(f"The current values in the organizer are: {stored_values}")
elif stored_user_input == 3:
    print(f"The items in the organizer are: {personal_info}")
elif stored_user_input == 4:
    user_input_key = input("Enter key name:")
    user_input_value = input("Enter value name:")
    personal_info[user_input_key] = user_input_value
    print(f"New item added successfully \n{personal_info}")
elif stored_user_input == 5:
    print(f"The items in the organizer are: {personal_info}")
    user_input_remove = input("Enter the item key: ").strip()
    stored_user_input_remove = user_input_remove.capitalize()
    if stored_user_input_remove in personal_info:
        personal_info.pop(stored_user_input_remove)
        print(f"Item removed succesfully. \n{personal_info}")
    else: print("\nItem not found!")
else: print("\nInput error!")