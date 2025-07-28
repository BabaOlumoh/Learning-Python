my_list = ["one", "two", "three"] #list can contain just one data type
print(my_list)
myList = ["one", "2", "3.5"] #list can contain multiple object types
new_list = my_list + myList #list can be concatenated
print(new_list)
print(new_list[0]) #Indexing works with lists just like with strings
print(new_list[1:]) #slicing works with lists just like with strings
print(new_list[:3]) #slicing works with lists just like with strings
new_list[0] = "ONE IN ALL CAPS" #You can change items in a list can reassign it like this
print(new_list)

#Append
new_list.append("four") #You can add a new item by appending it at the end
new_list.append("5")
print(new_list)

#Pop
new_list.pop() #You can pop/remove an item from the list of the list
new_list.pop(-1) #You can pop an item within the list using the item index
print(new_list)


newList = ["a","e","d","c","b"]
numList = [1,2,5,8]

#Sort
newList.sort() 
print(newList) #You don't need to assign the sort method to action it

#Reverse
numList.reverse()
print(numList) #You don't need to assign the reverse method to action it