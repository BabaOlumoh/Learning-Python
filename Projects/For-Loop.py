stored_entry = (("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/diaryfile.txt"))
myfav = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/myfav.txt")

print("Welcome to your Daily Diary Logger")
print("1. Check your Weekly Activities \n2. Find Activity Occurance \n3. Add your Favourites \n4. Search for Keyword \n5. Show Most Frequent Activity \n")

menu_input = int(input("Choose between 1-5: ").strip())

if menu_input == 1:
    with open (stored_entry, "r") as f:
        diarylines = f.readlines()
        for lines in diarylines:
            print(f"{lines}")
elif menu_input == 2:
    with open (stored_entry, 'r') as f:
        diarylines = f.readlines()
        occurance = tuple(diarylines)
        #occurance_input = input("Enter activity name: ").strip().capitalize()
        print(occurance.count("Monday: Football\n"))