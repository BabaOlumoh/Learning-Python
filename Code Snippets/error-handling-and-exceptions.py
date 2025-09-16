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