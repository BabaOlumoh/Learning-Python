#Use for, .split(), and if to create a Statement that will print out words that start with 's':
str1 = 'Print only the words that start with s in this sentence'
for word in str1.split():
    if word[0] == 's':
        print(word)
    

#Use range() to print all the even numbers from 0 to 10.
for num in range(2,11,2):
    print(num)

#Create a list of all numbers between 1 and 50 that are divisible by 3.
num_list = []
for num in range(1,51):
    if num % 3 == 0:
        num_list.append(num)
print(num_list)


#Go through the string below and if the length of a word is even print "even!"
str2 = 'Print every word in this sentence that has an even number of letters'
for word in str2.split():
    if len(word) % 2 == 0:
        print(word)


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} is FizzBuzz')
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")

#Create a list of the first letters of every word in the string below:
str3 = 'Create a list of the first letters of every word in this string'
newList = []
for worditem in str3.split():
    firstletter = worditem[0]
    newList.append(firstletter)
print(newList)