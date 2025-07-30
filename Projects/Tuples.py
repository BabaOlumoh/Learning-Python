#Mini Project: Weekly Activity Logger (Using Tuples)
print("Welcome to your Weekly Activity Logger\n")
print("Add an activity for each day of the week")

monday = input("Monday: ").strip().capitalize()
tuesday = input("Tuesday: ").strip().capitalize()
wednesday = input("Wednesday: ").strip().capitalize()
thursday = input("Thursday: ").strip().capitalize()
friday = input("Friday: ").strip().capitalize()
saturday = input("Saturday: ").strip().capitalize()
sunday = input("Sunday: ").strip().capitalize()

activity_log = (monday, tuesday, wednesday, thursday, friday, saturday, sunday)



print("1. Check Current Weekly Log \n2. Check Recurring Activities \n3. Check Activity Day \n4. Display Activity in Reverse \n5. Show Midweek Activities")
user_input = int(input("Choose option 1-5: "))

if user_input == 1:
    print(activity_log)

elif user_input == 2:
    activity_input =input("Enter activity").strip().capitalize()
    activity_result = activity_log.count(activity_input)
    print(f"You did {activity_input} {activity_result} times")
elif user_input == 3:
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    activity_day_input = input("Enter activity name: ").strip().capitalize()
    if activity_day_input in activity_log:
        stored_input = activity_log.index(activity_day_input)
        print(f"You first did {activity_day_input} first on {days[stored_input]}")
    else: print(f"{activity_day_input} not found")
elif user_input == 4:
    print(activity_log[::-1])
elif user_input == 5:
    print(activity_log[2:5])
else: print("Item not found!")