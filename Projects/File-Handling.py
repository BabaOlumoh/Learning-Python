
stored_entry = (("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/diaryfile.txt"))
myfavourite = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/myfavourite.txt")



print("Welcome to your Daily Diary Logger")
print("1. Write Entry \n2. Read all Recorded Entry \n3. Add your Favourites \n4. Search for Keyword \n5. Show the Last Recorded Entry \n")

menu_input = int(input("Choose between 1-5: ").strip())

if menu_input == 1:
    user_stored_entry = (input("Enter your activities for the day: "))
    with open (stored_entry, 'a') as f:
        f.write(f"{user_stored_entry}\n")
elif menu_input == 2:
    with open(stored_entry, 'r') as f:
        print(f.read())
elif menu_input == 3:
    fav_input = tuple(input("Record your three favourites activities here: "))
    with open(myfavourite, 'a') as f:
        f.write(f"{fav_input}\n")
elif menu_input == 4:
    checker_input = input("Enter keywords: ")
    with open(stored_entry, 'r') as f:
        keyword = f.read()
    if checker_input in keyword :
        print(f"{checker_input} is present in the document provided")
    else: print(f"{checker_input} is not present in the document")
elif menu_input == 5:
    with open(stored_entry, 'r') as f:
        last_entry = list(f.read())
        print(f"Your last entry is {last_entry[::-1]}")
else: print("Invalid input")