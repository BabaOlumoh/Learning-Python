def ask_for_it():
    while True: #loop so that the block can restart
        try: #try this block to see if any errors
            result = int(input("Please provide a number: "))
        except: #If there's an error, do this
            print(("Whoops! That is not a number"))
            continue #continue 
        else: #if there's no error, continue with this block of code
            print("Correct, thank you")
            break
        finally: #this block will always run regardless if there's error or not
            print("This block will always run")

ask_for_it()

for i in ['a','b',3]:
    try:
        print(i**2)
    except: 
        print("This is invalid \n Try again!")
        continue
    else: 
        print("Correct")
        break

x = 5
y = 0
try: 
    z = x/y
except ZeroDivisionError: 
    print("Can't be divided by zero")
finally: 
    print("All Done")

def ask():
    while True:
        try:
            sq = int(input("Input an integer: "))
            sq*=sq
        except: 
            print("An error occurred! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is:  {sq}")
            break

ask()