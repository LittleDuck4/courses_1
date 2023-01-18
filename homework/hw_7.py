phone_book = {
    "Donald": "+28483149",
    "Roy": "+57625262",
    "Tom": "+70981059",
    "Steve": "+62667575",
    "Tony": "+23623423"
}
print("write: \n 'stats' to see the number of entries \n 'add <name> <number>' to add an entry \n 'delete <name>' to delete the entry by name \n 'list' to see a list of all names \n 'show <name>' to see detailed information by name ")
while True:
    print()
    user_actions = input("Your input: ").split()
    command, name, number = 0, 0, 0
    # С помощью цикла появляется возможность использовать команды которые состоят из одного или двух элементов без ошибок
    for i in range(len(user_actions) + 1):
        if i == 1:
            command = user_actions[0]
        elif i == 2:
            name = user_actions[1]
        elif i == 3:
            number = user_actions[2]

    if command == "stats":
        print("number of entries =", len(phone_book))
    elif command == "add" and name != 0 and name not in phone_book:
        flag = True
        for i in phone_book.items():
            if number in i:
                print("This number already exists")
                flag = False
                break
        if flag:
            phone_book[name] = number
    elif command == "delete" and name in phone_book:
        del phone_book[name]
        print(f"You have deleted the information of the user '{name}'")
    elif command == "list":
        print(phone_book.keys())
    elif command == "show" and name in phone_book:
        print(name, phone_book[name])
    else:
        print("Unknown command")
