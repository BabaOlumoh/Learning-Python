
my_file = ("/Users/homebase/Desktop/Python/Udemy Course/Dependencies/myfile.txt") #You need to open the file you want by passing the file location
#contents = my_new.read() #You can read the content of the file
#print(contents)
#my_new.seek(0) #You can take the cursor back to the first character to read again
#my_file.readline() #Gives you the output in a list format so you can loop through etc
#my_file.close() #You need to close the file after use or you can do:

with open(my_file) as close_this_file:
    closed_file = close_this_file



#Reading
with open(my_file, mode='r') as f:
    print(f.read())

#You can specify how many characters you want printed
with open(my_file, mode='r') as f:
    print(f.read(5))

#Appending at the end
with open(my_file, mode='a') as f:
    f.write("\nthis is the fourth line")

#print
with open(my_file, mode='r') as f:
    print(f.read())

#Create a new file
with open('new_file.txt', mode='w+') as f:
    f.write("I created a new another file!")


