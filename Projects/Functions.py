
file = {'Tunde':90, 'Tade':70}

def menu_choice():
    user_menu = int(input("Choose between 1-6: "))
    return user_menu

def user_input():
    global get_user_input
    get_user_input = input().capitalize().strip()
    return get_user_input


while True:
    print("======== Student Grade Manager ========\n")
    print("1. Add Student \n2. View Students \n3. Search for Student \n4. Remove Student \n5. Update Grade \n6. Exit")
    choice = menu_choice()

    if choice == 1:
        print("Enter student name below:")
        get_student_name = user_input()
        print("Enter student grade below:")
        get_student_grade = int(user_input())
        if get_student_grade >= 0 and get_student_grade <= 100:
            file[get_student_name] = get_student_grade
        else: print("The allowed grade input is 0-100")
        print(f"The updated database \n{file}")
    elif choice == 2:
        if file:
            print("\nStudents currently in the datebase.")
            for name, grade in file.items():
                print(f"{name} : {grade}")
        else: print("No Student found!!")
    elif choice == 3:
        print("Enter student name below: ")
        get_search_name = user_input()
        if get_search_name in file:
            print(f"{get_search_name} : {file[get_search_name]}")
        else: print(f"{get_search_name} not found!!")
    elif choice == 4:
        print("Enter student name below: ")
        get_remove_name = user_input()
        if get_remove_name in file:
            file.pop(get_remove_name)
            print(f"{get_remove_name} has been removed")
            print(f"The updated database \n{file}")
        else: print(f"{get_remove_name} not in database")
    elif choice == 5:
        print("Enter student name below: ")
        get_update_name = user_input()
        
        if get_update_name in file:
            print("Enter new grade below: ")
            get_update_grade = int(user_input())
            if get_update_grade >= 0 and get_update_grade  <= 100:
                file[get_update_name] = get_update_grade
            else: print("The allowed grade input is 0-100")
            print(f"The updated database \n{file}")
        else: print(f"{get_update_name} not found in datebase")
    elif choice == 6:
        print("Program Closed! \n")
        break
    
    else: print("Invalid Input \n")