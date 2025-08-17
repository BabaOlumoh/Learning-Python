def myfunc(*args):
    even_numbers = []
    for item in args:
        if item % 2 == 0:
            even_numbers.append(item)
    return even_numbers