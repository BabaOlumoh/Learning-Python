prices_lookup = {"apple":2.99, "oranges": 1.99, "milk":5.80}
prices_lookup["apple"]
d = {"k1":123, "k2": [0,1,2], "k3":{"insideKey":100}, "k4":"fifty"} #Dictionary is really flexible and you can different object types in it.
d['k2']
d["k3"]["insideKey"] #You can stack key calls to get the value in a dictionary
d["k2"][2] #You can stack index calls to get value in a list
#To expand the above
dict_list = {"key1":["a","b","c"]}
print(dict_list)
my_list = dict_list["key1"]
print(my_list)
letter = my_list[-1]
print(letter)
letter.upper()
#Or in one line
dict_list["key1"][-1].upper()
#Append
d["k5"] = 99.9 #you can add new key pair 
print(d)
#Reassign
d["k1"] = "One" #You can change a key pair by reassigning it
#Methods
d.keys() #To print only keys in a dictionary
d.values() #To print only values in a dictionary
d.items() #To print all items in a dictionary