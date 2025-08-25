def user_choice():
    choice = "Wrong"
    acceptance_range = range(0,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number(0-10): ")
        
        if choice.isdigit() == False:
            print("Please enter a digit")
            
        if choice.isdigit() == True:
            if int(choice) in acceptance_range:
                within_range = True
            else:
                print("Please enter a digit between (0-10)")
                within_range = False
        
    return int(choice)

user_choice()