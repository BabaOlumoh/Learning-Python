looper = 0
while looper < 1:
    start_input = input("Enter Y to start app or X to close app: ").lower()
    if start_input == 'y':
        print(looper)
    elif start_input == 'x':
        looper += 1
        print("App Closed")
        break
else:
    print("Invalid input")
