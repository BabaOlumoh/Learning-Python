stored_entry = (("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/diaryfile.txt"))
myfav = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/myfav.txt")

print("Welcome to your Daily Diary Logger")
print("1. Check your Weekly Activities \n2. Find Activity Occurence \n3. Add your Favourites \n4. Search for Keyword \n5. Show Most Frequent Activity \n")

menu_input = int(input("Choose between 1-5: ").strip())

if menu_input == 1:
    with open (stored_entry, "r") as f:
        diarylines = f.readlines()
        for lines in diarylines:
            print(f"- {lines.strip()}")
elif menu_input == 2:
    with open (stored_entry, 'r') as f:
        diarylines = f.readlines()
        occurence = tuple(diarylines)
        occurence_input = input("Enter day:activity name(): ").strip()
        print(occurence.count(occurence_input + "\n"))
elif menu_input == 3:

    fav_entry1 = input("Enter your first favourite activity here: ")
    fav_entry2 = input("Enter your second favourite activity here: ")
    fav_entry3 = input("Enter your third favourite activity here: ")
    fav_input = (fav_entry1,fav_entry2,fav_entry3)

    with open(myfav, 'a') as f:
        f.write(f"{fav_input}\n")

    with open(myfav, 'r') as f:
        print(f.read())
elif menu_input == 4:
    keyword = input("Enter keyword here: ").strip()
    with open(stored_entry, 'r') as f:
        content = f.read()
        if keyword in content:
            print(f"{keyword} is in file")
        else: print(f"{keyword} is not in file")
else: print("invalid option")