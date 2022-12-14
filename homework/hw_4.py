text = input("just write something: ")
if text.isdigit():
    print("you wrote the number, good job!")
    if int(text) % 2 == 0:
        print("this number is even, btw")
    else:
        print("this number is odd, btw")
elif text.isalpha():
    print("you wrote the word, good job!")
    print("the length of your word is:", len(text))
else:
    print("ok, you can write anything, but not this")