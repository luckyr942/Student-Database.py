student_name = []
student_number = []


def add():
    print('Enter Details')
    name = input('Enter name: ')
    number = int(input('Enter phone number: '))
    student_name.append(name)
    student_number.append(number)


def search_name():
    name_search = input('Enter name: ')
    for i in range(len(student_name)):
        if student_name[i] == name_search:
            print('The number is: ', student_number[i])
        else:
            print('Student does not exist. Try Again')


def search_number():
    number_search = int(input('Enter number:'))
    for i in range(len(student_number)):
        if student_number[i] == number_search:
            print('The name is ', student_name[i])
        else:
            print('Student does not exist. Try Again')


def search():
    print('1. Enter Name')
    print('2. Enter Number')
    choice_search = int(input('Enter choice: '))
    if choice_search == 1:
        search_name()
    elif choice_search == 2:
        search_number()
    else:
        print('Try Again')


def display():
    for i in range(len(student_name)):
        print(student_name[i], '', student_number[i])


def main():
    print('Student Database')
    print('1. Add')
    print('2. Search')
    print('3. Display')
    print('4. Exit')
    choice_main = int(input('Enter choice: '))
    if choice_main == 1:
        add()
        main()
    elif choice_main == 2:
        search()
        main()
    elif choice_main == 3:
        display()
    elif choice_main == 4:
        exit()
    else:
        print('Wrong input. Try Again')
        main()


main()