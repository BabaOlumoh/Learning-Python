
#range
range(0,10,2) #start, stop, step side:  +=2
#range is used for generating data rather than saving data to memory

for num in range(1,11):
    print(num)

#Enumerate
word = 'abcde'

for item in enumerate(word):
    print(item)


#Zip
mylist = [1,2,3]
mylist2 = ['a','b','c']

for item1, item2 in zip(mylist,mylist2):
    print(item1)
    print(item2)

#IN

#It's used for checking in a letter or word is in a list, it works like an boolean

xfind = 'x'
results = xfind in ['x', 'y', 'z']
print(results)

#Min
#To get the mininum value in the list

#Max
#To get the maximum value in the list

#Random
#It a built in lib with various functions to generate randoms