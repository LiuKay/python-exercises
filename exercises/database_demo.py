import shelve


def store_person(db):
    """
    让用户输入数据并将其存储到shelf对象中
    """
    pid = input('Enter unique ID : ')
    person = {'name': input('Enter name:'),
              'age': input('Enter age:'),
              'phone': input('Enter phone number:')}
    db[pid] = person


def lookup_person(db):
    """
    让用户输入ID 和所需字段，并从shelf 对象中获取对应数据
    """
    pid = input("Enter ID:")
    field = input("What do you like to know?(name, age, phone) ")
    field = field.strip().lower()

    try:
        obj = db[pid]
        print(field.capitalize() + ":", obj[field])
    except KeyError:
        print(f"Oops! the ID is not existed:{pid}")


def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')


def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('test.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
