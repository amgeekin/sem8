def import_contact():
    phonebook = dict()
    with open("phonebook.txt", "r", encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
            print(*phonebook[i])

def export_contact(new_line):
    with open("phonebook.txt", "a+", encoding='utf-8') as data:
        s = (' '.join(new_line) + '\n')
        data.writelines(s)

def delete_contact():
    phonebook = dict()
    with open("phonebook.txt", "r+", encoding='utf-8') as data:
        s = data.readlines()
        delete_someone = input('Кого вы хотели бы удалить из списка?: ')
        for i in range(len(s)):
            if delete_someone in s[i]:
                continue
            else:
                phonebook[i] = s[i].split()
                print(phonebook[i])
    with open("phonebook.txt", "w", encoding='utf-8') as data:
        for i in phonebook:
            s = (' '.join(phonebook[i]) + '\n')
            data.writelines(s)

def replace_contact():
    phonebook = dict()
    with open("phonebook.txt", "r+", encoding='utf-8') as data:
        s = data.readlines()
        delete_someone = input('Кого вы хотели бы заменить в списке?: ')
        for i in range(len(s)):
            if delete_someone in s[i]:
                continue
            else:
                phonebook[i] = s[i].split()
                print(phonebook[i])
    with open("phonebook.txt", "w", encoding='utf-8') as data:
        for i in phonebook:
            s = (' '.join(phonebook[i]) + '\n')
            data.writelines(s)
    input_contact()


def input_contact():
    new_contact = list()
    new_contact.append(input("surname:"))
    new_contact.append(input("name:"))
    new_contact.append(input("fathers_name:"))
    new_contact.append(input("phone_number:"))
    export_contact(new_contact)

def find_contact():
    str = input("Кого вы хотите найти?: ")
    with open("phonebook.txt", "r", encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            if str in s[i]:
                print(s[i])

def user_interface():
    print('Phonebook\n What you want?\n '
          '1 - Add contact\n '
          '2 - Find contact\n '
          '3 - View all list\n '
          '4 - Delete someone\n '
          '5 - Replace contact\n '
          'any other input - end the programm')
    user_input = input('Your choise: ')
    while user_input == '1' or user_input == '2' or user_input == '3' \
            or user_input == '4' or user_input == '5':
        if user_input == '1':
            input_contact()
        elif user_input == '2':
            find_contact()
        elif user_input == '3':
            import_contact()
        elif user_input == '4':
            delete_contact()
        elif user_input == '5':
            replace_contact()
        user_input = input('Your choise: ')
    print("Buy")


user_interface()