#String Manipulation

phrase = input("Enter your secret phrase: ")
def fiveLetters():
    print(f"Your first 5 letters are: {phrase[:5].upper()}")
fiveLetters()

def threeLastLetters():
    print(f"Your last 3 letters are: {phrase[-3:].lower()}")
threeLastLetters()

def secondLetters():
    print(f"Every 2nd letters are {phrase[::2]}")
secondLetters()

def reversedPhrase():
    print(f"Reversed secret phrase is {phrase[::-1]}")
reversedPhrase()

def secretPhrase():
    print(f"Secret code is {phrase[:3]}{phrase[-3:]}")
secretPhrase()

