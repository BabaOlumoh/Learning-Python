
def check_even_list(user_input):
    even_numbers = []
    for num in user_input:
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)
    return even_numbers

check_even_list([1,2,3,4,5,6,7,8])