#Mini Project: Weekly Activity Logger (Using Tuples)

activity_log = ("Football", "Basketball", "Vollyball", "Golf", "Swimming", "Tennis", "Football")
print("Welcome to your Weekly Activity Logger\n")
print("1. Check Current Weekly Log \n2. Add to Activity Log \n3. Check Recurring Activities \n4. Check Activity Day \n5. Display Activity in Reverse \n6. Show Midweek Activities")
user_input = int(input("Choose option 1-6: "))

if user_input == 1:
    print(activity_log)
elif user_input == 2:
    print("Add an activity for each day of the week")
    daily_log = input("")
elif user_input == 3:
    activity_input =input("Enter activity").strip().capitalize
    activity_result = activity_log.count(activity_input)
    print(f"You did {activity_input} {activity_result} times")
elif user_input == 4:
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    activity_day_input = input("Enter activity name: ").strip().capitalize()
    stored_input = activity_log.index(activity_day_input)
    if activity_day_input in activity_log:
        print(f"You first did {activity_day_input} first on {days[stored_input]}")
    else: print(f"{activity_day_input} not found")
elif user_input == 5:
    print(activity_log[::-1])
elif user_input == 6:
    print(activity_log[2:5])
else: print("Item not found!")