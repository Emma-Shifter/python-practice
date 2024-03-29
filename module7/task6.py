contacts = {}

def addContact() -> bool:
    name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
    contact = (name, surname)
    if (contact in contacts): return False
    else:
        phoneNumber = input("Введите номер телефона: ")
        contacts[contact] = phoneNumber
        return True

def findContact() -> list:
    find_contacts = []
    surname = input("Введите фамилию для поиска: ")
    for contact in contacts.keys():
        if (surname in contact): find_contacts.append(f"{' '.join(contact)} {contacts[contact]}")
    return find_contacts

while True:
    do = input("Введите номер действия:\n1. Добавить контакт.\n2. Найти человека.\nДействие: ")
    match do:
        case "1":
            if not addContact():
                print("Такой человек уже есть в контактах.")
            print(f"Текущий словарь контактов: {contacts}")
        case "2":
            print("\n".join(findContact()))
    print()