for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} is FizzBuzz')
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")