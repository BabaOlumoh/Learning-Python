#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
    

#Use range() to print all the even numbers from 0 to 10.