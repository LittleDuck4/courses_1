import json
from datetime import datetime

phone_book = {}


class MyCustomException(Exception):
    pass


def decor(func):
    def wrap(*args, **kwargs):
        func(*args, **kwargs)
        with open("task2", "a") as f4:
            print(f"function: {func.__name__}, time of call: {datetime.now()}", file=f4)

    return wrap


@decor
def add():
    if number in phone_book.values():
        print("This number already exists")
    else:
        phone_book[name] = number
    with open("json", "w") as f2:
        json.dump(phone_book, f2)


@decor
def delete():
    del phone_book[name]
    print(f"You have deleted the information of the user '{name}'")
    with open("json", "w") as f3:
        json.dump(phone_book, f3)


print("write: \n 'add <name> <number>' to add an entry \n 'delete <name>' to delete the entry by name")

while True:
    # try:
    with open("json") as f1:
        phone_book = json.load(f1)
    # except Exception as e:
    #     with open("task2", "a") as f4:
    #         print(e, file=f4)

    user_actions = input("\n Your input: ").split()
    command, name, number = 0, 0, 0
    for i in range(len(user_actions) + 1):
        if i == 1:
            command = user_actions[0]
        elif i == 2:
            name = user_actions[1]
        elif i == 3:
            number = user_actions[2]

    if command == "add" and name != 0 and name not in phone_book:
        add()

    elif command == "delete" and name in phone_book:
        delete()

    else:
        try:
            zhaba
        except Exception as e:
            with open("task2", "a") as f4:
                print(e, datetime.now(), file=f4)
            raise MyCustomException("Custom exception is occured")
