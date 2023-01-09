counter = 0
def fibonacci_number(x):
    digit_1, digit_2 = 0, 1
    for i in range(x + 1):
        yield digit_1
        digit_1, digit_2 = digit_2, digit_1 + digit_2


number = int(input("what fibonacci number do you want to know? "))
generator = fibonacci_number(number)

for item in generator:
     if number == counter:
         print("your number is ", item)
     counter += 1