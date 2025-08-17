def myfunc(word):
    result = ""
    for i, char in enumerate(word):
        if i % 2 == 0:
            result += char.lower()
        elif i % 2 != 0:
            result+= char.upper()
    return result

myfunc("Dearest")