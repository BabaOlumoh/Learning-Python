#Even or Odd Reporter

for numreporter in range(1,51):
    if numreporter % 2 == 0:
        print(f"{numreporter} is even")
    elif numreporter % 2:
        print(f"{numreporter} is odd")

#Vowel or Consonant Checker
user_input1 = input("Enter a word: ").strip()
for letter in user_input1:
    if letter in 'aeiou':
        print(f"{letter.capitalize()} is a vowel")
    else: print(f"{letter.capitalize()} is a consonant")

#Word Length Checker
user_input2 = input("Enter a word: ").split()
for word in user_input2:
    wordlen = len(word)
    if wordlen > 4:
        print(f"{word} has more than 4 letters")
    else: print("None")

#Find the Numbers
for numfinder in range(1,101):
    if numfinder % 2 == 0 and numfinder % 7 == 0:
        print(f"{numfinder} is divisible by 2 and 7")

#Every Other Word
user_input3 = input("Enter a word: ").split()
for otherword, word in enumerate(user_input3):
    if otherword % 2 == 0:
        print(word)
    

#Letter Counter
counter = 0
user_input4 = input("Enter a word: ").strip().lower()
for wordfinder in user_input4:
    if wordfinder == 'a':
        counter+=1
print(counter)


#Sum of Multiples
totalSum = 0
for numMul in range(1,101):
    if numMul % 4 == 0:
        totalSum+=numMul
print(totalSum)



user_input5 = input("Enter a word: ").split()
result = []
for eachword in user_input5:
    if eachword[0].lower() == 'h':
        result.append('😀')
    else:
        result.append(eachword)
print(' '.join(result))
