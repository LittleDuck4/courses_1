import time

#task 1

text = input()
for i in text:
    if i.isdigit():
        print(i, "is digit", end=" ")
        if int(i) % 2 == 0:
            print("and it's even")
        else:
            print("and it's odd")
    elif i.isalpha():
        print(i, "is letter", end=" ")
        if i.islower():
            print("and it's in lowercase")
        else:
            print("and it's in uppercase")
    else:
        print(i, "is symbol")

#task 2

while True:
    print("I love Python")
    time.sleep(4.2)
