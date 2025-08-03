
stored_entry = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/stored_entry.txt")
myfavourite = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/myfavourite.txt")
diary_entry = stored_entry


print("Welcome to your Daily Diary Logger")
print("1. Write Entry \n2. Read all Recorded Entry \n3. Add your Favourites \n4. Search for Keyword \n5. Show the Last Recorded Entry \n")

menu_input = int(input("Choose between 1-5: ").strip())

if menu_input == 1:
    print("Record Activities")
    user_diary_entry = input("Enter your activities for the day: ")
    with open (diary_entry, 'a') as f:
        f.write(f"{user_diary_entry}\n")
elif menu_input == 2:
    with open(diary_entry, 'r') as f:
        print(f.read())
elif menu_input == 3:
    print
elif menu_input == 4:
    print
elif menu_input == 5:
    print

else: print("Invalid input")