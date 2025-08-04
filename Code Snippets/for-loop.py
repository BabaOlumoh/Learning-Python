my_iterable = [1,2,3]

for item_name in my_iterable: #For each item_name in my_iterable do print each item_name
    print(item_name)

#For loop for list
my_list = [1,2,3,4,5,6,7,8,9,10]
for item in my_list:
    if item % 2 == 0: #to print even number
        print(item)

list_sum = 0

for num in my_list:
    list_sum = list_sum + num
    print(list_sum)


#For loop for tuples
my_tuple = (10,9,8,7,6,5,4,3,2,1)
for item in my_tuple:
    if item % 2 >= 1:  #to print odd numbers
        print(item)

#Tuples unpacking

my_tuple_list = [(1,2),(3,4),(5,6)]
for a,b in my_tuple_list:
    print(a)
    print(b)

#For loop for tuples
d = {"k1":1, "k2":2, "k3":3}

for item in d.items(): #for whole list
    print(item)

for value in d.values():
    print(value)