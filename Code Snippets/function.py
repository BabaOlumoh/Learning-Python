def say_hello():
    print("Hello")

def say_hello(name):
    print(f"Hello {name}")

def add_num(num1,num2):  #Just save and break out of the function with output
    return num1+num2

def print_result(a,b): #Gives you output
    print(a+b)

print_result(10,20)

def check_even_list(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers #Return breaks out of the function and will often need to line up with the function name 
        