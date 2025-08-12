
file = {}

def menu_choice():
    user_menu = int(input("Choose between 1-5: "))
    return user_menu

def user_input():
    get_user_input = input().capitalize().strip()
    return get_user_input


while True:
    print("======== Student Grade Manager ========\n")
    print("1. Add Student \n2. View Students \n3. Search for Student \n4. Remove Student \n5. Exit")
    choice = menu_choice()

    if choice == 1:
        print("Enter student name below:")
        get_student_name = user_input()
        print("Enter student grade below:")
        get_student_grade = user_input()
        file[get_student_name] = get_student_grade
        print(f"The updated database \n{file}")
    elif choice == 5:
        print("Program Closed! \n")
        break
    
    else: print("Invalid Input \n")