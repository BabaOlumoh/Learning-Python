#Warm up for the Milestone project

#My version

def user_choice():
    choice = 'WRONG'
    
    while choice.isdigit() == False or choice not in ['0','1','2']:
        choice = (input("Enter a number between 0-2: "))
        
        if choice.isdigit() == False:
            print("Sorry that's not a digit!")
        elif choice not in ['0','1','2']:
            print("Please enter a digit between 0-2")


#Tutorial version

def user_choice():
    #VARIBLES

    #initial
    choice = 'WRONG'
    acceptance_range = range(0,11)
    within_range = False

    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE == FALSE
    
    while choice.isdigit() == False or within_range == False:
        choice = (input("Enter a number between 0-10: "))

        #DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that's not a digit!")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptance_range:
                within_range = True
            else:
                print("You're out of acceptable range")
                within_range = False