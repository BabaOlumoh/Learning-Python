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